# KLAVIYO FLOW BUILD - Action Plan

**Project:** KUL KID Automated Email Flows  
**Date:** 2025-10-30  
**Status:** Ready for execution

---

## 📋 EXECUTIVE SUMMARY

This document outlines the complete execution plan for building 4 core automated email flows in Klaviyo for KULKID.no. The flows are designed to increase customer engagement, drive repeat purchases, and recover abandoned carts using Norwegian-language emails with proper brand alignment.

### Target Flows:
1. **Welcome Flow** - New subscriber onboarding with 15% discount
2. **First Order Flow** - Post-purchase nurture sequence (5 emails)
3. **Cart Abandonment Flow** - Recovery sequence (4 emails)
4. **Reactivation Flow** - Win-back campaign (4 emails)

---

## 🎯 PREREQUISITES AUDIT

### ✅ Assets Available:
- ✅ Brand Guide (`BRAND_GUIDE.md`) - Complete with colors, fonts, tone
- ✅ HTML Email Template (`kulkid_template_final.html`) - Brand-aligned
- ✅ Upload Scripts (`simple_upload.py`, `upload_templates.py`)
- ✅ Template Documentation (`template_ready.md`)
- ✅ Collection URLs confirmed:
  - `https://kulkid.no/collections/basics`
  - `https://kulkid.no/collections/superhelter`
  - `https://kulkid.no/collections/gymtime`
- ✅ Instagram handle: `@kulkid.no`
- ✅ Brand Colors: #121212 (ink), #F3F3F3 (surface), #334FB4 (accent)
- ✅ Brand Fonts: Luckiest Guy (headings), Quicksand (body)

### ⚠️ Issues Found in Current README.md:

1. **Incomplete File Structure** - Shows directory tree but no actual email files exist
2. **Missing Email Content** - References 14 email markdown files that don't exist
3. **No Timing Specifications** - Missing delay/trigger details for flows
4. **No Segmentation Logic** - Missing customer targeting criteria
5. **No Product Recommendations** - Missing dynamic content strategy
6. **Assets Folder Empty** - No logo, product images referenced

### 🔧 What YOU Need to Fix:

1. **Create Klaviyo Account Setup**
   - Ensure you have a Klaviyo Private API Key
   - Confirm Shopify-Klaviyo integration is active
   - Verify customer sync is working

2. **Confirm Discount Codes**
   - Create discount code: `KULKID15` (15% off, 7-day validity)
   - Create reactivation code: `VELKOMMEN` (20% off, 14-day validity)
   - Set up cart abandonment dynamic codes in Klaviyo

3. **Upload Brand Assets to Klaviyo**
   - Logo file (check Shopify: "Kul_Kid_Logo.svg")
   - Product images for top sellers (BASICS, SUPERHELTER, GYMTIME collections)
   - Optional: Lifestyle/brand imagery for visual variety

4. **Verify Collection URLs**
   - Confirm these collections are live and properly tagged:
     - `/collections/basics`
     - `/collections/superhelter`
     - `/collections/gymtime`

5. **Custom Properties Setup**
   - Will be created automatically via API or manually in Klaviyo Settings
   - Required properties:
     - `last_purchase_size` (Text)
     - `predicted_next_size` (Text)
     - `size_progression_date` (Date/Time)
     - `preferred_categories` (Text)

---

## 🤖 What I (AI) Will Do:

### Phase 1: Content Creation (Email Copywriting)
✍️ I will create all 14 Norwegian email markdown files with:
- Brand-aligned copy (playful, bold, kid-first tone from Brand Guide)
- Proper personalization variables (`{{ first_name }}`, etc.)
- Call-to-action buttons aligned with flow goals
- Subject lines and preview text optimized for open rates
- UTM tracking parameters for analytics

### Phase 2: HTML Template Generation
🎨 I will convert markdown emails to Klaviyo-ready HTML templates:
- Apply KULKID brand styles (fonts, colors, corners)
- Use existing `kulkid_template_final.html` as base
- Ensure mobile responsiveness
- Include proper Klaviyo template variables
- Maintain WCAG AA contrast compliance

