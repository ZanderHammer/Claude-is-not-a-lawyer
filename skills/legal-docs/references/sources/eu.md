# European Union: sources

EU law applies in all 27 member states (and, for most items, the EEA: Iceland, Liechtenstein,
Norway). Regulations apply directly. Directives are implemented by national law, so for
directives also cite the national implementation (`de.md`, `at.md`, `eu-member-states.md`).

**How to fetch EU law.** eur-lex.europa.eu answers automated clients with a JavaScript bot
challenge, so web-fetch tools usually get an empty page. Each entry therefore has:
- `URL`: the same official text served directly by the EU Publications Office ("Cellar"); a plain
  web fetch works. It is the version that was current at `Last verified`.
- `CELEX`: the document number. With a shell, run
  `python3 <skill-dir>/scripts/eurlex.py <celex> --latest --article <n> [--lang de]` to get the
  **newest consolidated version** of one article in any official language.
- `Cite as`: the EUR-Lex link to put in documents and defense reports (for humans).

Consolidated versions have CELEX numbers starting with `0` and ending in the consolidation date.
They are not legally binding (only the Official Journal is) but are what you read to know the
current state.

Entry format: see `references/workflow/source-policy.md`. `Last verified` is when the URL and
expected text were last checked by `scripts/check_sources.py` and by hand.

## Data protection and privacy

### EU-GDPR — General Data Protection Regulation (EU) 2016/679
- URL: https://publications.europa.eu/resource/cellar/5f2552c2-cc45-11e6-ad7c-01aa75ed71a1.0022.03/DOC_1
- CELEX: 02016R0679-20160504
- Cite as: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02016R0679-20160504
- Tier: T1
- Expect: Information to be provided where personal data are collected from the data subject
- Key provisions: Art. 3 (territorial scope, incl. non-EU controllers targeting the EU); Art. 4 (definitions); Art. 5 (principles); Art. 6 (lawful bases); Art. 7 (consent conditions); Art. 8 (children, information society services); Art. 9 (special categories); Art. 12 (transparent, concise, plain language); Art. 13/14 (mandatory privacy-notice content); Art. 15–22 (data subject rights); Art. 21 (right to object, must be presented separately); Art. 22 (automated decisions); Art. 26 (joint controllers); Art. 27 (EU representative of non-EU controllers); Art. 28 (processors and DPA content); Art. 30 (records of processing); Art. 32 (security); Art. 37–39 (DPO); Art. 44–49 (third-country transfers); Art. 77 (complaint to a supervisory authority)
- Used for: privacy-policy, cookie-policy, dpa, terms (account and data clauses)
- Notes: Consolidated version incorporating the 2016 corrigendum; no later consolidation existed at verification. Run `eurlex.py 32016R0679 --latest` to detect amendments (e.g. from "digital omnibus" proposals).
- Last verified: 2026-10-17

### EU-EPRIVACY — ePrivacy Directive 2002/58/EC (consolidated)
- URL: https://publications.europa.eu/resource/cellar/6def8269-d337-4373-83c1-8c57678fc93f.0006.03/DOC_3
- CELEX: 02002L0058-20091219
- Cite as: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02002L0058-20091219
- Tier: T1
- Expect: gaining of access to information already stored
- Key provisions: Art. 5(3) (storing or accessing information on terminal equipment, i.e. cookies, local storage, SDKs, fingerprinting: consent unless strictly necessary or solely for transmission); Art. 13 (unsolicited e-mail marketing, soft opt-in)
- Used for: cookie-policy, privacy-policy (newsletter, tracking)
- Notes: Directive, implemented nationally (DE: TDDDG § 25; AT: TKG 2021 § 165; FR: Loi Informatique et Libertés art. 82; …). Always cite the national rule too.
- Last verified: 2026-10-17

### EU-SCC-TRANSFERS — Standard contractual clauses for third-country transfers, Implementing Decision (EU) 2021/914
- URL: https://publications.europa.eu/resource/cellar/55862dbf-c72b-11eb-a925-01aa75ed71a1.0006.03/DOC_1
- CELEX: 32021D0914
- Cite as: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32021D0914
- Tier: T1
- Expect: standard contractual clauses for the transfer of personal data to third countries
- Key provisions: Annex (modules 1–4: C2C, C2P, P2P, P2C)
- Used for: privacy-policy (transfer safeguards section), dpa
- Last verified: 2026-10-17

