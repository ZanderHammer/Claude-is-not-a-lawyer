# United States (federal): sources

There is **no general federal privacy law** in the US. Federal law covers specific areas (children,
e-mail marketing, subscriptions, copyright), and the FTC polices unfair or deceptive practices,
which includes breaking the promises in your own privacy policy. Comprehensive privacy rules come
from the states (`us-states.md`).

URL patterns:
- US Code (official, GPO): `https://www.govinfo.gov/link/uscode/<title>/<section>?type=usc&year=mostrecent&link-type=html`
  (redirects to the most recent annual edition; check the "Office of the Law Revision Counsel"
  site `uscode.house.gov` for later amendments when it is reachable).
- Code of Federal Regulations: the annual edition on govinfo
  (`https://www.govinfo.gov/content/pkg/CFR-<year>-title<t>-vol<v>/xml/CFR-<year>-title<t>-vol<v>-part<p>.xml`).
  eCFR (`ecfr.gov`) is more current but blocks automated clients.
- FTC guidance (ftc.gov) blocks some automated clients (`Bot-protected`); a normal web-fetch tool
  usually works.

### US-FTC-ACT-5 — FTC Act § 5, 15 U.S.C. § 45 (unfair or deceptive acts or practices)
- URL: https://www.govinfo.gov/link/uscode/15/45?type=usc&year=mostrecent&link-type=html
- Tier: T1
- Expect: unfair or deceptive acts or practices in or affecting commerce
- Key provisions: § 45(a)(1) (unfair or deceptive practices unlawful). Basis for FTC enforcement against misleading privacy policies, dark patterns, broken security promises
- Used for: privacy-policy (every statement must be true and kept), terms
- Last verified: 2026-10-17

### US-COPPA — Children's Online Privacy Protection Act, 15 U.S.C. §§ 6501–6506
- URL: https://www.govinfo.gov/link/uscode/15/6502?type=usc&year=mostrecent&link-type=html
- Tier: T1
- Expect: notice on the website
- Key provisions: § 6501 (definitions: child = under 13); § 6502(b)(1)(A) (notice and verifiable parental consent)
- Used for: privacy-policy (services directed to children under 13, or with actual knowledge)
- Last verified: 2026-10-17

### US-COPPA-RULE — COPPA Rule, 16 C.F.R. Part 312 (CFR edition of 1 Jan 2026, incl. 2025 amendments)
- URL: https://www.govinfo.gov/content/pkg/CFR-2026-title16-vol1/xml/CFR-2026-title16-vol1-part312.xml
- Tier: T1
- Expect: CHILDREN'S ONLINE PRIVACY PROTECTION RULE
- Also: https://www.govinfo.gov/content/pkg/FR-2025-04-22/html/2025-05904.htm
- Key provisions: § 312.2 (definitions, expanded personal information incl. biometric identifiers); § 312.4 (direct notice to parents and online notice content); § 312.5 (parental consent, separate consent for disclosure to third parties); § 312.8 (security program); § 312.10 (written data retention policy)
- Used for: privacy-policy
- Notes: The amended rule (FR 2025-04-22) applied from 23 June 2025, compliance date 22 April 2026 for most provisions. The `Also` URL is the Federal Register final rule with the FTC's explanation (T2-quality reasoning).
- Last verified: 2026-10-17

### US-FTC-COPPA-FAQ — FTC: Complying with COPPA, Frequently Asked Questions
- URL: https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions
- Tier: T2
- Bot-protected: yes
- Expect: COPPA
- Key provisions: "Directed to children" factors, mixed-audience services, notice content
- Used for: privacy-policy
- Verification: web-fetch tool: page title confirmed; ftc.gov answers scripts and headless browsers with a fake 404 / "abusive automated request" page
- Notes: Open with a web-fetch tool or a normal browser. The statute and rule entries above cover the legal text.
- Last verified: 2026-10-18

