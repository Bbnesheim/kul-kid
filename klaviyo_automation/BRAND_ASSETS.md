# KULKID Brand Assets Reference

**Last Updated:** 2025-10-30

---

## 🌐 Social Media Channels

### Active Channels:

**Instagram**
- Handle: `@kulkidno`
- URL: `https://instagram.com/kulkidno`
- Primary: ✅ (Main social channel)

**Facebook**
- Page: `kulkidno`
- URL: `https://facebook.com/kulkidno`
- Active: ✅

**Spotify**
- Artist Profile
- URL: `https://open.spotify.com/artist/5gUHOcGdJU7evr7qx0cvjN`
- Active: ✅

### TikTok
- Handle: `@kulkidno`
- URL: `https://www.tiktok.com/@kulkidno`
- Active: ✅

### YouTube
- Channel: `KUL KID`
- URL: `https://www.youtube.com/@KULKIDno`
- Active: ✅

---

## 🎨 Brand Colors

**Core Colors:**
- **Black:** `#121212`
- **White:** `#FDFDFD`
- **Rainbow Gradients:** Used as accents only (see codebase for implementations).

**Secondary Colors:**
- **Green:** `#4d6d5d` – detailing, accents, and text on light backgrounds.
- **Light Green:** `#f0fff4` – use instead of greys for backgrounds and soft surfaces.

**Deprecated:**
- `#F3F3F3` surface grey – do not use going forward.
- Replace any remaining greys used as surfaces with `#f0fff4` or white.

---

## 🔤 Typography

**Headings (Web):**
- Font: Luckiest Guy (Google Fonts)
- Weight: 400 (only weight available)
- **LOCKED:** Use for title headings on the website.

**Headings (Email / Klaviyo):**
- Visual font: Luckiest Guy represented as **PNG images with transparent background**.
- Workflow:
  - Design the heading text in Luckiest Guy.
  - Export as PNG with transparent background.
  - Upload to Klaviyo Images and use the image URL in the email HTML (see `templates/kulkid_newsletter_design.html` for examples).
- **Fallback when no image `src` is provided:** use **Quicksand with `font-weight: 700`** for headings.

**Body:**
- Font: Quicksand (Google Fonts)
- Weights: 400, 500, 700
- Default: 400-500

---

## 🔗 Website & Links

**Primary Domain:** `https://kulkid.no`

**Collection URLs:**
- Basics: `https://kulkid.no/collections/basics`
- Gymtime: `https://kulkid.no/collections/gymtime`
- Skole & Sekk: `https://kulkid.no/collections/skole`
- Superhelter: `https://kulkid.no/collections/superhelter`
- Superkul: `https://kulkid.no/collections/superkul`
- All: `https://kulkid.no/collections/all`

**Contact:**
- Email: `kontakt@kulkid.no`

---

## 📷 Image Assets

### Logo
- Filename: `Kul_Kid_Logo.svg`
- Location: Shopify Files (Settings → Files)
- Usage: Email headers, social profiles

### Product Images
- Source: Shopify product library
- Collections: BASICS, SUPERHELTER, GYMTIME
- To upload: Hero images for each collection

---

## 💬 Brand Voice

**Tone:** Playful, bold, kid-first

**Characteristics:**
- Short, punchy sentences
- Active verbs
- Speak to both kids and parents
- Encourage creativity and play

**Do:**
- ✅ "Kul shopping!"
- ✅ "Perfekte plagg til din lille helt"
- ✅ "Klar, ferdig, KUL!"
- ✅ "Gi MINI looken – du tar æren."
- ✅ "Myke favoritter som tåler lek hver dag."
- ✅ "Velg én kul farge til – MINI bestemmer!"

**Don’t (examples of what to avoid):**
- ❌ "Leverage customizable configurations"
- ❌ "Optimaliser konverteringsfrekvensen med modulære outfits."
- ❌ "Vennligst verifiser bestillingen i vårt system for å fortsette."
- ❌ "Utforsk vår omfattende produktportefølje for barn og unge."
- ❌ "Dine preferanser er registrert i vårt lojalitetsprogram-dashbord."

---

## 🎯 Brand Name Usage