### EU-SCC-ART28 — Standard contractual clauses between controllers and processors, Implementing Decision (EU) 2021/915
- URL: https://publications.europa.eu/resource/cellar/2b85eb9d-c72b-11eb-a925-01aa75ed71a1.0006.03/DOC_1
- CELEX: 32021D0915
- Cite as: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32021D0915
- Tier: T1
- Expect: standard contractual clauses between controllers and processors
- Key provisions: Annex (clauses 1–10, annexes I–IV: parties, description of processing, technical and organisational measures, sub-processors)
- Used for: dpa (a safe structural template for Art. 28(3) content)
- Last verified: 2026-10-17

### EU-DPF — EU–US Data Privacy Framework adequacy decision, Implementing Decision (EU) 2023/1795
- URL: https://publications.europa.eu/resource/cellar/abb0ba05-5750-11ee-9220-01aa75ed71a1.0006.03/DOC_1
- CELEX: 32023D1795
- Cite as: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023D1795
- Tier: T1
- Expect: EU-U.S. Data Privacy Framework
- Key provisions: Art. 1 (adequacy for US organisations on the DPF List)
- Used for: privacy-policy (transfers to US providers), dpa
- Notes: Covers only US recipients that are **self-certified** on the DPF List (`US-DPF-LIST`). A challenge (Latombe, General Court T-553/23 dismissed 3 Sept 2025; appeal C-703/25 P) was pending at the CJEU at last verification. **Check the current status live** and mention the risk in the defense report. Consider SCCs as a fallback.
- Last verified: 2026-10-17

### EU-ADEQUACY — European Commission: list of adequacy decisions
- URL: https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en
- Tier: T2
- Expect: adequacy
- Key provisions: Current list of countries with adequacy (e.g. CH, UK, JP, KR, CA (commercial), US (DPF only), …)
- Used for: privacy-policy (transfers), dpa
- Last verified: 2026-10-17

### EU-EDPB-CONSENT — EDPB Guidelines 05/2020 on consent under Regulation 2016/679
- URL: https://www.edpb.europa.eu/documents/guideline/guidelines-052020-on-consent-under-regulation-2016679_en
- Tier: T2
- Expect: Guidelines 05/2020 on consent
- Key provisions: Freely given (no "cookie walls" in general), specific, informed, unambiguous; scrolling is not consent; withdrawal as easy as giving
- Used for: cookie-policy, privacy-policy
- Last verified: 2026-10-17

### EU-EDPB-TRANSPARENCY — Article 29 WP Guidelines on transparency (WP260 rev.01), endorsed by the EDPB
- URL: https://ec.europa.eu/newsroom/article29/items/622227
- Tier: T2
- Expect: transparency
- Key provisions: Layered notices; plain language; Art. 13/14 checklist in the annex; no vague terms like "may", "some", "often"
- Used for: privacy-policy
- Last verified: 2026-10-17

### EU-EDPB-TERRITORIAL — EDPB Guidelines 3/2018 on the territorial scope of the GDPR (Art. 3)
- URL: https://www.edpb.europa.eu/documents/guideline/guidelines-32018-on-the-territorial-scope-of-the-gdpr-article-3-version-adopted_en
- Tier: T2
- Expect: territorial scope
- Key provisions: Establishment criterion; targeting criterion (language, currency, delivery, marketing); Art. 27 representative
- Used for: interview (jurisdiction decisions), privacy-policy
- Last verified: 2026-10-17

### EU-EDPB-5-3 — EDPB Guidelines 2/2023 on the technical scope of Art. 5(3) ePrivacy Directive
- URL: https://www.edpb.europa.eu/documents/guideline/guidelines-22023-on-technical-scope-of-art-53-of-eprivacy-directive_en
- Tier: T2
- Expect: Technical Scope of Art. 5(3)
- Key provisions: Covers pixels, tracking links, local storage, device fingerprinting, IoT/SDK access, not just cookies
- Used for: cookie-policy, codebase investigation
- Last verified: 2026-10-17

### EU-EDPB-CONTROLLER — EDPB Guidelines 07/2020 on the concepts of controller and processor
- URL: https://www.edpb.europa.eu/documents/guideline/guidelines-072020-on-the-concepts-of-controller-and-processor-in-the-gdpr_en
- Tier: T2
- Expect: concepts of controller and processor
- Key provisions: Who is controller/processor/joint controller; Art. 28 contract content explained clause by clause
- Used for: dpa, privacy-policy (recipients, joint controllers such as social plugins)
- Last verified: 2026-10-17

### EU-EDPB-MEMBERS — EDPB: list of national supervisory authorities
- URL: https://www.edpb.europa.eu/about-edpb/our-members_en
- Tier: T2
- Expect: members
- Key provisions: Name and contact of each national data protection authority (for the "right to lodge a complaint" clause)
- Used for: privacy-policy
- Last verified: 2026-10-17

