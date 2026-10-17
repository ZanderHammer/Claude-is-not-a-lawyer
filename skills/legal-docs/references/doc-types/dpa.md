# Data processing agreement (DPA / Auftragsverarbeitungsvertrag, AVV)

Checklist items point to sources. **Fetch and read every provision before you rely on it.**

## When is it required

When the user's company processes personal data **on behalf of** its customers (typical for B2B
SaaS: customers upload their users' or employees' data), the user is a **processor** and needs a
contract meeting EU-GDPR Art. 28(3) / UK-GDPR Art. 28(3) with each customer. Switzerland: CH-DSG
Art. 9 (processing by processors, check the text). Check the roles carefully with
EU-EDPB-CONTROLLER. A provider that decides purposes itself is a controller, not a processor.

The **other direction** (the user signing DPAs with their own processors such as hosting or
e-mail providers) is usually done by accepting the provider's DPA. List those in the
implementation checklist instead of drafting them.

## Recommended approach

Base the DPA on the Commission's standard contractual clauses for Art. 28 (EU-SCC-ART28). They
are drafted to meet Art. 28(3)–(4), and using them reduces drafting risk. Fill in the annexes
from the inventory record. If transfers to third countries happen (sub-processors outside the
EEA), add the transfer SCCs (EU-SCC-TRANSFERS, module 2 or 3) or rely on an adequacy decision.

## Checklist (EU-GDPR Art. 28)

| Item | Source |
|---|---|
| Subject-matter, duration, nature and purpose of processing, type of personal data, categories of data subjects, obligations and rights of the controller | EU-GDPR Art. 28(3) first sentence |
| Processing only on documented instructions (incl. transfers) | Art. 28(3)(a) |
| Confidentiality of authorised persons | Art. 28(3)(b) |
| Security measures (Art. 32), with a TOMs annex | Art. 28(3)(c), Art. 32 |
| Sub-processors: prior specific or general written authorisation, information on changes, right to object, same obligations flowed down | Art. 28(2), (3)(d), (4) |
| Assistance with data subject requests | Art. 28(3)(e) |
| Assistance with Art. 32–36 (security, breach notification, DPIA, prior consultation) | Art. 28(3)(f) |
| Deletion or return at the end, at the controller's choice | Art. 28(3)(g) |
| Information and audits; processor informs the controller of infringing instructions | Art. 28(3)(h) and the following subparagraph |
| Written form, incl. electronic | Art. 28(9) |
| Structure and wording | EU-SCC-ART28 (clauses + annexes I–IV) |
| UK customers | UK-GDPR Art. 28; UK-ICO-TRANSFERS for transfers |

## Pitfalls

- Declaring the SaaS provider a processor while it also uses the data for its own purposes
  (analytics, AI training). Those purposes make it a controller for that part. Say so.
- Sub-processor lists that don't match the inventory.
- TOMs annex promising measures the code/infrastructure does not implement.
