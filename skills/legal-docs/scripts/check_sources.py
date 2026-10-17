#!/usr/bin/env python3
"""Check the bundled source library of the legal-docs skill.

Parses every source entry in references/sources/*.md of this skill and,
for each one, fetches the URL and confirms that the page still contains the
"Expect" text. Uses only the Python standard library so any agent or CI
runner can execute it.

Entry format (see references/workflow/source-policy.md):

    ### EU-GDPR — General Data Protection Regulation
    - URL: https://eur-lex.europa.eu/eli/reg/2016/679/oj
    - Expect: 2016/679
    - Also: https://... https://...   (optional: extra pinpoint URLs, reachability only)
    - Bot-protected: yes        (optional: 401/403/404/429/503 and refused connections are
                                 reported as WARN, not FAIL; verify such entries by hand)

Usage:
    python3 <skill-dir>/scripts/check_sources.py                 # check everything
    python3 <skill-dir>/scripts/check_sources.py --file de.md    # one jurisdiction file
    python3 <skill-dir>/scripts/check_sources.py --id EU-GDPR    # single entries (repeatable)
    python3 <skill-dir>/scripts/check_sources.py --json          # machine-readable output

Exit code is 1 if any entry FAILs, 0 otherwise (WARNs do not fail).
"""

from __future__ import annotations

import argparse
import concurrent.futures
import gzip
import html
import json
import re
import ssl
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
import zlib
from dataclasses import asdict, dataclass, field
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
SOURCES_DIR = SKILL_DIR / "references" / "sources"
USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0 Safari/537.36 legal-docs-source-checker"
)
HEADER_RE = re.compile(r"^###\s+([A-Z0-9][A-Z0-9-]*)\s+[—-]\s+(.+?)\s*$")
FIELD_RE = re.compile(r"^-\s+([A-Za-z-]+):\s*(.+?)\s*$")


@dataclass
class Entry:
    id: str
    title: str
    file: str
    line: int
    url: str = ""
    expect: str = ""
    also: list[str] = field(default_factory=list)
    bot_protected: bool = False


@dataclass
class Result:
    id: str
    file: str
    line: int
    url: str
    status: str  # OK | WARN | FAIL
    http: int | None = None
    final_url: str = ""
    message: str = ""
    notes: list[str] = field(default_factory=list)
    unreachable: bool = False


def parse_entries(paths: list[Path]) -> list[Entry]:
    entries: list[Entry] = []
    for path in paths:
        current: Entry | None = None
        for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            header = HEADER_RE.match(raw)
            if header:
                current = Entry(header.group(1), header.group(2), path.name, lineno)
                entries.append(current)
                continue
            if raw.startswith("#"):
                current = None
                continue
            field_match = FIELD_RE.match(raw)
            if not (current and field_match):
                continue
            key, value = field_match.group(1).lower(), field_match.group(2)
            if key == "url":
                current.url = value.strip("<>")
            elif key == "expect":
                current.expect = value.strip().strip('"')
            elif key == "also":
                current.also.extend(re.findall(r"https?://[^\s<>,)]+", value))
            elif key == "bot-protected":
                current.bot_protected = value.lower().startswith("y")
    return entries


def normalise(text: str) -> str:
    text = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", text)
    text = html.unescape(re.sub(r"<[^>]+>", " ", text))
    return re.sub(r"\s+", " ", text).lower()


def decode(body: bytes, encoding: str | None) -> str:
    if encoding == "gzip":
        body = gzip.decompress(body)
    elif encoding == "deflate":
        body = zlib.decompress(body)
    for charset in ("utf-8", "cp1252", "latin-1"):
        try:
            return body.decode(charset)
        except UnicodeDecodeError:
            continue
    return body.decode("utf-8", errors="replace")


class Challenge(Exception):
    """The site answered with a bot challenge or rate limit instead of content."""


CHALLENGE_MARKERS = (
    "awswafcookiedomainlist", "cf-challenge", "challenge-platform", "captcha",
    "resembles an abusive automated request",  # ftc.gov answers bots with a 404 like this
)
_host_locks: dict[str, threading.Lock] = {}
_host_last: dict[str, float] = {}
_registry_lock = threading.Lock()


def _is_block_page(err: urllib.error.HTTPError) -> bool:
    try:
        body = decode(err.read(200_000), err.headers.get("Content-Encoding")).lower()
    except Exception:
        return False
    return any(marker in body for marker in CHALLENGE_MARKERS)


