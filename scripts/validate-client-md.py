#!/usr/bin/env python3
"""Validate client/client.md against the schema. Exit 1 on blockers."""
import re, sys, pathlib

CLIENT = pathlib.Path("client/client.md")
REQUIRED = ["Business", "Contact", "Services", "Pages", "Brand",
            "Audience", "Mood", "Stack"]
OPTIONAL = ["Links", "Testimonials", "Photos", "Competitors",
            "Style references", "Special requests", "Autonomy"]
STACK_KEYS = {
    "animation": {"gsap", "css-only", "none"},
    "3d": {"yes", "no"},
    "booking": {"calendly", "none"},
    "forms": {"formspree", "none"},
    "email-marketing": {"brevo", "none"},
    "analytics": {"ga4", "plausible", "none"},
    "hero-media": {"video", "image-sequence", "static", "propose"},
}

if not CLIENT.exists():
    print("BLOCKER: client/client.md missing"); sys.exit(1)

text = CLIENT.read_text(encoding="utf-8")
sections = {}
for m in re.finditer(r"^## (.+?)\s*$", text, re.M):
    start = m.end()
    nxt = re.search(r"^## ", text[start:], re.M)
    sections[m.group(1).strip()] = text[start:start + nxt.start() if nxt else len(text)].strip()

blockers, soft = [], []
for s in REQUIRED:
    body = sections.get(s)
    if body is None:
        blockers.append(f"required section '## {s}' missing")
    elif "TODO" in body or not body:
        blockers.append(f"required section '## {s}' incomplete (contains TODO or empty)")
for s in OPTIONAL:
    body = sections.get(s, "")
    if not body or "TODO" in body:
        soft.append(f"optional section '## {s}' missing or TODO")

stack = sections.get("Stack", "")
found = {}
for line in stack.splitlines():
    if ":" in line:
        k, v = line.split(":", 1)
        found[k.strip()] = v.strip()
for k, allowed in STACK_KEYS.items():
    v = found.get(k)
    if v is None:
        blockers.append(f"Stack flag '{k}' missing")
    elif v not in allowed:
        blockers.append(f"Stack flag '{k}: {v}' invalid (allowed: {sorted(allowed)})")

print("=== CLIENT.MD VALIDATION ===")
for b in blockers: print(f"BLOCKER  {b}")
for s in soft:     print(f"SOFT     {s}")
print(f"{len(blockers)} blockers, {len(soft)} soft gaps")
sys.exit(1 if blockers else 0)
