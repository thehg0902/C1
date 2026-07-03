# Contract: File Structure  (v1.1.0)

Canonical output tree for every client site. `assets/` lives INSIDE `src/`
(nested, not a sibling) so the entire deliverable is one self-contained
folder - zip `src/` alone and it's the complete site, no assembly step:

src/
  index.html                 (+ one .html per page in client.md Pages)
  css/
    tokens.css               (design tokens ONLY — see design-tokens contract)
    base.css                 (reset, element defaults, utilities)
    components.css           (component styles)
    pages.css                (page-specific overrides, kept minimal)
  js/
    main.js                  (init, nav, small interactions)
    hero.js                  (hero media logic, if any)
    animations.js            (scroll/entrance animation, if any)
  assets/
    images/                  (optimized web images: .webp preferred + fallbacks)
    video/                   (hero/section video: .mp4 h.264; poster .webp)
    fonts/                   (self-hosted .woff2 only)

Rules:
1. Kebab-case filenames. No spaces, no uppercase.
2. No build step, no framework, no bundler: plain HTML/CSS/JS, deployable
   as static files via Hostinger Git integration.
3. Every image referenced from HTML lives in src/assets/images (no
   hotlinks). Reference as `assets/images/...` from HTML/JS (same
   directory) and `../assets/images/...` from src/css/*.css (one
   directory down).
4. Every generated media asset must have a row in agency/state/MEDIA_LOG.md
   (see media-log contract) before it enters src/assets/. The `file`
   column is the path relative to repo root, i.e. `src/assets/...`.
5. Third-party embeds (Calendly, maps, Formspree endpoints) are the only
   allowed external references besides analytics.

## Changelog
- 1.1.0 (2026-07-03): assets/ moved from a sibling of src/ to nested
  inside it (src/assets/), so the client deliverable is a single
  self-contained folder. agency/scripts/flatten-site.sh simplified to a
  plain copy (no more path rewriting needed).
- 1.0.0 initial (assets/ as a sibling of src/).
