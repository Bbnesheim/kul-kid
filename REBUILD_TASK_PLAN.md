# KUL KID Shopify Rebuild — New Repo Plan (Dawn base)

Status: Initiated
Goal: Clean Dawn theme in a brand-new repo, then migrate existing functionality section-by-section with confidence.

---

## Repositories and Sources
- New repo: Bbnesheim/kul-kid (this repo)
- Old code: /home/ben/projects/kulkid
- Base theme: /home/ben/projects/kulkid/_vendor/dawn (Shopify Dawn)
- Brought over docs: BRAND_GUIDE.md, REBUILD_TASK_PLAN.md (this file)

---

## Working Principles
- Start from pristine Dawn; avoid modifying core behavior unless truly necessary.
- Migrate section-by-section; test locally after each change before merging.
- Prefer Dawn defaults for JS (variants, galleries, filters). Remove legacy scripts that override Dawn behavior.
- Keep live theme untouched; use draft themes for testing.

---

## Migration Flow (high level)
1) Bootstrap new repo with Dawn
   - Copy Dawn into kul-kid (done)
   - Add BRAND_GUIDE.md (done)
   - Add this REBUILD_TASK_PLAN.md (updated)
2) Local dev setup
   - Use: shopify theme dev to preview locally
   - Keep a draft theme for staging tests (push when needed)
3) Section-by-section migration
   - Order: header/footer → homepage sections → product page → collection templates → cart/minicart → utility pages
   - For each section:
     - Copy only the needed section/snippet/assets/locales from old repo
     - Rename to kk-* if customizing to avoid future Dawn conflicts
     - Bring minimal CSS; prefer Dawn tokens/variables
     - Verify settings schema and defaults in the theme editor
     - Test locally; fix console errors; ensure responsive
     - Commit on feature/section-<name> and open PR to main
4) QA and parity checks
   - Verify variant switching, media gallery, filters, cart
   - Run theme checks: shopify theme check --fail-level=error
   - Cross-browser and mobile pass
5) Cutover
   - Push as unpublished draft, review, then publish when parity is reached

---

## Detailed Checklist per Section
- [ ] Files copied (sections/, snippets/, assets/, locales/ as needed)
- [ ] Namespaced (kk-* for custom sections)
- [ ] No JS conflicts with Dawn core (no global overrides)
- [ ] Theme editor settings render and save
- [ ] Mobile/desktop layout sound
- [ ] Lighthouse/Theme Check clean

---

## What NOT to migrate
- Legacy global JS that replaces Dawn variant/gallery logic
- Conflicting CSS overrides that fight Dawn’s utilities
- Unused/broken sections and experiments

---

## Branching and Environments
- main: stable; protected
- feature/section-*: one PR per logical addition
- Optional: staging branch that maps to a draft theme

---

## Commands reference
- Local preview: shopify theme dev
- Validate: shopify theme check --fail-level=error
- Draft push (when needed): shopify theme push --unpublished --theme="KUL KID Rebuild"

---

## Progress Tracking
Current status: [ ] Not Started  [x] Repo bootstrapped  [ ] Sections migrating  [ ] QA  [ ] Launch

Notes:
- Use BRAND_GUIDE.md for colors/typography; implement via Dawn variables where possible.
- Lock headings to the brand heading font via theme settings or CSS tokens during the branding pass.

