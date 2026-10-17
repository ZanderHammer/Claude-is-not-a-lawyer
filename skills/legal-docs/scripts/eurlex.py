#!/usr/bin/env python3
"""Fetch EU law from the Publications Office (Cellar) instead of eur-lex.europa.eu.

EUR-Lex answers automated clients with a JavaScript bot challenge, so web-fetch
tools often get an empty page. The same official texts are served by the EU
Publications Office repository ("Cellar"), which this script queries.

Usage:
    python3 eurlex.py 32016R0679 --article 13          # GDPR Art. 13, English
    python3 eurlex.py 32011L0083 --latest --article 11a # newest consolidated CRD, Art. 11a
    python3 eurlex.py 32016R0679 --lang de --article 13 # German text
    python3 eurlex.py 32011L0083 --latest --url         # print fetchable URLs only
    python3 eurlex.py 32019L0770 --out dcd.txt          # whole act as plain text

CELEX numbers: 3YYYYRNNNN regulation, 3YYYYLNNNN directive, 3YYYYDNNNN decision.
Consolidated versions: 0YYYYXNNNN-YYYYMMDD (use --latest to find the newest).

Standard library only.
"""

import argparse
import html
import json
import re
import sys
import urllib.parse
import urllib.request

RESOURCE = "https://publications.europa.eu/resource/celex/{celex}"
SPARQL = "https://publications.europa.eu/webapi/rdf/sparql"
LANGS = {
    "bg": "bul", "cs": "ces", "da": "dan", "de": "deu", "el": "ell", "en": "eng", "es": "spa",
    "et": "est", "fi": "fin", "fr": "fra", "ga": "gle", "hr": "hrv", "hu": "hun", "it": "ita",
    "lt": "lit", "lv": "lav", "mt": "mlt", "nl": "nld", "pl": "pol", "pt": "por", "ro": "ron",
    "sk": "slk", "sl": "slv", "sv": "swe",
}
ARTICLE_WORD = {
    "en": "Article", "de": "Artikel", "fr": "Article", "it": "Articolo", "es": "Artículo",
    "nl": "Artikel", "pt": "Artigo", "pl": "Artykuł", "sv": "Artikel", "da": "Artikel",
}
LATEST_QUERY = """PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
SELECT ?celex ?date WHERE {{
  ?act cdm:resource_legal_id_celex "{celex}"^^<http://www.w3.org/2001/XMLSchema#string> .
  ?c cdm:act_consolidated_consolidates_resource_legal ?act .
  ?c cdm:resource_legal_id_celex ?celex .
  OPTIONAL {{ ?c cdm:act_consolidated_date ?date }}
  FILTER (STRSTARTS(STR(?celex), "0{base}-"))
}} ORDER BY DESC(?celex) LIMIT 1"""
HEADING_CLASSES = ("oj-ti-art", "title-article-norm", "ti-art")


def latest_consolidated(celex: str) -> str | None:
    data = urllib.parse.urlencode({"query": LATEST_QUERY.format(celex=celex, base=celex[1:])}).encode()
    request = urllib.request.Request(SPARQL, data=data, headers={"Accept": "application/sparql-results+json"})
    with urllib.request.urlopen(request, timeout=60) as response:
        rows = json.load(response)["results"]["bindings"]
    return rows[0]["celex"]["value"] if rows else None


def fetch(celex: str, lang: str) -> tuple[str, str]:
    request = urllib.request.Request(
        RESOURCE.format(celex=celex),
        headers={"Accept": "application/xhtml+xml, text/html;q=0.9", "Accept-Language": LANGS.get(lang, lang)},
    )
    with urllib.request.urlopen(request, timeout=90) as response:
        return response.geturl(), response.read().decode("utf-8", errors="replace")


def to_text(fragment: str) -> str:
    fragment = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", fragment)
    fragment = re.sub(r"(?i)<br\s*/?>|</(p|div|tr|li|h\d)>", "\n", fragment)
    text = html.unescape(re.sub(r"<[^>]+>", " ", fragment))
    lines = (re.sub(r"[ \t\xa0]+", " ", line).strip() for line in text.splitlines())
    return "\n".join(line for line in lines if line)


def extract_article(doc: str, number: str, lang: str) -> str | None:
    word = ARTICLE_WORD.get(lang, "Article")
    heading = re.compile(
        r'<p[^>]*class="[^"]*(?:%s)[^"]*"[^>]*>\s*(?:%s|Article)\s+(\d+[a-z]*)\s*<' % ("|".join(HEADING_CLASSES), re.escape(word)),
        re.I,
    )
    matches = list(heading.finditer(doc))
    for index, match in enumerate(matches):
        if match.group(1).lower() == number.lower():
            end = matches[index + 1].start() if index + 1 < len(matches) else len(doc)
            return to_text(doc[match.start():end])
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("celex", help="CELEX number, e.g. 32016R0679")
    parser.add_argument("--lang", default="en", help="two-letter language code (default: en)")
    parser.add_argument("--latest", action="store_true", help="use the newest consolidated version, if any")
    parser.add_argument("--article", help="print only this article, e.g. 13 or 11a")
    parser.add_argument("--url", action="store_true", help="only print the resolved, directly fetchable URL")
    parser.add_argument("--out", help="write the text to this file instead of stdout")
    args = parser.parse_args()

    celex = args.celex.strip()
    if args.latest:
        consolidated = latest_consolidated(celex.split("-")[0].replace("0", "3", 1) if celex.startswith("0") else celex)
        if consolidated:
            celex = consolidated
        else:
            print(f"note: no consolidated version found for {celex}; using the original act", file=sys.stderr)

    final_url, doc = fetch(celex, args.lang)
    print(f"CELEX: {celex}\nSource: {final_url}\nEUR-Lex page (for humans): "
          f"https://eur-lex.europa.eu/legal-content/{args.lang.upper()}/TXT/?uri=CELEX:{celex}", file=sys.stderr)
    if args.url:
        print(final_url)
        return 0

    text = extract_article(doc, args.article, args.lang) if args.article else to_text(doc)
    if text is None:
        print(f"article {args.article} not found in {celex}", file=sys.stderr)
        return 1
    if args.out:
        with open(args.out, "w", encoding="utf-8") as handle:
            handle.write(text + "\n")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
