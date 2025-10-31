# First Order Email 5: Referral Program

**Flow:** First Order Flow  
**Timing:** 21 days after first purchase  
**Goal:** Drive referrals and word-of-mouth growth

---

## Email Metadata

**Subject Line:** Del KUL KID med en venn – dere får begge rabatt! 🎁

**Preview Text:** Gi 15% til en venn, få 15% selv når de handler

**From Name:** KUL KID Kundeklubb  
**From Email:** post@kulkid.no

---

## Email Content (Norwegian)

### Header
**Heading:** Del KUL KID med vennene dine! 🎉

### Body Copy

Hei {% if first_name %}{{ first_name }}{% else %}der{% endif %}!

Elsker du KUL KID like mye som vi håper? Del gleden med vennene dine!

### Referral Program Section

**Heading:** Slik fungerer det:

**Step 1:** Del din personlige lenke med venner  
**Step 2:** De får 15% rabatt på sitt første kjøp  
**Step 3:** Du får 15% rabatt når de handler

Alle vinner! 🌟

### Personal Referral Link
**Your unique link:**  
`{{ referral_link|default:"https://kulkid.no/pages/anbefal" }}`

### Primary CTA
**Text:** Del med venner  
**Link:** {{ referral_link|default:"https://kulkid.no/pages/anbefal?utm_source=klaviyo&utm_medium=email&utm_campaign=first_order_referral" }}

### Share Section
**Heading:** Del enkelt via:

**Email Button:** Del via e-post  
**WhatsApp Button:** Del på WhatsApp  
**Facebook Button:** Del på Facebook

### Benefits Section
**Heading:** Hvorfor dele KUL KID?

✨ Kvalitetsplagg barna elsker  
🎨 Unikt design med personlighet  
💚 Bærekraftige materialer  
📦 Rask levering over hele Norge

### Footer
Takk for at du deler KUL KID! 💙  
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
- [x] Personalization: {{ first_name }}, {{ referral_link }}
- [x] UTM tracking in links
- [x] Short, friendly copy (brand voice)

---

## Technical Notes

- **Email Template Name:** kulkid_first_order_anbefaling_nb
- **Klaviyo Variables:** 
  - `{{ first_name }}` with fallback "venn"
  - `{{ referral_link }}` (dynamic referral URL)
  - `{{ unsubscribe_url }}`
- **Referral Discount:** 15% for both referrer and referee
- **Share Buttons:** Email, WhatsApp, Facebook
- **Mobile Responsive:** Yes
