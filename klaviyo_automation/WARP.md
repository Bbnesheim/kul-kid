# Klaviyo Email Template Development Rules

## Design Authority

The **current HTML template** (`klaviyo_automation/templates/kulkid_newsletter_design.html`) is the **single source of truth** for the email design.

The images in `klaviyo_automation/templates/example/` are **reference examples only** and should NOT be treated as the authoritative design specification.

## Development Guidelines

1. **Template First**: All design decisions and implementations should be based on the current state of the HTML template file, not the example images.

2. **Example Images**: The example images serve as:
   - Initial inspiration only
   - Historical reference of early design concepts
   - Visual examples, but NOT specifications to match exactly

3. **Iterative Design**: As changes are made to the template, those changes take precedence over what appears in the example images.

4. **No Image Matching**: Do not attempt to make the template "match" the example images. The template evolves independently.

## Current Design Specifications

### Discount Section Layout
**Column Split: 60/40** (mobile-first approach)
- Left column: 60% width, black background (#000000)
- Right column: 40% width, transparent background
- Mobile responsive: Under 480px, both sections stack vertically at 100% width (black section first)

#### Left Column (60% - Black Background #000000)
- **Top**: "MOTTA" in pink (#FF1493), 30px font size, Luckiest Guy font
- **Bottom**: "DIN EKSKLUSIVE RABATT" in white (#FFFFFF), 24px font size, Luckiest Guy font
  - Line breaks after "DIN" and "EKSKLUSIVE"
- **Padding**: 14px top, 10px sides, 8px-16px bottom

#### Right Column (40% - Transparent Background)
- **Top**: "Bruk koden under ved utsjekk" in 10px, letter-spacing 0.8px, color #121212
- **Bottom**: 
  - "15%" displayed with left tilt (skewY(-8deg) transform), 52px font size, color #121212
  - Margin-top: 14px, margin-bottom: 10px
  - Example discount code below: "VELKOMST15-2252F3C4" in small highlighted white box (10px font, #121212 text)
- **Padding**: 14px top, 10px sides, 8px-14px bottom

#### Divider Line
- Follows 60/40 split
- Left 60%: transparent (matches black box area)
- Right 40%: black line (#121212) with 10px inset from edges
- Height: 2px

#### Technical Requirements
- Use `table-layout: fixed` on discount section table
- Use HTML `width="60%"` and `width="40%"` attributes (not just inline styles)
- All styles must be inline for email client compatibility
- No external CSS, flexbox, or background images
- Compatible with Klaviyo and Outlook
- Fonts: Luckiest Guy for headings, Quicksand for body text

### Mobile-First Approach
- Base design optimized for 340px width
- Scales to 560px on desktop
- All text and spacing must remain within bounds regardless of content length

### Text Overflow Protection
- All dynamic content areas must include overflow protection
- Use word-wrap, overflow-wrap, and word-break properties
- Prevent any text from breaching container boundaries
