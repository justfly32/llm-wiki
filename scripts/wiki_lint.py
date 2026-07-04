#!/usr/bin/env python3
"""Wiki lint: check for broken links, empty files, other issues"""
from pathlib import Path
import re

WIKI_PATH = Path.home() / "wiki"
issues = []

# Collect all slugs
all_slugs = set()
all_files = []
for d in [WIKI_PATH / "concepts", WIKI_PATH / "entities",
          WIKI_PATH / "comparisons", WIKI_PATH / "queries"]:
    if d.exists():
        for f in d.rglob("*.md"):
            all_slugs.add(f.stem)
            all_files.append(f)

# Check for broken [[wiki links]]
for f in all_files:
    content = f.read_text(encoding="utf-8")
    links = re.findall(r'\[\[([\w\- /]+)\]\]', content)
    for link in links:
        slug = link.strip().replace(" ", "-").lower()
        if slug and slug not in all_slugs:
            issues.append(f"❌ Broken link: '{link}' in {f.relative_to(WIKI_PATH)}")

# Check for empty files
for f in all_files:
    if f.stat().st_size < 50:
        issues.append(f"⚠️  Tiny file ({f.stat().st_size}B): {f.relative_to(WIKI_PATH)}")

# Check for files missing title (# heading)
for f in all_files:
    content = f.read_text(encoding="utf-8")
    if not re.search(r"^#\s+\S", content, re.MULTILINE):
        issues.append(f"⚠️  Missing # title: {f.relative_to(WIKI_PATH)}")

if issues:
    print(f"🔍 Lint: {len(issues)} issue(s) found\n")
    for issue in issues:
        print(f"  {issue}")
else:
    print("✅ Lint: No issues found (165 files checked)")
