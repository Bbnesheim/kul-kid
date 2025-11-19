# KUL KID Brand Guide

Status: Derived from current live theme, Klaviyo templates and `/klaviyo_automation` brand assets.

---

## 1) Brand Essence
- **Personlighet:** Lekent, modig, kid‑first. Enkelt formspråk, høy kontrast.
- **Verdier:** Kreativitet, inkludering, hverdagslek.
- **Stemme:** Kort, tydelig og oppmuntrende. Aktive verb, få utropstegn, ingen sarkasme.
- E‑poster skal skrives på **norsk bokmål**.

For detaljer om tone, se også `BRAND_VOICE.md`.

---

## 2) Brandnavn & skriving

**Alltid bruk disse formene i tekst:**
- `KUL KID`
- `KUL KID's`
- `KUL KID Kundeklubb`
- `KUL KID Kundeklubb's`
- `www.KULKID.no` (kun URL)
- `KULKID.no` (nettstedsreferanser)

**Aldri bruk:**
- `KULKID` (uten mellomrom, i brødtekst)
- `Kul Kid`, `kulkid`, `Kul-Kid`, eller sammensetninger som `KULKID-plagg` (bruk `KUL KID-plagg`).

**Standardformuleringer i flows (Klaviyo/nettbutikk):**
- Takkemelding: bruk
  - `Tusen takk, {{ first_name }}` når navn finnes
  - `Tusen takk` uten navn
- Leveringstid: bruk alltid setningen
  - `Leveringstid er normalt 12-14 virkedager.`

Disse tekstene er felles referanse for nye flows, e‑poster og on‑site meldinger.

---

## 3) Logo
- Primærlogo: Shopify‑fil `Kul_Kid_Logo.svg`.
- Brukes primært på **lyse bakgrunner**.
- Minimumshøyde: ca. **24px** på mobil, **32px+** på desktop.
- Frisone: minst høyden på «K» rundt logoen.
- Ikke: vri, strekke, legge på effekter, endre farger utenfor paletten, eller plassere logo på lav kontrast.

---

## 4) Farger

### 4.1 Kjernepalett (web + e‑post)
- **Svart:** `#121212`
  - All hovedtypografi, brødtekst og ikoner.
  - Default bakgrunn for primær CTA på lys bakgrunn.
- **Hvit:** `#FDFDFD`
  - Sider, kort og flater. Kan mappes til temaets hvite bakgrunns‑token.

### 4.2 Sekundærpalett (definert i `klaviyo_automation/BRAND_ASSETS.md`)
- **Grønn:** `#4d6d5d`
  - Små detaljer: ikoner, labels, streker. Ikke bruk som store bakgrunner.
- **Lys grønn:** `#f0fff4`
  - Primær myk bakgrunn for seksjoner/bannere i stedet for grå.

### 4.3 E‑post‑gradienter (Klaviyo)
Kilde: `klaviyo_automation/templates/kulkid_newsletter_design.html`.

- Helhetlig bakgrunnsgradient (body / `.email-wrapper`):
  - `linear-gradient(180deg, #C8E6C9 0%, #FFE0B2 40%, #FFCDD2 70%, #C8E6C9 100%)`
- Kort/produkt‑gradienter:
  - `linear-gradient(45deg, #FFE0B2, #FFCDD2)` rundt produktbilder.
- Hovedknapper i e‑post:
  - Primær: `#121212` bakgrunn, hvit tekst.
  - Rosa variant: `#FF1493` (`.btn-pink`) med hvit tekst.

**Regler for e‑postfarger:**
- Gradienter er **bakgrunner**, ikke tekstfarger.
- Tekst på gradient: alltid `#121212`.
- Bruk hvit (`#FDFDFD`) kun på sorte (`#000000` / `#121212`) flater.

### 4.4 Rainbow‑gradient (nettsted)
Kilde: `sections/main-footer.liquid` + `assets/kk-section-footer.css`.

- Default‑stopp i footer (kan overstyres i Theme Editor):
  - `#ff6b6b, #4ecdc4, #45b7d1, #96ceb4, #feca57, #ff9ff3, #54a0ff`
- Animasjon: `@keyframes rainbowGradient` med `background-size: 1200% 1200%` og justerbar `gradient_speed`.

**Bruk:**
- Full‑bredde, animert bakgrunn **kun i hovedfooter**.
- Innhold inni footeren skal ha lesbar tekstfarge (`--kk-footer-text-color`, default svart).

### 4.5 Utkoblet / ikke i bruk
- `#F3F3F3` som flatefarge – skal ikke brukes fremover.
- Grå bakgrunner på nye flater erstattes med `#f0fff4` eller hvitt.

---

## 5) Typografi

### 5.1 Web (nettbutikk)
Kilde: `layout/theme.liquid`, `assets/base.css`.

