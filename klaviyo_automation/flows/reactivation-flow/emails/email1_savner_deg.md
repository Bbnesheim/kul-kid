# Reactivation Email 1: We Miss You

**Flow:** Reactivation Flow  
**Timing:** 90 days after last purchase  
**Goal:** Re-engage inactive customers

---

## Email Metadata

**Subject Line:** Vi savner deg{% if first_name %}, {{ first_name }}{% endif %}! 💙

**Preview Text:** Det har vært en stund – kom innom og se hva som er nytt

**From Name:** KUL KID Kundeklubb  
**From Email:** post@kulkid.no

---

## Email Content (Norwegian)

### Header
**Heading:** Lenge siden sist! 👋

### Body Copy

Hei {% if first_name %}{{ first_name }}{% else %}der{% endif %}!

Det har vært en stund siden sist vi så deg. Vi håper alt står bra til!

Barna vokser fort, og vi har masse nytt siden sist du var innom.

### What's New Section

**Heading:** Hva er nytt hos KUL KID?

✨ Nye kolleksjoner for høsten  
🎨 Friske farger og mønstre  
👕 Oppdaterte størrelser  
🌟 Fortsatt samme kvalitet du elsker

### Product Showcase

**Heading:** Sjekk ut våre nyeste favoritter:

**Dynamic Product Feed:**  
Show 4 new arrivals or bestsellers from past 90 days

### Primary CTA
**Text:** Se hva som er nytt  
**Link:** https://kulkid.no/collections/new?utm_source=klaviyo&utm_medium=email&utm_campaign=reactivation_savner

### Personal Touch

**Heading:** Vi husker hva du likte! 💭

Basert på tidligere kjøp tror vi du vil like:

**Personalized Recommendations:**  
Show 3 products similar to past purchases

### Footer
Velkommen tilbake! 🌟  
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
- [x] Warm, friendly tone (brand voice)

---

## Technical Notes

- **Email Template Name:** kulkid_reactivation_savner_deg_nb
- **Klaviyo Variables:** 
  - `{{ first_name }}` with fallback "venn"
  - Product recommendations based on past purchases
  - `{{ unsubscribe_url }}`
- **Trigger:** 90 days since last order
- **Segment:** Has placed order but not in last 90 days
- **Mobile Responsive:** Yes
