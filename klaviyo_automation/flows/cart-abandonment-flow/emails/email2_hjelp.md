# Cart Abandonment Email 2: Help & Support

**Flow:** Cart Abandonment Flow  
**Timing:** 6 hours after cart abandonment  
**Goal:** Address potential concerns or questions

---

## Email Metadata

**Subject Line:** Trenger du hjelp med bestillingen? 💬

**Preview Text:** Vi er her for å hjelpe deg – handlekurven din er fortsatt tilgjengelig

**From Name:** KUL KID Kundeklubb  
**From Email:** post@kulkid.no

---

## Email Content (Norwegian)

### Header
**Heading:** Kan vi hjelpe deg? 🤝

### Body Copy

Hei {{ first_name|default:"venn" }}!

Vi så at du fortsatt ikke har fullført bestillingen din. Kanskje du lurer på noe?

### FAQ Section

**Heading:** Ofte stilte spørsmål:

**Q: Hva er fraktkostnadene?**  
A: Fri frakt over 500 kr. Under 500 kr koster frakt 49 kr.

**Q: Hvor lang er leveringstiden?**  
A: 2-4 virkedager med Posten/Bring.

**Q: Kan jeg returnere hvis det ikke passer?**  
A: Absolutt! 30 dagers åpent kjøp, ingen spørsmål stilt.

**Q: Er størrelsene riktige?**  
A: Vi har størrelsesguide på hver produktside. Kontakt oss hvis du er usikker!

### Cart Reminder
**Heading:** Dine valgte produkter:

**Dynamic Cart Feed** (same as email 1)

### Primary CTA
**Text:** Fullfør bestillingen  
**Link:** {{ checkout_url }}

### Contact Section
**Heading:** Fortsatt usikker?

Kontakt oss direkte – vi svarer raskt!

**Email:** post@kulkid.no  
**Instagram:** @kulkidno

### Footer
Vi er her for deg! 💙  
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
- [x] Short, helpful copy (brand voice)

---

## Technical Notes

- **Email Template Name:** kulkid_cart_hjelp_nb
- **Klaviyo Variables:** 
  - `{{ first_name }}` with fallback "venn"
  - `{{ checkout_url }}`
  - Cart items loop
  - `{{ unsubscribe_url }}`
- **Timing:** Send 6 hours after checkout started (5 hours after email 1)
- **Exit Condition:** Order placed
- **Mobile Responsive:** Yes