def _raw_fetch(url: str, timeout: int) -> tuple[int, str, str]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/pdf;q=0.9,*/*;q=0.8",
            "Accept-Language": "en,de;q=0.8,fr;q=0.6",
            "Accept-Encoding": "gzip, deflate",
        },
    )
    context = ssl.create_default_context()
    with urllib.request.urlopen(request, timeout=timeout, context=context) as response:
        body = response.read(8_000_000)
        return response.status, response.geturl(), decode(body, response.headers.get("Content-Encoding"))


def fetch(url: str, timeout: float, delay: float = 0.0, retries: int = 2) -> tuple[int, str, str]:
    """Fetch politely: one request at a time per host, `delay` seconds apart,
    backing off and retrying when the host serves a challenge/rate limit,
    and retrying once after a network error (timeout, reset, DNS)."""
    host = urllib.parse.urlsplit(url).hostname or ""
    with _registry_lock:
        lock = _host_locks.setdefault(host, threading.Lock())
    with lock:
        network_retry_used = False
        attempt = 0
        while True:
            wait = _host_last.get(host, 0.0) + delay - time.monotonic()
            if wait > 0:
                time.sleep(wait)
            try:
                status, final_url, body = _raw_fetch(url, timeout)
                challenged = status == 202 or any(m in body[:5000].lower() for m in CHALLENGE_MARKERS)
            except urllib.error.HTTPError as err:
                if err.code != 429 and not _is_block_page(err):
                    raise
                challenged = True
            except OSError:  # URLError, timeouts, resets, TLS errors
                if network_retry_used:
                    raise
                network_retry_used = True
                time.sleep(5)
                continue
            finally:
                _host_last[host] = time.monotonic()
            if not challenged:
                return status, final_url, body
            if attempt >= retries:
                raise Challenge("site served a bot challenge / rate limit")
            attempt += 1
            time.sleep(30 * attempt)


def check(entry: Entry, timeout: float, delay: float) -> Result:
    result = Result(entry.id, entry.file, entry.line, entry.url, "FAIL")
    if not entry.url:
        result.message = "entry has no URL"
        return result
    try:
        result.http, result.final_url, body = fetch(entry.url, timeout, delay)
    except Challenge as err:
        result.status = "WARN"
        result.message = f"{err}; content not verified, re-run later or open in a browser"
        return result
    except urllib.error.HTTPError as err:
        result.http = err.code
        # Some sites (e.g. ftc.gov) answer automated clients with a fake 404.
        if entry.bot_protected and err.code in (401, 403, 404, 429, 503):
            result.status = "WARN"
            result.message = f"HTTP {err.code} (site is marked bot-protected; verify with a browser or web-fetch tool)"
        elif err.code >= 500:  # server trouble says nothing about whether the page still exists
            result.status = "WARN"
            result.unreachable = True
            result.message = f"HTTP {err.code} server error; not verified, re-run later"
        else:
            result.message = f"HTTP {err.code}"
        return result
    except Exception as err:  # timeouts, resets, DNS, TLS: blocked from this network, not proof the source is gone
        result.status = "WARN"
        result.unreachable = True
        result.message = f"unreachable from this network ({type(err).__name__}: {err}); not verified"
        return result

    if entry.expect and normalise(entry.expect) not in normalise(body):
        if entry.bot_protected:
            result.status = "WARN"
            result.message = f'expected text "{entry.expect}" not found (bot-protected site, may be a challenge page)'
        else:
            result.message = f'expected text "{entry.expect}" not found on page'
        return result

    warn = False
    for extra in entry.also:
        try:
            fetch(extra, timeout, delay)
        except Challenge:
            result.notes.append(f"Also-URL {extra} served a challenge; not verified")
        except urllib.error.HTTPError as err:
            if err.code in (404, 410):
                result.message = f"Also-URL {extra} returned HTTP {err.code}"
                return result
            if not entry.bot_protected:
                warn = True
            result.notes.append(f"Also-URL {extra} returned HTTP {err.code}; not verified")
        except Exception as err:  # refused connections, TLS problems: blocked, not necessarily gone
            warn = True
            result.notes.append(f"Also-URL {extra} unreachable ({type(err).__name__}: {err})")

    result.status = "WARN" if warn else "OK"
    if result.final_url.rstrip("/") != entry.url.rstrip("/"):
        result.notes.append(f"redirected to {result.final_url}")
    if not entry.expect:
        result.notes.append("no Expect text defined; only reachability was checked")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--file", action="append", help="only check this sources file (e.g. de.md)")
    parser.add_argument("--id", action="append", help="only check this source ID (repeatable)")
    parser.add_argument("--timeout", type=float, default=30, help="seconds per request")
    parser.add_argument("--workers", type=int, default=16, help="hosts checked in parallel")
    parser.add_argument("--delay", type=float, default=3.0, help="seconds between requests to the same host")
    parser.add_argument("--json", action="store_true", help="print JSON instead of a table")
    args = parser.parse_args()

    paths = sorted(SOURCES_DIR.glob("*.md"))
    if args.file:
        paths = [p for p in paths if p.name in args.file]
    entries = parse_entries(paths)
    if args.id:
        wanted = set(args.id)
        entries = [e for e in entries if e.id in wanted]
    if not entries:
        print("no source entries matched", file=sys.stderr)
        return 1

    duplicates = {e.id for e in entries if sum(o.id == e.id for o in entries) > 1}
    # One worker per host so a slow or rate-limiting site does not starve the others.
    by_host: dict[str, list[Entry]] = {}
    for entry in entries:
        by_host.setdefault(urllib.parse.urlsplit(entry.url).hostname or "", []).append(entry)
    checked: dict[int, Result] = {}

    def run_host(group: list[Entry]) -> None:
        for entry in group:
            checked[id(entry)] = check(entry, args.timeout, args.delay)

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        list(pool.map(run_host, by_host.values()))
    results = [checked[id(e)] for e in entries]
    for res in results:
        if res.id in duplicates:
            res.status = "FAIL"
            res.message = (res.message + "; " if res.message else "") + "duplicate source ID"

    if args.json:
        print(json.dumps([asdict(r) for r in results], indent=2, ensure_ascii=False))
    else:
        for res in results:
            detail = res.message or "; ".join(res.notes)
            print(f"{res.status:4}  {res.id:28} {res.file}:{res.line}  {detail}")
        counts = {s: sum(r.status == s for r in results) for s in ("OK", "WARN", "FAIL")}
        print(f"\n{len(results)} sources: {counts['OK']} OK, {counts['WARN']} WARN, {counts['FAIL']} FAIL")
        # A whole host failing at network level is a block or outage, not many dead links.
        for host, group in by_host.items():
            if len(group) > 1 and all(checked[id(e)].unreachable for e in group):
                print(f"note: host {host} was unreachable for all {len(group)} entries "
                      "(blocked from this network or down); check it from another network")
        print("WARN = blocked, rate-limited or unreachable from this network: verify by hand. "
              "FAIL = the source is broken (dead link or expected text missing).")
    return 1 if any(r.status == "FAIL" for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
