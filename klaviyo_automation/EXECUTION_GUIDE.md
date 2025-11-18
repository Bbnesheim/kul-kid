# EXECUTION GUIDE - Template-Based Approach

**Method:** Option 2 (Fast HTML Generation)  
**Total Time:** ~60 minutes  
**Date:** 2025-10-30

---

## 📋 OVERVIEW

Instead of manually creating 28 files, we'll:
1. AI creates all 14 markdown content files (Norwegian copy)
2. AI creates HTML template generator script
3. YOU run script → generates all 14 HTML files automatically
4. AI creates flow configs + upload scripts
5. YOU upload everything to Klaviyo

**Efficiency:** 1 hour vs 3+ hours

---

## ⏱️ TIMELINE

| Phase | Who | Time | What You Do |
|-------|-----|------|-------------|
| **1. Markdown Creation** | AI | 30 min | Nothing - wait |
| **2. Template Script** | AI | 15 min | Nothing - wait |
| **3. Generate HTMLs** | YOU | 2 min | Run script |
| **4. Flow Configs** | AI | 15 min | Nothing - wait |
| **5. Upload Scripts** | AI | 10 min | Nothing - wait |
| **6. Upload to Klaviyo** | YOU | 30 min | Run upload script |
| **7. Create Flows in UI** | YOU | 60 min | Follow config guides |
| **8. Test** | YOU | 30 min | Send test emails |

**YOUR ACTIVE TIME:** ~2 hours (mostly in phases 6-8)  
**AI WORKING TIME:** ~70 minutes

---

## 🚀 PHASE 1: Markdown Creation (AI - 30 min)

**What happens:**
- AI writes Norwegian email copy for all 14 emails
- Files created in `flows/*/emails/*.md`
- Includes subject lines, preview text, body copy, CTAs

**What YOU do:**
- ☕ Nothing - grab coffee while AI works

**Output:**
```
✅ flows/welcome-flow/emails/email1_welcome_15prosent.md
✅ flows/welcome-flow/emails/email2_merkehistorie.md
✅ flows/first-order-flow/emails/email1_takk.md
✅ flows/first-order-flow/emails/email2_stylingtips.md
✅ flows/first-order-flow/emails/email3_fellesskap.md
✅ flows/first-order-flow/emails/email4_vurdering.md
✅ flows/first-order-flow/emails/email5_anbefaling.md
✅ flows/cart-abandonment-flow/emails/email1_du_glemte_noe.md
✅ flows/cart-abandonment-flow/emails/email2_hjelp.md
✅ flows/cart-abandonment-flow/emails/email3_insentiv.md
✅ flows/cart-abandonment-flow/emails/email4_siste_sjanse.md
✅ flows/reactivation-flow/emails/email1_savner_deg.md
✅ flows/reactivation-flow/emails/email2_tilbud.md
✅ flows/reactivation-flow/emails/email3_bestselgere.md
✅ flows/reactivation-flow/emails/email4_siste_sjanse.md
```

---

## 🛠️ PHASE 2: Template Generator Script (AI - 15 min)

**What happens:**
- AI creates `scripts/generate_html_templates.py`
- Script reads markdown files
- Converts to Klaviyo-compliant HTML
- Applies KULKID branding automatically

**What YOU do:**
- Nothing yet

**Output:**
```
✅ scripts/generate_html_templates.py
```

---

## ▶️ PHASE 3: Generate HTML Files (YOU - 2 min)

**What YOU do:**

### Step 1: Navigate to directory
```bash
cd /home/ben/projects/kul-kid/klaviyo_automation
```

### Step 2: Run generator script
```bash
python3 scripts/generate_html_templates.py
```

**Expected output:**
```
🚀 KULKID Email Template Generator
==================================

Reading markdown files...
✓ email1_welcome_15prosent.md
✓ email2_merkehistorie.md
✓ email1_takk.md
...

Generating HTML templates...
✓ email1_welcome_15prosent.html (validated)
✓ email2_merkehistorie.html (validated)
✓ email1_takk.html (validated)
...

✅ SUCCESS: 14 HTML files generated
📂 Location: flows/*/emails/*.html

Next: Review templates and upload to Klaviyo
```

### Step 3: Verify files created
```bash
find flows -name "*.html" | wc -l
# Should output: 14
```

**What if script fails?**
- Check Python 3 is installed: `python3 --version`
- Check markdown files exist: `ls flows/*/emails/*.md`
- Read error message - I'll fix the script

---

## 📊 PHASE 4: Flow Configuration Files (AI - 15 min)

**What happens:**
- AI creates 4 JSON config files
- Each defines flow triggers, timing, filters
- You'll use these to set up flows in Klaviyo UI

**What YOU do:**
- Nothing

**Output:**
```
✅ flows/welcome-flow/flow-config.json
✅ flows/first-order-flow/flow-config.json
✅ flows/cart-abandonment-flow/flow-config.json
✅ flows/reactivation-flow/flow-config.json
```

---

## 🔧 PHASE 5: Upload Scripts (AI - 10 min)

