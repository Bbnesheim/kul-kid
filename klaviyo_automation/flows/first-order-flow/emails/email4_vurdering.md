# First Order Email 4: Review Request

**Flow:** First Order Flow  
**Timing:** 14 days after first purchase  
**Goal:** Generate reviews and social proof

---

## Email Metadata

**Subject Line:** Hva synes du om {{ product_name|default:"ditt KUL KID-plagg" }}? ⭐

**Preview Text:** Din mening betyr mye for oss – del gjerne dine tanker!

**From Name:** KUL KID Kundeklubb
**From Email:** post@kulkid.no

---

## Email Content (Norwegian)

### Header
**Heading:** Vi vil gjerne høre fra deg! 💬

### Body Copy

Hei {% if first_name %}{{ first_name }}{% else %}der{% endif %}!

Det har gått litt tid siden du mottok din bestilling. Vi håper dere elsker det!

Din mening betyr mye for oss og andre foreldre som vurderer samme plagg.

### Review Section

**Heading:** Vil du dele dine tanker?

Det tar bare 2 minutter å skrive en anmeldelse.

**Benefits:**
✨ Hjelp andre foreldre med valget  
💡 Del tips om passform og styling  
🌟 Alle anmeldelser blir lest av teamet vårt

### Primary CTA
**Text:** Skriv en anmeldelse  
**Link:** https://kulkid.no/pages/reviews?utm_source=klaviyo&utm_medium=email&utm_campaign=first_order_review

### Incentive (Optional)
Som takk for din anmeldelse får du **10% rabatt** på neste kjøp!

**Code:** TAKK10

### Secondary Section
**Heading:** Trenger du hjelp?

Kontakt oss gjerne hvis det er noe vi kan hjelpe deg med.

**Support CTA:**  
**Text:** Kontakt kundeservice  
**Link:** mailto:post@kulkid.no

### Footer
Tusen takk! 🙏  
Teamet på KULKID.no  
{{ unsubscribe_link }}

---

## Brand Compliance Checklist

- [x] Heading uses "Luckiest Guy" font
- [x] Brand colors: #121212, #F3F3F3
- [x] 0px border-radius (sharp corners)
- [x] Norwegian language (Bokmål)
- [x] Personalization: {{ first_name }}, {{ product_name }}
- [x] UTM tracking in links
- [x] Email: post@kulkid.no
- [x] Short, friendly copy (brand voice)

---

## Technical Notes

- **Email Template Name:** kulkid_first_order_vurdering_nb
- **Klaviyo Variables:** 
  - `{{ first_name }}` with fallback "venn"
  - `{{ product_name }}` from order
  - `{{ unsubscribe_url }}`
- **Discount Code:** TAKK10 (10% off)
- **Mobile Responsive:** Yes
