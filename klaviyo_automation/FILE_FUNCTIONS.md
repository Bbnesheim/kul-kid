# Klaviyo Automation Files - Function Explanation

**Last Updated:** 2025-10-30

---

## 📁 Current Files (Existing)

### 1. `README.md`
**Purpose:** Main navigation and setup overview  
**What it does:**
- Provides quick-start guide for the Klaviyo automation project
- Lists all planned email flows (Welcome, First Order, Cart Abandonment, Reactivation)
- Shows file structure before and after content generation
- Links to detailed documentation
- Quick reference for brand guidelines
- Explains existing file purposes

**When to use:**
- First entry point for anyone working on Klaviyo setup
- Quick reference for flow specifications
- Understanding project status and next steps

---

### 2. `KLAVIYO_FLOW_BUILD.md`
**Purpose:** Comprehensive action plan and execution guide  
**What it does:**
- **Prerequisites Audit:** Lists what assets are ready and what's missing
- **Task Division:** Clearly separates what YOU (human) must do vs what AI will do
- **Flow Specifications:** Detailed breakdown of all 4 flows with timing, triggers, exit conditions
- **Execution Timeline:** Hour-by-hour breakdown of work required
- **Step-by-Step Instructions:** Chronological checklist for setup and launch
- **Brand Guidelines:** Email-specific tone, design, and content rules
- **Testing Checklists:** Pre-launch validation steps
- **Troubleshooting:** Common issues and solutions
- **Success Metrics:** KPIs to track post-launch

**When to use:**
- Before starting any work (read this first!)
- When planning your time commitment
- During execution to stay on track
- When troubleshooting issues
- For reference during testing and launch

**Key Sections:**
- "What YOU Need to Fix" → Your responsibilities
- "What I (AI) Will Do" → AI responsibilities
- "Chronological Execution Steps" → Follow this order
- "Final Checklist Before Launch" → Pre-launch validation

---

