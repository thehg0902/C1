---
name: seo-technical
description: Technical + local SEO - titles, meta descriptions, Open Graph,
  schema.org LocalBusiness JSON-LD, sitemap.xml, robots.txt, GBP/NAP
  consistency. Use in Phase 5 finishing pass. Not copy tone (copywriting)
  or GBP embeds (maps-gbp).
metadata: {version: 1.0.0, category: seo, tier: B}
---
# SEO Technical

## Purpose
Local businesses win on local pack + a technically clean site; this skill
covers the on-site half.

## Inputs
client.md (Business, Contact, Links, Services), final pages in src/.

## Outputs
Per-page head metadata, JSON-LD, sitemap.xml, robots.txt.

## Rules
1. Title pattern: {Primary service/what} in {City} | {Business Name} -
   <= 60 chars, unique per page. Meta description <= 155 chars, contains
   the page's conversion offer.
2. NAP (name/address/phone) rendered in HTML footer/contact must match
   client.md and GBP EXACTLY, character for character (references/local-seo.md).
3. JSON-LD: LocalBusiness (or subtype - Dentist, Restaurant, HVACBusiness
   etc.) per references/structured-data.md; one block, on every page,
   facts only from client.md.
4. OG/Twitter: og:title, og:description, og:image (1200x630 derived from
   hero poster), og:url per page.
5. sitemap.xml lists every html page with the final domain (ask if domain
   unknown -> QUESTIONS.md); robots.txt allows all + sitemap line.
6. Canonical tag per page; no duplicate titles/descriptions (qa should
   catch, but own it here).

## References
- references/local-seo.md, references/structured-data.md

## Anti-patterns
- Keyword-stuffed titles; schema claiming ratings/reviews not on the page;
  guessing the domain.

## Changelog
- 1.0.0 initial
