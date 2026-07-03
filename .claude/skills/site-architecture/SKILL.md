---
name: site-architecture
description: Decide page map, navigation, and per-page section composition
  for a local small-business website. Use in pipeline Phase 1, or when
  adding/removing pages. Not for visual design (design-direction) or
  copy (copywriting).
metadata: {version: 1.0.0, category: process, tier: A}
---
# Site Architecture

## Purpose
Turn client.md Pages + Services + Audience into a concrete sitemap and a
section list per page that every later phase builds against.

## Inputs
client/client.md (Pages, Services, Audience, Links), contracts/component-api.md

## Outputs
Sitemap + per-page section lists appended to state/DECISIONS.md.

## Rules
1. Default for local businesses: fewer pages, stronger pages. If client
   listed only "Home", propose a single-page site with anchor nav
   (references/single-page.md). 5+ services with distinct search intent
   justify separate service pages (SEO), otherwise one Services page.
2. Every page gets: purpose (one line), primary conversion action
   (call / book / form), ordered section list using standard names from
   contracts/component-api.md.
3. Conversion action appears within the first viewport of every page and
   again at the bottom (cta section).
4. Nav: max 6 items; phone number always visible in header on mobile
   for call-first niches (HVAC, dental, restaurants).
5. Contact page exists whenever a physical address exists; embed map per
   maps-gbp skill flag.
6. Log the architecture in DECISIONS.md before proceeding - later phases
   treat it as level-3 precedence.

## Decision guide
| Situation | Approach |
|---|---|
| 1-3 services, walk-in business | Single page + anchors |
| Services with distinct search terms | /services/<service>.html each |
| Client insists on many thin pages | Push back once in QUESTIONS.md with SEO reasoning, then obey |

## References
- references/single-page.md - anchor-nav pattern, section order defaults
- references/multi-page.md - shared header/footer strategy, URL naming

## Anti-patterns
- Blog scaffolding for clients with no content plan.
- Deep nav hierarchies for a 6-page site.

## Changelog
- 1.0.0 initial
