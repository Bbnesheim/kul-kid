# KUL KID – Merkevarestemme

Denne guiden beskriver hvordan KUL KID skal høres ut – på nett, i e‑poster og i automatiserte Klaviyo‑flows.
Alle e‑poster skal skrives på **norsk bokmål**.

---

## 1. Rolle & perspektiv

- Vi snakker som **vennlig, kompetent guide** for både barn og foresatte.
- Barn først – men vi vet at det er voksne som handler.
- Vi er tydelige uten å være strenge, morsomme uten å være masete.

**Fortellerstemme:**
- "vi" når vi snakker om merke og team.
- "du" og "MINI" når vi snakker til kundene.

---

## 2. Tone

- **Lekent og varmt** – små glimt av humor, men alltid trygt og inkluderende.
- **Direkte og konkret** – rett på sak, ingen unødvendige ord.
- **Optimistisk** – vi heier på barnas uttrykk og foreldres hverdag.
- **Null sarkasme** – ingen ironi, ingen stikk.

Eksempel (fra velkomstflow):
- «Tusen takk for at du ble med i KUL KID Kundeklubb.»
- «Vi lover myke stoffer, kule trykk og komfort barna faktisk vil ha på.»

---

## 3. Stil

- Korte setninger.
- Enkle, konkrete ord («plagg», «pakke», «handlekurv», «rabatt»).
- Aktive verb ("Bygg", "Velg", "Oppdag", "Bli med").
- Få utropstegn (maks 1 per seksjon / e‑post).
- Inkluderende og jordnær – ingen intern jargong.

**Formatering:**
- Overskrifter: **tittel‑stil**, 5–7 ord der det er mulig.
- Brødtekst: 1–3 setninger per avsnitt.
- Lister: bruk punktlister når mye informasjon skal deles.

---

## 4. Brandnavn & standardfraser

**Alltid slik i tekst:**
- `KUL KID`
- `KUL KID Kundeklubb`
- `KUL KID's`, `KUL KID Kundeklubb's` ved eierskap.
- `KULKID.no` / `www.KULKID.no` **kun** som domene/URL.

**Aldri slik:**
- `KULKID` som vanlig ord i brødtekst.
- `Kul Kid`, `kulkid`, `Kul-Kid`.

**Standardfraser i flows (skal gjenbrukes):**
- Velkomst / sign‑up: `Tusen takk for at du ble med i KUL KID Kundeklubb.`
- Takk for ordre: `Tusen takk for bestillingen.` / `Tusen takk for at du valgte oss.`
- Levering: `Leveringstid er normalt 12-14 virkedager.`

Alle nye e‑poster skal bruke disse formuleringene der de passer.

---

## 5. Gjør / Ikke gjør

### Gjør

- «Velg favorittfarger.»
- «Klar, ferdig, KUL!»
- «Gi MINI looken – du tar æren.»
- «Myke basics som tåler lek hver dag.»
- «Dine nye KUL KID‑plagg er på vei.»
- «Tusen takk for at du ble med.»

### Unngå
- Fagjargong og kompliserte setninger:
  - Ikke: «Optimaliser konverteringsfrekvensen med modulære produktpakker.»
  - Ja: «Bygg en pakke med favorittplaggene deres.»
- Ironi/sarkasme og "tøff" tone.
- Overdrevent formelt språk («verifiser», «preferanser», «dashboard» osv.).
- Lange avsnitt og vegger av tekst.

---

## 6. Kjerneegenskaper

- **Modig, men ikke masete** – vi tør sterke farger og tydelige utsagn, men roper ikke.
- **Inkluderende** – alle barn hører til, uansett stil.
- **Gøy + funksjonelt** – lekne uttrykk, praktiske detaljer.
- **Heier på kreativitet** – vi oppfordrer til å blande, velge og teste egen stil.

---

## 7. E‑postretningslinjer (Klaviyo)

**Emnefelt:**
- 35–50 tegn.
- 1 hovedbudskap, ev. én emoji på slutten (valgfritt).
- Norsk bokmål, tittel‑stil.

Eksempler:
- «Velkommen til KUL KID Kundeklubb – her er din rabatt»
- «Tusen takk for bestillingen din»
- «Du glemte noe i handlekurven»

**Forhåndstekst (preview):**
- 40–80 tegn.
- Utfyller emnet, gjentar det ikke.

**Brødtekst:**
- 1–3 korte setninger per avsnitt.
- Første avsnitt skal forklare *hvorfor* kunden får e‑posten (velkomst, takk, påminnelse osv.).

**Hilsener:**
- `Hei {{ first_name|default:"du" }},`
- Bruk "du" – aldri "De".

**CTA‑er:**
- 1 primær CTA per e‑post, maks 2 totalt.
- 2–4 ord, handlingsorientert.

Eksempler:
- «Til butikk»
- «Se alle nyheter»
- «Fullfør bestilling»
- «Bruk rabatten din»

**Footer:**
- Alltid inkluder:
  - Avmeldingslenke.
  - Avsender (`{{ organization.name }} {{ organization.full_address }}`).
  - Avslutning i teksten som kan være enkel, f.eks. «Hilsen teamet på KULKID.no».

---

## 8. Microcopy – mønstre

**Tom handlekurv:**
- «Klar for noe gøy? Legg til din første favoritt.»

**Velkommen / sign‑up:**
- «Tusen takk for at du ble med i KUL KID Kundeklubb.»
- «Som velkomst får du 15% rabatt på ditt første kjøp med koden KULKID15.»

**Bekreftelse / ordre:**
- «Tusen takk for bestillingen.»
- «Din første KUL KID‑bestilling er bekreftet og pakket med omtanke!»
- «Du vil motta sporingsinfo når pakken er sendt. Leveringstid er normalt 12-14 virkedager.»

**Abandon cart:**
- «Du glemte noe i handlekurven.»
- «Trenger du hjelp med bestillingen?»

**Win‑back / reaktivering:**
- «Vi savner deg.»
- «Her er en liten ekstra dytt for å komme i gang igjen.»

Disse setningene kan gjenbrukes og tilpasses, men grunnformen bør gjenkjennes i alle flows.

---

## 9. Samspill med design

- Overskrifter settes typografisk i **Luckiest Guy** (se `BRAND_GUIDE.md`), men copyen skal fortsatt være kort og tydelig.
- Brødtekst settes i **Quicksand** og skal være lett å lese på mobil.
- Tone og tekst må alltid ta hensyn til kontrast og lesbarhet – ingen tekst direkte på sterke rainbow‑bakgrunner.

Kort sagt: **Svart‑på‑hvitt i språket** – tydelig, ærlig og lekent.
