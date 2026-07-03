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

Slugs kept kebab-case per contracts/file-structure.md: `what-we-do.html`,
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
follow when it processes client/assets-intake/ into assets/: logo ->
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