## Consumer and contract law

### EU-CRD — Consumer Rights Directive 2011/83/EU (consolidated)
- URL: https://publications.europa.eu/resource/cellar/82067e60-3e52-11f1-814f-01aa75ed71a1.0006.03/DOC_1
- CELEX: 02011L0083-20260927
- Cite as: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02011L0083-20260927
- Tier: T1
- Expect: right of withdrawal
- Key provisions: Art. 6 (pre-contractual information for distance contracts); Art. 8(2) (order button "order with obligation to pay"); Art. 11a (electronic withdrawal function); Art. 9–16 (right of withdrawal, 14 days, exceptions in Art. 16); Annex I (A: model withdrawal instructions, B: model withdrawal form)
- Used for: terms, withdrawal-notice
- Notes: Consolidated version of 27 Sept 2026, including **Art. 11a (withdrawal function: "withdraw from contract here" / "confirm withdrawal")** inserted by `EU-DIR-2023-2673`, applicable from 19 June 2026.
- Last verified: 2026-10-17

### EU-DIR-2023-2673 — Directive (EU) 2023/2673 (financial services at a distance; adds the withdrawal function to the CRD)
- URL: https://publications.europa.eu/resource/cellar/ba0121b2-8d8f-11ee-8aa6-01aa75ed71a1.0006.03/DOC_1
- CELEX: 32023L2673
- Cite as: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023L2673
- Tier: T1
- Expect: withdrawal function
- Key provisions: Inserts Art. 11a into the CRD (withdrawal function on online interfaces); member states apply the measures from 19 June 2026 (transposition article)
- Used for: terms, withdrawal-notice (B2C distance contracts concluded via an online interface)
- Last verified: 2026-10-17

### EU-UCTD — Unfair Contract Terms Directive 93/13/EEC
- URL: https://publications.europa.eu/resource/cellar/ca4536e5-e274-11ec-a534-01aa75ed71a1.0007.02/DOC_1
- CELEX: 01993L0013-20220528
- Cite as: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:01993L0013-20220528
- Tier: T1
- Expect: unfair terms
- Key provisions: Art. 3 (unfairness test); Art. 5 (plain, intelligible language; ambiguity against the trader); Annex (indicative grey list)
- Used for: terms (B2C)
- Last verified: 2026-10-17

### EU-ECD — E-Commerce Directive 2000/31/EC
- URL: https://publications.europa.eu/resource/cellar/88aa5abc-f6a0-11ee-a251-01aa75ed71a1.0002.02/DOC_1
- CELEX: 02000L0031-20240217
- Cite as: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02000L0031-20240217
- Tier: T1
- Expect: General information to be provided
- Key provisions: Art. 5 (general information: name, address, e-mail, register, authority, VAT; basis of imprint duties); Art. 10–11 (information on contract steps, order confirmation)
- Used for: imprint, terms
- Notes: Consolidated version of 17 Feb 2024 (Arts. 12–15 deleted by the DSA). Implemented by DE-DDG § 5, AT-ECG § 5, UK-ECR2002 reg. 6, etc.
- Last verified: 2026-10-17

### EU-DCD — Digital Content Directive (EU) 2019/770
- URL: https://publications.europa.eu/resource/cellar/c426ed23-7c64-11e9-9f05-01aa75ed71a1.0006.03/DOC_1
- CELEX: 32019L0770
- Cite as: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32019L0770
- Tier: T1
- Expect: digital content
- Key provisions: Art. 3(1) (also applies when consumers "pay" with personal data); Art. 7–8 (conformity); Art. 19 (modifications of digital content); Art. 14 (remedies)
- Used for: terms (SaaS/apps for consumers)
- Last verified: 2026-10-17

### EU-SGD — Sale of Goods Directive (EU) 2019/771
- URL: https://publications.europa.eu/resource/cellar/9fb0f204-640a-11f1-9b18-01aa75ed71a1.0007.02/DOC_1
- CELEX: 02019L0771-20260731
- Cite as: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02019L0771-20260731
- Tier: T1
- Expect: sale of goods
- Key provisions: Art. 10 (two-year liability for lack of conformity); Art. 17 (commercial guarantees)
- Used for: terms (physical goods incl. goods with digital elements)
- Last verified: 2026-10-17

