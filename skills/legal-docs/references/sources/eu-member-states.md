# Other EU member states (and EEA): sources

Germany, Austria and Spain have their own files (`de.md`, `at.md`, `es.md`; the Spanish IDs `MS-ES` and `MS-ES-DPA` live in `es.md`). For every other member state this
file gives the **data protection authority** (needed for the complaint clause and for national
guidance) and the **official legislation portal** (for national implementations of the EU
directives in `eu.md`: ePrivacy/cookies, consumer rights, e-commerce information duties).
Coverage is deliberately lighter than for DE/AT. For a member state that matters to the user
(interview Q16), follow this procedure:

1. Start from the EU act in `eu.md` (the directive sets the minimum content).
2. Find the national implementation: open `MS-NLEX` and search for the directive number, or use
   the portal below.
3. Check the DPA's guidance on cookies and privacy notices (many DPAs publish stricter
   expectations than the EU guidelines).
4. Record the national sources you used in `sources-used.md`. National sources you found
   yourself are `replacement` / `non-official` per `source-policy.md` unless they are on the
   portal or DPA domain listed here.

EEA states (Iceland, Liechtenstein, Norway) apply the GDPR and most consumer directives. Their
DPAs are listed in `EU-EDPB-MEMBERS`.

### MS-NLEX — N-Lex: common gateway to the national law databases of all member states (European Union)
- URL: https://n-lex.europa.eu/n-lex/index
- Tier: T2
- Expect: N-Lex
- Key provisions: Search national legislation of each member state from one place (links to the official national portals)
- Used for: finding national implementations of EU directives
- Last verified: 2026-10-17

## Countries with notable national specifics

### MS-FR — France
- URL: https://www.cnil.fr/fr/cookies-et-autres-traceurs
- Tier: T2
- Expect: cookies
- Also: https://www.legifrance.gouv.fr/
- Bot-protected: yes
- Key provisions: CNIL guidelines and recommendation on cookies and trackers ("Refuser tout" as easy as "Accepter tout"; consent validity); Loi Informatique et Libertés art. 82 (implements ePrivacy Art. 5(3)); LCEN (loi n° 2004-575) **mentions légales** (French imprint duty): look up the current article on Légifrance; Code de la consommation (pre-contractual information, droit de rétractation)
- Used for: imprint ("Mentions légales"), cookie-policy, privacy-policy, terms (CGU/CGV)
- Notes: The CNIL is very active on cookies. Légifrance blocks automated clients; ask the user to open the article if needed.
- Last verified: 2026-10-17


### MS-IT — Italy
- URL: https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9677876
- Tier: T2
- Expect: Linee guida cookie
- Also: https://www.garanteprivacy.it/ https://www.normattiva.it/
- Bot-protected: yes
- Key provisions: Garante guidelines on cookies and other tracking tools (10 June 2021); Codice privacy (D.lgs. 196/2003) art. 122 (cookies); Codice del consumo (consumer rights)
- Used for: cookie-policy, privacy-policy, terms
- Notes: normattiva.it refused automated connections at verification.
- Last verified: 2026-10-17

### MS-NL — Netherlands
- URL: https://wetten.overheid.nl/BWBR0009950
- Tier: T1
- Expect: Telecommunicatiewet
- Also: https://www.autoriteitpersoonsgegevens.nl/
- Key provisions: Telecommunicatiewet art. 11.7a (cookies; consent, exemptions for functional and certain analytics cookies) and art. 11.7 (unsolicited communications); Burgerlijk Wetboek Book 6 (consumer contracts, general terms: art. 6:231 ff.)
- Used for: cookie-policy, privacy-policy, terms
- Last verified: 2026-10-17

### MS-IE — Ireland
- URL: https://www.irishstatutebook.ie/eli/2011/si/336/made/en/print
- Tier: T1
- Expect: Electronic Communications Networks and Services
- Also: https://www.dataprotection.ie/en/dpc-guidance
- Key provisions: S.I. No. 336/2011 (ePrivacy Regulations): reg. 5 (cookies), reg. 13 (unsolicited communications); DPC guidance (cookies, transparency). The DPC is lead supervisory authority for many large tech companies
- Used for: cookie-policy, privacy-policy
- Last verified: 2026-10-17

## Data protection authorities and legislation portals

`URL` is the DPA (T2), `Also` is the official legislation portal (T1). `Bot-protected` means at
least one of the two refused automated access at verification.

### MS-BE — Belgium
- URL: https://www.autoriteprotectiondonnees.be/citoyen
- Tier: T2
- Expect: Autorité de protection des données
- Also: https://www.ejustice.just.fgov.be/
- Last verified: 2026-10-17

### MS-BG — Bulgaria
- URL: https://www.cpdp.bg/
- Tier: T2
- Also: https://dv.parliament.bg/
- Bot-protected: yes
- Notes: The DPA site had a TLS certificate chain problem for some clients at verification.
- Last verified: 2026-10-17

