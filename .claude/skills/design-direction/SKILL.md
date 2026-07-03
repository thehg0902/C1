---
name: design-direction
description: Translate client mood adjectives + niche into a concrete visual
  direction (style, imagery, layout personality) before any tokens or code.
  Use in pipeline Phase 2 before design-tokens. Not for producing CSS
  (design-tokens does that).
metadata: {version: 1.0.0, category: design, tier: A}
---
# Design Direction

## Purpose
Prevent generic template-looking output by committing to a specific,
client-appropriate visual direction and writing it down before building.

## Inputs
client/client.md (Mood, Audience, Brand, Style references, Niche),
niche playbook in references/.

## Outputs
A 10-line design rationale in state/DECISIONS.md: direction name, type
pairing intent, color intent, imagery style, layout personality, motion
level.

## Rules
1. Read the matching niche playbook in references/ first; it encodes what
   converts for that business type. No playbook for the niche: use the
   closest one and note the adaptation in DECISIONS.md.
2. Mood adjectives are the brief. "Warm, premium, trustworthy" and
   "bold, energetic, young" must produce visibly different sites. Name
   the direction (e.g. "quiet luxury", "craft workshop", "clinical calm").
3. Client brand colors (if given) are constraints, not the whole palette -
   design-tokens expands them into the full token set.
4. Decide imagery style here (photo-real warm / editorial / illustrative)
   so media-generation prompts stay consistent.
5. Pick ONE distinctive element per site (typography scale, unusual hero
   treatment, signature section shape). One, not five.
6. Motion level (none / subtle / expressive) must match both mood and the
   Stack animation flag; conflict goes to QUESTIONS.md.

## References
- references/coffee-shop.md, restaurant.md, gym.md, hvac.md, dental.md

## Anti-patterns
- Defaulting to the same palette/typeface across clients.
- Trend-chasing that fights the niche playbook (brutalism for a dentist).

## Changelog
- 1.0.0 initial
