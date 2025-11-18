# KULKID Klaviyo Automation - Setup Guide

**Status:** ⚠️ In Progress - Files Ready for Generation  
**Last Updated:** 2025-10-30

---

## 📋 Quick Start

This folder contains everything needed to set up automated email flows for KULKID.no in Klaviyo.

### What's Here:
- ✅ **HTML Email Template** (`kulkid_template_final.html`) - Brand-aligned base template
- ✅ **Upload Scripts** (`simple_upload.py`, `upload_templates.py`) - API automation tools
- ✅ **Setup Documentation** (`template_ready.md`) - Manual setup guide
- 📄 **Master Action Plan** (`KLAVIYO_FLOW_BUILD.md`) - Complete execution guide

### What's Missing (To Be Generated):
- 📧 14 email content files (markdown + HTML)
- ⚙️ Flow configuration files
- 🖼️ Image assets folder
- 🔧 Enhanced automation scripts

---

## 🎯 Current Status

### Completed:
1. ✅ Brand guide reviewed
2. ✅ Base HTML template created with proper KULKID branding
3. ✅ Collection URLs verified (basics, superhelter, gymtime)
4. ✅ Upload scripts created
5. ✅ Comprehensive action plan documented

### Next Steps (YOU):
1. **Get Klaviyo API Key** (Settings → API Keys)
2. **Create Discount Codes** in Shopify:
   - `KULKID15` (15% off, 7-day validity)
   - `VELKOMMEN` (20% off, 14-day validity)
3. **Upload Brand Assets** to Klaviyo library (logo, product images)
4. **Confirm Integration** - Verify Shopify ↔ Klaviyo sync is active

Then respond with: **"Ready for content generation"**

### Next Steps (AI):
Once you've completed setup, AI will generate:
- 14 Norwegian email files (markdown + HTML)
- Flow configuration JSON files
- Enhanced batch upload scripts
- Testing documentation

---

## 📧 Planned Flows

### 1. Welcome Flow (2 emails)
- Email 1: Immediate welcome + 15% discount
- Email 2: Brand story (2 days later)

### 2. First Order Flow (5 emails)
- Email 1: Thank you (1 hour post-fulfillment)
- Email 2: Styling tips (3 days)
- Email 3: Community invite (7 days)
- Email 4: Review request (14 days)
- Email 5: Product recommendations (21 days)

### 3. Cart Abandonment Flow (4 emails)
- Email 1: Reminder (1 hour)
- Email 2: Help offer (6 hours)
- Email 3: 10% discount incentive (24 hours)
- Email 4: Urgency/final push (48 hours)

### 4. Reactivation Flow (4 emails)
- Email 1: "We miss you" (90 days inactive)
- Email 2: 20% discount (7 days later)
- Email 3: Bestsellers showcase (14 days)
- Email 4: Final goodbye (21 days)

---

## 📂 File Structure (After Generation)

```
klaviyo_automation/
├── README.md                          ← This file
├── KLAVIYO_FLOW_BUILD.md             ← Master action plan (READ THIS)
├── kulkid_template_final.html        ✅ Base template
├── template_ready.md                 ✅ Manual setup guide
├── simple_upload.py                  ✅ Simple upload script
├── upload_templates.py               ✅ Full upload script
│
├── flows/                            ← TO BE CREATED
│   ├── welcome-flow/
│   │   ├── flow-config.json
│   │   └── emails/
│   │       ├── email1_welcome_15prosent.md
│   │       ├── email1_welcome_15prosent.html
│   │       ├── email2_merkehistorie.md
│   │       └── email2_merkehistorie.html
│   │
│   ├── first-order-flow/
│   │   ├── flow-config.json
│   │   └── emails/
│   │       ├── email1_takk.md / .html
│   │       ├── email2_stylingtips.md / .html
│   │       ├── email3_fellesskap.md / .html
│   │       ├── email4_vurdering.md / .html
│   │       └── email5_anbefaling.md / .html
│   │
│   ├── cart-abandonment-flow/
│   │   ├── flow-config.json
│   │   └── emails/
│   │       ├── email1_du_glemte_noe.md / .html
│   │       ├── email2_hjelp.md / .html
│   │       ├── email3_insentiv.md / .html
│   │       └── email4_siste_sjanse.md / .html
│   │
│   └── reactivation-flow/
│       ├── flow-config.json
│       └── emails/
│           ├── email1_savner_deg.md / .html
│           ├── email2_tilbud.md / .html
│           ├── email3_bestselgere.md / .html
│           └── email4_siste_sjanse.md / .html
│
├── assets/                           ← TO BE CREATED (YOU UPLOAD)
│   ├── logo.png
│   └── product-images/
│       ├── basics_hero.jpg
│       ├── superhelter_hero.jpg
│       └── gymtime_hero.jpg
│
└── scripts/                          ← TO BE CREATED
    ├── batch_upload_all.py
    ├── validate_templates.py
    └── test_emails.py
```

