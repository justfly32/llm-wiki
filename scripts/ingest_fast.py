#!/usr/bin/env python3
"""Process only new files from scan results"""
import os, re, json, hashlib, subprocess, sys
from pathlib import Path
from datetime import date

WIKI_PATH = Path.home() / "wiki"
RAW_DIR = WIKI_PATH / "raw" / "local"
CONCEPTS_DIR = WIKI_PATH / "concepts"
ENTITIES_DIR = WIKI_PATH / "entities"
INDEX_FILE = WIKI_PATH / "index.md"
LOG_FILE = WIKI_PATH / "log.md"
PROGRESS_FILE = WIKI_PATH / ".local_ingest_progress.json"
SCAN_FILE = WIKI_PATH / ".local_scan_results.json"

EXCLUDE_FILES = {"readme.md", "changelog.md", "license.md", "package.md"}

def file_hash(content):
    return hashlib.md5(content.encode()).hexdigest()[:12]

def slugify(text, max_len=50):
    slug = re.sub(r"[^\w\-]", "-", text.lower())[:max_len].strip("-")
    return re.sub(r"-+", "-", slug)

def detect_category(filepath):
    path_str = str(filepath).lower()
    if "memory" in path_str or "daily_memory" in path_str: return "memory"
    if "hermes_ops" in path_str or "hermes-guide" in path_str: return "hermes"
    if "investment" in path_str or "stock" in path_str or "gold" in path_str: return "investment"
    if "security" in path_str: return "security"
    if "db-ontology" in path_str or "netmaster" in path_str: return "project"
    if "claude" in path_str or "agent" in path_str: return "ai-ml"
    if "personal-site" in path_str or "post1" in path_str: return "web"
    if "business" in path_str or "legal" in path_str: return "business"
    if "world_news" in path_str: return "news"
    if "univ" in path_str: return "education"
    return "general"

def auto_tag(content, filepath):
    tags = []
    cat = detect_category(filepath)
    cat_tags = {
        "memory": ["personal", "memory"], "hermes": ["hermes", "ai-ml", "tool"],
        "investment": ["investment", "finance", "business"], "security": ["security", "system"],
        "project": ["project", "programming"], "ai-ml": ["ai-ml", "programming", "research"],
        "web": ["web", "programming"], "business": ["business", "research"],
        "news": ["news", "world"], "education": ["education", "personal"], "general": ["document"],
    }
    tags.extend(cat_tags.get(cat, ["document"]))
    text = content.lower()
    for kw, tag in {"python": "python", "javascript": "javascript", "docker": "devops",
        "kubernetes": "devops", "api": "api", "database": "database", "sql": "database",
        "machine learning": "ai-ml", "llm": "ai-ml", "claude": "ai-ml", "react": "web"}.items():
        if kw in text and tag not in tags:
            tags.append(tag)
    return list(dict.fromkeys(tags))[:5]

def extract_title(content, filepath):
    m = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if m: return m.group(1).strip()[:80]
    return filepath.stem.replace("-", " ").replace("_", " ").title()

def create_wiki_page(filepath, content):
    result = {"file": str(filepath), "status": "error", "hash": ""}
    try:
        today = date.today().isoformat()
        title = extract_title(content, filepath)
        slug = slugify(filepath.parent.name + "-" + filepath.stem)
        tags = auto_tag(content, filepath)
        category = detect_category(filepath)
        fhash = file_hash(content)
        result["hash"] = fhash

        raw_dir = RAW_DIR / category
        raw_dir.mkdir(parents=True, exist_ok=True)
        raw_path = raw_dir / (slug + "-" + today + ".md")
        raw_fm = ("---\n"
            "source_file: " + str(filepath) + "\n"
            "ingested: " + today + "\n"
            "sha256: " + fhash + "\n"
            "category: " + category + "\n"
            "original_title: " + title + "\n"
            "---\n\n")
        raw_path.write_text(raw_fm + content, encoding="utf-8")

        concept_path = CONCEPTS_DIR / (slug + ".md")
        body = re.sub(r"^---\s*\n.*?\n---\s*\n", "", content, flags=re.DOTALL)
        if len(body) > 3000:
            body = body[:3000] + "\n\n...(truncated)..."
        concept_fm = ("---\n"
            "title: " + title + "\n"
            "created: " + today + "\n"
            "updated: " + today + "\n"
            "type: concept\n"
            "tags: [" + ", ".join(tags) + "]\n"
            "sources: [raw/local/" + raw_path.parent.name + "/" + raw_path.name + "]\n"
            "source_file: " + str(filepath) + "\n"
            "confidence: high\n"
            "---\n\n")
        concept_body = ("# " + title + "\n\n"
            "> source: `" + str(filepath) + "`\n"
            "> date: " + today + "\n"
            "> category: " + category + "\n\n"
            "## Content\n\n" + body + "\n")
        concept_path.write_text(concept_fm + concept_body, encoding="utf-8")

        result["status"] = "ok"
        result["slug"] = slug
        result["title"] = title
        result["tags"] = tags
    except Exception as e:
        result["error"] = str(e)
    return result

