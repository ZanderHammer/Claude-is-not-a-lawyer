# Spain: sources

Spanish state law is published in the **Boletín Oficial del Estado (BOE)**. The page
`https://www.boe.es/buscar/act.php?id=<BOE-A-…>` shows the consolidated text ("texto consolidado")
with the date of the last update. Spain implements the EU directives listed in `eu.md`; the GDPR
applies directly and is supplemented by the LOPDGDD. Regional (comunidades autónomas) consumer
and language rules can add duties, for example Catalonia's Código de Consumo: check them if the
user targets a region.

Imprint duties in Spain come from LSSI art. 10 ("aviso legal"); there is no separate media-law
imprint for ordinary websites.

## Imprint and e-commerce

### MS-ES — Ley 34/2002 (LSSI), servicios de la sociedad de la información y de comercio electrónico
- URL: https://www.boe.es/buscar/act.php?id=BOE-A-2002-13758
- Tier: T1
- Expect: Artículo 10
- Also: https://www.aepd.es/guias/guia-cookies.pdf https://www.aepd.es/
- Key provisions: art. 10(1)(a)–(g) (permanent, easy, direct, free access to: name or company name, address, e-mail and other direct contact data; commercial register data; authorisation data and supervising body; regulated-profession data; NIF; clear price information incl. taxes and shipping; codes of conduct); art. 10(2) (duty is met by publishing it on the website); art. 20 (information in commercial communications); art. 21 (no unsolicited commercial e-mail; exception for similar products to existing customers, with free opt-out in every message); art. 22(1) (easy, free revocation of consent to commercial communications); art. 22(2) (cookies and similar technologies: consent after clear and complete information; exemption for strictly necessary use); art. 27 (information before contracting); art. 28 (confirmation after contracting)
- Used for: imprint, cookie-policy, privacy-policy, terms
- Notes: Art. 10 is the Spanish imprint ("aviso legal"). Art. 22(2) refers to the data protection law for the information and consent standard.
- Last verified: 2026-10-18

## Cookies and tracking

### ES-AEPD-COOKIES — AEPD: Guía sobre el uso de las cookies (May 2024)
- URL: https://www.aepd.es/guias/guia-cookies.pdf
- Tier: T2
- Key provisions: section 3.1 (transparency, layered information); section 3.2 (consent: continued browsing is not valid consent, citing the EDPB; mere inactivity is not consent; if an "accept" button is offered, an equally prominent "Rechazar" button is required; granular choice at least by purpose); section 3.2.4 (minors under 14)
- Used for: cookie-policy
- Notes: PDF; the checker only tests reachability. Page references checked in the text of the May 2024 edition on 2026-10-18. The AEPD updates this guide, so check for a newer edition.
- Last verified: 2026-10-18

## Data protection

### MS-ES-DPA — Spain (DPA)
- URL: https://www.aepd.es/
- Tier: T2
- Expect: Agencia Española de Protección de Datos
- Used for: privacy-policy (complaint clause, authority name), national guidance
- Last verified: 2026-10-17

### ES-LOPDGDD — Ley Orgánica 3/2018 de Protección de Datos Personales y garantía de los derechos digitales
- URL: https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673
- Tier: T1
- Expect: Protección de Datos Personales y garantía de los derechos digitales
- Key provisions: art. 7(1) (age of digital consent: **14**; below 14, consent of the holder of parental authority is required); art. 11 (layered information: basic information with identity of the controller, purpose and rights under GDPR arts. 15–22, plus a link to the full information)
- Used for: privacy-policy
- Notes: The layered-information model of art. 11 is the format the AEPD expects for web forms.
- Last verified: 2026-10-18

## Consumer contracts

### ES-TRLGDCU — Real Decreto Legislativo 1/2007, Ley General para la Defensa de los Consumidores y Usuarios
- URL: https://www.boe.es/buscar/act.php?id=BOE-A-2007-20555
- Tier: T1
- Expect: Defensa de los Consumidores y Usuarios
- Key provisions: art. 60 (pre-contractual information); art. 80 (requirements for terms not individually negotiated); arts. 82–90 (unfair terms: definition, nullity, black list); art. 97 (pre-contractual information for distance contracts); art. 98 (formal requirements for distance contracts); art. 102 (14-day withdrawal right, "desistimiento"; penalty clauses void); art. 103 (exceptions, incl. digital content after consent); arts. 104–108 (period, omitted information, exercise, effects); arts. 114–127 (conformity and warranty for goods and digital content or services: art. 115 ff.; art. 126 for modifications of digital content)
- Used for: terms, withdrawal-notice
- Notes: The consolidated text checked on 2026-10-18 was last updated on 28/02/2026 and contains **no electronic withdrawal function** yet (search for "función de desistimiento" had no hits). The deadline for implementing `EU-DIR-2023-2673` has passed, so check the BOE for a later amendment before drafting the withdrawal function; if there is none, report that the national rule is missing and rely on the Directive.
- Last verified: 2026-10-18

### ES-LCGC — Ley 7/1998 sobre condiciones generales de la contratación
- URL: https://www.boe.es/buscar/act.php?id=BOE-A-1998-8789
- Tier: T1
- Expect: condiciones generales de la contratación
- Key provisions: art. 5 (incorporation requirements: acceptance, reference in the contract, clear and comprehensible wording, copy for the adherent; electronic contracts); art. 7 (terms not incorporated); art. 8 (nullity of terms against mandatory rules and, for consumers, of unfair terms)
- Used for: terms
- Last verified: 2026-10-18

## Accessibility

### ES-LEY-11-2023 — Ley 11/2023 (transposición de la Directiva (UE) 2019/882, accesibilidad de productos y servicios)
- URL: https://www.boe.es/buscar/act.php?id=BOE-A-2023-11022
- Tier: T1
- Expect: accesibilidad de determinados productos y servicios
- Key provisions: art. 3(1) and (3) (accessibility requirements of Annex I; microenterprises providing services are exempt); art. 13(2) (service providers must describe in their general terms how the service meets the accessibility requirements); art. 27 (market surveillance authorities; regions designate their own)
- Used for: terms (accessibility statement for e-commerce services)
- Notes: Check scope in art. 2 for e-commerce services before applying. Product and service scope follows `EU-DIR-2019-882`.
- Last verified: 2026-10-18

## Digital services (DSA)

### ES-CNMC — Comisión Nacional de los Mercados y la Competencia
- URL: https://www.cnmc.es/
- Tier: T2
- Expect: CNMC
- Notes: Not verified as the Spanish Digital Services Coordinator. The Commission's DSC page (digital-strategy.ec.europa.eu, "dsa-dscs") says Spain faced infringement proceedings over the designation or empowerment of its coordinator. Confirm the current authority there before citing one in a document.
- Used for: terms (DSA contact point, if the user is an intermediary service)
- Last verified: 2026-10-18
