# Cart Abandonment Email 3: Special Incentive

**Flow:** Cart Abandonment Flow  
**Timing:** 24 hours after cart abandonment  
**Goal:** Provide incentive to complete purchase

---

## Email Metadata

**Subject Line:** Bare for deg: 10% rabatt på handlekurven din! 🎁

**Preview Text:** Din eksklusive rabatt utløper snart – fullfør kjøpet nå

**From Name:** KUL KID Kundeklubb  
**From Email:** post@kulkid.no

---

## Email Content (Norwegian)

### Header
**Heading:** Vi vil gjerne hjelpe deg! 💙

### Body Copy

Hei {{ first_name|default:"venn" }}!

Vi ser at du fortsatt ikke har fullført bestillingen. Som et lite dytt i riktig retning, gir vi deg **10% ekstra rabatt**!

### Discount Section

**Heading:** Din eksklusive rabattkode:

**Code Display:** FULLFOR10

**Details:**  
✨ Gyldig kun på produktene i handlekurven din  
⏰ Utløper om 48 timer  
💰 Kombineres ikke med andre tilbud

### Cart Items
**Heading:** I handlekurven din:

**Dynamic Cart Feed** (with discount applied preview)

**Savings Highlight:**  
Ordinær pris: {{ cart_total }} kr  
Med FULLFOR10: {{ discounted_total }} kr  
**Du sparer: {{ savings }} kr!**

### Primary CTA
**Text:** Bruk rabatten nå  
**Link:** {{ checkout_url }}?discount=FULLFOR10

### Urgency Section
**Heading:** ⏰ Kun 48 timer igjen!

Både rabattkoden og produktene i handlekurven din er reservert i 48 timer.

### Footer
Lykke til med handlingen! 🛍️  
Teamet på KULKID.no  
{{ unsubscribe_link }}

---

## Brand Compliance Checklist

- [x] Heading uses "Luckiest Guy" font
- [x] Brand colors: #121212, #F3F3F3
- [x] 0px border-radius (sharp corners)
- [x] Norwegian language (Bokmål)
- [x] From Name: "KUL KID Kundeklubb"
- [x] From Email: post@kulkid.no
- [x] Personalization: {{ first_name }}, {{ checkout_url }}
- [x] Discount code: FULLFOR10
- [x] Urgency without being pushy (brand voice)

---

## Technical Notes

- **Email Template Name:** kulkid_cart_insentiv_nb
- **Klaviyo Variables:** 
  - `{{ first_name }}` with fallback "venn"
  - `{{ checkout_url }}`
  - `{{ cart_total }}`, `{{ discounted_total }}`, `{{ savings }}`
  - Cart items loop
  - `{{ unsubscribe_url }}`
- **Discount Code:** FULLFOR10 (10% off cart)
- **Timing:** Send 24 hours after checkout started
- **Expiry:** 48 hours from email send
- **Exit Condition:** Order placed
- **Mobile Responsive:** Yes