### Phase 3: Flow Logic Documentation
📊 I will document detailed flow configurations:
- Trigger conditions for each flow
- Email timing/delays between messages
- Smart sending windows (best times to send)
- Exit conditions and suppression lists
- A/B test recommendations

### Phase 4: API Automation Scripts
⚙️ I will create/update Python scripts to:
- Batch upload all email templates to Klaviyo
- Create custom profile properties
- Set up tracking for email performance
- Handle error logging and retries

### Phase 5: Testing & QA Documentation
🧪 I will provide comprehensive testing checklists:
- Email rendering tests (Gmail, Outlook, mobile)
- Link validation
- Personalization variable checks
- Flow trigger verification steps
- Spam score optimization tips

---

## 📧 FLOW SPECIFICATIONS

### 1. WELCOME FLOW
**Trigger:** Profile subscribed to list OR Newsletter signup form submitted  
**Goal:** Convert new subscribers to first-time buyers  
**Emails:** 2

| Email | Timing | Subject | Goal |
|-------|--------|---------|------|
| Email 1 | Immediately | "Velkommen til KUL KID Kundeklubb! 🎉 Her er din 15% rabatt" | Deliver discount, introduce brand |
| Email 2 | 2 days later (if no purchase) | "Møt merkehistorien bak KULKID ✨" | Build brand connection, emotional story |

**Exit Conditions:**
- Placed order (move to First Order Flow)
- Unsubscribed

---

### 2. FIRST ORDER FLOW (Post-Purchase Nurture)
**Trigger:** Placed Order (first time)  
**Goal:** Build loyalty, encourage reviews, drive repeat purchases  
**Emails:** 5

| Email | Timing | Subject | Goal |
|-------|--------|---------|------|
| Email 1 | 1 hour after fulfillment | "Takk for din første bestilling! 🎉" | Thank you, order confirmation tips |
| Email 2 | 3 days after fulfillment | "Stylingtips for dine nye KULKID-plagg 👕" | Product education, cross-sell |
| Email 3 | 7 days after fulfillment | "Bli med i fellesskapet! 💙" | Community building, UGC invite |
| Email 4 | 14 days after fulfillment | "Hvordan var opplevelsen? ⭐" | Review request, feedback |
| Email 5 | 21 days after fulfillment | "Andre foreldre elsker også disse 🔥" | Product recommendations, repeat purchase |

**Exit Conditions:**
- Made second purchase (exit flow)
- Unsubscribed

---

### 3. CART ABANDONMENT FLOW
**Trigger:** Started Checkout BUT did NOT place order  
**Goal:** Recover lost revenue  
**Emails:** 4

| Email | Timing | Subject | Goal |
|-------|--------|---------|------|
| Email 1 | 1 hour after abandonment | "Du glemte noe i handlekurven din! 🛒" | Reminder with cart preview |
| Email 2 | 6 hours later | "Trenger du hjelp med bestillingen? 💬" | Address objections, offer support |
| Email 3 | 24 hours later | "Her er 10% ekstra rabatt på handlekurven din 🎁" | Incentive to complete |
| Email 4 | 48 hours later | "Siste sjanse – kurven utløper snart ⏰" | Urgency, final push |

**Exit Conditions:**
- Placed order
- Cart is empty
- 72 hours elapsed since last email

**Smart Sending:** Avoid 11 PM - 7 AM

---

### 4. REACTIVATION FLOW (Win-Back)
**Trigger:** Has purchased before BUT no activity in 90+ days  
**Goal:** Re-engage dormant customers  
**Emails:** 4

| Email | Timing | Subject | Goal |
|-------|--------|---------|------|
| Email 1 | Immediately upon 90-day threshold | "Vi savner deg! 👋" | Friendly reminder, show new products |
| Email 2 | 7 days later | "20% rabatt – bare til deg! 💙" | Strong discount incentive |
| Email 3 | 14 days later | "Dette er bestselgerne akkurat nå 🔥" | Social proof, trending products |
| Email 4 | 21 days later | "Siste sjanse før vi sier farvel 💔" | Final attempt, FOMO |

