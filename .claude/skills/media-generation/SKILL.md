---
name: media-generation
description: Plan and generate AI media (Higgsfield) for the site - storyboard
  first, human approval gate, then generation, all logged to MEDIA_LOG.md.
  Use in pipeline Phase 4 or whenever new media is needed. Not for
  optimizing/converting files (image-optimization) or hero playback code
  (hero-media).
metadata: {version: 1.0.0, category: media, tier: C}
---
# Media Generation

## Purpose
Consistent, on-direction media at controlled credit cost, with a hard
human gate before any credit is spent.

## Inputs
Design direction imagery style (DECISIONS.md), client.md Photos section
(what exists vs what's needed), contracts/media-log.md.

## Outputs
Storyboard rows (status=planned) in state/MEDIA_LOG.md -> after human
approval -> generated assets in assets/ + updated rows.

## Rules
1. HARD INVARIANT (CLAUDE.md): no paid generation without a MEDIA_LOG row
   whose storyboard-approved column the HUMAN set to YES. Claude never
   writes YES in that column. Ever.
2. Storyboard first: for each needed asset write a row - type (image/video),
   intended placement, model choice, prompt summary, estimated credits.
   Present the storyboard, then STOP.
3. Real client photos beat generated media - generate only what intake
   says is missing. Never generate fake team members, fake premises
   interiors presented as real, or fake review/before-after imagery.
4. Prompt consistency: one style block (from references/image-prompts.md,
   built from the design direction) reused verbatim across all prompts
   for the site.
5. Video for hero per hero-media constraints (duration/weight targets
   inform the generation settings - see references/video-prompts.md).
6. After generation: fill actual credits, set status=generated, hand files
   to image-optimization before they enter assets/.
7. Budget per references/credit-budgeting.md; nearing the per-site cap ->
   stop and ask.

## References
- references/image-prompts.md, video-prompts.md, credit-budgeting.md

## Anti-patterns
- "Client said generate whatever" as gate bypass (invariant holds);
  regenerating on taste without logging the rejected row.

## Changelog
- 1.0.0 initial (encodes the storyboard-approval workflow)
