# First Order Email 2: Styling Tips

**Flow:** First Order Flow  
**Timing:** 3 days after first purchase  
**Goal:** Provide value through styling inspiration

---

## Email Metadata

**Subject Line:** Slik styler du {{ product_name|default:"favorittplaggene" }} 👕✨

**Preview Text:** Enkle tips for å få mest mulig ut av ditt nye KUL KID-plagg

**From Name:** KUL KID  
**From Email:** hei@kulkid.no

---

## Email Content (Norwegian)

### Header
**Heading:** Slik styler du {{ product_name|default:"dine nye plagg" }}

### Body Copy

Hei {% if first_name %}{{ first_name }}{% else %}der{% endif %}!

Håper du elsker ditt nye KUL KID-plagg! Vi tenkte du kanskje vil ha noen tips til hvordan du kan style det.

### Styling Section

**Heading:** 3 enkle styling-tips

**Tip 1: Lag et komplett sett**  
Kombiner med joggebukse eller shorts fra samme kolleksjon. Match fargene for et helhetlig uttrykk.

**Tip 2: Lag personlig stil**  
La barnet velge favorittplagg selv. Kreativitet kommer best frem når de får bestemme!

**Tip 3: Everyday cool**  
KUL KID passer både til leken, skolen og familiemiddagen. Komfort møter stil.

### Product Recommendations
**Heading:** Perfekte kombinasjoner

Vi tror du vil like disse:

**Dynamic Product Feed:**
- Show 3 products from same collection as purchased item
- Fallback: Show bestsellers if no collection match

### Primary CTA
**Text:** Se hele kolleksjonen  
**Link:** https://kulkid.no/collections/all?utm_source=klaviyo&utm_medium=email&utm_campaign=first_order_stylingtips

### Social Proof Section
**Heading:** Del din stil! 📸

Tag oss på Instagram [@kulkidno](https://instagram.com/kulkidno) så deler vi de kuleste stylingene!

### Footer
Klem fra teamet på KULKID.no  
{{ unsubscribe_link }}

---

## Brand Compliance Checklist

- [x] Heading uses "Luckiest Guy" font
- [x] Brand colors: #121212, #F3F3F3
- [x] 0px border-radius (sharp corners)
- [x] Norwegian language (Bokmål)
- [x] Personalization: {{ first_name }}, {{ product_name }}
- [x] UTM tracking in links
- [x] Short, punchy copy (brand voice)

---

## Technical Notes

- **Email Template Name:** kulkid_first_order_stylingtips_nb
- **Klaviyo Variables:** 
  - `{{ first_name }}` with fallback "venn"
  - `{{ product_name }}` from last order
  - Dynamic product feed
  - `{{ unsubscribe_url }}`
- **Mobile Responsive:** Yes
