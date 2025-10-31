# First Order Email 3: Community Invite

**Flow:** First Order Flow  
**Timing:** 7 days after first purchase  
**Goal:** Build community engagement and brand loyalty

---

## Email Metadata

**Subject Line:** Bli med i KUL KID-fellesskapet! 🌟

**Preview Text:** Følg oss på sosiale medier for inspirasjon, tips og eksklusive tilbud

**From Name:** KUL KID  
**From Email:** post@kulkid.no

---

## Email Content (Norwegian)

### Header
**Heading:** Velkommen til KUL KID-familien! 🎉

### Body Copy

Hei {{ first_name|default:"venn" }}!

Nå som du er en del av KUL KID-familien, vil vi gjerne holde kontakten.

Følg oss på sosiale medier for daglig inspirasjon, styling-tips og være først ute med nye kolleksjoner!

### Social Media Section

**Instagram**
- Icon: Instagram logo
- Handle: @kulkidno
- Link: https://instagram.com/kulkidno
- Description: Styling-inspirasjon & fellesskap

**TikTok**
- Icon: TikTok logo  
- Handle: @kulkidno
- Link: https://tiktok.com/@kulkidno
- Description: Kuleste trendene

**Facebook**
- Icon: Facebook logo
- Handle: KUL KID
- Link: https://facebook.com/kulkidno
- Description: Nyheter & tips

### Community Benefits Section

**Heading:** Hva får du?

✨ Styling-inspirasjon fra andre foreldre  
🎁 Eksklusive tilbud kun for følgere  
👕 Førsterett til nye drops  
📸 Vinn premier i våre konkurranser

### Primary CTA
**Text:** Følg oss på Instagram  
**Link:** https://instagram.com/kulkidno

### UGC Call-to-Action
**Heading:** Del din stil!

Tag oss i dine bilder med **#kulkidstyle** så deler vi de beste!

### Footer
Vi ses der! 👋  
Teamet på KULKID.no  
{{ unsubscribe_link }}

---

## Brand Compliance Checklist

- [x] Heading uses "Luckiest Guy" font
- [x] Brand colors: #121212, #F3F3F3
- [x] 0px border-radius (sharp corners)
- [x] Norwegian language (Bokmål)
- [x] Personalization: {{ first_name }}
- [x] UTM tracking in social links
- [x] Short, friendly copy (brand voice)

---

## Technical Notes

- **Email Template Name:** kulkid_first_order_fellesskap_nb
- **Klaviyo Variables:** 
  - `{{ first_name }}` with fallback "venn"
  - `{{ unsubscribe_url }}`
- **Social Icons:** Use brand-compliant SVGs from assets
- **Mobile Responsive:** Yes
