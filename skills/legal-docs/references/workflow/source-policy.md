# Source policy

The point of this skill is that legal requirements come from **the law and the regulators**, not
from the model's memory. This file defines which sources count, how to use them, and what to do
when they fail.

## Tiers

| Tier | What | Examples | May be used for |
|---|---|---|---|
| **T1** | Official legislation portals: the binding or officially published text | EUR-Lex, gesetze-im-internet.de, RIS (AT), fedlex (CH), legislation.gov.uk, uscode.house.gov, eCFR / govinfo, state legislature sites | Any legal requirement |
| **T2** | Official guidance from regulators, supervisory authorities, courts and governments | EDPB, European Commission, national DPAs (DSK, BfDI, DSB, EDÖB, ICO, CNIL…), FTC, CPPA, state AGs, statutory chambers (WKO) | Interpreting T1; best practice; what regulators expect |
| **T3** | Reputable non-official best-practice material | IAPP trackers, bar association guides, established law-firm publications | Orientation only (status trackers, "which laws exist"). Never the sole basis of a requirement |
| **T4** | Anything you found yourself that is not in the bundled library | Search results | Only after the fallback procedure below, always labelled |

Prefer T1 for *what the law requires* and T2 for *how to do it*. When T1 and T2 disagree, the text
of the law wins and you point out the conflict in the defense report.

## How to use a source

1. Find the entry in `references/sources/<jurisdiction>.md`. Use its ID in all citations.
2. **Fetch the URL in this session** and read the provision you rely on. A doc-type checklist
   saying "Art. 13(1)(c)" is a pointer, not the content. Read the actual text.
3. Cite with ID + pinpoint: `EU-GDPR Art. 13(1)(c)`, `DE-DDG § 5(1) Nr. 2`, `UK-PECR reg. 6(1)`,
   `US-CA-CCPA Civ. Code § 1798.130(a)(5)`.
4. Log every source you used in the project's `sources-used.md` with date fetched, the pinpoints
   used, and status (`bundled`, `replacement`, `non-official`, `unverified`).
5. Check whether you are reading the **current** version: consolidated text, "Stand"/"Fassung vom",
   "changes to legislation" banners on legislation.gov.uk, amendment notes, effective dates. If a
   law was amended after the bundled `Last verified` date, say so and use the current text.
6. Quote short passages verbatim in the defense report when the wording matters (e.g. the
   mandatory model withdrawal form). Paraphrase everything else, and keep the pinpoint.

## Fetching tips

- **EUR-Lex** answers automated clients with an empty JavaScript "challenge" page. Do not fetch
  eur-lex.europa.eu directly. Use the entry's `URL` (the same official text served by the EU
  Publications Office) or, with a shell,
  `python3 <skill-dir>/scripts/eurlex.py <celex> --latest --article <n> [--lang de]`, which
  finds the newest consolidated version and prints a single article. Cite the EUR-Lex link
  (`Cite as`) in documents. Never substitute the UK's retained version on legislation.gov.uk for
  the EU text: it is a different, amended law.
- **fedlex (CH)** is a JavaScript app. Run `python3 <skill-dir>/scripts/fedlex_latest.py <eli>` to
  get the static HTML of the current consolidated version, or use the bundled filestore URL and
  check whether a newer consolidation exists.
- **RIS (AT)** `GeltendeFassung.wxe?...&Gesetzesnummer=...` shows the whole current law. Single
  paragraphs can be opened from there.
- **gesetze-im-internet.de** has one page per section: `https://www.gesetze-im-internet.de/<law>/__<n>.html`
  (e.g. `bgb/__312k.html`). Annexes look like `bgbeg/art_253anlage_1.html`.
- **legislation.gov.uk** pinpoints: `/article/13`, `/section/5`, `/regulation/6`, `/schedule/3`.
- **uscode.house.gov** pinpoints: `view.xhtml?req=granuleid:USC-prelim-title<T>-section<S>&num=0&edition=prelim`.
- Sites marked `Bot-protected: yes` often block automated fetches. Try in this order:
  1. your web-fetch tool (some sites that block scripts answer it, e.g. ftc.gov, gc.nh.gov);
  2. a headless browser if you have one (some sites that refuse plain HTTP clients load in it,
     e.g. dsb.gv.at, normattiva.it);
  3. the official alternative listed in the entry's `Also` field (gazette, regulator, AG page);
  4. ask the user to open the link and paste the relevant text; then the fallback procedure below.
  Do **not** try to defeat a bot challenge (Cloudflare "verify you are human") or turn off TLS
  verification when a server sends a broken certificate chain. Treat those sites as unreachable.
- The entry's `Verification` field says how it was last read (automated, browser, web-fetch,
  or "unverified"). Where it says the official text was not read, treat the entry's key
  provisions as a pointer from a secondary source and say so in the defense report.
- PDFs are fine. If your fetch tool cannot read PDFs, say so and use the HTML alternative.

## Fallback procedure (bundled source fails)

A source "fails" when the URL errors, redirects to something unrelated, shows a repeal notice, or
no longer contains the provision.

1. **Tell the user immediately and explicitly**, e.g.:
   > The bundled source `DE-TDDDG` (https://…) could not be retrieved (HTTP 404). The skill's
   > source library may be out of date. I will now search for a replacement on official sites.
2. Search for a replacement **on official domains first** (the same portal, the regulator, the
   official gazette). Prefer queries like `site:gesetze-im-internet.de TDDDG 25`.
3. If you find an official replacement, use it, mark it `replacement` in `sources-used.md`, and
   suggest updating the skill's library (see the repo's CONTRIBUTING.md).
4. If **no official source can be retrieved**, say so explicitly before going on:
   > I could not retrieve any official source for <topic>. What follows rests on non-official
   > sources (<list>). Treat it with extra caution and have a lawyer verify it.
   Use the best T3/T4 source you can find, mark it `non-official` in `sources-used.md`, and mark
   the affected clause `NON-OFFICIAL SOURCE` in the draft's traceability comment and in the
   defense report.
5. If you cannot retrieve **anything** and would have to rely on model knowledge, do not hide it:
   mark the clause `UNVERIFIED (model knowledge)` in the draft (visible, not only in a comment),
   list it at the top of the defense report, and tell the user. Prefer leaving a clause out and
   asking the user or a lawyer over inventing it.

## Things that change often: always check live

- Effective dates and amendments of US state privacy laws (use `US-IAPP-TRACKER` for status, then
  the state's official text).
- Adequacy decisions and the status of the EU–US Data Privacy Framework (court challenges are
  pending; see `EU-DPF` notes).
- Commencement of UK reforms (DUAA 2025, DMCC Act 2024 subscription rules).
- New consolidations of Swiss and Austrian law.
- EDPB guidelines that are "for public consultation" vs. adopted final versions.
