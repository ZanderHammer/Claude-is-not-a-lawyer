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
- Also: https://entreprendre.service-public.gouv.fr/vosdroits/F31228 https://www.legifrance.gouv.fr/
- Bot-protected: yes
- Key provisions: CNIL guidelines and recommendation on cookies and trackers ("Refuser tout" as easy as "Accepter tout"; consent validity); Loi Informatique et Libertés art. 82 (implements ePrivacy Art. 5(3)); LCEN (loi n° 2004-575) art. 6-III **mentions légales** (French imprint duty: per a law-firm summary, name/denomination, seat, director of publication, phone and e-mail, host details; not yet checked against Légifrance); Code de la consommation (pre-contractual information, droit de rétractation)
- Used for: imprint ("Mentions légales"), cookie-policy, privacy-policy, terms (CGU/CGV)
- Notes: The CNIL is very active on cookies. Légifrance is behind a Cloudflare bot challenge that neither plain fetch nor a headless browser passes, so the LCEN article was **not read from the official text**; the content of art. 6-III below comes from a law-firm summary. Official guidance on cookies and consent (DILA): https://entreprendre.service-public.gouv.fr/vosdroits/F31228. Ask the user to open Légifrance, or follow the fallback procedure.
- Verification: browser/web-fetch: DPA and Service-Public pages read; Légifrance blocked (Cloudflare challenge), LCEN text not read
- Last verified: 2026-10-18


### MS-IT — Italy
- URL: https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9677876
- Tier: T2
- Expect: Linee guida cookie
- Also: https://www.garanteprivacy.it/ https://www.normattiva.it/
- Bot-protected: yes
- Key provisions: Garante guidelines on cookies and other tracking tools (10 June 2021); Codice privacy (D.lgs. 196/2003) art. 122 (cookies); Codice del consumo (consumer rights)
- Used for: cookie-policy, privacy-policy, terms
- Notes: normattiva.it refuses plain HTTP clients but loads in a headless browser. Search for D.lgs. 196/2003 there to read art. 122.
- Verification: automated + browser: DPA guideline page and normattiva.it home page read
- Last verified: 2026-10-18

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
- Notes: The DPA server sends an incomplete TLS certificate chain, which the verification environment (correctly) refuses; the site is therefore **unverified**. Its domain appears in an official CPDP document and in search results. State gazette (reachable): https://dv.parliament.bg/. Use `EU-EDPB-MEMBERS` for the DPA contact details.
- Verification: unverified: not reachable from the verification environment
- Last verified: 2026-10-18

### MS-HR — Croatia
- URL: https://azop.hr/
- Tier: T2
- Expect: AZOP
- Also: https://www.narodne-novine.nn.hr/
- Bot-protected: yes
- Verification: automated: DPA home page read; Narodne novine not reachable
- Notes: narodne-novine.nn.hr was unreachable from the verification environment (tunnel error). Use `MS-NLEX` for Croatian legislation if it stays unreachable.
- Last verified: 2026-10-18

### MS-CY — Cyprus
- URL: https://www.gov.cy/dataprotection/
- Tier: T2
- Bot-protected: yes
- Notes: Use `MS-NLEX` for legislation.
- Verification: automated: home page read
- Expect: Προστασίας Δεδομένων
- Last verified: 2026-10-18

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
- Verification: automated + browser: both sites read
- Notes: retsinformation.dk answers plain HTTP clients with a challenge but loads in a headless browser.
- Last verified: 2026-10-18

### MS-EE — Estonia
- URL: https://www.aki.ee/
- Tier: T2
- Also: https://www.riigiteataja.ee/
- Bot-protected: yes
- Verification: browser: both sites read in a headless browser
- Notes: Both sites refuse plain HTTP clients (403) but load in a headless browser.
- Last verified: 2026-10-18

### MS-FI — Finland
- URL: https://tietosuoja.fi/
- Tier: T2
- Also: https://www.finlex.fi/en
- Bot-protected: yes
- Verification: partial: tietosuoja.fi blocked (Cloudflare challenge); Finlex read; cookie supervision from a search result only
- Notes: tietosuoja.fi is behind a Cloudflare bot challenge that no tool here passed, so the DPA site was **not read**. In Finland the electronic-communications regulator Traficom supervises cookie rules, with the DPA competent for personal data questions (per a Traficom cookie guide for service providers co-produced with the DPA, seen in search results only; check traficom.fi).
- Last verified: 2026-10-18

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
- Also: https://magyarkozlony.hu/ https://njt.hu/
- Bot-protected: yes
- Verification: automated + partial: DPA read; njt.hu unreachable
- Notes: njt.hu (national legislation database) refuses connections from the verification environment. The official gazette magyarkozlony.hu is reachable.
- Last verified: 2026-10-18

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
- Also: https://e-seimas.lrs.lt/ https://www.e-tar.lt/
- Bot-protected: yes
- Verification: partial: vdai.lrv.lt blocked (Cloudflare challenge); register of legal acts read
- Notes: vdai.lrv.lt is behind a Cloudflare bot challenge that no tool here passed, so the DPA site was **not read**; its domain appears in search results. The Seimas register of legal acts (e-seimas.lrs.lt) is reachable; e-tar.lt refused automated access.
- Last verified: 2026-10-18

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
- Also: https://www.dziennikustaw.gov.pl/ https://isap.sejm.gov.pl/
- Bot-protected: yes
- Verification: automated + partial: DPA read; isap.sejm.gov.pl refuses automated access
- Notes: isap.sejm.gov.pl returns 403 to every automated client tried. The official gazette dziennikustaw.gov.pl is reachable.
- Last verified: 2026-10-18

### MS-PT — Portugal
- URL: https://www.cnpd.pt/
- Tier: T2
- Expect: CNPD
- Also: https://diariodarepublica.pt/dr/home
- Last verified: 2026-10-17

### MS-RO — Romania
- URL: https://www.dataprotection.ro/
- Tier: T2
- Also: https://monitoruloficial.ro/ https://legislatie.just.ro/
- Bot-protected: yes
- Verification: automated + partial: DPA read; legislatie.just.ro unreachable
- Notes: legislatie.just.ro closes connections from the verification environment. The official gazette monitoruloficial.ro is reachable.
- Expect: dataprotection
- Last verified: 2026-10-18

### MS-SK — Slovakia
- URL: https://dataprotection.gov.sk/
- Tier: T2
- Also: https://www.slov-lex.sk/
- Bot-protected: yes
- Verification: browser: DPA read in a headless browser; Slov-Lex read automatically
- Notes: dataprotection.gov.sk answers plain HTTP clients with 503 but loads in a headless browser.
- Last verified: 2026-10-18

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
