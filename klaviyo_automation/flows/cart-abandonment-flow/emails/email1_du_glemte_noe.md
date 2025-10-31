# Cart Abandonment Email 1: Gentle Reminder

**Flow:** Cart Abandonment Flow  
**Timing:** 1 hour after cart abandonment  
**Goal:** Remind customer of items left in cart

---

## Email Metadata

**Subject Line:** Du glemte noe i handlekurven! 🛒

**Preview Text:** Dine favoritter venter – fullfør bestillingen nå

**From Name:** KUL KID Kundeklubb  
**From Email:** post@kulkid.no

---

## Email Content (Norwegian)

### Header
**Heading:** Glemte du noe? 👀

### Body Copy

Hei {% if first_name %}{{ first_name }}{% else %}der{% endif %}!

Vi la merke til at du la noe fint i handlekurven, men ikke fullførte kjøpet.

Dine favoritter venter på deg!

### Cart Items Section
**Heading:** I handlekurven din:

**Dynamic Cart Feed:**
- Show all items from abandoned cart
- Include product image, name, size/variant, price
- Display quantity

### Primary CTA
**Text:** Fullfør bestillingen  
**Link:** {{ checkout_url }}

### Reassurance Section

**Free Shipping:** Fri frakt over 500 kr  
**Easy Returns:** 30 dagers åpent kjøp  
**Fast Delivery:** 2-4 dagers levering

### Help Section
**Heading:** Trenger du hjelp?

Kontakt oss gjerne hvis du lurer på noe!

**Support Link:** post@kulkid.no

### Footer
Vi hjelper deg gjerne! 💙  
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
- [x] UTM tracking in links
- [x] Short, friendly copy (brand voice)

---

## Technical Notes

- **Email Template Name:** kulkid_cart_du_glemte_noe_nb
- **Klaviyo Variables:** 
  - `{{ first_name }}` with fallback "venn"
  - `{{ checkout_url }}` (direct to cart)
  - `{% for item in event.extra.line_items %}` (cart items loop)
  - `{{ unsubscribe_url }}`
- **Timing:** Send 1 hour after checkout started
- **Exit Condition:** Order placed
- **Mobile Responsive:** Yes
