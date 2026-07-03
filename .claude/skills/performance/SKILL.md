---
name: performance
description: Enforce speed budgets - Core Web Vitals targets, asset weight
  limits, loading strategy for images/video/fonts/scripts. Use in Phase 5
  while wiring assets and as a pre-QA audit. Not image file generation
  (image-optimization does conversion; this skill sets the budgets).
metadata: {version: 1.0.0, category: frontend, tier: B}
---
# Performance

## Purpose
Local-business sites must load instantly on mid mobile - speed is a
conversion feature and a retainer selling point.

## Inputs
src/, assets/, hero-media weight rules.

## Outputs
Budget-compliant loading setup; numbers recorded in BUILD_STATE.md notes.

## Rules
1. Budgets (mobile): page weight <= 1.5MB excl. hero video; hero video per
   hero-media caps; LCP target < 2.5s on simulated 4G; CLS < 0.1
   (width/height everywhere); JS total < 60KB before GSAP/three, which
   must be deferred and non-blocking.
2. Images: .webp with sized variants via srcset for anything > 400px
   display width; loading=lazy below the fold; hero poster preloaded,
   never lazy.
3. Fonts: <= 3 woff2 files, font-display swap, preload the above-the-fold
   heading face only.
4. Scripts: defer everything; no script in <head> without defer; third-party
   (Calendly, analytics) loaded per their skill's lazy pattern.
5. CSS: 4 files per file-structure contract, no @import chains.
6. Verify: no Lighthouse in this environment by default - do a manual
   weight audit (sum asset bytes referenced per page) and record it. If
   the user has Lighthouse/PageSpeed available, ask them to run it and
   paste scores; treat unverified budgets as open QA items, not passes.

## References
- references/loading-strategy.md

## Anti-patterns
- Claiming a Core Web Vitals pass without a measurement to point to.

## Changelog
- 1.0.0 initial
