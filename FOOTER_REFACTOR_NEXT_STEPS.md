# Footer Refactor - Next Steps

## Ultimate Goal
**Disable `footer.liquid` and use `main-footer.liquid` (refactored) as the only footer in the codebase.**

## Current Status
✅ **Completed:**
- Created 5 external CSS component files (~942 lines)
- Created 2 reusable snippets (newsletter, link-group) (~170 lines)
- Backed up original footer
- Committed progress to `feature/main-footer` branch

## Current File Size
- **Before:** 2,815 lines
- **Target:** ~500-600 lines (80% reduction)

## What Needs to Be Done

### 1. Replace Inline CSS Block (Lines 36-1024)
**Current:** 988 lines of CSS in `{% stylesheet %}` with Liquid variable interpolation
**Replace with:**
```liquid
{{ 'kk-section-footer.css' | asset_url | stylesheet_tag }}
{{ 'kk-component-footer-newsletter.css' | asset_url | stylesheet_tag }}
{{ 'kk-component-footer-social.css' | asset_url | stylesheet_tag }}
{{ 'kk-component-footer-links.css' | asset_url | stylesheet_tag }}
{{ 'kk-component-footer-payments.css' | asset_url | stylesheet_tag }}

{%- style -%}
  .kk-footer-{{ section.id }} {
    --kk-footer-text-color: {{ section.settings.master_text_color }};
    --kk-footer-section-spacing: {{ section.settings.section_spacing }}px;
    --kk-footer-copyright-spacing: {{ section.settings.copyright_top_margin }}px;
    padding-top: {{ section.settings.padding_top }}px;
    padding-bottom: {{ section.settings.padding_bottom }}px;
    padding-left: {{ section.settings.footer_padding }}px;
    padding-right: {{ section.settings.footer_padding }}px;
    {% if section.settings.enable_gradient %}
      background: linear-gradient(270deg, {{ gradient_colors }});
      background-size: 1200% 1200%;
      animation: rainbowGradient {{ gradient_speed }}s ease infinite;
    {% else %}
      background-color: {{ section.settings.static_bg_color }};
    {% endif %}
  }
  
  @media (max-width: 1024px) {
    .kk-footer-{{ section.id }} {
      padding-left: {{ section.settings.footer_padding | times: 0.8 | round }}px;
      padding-right: {{ section.settings.footer_padding | times: 0.8 | round }}px;
      padding-top: {{ section.settings.padding_top | times: 0.8 | round }}px;
      padding-bottom: {{ section.settings.padding_bottom | times: 0.8 | round }}px;
    }
  }
  
  @media (max-width: 768px) {
    .kk-footer-{{ section.id }} {
      padding-left: {{ section.settings.footer_padding | times: 0.65 | round }}px;
      padding-right: {{ section.settings.footer_padding | times: 0.65 | round }}px;
      padding-top: {{ section.settings.padding_top | times: 0.65 | round }}px;
      padding-bottom: {{ section.settings.padding_bottom | times: 0.65 | round }}px;
    }
  }
{%- endstyle -%}
```
**Lines saved:** ~940 lines

### 2. Simplify Block Rendering (Lines 1052-1721)
**Current:** ~670 lines of inline case statements for each block type
**Replace with:** Snippet calls

Example for newsletter block:
```liquid
{%- when 'newsletter' -%}
  {% render 'kk-footer-newsletter', 
    block: block, 
    newsletter_success_fallback: section.settings.newsletter_success_fallback 
  %}
```

Example for link_group:
```liquid
{%- when 'link_group' -%}
  {% render 'kk-footer-link-group', block: block %}
```

**Lines saved:** ~500 lines (replaced with ~50 lines of snippet calls)

### 3. Simplify Social Icons & Payments
These still need snippets created OR can be kept inline (they're complex with nested blocks).
**Option A:** Keep inline (simpler for now)
**Option B:** Create additional snippets (more work but cleaner)

### 4. Keep Schema Intact (Lines 1904-2815)
The schema is ~911 lines and should be preserved as-is (already has "KUL KID Main Footer" name).

## Manual Steps Required

Since the file is 2,815 lines and very complex, here's the recommended approach:

### Option 1: Manual Refactor (Safest)
1. Open `sections/main-footer.liquid` in your editor
2. Replace lines 36-1024 (CSS block) with the CSS file references above
3. Simplify lines 1052-1721 (block rendering) by replacing newsletter and link_group cases with snippet calls
4. Keep social icons and payments inline for now
5. Test in theme editor
6. Iterate

### Option 2: Automated (Riskier but faster)
Run this script to do the replacement:
```bash
# This would require creating a Python/Node script to:
# - Extract schema (lines 1904-2815)
# - Rebuild header with CSS refs
# - Rebuild body with simplified logic
# - Append schema
# - Save as new file
```

## Expected Final Structure

```liquid
{%- # Lines 1-35: Variable assignments (gradient colors, etc.) -%}

{%- # Lines 36-50: CSS file references + minimal inline styles -%}

{%- # Lines 51-400: Section HTML with snippet calls -%}
<footer class="kk-footer kk-footer-{{ section.id }}" role="contentinfo">
  <div class="kk-footer__inner">
    {%- # Grid layout -%}
    {%- # Block rendering with snippets -%}
    {%- # Policies -%}
    {%- # Copyright -%}
  </div>
</footer>

{%- # Lines 401-450: Accordion JavaScript (keep as-is) -%}

{%- # Lines 451-1361: Schema (keep as-is) -%}
```

**Total:** ~500-600 lines

## Next Action
Since this is a large structural change, I recommend:
1. **Test current changes first** - Push CSS files and snippets to a test theme
2. **Verify they work** - Check that styles load correctly
3. **Then proceed with full refactor** - Either manually or via script

Would you like me to:
- A) Create the full refactored file now (will require careful review)
- B) Create a refactor script to automate it
- C) Provide step-by-step manual instructions

---

## Progress Update (2025-10-28 13:46)

### ✅ Completed
1. **CSS Extraction** - Moved 988 lines to external files ✓
2. **Class Name Updates** - All HTML classes now match CSS ✓  
3. **Minor CSS Fixes** - Typography and mobile accordion ✓
4. **File Size** - Reduced from 2,815 to 1,868 lines (34% reduction) ✓

### 🎯 Current Status
- Rainbow gradient: ✅ Working
- Newsletter block: ✅ Displaying (minor styling tweaks needed)
- Social icons: ✅ Working
- Link groups: ✅ Visible and functional
- Accordion: ✅ Mobile-only as intended

### 📋 Next Phase: Code Simplification
Replace ~750 lines of inline block rendering with snippet calls:

**Priority 1: Newsletter Block** (~150 lines → ~10 lines)
Currently: Massive inline code (lines 97-197)
Target: `{% render 'kk-footer-newsletter', block: block, newsletter_success_fallback: section.settings.newsletter_success_fallback %}`

**Priority 2: Link Groups** (~70 lines → ~5 lines)  
Currently: Inline accordion logic (lines 213-264)
Target: `{% render 'kk-footer-link-group', block: block %}`

**Priority 3: Social Icons** (~350 lines → keep or simplify)
Complex nested block logic - evaluate if worth snippet extraction

**Expected final size:** ~1,100-1,300 lines (50-55% total reduction from original)

### 📊 Metrics
- Original: 2,815 lines
- Current: 1,868 lines  
- Target: ~1,200 lines
- Progress: 34% → Target: 57%

