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

---

## Phase 4.5: Section-by-Section Refactor & Branding Rollout (Small Commits)

Goal: Shorten code, extract repeated logic into snippets, and gradually add brand elements (rainbow gradients) and subtle, accessible animations. Work proceeds in very small, reviewable commits per section (or per sub-task), merged via PRs to staging.

---

### 1) Operating Rules (for this phase)

**Commit & PR Guidelines:**
- One atomic change per commit, per section.
- PR naming conventions:
  - `feat(section): ...` — new features or capabilities
  - `refactor(section): ...` — code restructuring without behavior change
  - `style(brand): ...` — visual/brand additions (gradients, animations)
  - `fix(section): ...` — bug fixes

**Each PR must include:**
- A screenshot or short screen recording of desktop + mobile
- Notes on snippets introduced/edited
- Before/after line counts for the edited file(s)
- Accessibility checks (focus states, motion)

**Branch flow:**
- `feature/section-<name>-<subtask>` → PR → `staging`
- Never push directly to `main`

**Testing checklist (per PR):**
- [ ] Renders in theme editor without console errors
- [ ] Mobile/desktop layout OK
- [ ] No regressions in header, cart, filters
- [ ] Lighthouse quick pass (no major drops)
- [ ] Theme Check passes (error-free)

---

### 2) Conventions to Apply During Refactors

**Snippetization pattern:**
Create small, composable snippets with explicit props via schema settings:
- `snippets/nav-menu.liquid`
- `snippets/header-logo.liquid`
- `snippets/announcement-bar.liquid`
- `snippets/category-bubbles.liquid`
- `snippets/gradient-badge.liquid`

**Schema guidelines:**
- Prefer small, typed settings; avoid mega-schemas
- Group settings by UX intent; name keys consistently (`kulkid_*` prefix)

**Brand tokens (add to settings_data or CSS variables):**
```css
--kk-rainbow: linear-gradient(90deg, #FF5C5C, #FFB347, #F9F871, #6EE7B7, #60A5FA, #C084FC, #F472B6)
--kk-accent-1: [define based on BRAND_GUIDE.md]
--kk-accent-2: [define based on BRAND_GUIDE.md]
```

**Animation rules:**
- Use CSS-only where possible; respect `prefers-reduced-motion`
- Durations: 180–300ms
- Easing: `cubic-bezier(.2,.8,.2,1)`
- No layout thrash; transform/opacity only

---

### 3) Work Items (initial backlog)

Each item has sub-tasks and acceptance criteria. These will be tracked in the table below.

#### A) Announcement Bar (brand)
**Tasks:**
- Add rainbow gradient background option (tokenized)
- Add subtle looping text shimmer/scroll (prefers-reduced-motion fallback)
- Extract to `snippets/announcement-bar.liquid`

**Acceptance:**
- [ ] Gradient toggle + intensity control in schema
- [ ] Motion disabled under reduced-motion
- [ ] ≤ ~60 lines in section + snippet(s)

#### B) blocks/comprehensive-overlay-header.liquid (navigation/header)
**Tasks:**
- Finish new main-header composition using snippets: `header-logo`, `nav-menu`, `mobile-toggle`, `search`, `cart`
- Shorten file by extracting logic; ensure schema remains functional
- Validate overlay menu shows nav on mobile

**Acceptance:**
- [ ] Mobile overlay renders nav correctly
- [ ] No console errors; keyboard navigation OK
- [ ] Header section ≤ ~150 lines; moves logic into snippets

#### C) kids-hero (split & simplify)
**Tasks:**
- Create two sections:
  1. `kids-hero-visuals`: split images with blocks
  2. `kids-hero-categories`: category bubbles
- Extract category bubble UI into `snippets/category-bubbles.liquid`
- Keep schemas minimal; provide image ratio and bubble count controls

**Acceptance:**
- [ ] Each new section loads independently in editor
- [ ] Category bubbles clickable and manageable
- [ ] Combined line count reduced by ≥30%

#### D) featured-collection (brand polish)
**Tasks:**
- Add rainbow gradient accents for headings/badges
- Keep performance: gradients as CSS, no heavy assets

**Acceptance:**
- [ ] Toggle for gradient headline/badge
- [ ] No layout shift; collection cards unaffected

#### E) main-footer.liquid (shorten & inherit Dawn defaults)
**Tasks:**
- Inherit Dawn default logic where possible
- Extract link lists, newsletter, badges into snippets
- Reduce line count substantially

**Acceptance:**
- [ ] Footer customizable fully via schema
- [ ] No duplicated logic from core Dawn components
- [ ] Clear separation of concerns across snippets

#### F) Remaining AI blocks → rebuilt as short sections + snippets
**Tasks:**
- For each AI block: create a concise section and factor shared UI into reusable snippets
- Normalize schema keys, reduce options to what is used

**Acceptance:**
- [ ] Each replacement section compiles and renders
- [ ] Shared UI lives in snippets with ≤ ~80 lines per section

#### G) Product View — Map Color Selection → Show All Images for That Color (no sort/thumbnail regressions)
**Problem:**
- Each color currently links to a single image, but we have 5–6 mockups per color. When a user clicks a color swatch in product view, we must show *all* images for that color in the gallery/thumbnail strip (keeping existing sort and thumbnail behaviors intact).
- Must not break: variant selection, gallery sorting, thumbnail navigation, URL `?variant=` behavior, or performance.

**Scope & Goals:**
- On color selection, filter the gallery to only the media belonging to that color (in order), without duplications or layout shift.
- Preserve current sorting (media position) and thumbnail keyboard accessibility.
- Keep the solution author-friendly for ongoing content updates.

