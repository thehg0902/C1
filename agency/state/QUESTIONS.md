# Open Questions for the Client / Owner
<!-- Written by the pipeline. Answered inline by the human, then promoted
     to DECISIONS.md. Format:
     - [ ] Q: ...   A: (pending) -->

## Resolved at intake (2026-07-03)

These gaps were found during Phase 0 validation and resolved directly with
the human in the same session rather than left pending. Promoted to
agency/state/DECISIONS.md; kept here only as an audit trail.

- [x] Q: Stack.booking value "leave space for calandly integration" is not a
      valid enum (calendly|none). Normalize to which value?
      A: `calendly`
- [x] Q: Contact.Email is "na" — is there a business email to publish?
      A: None. Call/form only, no email published anywhere on the site.
- [x] Q: Contact.Address is "na" — is there a street address, or is this a
      service-area business?
      A: Service-area model, no storefront/public address.
- [x] Q: What service area should the site reference in place of an address?
      A: Toronto, framed with "GTA / surrounding areas" as regional context.
- [x] Q: Links.Google Maps and Links.Socials are both "na" — provide, or omit?
      A: Omit both. No maps embed, no social icons/links.
- [x] Q: Optional sections Competitors / Style references are missing —
      provide any, or proceed without?
      A: None provided. Design direction relies on mood + niche + given
      brand colors only.
- [x] Q: Optional section Autonomy is missing — how much creative latitude
      should Claude take on ambiguous decisions?
      A: HIGH — make reasonable judgment calls independently; only surface
      genuinely ambiguous or high-stakes items. (Phase 4 media approval gate
      is a hard stop regardless of autonomy level.)
- [x] Q: Is C Plus Roofing Inc licensed and insured (trust claim for copy)?
      A: Yes — state it.
- [x] Q: Does C Plus Roofing offer true 24/7 emergency response, or standard
      business hours with urgent priority?
      A: True 24/7 emergency service.

## Open at Phase 5 (2026-07-03)

- [ ] Q: What is the Formspree form ID for the contact form (or should a
      new Formspree form be created for this client, and if so which email
      address should receive submissions)?
      A: (pending) - contact.html currently ships with a placeholder
      action="https://formspree.io/f/YOUR_FORM_ID"; main.js detects the
      placeholder and lets the browser's native form submit happen instead
      of silently failing, but the form will not actually deliver anywhere
      until this is set.
- [ ] Q: What is the exact Calendly scheduling link (username/event type)
      to embed on contact.html?
      A: (pending) - contact.html currently ships with a placeholder
      data-calendly-url="https://calendly.com/YOUR_CALENDLY_LINK"; the
      lazy-load script in main.js detects the placeholder and leaves the
      static "call us to schedule" fallback link active instead of loading
      a broken widget.
