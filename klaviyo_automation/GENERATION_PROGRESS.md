# Email Content Generation Progress

**Started:** 2025-10-30  
**Last Updated:** 2025-11-19  
**Status:** In progress – base template, assets and flow configs ready; 2/26 email content files (HTML) created

---

## 📦 Planned file set

Planned files are based on the actual flow definitions in `flows/*/flow-config.json` and the naming in `klaviyo_automation/README.md`.

Each email will ultimately have **two files**:
- A human‑readable markdown file (`.md`)
- A Klaviyo‑ready HTML file (`.html`) generated from `templates/kulkid_newsletter_design.html`

### Welcome Flow (2 emails → 4 files)

Folder: `flows/welcome-flow/emails/`

- `email1_double_optin_confirmation.md`
- `email1_double_optin_confirmation.html`
- `email2_welcome_discount15.md`
- `email2_welcome_discount15.html`

### First Order Flow (3 emails → 6 files)

Folder: `flows/first-order-flow/emails/`

- `email1_takk_for_din_ordre.md`
- `email1_takk_for_din_ordre.html`
- `email2_ikke_glem_a_bruke_rabattkoden_din.md`
- `email2_ikke_glem_a_bruke_rabattkoden_din.html`
- `email3_koden_din_utloper_om_48_timer.md`
- `email3_koden_din_utloper_om_48_timer.html`

### Cart Abandonment Flow (4 emails → 8 files)

Folder: `flows/cart-abandonment-flow/emails/`

- `email1_du_glemte_noe.md`
- `email1_du_glemte_noe.html`
- `email2_trenger_du_hjelp.md`
- `email2_trenger_du_hjelp.html`
- `email3_ekstra_rabatt.md`
- `email3_ekstra_rabatt.html`
- `email4_siste_sjanse.md`
- `email4_siste_sjanse.html`

### Reactivation Flow (4 emails → 8 files)

Folder: `flows/reactivation-flow/emails/`

- `email1_savner_deg.md`
- `email1_savner_deg.html`
- `email2_tilbud.md`
- `email2_tilbud.html`
- `email3_bestselgere.md`
- `email3_bestselgere.html`
- `email4_siste_sjanse.md`
- `email4_siste_sjanse.html`

### Config & script files tracked here

- Flow configs (already exist):
  - `flows/welcome-flow/flow-config.json`
  - `flows/first-order-flow/flow-config.json`
  - `flows/cart-abandonment-flow/flow-config.json`
  - `flows/reactivation-flow/flow-config.json`
- Planned automation scripts (do **not** exist yet):
  - `scripts/batch_upload_all.py`
  - `scripts/validate_templates.py`
  - `scripts/test_emails.py`

---

## ✅ Completed so far

### Flow configuration files (4/4)

- [x] `flows/welcome-flow/flow-config.json`
- [x] `flows/first-order-flow/flow-config.json`
- [x] `flows/cart-abandonment-flow/flow-config.json`
- [x] `flows/reactivation-flow/flow-config.json`

### Email content files (2/26)

Welcome Flow:
- [x] `flows/welcome-flow/emails/email1_double_optin_confirmation.html`
- [x] `flows/welcome-flow/emails/email2_welcome_discount15.html`
- [x] `flows/welcome-flow/emails/email1_double_optin_confirmation.md`
- [x] `flows/welcome-flow/emails/email2_welcome_discount15.md`

First Order Flow:
- [ ] All markdown + HTML files listed in the plan above

Cart Abandonment Flow:
- [ ] All markdown + HTML files listed in the plan above

Reactivation Flow:
- [ ] All markdown + HTML files listed in the plan above

### Scripts (0/3)

- [ ] `scripts/batch_upload_all.py`
- [ ] `scripts/validate_templates.py`
- [ ] `scripts/test_emails.py`

> Note: `simple_upload.py` and `scripts/generate_remaining_emails.sh` already exist but are treated as **setup/test helpers**, not part of the content generation tally.

---

## 📊 Summary

**Total email content files (MD + HTML):** 26  
**Completed email files:** 2/26  
**Remaining email files:** 24/26

**Flow configs:** 4/4 (100% complete)  
**Automation scripts (tracked here):** 0/3

If you include configs + scripts in the overall count:
- **Total tracked items:** 26 (email) + 4 (configs) + 3 (scripts) = 33
- **Completed:** 6/33 (2 email HTML + 4 configs) ≈ 18%

---

## 🔄 Next steps (high level)

1. **Finalize Welcome Flow source:**
   - [ ] Create markdown files for the two existing welcome emails.
   - [ ] Ensure copy follows brand voice from `BRAND_GUIDE.md` and `BRAND_ASSETS.md`.
   - [ ] Verify brand name usage ("KUL KID" in text, "KULKID.no" only in URLs).

2. **Generate First Order Flow emails (3 emails):**
   - [ ] Draft markdown copy for all three emails.
   - [ ] Generate corresponding HTML using `templates/kulkid_newsletter_design.html`.

3. **Generate Cart Abandonment and Reactivation emails (8 + 4 emails):**
   - [ ] Draft markdown copy and HTML for each email listed in the plan.
   - [ ] Keep filenames exactly matching this document and the `flow-config.json` files.

4. **Add automation scripts (optional but recommended):**
   - [ ] Implement `scripts/batch_upload_all.py` to upload all email templates.
   - [ ] Implement `scripts/validate_templates.py` to perform simple HTML/link checks.
   - [ ] Implement `scripts/test_emails.py` to send test mails.

5. **Keep this file in sync:**
   - After each batch of files is created, **update the checkboxes here** and in `KLAVIYO_FLOW_BUILD.md` so all docs match the real state of `klaviyo_automation/`.

---

## 🧩 Alignment with other docs

This progress file is aligned with:

- `klaviyo_automation/README.md` – for high‑level status and folder structure.
- `KLAVIYO_FLOW_BUILD.md` – for flow logic and execution plan.
- `BRAND_ASSETS.md` – for brand name usage ("KUL KID", `KULKID.no`), colors, and social handles (Instagram `@kulkidno`).

When in doubt, treat `BRAND_ASSETS.md` as the source of truth for **branding**, and the `flows/*/flow-config.json` files as the source of truth for **flow structure and filenames**.