**Proposed Approaches (choose one, document in PR):**

A) **Metafield JSON map (preferred):**
   - Product-level metafield: namespace `kk`, key `color_media_map` (JSON).
   - Structure: `{ "Red": [<media_id>, <media_id>, ...], "Blue": [...] }`.
   - Editor workflow: merch team fills the map with media IDs (copyable from theme editor or admin), or we provide a helper note.

B) **Alt-text tag fallback:**
   - Tag media with `[color: Red]` in alt text; parser collects all images tagged with the selected color.
   - Lowest-friction authoring; less strict than IDs, but works without metafield UI.

C) **Variant-media hybrid:**
   - Use Shopify variant media as baseline; augment by also showing media tagged for the selected color (A or B) so multiple images appear, not just the first.

**Implementation Tasks (small, separate commits):**
1. **Audit:**
   - Locate current variant change handlers and gallery code (JS/Liquid).
   - Identify where thumbnails are derived and how sorting is defined (media position vs. explicit order).
2. **Data layer:**
   - Add support for reading `kk.color_media_map` (JSON) if present.
   - Add parser for alt-text tags `[color: <Name>]` as fallback.
   - Normalize color names (case-insensitive, trim, consistent slug).
3. **Filtering logic:**
   - On color change (swatch or variant selection), compute the media set:
     - Prefer JSON map for the selected color; else derive from alt-text tags; else fallback to variant's assigned media.
   - Preserve sort by original media position.
   - De-duplicate media IDs.
4. **Gallery/thumbnail update:**
   - Update main media gallery and thumbnail strip to the filtered list.
   - Maintain keyboard navigation, focus order, and lazy-loading.
   - Ensure no console errors and no layout thrash (transform/opacity only for transitions).
5. **URL & state:**
   - Preserve `?variant=` in URL and deep-link behavior.
   - If user loads a URL with a preselected variant/color, initialize gallery with that color's media set.
6. **Admin authoring guide (docs only in PR):**
   - Short "How to map color → images" note with examples for JSON and alt-text tag methods.
   - Naming conventions for colors (e.g., exact swatch label).
7. **Safeguards:**
   - Fallback gracefully: if a color has no mapped media, show default gallery.
   - Guard against missing/invalid metafield JSON.
   - Respect `prefers-reduced-motion` for any transitions.

**Acceptance:**
- [ ] Selecting a color shows all images linked to that color in the gallery and thumbnails (≥5 images supported)
- [ ] Sort order matches media position; no duplicate thumbnails
- [ ] Variant selection, thumbnails, and keyboard nav remain functional
- [ ] `?variant=` links initialize the correct color and gallery
- [ ] No performance regressions (first interaction ≤ 100ms handler time on a typical PDP)
- [ ] No console errors; passes Theme Check; a11y checks pass (focus, aria-current/selected where applicable)

**Risks & Mitigations:**
- Authoring drift (inconsistent color names) → normalize to a slug; document conventions.
- Large galleries causing jank → preserve lazy-load, limit DOM updates to diff.
- Conflicts with existing variant-media logic → gate new behavior behind a schema toggle until fully validated.

---

### 4) Tracking Table

| Section | Subtask | Branch | PR Title | Screens (D/M) | Theme Check | A11y | Lines Before→After | Status |
|---------|---------|--------|----------|---------------|-------------|------|-------------------|--------|
| Announcement Bar | Gradient background | | | | | | | |
| Announcement Bar | Text animation | | | | | | | |
| Announcement Bar | Extract snippet | | | | | | | |
| Header | Extract nav-menu | | | | | | | |
| Header | Extract logo | | | | | | | |
| Header | Mobile overlay | | | | | | | |
| Kids Hero | Split visuals section | | | | | | | |
| Kids Hero | Categories section | | | | | | | |
| Kids Hero | Extract bubbles snippet | | | | | | | |
| Featured Collection | Gradient accents | | | | | | | |
| Footer | Inherit Dawn defaults | | | | | | | |
| Footer | Extract link lists | | | | | | | |
| Footer | Extract newsletter | | | | | | | |
| PDP (Product) | Color→images mapping | feature/pdp-color-media | feat(pdp): show all images for selected color | | | | | Planned |
| AI Blocks | Rebuild block 1 | | | | | | | |
| AI Blocks | Rebuild block 2 | | | | | | | |
| AI Blocks | Rebuild block 3 | | | | | | | |
| AI Blocks | Rebuild block 4 | | | | | | | |

---

### 5) Commit Plan Examples (documentation only; do not run)

These are example commit messages for reference:

```bash
# Documentation
docs(plan): add Section-by-Section Refactor & Branding Rollout

# Feature additions
feat(announcement-bar): gradient + accessible text animation

# Refactoring
refactor(header): extract nav-menu + logo into snippets

# Brand/style
style(brand): add rainbow gradient tokens to theme CSS

# Fixes
fix(footer): correct social icon fallback URL logic
```

---

### Next Up (Execution Order)

1. **Announcement Bar** — gradient background + text animation + snippet extraction
2. **Header** — extract navigation snippets + mobile overlay validation
3. **Kids Hero (visuals)** — split images section
4. **Kids Hero (categories)** — category bubbles section + snippet
5. **Featured Collection** — gradient accents for headings/badges
6. **Footer** — inherit Dawn defaults + extract snippets
7. **Product View — Color→Images mapping** — show all images for selected color with metafield or alt-text approach
8. **Remaining AI blocks** — rebuild as concise sections with shared snippets

---

