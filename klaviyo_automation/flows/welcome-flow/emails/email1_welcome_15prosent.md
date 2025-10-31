# Welcome Email 1: 15% Discount

**Flow:** Welcome Flow  
**Timing:** Immediately upon subscription  
**Goal:** Convert new subscribers to first-time buyers

---

## Email Metadata

**Subject Line:** Velkommen til KUL KID Kundeklubb! 🎉 Her er din 15% rabatt

**Preview Text:** Din personlige rabattkode venter – perfekte plagg til din lille helt

**From Name:** KUL KID Kundeklubb  
**From Email:** post@kulkid.no

---

## Email Content (Norwegian)

### Header
**Heading:** Velkommen til KUL KID Kundeklubb, {{ first_name|default:"venn" }}! 🌟

### Body Copy

Tusen takk for at du ble med i KUL KID Kundeklubb!

Vi er så glade for å ha deg med. Som takk for at du meldte deg på, får du **15% rabatt** på ditt første kjøp.

### Discount Code Box
**Label:** Din personlige rabattkode:  
**Code:** KULKID15  
**Validity:** Gyldig i 7 dager

### Main CTA
Vi ser frem til å hjelpe deg finne de perfekte plaggene! Start gjerne med å se våre mest populære kolleksjoner:

### Collection Cards

**1. BASICS**
- Link: https://kulkid.no/collections/basics
- Description: Tidløse favoritter

**2. SUPERHELTER**
- Link: https://kulkid.no/collections/superhelter
- Description: For de tøffeste

**3. GYMTIME**
- Link: https://kulkid.no/collections/gymtime
- Description: Komfort i hverdagen

### Primary Button
**Text:** Kul shopping! 👕✨  
**Link:** https://kulkid.no?utm_source=klaviyo&utm_medium=email&utm_campaign=welcome_15

### Social Section
P.S. Følg oss på Instagram for daglig inspirasjon!

**Instagram Button:**
- Text: @kulkidno
- Link: https://instagram.com/kulkidno

### Footer
Teamet på KULKID.no  
{{ unsubscribe_link }}

---

## Brand Compliance Checklist

- [x] Heading uses "Luckiest Guy" font
- [x] "KUL KID Kundeklubb" (correct branding)
- [x] Brand colors: #121212, #F3F3F3, #334FB4
- [x] 0px border-radius (sharp corners)
- [x] Norwegian language (Bokmål)
- [x] Personalization: {{ first_name|default:"venn" }}
- [x] UTM tracking in links
- [x] Instagram: @kulkid.no
- [x] Website: KULKID.no (all caps)

---

## Technical Notes

- **Email Template Name:** kulkid_welcome_15prosent_nb
- **Klaviyo Variables:** 
  - `{{ first_name }}` with fallback "venn"
  - `{{ unsubscribe_url }}` in footer
- **Mobile Responsive:** Yes
- **Plain Text Version:** Auto-generated from HTML
