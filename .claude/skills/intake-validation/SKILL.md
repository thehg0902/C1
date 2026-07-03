---
name: intake-validation
description: Validate agency/client/client.md against agency/client/client.schema.md and
  turn every gap into a client question. Use at the start of every build
  (pipeline Phase 0) or whenever client.md changes. Not for validating
  code or site output (see qa-review).
metadata: {version: 1.0.0, category: process, tier: A}
---
# Intake Validation

## Purpose
Convert an incomplete client brief into either a green light or a precise
question list, so no phase ever runs on invented facts.

## Inputs
agency/client/client.md, agency/client/client.schema.md

## Outputs
agency/state/QUESTIONS.md entries; phase 0 status in agency/state/BUILD_STATE.md.

## Rules
1. Run `python3 agency/scripts/validate-client-md.py` first. It is authoritative
   for missing/TODO required sections and malformed Stack flags.
2. Classify each gap: BLOCKER (required section missing/TODO) or
   SOFT (optional section missing that would improve quality).
3. Every gap becomes one specific, answerable question in
   agency/state/QUESTIONS.md - phrased for a non-technical business owner.
   Bad: "Provide brand guidelines." Good: "Do you have exact brand colors
   (hex codes)? If not, reply 'propose' and I'll design a palette."
4. BLOCKERs: mark phase 0 blocked and stop the pipeline. SOFT gaps:
   proceed, but mark affected copy/design as [PLACEHOLDER] until answered.
5. Sanity-check consistency: pages listed vs services described, booking
   flag vs booking link provided, logo path actually exists in
   assets-intake. Inconsistencies are questions, not silent fixes.

## Anti-patterns
- Filling a missing phone/address/price from the web without logging it
  as a decision. GBP/Maps data may be scraped ONLY as a proposed answer
  in QUESTIONS.md, never straight into the site.
- Asking vague or compound questions.

## Changelog
- 1.0.0 initial
