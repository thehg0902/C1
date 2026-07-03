# client.md Schema  (v1.0.0)

Validated by agency/scripts/validate-client-md.py. Section headers must match
exactly. REQUIRED sections missing or containing "TODO" block the pipeline
at Phase 0 and generate entries in agency/state/QUESTIONS.md.

## REQUIRED sections
- `## Business`        - name, niche, one-line description
- `## Contact`         - phone, email, address (or "no physical address")
- `## Services`        - bullet list, at least one
- `## Pages`           - bullet list of pages wanted
- `## Brand`           - colors (hex or "none - propose"), logo path in
                          agency/client/assets-intake/ or "none - text logo"
- `## Audience`        - who the site must convince
- `## Mood`            - 3-6 adjectives
- `## Stack`           - flags, one per line, exact keys:
    animation: gsap | css-only | none
    3d: yes | no
    booking: calendly | none
    forms: formspree | none
    email-marketing: brevo | none
    analytics: ga4 | plausible | none
    hero-media: video | image-sequence | static | propose

## OPTIONAL sections
- `## Links`           - Google Maps URL, Google Business Profile, socials,
                          existing website, booking link
- `## Testimonials`    - verbatim quotes with attribution
- `## Photos`          - what exists in assets-intake, what must be generated
- `## Competitors`     - names/URLs
- `## Style references`- sites the client likes/dislikes
- `## Special requests`- anything unique
- `## Autonomy`        - low | normal | high (default normal). high relaxes
                          non-safety gates; media approval gate ALWAYS holds.
