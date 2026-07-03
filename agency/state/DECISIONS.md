# Decisions Log
<!-- Resolved ambiguities. Once logged here, a decision outranks skills
     and contracts (precedence level 3). Format:
     YYYY-MM-DD | topic | decision | decided-by (human/claude) | why -->

2026-07-03 | stack.booking | Normalized "leave space for calandly integration" to `calendly` | human | invalid enum value in client.md; human confirmed intent was to reserve/implement Calendly booking space
2026-07-03 | contact.email | No email published anywhere on the site | human | business operates call/form-only
2026-07-03 | contact.address | No street address; service-area model (no storefront) | human | confirmed
2026-07-03 | service-area | Toronto, framed with "GTA / surrounding areas" as natural regional context | human | regional roofing business, no fixed address to anchor local SEO to
2026-07-03 | links.maps | No Google Maps embed | human | no public address to anchor a map to
2026-07-03 | links.socials | No social links/icons on site | human | none provided
2026-07-03 | competitors / style-refs | None provided; design direction relies solely on mood adjectives + niche + given brand colors | human | confirmed, nothing to incorporate
2026-07-03 | autonomy | HIGH — proceed on reasonable judgment; surface only genuinely ambiguous/high-stakes items | human | confirmed; Phase 4 media-approval gate remains a hard stop regardless
2026-07-03 | trust-claim.licensed-insured | State "licensed and insured" in copy | human | fact not in client.md, confirmed directly to avoid a placeholder
2026-07-03 | trust-claim.emergency-hours | State true 24/7 emergency availability in copy | human | fact not in client.md, confirmed directly; matches audience described as often "emergency" homeowners

## Phase 1 — Site Architecture (2026-07-03)

Sitemap: 5 pages, multi-page pattern (client.md Pages lists 5 distinct named
pages, not just "Home"). 10 services are roofing-adjacent without distinct
individual search intent worth 10 separate SEO pages -> one consolidated
Services page (client named it "Service," singular).

- decided-by: claude | why: client.md Pages already names 5 pages
  explicitly; services list doesn't meet the "5+ services with distinct
  search intent" bar for per-service pages per site-architecture skill
  decision guide.

| file | page | purpose | primary conversion action | section order |
|---|---|---|---|---|
| index.html | Home | Convert both emergency and planned-project visitors fast | Call (primary), form (secondary) | hero (video), services (summary grid -> services.html), about (trust/experience snapshot), gallery (6 supplied photos), faq (generic, non-fabricated), cta, footer |
| what-we-do.html | What We Do | Explain process/approach, build trust pre-service-specifics | Call | hero (static), about (process/approach), services (brief cross-link), cta, footer |
| why-choose-us.html | Why We're the Best | Differentiate via mood + confirmed trust facts, no fabricated stats | Call | hero, section--why (differentiators: family-owned 15+ yrs, licensed & insured, 24/7 emergency), gallery (photo subset as proof), cta, footer |
| services.html | Service(s) | List all 10 services with enough detail to qualify emergency vs planned leads | Call, form | hero, services (10 cards, one per service), cta, footer |
| contact.html | Contact | Capture the lead via form, Calendly, or call | Form, Calendly (primary); call (always visible) | hero (small), contact (Formspree form + Calendly embed + phone; no map/address block), footer |

