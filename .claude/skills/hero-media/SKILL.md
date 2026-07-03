---
name: hero-media
description: Implement hero sections with motion media - MP4 video vs JPEG
  image-sequence selection, play-once-then-freeze, reverse-then-freeze, and
  localStorage returning-visitor detection. Use when building or editing any
  hero with video/sequence media. Not for general page animation
  (frontend-animation) or generating the media itself (media-generation).
metadata: {version: 1.0.0, category: frontend, tier: B}
---
# Hero Media

## Purpose
Cinematic hero motion that is fast, robust, and plays exactly once per
visitor - the agency's signature hero system.

## Inputs
client.md Stack hero-media flag, generated assets in assets/video/ (with
MEDIA_LOG rows), tokens.css, contracts/file-structure.md.

## Outputs
Hero section markup + src/js/hero.js + poster assets wired in.

## Rules
1. Format decision per references/mp4-vs-sequence.md. Default: MP4
   (h.264, muted, playsinline) with .webp poster. Sequence only when
   scroll-scrubbing or transparency is required.
2. Behavior default: play once on first visit, freeze on final frame;
   returning visitors (localStorage flag, site-slug prefixed) see the
   final frame immediately - templates/returning-visitor.js.
3. Play-once: templates/play-once-freeze.js (pause on 'ended', never
   loop). Reverse effects: templates/reverse-freeze.js (rAF-driven
   currentTime stepping - native reverse playback is not reliable).
4. Poster is mandatory and is the LCP candidate: preload it, size it,
   never lazy-load hero media.
5. Reduced motion: prefers-reduced-motion users get the poster only -
   wire in JS, not just CSS.
6. Autoplay requires muted + playsinline; never audio. If autoplay is
   blocked, the poster stands - design so the frozen frame is a complete
   hero on its own.
7. Weight budget: hero video <= 2.5MB target, <= 4MB hard cap, <= 8s;
   over budget -> re-encode or cut before shipping (performance skill
   verifies).

## References
- references/mp4-vs-sequence.md - decision table + encoding settings

## Scripts / Templates
- templates/hero-video.html - canonical markup
- templates/play-once-freeze.js, reverse-freeze.js, returning-visitor.js
  (copy into src/js/hero.js and adapt; keep the defensive guards)

## Anti-patterns
- Looping hero video (distracting, battery); YouTube embeds as heroes;
  lazy-loading the poster; localStorage keys without site prefix.

## Changelog
- 1.0.0 initial (encodes patterns from prior client work)
