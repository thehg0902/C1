---
name: email-marketing
description: Brevo newsletter/lead signup embed - styled form posting to a
  Brevo list, GDPR-appropriate consent line. Use when Stack
  email-marketing:brevo. Not for contact/quote forms (forms).
metadata: {version: 1.0.0, category: integrations, tier: D}
---
# Email Marketing

## Purpose
List growth for retainer-tier marketing without heavy embeds.

## Inputs
Brevo form action URL/ID from client setup (absent -> QUESTIONS.md:
create the form in Brevo, send the embed action URL).

## Outputs
Signup block (usually footer or a band section) wired to Brevo.

## Rules
1. Prefer Brevo's plain HTML form action over their script embed: style
   it with site tokens, single email field + submit, honeypot if their
   embed provides one.
2. Consent: one-line plain-language consent text + link to privacy page
   (legal-pages skill) - REQUIRED for CA/CASL context; unsubscribe is
   Brevo's job, mention "unsubscribe anytime".
3. Success/error handled inline (aria-live) if using fetch; otherwise
   Brevo's redirect back to a ?subscribed=1 param the page acknowledges.
4. One signup block per page maximum; never a popup/interstitial unless
   the client explicitly requests it (and push back once via QUESTIONS.md).
5. Double opt-in recommended to the client (deliverability) - their call,
   configured in Brevo, log the decision.

## Anti-patterns
- Loading Brevo's full script sitewide for one footer form.

## Changelog
- 1.0.0 initial