### EU-OMNIBUS — Directive (EU) 2019/2161 (better enforcement and modernisation of consumer rules)
- URL: https://publications.europa.eu/resource/cellar/eefb17ee-2173-11ea-95ab-01aa75ed71a1.0006.03/DOC_1
- CELEX: 32019L2161
- Cite as: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32019L2161
- Tier: T1
- Expect: better enforcement and modernisation
- Key provisions: Personalised pricing disclosure; reviews verification disclosure; marketplace information; price reduction rules
- Used for: terms, privacy-policy (personalised pricing)
- Last verified: 2026-10-17

### EU-GEOBLOCKING — Geo-blocking Regulation (EU) 2018/302
- URL: https://publications.europa.eu/resource/cellar/058372dc-1def-11e8-ac73-01aa75ed71a1.0006.03/DOC_1
- CELEX: 32018R0302
- Cite as: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32018R0302
- Tier: T1
- Expect: geo-blocking
- Key provisions: Art. 3–5 (no discrimination on nationality/residence for access, conditions, payment)
- Used for: terms (shipping/territory clauses)
- Last verified: 2026-10-17

### EU-ODR-REPEAL — Regulation (EU) 2024/3228 repealing the ODR Regulation 524/2013
- URL: https://publications.europa.eu/resource/cellar/cae74f0d-c64e-11ef-91ed-01aa75ed71a1.0006.03/DOC_1
- CELEX: 32024R3228
- Cite as: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R3228
- Tier: T1
- Expect: online dispute resolution
- Key provisions: Art. 1 (Regulation (EU) No 524/2013 repealed with effect from 20 July 2025); Art. 2 (ODR platform discontinued; complaint submission ended 20 March 2025). With the regulation, the duty to link to the ODR platform ended.
- Used for: imprint, terms: **do not** add the old "EU online dispute resolution platform" link. National ADR notices (e.g. DE-VSBG §§ 36–37) still apply.
- Last verified: 2026-10-17

## Platforms, accessibility, AI

### EU-DSA — Digital Services Act, Regulation (EU) 2022/2065
- URL: https://publications.europa.eu/resource/cellar/3ff67256-55c4-11ed-92ed-01aa75ed71a1.0006.03/DOC_1
- CELEX: 32022R2065
- Cite as: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2065
- Tier: T1
- Expect: terms and conditions
- Key provisions: Art. 11–12 (points of contact for authorities and users); Art. 14 (terms and conditions must describe content moderation, algorithmic decision-making, complaint handling; clear language; minors); Art. 16 (notice and action, for hosting services); Art. 17 (statement of reasons); Art. 20 (internal complaints, online platforms); Art. 24 (transparency reporting); Art. 26–28 (advertising transparency, recommender systems, minors); Art. 30 (trader traceability for marketplaces). Micro/small enterprise exemptions in Art. 19 and 29.
- Used for: terms (any service hosting user content), imprint (contact points)
- Last verified: 2026-10-17

### EU-EAA — European Accessibility Act, Directive (EU) 2019/882
- URL: https://publications.europa.eu/resource/cellar/6eb3ceb5-8905-11e9-9369-01aa75ed71a1.0006.03/DOC_1
- CELEX: 32019L0882
- Cite as: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32019L0882
- Tier: T1
- Expect: accessibility requirements for products and services
- Key provisions: Art. 4 and Annex I (requirements, incl. e-commerce services); Art. 4(5) (microenterprises providing services are exempt); Art. 13(2) + Annex V (service providers must publish information explaining how the service meets the accessibility requirements, typically in the terms or a separate accessibility statement); Art. 32 (transitional); applies since 28 June 2025
- Used for: terms (accessibility information for consumer e-commerce services); flag the need for an accessibility statement
- Notes: National implementations: DE-BFSG, AT-BAFG.
- Last verified: 2026-10-17

### EU-AI-ACT — Artificial Intelligence Act, Regulation (EU) 2024/1689
- URL: https://publications.europa.eu/resource/cellar/b1730fb2-8f1c-11f1-9262-01aa75ed71a1.0001.03/DOC_1
- CELEX: 02024R1689-20260727
- Cite as: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02024R1689-20260727
- Tier: T1
- Expect: Transparency obligations for providers and deployers of certain AI systems
- Key provisions: Art. 50 (inform people that they interact with an AI system; machine-readable marking of AI-generated content; deep fakes and AI-generated public-interest text); Art. 113 (application: generally 2 Aug 2026; high-risk rules postponed to 2027/2028 by the 2026 amendment); Art. 4 (AI literacy); Art. 5 (prohibited practices)
- Used for: terms, privacy-policy (AI features)
- Notes: Consolidated version of 27 July 2026 (amendment "M1"). Check Art. 111 and 113 for transitional rules before stating dates.
- Last verified: 2026-10-17
