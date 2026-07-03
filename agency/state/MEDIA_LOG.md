# Media Generation Ledger
See agency/contracts/media-log.md for format and rules.

Style block (design direction, Phase 2 - "Grounded Trade Confidence"),
reused verbatim in every image prompt below: "photo-real, warm natural
daylight, documentary-style trade photography (not overly polished or
staged), colors harmonizing with a warm burnt-orange and cream palette,
no text, no watermarks, no visible competitor branding." Ethics per
references/image-prompts.md: any generated people are ambient/lifestyle
only, never presented as actual C Plus Roofing staff.

Client already supplied real assets that cover the primary hero and
gallery needs - NOT regenerated: logo.png, 6 operation photos
(image1.png-image6.webp), hero.mp4. Per client.md Photos note ("generate
every other image assets if needed"), the rows below are the only
candidates identified as still missing.

Human approved all 4 rows on 2026-07-03: an initial file edit set "YES"
outside the proper column, which Claude did not treat as sufficient on
its own; the human then explicitly confirmed "Yes, generate all 4" in
chat before any generation call was made.

Proposed per-site credit cap: 20 credits (estimated need + ~30% iteration
margin per references/credit-budgeting.md). Exact costs to be confirmed
via the generation tool's own pricing lookup at approval time - estimates
below are rough placeholders for planning only.

| id | date | type | model | prompt-summary | credits | storyboard-approved | file | status |
|----|------|------|-------|----------------|---------|---------------------|------|--------|
| M001a | 2026-07-03 | image | z_image (Tongyi-MAI) - switched from recraft_v4_1/vector (2.5 credits/icon) to z_image (0.15 credits/icon) per human cost-tradeoff decision; one storyboard decision, split into one row per file per agency/contracts/media-log.md (file = single path) | Flat-line icon, single color line art in --color-primary, service: Roofing; consistent style, no text, no watermarks; services.html card grid | 0.15 | YES | src/assets/images/icon-roofing.webp | generated |
| M001b | 2026-07-03 | image | z_image (Tongyi-MAI) | Flat-line icon, service: Roof Installation | 0.15 | YES | src/assets/images/icon-roof-installation.webp | generated |
| M001c | 2026-07-03 | image | z_image (Tongyi-MAI) | Flat-line icon, service: Roof Repair | 0.15 | YES | src/assets/images/icon-roof-repair.webp | generated |
| M001d | 2026-07-03 | image | z_image (Tongyi-MAI) | Flat-line icon, service: Roof Inspection | 0.15 | YES | src/assets/images/icon-roof-inspection.webp | generated |
| M001e | 2026-07-03 | image | z_image (Tongyi-MAI) | Flat-line icon, service: Roof Damage Repair | 0.15 | YES | src/assets/images/icon-roof-damage-repair.webp | generated |
| M001f | 2026-07-03 | image | z_image (Tongyi-MAI) | Flat-line icon, service: Attic Venting | 0.15 | YES | src/assets/images/icon-attic-venting.webp | generated |
| M001g | 2026-07-03 | image | z_image (Tongyi-MAI) | Flat-line icon, service: Gutter Installation | 0.15 | YES | src/assets/images/icon-gutter-installation.webp | generated |
| M001h | 2026-07-03 | image | z_image (Tongyi-MAI) | Flat-line icon, service: Gutter Repair | 0.15 | YES | src/assets/images/icon-gutter-repair.webp | generated |
| M001i | 2026-07-03 | image | z_image (Tongyi-MAI) | Flat-line icon, service: Skylight Installation | 0.15 | YES | src/assets/images/icon-skylight-installation.webp | generated |
| M001j | 2026-07-03 | image | z_image (Tongyi-MAI) | Flat-line icon, service: Skylight Repair | 0.15 | YES | src/assets/images/icon-skylight-repair.webp | generated |
| M002 | 2026-07-03 | image | text2image_soul_v2 (Higgsfield Soul 2.0, resolved from soul_2) | Roofing crew member in safety gear installing shingles, mid-action, [STYLE BLOCK], 4:3, 1.5k quality | 0.12 (exact; billed as 1) | YES | src/assets/images/crew-in-action.webp | generated |
| M003 | 2026-07-03 | image | soul_location (Higgsfield) | Close-up subtle asphalt shingle roofing texture, low contrast, no people, [STYLE BLOCK adapted], 1:1 | 0.12 (exact; billed as 1) | YES | src/assets/images/texture-shingle.webp | generated |
| M004 | 2026-07-03 | image | soul_location (Higgsfield) | Toronto-area residential rooftop exterior, suburban backdrop, [STYLE BLOCK], 4:3 | 0.12 (exact; billed as 1) | YES | src/assets/images/contact-rooftop.webp | generated |

**Running total generated: ~1.86 credits exact (icons 1.5 + 3x0.12),
likely billed as ~4-5 credits with per-job rounding** - well under the
20-credit cap. Files downloaded, then resized/recompressed via ffmpeg in
Phase 5 (image-optimization pass): 10 icons -> 256x256 (~3-7KB each,
down from 2048px/25-58KB), crew-in-action.webp -> 900px wide (~83KB),
texture-shingle.webp -> 800px wide (~37KB), contact-rooftop.webp ->
1000px wide (~91KB). Client-supplied gallery photos and logo also
converted/optimized in the same pass (see BUILD_STATE.md Phase 5 notes).
