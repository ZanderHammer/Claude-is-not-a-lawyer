#!/usr/bin/env python3
"""Resolve the current consolidated text of a Swiss federal act on fedlex.

fedlex.admin.ch is a JavaScript app, so its normal pages (e.g.
https://www.fedlex.admin.ch/eli/cc/2022/491/de) show nothing to a plain HTTP
fetch. The static HTML/PDF files behind it live under a date-stamped path.
This script asks the official fedlex SPARQL endpoint for the newest
consolidation date and prints fetchable URLs.

Usage:
    python3 fedlex_latest.py eli/cc/2022/491            # Datenschutzgesetz (DSG), German
    python3 fedlex_latest.py eli/cc/2022/491 --lang fr  # de | fr | it | rm | en (en = unofficial)

Standard library only.
"""

import argparse
import json
import sys
import urllib.parse
import urllib.request

ENDPOINT = "https://fedlex.data.admin.ch/sparqlendpoint"
QUERY = """PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
SELECT ?c ?d WHERE {{
  ?c jolux:isMemberOf <https://fedlex.data.admin.ch/{eli}> .
  ?c jolux:dateApplicability ?d .
  FILTER (?d <= NOW())
}} ORDER BY DESC(?d) LIMIT 1"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("eli", help="ELI path of the act, e.g. eli/cc/2022/491")
    parser.add_argument("--lang", default="de")
    args = parser.parse_args()
    eli = args.eli.strip("/").split("fedlex.admin.ch/")[-1].split("fedlex.data.admin.ch/")[-1]

    data = urllib.parse.urlencode({"query": QUERY.format(eli=eli)}).encode()
    request = urllib.request.Request(ENDPOINT, data=data, headers={"Accept": "application/sparql-results+json"})
    with urllib.request.urlopen(request, timeout=30) as response:
        bindings = json.load(response)["results"]["bindings"]
    if not bindings:
        print(f"no consolidation found for {eli}", file=sys.stderr)
        return 1

    date = bindings[0]["d"]["value"].replace("-", "")
    slug = f"fedlex-data-admin-ch-{eli.replace('/', '-')}-{date}-{args.lang}"
    base = f"https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/{eli}/{date}/{args.lang}"
    print(f"consolidation date: {bindings[0]['d']['value']}")
    print(f"html: {base}/html/{slug}-html-1.html")
    print(f"pdf:  {base}/pdf-a/{slug}-pdf-a.pdf")
    print(f"page: https://www.fedlex.admin.ch/{eli}/{args.lang} (JavaScript app, for humans)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