- **Brødtekst:**
  - Font: **Quicksand**
  - Familie: `--font-body-family`
  - Standardstørrelse: ca. 15–16px (skaleres via `--font-body-scale`).
- **Overskrifter (H1–H6, .h0/.hxl/.hxxl):**
  - Fontfamilie (`--font-heading-family`):
    - `"Luckiest Guy", "Quicksand", <system‑fallbacks>`
  - Vekt: hentes fra `settings.type_header_font`, men **visuelt skal Luckiest Guy brukes**.

**Låseregel for titler (web):**
- Alle seksjons‑ og sideoverskrifter (H1–H4 og store display‑størrelser) skal bruke **Luckiest Guy**.
- Ikke overstyr heading‑familien lokalt i seksjoner/snippets.

Praktisk skala (tilpasningsvennlig mot `base.css`):
- H1: ~40–52px desktop, 30–40px mobil.
- H2: ~24–32px.
- Brødtekst: 16–18px, bildetekster 12–14px.

### 5.2 E‑post (Klaviyo)
Kilder: `klaviyo_automation/BRAND_ASSETS.md`, `kulkid_newsletter_design.html`, `WARP.md`.

- E‑postklienter støtter ikke alltid webfonter → **Luckiest Guy må representeres som bilder**.
- Overskrifter i designede moduler (f.eks. Kundeklubb‑banner, «MOTTA DIN EKSKLUSIVE RABATT»):
  - Lag teksten i Luckiest Guy.
  - Eksporter som PNG med gjennomsiktig bakgrunn.
  - Last opp til Klaviyo og bruk `img` med meningsfulle `alt`‑tekster.
- HTML‑tekst (fallback / brødtekst):
  - Font: **Quicksand** for all tekst som rendres som HTML.
  - Overskrifter uten bilde: Quicksand med `font-weight: 700` for å etterligne display‑preg.

**Viktig:**
- Ikke sett `font-family: 'Luckiest Guy'` direkte på HTML‑tekst i e‑post hvis det er kritisk copy; bruk bilde.
- Alle dynamiske felter (rabattkode, adresser osv.) skrives i Quicksand.

---

## 6) Layout & komponenter (web)
Kilder: `assets/base.css`, `sections/email-signup-banner.liquid`, `assets/kk-*`.

- **Sidebredde:** `--page-width` styres fra Theme Settings; innhold ligger i `.page-width` med horisontal padding som øker på desktop.
- **Seksjonsavstand:**
  - Mobil: `--spacing-sections-mobile` (ca. 70 % av desktop‑verdi, minimum ~20px).
  - Desktop: `--spacing-sections-desktop` (styres fra `settings.spacing_sections`).
- **Kort (produkter/blogg):**
  - Radiuser og skygger styres via `--product-card-*` / `--blog-card-*` tokens.
  - Hold kort visuelt enkle, med tydelig avstand og uten store skygger.
- **Footer‑layout:**
  - Bygget på `kk-footer__layout` (2 kolonner, faller til 1 på mobil).
  - Tekstblokker og nyhetsbrevmodul har runde hjørner (`12px`) og luft.

### 6.1 Nyhetsbrevseksjoner

**Footer‑nyhetsbrev (web):**
- Kort: `kk-footer-newsletter__card` med lys, semitransparent hvit bakgrunn over gradient.
- Input‑felt: hvite, lett skygge, Quicksand.
- Knapp: gradient‑lilla (`#6366f1 → #8b5cf6`), hvit tekst, avrundet (8px), uppercase label.

**Email‑signup‑banner (seksjon):**
- Default bakgrunn kommer fra `email-signup-banner-background.svg` (+ mobilvariant).
- På mobil med bilde bakgrunn settes:
  - `--color-foreground: 255,255,255`
  - `--color-button: 255,255,255`
  - `--color-button-text: 0,0,0`
- Skjema følger globale `field`/`button`‑tokens.

---

## 7) Knapper

### 7.1 Web
Kilde: `assets/base.css`, `layout/theme.liquid` (button‑tokens).

- Default CTA:
  - Bakgrunn: `rgb(var(--color-button))` (typisk mørk/svart i hovedfarge‑schemet).
  - Tekst: `rgb(var(--color-button-text))` (typisk hvit).
- Størrelse:
  - Min. bredde ≈ 12rem, min. høyde ≈ 4.5rem.
  - Tekststørrelse ≈ 15px, lett `letter-spacing`.
- Hjørner:
  - Styres av `--buttons-radius` (Theme Settings). Hold den **liten og skarp**, ikke pille‑form, for hoved‑CTA.
- Sekundære knapper:
  - Bruk `button--secondary`/`button--tertiary` med transparente/lette bakgrunner.

### 7.2 E‑post (Klaviyo)
Kilde: `kulkid_newsletter_design.html`.

