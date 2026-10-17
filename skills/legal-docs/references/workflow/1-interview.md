# Phase 1: The interview

Interview the user about every fact the documents depend on, the way a careful lawyer would on a
first call. Keep going until you reach a shared understanding. Stop at shared understanding, not
when you get bored.

## Interview rules

- **One question at a time.** Wait for the answer before asking the next one. Never send a
  questionnaire.
- **Always give your recommended answer** and one line on why the question matters, e.g.:
  > **Q7. Do you sell to consumers, businesses, or both?**
  > My recommendation, based on what I've seen so far: *both*, because the pricing page offers a
  > personal plan. This matters because consumer sales trigger withdrawal rights and stricter
  > rules for terms (EU-CRD, DE-BGB-AGB § 309).
- **Look it up instead of asking** whenever the repo can answer: the company name in
  `package.json` or footer components, languages from i18n files, the domain from config, the
  payment provider from dependencies. Then ask the user only to *confirm* what you found ("I found
  X in `src/footer.tsx:12`. Is that correct and current?").
- **Walk the decision tree.** Each answer opens or closes branches (see below). Go depth-first:
  finish a branch before starting the next. Track open branches visibly ("Still open: payments,
  minors, newsletter").
- **Challenge vague answers.** "We don't collect data" is almost never true for a web app.
  "Worldwide" is not a jurisdiction. "Like Stripe's terms" is not a decision. Push for specifics,
  politely and relentlessly.
- **Flag consequences as you learn them.** When an answer triggers an obligation ("non-EU company
  targeting EU consumers → you likely need an EU representative under GDPR Art. 27"), say so,
  name the source ID, and note that you will verify it against the text in phase 4.
- **Do not give legal conclusions as facts.** Say "this likely triggers…, to be verified against
  the source and by your lawyer".
- **Record as you go.** After each topic is settled, write or update its LDR (phase 2) and show
  the user a one-line summary. Mark anything the user doesn't know as an `open question`.
- **Personal data in the repo.** Records hold names and addresses that will appear in the imprint
  anyway, but warn the user before writing private details (e.g. a sole trader's home address)
  into a public repository, and offer to keep that record outside version control.

## Question tree

Ask in this order. Skip what the repo already answered (confirm instead). Branches marked ⤷ only
open when the condition holds.

### A. Project and documents
1. What is the product (website, SaaS, mobile app, desktop app, API, browser extension, open-source
   library)? Which parts are public-facing?
2. Which documents do you want? Offer the list (privacy policy, terms, imprint, cookie policy,
   withdrawal notice, DPA). Tell them which ones you expect they'll *need* once the interview is
   done. The final list is decided in phase 4.
3. Do legal documents already exist (in the repo, on the website, from a generator)? ⤷ yes: get
   them; they become input and the defense report must explain every deviation.
4. In which languages must the documents exist? (Check i18n setup first.) Which version is
   binding if they differ?

### B. Who is responsible (controller / provider / contracting party)
5. Legal entity: exact registered name and legal form (GmbH, UG, e.K., sole trader, Ltd, LLC,
   Inc., AG, e.V., natural person / hobby project).
6. Registered address (no P.O. box for imprints in DE/AT). Different operational address?
7. Representatives: managing directors / directors / owners (names as registered).
8. Register: court/registry and number (Handelsregister, Firmenbuch, Companies House,
   Handelsregister CH / UID, state of incorporation).
9. VAT ID (USt-IdNr., UID, VAT number). ⤷ DE/AT: Wirtschafts-ID, if any.
10. Contact channels: e-mail, phone, contact form (DE-DDG § 5 / AT-ECG § 5 require fast electronic
    contact incl. e-mail; German practice adds a second direct channel). Which ones may be published?
11. Regulated profession or licensed activity (lawyer, doctor, architect, financial services,
    trade licence, supervisory authority)? ⤷ yes: chamber, title, professional rules → imprint
    duties, and red flag check (SKILL.md rule 8).
12. Editorial / journalistic content (blog, news, magazine)? ⤷ DE: person responsible under
    DE-MSTV § 18(2); AT: disclosure under AT-MEDIENG § 25.
13. Data protection officer appointed or required? Name/contact (may be external). ⤷ unsure:
    note it; phase 4 checks EU-GDPR Art. 37 and DE-BDSG § 38.
14. ⤷ Controller outside the EU/EEA but offering to people in the EU (or outside the UK offering
    to UK residents): EU (Art. 27) / UK representative appointed?

### C. Where (jurisdictions)
15. Where is the entity established (country, and US state)?
16. Where are the users? Which countries do you actively target (language, currency, shipping,
    marketing, domain)? "Available worldwide" → ask which markets actually matter and record the
    rest as an accepted risk.
17. ⤷ US users: which states do you have significant numbers of users in, and what are your annual
    revenue and number of consumers whose data you process per state? (State-law thresholds.)
18. ⤷ Switzerland: Swiss users or a Swiss entity?
19. Which law should govern the terms, and which courts / arbitration? (Note: consumer
    protection of the consumer's country usually still applies; verify in phase 4.)

### D. Who uses it (audience)
20. Consumers (B2C), businesses (B2B), or both? ⤷ B2B only: how do you ensure it (checkbox, VAT ID,
    contracts)? Consumer protection rules depend on this.
21. Minimum age? Are children or teenagers likely users (school context, games, social)? ⤷ yes:
    EU-GDPR Art. 8, US-COPPA, UK children's code → red flag check.
22. Do users create accounts? Can they post content others see (UGC)? ⤷ UGC: notice-and-action,
    moderation, DSA duties (EU-DSA), DMCA agent (US-DMCA), UK Online Safety Act.

### E. Money and contracts
23. Is anything sold? Free, freemium, one-off, subscription, in-app purchases, marketplace?
24. ⤷ paid: which payment provider(s)? Prices incl. VAT? Free trials? Automatic renewal?
    Cancellation path? (DE-BGB § 312k cancellation button, US auto-renewal laws, UK DMCC.)
25. ⤷ B2C sales of goods, digital content/services in the EU/UK: right of withdrawal applies?
    Do you want to use the early-performance waiver for digital content? Physical goods: shipping
    countries, return costs?
26. Warranty / guarantee / liability limits you want? SLA for B2B?
27. Termination and account deletion: who can terminate, notice periods, what happens to data?

### F. Data and processing (business view)
The code tells you *what* is technically there (phase 3). Here you ask for *why* and *what else*.
28. What personal data do you deliberately collect, and for what purpose? (account, orders,
    support, analytics, marketing, product improvement, AI features, fraud prevention…)
29. Newsletter or marketing e-mails? ⤷ double opt-in? existing-customer exception?
    (DE-UWG § 7, UK-PECR reg. 22, US-CAN-SPAM.)
30. Analytics, advertising, retargeting, A/B testing, session replay? Consent management tool?
31. Do you sell or share personal data for advertising (US "sale"/"sharing" definitions)?
32. Special categories (health, biometrics, religion, sexual orientation, union membership),
    precise location, data about children, criminal data? ⤷ red flag check.
33. AI features: do you send user content to an LLM/AI provider? Is it used for training? Any
    automated decisions with legal or similarly significant effect (EU-GDPR Art. 22)? Chatbots or
    generated content shown to users (EU-AI-ACT Art. 50)?
34. Where is data hosted and who are your service providers (hosting, e-mail, CRM, support,
    payments, analytics, error tracking)? Do you already have DPAs with them? Any transfers outside
    the EU/EEA/UK/CH?
35. Retention: how long do you keep accounts, logs, invoices, backups?
36. Security measures you can state truthfully (encryption, access control). Never let the user
    overstate them.
37. ⤷ B2B SaaS processing customers' personal data: are *you* a processor for your customers?
    → DPA document needed (EU-GDPR Art. 28).

### G. Wrap-up
38. Anything unusual the documents must cover (physical events, hardware, marketplace sellers,
    affiliate links, sponsored content, open-source licence terms, beta features)?
39. Who will do the legal review, and by when? (Record it; it shows up in every hand-off.)
40. Read back a summary of all records and get explicit confirmation ("Is everything in these
    records correct and complete?"). Only then go to phase 3.

## After the codebase investigation

Phase 3 will contradict some answers ("You said no analytics, but `@vercel/analytics` is in
`package.json` and used in `app/layout.tsx:8`"). Come back to the interview for every
contradiction or gap, same rules: one question at a time, with a recommendation. Record the
resolution in the inventory LDR.