**Exit Conditions:**
- Placed order (return to normal customer flows)
- Unsubscribed
- 60 days elapsed with no engagement

---

## 🗂️ FILE STRUCTURE TO BE CREATED

```
klaviyo_automation/
├── README.md                           ← Update with execution guide
├── KLAVIYO_FLOW_BUILD.md              ← This document
├── kulkid_template_final.html         ✅ Exists
├── template_ready.md                  ✅ Exists
├── simple_upload.py                   ✅ Exists (to be updated)
├── upload_templates.py                ✅ Exists (to be updated)
│
├── flows/
│   ├── welcome-flow/
│   │   ├── flow-config.json           ← NEW: Flow setup parameters
│   │   └── emails/
│   │       ├── email1_welcome_15prosent.md         ← NEW
│   │       ├── email1_welcome_15prosent.html       ← NEW
│   │       ├── email2_merkehistorie.md             ← NEW
│   │       └── email2_merkehistorie.html           ← NEW
│   │
│   ├── first-order-flow/
│   │   ├── flow-config.json           ← NEW
│   │   └── emails/
│   │       ├── email1_takk.md                      ← NEW
│   │       ├── email1_takk.html                    ← NEW
│   │       ├── email2_stylingtips.md               ← NEW
│   │       ├── email2_stylingtips.html             ← NEW
│   │       ├── email3_fellesskap.md                ← NEW
│   │       ├── email3_fellesskap.html              ← NEW
│   │       ├── email4_vurdering.md                 ← NEW
│   │       ├── email4_vurdering.html               ← NEW
│   │       ├── email5_anbefaling.md                ← NEW
│   │       └── email5_anbefaling.html              ← NEW
│   │
│   ├── cart-abandonment-flow/
│   │   ├── flow-config.json           ← NEW
│   │   └── emails/
│   │       ├── email1_du_glemte_noe.md             ← NEW
│   │       ├── email1_du_glemte_noe.html           ← NEW
│   │       ├── email2_hjelp.md                     ← NEW
│   │       ├── email2_hjelp.html                   ← NEW
│   │       ├── email3_insentiv.md                  ← NEW
│   │       ├── email3_insentiv.html                ← NEW
│   │       ├── email4_siste_sjanse.md              ← NEW
│   │       └── email4_siste_sjanse.html            ← NEW
│   │
│   └── reactivation-flow/
│       ├── flow-config.json           ← NEW
│       └── emails/
│           ├── email1_savner_deg.md                ← NEW
│           ├── email1_savner_deg.html              ← NEW
│           ├── email2_tilbud.md                    ← NEW
│           ├── email2_tilbud.html                  ← NEW
│           ├── email3_bestselgere.md               ← NEW
│           ├── email3_bestselgere.html             ← NEW
│           ├── email4_siste_sjanse.md              ← NEW
│           └── email4_siste_sjanse.html            ← NEW
│
├── assets/                            ← NEW: Image assets
│   ├── logo.png                       ← You upload from Shopify
│   └── product-images/                ← You upload from Shopify
│       ├── basics_hero.jpg
│       ├── superhelter_hero.jpg
│       └── gymtime_hero.jpg
│
└── scripts/                           ← NEW: Enhanced automation
    ├── batch_upload_all.py            ← NEW: Upload all templates at once
    ├── create_flows.py                ← NEW: Create flow structures via API
    ├── test_emails.py                 ← NEW: Send test emails
    └── validate_templates.py          ← NEW: Check for errors before upload
```

---

## 🚀 EXECUTION TIMELINE

### ⏱️ Estimated Time Breakdown:

