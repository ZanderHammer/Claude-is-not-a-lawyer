# Cookie policy and consent texts

Checklist items point to sources. **Fetch and read every provision before you rely on it.**
"Cookies" means any storing of or access to information on the user's device: cookies,
localStorage/sessionStorage, IndexedDB, pixels, SDK identifiers, fingerprinting
(EU-EDPB-5-3). The cookie list must come from the codebase investigation, never from a template.

## When is it required

- **EU/EEA**: consent for any device storage/access that is not strictly necessary for a service
  the user explicitly requested (EU-EPRIVACY Art. 5(3) + national law: DE-TDDDG § 25, AT-TKG-165
  § 165(3), MS-FR, MS-IT, MS-ES, MS-NL, MS-IE). Consent must meet GDPR standards
  (EU-GDPR Art. 4(11), 7; EU-EDPB-CONSENT). Subsequent processing of the data needs a GDPR
  legal basis too (privacy policy).
- **UK**: UK-PECR reg. 6 with the exceptions in Sch. A1 (some analytics/functionality uses may be
  exempt subject to conditions); UK-ICO-COOKIES.
- **Switzerland**: no specific consent rule; transparency under CH-DSG Art. 19 and CH-EDOEB
  guidance.
- **US**: no general consent duty. California: cross-context behavioural advertising = "sharing"
  → opt-out link and opt-out preference signals (US-CA-CCPA § 1798.135, US-CA-CPPA-REGS § 7025).
  CalOPPA: Do-Not-Track disclosure (US-CA-CALOPPA).

A separate cookie policy is not mandatory if the privacy policy contains the information, but
a separate page plus a consent banner text is the usual structure.

## Deliverables

1. Cookie policy page (`documents/cookie-policy.<lang>.md`)
2. Consent banner texts (first layer, settings layer, category descriptions, button labels),
   as a separate file `documents/consent-banner.<lang>.md` or JSON if the project's CMP needs it
3. Implementation notes for the code (what must wait for consent)

## Checklist

| Item | Source |
|---|---|
| Table of all cookies/storage items: name, provider, purpose, category, duration, first/third party | EU-EPRIVACY Art. 5(3) ("clear and comprehensive information"); EU-GDPR Art. 13; inventory record |
| Strictly-necessary exemption only for what the explicitly requested service needs (no analytics, no ads) | EU-EPRIVACY Art. 5(3) second sentence; DE-TDDDG § 25(2) Nr. 2; AT-TKG-165; UK-PECR Sch. A1 |
| Consent: prior, freely given, specific, informed, unambiguous; no pre-ticked boxes; scrolling is not consent | EU-GDPR Art. 4(11), 7; EU-EDPB-CONSENT |
| Reject as easy as accept (first layer) | EU-EDPB-CONSENT; MS-FR (CNIL); DE-DSK guidance (OH Digitale Dienste) |
| Withdrawal of consent as easy as giving it (persistent settings link) | EU-GDPR Art. 7(3) |
| Third-country transfers by cookie providers | EU-GDPR Art. 13(1)(f), 44 ff.; EU-DPF |
| Joint controllership for some third-party tools (e.g. social plugins) | EU-GDPR Art. 26; EU-EDPB-CONTROLLER |
| UK: describe use of exceptions and the right to object where Sch. A1 requires it | UK-PECR Sch. A1; UK-ICO-COOKIES |
| California: "Do Not Sell or Share" link, honouring Global Privacy Control | US-CA-CCPA § 1798.135; US-CA-CPPA-REGS § 7025 |
| Do-Not-Track response | US-CA-CALOPPA § 22575(b) |

## Pitfalls

- Declaring analytics "necessary". Declaring Google Fonts/CDNs "no cookies, so no issue" (they
  still transfer IP addresses, so they belong in the privacy policy).
- A banner whose "Reject" is hidden on the second layer.
- Cookie lists copied from a scanner that doesn't match the code (or vice versa). Re-scan in
  update mode.
- Claiming scripts wait for consent when the code loads them immediately. Report it as a code
  gap instead.
