# Cart Abandonment Email 4: Last Chance

**Flow:** Cart Abandonment Flow  
**Timing:** 48 hours after cart abandonment  
**Goal:** Final reminder before cart expires

---

## Email Metadata

**Subject Line:** Siste sjanse! Rabatten din utløper snart ⏰

**Preview Text:** Handlekurven din og 10% rabatten er kun tilgjengelig i noen timer til

**From Name:** KUL KID Kundeklubb  
**From Email:** post@kulkid.no

---

## Email Content (Norwegian)

### Header
**Heading:** Siste sjanse! ⏰

### Body Copy

Hei {% if first_name %}{{ first_name }}{% else %}der{% endif %}!

Dette er en siste påminnelse – både handlekurven din og **10% rabatten** utløper om få timer.

### Urgency Section

**Countdown Timer (if possible):**  
Utløper om: [XX timer XX minutter]

**Or static text:**  
⏰ **Kun noen timer igjen!**

### Cart Items
**Heading:** Ikke gå glipp av disse:

**Dynamic Cart Feed**

### Discount Reminder

**Code:** FULLFOR10  
**Savings:** Spar {{ savings }} kr på denne bestillingen!

### Primary CTA
**Text:** Fullfør bestillingen nå  
**Link:** {{ checkout_url }}?discount=FULLFOR10

### Scarcity Section (if applicable)

**Stock Alert:**  
⚠️ Noen av produktene i handlekurven din har begrenset lagerbeholdning.

### Alternative Section
**Heading:** Ikke det du leter etter?

Se andre populære valg:

**Product Recommendations:**  
Show 3 bestsellers or similar products

### Footer
Vi håper å se deg snart! 👋  
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
- [x] Urgency without being aggressive (brand voice)

---

## Technical Notes

- **Email Template Name:** kulkid_cart_siste_sjanse_nb
- **Klaviyo Variables:** 
  - `{{ first_name }}` with fallback "venn"
  - `{{ checkout_url }}`
  - `{{ savings }}`
  - Cart items loop
  - Product recommendations
  - `{{ unsubscribe_url }}`
- **Discount Code:** FULLFOR10 (must be same as email 3)
- **Timing:** Send 48 hours after checkout started (24 hours before expiry)
- **Exit Condition:** Order placed or 72 hours elapsed
- **Mobile Responsive:** Yes