**What happens:**
- AI creates enhanced upload scripts:
  - `scripts/batch_upload_all.py` - Upload all 14 templates
  - `scripts/validate_templates.py` - Check for errors
  - `scripts/test_emails.py` - Send test emails

**What YOU do:**
- Nothing yet

**Output:**
```
✅ scripts/batch_upload_all.py
✅ scripts/validate_templates.py
✅ scripts/test_emails.py
```

---

## 📤 PHASE 6: Upload to Klaviyo (YOU - 30 min)

**What YOU do:**

### Step 1: Validate templates (optional but recommended)
```bash
python3 scripts/validate_templates.py
```

**Expected output:**
```
Validating 14 templates...
✓ All templates valid
✓ No missing variables
✓ All links present
✓ Brand compliance checked

Ready for upload!
```

### Step 2: Set API key (if not already set)
```bash
export KLAVIYO_API_KEY="your_api_key_here"
```

### Step 3: Upload all templates
```bash
python3 scripts/batch_upload_all.py
```

**Expected output:**
```
🚀 Uploading 14 templates to Klaviyo...

[1/14] kulkid_welcome_15prosent_nb ✓
[2/14] kulkid_welcome_merkehistorie_nb ✓
[3/14] kulkid_first_order_takk_nb ✓
[4/14] kulkid_first_order_stylingtips_nb ✓
...
[14/14] kulkid_reactivation_siste_sjanse_nb ✓

✅ SUCCESS: All 14 templates uploaded!

Next steps:
1. Go to Klaviyo → Content → Email Templates
2. Verify templates appear
3. Send test emails to yourself
```

### Step 4: Verify in Klaviyo UI
1. Login to Klaviyo
2. Go to **Content** → **Email Templates**
3. Search for "kulkid"
4. You should see 14 templates

### Step 5: Send test emails
```bash
python3 scripts/test_emails.py your.email@example.com
```

**Or manually in Klaviyo:**
- Open each template
- Click "Send Test Email"
- Enter your email
- Check inbox (Gmail, mobile)

---

## 🔄 PHASE 7: Create Flows in Klaviyo UI (YOU - 60 min)

**What YOU do:**

For each of the 4 flows, you'll:

### Welcome Flow (~15 min)

1. In Klaviyo, click **Flows** → **Create Flow** → **Create From Scratch**
2. Name: "Welcome Flow"
3. **Trigger:** "List: Subscribed to List" OR "Metric: Subscribed to List"
4. **Add Email 1:**
   - Wait: 0 minutes (immediate)
   - Template: `kulkid_welcome_15prosent_nb`
   - Subject: Use from `flows/welcome-flow/flow-config.json`
5. **Add Time Delay:** 2 days
6. **Add Conditional Split:**
   - IF: "Placed Order" → Exit flow
   - ELSE: Continue
7. **Add Email 2:**
   - Template: `kulkid_welcome_merkehistorie_nb`
   - Subject: Use from config
8. **Smart Sending:** Enable (9 AM - 8 PM)
9. **Save & Review**

### First Order Flow (~20 min)

1. **Create Flow** → Name: "First Order Flow"
2. **Trigger:** "Metric: Fulfilled Order" + "Placed Order Number of Times = 1"
3. **Add Email 1:** 1 hour wait → Template: `kulkid_first_order_takk_nb`
4. **Add Time Delay:** 3 days
5. **Add Email 2:** Template: `kulkid_first_order_stylingtips_nb`
6. **Add Time Delay:** 4 days (total 7 days from start)
7. **Add Email 3:** Template: `kulkid_first_order_fellesskap_nb`
8. **Add Time Delay:** 7 days (total 14 days)
9. **Add Email 4:** Template: `kulkid_first_order_vurdering_nb`
10. **Add Time Delay:** 7 days (total 21 days)
11. **Add Email 5:** Template: `kulkid_first_order_anbefaling_nb`
12. **Exit Condition:** If "Placed Order" again, exit flow
13. **Smart Sending:** Enable

### Cart Abandonment Flow (~15 min)

1. **Create Flow** → Name: "Cart Abandonment"
2. **Trigger:** "Metric: Started Checkout"
3. **Add Time Delay:** 1 hour
4. **Add Conditional Split:**
   - IF: "Placed Order" → Exit
   - ELSE: Continue
5. **Add Email 1:** Template: `kulkid_cart_du_glemte_noe_nb`
6. **Add Time Delay:** 5 hours (total 6 hours)
7. **Add Conditional Split** (check order again)
8. **Add Email 2:** Template: `kulkid_cart_hjelp_nb`
9. **Add Time Delay:** 18 hours (total 24 hours)
10. **Add Email 3:** Template: `kulkid_cart_insentiv_nb`
11. **Add Time Delay:** 24 hours (total 48 hours)
12. **Add Email 4:** Template: `kulkid_cart_siste_sjanse_nb`
13. **Smart Sending:** Quiet hours 11 PM - 7 AM

### Reactivation Flow (~10 min)