**IMPORTANT: In all text content, ALWAYS use "KUL KID" (with space), never "KULKID" (no space)**

**Correct:**
- KUL KID (in body text and headings)
- KUL KID's (possessive form)
- KUL KID Kundeklubb (customer club)
- KUL KID Kundeklubb's (possessive)
- www.KULKID.no (website URL only)
- KULKID.no (website references)

**Incorrect:**
- ❌ KULKID (no space in body text - only acceptable in domain/URLs)
- ❌ Kul Kid (title case)
- ❌ kulkid (lowercase in formal contexts)
- ❌ Kul-Kid (hyphenated)
- ❌ KULKID-fellesskapet (should be: KUL KID-fellesskapet)
- ❌ KULKID-plagg (should be: KUL KID-plagg)

---

## 📱 Social Media Buttons (Email)

We use **icon images as buttons**, not styled HTML `<button>`/CTA blocks.
All implementations must follow the pattern in `templates/kulkid_newsletter_design.html` lines 367–383 (icon-only links in a row).

**Implementation Rules:**
- Use the provided PNG/SVG icons only (Instagram, Facebook, TikTok, Spotify, YouTube).
- Wrap each icon in an `<a>` tag with proper `aria-label` and target URL.
- Do **not** add extra backgrounds, rounded rectangles, or text labels around the icons.
- Do **not** create new button styles (colors, borders, shapes) beyond what the icons themselves provide.

**Current Icon Assets (source of truth):**
- Instagram icon `src` → `https://d3k81ch9hvuctc.cloudfront.net/company/XkZSsU/images/63d711c6-fdb4-4332-bea5-fc3b915573ed.png`
- Facebook icon `src` → `https://d3k81ch9hvuctc.cloudfront.net/company/XkZSsU/images/b66cd375-8d50-4bc2-b2e5-dc91f5e6abb3.png`
- TikTok icon `src` → `https://d3k81ch9hvuctc.cloudfront.net/company/XkZSsU/images/a8f7daab-6bc7-4251-854d-5703cd7eea88.png`
- Spotify icon `src` → `https://d3k81ch9hvuctc.cloudfront.net/company/XkZSsU/images/a7f77e15-dd31-4fa0-bd6e-c0c13bd68bb1.png`
- YouTube icon `src` → `https://d3k81ch9hvuctc.cloudfront.net/company/XkZSsU/images/599f3d9a-73b5-40ba-b689-69617fa1e918.png`

---

## 🏷️ Hashtags

**Primary:**
- `#kulkidstyle` (for UGC content)
- `#kulkid` (general brand tag)

---

## 📋 Discount Codes

**Active Codes:**
- `KULKID15` - 15% off welcome discount (7-day validity)
- `VELKOMMEN` - 20% off reactivation (14-day validity)

---

## 🎵 Spotify Integration

**Artist Page:** [KULKID on Spotify](https://open.spotify.com/artist/5gUHOcGdJU7evr7qx0cvjN)

**Usage in Emails:**
- Could be featured in brand story emails
- Community building content
- Behind-the-scenes content

---

## 📧 Email Signature

**Standard Footer:**
```
Teamet på KULKID.no
{{ unsubscribe_url }}
```

**With Social Links:**
```
Følg oss:
Instagram: @kulkidno | Facebook: kulkidno

Teamet på KULKID.no
{{ unsubscribe_url }}
```

---

## 🚀 Future Channels

*(Currently all planned channels are active. Use this section for truly new platforms only.)*

---

## 📝 Usage Notes for Email Templates

1. **Primary Social CTA:** Always Instagram first (@kulkidno) using the icon button style from `templates/kulkid_newsletter_design.html`.
2. **Secondary Social:** Facebook for broader reach (icon button only).
3. **Spotify:** Use in brand story/community emails (icon button only).
4. **Do not create new social button shapes or styles** – only use the icon-row pattern with images as buttons.
5. **UTM Tracking:** Always add to social links in emails:
   - `?utm_source=klaviyo&utm_medium=email&utm_campaign=[campaign_name]`

---

**Questions?** Refer to `/home/ben/projects/kul-kid/BRAND_GUIDE.md` for complete brand specifications.
