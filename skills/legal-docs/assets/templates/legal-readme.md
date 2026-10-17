# Legal records

> **I am not a lawyer, and this is not legal advice.** These records and documents were prepared
> by an AI coding agent using the `legal-docs` skill. Everything here is a **draft for review by a
> qualified lawyer**. Do not publish or sign any document before that review.

This folder documents every fact, decision and source behind the project's legal documents, so
a lawyer can review the reasoning and the documents can be updated when the product changes.

- `records/`: Legal Decision Records (LDRs), one topic each. Accepted records are never
  rewritten. Changes come as new records that supersede old ones.
- `documents/`: the drafted legal documents.
- `defense/`: one defense report per document: each clause, its reasoning, sources, risks and
  open questions for the lawyer.
- `sources-used.md`: every legal source consulted, with dates and pinpoints.

## Records

| ID | Title | Type | Status | Date |
|---|---|---|---|---|
| LDR-0001 | Legal entity and contact details | fact | proposed | YYYY-MM-DD |

## Documents

| Document | File | Version | Date | Based on | Review status |
|---|---|---|---|---|---|
| Privacy policy (EN) | `documents/privacy-policy.en.md` | 0.1 | YYYY-MM-DD | LDR-0001, … | DRAFT – not reviewed |

## Legal review

- Reviewer: <name / firm, or "not yet assigned">
- Planned by: <date>
- Result: <pending>

## How to update

Re-run the `legal-docs` skill in update mode whenever the product's data processing, business
model, markets or company details change. The agent will diff the code against the processing
inventory, ask about changes, supersede records and regenerate the affected documents.