### MS-HR — Croatia
- URL: https://azop.hr/
- Tier: T2
- Expect: AZOP
- Also: https://www.narodne-novine.nn.hr/
- Bot-protected: yes
- Last verified: 2026-10-17

### MS-CY — Cyprus
- URL: https://www.gov.cy/dataprotection/
- Tier: T2
- Bot-protected: yes
- Notes: Use `MS-NLEX` for legislation.
- Last verified: 2026-10-17

### MS-CZ — Czechia
- URL: https://uoou.gov.cz/
- Tier: T2
- Expect: Úřad pro ochranu osobních údajů
- Also: https://e-sbirka.gov.cz/
- Last verified: 2026-10-17

### MS-DK — Denmark
- URL: https://www.datatilsynet.dk/
- Tier: T2
- Expect: Datatilsynet
- Also: https://www.retsinformation.dk/
- Bot-protected: yes
- Last verified: 2026-10-17

### MS-EE — Estonia
- URL: https://www.aki.ee/
- Tier: T2
- Also: https://www.riigiteataja.ee/
- Bot-protected: yes
- Last verified: 2026-10-17

### MS-FI — Finland
- URL: https://tietosuoja.fi/
- Tier: T2
- Also: https://www.finlex.fi/en
- Bot-protected: yes
- Last verified: 2026-10-17

### MS-FR-DPA — France (DPA)
- URL: https://www.cnil.fr/fr
- Tier: T2
- Expect: CNIL
- Last verified: 2026-10-17

### MS-GR — Greece
- URL: https://www.dpa.gr/
- Tier: T2
- Expect: Αρχή Προστασίας Δεδομένων Προσωπικού Χαρακτήρα
- Notes: Use `MS-NLEX` for legislation.
- Last verified: 2026-10-17

### MS-HU — Hungary
- URL: https://naih.hu/
- Tier: T2
- Expect: Nemzeti Adatvédelmi és Információszabadság Hatóság
- Also: https://njt.hu/
- Bot-protected: yes
- Last verified: 2026-10-17

### MS-IE-DPA — Ireland (DPA)
- URL: https://www.dataprotection.ie/en
- Tier: T2
- Expect: Data Protection Commission
- Also: https://www.irishstatutebook.ie/
- Last verified: 2026-10-17

### MS-IT-DPA — Italy (DPA)
- URL: https://www.garanteprivacy.it/
- Tier: T2
- Expect: Garante
- Last verified: 2026-10-17

### MS-LV — Latvia
- URL: https://www.dvi.gov.lv/lv
- Tier: T2
- Expect: Datu valsts inspekcija
- Also: https://likumi.lv/
- Last verified: 2026-10-17

### MS-LT — Lithuania
- URL: https://vdai.lrv.lt/
- Tier: T2
- Also: https://www.e-tar.lt/
- Bot-protected: yes
- Last verified: 2026-10-17

### MS-LU — Luxembourg
- URL: https://cnpd.public.lu/fr.html
- Tier: T2
- Expect: Commission nationale pour la protection des données
- Also: https://legilux.public.lu/
- Last verified: 2026-10-17

### MS-MT — Malta
- URL: https://idpc.org.mt/
- Tier: T2
- Expect: IDPC
- Also: https://legislation.mt/
- Last verified: 2026-10-17

### MS-NL-DPA — Netherlands (DPA)
- URL: https://www.autoriteitpersoonsgegevens.nl/
- Tier: T2
- Expect: Autoriteit Persoonsgegevens
- Last verified: 2026-10-17

### MS-PL — Poland
- URL: https://uodo.gov.pl/
- Tier: T2
- Expect: UODO
- Also: https://isap.sejm.gov.pl/
- Bot-protected: yes
- Last verified: 2026-10-17

### MS-PT — Portugal
- URL: https://www.cnpd.pt/
- Tier: T2
- Expect: CNPD
- Also: https://diariodarepublica.pt/dr/home
- Last verified: 2026-10-17

### MS-RO — Romania
- URL: https://www.dataprotection.ro/
- Tier: T2
- Also: https://legislatie.just.ro/
- Bot-protected: yes
- Last verified: 2026-10-17

### MS-SK — Slovakia
- URL: https://dataprotection.gov.sk/
- Tier: T2
- Also: https://www.slov-lex.sk/
- Bot-protected: yes
- Last verified: 2026-10-17

### MS-SI — Slovenia
- URL: https://www.ip-rs.si/
- Tier: T2
- Expect: IPRS
- Also: https://pisrs.si/
- Last verified: 2026-10-17


### MS-SE — Sweden
- URL: https://www.imy.se/
- Tier: T2
- Expect: Integritetsskyddsmyndigheten
- Also: https://www.riksdagen.se/sv/dokument-och-lagar/
- Last verified: 2026-10-17
