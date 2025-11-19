# KUL KID Klaviyo Automation - Setup & Status Guide

**Status:** ⚠️ In Progress – Template, assets, and flow configs ready; most email content still to be generated  
**Last Updated:** 2025-11-19

---

## 📋 Quick Start

This folder contains everything needed to set up automated email flows for KUL KID Kundeklubb in Klaviyo.

### What's here right now
- ✅ **HTML email template:** `templates/kulkid_newsletter_design.html` – single source of truth for design (see `WARP.md`).
- ✅ **Klaviyo setup docs:** `KLAVIYO_FLOW_BUILD.md`, `template_ready.md`, `FILE_FUNCTIONS.md`.
- ✅ **Brand assets & rules:** `BRAND_ASSETS.md` + project root `BRAND_GUIDE.md`.
- ✅ **Klaviyo API test script:** `simple_upload.py` (single-template upload).
- ✅ **Flow configuration JSONs:**
  - `flows/welcome-flow/flow-config.json`
  - `flows/first-order-flow/flow-config.json`
  - `flows/cart-abandonment-flow/flow-config.json`
  - `flows/reactivation-flow/flow-config.json`
- ✅ **Email HTML already created:**
  - `flows/welcome-flow/emails/email1_double_optin_confirmation.html`
  - `flows/welcome-flow/emails/email2_welcome_discount15.html`
- ✅ **Assets folder for email:**
  - `assets/banner/` (email banner images)
  - `assets/logo/` (KUL KID Kundeklubb logo)
  - `assets/icons/` (social icons)
  - `assets/font/` (Luckiest Guy TTF for reference)
- ✅ **Helper script stub:** `scripts/generate_remaining_emails.sh` (structure/logging only – no content generation yet).

### Still missing / to be generated
- 📧 Markdown + HTML files for all remaining emails (all flows except the 2 welcome emails above).
- 📄 Markdown source for existing welcome emails (currently only HTML exists).
- 🔧 Enhanced automation scripts (planned but **not yet present**):
  - `scripts/batch_upload_all.py`
  - `scripts/validate_templates.py`
  - `scripts/test_emails.py`
  - Any `upload_templates.py` batch uploader referenced in older docs.
- 🧾 Updated progress tracking in `GENERATION_PROGRESS.md` (currently aspirational, not reflecting the real file set).

---

## 🎯 Current Status

### Completed
1. ✅ Brand guides written (`BRAND_GUIDE.md`, `BRAND_ASSETS.md`).
2. ✅ Base HTML template created in `templates/kulkid_newsletter_design.html` with proper KUL KID branding.
3. ✅ Core flows defined at config level (`flows/*/flow-config.json`).
4. ✅ Welcome flow double opt‑in + first discount email HTML created.
5. ✅ Assets folder populated with logo, banner, icons, and font file.
6. ✅ High-level action plan documented in `KLAVIYO_FLOW_BUILD.md` and file roles in `FILE_FUNCTIONS.md`.

### In progress / not yet done
1. ❌ Markdown + HTML files for:
   - First Order Flow emails
   - Cart Abandonment Flow emails
   - Reactivation Flow emails
2. ❌ Batch upload + validation scripts (Python) – currently only `simple_upload.py` and the shell stub exist.
3. ❌ `GENERATION_PROGRESS.md` and some parts of `FILE_FUNCTIONS.md` still describe future files (e.g. `kulkid_template_final.html`, `upload_templates.py`). Treat those sections as a roadmap, not as ground truth.

---

## 📧 Flows (based on current flow-config.json files)

### 1. Welcome Flow
- **Trigger:** Subscribed to main list (double opt‑in).
- **Emails in config:**
  - `email1_double_optin_confirmation.html` – confirmation email after signup.
  - `email2_welcome_discount15.html` – delivers 15% sign‑up rabattkode after confirmation.

### 2. First Order Flow (Post‑purchase)
- **Trigger:** `Placed Order` (first order only).
- **Emails in config (3 HTML templates to be created):**
  - `email1_takk_for_din_ordre.html` – thank‑you / what happens next.
  - `email2_ikke_glem_a_bruke_rabattkoden_din.html` – reminder to use welcome code.
  - `email3_koden_din_utloper_om_48_timer.html` – urgency email when code is about to expire.

### 3. Cart Abandonment Flow
- **Trigger:** `Started Checkout` without completed order.
- **Emails in config (4 HTML templates to be created):**
  - `email1_du_glemte_noe.html` – reminder.
  - `email2_trenger_du_hjelp.html` – offer help.
  - `email3_ekstra_rabatt.html` – incentive.
  - `email4_siste_sjanse.html` – final reminder.

### 4. Reactivation Flow (Win‑back)
- **Trigger:** Segment of previous customers inactive for 90+ days.
- **Emails in config (4 HTML templates to be created):**
  - `email1_savner_deg.html`
  - `email2_tilbud.html`
  - `email3_bestselgere.html`
  - `email4_siste_sjanse.html`

For detailed timing, triggers and smart‑sending rules, see each `flows/*/flow-config.json` file and `KLAVIYO_FLOW_BUILD.md`.

---

## 📂 Current File Structure (audited)

