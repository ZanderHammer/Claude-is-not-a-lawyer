# Defense report: <Document name> (<language>)

> **I am not a lawyer, and this is not legal advice.**
> I am an AI coding agent. I can draft legal documents based on the official sources bundled with
> this skill, your answers and your code, and I explain every choice I make. But I can
> misread the law, miss a rule, apply the wrong rule to your situation, or rely on facts that are
> incomplete. Laws and court decisions change, and they differ between countries.
> Everything I produce is a **draft for review by a qualified lawyer** in the relevant
> jurisdiction(s). Do not publish or sign any of it before that review. You remain responsible for
> the documents you use.

- **Document**: `docs/legal/documents/<doc>.<lang>.md`
- **Version / date**: 0.1 / YYYY-MM-DD
- **Jurisdictions**: …
- **Audience**: B2C / B2B / both; minors: yes/no
- **Based on records**: LDR-…, LDR-…

## 1. Warnings (read first)

| Clause | Issue | Marker |
|---|---|---|
| § 4 Analytics | Code loads analytics before consent (`app/layout.tsx:8`); the document describes consent-based loading, which is not true yet | CODE GAP |
| § 9 Retention | Retention for backups unknown | TODO |
| … | Source `XX-…` unreachable; replacement used | REPLACEMENT |

## 2. Clause-by-clause defense

### § 1 <Clause title>

- **What it says**: …
- **Why it is there**: …
- **Sources**: `EU-GDPR Art. 13(1)(a)` (https://…, fetched YYYY-MM-DD): "…short quote…"; records LDR-0001
- **Choice and alternatives**: …
- **Confidence**: high / medium / low, because …

(Repeat for every clause.)

## 3. Requirements considered and not included

| Requirement | Source | Why not included |
|---|---|---|
| Data protection officer | DE-BDSG § 38 | Threshold not met (LDR-0006). Re-check if headcount grows |

## 4. Conflicts and judgment calls

- …

## 5. Questions for the lawyer

1. …

## 6. Implementation checklist

- [ ] …

## 7. Changelog

| Version | Date | Change | Reason / records |
|---|---|---|---|
| 0.1 | YYYY-MM-DD | First draft | LDR-0001–LDR-00NN |
