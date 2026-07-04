#!/usr/bin/env python3
"""Rebuild wiki index.md — includes root + subdir concept files"""
from pathlib import Path
from datetime import date
import re

WIKI_PATH = Path.home() / "wiki"
INDEX_FILE = WIKI_PATH / "index.md"

pages = []

# Concepts — both root-level and subdirectories
concepts_dir = WIKI_PATH / "concepts"
if concepts_dir.exists():
    for f in sorted(concepts_dir.rglob("*.md")):
        content = f.read_text(encoding="utf-8")
        title_m = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        title = title_m.group(1).strip() if title_m else f.stem
        pages.append(("concept", f.stem, title))

# Flat dirs
for dirname, ptype in [("entities", "entity"),
                        ("comparisons", "comparison"),
                        ("queries", "query")]:
    d = WIKI_PATH / dirname
    if d.exists():
        for f in sorted(d.glob("*.md")):
            content = f.read_text(encoding="utf-8")
            title_m = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
            title = title_m.group(1).strip() if title_m else f.stem
            pages.append((ptype, f.stem, title))

pages.sort(key=lambda x: x[2].lower())

lines = [
    "# Wiki Index", "",
    f"> Content catalog. Last updated: {date.today().isoformat()}",
    f"> Total pages: {len(pages)}", ""
]

current_type = None
for ptype, slug, title in pages:
    if ptype != current_type:
        lines.append(f"## {ptype.title()}s")
        current_type = ptype
    lines.append(f"- [[{slug}]] — {title}")

INDEX_FILE.write_text("\n".join(lines), encoding="utf-8")
print(f"✅ Index rebuilt: {len(pages)} pages")
counts = {}
for p, _, _ in pages:
    counts[p] = counts.get(p, 0) + 1
for k, v in sorted(counts.items()):
    print(f"   {k.title()}s: {v}")