```text
klaviyo_automation/
├── README.md
├── BRAND_ASSETS.md
├── FILE_FUNCTIONS.md
├── GENERATION_PROGRESS.md   # Progress doc – currently out of sync with real files
├── KLAVIYO_FLOW_BUILD.md
├── WARP.md
├── simple_upload.py
├── template_ready.md
├── assets/
│   ├── banner/
│   │   ├── email-banner.png
│   │   └── KULKID_banner.png
│   ├── font/
│   │   └── LuckiestGuy-Regular.ttf
│   ├── icons/
│   │   ├── facebook-icon.svg
│   │   ├── instagram-icon.svg
│   │   ├── spotify-icon.svg
│   │   ├── tiktok-icon.svg
│   │   └── youtube-icon.svg
│   └── logo/
│       └── KUL_KID_Kundeklubb.svg
├── flows/
│   ├── welcome-flow/
│   │   ├── flow-config.json
│   │   └── emails/
│   │       ├── email1_double_optin_confirmation.html
│   │       └── email2_welcome_discount15.html
│   ├── first-order-flow/
│   │   ├── flow-config.json
│   │   └── emails/           # currently empty
│   ├── cart-abandonment-flow/
│   │   ├── flow-config.json
│   │   └── emails/           # currently empty
│   └── reactivation-flow/
│       ├── flow-config.json
│       └── emails/           # currently empty
├── scripts/
│   └── generate_remaining_emails.sh
└── templates/
    └── kulkid_newsletter_design.html
```

---

## 🚀 How to Execute (given the current state)

### Phase 1: Prerequisites (YOU – 30–60 min)
- Get Klaviyo API key and confirm Shopify ↔ Klaviyo integration.
- Create discount codes in Shopify:
  - `KULKID15` – 15% welcome discount (7‑day validity).
  - `VELKOMMEN` – 20% reactivation discount (14‑day validity).
- Ensure brand assets in this folder are also uploaded to Klaviyo image library.

### Phase 2: Content Generation (AI + YOU)
- Generate markdown + HTML for all missing emails using `templates/kulkid_newsletter_design.html` as the base.
- Align filenames with the ones referenced in each `flow-config.json`.
- Keep Norwegian (Bokmål) copy, KUL KID tone, and brand rules from `BRAND_GUIDE.md` / `BRAND_ASSETS.md`.

### Phase 3: Automation Scripts (planned)
- Implement Python scripts in `scripts/` (not yet present):
  - `batch_upload_all.py` – upload all templates.
  - `validate_templates.py` – basic HTML/link checks.
  - `test_emails.py` – send a test for each template.

### Phase 4: Upload & Setup (YOU)
- Use `simple_upload.py` for initial API testing.
- Once batch scripts exist, upload all templates, then wire them into flows in the Klaviyo UI following `KLAVIYO_FLOW_BUILD.md`.

---

## 📚 Documentation

- **Master action plan:** `KLAVIYO_FLOW_BUILD.md` (full flow design + execution steps).
- **Manual setup path:** `template_ready.md` (UI‑only, no scripts required).
- **File roles & roadmap:** `FILE_FUNCTIONS.md` (note: some sections describe planned future files).
- **Brand details:** `/home/ben/projects/kul-kid/BRAND_GUIDE.md` and `BRAND_ASSETS.md`.

---

## 🔧 Key Existing Files

### `templates/kulkid_newsletter_design.html`
Brand‑aligned Klaviyo‑ready HTML email template with:
- Luckiest Guy look for headings (image‑based) + Quicksand as text fallback.
- Brand colors (#121212, #FDFDFD, #f0fff4, #334FB4, #4d6d5d).
- 0px border‑radius (sharp corners).
- Mobile‑first, table‑based layout suitable for email clients.
- Slots for dynamic content and collection links.

### `simple_upload.py`
Minimal Python script to upload a single Norwegian welcome template via the Klaviyo API.
- Use it to test that your API key and environment are working.

### `scripts/generate_remaining_emails.sh`
Shell script stub that logs intended generation steps.
- Does **not** generate real content; treat it as a placeholder / scaffold.

### `template_ready.md`
Manual setup guide for:
- Creating templates directly in Klaviyo.
- Copy‑pasting HTML from `templates/kulkid_newsletter_design.html`.
- Setting up custom properties via UI.

---

## ⚠️ Important Notes

1. **Language:** All email content must be Norwegian (Bokmål).
2. **Brand name usage (from `BRAND_ASSETS.md`):**
   - In text: use **"KUL KID"**, **"KUL KID Kundeklubb"**, **"KUL KID Kundeklubb's"**.
   - For domain & URLs: use **`KULKID.no`** or **`www.KULKID.no`**.
   - Avoid forms like "Kul Kid", "kulkid" (in body text), or hyphenated variants.
3. **Headings:** Must visually use Luckiest Guy (image‑based) or Quicksand `font-weight: 700` fallback.
4. **Corners:** 0px border‑radius on all buttons/cards.
5. **GDPR:** All templates must include Klaviyo’s unsubscribe + sender address.

---

## 📞 Support

For questions or issues:
1. Check `KLAVIYO_FLOW_BUILD.md` → Troubleshooting.
2. Review Klaviyo API docs: https://developers.klaviyo.com.
3. Use an email testing tool (Litmus, Email on Acid, etc.) or your email client’s preview to validate HTML until `scripts/validate_templates.py` exists.

---

**Ready to continue?** Once prerequisites are done, focus on generating the missing email files so they match the filenames and logic defined in `flows/*/flow-config.json`.