### 3. `kulkid_template_final.html`
**Purpose:** Brand-aligned base email template  
**What it does:**
- Provides a complete HTML email template with KULKID branding
- Includes proper Google Fonts imports (Luckiest Guy + Quicksand)
- Uses correct brand colors (#121212, #F3F3F3, #334FB4)
- Implements 0px border-radius (sharp corners) per brand guide
- Contains Klaviyo personalization variables (`{{ first_name }}`, etc.)
- Mobile-responsive table-based layout
- Includes collection links (basics, superhelter, gymtime)
- Footer with Instagram link and unsubscribe

**Technical Details:**
- Width: 600px (standard email width)
- Font fallbacks included for email client compatibility
- Inline styles (required for email HTML)
- WCAG AA contrast compliant

**When to use:**
- As base template for generating all 14 email variations
- Reference for proper brand implementation
- Testing Klaviyo template uploads
- Manual template creation in Klaviyo UI

**Important Features:**
- Line 7: Google Fonts import (Luckiest Guy + Quicksand)
- Line 17-19: Heading with "Luckiest Guy" font (locked per rules)
- Line 29-37: Discount code box
- Line 49-71: Collection cards with links
- Line 79-81: CTA button (black bg, white text, 0px radius)
- Line 90-92: Instagram button (accent color #334FB4)
- Line 99-101: Footer with unsubscribe

---

### 4. `template_ready.md`
**Purpose:** Manual setup guide (alternative to API)  
**What it does:**
- Provides step-by-step instructions for manual Klaviyo setup
- Lists custom properties to create manually in Klaviyo UI
- Explains how to copy/paste HTML template into Klaviyo
- Testing checklist for after template creation
- Alternative workflow for users uncomfortable with API/scripts

**When to use:**
- If you prefer UI-based setup over command-line scripts
- If API upload fails or has issues
- For creating custom properties manually
- When you want to see the Klaviyo UI workflow

**Key Sections:**
- Section 1: Custom properties (manual creation in Settings)
- Section 2: Template upload via Klaviyo UI
- Section 3: Testing steps
- "What You Get" → Expected outcomes

**Who this is for:**
- Non-technical users
- Those who prefer visual UI over CLI
- Backup method if scripts fail

---

### 5. `simple_upload.py`
**Purpose:** Minimal API script for uploading single template  
**What it does:**
- Uploads ONE Norwegian welcome email template to Klaviyo
- Uses Klaviyo API v2024-10-15
- Prompts for API key (not stored in file)
- Creates template with HTML and plain text versions
- Provides success/error feedback
- Lists custom properties to create manually

**Technical Details:**
- Python 3 script
- Dependencies: `requests`, `json` (standard library)
- API endpoint: `https://a.klaviyo.com/api/templates/`
- Template name: `kulkid_welcome_nb_v2`

**When to use:**
- Testing API connection for the first time
- Quickly uploading a single template
- Learning how Klaviyo API works
- Debugging API authentication issues

**How to run:**
```bash
cd /home/ben/projects/kul-kid/klaviyo_automation
python3 simple_upload.py
# Enter API key when prompted
```

**Limitations:**
- Only uploads 1 template (welcome email)
- Doesn't create flows or properties
- Basic error handling
- Manual API key entry required

---

### 6. `upload_templates.py`
**Purpose:** Comprehensive API automation script  
**What it does:**
- Uploads multiple email templates to Klaviyo
- Attempts to create custom customer properties via API
- Includes `KlaviyoAutomation` class for reusability
- HTML to plain text conversion
- Better error handling than `simple_upload.py`
- Cleanup of test profiles after property creation

**Technical Details:**
- Python 3 script with OOP structure
- Class: `KlaviyoAutomation` with methods:
  - `create_template()` - Upload email template
  - `create_custom_property()` - Initialize property via test profile
  - `_html_to_text()` - Convert HTML to plain text
  - `_cleanup_test_profile()` - Delete test profiles
- Reads API key from environment variable or prompts
- Uses dictionaries to store template data

**When to use:**
- After confirming API key works (test with `simple_upload.py` first)
- When ready to upload all templates at once
- For production setup with multiple flows
- When you need programmatic template management

**How to run:**
```bash
cd /home/ben/projects/kul-kid/klaviyo_automation
export KLAVIYO_API_KEY="your_key_here"
python3 upload_templates.py
```

**Advantages over simple_upload.py:**
- Handles multiple templates
- Attempts custom property creation
- Better code organization
- Environment variable support
- More robust error handling

**Current Limitation:**
- Only has 1 template defined in `TEMPLATES` dictionary
- Needs to be updated with all 14 templates after generation

---

## 🔄 How These Files Work Together

### Current Workflow:

1. **Start:** Read `README.md` for overview
2. **Plan:** Review `KLAVIYO_FLOW_BUILD.md` for detailed execution plan
3. **Setup:** Complete prerequisites (API key, discount codes, assets)
4. **Test:** Run `simple_upload.py` to verify API connection
5. **Manual Option:** Follow `template_ready.md` if you prefer UI-based setup

### After AI Content Generation (Future Workflow):

1. **Start:** Same as above
2. **Plan:** Same as above
3. **Setup:** Same as above
4. **Content Ready:** AI generates 14 email files + config
5. **Upload:** Run enhanced `batch_upload_all.py` (to be created)
6. **Validate:** Run `validate_templates.py` (to be created)
7. **Test:** Run `test_emails.py` (to be created)
8. **Deploy:** Follow Klaviyo UI steps in `KLAVIYO_FLOW_BUILD.md`

---

## 📊 File Relationships Diagram

```
README.md (Entry Point)
    ↓
KLAVIYO_FLOW_BUILD.md (Master Plan)
    ↓
    ├── template_ready.md (Manual Setup Path)
    │       ↓
    │   Klaviyo UI → Manual Template Creation
    │
    └── API Scripts Path (Automated)
            ↓
        simple_upload.py (Test/Single Upload)
            ↓
        upload_templates.py (Batch Upload - Current)
            ↓
        [TO BE CREATED] batch_upload_all.py (Full Automation)
            ↓
        kulkid_template_final.html (Base Template)
            ↓
        [TO BE CREATED] All 14 Email HTML Files
            ↓
        Klaviyo API → Templates Created
```

---

## 🎯 Which File Should I Use?

| Your Situation | Recommended File | Notes |
|----------------|------------------|-------|
| Just starting the project | `README.md` | Get oriented |
| Planning time/resources | `KLAVIYO_FLOW_BUILD.md` | See full scope |
| Prefer manual UI setup | `template_ready.md` | No coding required |
| First API test | `simple_upload.py` | Test connection |
| Need template design reference | `kulkid_template_final.html` | Brand standards |
| Ready for full automation | `upload_templates.py` | Current best option |
| Troubleshooting | `KLAVIYO_FLOW_BUILD.md` → Troubleshooting | Solutions included |

---

## 🚨 Common Misconceptions

### ❌ WRONG: "The README shows all email files exist"
✅ CORRECT: The README shows the **planned structure**. Files are NOT yet created.

### ❌ WRONG: "I can run upload_templates.py and all 14 emails will upload"
✅ CORRECT: Currently only 1 template is defined. Need AI to generate remaining 13.

### ❌ WRONG: "template_ready.md is outdated since we have scripts"
✅ CORRECT: It's an alternative path for non-technical users or if API fails.

### ❌ WRONG: "simple_upload.py and upload_templates.py do the same thing"
✅ CORRECT: simple_upload.py is for testing; upload_templates.py is for production.

---

## 🔮 Future Files (To Be Created)

### `flows/*/flow-config.json`
JSON files defining flow triggers, timing, and conditions for each flow.

### `flows/*/emails/*.md`
Markdown files containing email copy in Norwegian (human-readable format).

### `flows/*/emails/*.html`
HTML versions of emails ready for Klaviyo upload (based on `kulkid_template_final.html`).

### `scripts/batch_upload_all.py`
Enhanced script to upload all 14 templates at once with progress tracking.

### `scripts/validate_templates.py`
Pre-upload validation to check for HTML errors, broken links, missing variables.

### `scripts/test_emails.py`
Send test emails to specified address for all templates.

### `assets/logo.png` + product images
Brand assets to be uploaded by you from Shopify.

---

## 💡 Pro Tips

1. **Always test with simple_upload.py first** before running full automation
2. **Keep API key secure** - use environment variables, never commit to git
3. **Read KLAVIYO_FLOW_BUILD.md fully** before starting work
4. **Use template_ready.md as backup** if API issues occur
5. **Validate HTML** in email testing tools before launch
6. **The base template (kulkid_template_final.html) is the source of truth** for brand styling

---

## 📞 Quick Reference

| Need to... | Use this file... |
|------------|------------------|
| Understand project scope | `README.md` |
| Plan your work | `KLAVIYO_FLOW_BUILD.md` |
| Test API connection | `simple_upload.py` |
| See brand-correct HTML | `kulkid_template_final.html` |
| Do manual setup | `template_ready.md` |
| Upload templates (current) | `upload_templates.py` |
| Troubleshoot issues | `KLAVIYO_FLOW_BUILD.md` → Troubleshooting |

---

**Need more help?** Check the Troubleshooting section in `KLAVIYO_FLOW_BUILD.md` or review Klaviyo API docs at https://developers.klaviyo.com