1. **Create Flow** → Name: "Reactivation"
2. **Trigger:** "Segment: Has placed order" + "Has not placed order in last 90 days"
3. **Add Email 1:** Immediate → Template: `kulkid_reactivation_savner_deg_nb`
4. **Add Time Delay:** 7 days
5. **Add Conditional Split** (check for order)
6. **Add Email 2:** Template: `kulkid_reactivation_tilbud_nb`
7. **Add Time Delay:** 7 days (total 14 days)
8. **Add Email 3:** Template: `kulkid_reactivation_bestselgere_nb`
9. **Add Time Delay:** 7 days (total 21 days)
10. **Add Email 4:** Template: `kulkid_reactivation_siste_sjanse_nb`
11. **Exit:** After 60 days or if order placed

**Detailed instructions for each flow are in `flows/*/flow-config.json`**

---

## ✅ PHASE 8: Testing (YOU - 30 min)

### Step 1: Preview Mode Testing
In Klaviyo, for each flow:
1. Click flow name
2. Click **Preview**
3. Select a test profile
4. Step through the flow
5. Verify emails render correctly

### Step 2: Live Testing
1. Add your email to a test list
2. Trigger the flow (subscribe, make test order, etc.)
3. Check inbox for emails
4. Verify:
   - ✅ Subject lines correct
   - ✅ Personalization works (`{{ first_name }}`)
   - ✅ Links work
   - ✅ Mobile rendering good
   - ✅ Unsubscribe link functions

### Step 3: Desktop & Mobile Testing
Test emails in:
- [ ] Gmail (desktop)
- [ ] Gmail (mobile app)
- [ ] Outlook (if relevant)
- [ ] iOS Mail (if you have iPhone)

---

## 🎯 SUCCESS CRITERIA

Before launching:

- [ ] All 14 templates uploaded to Klaviyo
- [ ] All 4 flows created in Klaviyo UI
- [ ] Test emails sent and reviewed
- [ ] Mobile rendering verified
- [ ] Links tested (click each one)
- [ ] Unsubscribe tested
- [ ] Personalization verified (shows name, not `{{ first_name }}`)
- [ ] Smart sending configured
- [ ] Flow exit conditions set

---

## 🚨 TROUBLESHOOTING

### Script fails to run
```bash
# Check Python version
python3 --version  # Should be 3.7+

# Check dependencies
pip3 install requests markdown
```

### API upload fails
- Verify API key: `echo $KLAVIYO_API_KEY`
- Check key has full permissions in Klaviyo
- Retry with: `python3 scripts/batch_upload_all.py --retry`

### Templates show errors in Klaviyo
- Run: `python3 scripts/validate_templates.py`
- Check error message
- Fix HTML and re-upload

### Emails don't personalize
- Check profile has `first_name` field
- Test with real profile data
- Fallback "venn" should show if no name

---

## 📞 WHEN TO ASK FOR HELP

**Ask AI (me) if:**
- ✋ Script fails to generate HTMLs
- ✋ Validation errors you don't understand
- ✋ Need help fixing HTML syntax
- ✋ Flow config JSON unclear
- ✋ Want to add more social buttons (Facebook, Spotify)

**Handle yourself:**
- ✅ Running scripts (just follow commands)
- ✅ Uploading to Klaviyo (script handles it)
- ✅ Creating flows in UI (follow step-by-step above)
- ✅ Testing emails

---

## ⏭️ WHAT'S NEXT AFTER THIS GUIDE

Once all 8 phases complete:

1. **Monitor First 24 Hours**
   - Check flow analytics in Klaviyo
   - Look for errors or bounces
   - Monitor open/click rates

2. **Optimize** (Week 2)
   - A/B test subject lines
   - Adjust timing if needed
   - Review unsubscribe rates

3. **Scale**
   - Enable for all customers
   - Set up additional flows
   - Add more templates

---

## 📊 PROGRESS TRACKER

Use this to track your progress:

### Phase 1-5 (AI Work)
- [ ] All 14 markdown files created
- [ ] HTML generator script created
- [ ] Flow config JSONs created
- [ ] Upload scripts created

### Phase 3 (Your Action)
- [ ] Ran `generate_html_templates.py`
- [ ] Verified 14 HTML files exist

### Phase 6 (Your Action)
- [ ] Ran validation script
- [ ] Set KLAVIYO_API_KEY
- [ ] Ran batch upload script
- [ ] Verified templates in Klaviyo UI
- [ ] Sent test emails

### Phase 7 (Your Action)
- [ ] Created Welcome Flow
- [ ] Created First Order Flow
- [ ] Created Cart Abandonment Flow
- [ ] Created Reactivation Flow

### Phase 8 (Your Action)
- [ ] Tested all flows in preview mode
- [ ] Tested live with your email
- [ ] Verified mobile rendering
- [ ] Checked all links work

---

## 🎉 COMPLETION

When all checkboxes above are ✅:

**Congratulations!** You have:
- ✅ 14 professional Norwegian email templates
- ✅ 4 automated flows running in Klaviyo
- ✅ Brand-compliant design (KULKID fonts, colors, tone)
- ✅ Proper personalization and tracking
- ✅ Mobile-optimized emails

**Go live** and start seeing results! 📈

---

**Ready to start?** Tell me and I'll begin Phase 1 (creating all 14 markdown files).

**Questions about the process?** Ask before we begin!
