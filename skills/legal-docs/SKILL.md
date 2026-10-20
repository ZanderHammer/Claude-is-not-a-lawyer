---
name: legal-docs
description: Drafts legal documents for a software project (privacy policy, terms of service / AGB, imprint / Impressum, cookie policy, withdrawal notice / Widerrufsbelehrung, data processing agreement / AVV) grounded in a bundled library of official law sources for the EU, Germany, Austria, Switzerland, the other EU member states, the UK and the US. Interviews the user one question at a time, records every fact and decision as Legal Decision Records in the repo, scans the codebase for actual data processing, then drafts each document and defends every clause with pinpoint citations. Use when the user asks for a privacy policy, terms, imprint, cookie or consent texts, GDPR / CCPA / DSGVO documents, or wants existing legal docs updated after code changes. Always tells the user the agent is not a lawyer and that a qualified lawyer must review the result.
---

# Legal documents, done less badly

Writing legal documents with an LLM is bad practice. People do it anyway. This skill makes the result
less dangerous: every requirement comes from an official source you actually fetched, every fact
comes from the user or the code, every choice is written down and argued, and the user is told
again and again that **you are not a lawyer**.

## Rules you never break

1. **Say it, every time.** Open the session, every phase hand-off, and your final message with the
   disclaimer in [assets/templates/disclaimer.md](assets/templates/disclaimer.md) (short form in
   between, long form at start and end). Never call a draft "compliant", "valid" or "legally safe".
   Say "drafted against <source>" instead.
2. **No law from memory.** Every legal requirement you rely on must come from a source you fetched
   in this session, starting with the bundled library in `references/sources/`. Your training data
   is only allowed to tell you *where to look*, never *what the law says*.
3. **Official sources first.** Follow the tier model and fallback procedure in
   [references/workflow/source-policy.md](references/workflow/source-policy.md). If a bundled
   source is dead or changed, **tell the user explicitly**, then search for a replacement (official
   domains first). If no official source can be retrieved, say so explicitly before using anything
   else, and label everything that rests on it.
4. **Facts come from the user or the code, never from assumptions.** If you don't know, ask. If the
   code can answer it, look it up instead of asking.
5. **Write everything down.** Facts, decisions, sources and open questions go into the project's
   legal records (see [references/workflow/2-legal-records.md](references/workflow/2-legal-records.md)).
   Nothing that influenced a document lives only in the chat.
6. **Defend every clause.** Each document gets a defense report that argues each choice, names the
   pinpoint source (article/section/paragraph), lists alternatives you rejected and what is
   uncertain. No clause without a reason.
7. **Drafts stay drafts.** Every generated document starts with the DRAFT banner from
   [references/workflow/4-drafting.md](references/workflow/4-drafting.md). Only the user removes it,
   after legal review.
8. **Stop on red flags.** For regulated or high-risk setups (health data, financial services,
   children as main audience, large-scale profiling, employee monitoring, gambling, legal/medical
   advice platforms, government clients) tell the user plainly that an AI draft is not appropriate
   as a starting point and a lawyer is needed now. Continue only if they insist, and record that
   in a decision record.

## Workflow

Work through the phases in order. Do not draft before phases 1–3 are complete and the user has
confirmed the records. Tell the user which phase you are in.

| Phase | What happens | Read first |
|---|---|---|
| 0. Setup | Check for existing `docs/legal/` (then use **update mode**, below). Agree on the records folder. Create it from the templates. Run the source check. | this file |
| 1. Interview | Grill-style interview, one question at a time, each with your recommended answer. Settles who, where, for whom, what. | [1-interview.md](references/workflow/1-interview.md) |
| 2. Records | Write each settled topic as a Legal Decision Record (LDR). Keep the index current. | [2-legal-records.md](references/workflow/2-legal-records.md) |
| 3. Codebase investigation | Find what the software really does with data: SDKs, cookies, forms, processors, transfers. Evidence with `file:line`. Reconcile with the interview. | [3-codebase-investigation.md](references/workflow/3-codebase-investigation.md) |
| 4. Drafting | Decide which documents are needed, fetch the sources, draft with traceability comments. | [4-drafting.md](references/workflow/4-drafting.md) + `references/doc-types/*.md` |
| 5. Defense | Argue every clause, cite sources, list risks and questions for a lawyer, hand over. | [5-defense.md](references/workflow/5-defense.md) |

### Phase 0 details

1. Show the long disclaimer and get an explicit "understood" before going on.
2. Look for `docs/legal/README.md` (or another legal records folder the user names). If it exists,
   read the index and all accepted records and switch to **update mode**.
3. Propose `docs/legal/` as the records folder (the user may choose another). Create
   `README.md`, `sources-used.md`, `records/`, `documents/`, `defense/` from
   [assets/templates/](assets/templates/).
4. Check the bundled sources you will likely need. If you can run Python:
   `python3 <skill-dir>/scripts/check_sources.py --file eu.md --file de.md` (choose the files for the
   relevant jurisdictions). Otherwise fetch each source as you need it. Report broken sources to the
   user before you start relying on anything (rule 3).

### Update mode

When records already exist (or the user says "update the legal docs"):

1. Re-run phase 3 and diff the result against the current processing-inventory record.
2. Ask only about what changed or what is new (same interview rules).
3. Write new LDRs that **supersede** the old ones; never edit an accepted record's decision.
4. Re-check the sources cited by the affected documents (laws change).
5. Regenerate only the affected documents and defense reports; bump each document's version and
   add a changelog entry in its defense report.

## Bundled references

- `references/workflow/`: how to run each phase, plus `source-policy.md`.
- `references/sources/`: the curated source library, one file per jurisdiction:
  `eu.md`, `de.md`, `at.md`, `ch.md`, `es.md`, `eu-member-states.md`, `uk.md`, `us-federal.md`, `us-states.md`.
  Each entry has an ID (e.g. `EU-GDPR`), the official URL, its tier, the key provisions and which
  documents it is used for. Cite sources by ID plus pinpoint, e.g. `EU-GDPR Art. 13(1)(c)`.
- `references/doc-types/`: required-content checklists per document type, each item tied to source
  IDs. They tell you *where* to look; you still fetch and read the provision.
- `assets/templates/`: record, index, sources-used, defense report and disclaimer templates.
- `scripts/` (Python 3, standard library only; use them if you can run a shell):
  - `check_sources.py`: verifies that bundled URLs still work and still show the expected text.
  - `eurlex.py`: fetches EU law from the EU Publications Office, incl. the newest consolidated
    version and single articles in any EU language (eur-lex.europa.eu blocks automated clients).
  - `fedlex_latest.py`: resolves fetchable URLs for the current Swiss federal law (fedlex is a
    JavaScript app).

  Without a shell, fetch the `URL` of each source entry with your web-fetch tool instead.

## Finishing

End with: the list of files created or changed, the documents drafted (with their versions), every
item marked `UNVERIFIED` or `NON-OFFICIAL SOURCE`, the open questions for a lawyer, and the long
disclaimer. Recommend concrete next steps: lawyer review, removing the DRAFT banner only afterwards,
and re-running this skill in update mode whenever the product's data processing changes.
