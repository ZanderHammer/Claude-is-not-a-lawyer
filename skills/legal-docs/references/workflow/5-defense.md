# Phase 5: Defense

Every document gets a defense report: a written argument for each choice in it, with sources,
so the user and their lawyer can check the reasoning instead of trusting it. Write it in the
user's working language (English by default), even if the document is in another language.

File: `docs/legal/defense/<doc>.md`, from [assets/templates/defense-report.md](../../assets/templates/defense-report.md).

## What to write

1. **Disclaimer** (long form, at the top).
2. **Summary**: what the document is, for which jurisdictions and audience, which records it is
   based on, version and date.
3. **Warnings first**: every clause marked `UNVERIFIED`, `NON-OFFICIAL SOURCE` or `REPLACEMENT`,
   every `[[TODO]]`, every code gap from phase 3 that affects this document. Do not bury them.
4. **Clause-by-clause defense.** For each section or clause:
   - **What it says** (one line).
   - **Why it is there**: the legal requirement or the business decision behind it.
   - **Source**: source ID + pinpoint, the URL you fetched, the date, and a short verbatim quote
     where the wording matters. Records it relies on (LDR IDs).
   - **Choice and alternatives**: what you chose, what else was possible, why you rejected it
     (e.g. "Legal basis legitimate interest (Art. 6(1)(f)) rather than consent for server logs,
     because …; the alternative would require …").
   - **Confidence and risk**: `high` (directly required by the text, facts confirmed), `medium`
     (interpretation, regulator guidance, or facts partially confirmed), `low` (contested,
     unverified, or depends on facts you could not confirm). Say why.
5. **Requirements considered and not included**, with the reason (e.g. "No DPO named: BDSG § 38
   threshold not met per LDR-0006; re-check if headcount grows").
6. **Conflicts and judgment calls**: where sources disagree (law vs. regulator guidance, EU vs.
   US approach), what you did and why.
7. **Questions for the lawyer**: concrete, answerable questions. Not "please check everything",
   but "Is the limitation of liability in § 8(2) enforceable against consumers in Austria under
   AT-KSCHG § 6, given …?".
8. **Implementation checklist**: duties the code or the business must fulfil for the document to
   be true (see phase 4 step 5).
9. **Changelog**: version, date, what changed, why (link to superseding LDRs).

## Tone

Argue like a careful junior associate preparing a memo for a partner: precise, sourced, honest
about uncertainty. Never claim the document is compliant or safe. "Drafted to address
EU-GDPR Art. 13(1)–(2)" is fine; "GDPR compliant" is not.

## Hand-off message in chat

After writing all documents and defense reports, tell the user (and keep it scannable):

- the files created or changed,
- per document: version, jurisdictions, number of `low`-confidence clauses, open TODOs,
- all `UNVERIFIED` / `NON-OFFICIAL SOURCE` items,
- bundled sources that failed (so they can update the skill),
- the implementation checklist,
- the questions for the lawyer,
- and the long disclaimer, verbatim.
