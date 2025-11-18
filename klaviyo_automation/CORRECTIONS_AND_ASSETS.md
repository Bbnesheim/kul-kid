# Corrections Needed & Asset Inventory

**Date:** 2025-10-30  
**Status:** Action Required Before Phase 1

---

## 🚨 CRITICAL CORRECTIONS NEEDED

### 1. Border-Radius Error (ALL FILES)
**Current (WRONG):** `border-radius: 0px` in all HTML files  
**Correct (per BRAND_GUIDE.md line 94):** `border-radius: 2px`

**Affected Files:**
- ❌ `flows/welcome-flow/emails/email1_welcome_15prosent.html`
- ❌ `flows/welcome-flow/emails/email2_merkehistorie.html`
- ❌ All markdown files reference "0px border-radius"
- ❌ `BRAND_ASSETS.md` incorrectly states "0px"
- ❌ `EXECUTION_GUIDE.md` mentions "sharp corners"

**Must fix:**
- All existing HTML button elements
- All discount code boxes
- All collection cards
- Social media buttons
- All future generated templates

---

## ✅ AVAILABLE ASSETS

### Icons Directory: `/home/ben/projects/kul-kid/klaviyo_automation/icons/`

**Social Media Icons (SVG):**
- ✅ `instagram-icon.svg` (1.1KB)
- ✅ `facebook-icon.svg` (437 bytes)
- ✅ `spotify-icon.svg` (687 bytes)
- ✅ `tiktok-icon.svg` (438 bytes)
- ✅ `youtube-icon.svg` (1.4KB)

**Brand Assets:**
- ✅ `KUL_KID_Kundeklubb.svg` (22KB) - NEW club icon
- ✅ `KUL_KID_Banner.webp` (315KB) - NEW banner image

**Main Assets Directory:** `/home/ben/projects/kul-kid/assets/`
- ✅ All social icons also available here
- ✅ Email banner backgrounds available

---

## 📧 EMAIL TEMPLATE REQUIREMENTS

### Social Media Section (Enhanced)

Instead of text-only buttons, use **clickable icon images**:

#### Current Implementation (Text Only):
```html
<a href="https://instagram.com/kulkidno" style="background-color: #334FB4; color: #FFFFFF; padding: 10px 20px; text-decoration: none; border-radius: 0; font-size: 14px;">
    @kulkidno
</a>
```

#### NEW Implementation (Icons + Text):
```html
<!-- Social Media Section with Icons -->
<tr>
    <td align="center" style="padding: 20px 40px 40px; border-top: 1px solid #121212;">
        <p style="font-size: 14px; color: #121212; margin-bottom: 15px; font-family: 'Quicksand', sans-serif;">
            Følg oss på sosiale medier!
        </p>
        <table cellspacing="0" cellpadding="0" border="0" align="center">
            <tr>
                <!-- Instagram -->
                <td style="padding: 0 8px;">
                    <a href="https://instagram.com/kulkidno?utm_source=klaviyo&utm_medium=email&utm_campaign=welcome" style="display: inline-block;">
                        <img src="https://cdn.shopify.com/s/files/1/STORE_ID/instagram-icon.svg" alt="Instagram" width="32" height="32" style="display: block; border-radius: 2px;">
                    </a>
                </td>
                <!-- Facebook -->
                <td style="padding: 0 8px;">
                    <a href="https://facebook.com/kulkidno?utm_source=klaviyo&utm_medium=email&utm_campaign=welcome" style="display: inline-block;">
                        <img src="https://cdn.shopify.com/s/files/1/STORE_ID/facebook-icon.svg" alt="Facebook" width="32" height="32" style="display: block; border-radius: 2px;">
                    </a>
                </td>
                <!-- Spotify -->
                <td style="padding: 0 8px;">
                    <a href="https://open.spotify.com/artist/5gUHOcGdJU7evr7qx0cvjN?utm_source=klaviyo&utm_medium=email&utm_campaign=welcome" style="display: inline-block;">
                        <img src="https://cdn.shopify.com/s/files/1/STORE_ID/spotify-icon.svg" alt="Spotify" width="32" height="32" style="display: block; border-radius: 2px;">
                    </a>
                </td>
                <!-- TikTok (Coming Soon - Optional) -->
                <td style="padding: 0 8px;">
                    <a href="https://tiktok.com/@kulkidno?utm_source=klaviyo&utm_medium=email&utm_campaign=welcome" style="display: inline-block; opacity: 0.5;" title="Kommer snart">
                        <img src="https://cdn.shopify.com/s/files/1/STORE_ID/tiktok-icon.svg" alt="TikTok" width="32" height="32" style="display: block; border-radius: 2px;">
                    </a>
                </td>
            </tr>
        </table>
    </td>
</tr>
```

---

## 🎨 BANNER IMAGE USAGE

**Asset:** `KUL_KID_Banner.webp` (315KB)

**Use in:**
- Welcome Email 1 (header/hero section)
- Brand Story Email
- Community emails

**Implementation:**
```html
<!-- Hero Banner -->
<tr>
    <td align="center" style="padding: 0;">
        <img src="https://cdn.shopify.com/s/files/1/STORE_ID/KUL_KID_Banner.webp" 
             alt="KUL KID Kundeklubb" 
             width="600" 
             style="display: block; width: 100%; max-width: 600px; height: auto; border-radius: 2px 2px 0 0;">
    </td>
</tr>
```

---

## 🏷️ KUNDEKLUBB ICON USAGE

**Asset:** `KUL_KID_Kundeklubb.svg` (22KB)

**Use as:**
- Email header logo alternative
- Section divider
- Badge/stamp for exclusive offers