| Phase | Who | Duration | Tasks |
|-------|-----|----------|-------|
| **Setup** | YOU | 30 min | API key, discount codes, asset upload |
| **Content Creation** | AI | 2 hours | Write 14 email bodies in Norwegian |
| **Template Conversion** | AI | 1.5 hours | Convert to HTML, apply brand styles |
| **Flow Configuration** | AI | 1 hour | Create flow-config.json files |
| **Script Enhancement** | AI | 1 hour | Update upload scripts, add batch tools |
| **Manual Setup** | YOU | 1 hour | Create flows in Klaviyo UI |
| **Testing** | YOU + AI | 1 hour | Send tests, validate rendering |
| **Launch** | YOU | 15 min | Activate flows |

**TOTAL: ~8 hours** (3-4 hours YOU, 4-5 hours AI)

---

## ✅ CHRONOLOGICAL EXECUTION STEPS

### YOU DO FIRST:

#### Step 1: Klaviyo Account Setup (15 min)
- [ ] Log into Klaviyo account
- [ ] Navigate to Settings → API Keys
- [ ] Create new Private API Key (full read/write access)
- [ ] Save key securely (do not commit to git)
- [ ] Export as environment variable: `export KLAVIYO_API_KEY="your_key_here"`

#### Step 2: Shopify-Klaviyo Integration Check (10 min)
- [ ] Verify Klaviyo integration in Shopify Admin → Apps
- [ ] Check that customer data is syncing
- [ ] Confirm "Placed Order" and "Started Checkout" events are tracking

#### Step 3: Create Discount Codes in Shopify (15 min)
- [ ] Create code: `KULKID15` (15% off, minimum $0, 7-day expiry)
- [ ] Create code: `VELKOMMEN` (20% off, minimum $0, 14-day expiry)
- [ ] Enable dynamic cart abandonment codes in Klaviyo settings

#### Step 4: Upload Brand Assets (20 min)
- [ ] Download logo from Shopify: Settings → Files → "Kul_Kid_Logo.svg"
- [ ] Export hero images from top 3 collections
- [ ] Upload to `klaviyo_automation/assets/` folder
- [ ] Upload same images to Klaviyo → Content → Images Library

---

### AI DOES NEXT (Automated):

#### Step 5: Content Generation
✍️ I will generate all 14 email markdown files with:
- Norwegian copy following brand voice
- Proper subject lines and preview text
- Personalization variables
- Clear CTAs

#### Step 6: HTML Template Creation
🎨 I will convert emails to Klaviyo-ready HTML using:
- Base template from `kulkid_template_final.html`
- Brand colors: #121212, #F3F3F3, #334FB4
- Fonts: Luckiest Guy (headings), Quicksand (body)
- 0px border-radius (sharp corners per brand guide)

#### Step 7: Flow Configuration Files
📊 I will create `flow-config.json` for each flow with:
- Trigger specifications
- Timing/delays
- Filter conditions
- Exit rules

#### Step 8: Enhanced Upload Scripts
⚙️ I will create:
- `batch_upload_all.py` - One command to upload everything
- `validate_templates.py` - Pre-upload error checking
- `test_emails.py` - Send test to your inbox

---

### YOU DO AFTER (Manual Klaviyo Setup):

#### Step 9: Upload Templates to Klaviyo (30 min)
```bash
cd /home/ben/projects/kul-kid/klaviyo_automation
python3 scripts/batch_upload_all.py
```
- [ ] Verify all 14 templates appear in Klaviyo → Content → Email Templates
- [ ] Preview each template in Klaviyo UI
- [ ] Send test email to yourself for each

#### Step 10: Create Flows in Klaviyo UI (1 hour)
For each flow (Welcome, First Order, Cart Abandonment, Reactivation):
- [ ] Create new Flow in Klaviyo
- [ ] Set trigger based on `flow-config.json`
- [ ] Add time delays between emails
- [ ] Insert email templates
- [ ] Configure smart sending (9 AM - 8 PM, skip Sundays if desired)
- [ ] Set exit conditions
- [ ] Enable analytics tracking

#### Step 11: Testing (30 min)
- [ ] Use Klaviyo's "Preview Mode" to test triggers
- [ ] Add test profile to lists
- [ ] Verify emails send with proper timing
- [ ] Check mobile rendering (Gmail, iOS Mail)
- [ ] Validate all links work
- [ ] Confirm unsubscribe link functions