### US-CAN-SPAM — CAN-SPAM Act, 15 U.S.C. §§ 7701–7713, and 16 C.F.R. Part 316
- URL: https://www.govinfo.gov/link/uscode/15/7704?type=usc&year=mostrecent&link-type=html
- Tier: T1
- Expect: valid physical postal address
- Also: https://www.govinfo.gov/content/pkg/CFR-2026-title16-vol1/xml/CFR-2026-title16-vol1-part316.xml
- Key provisions: § 7704(a)(3) (functioning opt-out, honoured within 10 business days); § 7704(a)(5) (identification as advertisement, opt-out notice, valid physical postal address)
- Used for: privacy-policy (marketing e-mails), terms
- Notes: Opt-out regime (no prior consent needed), unlike the EU/UK. When both apply, design for the stricter one.
- Last verified: 2026-10-17

### US-FTC-CAN-SPAM-GUIDE — FTC: CAN-SPAM Act, A Compliance Guide for Business
- URL: https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business
- Tier: T2
- Bot-protected: yes
- Expect: CAN-SPAM
- Used for: privacy-policy (newsletter section)
- Verification: web-fetch tool: page title confirmed; ftc.gov answers scripts and headless browsers with a fake 404 / "abusive automated request" page
- Notes: Open with a web-fetch tool or a normal browser. The statute and rule entries above cover the legal text.
- Last verified: 2026-10-18

### US-ROSCA — Restore Online Shoppers' Confidence Act, 15 U.S.C. §§ 8401–8405
- URL: https://www.govinfo.gov/link/uscode/15/8403?type=usc&year=mostrecent&link-type=html
- Tier: T1
- Expect: simple mechanisms
- Key provisions: § 8403 (negative option online: clear and conspicuous disclosure of material terms before billing info, express informed consent before charging, simple mechanism to stop recurring charges)
- Used for: terms (subscriptions, free trials, auto-renewal)
- Notes: The FTC's 2024 "click-to-cancel" amendments to the Negative Option Rule (16 C.F.R. 425) were **vacated** by the 8th Circuit on 8 July 2025. The FTC started new rulemaking in 2026. ROSCA, FTC Act § 5 and state auto-renewal laws (e.g. `US-CA-ARL`) still apply. Check the current status live.
- Last verified: 2026-10-17

### US-DMCA-512 — DMCA safe harbor, 17 U.S.C. § 512
- URL: https://www.govinfo.gov/link/uscode/17/512?type=usc&year=mostrecent&link-type=html
- Tier: T1
- Expect: designated agent
- Also: https://www.copyright.gov/dmca-directory/
- Key provisions: § 512(c)(2) (designated agent, contact info on the website and registered with the Copyright Office); § 512(c)(3) (notice elements); § 512(g) (counter-notice); § 512(i)(1)(A) (repeat infringer policy, informed to users)
- Used for: terms (services hosting user content)
- Notes: The designated agent registration in the Copyright Office directory must be renewed every three years (check the directory page).
- Last verified: 2026-10-17

### US-ESIGN — E-SIGN Act, 15 U.S.C. § 7001
- URL: https://www.govinfo.gov/link/uscode/15/7001?type=usc&year=mostrecent&link-type=html
- Tier: T1
- Expect: consumer disclosures
- Key provisions: § 7001(a) (validity of electronic contracts and signatures); § 7001(c) (consumer consent before providing legally required information electronically)
- Used for: terms (clickwrap acceptance, electronic notices)
- Last verified: 2026-10-17

### US-DPF-LIST — Data Privacy Framework program: participant list and principles (US Department of Commerce)
- URL: https://www.dataprivacyframework.gov/
- Tier: T2
- Expect: Data Privacy Framework
- Key provisions: Check whether a US recipient is certified (EU–US DPF, UK extension, Swiss–US DPF). The list page is a JavaScript app; search for the company by name in a browser if a fetch shows nothing.
- Used for: privacy-policy (transfers), dpa
- Last verified: 2026-10-17
