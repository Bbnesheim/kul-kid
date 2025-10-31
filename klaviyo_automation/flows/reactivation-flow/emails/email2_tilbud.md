# Reactivation Email 2: Special Offer

**Flow:** Reactivation Flow  
**Timing:** 7 days after reactivation email 1  
**Goal:** Incentivize return with exclusive discount

---

## Email Metadata

**Subject Line:** Velkommen tilbake! Her er 20% rabatt bare for deg 🎁

**Preview Text:** Din eksklusive rabatt venter – gyldig i 7 dager

**From Name:** KUL KID Kundeklubb  
**From Email:** post@kulkid.no

---

## Email Content (Norwegian)

### Header
**Heading:** Velkommen tilbake! 🎉

### Body Copy

Hei {% if first_name %}{{ first_name }}{% else %}der{% endif %}!

Vi setter virkelig pris på at du har vært kunde hos oss. Som takk for din lojalitet, vil vi gi deg en ekstra spesiell rabatt.

### Offer Section

**Heading:** Bare for deg: 20% rabatt! 🎁

**Code Display:** VELKOMMEN20

**Details:**  
✨ 20% rabatt på hele bestillingen  
⏰ Gyldig i 7 dager  
🛍️ Ingen minimumskjøp  
💚 Gjelder også salg

### Collections Showcase

**Heading:** Perfekt timing for:

**Collection Cards:**

**1. Høstkolleksjonen**  
Varme lag på lag-plagg  
[Se kolleksjonen →]

**2. Everyday Basics**  
Tidløse favoritter  
[Se kolleksjonen →]

**3. Nyheter**  
Akkurat ankommet  
[Se kolleksjonen →]

### Primary CTA
**Text:** Bruk rabatten nå  
**Link:** https://kulkid.no?discount=VELKOMMEN20&utm_source=klaviyo&utm_medium=email&utm_campaign=reactivation_tilbud

### Social Proof

**Heading:** Se hva andre foreldre sier:

**Review Highlights:**  
⭐⭐⭐⭐⭐ "Beste barneklærne vi har kjøpt!" – Maria  
⭐⭐⭐⭐⭐ "Holder vask etter vask" – Thomas  
⭐⭐⭐⭐⭐ "Barna vil ikke ha noe annet" – Linda

### Urgency

**Countdown:**  
⏰ Rabatten utløper om: 7 dager

### Footer
Vi gleder oss til å se deg igjen! 💙  
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
- [x] Personalization: {{ first_name }}
- [x] Discount: VELKOMMEN20 (20% off)
- [x] UTM tracking in links
- [x] Warm, appreciative tone (brand voice)

---

## Technical Notes

- **Email Template Name:** kulkid_reactivation_tilbud_nb
- **Klaviyo Variables:** 
  - `{{ first_name }}` with fallback "venn"
  - `{{ unsubscribe_url }}`
- **Discount Code:** VELKOMMEN20 (20% off entire order)
- **Timing:** 7 days after first reactivation email
- **Expiry:** 7 days from email send
- **Exit Condition:** Order placed
- **Mobile Responsive:** Yes