#### Step 12: Launch (15 min)
- [ ] Set flows to LIVE (not draft)
- [ ] Enable for all eligible customers
- [ ] Monitor first 24 hours for errors
- [ ] Check open rates after 3 days

---

## 📝 BRAND TONE & VOICE GUIDELINES

From `BRAND_GUIDE.md`:

### ✅ DO:
- Use short, punchy sentences
- Active verbs ("Oppdag", "Finn", "Bli med")
- Speak to both kids and parents
- Playful but clear
- Examples: "Kul shopping!", "Perfekte plagg til din lille helt"

### ❌ DON'T:
- Sarcasm or irony
- Jargon or complex terms
- Excessive exclamation points (max 1 per email)
- All-caps body text
- Lengthy paragraphs (keep to 2-3 lines)

### 📧 Email-Specific Rules:
- Subject lines: 35-50 characters, include emoji for visual interest
- Preview text: 40-80 characters, complement subject line
- Personalization: Use `{{ first_name|default:"venn" }}` in greetings
- CTAs: Limit to 1-2 per email, use action verbs
- Footer: Always include "Teamet på KULKID.no" + unsubscribe

---

## 🎨 DESIGN SPECIFICATIONS

### Colors (from Brand Guide):
- **Primary Black:** #121212 (text, buttons)
- **Surface:** #F3F3F3 (backgrounds, cards)
- **Accent:** #334FB4 (Instagram button, links)
- **White:** #FFFFFF (page background)

### Typography:
- **Headings:** Luckiest Guy, 400 weight (custom font - LOCKED per rules)
- **Body:** Quicksand, 400-500 weight
- **Heading sizes:** H1: 32px, H2: 24px, H3: 16px (in emails)
- **Body size:** 16px, line-height: 1.6

### Layout:
- **Email width:** 600px max
- **Border radius:** 0px (sharp corners per brand)
- **Button style:** Black background, white text, 0px radius
- **Spacing:** 20-40px padding in sections

### Images:
- Logo: Top center, ~120px width
- Product images: Square or 4:5 ratio
- Alt text: Always include for accessibility

---

## 🧪 TESTING CHECKLIST

### Pre-Launch Validation:

#### Email Rendering:
- [ ] Gmail (desktop)
- [ ] Gmail (mobile)
- [ ] Outlook 2016+
- [ ] iOS Mail
- [ ] Apple Mail (macOS)

#### Functional Tests:
- [ ] All links resolve correctly
- [ ] Unsubscribe link works
- [ ] Personalization variables render (not showing raw `{{ }}`)
- [ ] Images load (check CDN paths)
- [ ] Discount codes apply at checkout

#### Brand Compliance:
- [ ] Headings use Luckiest Guy font
- [ ] Colors match brand guide
- [ ] Border radius is 0px (sharp corners)
- [ ] "KULKID.no" spelling consistent (not "kulkid.no" or "Kul Kid")
- [ ] Instagram handle is "@kulkid.no"

#### Content Quality:
- [ ] No typos in Norwegian
- [ ] Tone matches brand voice
- [ ] Subject lines under 50 characters
- [ ] Preview text complements subject
- [ ] CTAs are clear and action-oriented

---

## 📊 SUCCESS METRICS

### Track These KPIs (post-launch):

| Metric | Target | Flow |
|--------|--------|------|
| **Open Rate** | 40%+ | All flows |
| **Click Rate** | 8%+ | All flows |
| **Conversion Rate** | 5%+ | Welcome Flow |
| **Cart Recovery Rate** | 10%+ | Cart Abandonment |
| **Reactivation Rate** | 3%+ | Reactivation Flow |
| **Unsubscribe Rate** | <0.5% | All flows |

### A/B Test Ideas (Phase 2):
- Subject line variations (emoji vs no emoji)
- Discount depth (15% vs 10% in welcome)
- Email timing (morning vs evening)
- CTA button text variations

---

## 🔧 TROUBLESHOOTING

### Common Issues & Solutions:

**API Upload Fails:**
- Check API key has full read/write permissions
- Verify API revision date is correct: `2024-10-15`
- Confirm HTML is valid (no unclosed tags)

**Templates Don't Show Brand Fonts:**
- Klaviyo strips `<link>` tags; use inline Google Fonts import in `<head>`
- Fallback to web-safe fonts in style declarations

**Personalization Variables Don't Work:**
- Use Klaviyo syntax: `{{ first_name|default:"venn" }}`
- Test with Preview tool in Klaviyo UI
- Ensure profile data is syncing from Shopify

**Flows Don't Trigger:**
- Verify Shopify integration is active
- Check filter conditions aren't too restrictive
- Confirm Smart Sending isn't blocking sends
- Test with manual trigger on test profile

---

## 📚 DOCUMENTATION REFERENCE

### Files to Consult:
- **Brand Guidelines:** `/home/ben/projects/kul-kid/BRAND_GUIDE.md`
- **Base Template:** `/home/ben/projects/kul-kid/klaviyo_automation/kulkid_template_final.html`
- **Setup Guide:** `/home/ben/projects/kul-kid/klaviyo_automation/template_ready.md`
- **Upload Scripts:** 
  - `/home/ben/projects/kul-kid/klaviyo_automation/simple_upload.py`
  - `/home/ben/projects/kul-kid/klaviyo_automation/upload_templates.py`

### External Resources:
- [Klaviyo API Docs](https://developers.klaviyo.com/en/reference/api_overview)
- [Klaviyo Flow Best Practices](https://www.klaviyo.com/marketing-resources/flow-best-practices)
- [Norwegian Email Marketing Guide](https://mailchimp.com/resources/email-marketing-in-norway/)

---

## ✅ FINAL CHECKLIST BEFORE LAUNCH

### Your Responsibilities:
- [ ] Klaviyo API key obtained and exported
- [ ] Discount codes created in Shopify
- [ ] Brand assets uploaded to Klaviyo library
- [ ] Collection URLs verified as live
- [ ] Shopify-Klaviyo integration confirmed active

### AI Completion:
- [ ] All 14 email markdown files created
- [ ] All 14 HTML templates generated
- [ ] Flow configuration JSON files created
- [ ] Upload scripts enhanced and tested
- [ ] Testing documentation provided

### Launch Criteria:
- [ ] All templates uploaded successfully to Klaviyo
- [ ] Test emails sent and validated (mobile + desktop)
- [ ] Flows configured in Klaviyo UI with correct triggers
- [ ] Smart Sending enabled (9 AM - 8 PM)
- [ ] Analytics tracking confirmed
- [ ] Team notified of go-live date

---

## 🚨 IMPORTANT NOTES

1. **Norwegian Language:** All emails must be in Norwegian (Bokmål). No English fallbacks.

2. **Brand Name Consistency:** Always use "KUL KID" or "KULKID" (all caps), never "Kul Kid" (title case) in body text. Website references use "KULKID.no".

3. **Font Locking:** Per your rules, title headings MUST use "Luckiest Guy" font. This is non-negotiable.

4. **Sharp Corners:** Border radius is always 0px per brand guide. No rounded buttons/cards except variant pills.

5. **GDPR Compliance:** All emails must include unsubscribe link and sender address (Klaviyo handles this automatically).

6. **Testing First:** Never launch a flow without sending test emails to yourself first.

7. **Gradual Rollout:** Consider enabling flows for 10% of traffic first, then scale up after 48 hours if metrics look good.

---

## 📞 NEXT STEPS

Once you've completed **Steps 1-4** (API key, discount codes, asset upload), respond with:

> "Ready for content generation"

I will then:
1. Generate all 14 email markdown files
2. Convert to HTML templates
3. Create flow configuration files
4. Provide upload scripts
5. Give you step-by-step instructions for Klaviyo UI setup

**Estimated time to complete:** 3-4 hours (for AI content generation) + 2 hours (for your manual setup).

---

**Document Version:** 1.0  
**Last Updated:** 2025-10-30  
**Owner:** Ben (with AI assistance)