Nav: 5 items (Home, What We Do, Why We're the Best, Service, Contact) -
under the 6-item max. Phone (647) 732-1484 always visible in header on
mobile (call-first trade niche, matches HVAC/dental precedent in skill).
Conversion action appears in the hero viewport (CTA button + tap-to-call)
and again in a bottom `cta` section on every page.

`testimonials` section omitted site-wide - none supplied in client.md, and
copywriting rules forbid fabricating any. Will not be added as an empty
stub either (visibly empty sections read as unfinished).

Slugs kept kebab-case per agency/contracts/file-structure.md: `what-we-do.html`,
`why-choose-us.html` (clearer than a literal "why-we-are-best" reading),
`services.html`, `contact.html`.

## Phase 2 — Design Direction (2026-07-03)

Niche playbook: no dedicated "roofing" playbook exists in
.claude/skills/design-direction/references/ — used references/hvac.md
(closest trade/emergency-service analog) and adapted for roofing's more
project-based (vs. dispatch-based) service mix.

- Direction name: "Grounded Trade Confidence" — bold and energetic per
  client mood, but converts on trust + speed of contact per the HVAC/trades
  playbook, not on visual flourish.
- Type pairing intent: bold energy pairing (typography.md) - a grotesque
  display weight for headings against a plain grotesque body, i.e. weight
  contrast does the "bold/energetic" work, not novelty typefaces (matches
  HVAC playbook's "sturdy sans, zero cleverness").
- Color intent: primary #DC5E0F dominant (CTAs, links, accents, 60-30-10
  with primary structuring ~30%), secondary #F59208 and accent #F7BE2B
  used sparingly for highlights/badges (~10%), neutrals (bg/surface/text)
  dominate at ~60%. Warm palette signals energetic + hardworking without
  reading as generic-corporate blue (the HVAC default) - deliberate
  deviation from the playbook's "clean blues" since the client supplied a
  strong warm-orange brand identity that should stay dominant.
- Imagery style: photo-real, matching tone/lighting of the 6 supplied
  operation photos - keeps Phase 4 storyboard prompts consistent with
  existing assets rather than introducing a clashing illustrative style.
- Layout personality: straightforward and sturdy per HVAC playbook - big
  clear headlines, generous section padding, unambiguous single-purpose
  CTAs, no scroll gimmicks.
- Motion level: subtle. Resolves the mood ("energetic") vs. Stack
  (`animation: css-only`) tension directly rather than escalating to
  QUESTIONS.md: css-only is an explicit, unambiguous Stack constraint, and
  "energetic" is expressed instead through color contrast, type-weight
  boldness, and small hover/focus micro-interactions (all achievable with
  CSS only) rather than expressive scroll/entrance motion.
- One distinctive element: an angled/diagonal divider between the hero and
  the next section, evoking roofline geometry - one signature shape used
  consistently, not five different gimmicks.
- Must-haves carried from HVAC playbook: phone in header (tap-to-call),
  24/7 emergency badge (confirmed true), licensed & insured badge
  (confirmed true), service-area statement (Toronto/GTA), simple
  short-form quote intent on Contact. Avoid: long forms, animation-heavy
  pages, ambiguous CTAs.
- Voice/register (feeds Phase 3 copy): direct, confident, plain-spoken -
  bold without hype language; grade-7 reading level; benefit before
  feature.

## Phase 2 — Design Tokens (2026-07-03)

Fonts self-hosted in assets/fonts/ (fetched from Google Fonts' public
gstatic CDN, latin subset only, converted to local files - no
Google Fonts <link> tags used, per design-tokens anti-pattern rule):
archivo-bold-700.woff2, archivo-extrabold-800.woff2 (heading),
inter-regular-400.woff2, inter-medium-500.woff2, inter-semibold-600.woff2
(body). Archivo = grotesque display for headings (bold/energetic weight
contrast), Inter = plain grotesque body (max legibility for
trust-and-speed conversion per HVAC playbook). Modular scale ratio 1.333
("expressive/bold" per typography.md, matching the direction).

Contrast verification (WCAG AA, computed via relative luminance):
- --color-text (#22120D) on --color-bg (#F2F1EB): ~17.6:1 - passes AA/AAA
  for all text sizes easily.
- White text on --color-primary (#DC5E0F): ~3.7:1 - passes the 3:1 large-text
  /UI threshold but NOT the 4.5:1 body-text threshold. Decision: primary is
  used for large/bold CTA button labels and icon fills only, never small
  body copy, per color-theory.md guidance ("use it only for large
  elements/fills" when a brand color fails as small text).
- White text on --color-primary-dark (#7A3308, derived -26L from primary,
  same hue): ~9.1:1 - passes AA for body text; used for hover/active button
  states and anywhere a stronger-contrast brand-hue fill is needed.
- --color-text-muted (#6E6259, darkened from Brand Neutral Gray #BBAB9D) on
  --color-bg: ~5.2:1 - passes AA body text. Raw #BBAB9D was ~2.0:1 on bg -
  far too low for text, so it is NOT used as text anywhere, only as a
  reference/border source color.
- --color-border (#8C7D6E, darkened from Brand Neutral Gray #BBAB9D) on
  --color-bg: ~3.5:1 - passes the 3:1 UI-border threshold; raw #BBAB9D
  failed this (~2.0:1), so it was darkened rather than used as-is.
- --color-success (#2E7D32) / --color-error (#C62828): standard AA-safe
  on-light values: not specified by the client, added per contract's
  required token set.
- --color-surface: #FFFFFF, one step lighter than --color-bg (#F2F1EB),
  used for card/panel fills that need to lift off the cream background.

## Phase 3 — Content (2026-07-03)

Hero headline (Home) - two candidates per copywriting rule 3, using the
"emergency/need-now" formula from references/headlines.md:
1. "24/7 Emergency Roofing in Toronto & the GTA" (leads with availability + area)
2. "Your Roof Fixed Right, Fast - Toronto's 24/7 Roofing Team" (leads with outcome)
Picked #1 - states the two highest-intent facts (24/7, area) immediately,
matches the direct/plain-spoken register from Phase 2, and isn't something
a competitor could paste unchanged once paired with the confirmed
licensed/insured + family-owned subheadline. Register kept consistent
site-wide: direct, confident, benefit-before-feature, no hype adjectives
("best", "top-rated") without proof.

Asset filename convention decided here for Phase 5 (image-optimization) to
follow when it processes agency/client/assets-intake/ into assets/: logo ->
assets/images/logo.webp; the 6 supplied operation photos -> gallery-1.webp
through gallery-6.webp (mapping order: image1.png=1, image2.jpg=2,
image3.jpg=3, "image 4.jpg"=4, image5.jpg=5, image6.webp=6); hero.mp4 ->
assets/video/hero.mp4 (re-encoded to budget) + assets/video/hero-poster.webp.
Phase 3 HTML already references these final paths even though the files
don't exist under assets/ yet - Phase 5 is responsible for populating them.

Testimonials section intentionally absent from all 5 pages (none supplied,
per Phase 1 decision - not re-litigated here).

No new QUESTIONS.md entries from this phase - the two facts that would
otherwise have needed [PLACEHOLDER] (licensed/insured, 24/7 availability)
were already resolved with the human before this phase started (see
Phase 0 entries above) and are used directly in Home, Why-We're-the-Best,
and footer copy.

Contact page: Formspree form and Calendly embed are skeleton-only
(placeholder `action="#"` / placeholder booking text) - actual wiring is
the forms and booking skills' job in Phase 5, not in scope here.

## Retainer edit - logo format + loading screen (2026-07-03)

- decided-by: human | Client swapped the delivered logo from .webp to
  .png. All `logo.webp` references across the 5 pages updated to
  `logo.png` (10 occurrences).
- Investigated why: the client's raw logo.png has NO real alpha channel
  (rgb24, confirmed via ffprobe + ffmpeg alphaextract) - the "transparent"
  checkerboard look is baked into opaque pixels, not real transparency.
  This was already true of the original file used for the earlier webp
  conversion; only now visible/flagged.
- Attempted fix: Higgsfield `remove_background` AI tool. Result was
  unusable - the model misread the logo's orange paint-splash + bold
  "C PLUS" text as removable background, keeping only the cursive
  "Roofing" script as the detected subject (confirmed by extracting and
  visually inspecting the actual alpha mask, not just previewing the
  RGB - the preview tool doesn't composite alpha against a checkerboard,
  so a broken-alpha file can still look correct at a glance). Discarded;
  not shipped.
  decided-by: human | why: paid AI background removal isn't reliable for
  a multi-element graphic-design logo (splash + text) - a photographic
  subject-detection model doesn't understand "this whole graphic is the
  subject, only the canvas is background."
- Interim: `assets/images/logo.png` restored to a clean, correctly
  resized (400px wide, ~156KB) render of the client's original raw file
  - visually complete and correct, but still carried the baked
  pseudo-transparency issue.
- Resolved same session: client supplied a properly alpha-transparent
  logo.png (1536x1024 rgba). Verified by extracting and visually
  inspecting the full alpha mask (not just spot pixel checks) - clean
  silhouette matching the paint-splash shape exactly, no missing
  content. Resized to 400px wide (~150KB) for delivery; re-verified the
  alpha mask survived the resize intact before placing it at
  `assets/images/logo.png`. No code changes needed beyond the earlier
  webp->png reference swap, since everything already pointed at this
  path.
- New component: `.loading-screen` (src/css/base.css) + init in
  src/js/main.js - full-viewport fixed overlay, `--color-bg` background,
  centered logo with a subtle pulse (wrapped in
  `prefers-reduced-motion: no-preference`), fades and removes itself
  after `window.load` + a 500ms minimum display time (so it's actually
  visible on this fast-loading static site, not an imperceptible flash).
  Purely aesthetic per the client's request - never blocks content, site
  is fully functional underneath and without JS. Added to all 5 pages
  identically, right after `<body>`.

## Restructure - assets/ moved inside src/ (2026-07-03)

- decided-by: human | Moved `assets/` from a sibling of `src/` to nested
  inside it (`src/assets/`), so `src/` alone is the complete, zippable
  deliverable - matches the exact goal `/export-client` already serves,
  just simpler now (no assembly step needed at all).
- Updated: all HTML `../assets/` -> `assets/` (5 pages); CSS
  `../../assets/` -> `../assets/` (tokens.css, pages.css);
  `agency/contracts/file-structure.md` bumped to v1.1.0 with the new
  canonical tree + a changelog entry; `agency/state/MEDIA_LOG.md`'s 13
  file-column paths updated to `src/assets/...` (repo-root-relative, per
  the contract rule and what qa-review's check.py expects);
  `agency/scripts/flatten-site.sh` simplified from a two-directory
  copy + `../assets/` path-rewrite down to a plain `cp -r src/.` (no
  rewriting needed anymore - behavior verified identical via a local dry
  run before relying on it); `.github/workflows/deploy-pages.yml` and
  `agency/scripts/export-client.py` inherit the simplification
  automatically since both call the shared script.
- Bonus simplification this unlocked: `deploy-hostinger` skill's
  "target subdir src/ vs. production-branch layout" decision from the
  original contract is no longer a real decision - `src/` is
  self-contained now, so targeting it directly in hPanel's Git
  integration is unambiguously correct. Updated the skill accordingly.
- Verified end-to-end in a local preview: CSS/JS/fonts/logo/hero
  video/service icons all load with zero broken refs and zero console
  errors on both index.html and services.html.

## Retainer edit - hero redesign: full-bleed video underlay (2026-07-03)

- decided-by: human | Client feedback: the previous side-by-side treatment
  (video in a rounded card next to the text, per Phase 5's original
  layout) read as too bright.
- Changed to a full-bleed video underlay: `.hero__media` moved out of
  `.container` and made `position: absolute; inset: 0` covering the
  whole `.section--hero`, with a new `.hero__scrim` overlay
  (`color-mix(in srgb, var(--color-text) 62%, transparent)` - token-based,
  not a hardcoded rgba) dimming it. Text switches to
  `var(--color-surface)` (white) over the video via a
  `.section--hero:has(.hero__media)` scope, so the 4 text-only hero pages
  (What We Do, Why We're the Best, Service, Contact) are untouched -
  verified live.
- Hero given an explicit `min-height: clamp(26rem, 78vh, 42rem)` for a
  proper full-bleed feel (previously height was just whatever the
  side-by-side content needed).
- `.btn--text` ("Get a Free Quote") recolored to `var(--color-accent)`
  inside the video hero only, since its default dark-brown color would
  have had poor contrast against the new dark scrim.
- Playback logic (js/hero.js play-once-then-freeze, returning-visitor
  localStorage) untouched - this was a visual/CSS change only.
- Verified in local preview at desktop and mobile (375px): no horizontal
  overflow, text clearly readable over the dimmed footage, angled
  section-transition divider still renders correctly on top of the new
  scrim/video layers.

## Fix - hero.mp4 reverted to raw unoptimized original (2026-07-03)

- decided-by: claude (bug investigation) | Human reported the hero video
  not playing. Diagnosed live: `src/assets/video/hero.mp4` had reverted
  to the raw client-supplied file (70.9MB, 15s, 1764x1176, WITH an aac
  audio track) instead of the Phase 5 optimized version (1MB-class,
  7s, muted, 1280w) - almost certainly overwritten during the earlier
  "move assets/ into src/" operation. Root cause was the asset, not the
  CSS/JS: with a fresh localStorage, `video.play()` genuinely worked and
  the promise resolved, it just took the file's real ~15s to play
  through given the size/format, which read as "not playing" in normal
  use. (Separately, and expected by design: with a stale
  `cplusroofing:heroPlayed` localStorage flag from repeat testing, the
  video correctly skips straight to the frozen last frame every time -
  that's the intentional returning-visitor behavior, not a bug, and was
  the first thing ruled out before finding the real cause.)
- Fix: re-ran the Phase 5 optimization pipeline on the current source
  (ffmpeg: trim to 7s, strip audio, scale to 1280w, h264/crf30) ->
  src/assets/video/hero.mp4 now ~1MB. Regenerated
  src/assets/video/hero-poster.webp from the new trimmed file to keep
  them in sync (~124KB). Verified with fresh localStorage: video now
  autoplays, plays through its full (short) duration, and freezes on
  the last frame automatically, matching the designed behavior.

## Retainer edit - hero video now loops continuously (2026-07-03)

- decided-by: human | Replaces the previous play-once-then-freeze +
  returning-visitor localStorage pattern (which itself is now removed as
  dead code, not just unused).
- `src/index.html`: added the native `loop` attribute to the hero
  `<video>` - the browser handles the actual repeat, no JS needed for
  that part.
- `src/js/hero.js` simplified to: if `prefers-reduced-motion: reduce`,
  do nothing (poster frame stands as a static hero); otherwise call
  `video.play()` and let `loop` handle the rest. Same
  reduced-motion-early-return shape already used in `js/animations.js`.
- Verified live: currentTime wrapped from ~4.8s back to ~0.8s after
  waiting past the video's 7s duration, confirming it loops rather than
  stopping.

## Retainer edit - testimonials section added to Home (2026-07-03)

- decided-by: human | Reverses the Phase 1 architecture decision to omit
  `testimonials` site-wide (client.md said "leave empty space to add
  later" and none were supplied at build time - see that decision
  earlier in this log). Human now wants the section built now, content
  later.
- Markup follows the canonical component template exactly
  (`.claude/skills/components/templates/sections.html`):
  `<figure class="testimonial"><blockquote
  class="testimonial__quote">...<figcaption
  class="testimonial__author">...`, inside the existing `.card-grid`
  (reused, not a new grid system). 3 cards per the components skill rule
  ("static grid up to 3; carousel only for 4+ AND client approval").
- Placed on index.html between `about` and `gallery` - trust-building
  flow: services -> about -> testimonials -> gallery -> faq -> cta.
- Content is `[PLACEHOLDER: ...]` for all 3 quotes and names - the hard
  invariant against inventing testimonials applies regardless of how
  much the human wants the section to exist visually. Logged as an open
  question in agency/state/QUESTIONS.md. qa-review's automated check
  will correctly FAIL on these placeholders until real quotes arrive -
  this is expected and by design, not a bug to silently work around.
- New CSS block `.testimonial`/`.testimonial__quote`/`.testimonial__author`
  in components.css, token-only (var(--color-surface),
  var(--color-border), var(--color-text-muted), etc.), reuses the
  existing `.card-grid` layout so no new grid CSS was needed.

## Fix - Why We're the Best crew photo overflowed on mobile (2026-07-03)

- decided-by: human (bug report) | `.why__crew-photo` set `max-width: 40rem`
  (a class selector) without `width: 100%`, which beat the global
  `img { max-width: 100% }` reset (element selector, lower specificity)
  - the image rendered up to 640px wide regardless of viewport,
  overflowing a 375px phone screen. Fixed by adding `width: 100%` so the
  image is always constrained by its container first, with `max-width`
  only capping it on wide screens. Verified: zero horizontal overflow at
  375px, image renders full-width and proportional.

## Feature - testimonials converted to an auto-advancing carousel (2026-07-03)

- decided-by: human | Expanded from 3 static cards to 6 slides in a
  carousel (`.testimonial-carousel`, `data-carousel` on the root per
  component-api rule 4), each with a 5-star rating row added above the
  author name. This deliberately goes against the components skill's
  "no autoplay" carousel guidance (explicit user instruction outranks
  skill bodies on the precedence ladder) - mitigated responsibly rather
  than ignored: auto-advance pauses on hover/focus, respects
  `prefers-reduced-motion` (never starts), and prev/next buttons + dot
  indicators give full manual/keyboard control regardless of motion
  preference.
- Star ratings are a visual placeholder (5 stars on every slide,
  `aria-label` itself marked `[PLACEHOLDER: confirm star rating]`) - not
  a claimed/verified aggregate rating. Extended the existing testimonials
  question in QUESTIONS.md to ask for the real per-review rating
  alongside the real quote text when the human provides them.
- `src/js/main.js`: new `initTestimonialCarousel` IIFE - defensive
  (bails if `[data-carousel]` or any required child is missing),
  generates dot buttons from slide count, `setInterval`-based
  auto-advance restarted on manual interaction.
- Verified via direct DOM/computed-style inspection (not just
  screenshots, which produced a visually blank capture for this
  transform-heavy component - confirmed via scrollHeight/clientHeight,
  computed color/background, and transform values that this is a
  screenshot-tool rendering artifact, not a real bug): content isn't
  clipped, text isn't invisible-on-invisible, auto-advance correctly
  wraps around after slide 6, and a manual button click advances the
  transform by exactly one slide-width.
