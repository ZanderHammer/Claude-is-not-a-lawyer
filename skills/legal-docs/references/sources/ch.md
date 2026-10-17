# Switzerland: sources

Swiss federal law is published on **fedlex.admin.ch** (Systematische Rechtssammlung, SR). Official
languages: German, French, Italian (English translations are unofficial and may lag). Switzerland
is not in the EU. The GDPR does not apply to Swiss processing as such, but often applies in
parallel when Swiss companies target EU users. The EU recognises Switzerland as adequate, and
Switzerland recognises the EU/EEA.

**fedlex is a JavaScript app.** The `URL` entries below point to the static HTML of the
consolidated version that was current at verification. Before relying on one, run:

```
python3 <skill-dir>/scripts/fedlex_latest.py <eli> [--lang de|fr|it|en]
```

If it prints a newer consolidation date than the one in the URL, use the URL it prints.

## Data protection

### CH-DSG — Bundesgesetz über den Datenschutz (DSG / revDSG), SR 235.1
- URL: https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/491/20250707/de/html/fedlex-data-admin-ch-eli-cc-2022-491-20250707-de-html-1.html
- Tier: T1
- Expect: Informationspflicht bei der Beschaffung von Personendaten
- ELI: eli/cc/2022/491
- Key provisions: Art. 3 (territorial scope: effects in Switzerland); Art. 5 (definitions); Art. 6 (principles); Art. 14–15 (Swiss representative of foreign controllers); Art. 16–17 (disclosure abroad: adequacy list in DSV Annex 1, safeguards); Art. 19 (duty to inform: identity and contact, purpose, recipients, countries abroad and safeguards); Art. 21 (automated individual decisions); Art. 25 (right of access); Art. 60 (fines up to CHF 250,000 for **individuals** responsible, e.g. for wilful breach of information duties)
- Used for: privacy-policy
- Notes: In force since 1 Sept 2023. Swiss law has no general requirement of a legal basis like GDPR Art. 6, but justification is needed for certain processing (Art. 30–31). Consent is not the default model.
- Last verified: 2026-10-17

### CH-DSV — Datenschutzverordnung (DSV), SR 235.11
- URL: https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/568/20251201/de/html/fedlex-data-admin-ch-eli-cc-2022-568-20251201-de-html-1.html
- Tier: T1
- Expect: Datenschutzverordnung
- ELI: eli/cc/2022/568
- Key provisions: Art. 1–5 (data security); Art. 8 + Anhang 1 (countries with adequate protection; the US only for organisations certified under the Swiss–US Data Privacy Framework); Art. 13 (form of information: precise, transparent, understandable, easily accessible)
- Used for: privacy-policy (transfers), dpa
- Last verified: 2026-10-17

### CH-EDOEB — Eidgenössischer Datenschutz- und Öffentlichkeitsbeauftragter (FDPIC)
- URL: https://www.edoeb.admin.ch/de/datenschutz
- Tier: T2
- Expect: Datenschutz
- Key provisions: Guidance on the revDSG (information duties, cookies and tracking, transfers abroad); contact for the supervisory authority
- Used for: privacy-policy, cookie-policy
- Notes: Swiss law has no cookie-specific consent rule like ePrivacy Art. 5(3). Transparency and the processing principles still apply; check FDPIC guidance on tracking.
- Last verified: 2026-10-17

## Contracts, unfair competition, e-commerce

### CH-UWG — Bundesgesetz gegen den unlauteren Wettbewerb (UWG), SR 241
- URL: https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1988/223_223_223/20250101/de/html/fedlex-data-admin-ch-eli-cc-1988-223_223_223-20250101-de-html-1.html
- Tier: T1
- Expect: Verwendung missbräuchlicher Geschäftsbedingungen
- ELI: eli/cc/1988/223_223_223
- Key provisions: Art. 3 Abs. 1 lit. s (e-commerce: clear and complete identity and contact address incl. e-mail; technical steps to contract; means to correct input errors; immediate electronic order confirmation; this is the Swiss "imprint" duty); Art. 3 Abs. 1 lit. o (mass advertising e-mail needs consent, sender identification, easy opt-out); Art. 8 (unfair general terms against consumers)
- Used for: imprint, terms, privacy-policy (newsletter)
- Last verified: 2026-10-17

### CH-OR — Obligationenrecht (OR), SR 220
- URL: https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/27/317_321_377/20261001/de/html/fedlex-data-admin-ch-eli-cc-27-317_321_377-20261001-de-html-1.html
- Tier: T1
- Expect: Obligationenrecht
- ELI: eli/cc/27/317_321_377
- Key provisions: Art. 1 ff. (contract formation); Art. 40a ff. (withdrawal right only for doorstep and similar sales); Art. 100 (advance exclusion of liability for intent or gross negligence is void); Art. 197 ff. (warranty in sales)
- Used for: terms
- Notes: Switzerland has **no general statutory right of withdrawal** for online purchases (Art. 40a ff. cover doorstep-type sales, not distance contracts; verify against the current text). Do not copy EU withdrawal clauses into Swiss B2C terms unless offered voluntarily.
- Last verified: 2026-10-17
