---
name: image-optimization
description: Convert and compress media for the web - WebP conversion, srcset
  size variants, video re-encode to budget, poster extraction. Use whenever
  files move into assets/ (client photos or generated media). Not for
  choosing what to generate (media-generation).
metadata: {version: 1.0.0, category: media, tier: C}
---
# Image Optimization

## Purpose
Nothing enters assets/ raw. Every file web-ready, budget-compliant, named
per contract.

## Inputs
Files from client/assets-intake/ or fresh generations; performance budgets.

## Outputs
Optimized files in assets/images|video per file-structure contract.

## Rules
1. Images -> .webp q75-82; keep a jpg fallback only if a target embed
   requires it (og:image: use jpg/png 1200x630). Strip EXIF.
2. srcset variants for images displayed > 400px wide: 480/960/1440 widths;
   name {base}-{w}.webp.
3. Video -> hero-media encoding settings (references there are canonical);
   extract final frame as {name}-poster.webp.
4. Tooling: check availability first (which cwebp ffmpeg magick). Prefer
   scripts/optimize.sh; if tools are missing in the environment, DO NOT
   fake it - list exact commands for the user to run locally and mark the
   asset as pending-optimization in MEDIA_LOG.
5. Record final byte sizes in MEDIA_LOG prompt-summary or notes - budgets
   are verified numbers, not vibes.

## Scripts
- scripts/optimize.sh <file> - converts per rules; prints before/after bytes

## Anti-patterns
- Committing multi-MB originals to the repo; resizing with CSS instead of
  files.

## Changelog
- 1.0.0 initial
