# Reactivation Email 4: Last Chance

**Flow:** Reactivation Flow  
**Timing:** 21 days after reactivation email 1  
**Goal:** Final attempt to re-engage before removing from flow

---

## Email Metadata

**Subject Line:** Siste sjanse for 20% rabatt! ⏰

**Preview Text:** Din eksklusive rabatt utløper snart – vi håper å se deg igjen

**From Name:** KUL KID Kundeklubb  
**From Email:** post@kulkid.no

---

## Email Content (Norwegian)

### Header
**Heading:** Vi vil ikke gi opp! 💙

### Body Copy

Hei {% if first_name %}{{ first_name }}{% else %}der{% endif %}!

Dette er siste melding fra oss denne gangen. Din **20% rabatt** utløper snart, og vi ville ikke at du skulle gå glipp av den.

### Final Offer

**Heading:** Din siste sjanse! ⏰

**Code:** VELKOMMEN20  
**Expires:** Om 48 timer

**What you get:**  
✨ 20% på alt  
🚚 Fri frakt over 500 kr  
💚 Også på salg

### Curated Selection

**Heading:** Vi plukket ut dette for deg:

**Personalized Product Feed:**  
Show 4 products based on:
1. Past purchase behavior
2. Browsing history (if available)
3. Similar customer purchases
4. Bestsellers (fallback)

### Primary CTA
**Text:** Shop nå  
**Link:** https://kulkid.no?discount=VELKOMMEN20&utm_source=klaviyo&utm_medium=email&utm_campaign=reactivation_siste

### Preference Center

**Heading:** Ikke interessert akkurat nå?

Vi forstår! Kanskje du vil:

**Option 1:** Pause e-poster i 3 måneder  
**Option 2:** Få e-post kun ved store nyheter  
**Option 3:** Meld deg av helt

[Oppdater preferanser →]

### Goodbye (soft)

Hvis vi ikke hører fra deg, tar vi det som et tegn på at du trenger en pause. Du er alltid velkommen tilbake når det passer deg!

### Footer
Takk for tiden sammen! 💙  
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
- [x] Respectful exit option
- [x] UTM tracking in links
- [x] Graceful, non-pushy tone (brand voice)

---

## Technical Notes

- **Email Template Name:** kulkid_reactivation_siste_sjanse_nb
- **Klaviyo Variables:** 
  - `{{ first_name }}` with fallback "venn"
  - Personalized product recommendations
  - `{{ unsubscribe_url }}`
  - Preference center link
- **Discount Code:** VELKOMMEN20 (must be same as email 2)
- **Timing:** 21 days after first reactivation email
- **Expiry:** 48 hours from send
- **Exit Conditions:**
  - Order placed
  - 60 days total elapsed
  - Unsubscribed
- **Post-flow:** Suppress from reactivation for 90 days if no action
- **Mobile Responsive:** Yes
