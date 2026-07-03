# Contract: File Structure  (v1.0.0)

Canonical output tree for every client site:

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
  images/                    (optimized web images: .webp preferred + fallbacks)
  video/                     (hero/section video: .mp4 h.264; poster .webp)
  fonts/                     (self-hosted .woff2 only)

Rules:
1. Kebab-case filenames. No spaces, no uppercase.
2. No build step, no framework, no bundler: plain HTML/CSS/JS, deployable
   as static files via Hostinger Git integration.
3. Every image referenced from HTML lives in assets/images (no hotlinks).
4. Every generated media asset must have a row in agency/state/MEDIA_LOG.md
   (see media-log contract) before it enters assets/.
5. Third-party embeds (Calendly, maps, Formspree endpoints) are the only
   allowed external references besides analytics.
