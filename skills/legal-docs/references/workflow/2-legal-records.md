# Phase 2: Legal Decision Records (LDRs)

Everything the documents depend on is written down in the user's project, like Architecture
Decision Records, but for legal facts and choices. The records make the drafts reproducible,
reviewable by a lawyer, and updatable when the product changes.

## Folder layout (default `docs/legal/`)

```
docs/legal/
├── README.md              index of records and documents + disclaimer (from assets/templates/legal-readme.md)
├── sources-used.md        every source consulted, with date, pinpoints and status (assets/templates/sources-used.md)
├── records/
│   ├── 0001-legal-entity.md
│   ├── 0002-jurisdictions-and-target-markets.md
│   ├── 0003-audience-b2c-b2b-minors.md
│   └── ...
├── documents/             the drafted legal documents (phase 4)
│   ├── privacy-policy.en.md
│   └── imprint.de.md
└── defense/               one defense report per document (phase 5)
    └── privacy-policy.md
```

Ask before creating the folder somewhere else. If the project already has an ADR folder, keep
the legal records separate anyway (different reviewers, different lifecycle).

## Record format

Use [assets/templates/ldr.md](../../assets/templates/ldr.md). Rules:

- **File name**: `NNNN-kebab-case-title.md`, numbered sequentially, never reused.
- **ID**: `LDR-NNNN`. Documents and defense reports cite records by ID.
- **Type**: `fact` (something true about the business: the entity's name, the payment provider),
  `decision` (a choice: governing law, relying on consent for analytics, not offering a
  withdrawal waiver), or `inventory` (the processing inventory from phase 3).
- **Status**: `proposed` (written, not yet confirmed by the user) → `accepted` (user confirmed)
  → `superseded by LDR-NNNN` (replaced). Only `accepted` records may be used for drafting.
- **Source of the information**: `user (interview Q12, 2026-10-17)`, `code (src/lib/stripe.ts:14)`,
  or both. Never "assumed".
- **Legal sources**: source IDs + pinpoints that make this record relevant (e.g. "`DE-DDG § 5(1)
  Nr. 4` requires the register number in the imprint"). Mark each as `fetched YYYY-MM-DD`.
- **Consequences**: what this means for which document ("Imprint must show HRB 12345, Amtsgericht
  Berlin-Charlottenburg").
- **Open questions**: anything unknown. A record with open questions stays `proposed`, unless
  the user explicitly accepts the gap (then the open question moves to the defense report).

Immutability: once `accepted`, never rewrite a record's facts or decision. Write a new record
that supersedes it and update the old one's status line only. Typos and formatting are fine to fix.

## Which records to create (typical set)

| # | Title | Type |
|---|---|---|
| 0001 | Legal entity and contact details | fact |
| 0002 | Jurisdictions and target markets | decision |
| 0003 | Audience: consumers / businesses / minors | fact + decision |
| 0004 | Documents to produce and languages | decision |
| 0005 | Products, pricing, payment and contract model | fact |
| 0006 | Data protection roles (controller / processor / DPO / representative) | fact + decision |
| 0007 | Processing inventory (from code + interview) | inventory |
| 0008 | Third parties and international transfers | fact + decision |
| 0009 | Cookies, tracking and consent approach | decision |
| 0010 | Retention periods | decision |
| 0011 | Governing law, jurisdiction, dispute resolution | decision |
| 0012 | Liability, warranty, termination positions | decision |
| 0013 | Legal review: who and when | fact |

Add more as needed (newsletter, AI features, user-generated content, accessibility). Keep each
record small: one topic per record.

## Index (`docs/legal/README.md`)

Keep the table of records current after every change: ID, title, type, status, date. Also list
the drafted documents with version, date, the records they rely on, and review status
(`DRAFT – not reviewed` until the user says a lawyer approved it).

## sources-used.md

Append a row for every source you fetch: ID (or `REPLACEMENT`/`NON-OFFICIAL` + URL), title,
date fetched, pinpoints used, used in (records/documents), status, notes (e.g. "bundled URL
404, replacement found on gesetze-im-internet.de").
