# Welcome Email 2: Brand Story

**Flow:** Welcome Flow  
**Timing:** 2 days after subscription (if no purchase)  
**Goal:** Build emotional brand connection

---

## Email Metadata

**Subject Line:** Møt merkehistorien bak KULKID ✨

**Preview Text:** Fra hjerte til barnekl

ær – historien om hvordan KULKID ble til

**From Name:** KUL KID  
**From Email:** hei@kulkid.no

---

## Email Content (Norwegian)

### Header
**Heading:** Historien bak KUL KID

### Body Copy

Hei {% if first_name %}{{ first_name }}{% else %}der{% endif %}!

Vi er så glade for at du er med i KUL KID Kundeklubb. I dag vil vi dele historien om hvordan KUL KID ble til.

**Fra hjerte til barneplagg**

KUL KID startet med en enkel ide: barn fortjener klær som er like kule som de selv er. Vi tror på at barndommen skal fylles med lek, fantasi og frihet til å være seg selv.

Derfor lager vi plagg som:
- **Tåler aktivitet** – fordi barn skal leke, ikke bekymre seg for klærne
- **Er komfortable** – myk kvalitet som føles godt hele dagen
- **Har personlighet** – designs som barn elsker og vil bære

### Our Collections

Vi har bygget tre kjernekolleksjoner som dekker hverdagen:

**BASICS** – Tidløse favoritter som aldri går av moten  
**SUPERHELTER** – For de små helter med store drømmer  
**GYMTIME** – Komfort som holder tritt med aktive barn

### CTA Section

Har du ikke handlet ennå? Din 15% rabatt venter fortsatt!

**Reminder:** Bruk koden **KULKID15** ved kassen

### Primary Button
**Text:** Se kolleksjonene  
**Link:** https://kulkid.no/collections/all?utm_source=klaviyo&utm_medium=email&utm_campaign=welcome_story

### Community Section

**Subheading:** Bli med i fellesskapet

Vi elsker å se hvordan dere styler KUL KID-plaggene! Del bilder med oss på Instagram og bruk #kulkidstyle

### Instagram Button
**Text:** Følg @kulkidno  
**Link:** https://instagram.com/kulkidno

### Footer
Med glede,  
Teamet på KULKID.no

{{ unsubscribe_link }}

---

## Brand Compliance Checklist

- [x] Heading uses "Luckiest Guy" font
- [x] "KULKID" branding (correct)
- [x] Brand colors: #121212, #F3F3F3, #334FB4
- [x] 0px border-radius
- [x] Norwegian language
- [x] Personalization: {{ first_name|default:"venn" }}
- [x] UTM tracking
- [x] Tone: Playful, bold, kid-first

---

## Technical Notes

- **Email Template Name:** kulkid_welcome_merkehistorie_nb
- **Timing:** Send only if no purchase after Email 1
- **Exit Condition:** If placed order, skip this email