**Implementation:**
```html
<!-- Kundeklubb Badge -->
<div style="text-align: center; margin: 20px 0;">
    <img src="https://cdn.shopify.com/s/files/1/STORE_ID/KUL_KID_Kundeklubb.svg" 
         alt="KUL KID Kundeklubb" 
         width="80" 
         height="80" 
         style="display: inline-block;">
</div>
```

---

## 📋 BEFORE PHASE 1 CHECKLIST

### Files I Need to Fix:
- [ ] Update `flows/welcome-flow/emails/email1_welcome_15prosent.html` (border-radius: 0→2px)
- [ ] Update `flows/welcome-flow/emails/email2_merkehistorie.html` (border-radius: 0→2px)
- [ ] Update all markdown files (documentation correction)
- [ ] Update `BRAND_ASSETS.md` (border-radius correction)
- [ ] Update `EXECUTION_GUIDE.md` (remove "sharp corners" references)

### New Files I Need to Create:
- [ ] `klaviyo_automation/ASSET_URLS.md` - CDN URLs for all icons
- [ ] Email template with social icons (new version)
- [ ] Email template with banner image (hero version)

### What YOU Need to Provide:
- [ ] **Shopify Store ID** (for CDN URLs: `cdn.shopify.com/s/files/1/YOUR_STORE_ID/...`)
- [ ] **Upload icons to Shopify Files:**
  1. Go to Shopify Admin → Settings → Files
  2. Upload all 7 files from `klaviyo_automation/icons/`
  3. Copy CDN URLs for each file
  4. Provide URLs to me

**OR**
- [ ] **Upload to Klaviyo Image Library:**
  1. Klaviyo → Content → Images
  2. Upload all icons
  3. Get Klaviyo CDN URLs
  4. Provide URLs to me

---

## 🔗 SOCIAL MEDIA LINKS (Confirmed)

**Active:**
- Instagram: `https://instagram.com/kulkidno`
- Facebook: `https://facebook.com/kulkidno`
- Spotify: `https://open.spotify.com/artist/5gUHOcGdJU7evr7qx0cvjN`

**Coming Soon:**
- TikTok: URL pending (show icon grayed out with "Kommer snart" tooltip)
- YouTube: URL pending (omit from emails for now)

---

## 🎯 CORRECT BRAND SPECIFICATIONS

### Border Radius Rules:
✅ **Buttons:** `2px` (per BRAND_GUIDE.md line 94)  
✅ **Cards:** `2px` (following button standard)  
✅ **Discount boxes:** `2px`  
✅ **Social icons:** `2px`  
✅ **Images:** `2px` for decorative, `0px` for full-bleed  
❌ **Variant pills:** `~40px` (exception - rounded for playful selectors)

### Colors:
- Black: `#121212`
- White: `#FDFDFD`
- Light Green: `#f0fff4` (use instead of greys for backgrounds)
- Green: `#4d6d5d` (detailing, accents)
- Accent: `#334FB4` (social button blue)
- Rainbow gradients: accent effects only.

### Fonts:
- Headings (web): `Luckiest Guy`.
- Headings (email): Luckiest Guy look via PNG images with transparent background, uploaded to Klaviyo; **fallback font is Quicksand set to `font-weight: 700`**.
- Body: `Quicksand`.

---

## 🚀 EXECUTION PLAN UPDATE

### BEFORE starting Phase 1:

**Step 1: YOU upload assets** (10 min)
```bash
# Option A: Shopify Files
1. Go to Shopify Admin → Settings → Files
2. Upload these 7 files:
   - instagram-icon.svg
   - facebook-icon.svg
   - spotify-icon.svg
   - tiktok-icon.svg
   - youtube-icon.svg
   - KUL_KID_Kundeklubb.svg
   - KUL_KID_Banner.webp
3. Copy CDN URL for each
4. Send me the URLs

# Option B: Klaviyo Library (Recommended)
1. Klaviyo → Content → Images
2. Click "Upload Images"
3. Upload all 7 files
4. Copy Klaviyo CDN URLs
5. Send me the URLs
```

**Step 2: I fix existing files** (10 min)
- Fix border-radius in 2 existing HTML files
- Update documentation
- Add asset URL configuration file

**Step 3: I create enhanced templates** (40 min)
- New social media section with clickable icons
- Hero banner implementation
- Kundeklubb badge integration
- All 14 emails with corrected styling

**Step 4: YOU run script** (2 min)
- Same as before: `python3 scripts/generate_html_templates.py`

---

## 📧 EMAIL TEMPLATE VARIATIONS

I'll create 3 template types:

### Type A: Standard (No Banner)
- Text header with KUL KID Kundeklubb
- Main content
- Social icons footer
- Used for: Transactional, updates, reminders

### Type B: Hero Banner
- Full-width banner image at top
- Main content
- Social icons footer
- Used for: Welcome, brand story, launches

### Type C: Badge Variant
- Kundeklubb badge/icon in header
- Main content
- Social icons footer
- Used for: Exclusive offers, VIP content

---

## ✅ WHAT I NEED FROM YOU NOW:

1. **Asset URLs** - Upload icons to Shopify/Klaviyo and send me CDN URLs
2. **Confirmation** - Approve the social icon implementation above
3. **Priority** - Which email should have the banner? (I suggest Welcome Email 1)
4. **TikTok** - Show grayed out or omit completely?

**Once you provide these, I'll:**
1. Fix all border-radius errors
2. Add clickable social icons
3. Integrate banner and kundeklubb icon
4. Generate all 14 emails with corrected branding

---

**Ready when you are!** 🚀