- `.btn-primary`:
  - Bakgrunn: `#121212`, hvit tekst, Luckiest Guy look, `border-radius: 2px`.
- `.btn-pink`:
  - Bakgrunn: `#FF1493`, hvit tekst.
- Bredde: 130–150px avhengig av breakpoint.
- Bruk samme knappestil gjennom alle flows for konsistens.

---

## 8) Rainbow & andre effekter

### 8.1 Footer‑gradient (web)
- Kun i `sections/main-footer.liquid`.
- Animasjon via `rainbowGradient` og justerbar hastighet (`gradient_speed`).
- Tekst og ikoner i footeren må ha god kontrast (vanligvis svart tekst på lys gradientbakgrunn inne i kortene).

### 8.2 Rainbow‑kanter / kort
- Implementeres via pseudo‑element (`::before`) med gradient og blur.
- Bruk for å fremheve **enkeltkort** (produkt, skjema, nyhetsbrev), ikke hele seksjoner.
- Innholdet skal ligge på en **solid bakgrunn** (hvit/lys grønn) med svart tekst.

### 8.3 E‑postgradienter
- Se §4.3 – kun i e‑post, aldri direkte kopiert som sidebakgrunner på nett.

---

## 9) Bildebruk & ikoner

- Fokus: barna og fargene – tydelig motiv, lite rot.
- Bakgrunner: enkle, gjerne lyse flater eller myke gradienter.
- Unngå tunge filtere og overmetning.
- Ikoner: enkle, med konsistent strektykkelse.

**Sosiale ikoner i e‑post:**
- Alltid bruk bildefiler (PNG) som i `kulkid_newsletter_design.html` og URL‑ene i `BRAND_ASSETS.md`.
- Hver ikon er en `<a>` med `aria-label` og lenke.
- Ikke pakk ikonene inn i ekstra fargede knapper eller kapsler.

---

## 10) Språk & copy

- Korte, konkrete setninger.
- Snakk til både barn og foresatte.
- Unngå fagjargong og byråkratiske formuleringer.

**Eksempler – bra:**
- «Bygg din bundle.»
- «Velg favorittfarger.»
- «Klar, ferdig, KUL!»
- «Gi MINI looken – du tar æren.»
- «Myke basics som tåler lek hver dag.»
- «Velg én kul farge til – MINI bestemmer!»

**Eksempler – unngå:**
- «Leverage customizable multi‑variant configurations.»
- «Optimaliser konverteringsfrekvensen med modulære produktpakker.»
- «Vennligst verifiser dine preferanser i vårt lojalitetsprogram-dashboard.»
- «Opplev økt verdiskapning gjennom skalerbare barneklærsløsninger.»

**Spesifikke standarder:**
- Takkemeldinger i flows: `Tusen takk, {{ first_name }}` / `Tusen takk`.
- Levering: `Leveringstid er normalt 12-14 virkedager.`
- Overskrifter i e‑post og på web skal være korte (5–7 ord) og i tittelstil.

---

## 11) Implementasjonsreferanser

**Web (Shopify):**
- Fonter, fargetokens, radiuser: `layout/theme.liquid` (`:root`‑variabler).
- Base‑typografi, knapper, skjema: `assets/base.css`.
- Footer, gradient og nyhetsbrevkort: `sections/main-footer.liquid`, `assets/kk-section-footer.css`, `assets/kk-component-footer-newsletter.css`.
- E‑post‑signup‑banner: `sections/email-signup-banner.liquid`, `assets/section-email-signup-banner.css`.

**E‑post (Klaviyo):**
- Designkilde (single source of truth): `klaviyo_automation/templates/kulkid_newsletter_design.html`.
- Branddata og lenker: `klaviyo_automation/BRAND_ASSETS.md`.
- Regler for flows og generering: `klaviyo_automation/WARP.md`, `KLAVIYO_FLOW_BUILD.md`.

Retningslinje: **HTML‑malen er alltid autoritativ** fremfor gamle referansebilder.

---

## 12) Sjekkliste

- [x] Overskrifter på web bruker Luckiest Guy (låst via `--font-heading-family`).
- [x] Brødtekst bruker Quicksand på web og i e‑post.
- [x] Brandnavn skrevet i riktig form (KUL KID / KULKID.no).
- [x] Farger begrenset til svart/hvitt + definert sekundærpalett og gradienter.
- [x] Footer bruker animert rainbow‑gradient kun i bunnseksjonen.
- [x] E‑postknapper følger svart/rosa styles fra Klaviyo‑malen.
- [x] Takkemeldinger og leveringstekst følger standardformuleringene.
- [ ] Logo‑bruk og eventuelle nye illustrasjonsstiler er godkjent mot denne guiden.

---
Oppdater denne guiden når tema‑innstillinger (farger, typografi, radiuser) eller Klaviyo‑maler endres.
