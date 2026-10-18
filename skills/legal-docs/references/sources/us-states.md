# United States (states): sources

About twenty states have **comprehensive consumer privacy laws**. Most follow the same pattern
(Virginia/Colorado model): applicability thresholds (number of state residents' data processed per
year, share of revenue from selling data), a privacy notice with fixed content, rights to access /
correct / delete / port, opt-outs for targeted advertising, sale and profiling, consent for
sensitive data, and data protection assessments. California (CCPA/CPRA) is the outlier with the
most detailed rules.

**This list changes every year.** Before drafting:
1. Check `US-IAPP-TRACKER` for new laws, amendments and effective dates (T3, orientation only).
2. For every state the user has relevant users in (interview Q17), open the official text below
   and check the **applicability thresholds and the effective date in the statute itself**. Many
   small businesses fall below the thresholds; record that analysis in a decision record.
3. Texas, Nebraska (and partly others) apply to most businesses that are not "small businesses"
   under SBA definitions, with no volume threshold. Do not assume thresholds protect the user.

Several state sites block automated clients (`Bot-protected`) or are JavaScript apps. Use the
listed alternative (enrolled bill text, Attorney General page) and say which one you used.

## California

### US-CA-CCPA — California Consumer Privacy Act as amended by the CPRA, Civ. Code § 1798.100 ff.
- URL: https://cppa.ca.gov/pdf/20260101_ccpa_statute.pdf
- Tier: T1
- Also: https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?division=3.&part=4.&lawCode=CIV&title=1.81.5
- Bot-protected: yes
- Key provisions: § 1798.100 (notice at collection); § 1798.105–.125 (rights to delete, correct, know, opt out of sale/sharing, limit use of sensitive PI, non-discrimination); § 1798.130 (privacy policy content and update every 12 months; methods for requests); § 1798.135 ("Do Not Sell or Share My Personal Information" / "Limit the Use of My Sensitive Personal Information" links, opt-out preference signals); § 1798.140 (definitions incl. "business" thresholds, "sale", "sharing", "sensitive personal information")
- Used for: privacy-policy (California section / CCPA notice), cookie-policy (sharing for cross-context behavioural advertising)
- Notes: The URL is the statute as published by the California Privacy Protection Agency (effective 1 Jan 2026), which was read. leginfo (the legislature's site) is behind a Cloudflare bot challenge. Monetary thresholds are CPI-adjusted (see `US-CA-CPPA-REGS`).
- Verification: automated: CPPA PDF statute read; leginfo blocked
- Last verified: 2026-10-18

### US-CA-CPPA-REGS — CCPA Regulations, Cal. Code Regs. tit. 11 § 7000 ff. (CPPA)
- URL: https://cppa.ca.gov/regulations/
- Tier: T1
- Expect: California Consumer Privacy Act
- Also: https://cppa.ca.gov/regulations/pdf/ccpa_statute_eff_20260101.pdf https://cppa.ca.gov/regulations/cpi_adjustment.html
- Key provisions: § 7011 (privacy policy content); § 7012 (notice at collection); § 7013 (notice of right to opt out); § 7025 (opt-out preference signals, e.g. Global Privacy Control); § 7004 (methods for requests and consent: symmetry in choice, no dark patterns); newer rules on risk assessments, cybersecurity audits and automated decision-making technology (check effective dates)
- Used for: privacy-policy, cookie-policy
- Notes: The PDF linked as "CCPA Regulations (Effective January 1, 2026)" on the CPPA page is the `Also` PDF (the file name says "statute", the content is the regulations).
- Last verified: 2026-10-17

### US-CA-AG-CCPA — California Attorney General: CCPA overview
- URL: https://oag.ca.gov/privacy/ccpa
- Tier: T2
- Expect: California Consumer Privacy Act
- Used for: privacy-policy (plain-language explanation of rights and business duties)
- Last verified: 2026-10-17

### US-CA-CALOPPA — California Online Privacy Protection Act, Bus. & Prof. Code §§ 22575–22579
- URL: https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=BPC&division=8.&title=&part=&chapter=22.&article=
- Tier: T1
- Bot-protected: yes
- Key provisions: § 22575(b) (privacy policy must list categories of PII collected and third parties shared with, how users can review/request changes, how users are notified of changes, effective date, **how the site responds to "Do Not Track" signals**, whether third parties track across sites)
- Used for: privacy-policy (any commercial website or online service collecting PII from California residents, **no size threshold**)
- Notes: leginfo.legislature.ca.gov is behind a Cloudflare bot challenge that no tool here passed (plain fetch, web-fetch tool, headless browser), so the statute was **not read from the official site**. The California Attorney General page (`Also`) confirms that CalOPPA, Bus. & Prof. Code §§ 22575–22579, requires commercial sites collecting PII from Californians to conspicuously post a privacy policy. Details of § 22575(b), including the Do-Not-Track disclosure added by AB 370 (2013), were confirmed only on a third-party mirror (california.public.law). Ask the user to open the link, or follow the fallback procedure and label the clause.
- Verification: official AG page read; statute text from a non-official mirror only (leginfo blocked)
- Also: https://oag.ca.gov/privacy/facts/online-privacy/privacy-policy
- Last verified: 2026-10-18

### US-CA-ARL — California Automatic Renewal Law, Bus. & Prof. Code §§ 17600–17606
- URL: https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=BPC&division=7.&title=&part=3.&chapter=1.&article=9.
- Tier: T1
- Bot-protected: yes
- Key provisions: Clear and conspicuous offer terms before the subscription; affirmative consent; acknowledgement with cancellation info; online cancellation ("click to cancel"); notices before price changes and before free trials convert
- Used for: terms (subscriptions with California consumers)
- Notes: leginfo is blocked as for `US-CA-CALOPPA`, so the statute was **not read**. Secondary sources report that AB 390 (effective 1 July 2022) amended § 17602: offer terms must be clear and conspicuous before purchase, consumers who sign up online must be able to cancel online, and reminder notices are required before renewal and before free trials convert. Read the current text before drafting subscription clauses. Many other states have similar laws (check the tracker / state AG pages).
- Verification: unverified against official text: leginfo blocked; secondary sources only
- Last verified: 2026-10-18

## Other comprehensive state privacy laws

Official texts (legislature or code sites). The column "Notes" holds facts confirmed at
verification; everything else (thresholds, exemptions, effective dates of the older laws) must be
read from the text.

### US-VA-VCDPA — Virginia Consumer Data Protection Act, Va. Code § 59.1-575 ff.
- URL: https://law.lis.virginia.gov/vacodefull/title59.1/chapter53/
- Tier: T1
- Expect: Consumer Data Protection Act
- Key provisions: § 59.1-577 (consumer rights); § 59.1-578 (controller duties incl. the privacy notice content)
- Used for: privacy-policy (US state section)
- Last verified: 2026-10-17

### US-CO-CPA — Colorado Privacy Act, C.R.S. § 6-1-1301 ff. (+ CPA Rules, 4 CCR 904-3)
- URL: https://coag.gov/resources/colorado-privacy-act/
- Tier: T2
- Expect: Colorado Privacy Act
- Key provisions: Statute and the Attorney General's CPA Rules (privacy notice content, universal opt-out mechanism recognition, consent, refreshing consent). The AG page links to the statute and rules.
- Used for: privacy-policy
- Notes: Colorado's official statutes are published through a third-party publisher. Use the AG page and the rules it links to.
- Last verified: 2026-10-17

### US-CT-CTDPA — Connecticut Data Privacy Act, Conn. Gen. Stat. § 42-515 ff.
- URL: https://portal.ct.gov/ag/sections/privacy/the-connecticut-data-privacy-act
- Tier: T2
- Expect: Connecticut Data Privacy Act
- Also: https://www.cga.ct.gov/current/pub/chap_743jj.htm
- Bot-protected: yes
- Key provisions: Privacy notice content, rights, opt-outs, minors' data. Secondary sources report amendments effective 1 July 2026; check the current text
- Used for: privacy-policy
- Notes: The legislature page (`Also`, cga.ct.gov) sends an incomplete TLS certificate chain, which the verification environment refuses, so the statute was **not read**. The Attorney General page (`URL`) was read. One vendor checklist reports that Public Act 25-113 amends § 42-520 from 1 July 2026 (e.g. a statement on whether personal data is used to train large language models); that is **unverified**, so read the current text.
- Verification: official AG page read; legislature statute page unreachable
- Last verified: 2026-10-18

### US-UT-UCPA — Utah Consumer Privacy Act, Utah Code Title 13 Ch. 61
- URL: https://le.utah.gov/xcode/Title13/Chapter61/13-61.html
- Tier: T1
- Expect: 13-61
- Key provisions: Privacy notice duties; high applicability thresholds (read the applicability section)
- Used for: privacy-policy
- Notes: The code page loads its text with JavaScript. A web-fetch tool may show only the table of contents; open the section pages linked there.
- Last verified: 2026-10-17

### US-TX-TDPSA — Texas Data Privacy and Security Act, Bus. & Com. Code Ch. 541
- URL: https://capitol.texas.gov/tlodocs/88R/billtext/html/HB00004F.htm
- Tier: T1
- Expect: data privacy
- Also: https://statutes.capitol.texas.gov/Docs/BC/htm/BC.541.htm https://www.texasattorneygeneral.gov/consumer-protection/file-consumer-complaint/consumer-privacy-rights/texas-data-privacy-and-security-act
- Key provisions: § 541.102 (privacy notice; **selling sensitive data requires the exact notice "NOTICE: We may sell your sensitive personal data."**, biometric data has its own wording); § 541.002 (applicability: no revenue/volume threshold; excludes small businesses as defined by the US SBA, except § 541.107 (no sale of sensitive data without consent) still applies to them)
- Used for: privacy-policy
- Notes: The URL is the enrolled bill (HB 4, 2023). The codified chapter (`Also`, JavaScript page) may include later amendments.
- Last verified: 2026-10-17

### US-OR-OCPA — Oregon Consumer Privacy Act, ORS 646A.570–646A.589
- URL: https://www.oregonlegislature.gov/bills_laws/ors/ors646a.html
- Tier: T1
- Expect: 646A.570
- Also: https://www.doj.state.or.us/consumer-protection/id-theft-data-breaches/privacy/
- Used for: privacy-policy
- Last verified: 2026-10-17

### US-MT-MCDPA — Montana Consumer Data Privacy Act, MCA 30-14-2801 ff.
- URL: https://mca.legmt.gov/bills/mca/title_0300/chapter_0140/part_0280/sections_index.html
- Tier: T1
- Expect: Consumer Data Privacy
- Used for: privacy-policy
- Last verified: 2026-10-17

### US-IA-ICDPA — Iowa Consumer Data Protection Act, Iowa Code ch. 715D
- URL: https://www.legis.iowa.gov/docs/code/715D.pdf
- Tier: T1
- Used for: privacy-policy
- Last verified: 2026-10-17

### US-DE-DPDPA — Delaware Personal Data Privacy Act, 6 Del. C. ch. 12D
- URL: https://delcode.delaware.gov/title6/c012d/index.html
- Tier: T1
- Expect: Delaware
- Used for: privacy-policy (note: lower thresholds than most states)
- Last verified: 2026-10-17

### US-NH-PRIVACY — New Hampshire, RSA ch. 507-H (Expectation of Privacy)
- URL: https://gc.nh.gov/rsa/html/LII/507-H/507-H-mrg.htm
- Tier: T1
- Expect: 507-H
- Bot-protected: yes
- Used for: privacy-policy
- Notes: The old gencourt.state.nh.us address redirects here. The site blocks this environment's IP for direct fetches; the web-fetch tool and GitHub's runners could read it. Check the thresholds in the text before relying on this summary.
- Verification: web-fetch tool: statute text read; direct fetches get "403 Web Page Blocked" from this environment
- Key provisions: § 507-H:1 definitions; § 507-H:2 applicability (at least 35,000 consumers per year, or 10,000 with over 25% of gross revenue from selling personal data, per the web-fetch summary); § 507-H:4 consumer rights (access, correct, delete, port, opt out of targeted advertising, sale, profiling) and appeal; § 507-H:6 controller duties incl. privacy notice and honouring opt-out preference signals; § 507-H:8 data protection assessments; attorney general enforces, no private right of action
- Last verified: 2026-10-18

### US-NJ-NJDPA — New Jersey Data Privacy Act, P.L. 2023, c. 266 (N.J.S.A. 56:8-166.4 ff.)
- URL: https://pub.njleg.gov/bills/2022/PL23/266_.HTM
- Tier: T1
- Expect: personal data
- Key provisions: Privacy notice; rights; opt-outs; Division of Consumer Affairs rulemaking (check for final rules)
- Used for: privacy-policy
- Last verified: 2026-10-17

### US-TN-TIPA — Tennessee Information Protection Act (Public Chapter 408 of 2023, HB 1181)
- URL: https://www.capitol.tn.gov/Bills/113/Bill/HB1181.pdf
- Tier: T1
- Key provisions: High revenue threshold; affirmative defence for a privacy program aligned with the NIST Privacy Framework
- Used for: privacy-policy
- Last verified: 2026-10-17

### US-MN-MCDPA — Minnesota Consumer Data Privacy Act, Minn. Stat. ch. 325M
- URL: https://www.revisor.mn.gov/statutes/cite/325M
- Tier: T1
- Expect: 325M
- Used for: privacy-policy
- Last verified: 2026-10-17

### US-MD-MODPA — Maryland Online Data Privacy Act, Com. Law § 14-4701 ff.
- URL: https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gcl&section=14-4701&enactments=false
- Tier: T1
- Expect: Statute Text
- Key provisions: Strict data minimisation ("strictly necessary" for sensitive data); ban on selling sensitive data
- Used for: privacy-policy
- Notes: JavaScript page; a web-fetch tool returned the definitions section at verification. Following sections: change `section=14-4702`, etc.
- Last verified: 2026-10-17

### US-IN-ICDPA — Indiana Consumer Data Protection Act (SB 5 of 2023, IC 24-15), effective 1 Jan 2026
- URL: https://secure.in.gov/attorneygeneral/files/Indiana-Consumer-Data-Protection-Consumer-Bill-of-Rights_Web.pdf
- Tier: T2
- Also: https://iga.in.gov/legislative/2023/bills/senate/5
- Used for: privacy-policy
- Notes: The Attorney General's consumer guide. The official code (IC 24-15) and the bill page on iga.in.gov are a JavaScript app that plain fetches cannot read. Ask the user to open the bill page, or treat this as a case for the fallback procedure.
- Last verified: 2026-10-17

### US-KY-KCDPA — Kentucky Consumer Data Protection Act (HB 15 of 2024, KRS 367.3611 ff.), effective 1 Jan 2026
- URL: https://apps.legislature.ky.gov/record/24rs/hb15.html
- Tier: T1
- Expect: HB 15
- Used for: privacy-policy
- Notes: Bill record page with links to the enacted text; amended in 2025 (HB 473) before taking effect.
- Last verified: 2026-10-17

### US-RI-RIDTPPA — Rhode Island Data Transparency and Privacy Protection Act, R.I. Gen. Laws ch. 6-48.1, effective 1 Jan 2026
- URL: https://webserver.rilegislature.gov/Statutes/TITLE6/6-48.1/INDEX.htm
- Tier: T1
- Key provisions: § 6-48.1-3 (any commercial website or ISP doing business in RI or with RI customers must designate a controller and disclose its information sharing practices, regardless of the comprehensive-law thresholds)
- Used for: privacy-policy
- Last verified: 2026-10-17

### US-NE-NDPA — Nebraska Data Privacy Act, Neb. Rev. Stat. § 87-1101 ff.
- URL: https://nebraskalegislature.gov/laws/statutes.php?statute=87-1101
- Tier: T1
- Expect: 87-1101
- Key provisions: Read the applicability section (reported to follow the Texas model without volume thresholds)
- Used for: privacy-policy
- Last verified: 2026-10-17

### US-OK-OCDPA — Oklahoma consumer data privacy law (SB 546, 2026), effective 1 Jan 2027
- URL: https://www.oklegislature.gov/cf_pdf/2025-26%20ENR/SB/SB546%20ENR.PDF
- Tier: T1
- Used for: privacy-policy (prepare now if Oklahoma users matter)
- Notes: Enrolled bill, signed March 2026.
- Last verified: 2026-10-17

### US-AL-APDPA — Alabama Personal Data Protection Act (HB 351, 2026), effective 1 May 2027
- URL: https://alison.legislature.state.al.us/files/pdf/SearchableInstruments/2026RS/HB351-enr.pdf
- Tier: T1
- Used for: privacy-policy (prepare now if Alabama users matter)
- Notes: Enrolled bill, signed April 2026.
- Last verified: 2026-10-17

## Sector laws with broad reach

### US-WA-MHMDA — Washington My Health My Data Act, RCW ch. 19.373
- URL: https://app.leg.wa.gov/RCW/default.aspx?cite=19.373
- Tier: T1
- Expect: 19.373
- Also: https://www.atg.wa.gov/protecting-washingtonians-personal-health-data-and-privacy
- Key provisions: Separate "consumer health data privacy policy" with a **homepage link**; consent for collection and separate consent for sharing; written authorisation for sale; private right of action. "Consumer health data" is defined very broadly (can include fitness, diet, location near health facilities, inferences)
- Used for: privacy-policy (any service possibly touching health-related data of WA consumers) → red flag check
- Notes: Nevada (SB 370) and Connecticut have similar consumer health data rules.
- Last verified: 2026-10-17

## Trackers

### US-IAPP-TRACKER — IAPP: US State Privacy Legislation Tracker
- URL: https://iapp.org/resources/article/us-state-privacy-legislation-tracker/
- Tier: T3
- Expect: State
- Key provisions: Which states have enacted laws, effective dates, map and chart (PDF). Orientation only; confirm in the official text.
- Used for: interview (state list), source maintenance
- Last verified: 2026-10-17
