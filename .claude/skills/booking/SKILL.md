---
name: booking
description: Embed Calendly booking - inline widget or popup button - styled
  to the site and lazy-loaded. Use when Stack booking:calendly. Not for
  contact forms (forms).
metadata: {version: 1.0.0, category: integrations, tier: D}
---
# Booking

## Purpose
Frictionless booking without owning a scheduling backend.

## Inputs
Calendly link from client.md Links (absent -> QUESTIONS.md), design tokens.

## Outputs
Booking section/CTA wiring with lazy-loaded Calendly embed.

## Rules
1. Default: inline embed on the contact/booking section for
   consideration niches (dental, gym); popup-button pattern when booking
   is secondary to calling.
2. Lazy facade: render a styled placeholder (btn/skeleton at the embed's
   reserved height ~700px to prevent CLS); inject Calendly's script +
   widget on near-viewport or click - never in initial page load
   (performance skill).
3. Pass utm/source params on the Calendly URL so the client can attribute
   bookings to the site.
4. Style: Calendly embed colors via its URL params matched to tokens
   (primary/text/bg hex) - keep the widget from clashing.
5. No-JS fallback: plain link to the Calendly page, always present under
   the embed.
6. QA click-path: open the real widget, step to the date screen (don't
   book), verify colors and mobile fit at 360px.

## Anti-patterns
- Autoloading Calendly JS on every page; iframe with no reserved height.

## Changelog
- 1.0.0 initial
