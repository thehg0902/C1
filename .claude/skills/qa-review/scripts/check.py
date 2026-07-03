#!/usr/bin/env python3
"""Agency OS automated QA gate. Run from repo root. Exit 1 on any FAIL."""
import re, sys, pathlib

ROOT = pathlib.Path(".")
SRC = ROOT / "src"
fails, warns = [], []

def fail(msg): fails.append(msg)
def warn(msg): warns.append(msg)

html_files = sorted(SRC.rglob("*.html"))
css_files  = sorted(SRC.rglob("*.css"))
js_files   = sorted(SRC.rglob("*.js"))

if not html_files:
    fail("no HTML files in src/ - nothing to QA")

for f in html_files + css_files + js_files:
    text = f.read_text(encoding="utf-8", errors="replace")
    if "[PLACEHOLDER" in text: fail(f"{f}: unresolved [PLACEHOLDER]")
    if re.search(r"\bTODO\b", text): fail(f"{f}: leftover TODO")
    if "lorem ipsum" in text.lower(): fail(f"{f}: lorem ipsum")

for f in html_files:
    text = f.read_text(encoding="utf-8", errors="replace")
    # local refs exist
    for m in re.finditer(r'(?:src|href)="([^"#][^":]*?)"', text):
        ref = m.group(1)
        if ref.startswith(("http", "mailto:", "tel:", "//", "data:")): continue
        target = (f.parent / ref).resolve()
        if not target.exists():
            fail(f"{f}: broken local ref -> {ref}")
    # img alt
    for m in re.finditer(r"<img\b[^>]*>", text):
        if "alt=" not in m.group(0): fail(f"{f}: <img> missing alt")
    # single h1
    n_h1 = len(re.findall(r"<h1\b", text))
    if n_h1 != 1: fail(f"{f}: {n_h1} <h1> tags (need exactly 1)")
    if "<main" not in text: warn(f"{f}: no <main> landmark")

# hardcoded colors outside tokens.css
for f in css_files:
    if f.name == "tokens.css": continue
    text = f.read_text(encoding="utf-8", errors="replace")
    for m in re.finditer(r"#[0-9a-fA-F]{3,8}\b|rgb\(", text):
        fail(f"{f}: hardcoded color '{m.group(0)}' (use var(--token))"); break

# header/footer drift across pages
def block(tag, text):
    m = re.search(rf"<{tag}\b.*?</{tag}>", text, re.S)
    return re.sub(r"\s+", " ", m.group(0)) if m else None
if len(html_files) > 1:
    base = html_files[0].read_text(encoding="utf-8", errors="replace")
    for tag in ("header", "footer"):
        ref_block = block(tag, base)
        for f in html_files[1:]:
            other = block(tag, f.read_text(encoding="utf-8", errors="replace"))
            if ref_block and other and ref_block != other:
                warn(f"{f}: <{tag}> differs from {html_files[0].name} (drift?)")

# media log consistency
log = ROOT / "agency" / "state" / "MEDIA_LOG.md"
if log.exists():
    for line in log.read_text().splitlines():
        if "| generated" in line or "| in-use" in line:
            cells = [c.strip() for c in line.split("|")]
            if len(cells) > 8 and cells[8] not in ("-", "") and not (ROOT / cells[8]).exists():
                fail(f"MEDIA_LOG: file missing on disk -> {cells[8]}")

print("=== QA CHECK ===")
for w in warns: print(f"WARN  {w}")
for x in fails: print(f"FAIL  {x}")
print(f"{len(fails)} fail, {len(warns)} warn")
sys.exit(1 if fails else 0)