---

## 🎨 Brand Guidelines (Quick Reference)

### Colors:
- **Black:** #121212
- **White:** #FDFDFD
- **Light Green:** #f0fff4 (use instead of greys for backgrounds)
- **Green:** #4d6d5d (detailing, subtle accents)
- **Accent:** #334FB4 (blue for Instagram)
- **Rainbow Gradients:** accent effects only (see theme CSS).

### Typography:
- **Headings:** Luckiest Guy (LOCKED per rules)
- **Body:** Quicksand
- **Border Radius:** 0px (sharp corners)

### Tone:
- Playful, bold, kid-first
- Short, punchy sentences
- Active verbs
- Speak to both kids and parents

### Links:
- Collections: `/collections/basics`, `/collections/superhelter`, `/collections/gymtime`
- Instagram: `@kulkid.no`
- Website: `KULKID.no` (all caps)

---

## 🚀 How to Execute

### Phase 1: Prerequisites (YOU - 30-60 min)
See **KLAVIYO_FLOW_BUILD.md** → Section "What YOU Need to Fix"

### Phase 2: Content Generation (AI - 3-4 hours)
AI generates all email files, templates, and configuration

### Phase 3: Upload & Setup (YOU - 2 hours)
1. Run batch upload script
2. Create flows in Klaviyo UI
3. Configure triggers and timing
4. Test all emails

### Phase 4: Launch (YOU - 15 min)
Activate flows and monitor performance

---

## 📚 Documentation

- **Full Action Plan:** See `KLAVIYO_FLOW_BUILD.md` (comprehensive guide)
- **Manual Setup:** See `template_ready.md` (alternative to API)
- **Brand Guide:** See `/home/ben/projects/kul-kid/BRAND_GUIDE.md`

---

## 🔧 Existing Files Explained

### `kulkid_template_final.html`
Brand-aligned HTML email template with:
- KULKID fonts (Luckiest Guy + Quicksand)
- Brand colors (#121212, #F3F3F3, #334FB4)
- 0px border-radius (sharp corners)
- Mobile responsive
- Klaviyo personalization variables

### `simple_upload.py`
Python script to upload a single Norwegian welcome template via Klaviyo API.
Use when you only need to test the API connection.

### `upload_templates.py`
More comprehensive Python script that:
- Creates custom customer properties
- Uploads email templates
- Handles API errors gracefully
- Uses Klaviyo API v2024-10-15

### `template_ready.md`
Manual setup guide for users who prefer to:
- Create templates manually in Klaviyo UI
- Copy/paste HTML instead of using API
- Set up custom properties via UI

---

## ⚠️ Important Notes

1. **Norwegian Only:** All emails are in Norwegian (Bokmål)
2. **Brand Name:** Always "KULKID" or "KUL KID" (all caps), never "Kul Kid"
3. **Font Rule:** Headings MUST use Luckiest Guy (per your custom rules)
4. **Sharp Corners:** 0px border-radius on all buttons/cards
5. **GDPR:** All emails include unsubscribe + sender address automatically

---

## 📞 Support

For questions or issues:
1. Check `KLAVIYO_FLOW_BUILD.md` → Troubleshooting section
2. Review Klaviyo API docs: https://developers.klaviyo.com
3. Validate HTML before upload: `python3 scripts/validate_templates.py`

---

**Ready to start?** Read `KLAVIYO_FLOW_BUILD.md` for the complete step-by-step guide.