def update_index():
    pages = []
    for d in [CONCEPTS_DIR, ENTITIES_DIR, WIKI_PATH / "comparisons", WIKI_PATH / "queries"]:
        if not d.exists(): continue
        for f in d.glob("*.md"):
            content = f.read_text(encoding="utf-8")
            title_m = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
            title = title_m.group(1).strip() if title_m else f.stem
            pages.append((f.stem, title))
    lines = ["# Wiki Index", "", "> Last updated: " + date.today().isoformat(),
             "> Total: " + str(len(pages)) + " pages", ""]
    for slug, title in sorted(pages, key=lambda x: x[1]):
        lines.append("- [[" + slug + "]] - " + title)
    INDEX_FILE.write_text("\n".join(lines), encoding="utf-8")

def append_log(action, subject):
    today = date.today().isoformat()
    with open(LOG_FILE, "a") as f:
        f.write("\n## [" + today + "] " + action + " | " + subject + "\n")

def main():
    progress = json.loads(PROGRESS_FILE.read_text()) if PROGRESS_FILE.exists() else {"ingested": [], "failed": [], "skipped": []}
    home = Path.home()
    all_files = []

    # Load scan results from non-Documents dirs
    if SCAN_FILE.exists():
        scan = json.loads(SCAN_FILE.read_text())
        for fp in scan.get("files", []):
            all_files.append(Path(fp))

    # Scan Documents with longer timeout
    print("Scanning Documents (max 5 min)...")
    docs_dir = home / "Documents"
    if docs_dir.exists():
        try:
            result = subprocess.run(
                ["find", str(docs_dir), "-name", "*.md", "-size", "+200c", "-size", "-80000c"],
                capture_output=True, text=True, timeout=300
            )
            doc_count = 0
            for line in result.stdout.strip().split("\n"):
                if not line: continue
                f = Path(line)
                ex_dirs = ["node_modules", ".git", "__pycache__", "venv", ".venv", "site-packages", ".npm", ".cache", "dist", "build", ".claude", "skills"]
                if any(ex in f.parts for ex in ex_dirs): continue
                if f.name.lower() in EXCLUDE_FILES: continue
                all_files.append(f)
                doc_count += 1
            print("Documents: " + str(doc_count) + " files found")
        except subprocess.TimeoutExpired:
            print("Documents scan timed out! (5 min)")

    print("Total targets: " + str(len(all_files)))

    success, skip, fail = 0, 0, 0

    for i, f in enumerate(all_files, 1):
        try:
            content = f.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            fail += 1
            continue

        fhash = file_hash(content)
        if fhash in progress["ingested"]:
            skip += 1
            continue

        rel = f.relative_to(home)
        sys.stdout.write("  [" + str(i) + "/" + str(len(all_files)) + "] " + str(rel) + " (" + str(len(content)//1024) + "KB) ")
        sys.stdout.flush()

        result = create_wiki_page(f, content)

        if result["status"] == "ok":
            progress["ingested"].append(fhash)
            success += 1
            print("OK " + result["title"][:40])
        else:
            progress["failed"].append(str(f))
            fail += 1
            print("FAIL " + str(result.get("error", "unknown"))[:50])

    PROGRESS_FILE.write_text(json.dumps(progress, indent=2))
    update_index()
    append_log("batch_ingest", "PC files: " + str(success) + " new, " + str(skip) + " skip, " + str(fail) + " fail")

    print("")
    print("=" * 60)
    print("Done!")
    print("  New: " + str(success))
    print("  Skip: " + str(skip))
    print("  Fail: " + str(fail))
    print("  Total wiki pages: " + str(len(progress["ingested"])))

if __name__ == "__main__":
    main()
