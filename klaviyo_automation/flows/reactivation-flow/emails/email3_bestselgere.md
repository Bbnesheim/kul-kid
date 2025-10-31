# Reactivation Email 3: Bestsellers Showcase

**Flow:** Reactivation Flow  
**Timing:** 14 days after reactivation email 1  
**Goal:** Show what's popular and trending

---

## Email Metadata

**Subject Line:** Dette elsker andre foreldre akkurat nå! ⭐

**Preview Text:** Se våre mest populære plagg – kanskje noe for dere også?

**From Name:** KUL KID Kundeklubb  
**From Email:** post@kulkid.no

---

## Email Content (Norwegian)

### Header
**Heading:** Mest elsket akkurat nå! 🌟

### Body Copy

Hei {{ first_name|default:"venn" }}!

Lurer du på hva andre foreldre handler mest? Her er våre bestselgere som alle snakker om!

### Bestsellers Section

**Heading:** Topp 6 favoritter:

**Dynamic Product Feed:**  
Show 6 top-selling products from last 30 days
- Include product image
- Product name
- Price
- Star rating
- Number of reviews
- "Bestseller" badge

### Social Proof Stats

📦 Over 500 fornøyde familier  
⭐ 4.8 gjennomsnittsvurdering  
💚 95% vil anbefale videre

### Primary CTA
**Text:** Se alle bestselgere  
**Link:** https://kulkid.no/collections/bestsellers?utm_source=klaviyo&utm_medium=email&utm_campaign=reactivation_bestselgere

### Why They Love It Section

**Heading:** Derfor velger foreldre KUL KID:

**Feature 1: Kvalitet som holder**  
Tåler både lek og vask, dag etter dag.

**Feature 2: Komfort hele dagen**  
Myke, pustende materialer barna elsker.

**Feature 3: Design med personlighet**  
Unike prints som skiller seg ut.

### Reminder: Discount Still Active

**Callout Box:**  
💡 PS: Din 20% rabatt (**VELKOMMEN20**) er fortsatt gyldig!

### Secondary CTA
**Text:** Bruk rabatten  
**Link:** https://kulkid.no?discount=VELKOMMEN20

### Footer
Håper vi sees snart! 👋  
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
- [x] UTM tracking in links
- [x] Helpful, non-pushy tone (brand voice)

---

## Technical Notes

- **Email Template Name:** kulkid_reactivation_bestselgere_nb
- **Klaviyo Variables:** 
  - `{{ first_name }}` with fallback "venn"
  - Dynamic product feed (bestsellers)
  - `{{ unsubscribe_url }}`
- **Timing:** 14 days after first reactivation email (7 days after discount email)
- **Product Feed:** Top 6 products by sales (last 30 days)
- **Discount Reminder:** VELKOMMEN20 (if still valid)
- **Exit Condition:** Order placed
- **Mobile Responsive:** Yes
