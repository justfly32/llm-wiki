#!/usr/bin/env python3
"""
PC 마크다운 파일 일괄 수집 스크립트
- 로컬 md 파일을 읽어서 LLM으로 요약 + 태깅
- 위키 페이지로 저장 (raw/ + concepts/)
- 중복 건너뛰기, 진행률 표시
"""
import os, re, json, hashlib, sys
from pathlib import Path
from datetime import date

WIKI_PATH = Path.home() / "wiki"
RAW_DIR = WIKI_PATH / "raw" / "local"
CONCEPTS_DIR = WIKI_PATH / "concepts"
ENTITIES_DIR = WIKI_PATH / "entities"
INDEX_FILE = WIKI_PATH / "index.md"
LOG_FILE = WIKI_PATH / "log.md"
PROGRESS_FILE = WIKI_PATH / ".local_ingest_progress.json"

# 제외 패턴
EXCLUDE_DIRS = ["node_modules", ".git", "__pycache__", "venv", ".venv", "site-packages", ".npm", ".cache", "dist", "build", "skills"]
EXCLUDE_FILES = {"readme.md", "changelog.md", "license.md", "package.md"}

# 수집 대상 디렉토리
INCLUDE_DIRS = [
    "projects",
    "Documents",
    "coding_projects",
    ".hermes/memories",
]

def should_include(f: Path) -> bool:
    for ex in EXCLUDE_DIRS:
        if ex in f.parts:
            return False
    if f.name.lower() in EXCLUDE_FILES:
        return False
    return True

def collect_files() -> list:
    home = Path.home()
    files = []
    for d_name in INCLUDE_DIRS:
        d = home / d_name
        if d.exists():
            for f in d.rglob("*.md"):
                if should_include(f) and 200 < f.stat().st_size < 80_000:
                    files.append(f)
    return files

def load_progress() -> dict:
    if PROGRESS_FILE.exists():
        return json.loads(PROGRESS_FILE.read_text())
    return {"ingested": [], "failed": [], "skipped": []}

def save_progress(p: dict):
    PROGRESS_FILE.write_text(json.dumps(p, indent=2))

def slugify(text: str, max_len: int = 50) -> str:
    slug = re.sub(r"[^\w\-]", "-", text.lower())[:max_len].strip("-")
    return re.sub(r"-+", "-", slug)

def file_hash(content: str) -> str:
    return hashlib.md5(content.encode()).hexdigest()[:12]

def detect_category(filepath: Path) -> str:
    """파일 경로 기반 카테고리 자동 분류"""
    parts = [p.lower() for p in filepath.parts]
    path_str = str(filepath).lower()
    
    if "memory" in path_str or "daily_memory" in path_str:
        return "memory"
    if "hermes_ops" in path_str or "hermes-guide" in path_str:
        return "hermes"
    if "investment" in path_str or "stock" in path_str or "gold" in path_str:
        return "investment"
    if "security" in path_str:
        return "security"
    if "db-ontology" in path_str or "netmaster" in path_str:
        return "project"
    if "claude" in path_str or "agent" in path_str:
        return "ai-ml"
    if "personal-site" in path_str or "post1" in path_str:
        return "web"
    if "business" in path_str or "legal" in path_str:
        return "business"
    if "world_news" in path_str:
        return "news"
    if "univ" in path_str:
        return "education"
    return "general"

def auto_tag(content: str, filepath: Path) -> list:
    """내용 + 경로 기반 자동 태깅"""
    tags = []
    cat = detect_category(filepath)
    
    cat_tags = {
        "memory": ["personal", "memory"],
        "hermes": ["hermes", "ai-ml", "tool"],
        "investment": ["investment", "finance", "business"],
        "security": ["security", "system"],
        "project": ["project", "programming"],
        "ai-ml": ["ai-ml", "programming", "research"],
        "web": ["web", "programming"],
        "business": ["business", "research"],
        "news": ["news", "world"],
        "education": ["education", "personal"],
        "general": ["document"],
    }
    tags.extend(cat_tags.get(cat, ["document"]))
    
    # 내용 기반 추가 태깅
    text = content.lower()
    content_tags = {
        "python": "python",
        "javascript": "javascript",
        "docker": "devops",
        "kubernetes": "devops",
        "api": "api",
        "database": "database",
        "sql": "database",
        "machine learning": "ai-ml",
        "deep learning": "ai-ml",
        "neural": "ai-ml",
        "transformer": "ai-ml",
        "llm": "ai-ml",
        "gpt": "ai-ml",
        "claude": "ai-ml",
        "react": "web",
        "html": "web",
        "css": "web",
        "flask": "web",
        "fastapi": "web",
    }
    for keyword, tag in content_tags.items():
        if keyword in text and tag not in tags:
            tags.append(tag)
    
    return list(dict.fromkeys(tags))[:5]  # 중복 제거, 최대 5개

def extract_title(content: str, filepath: Path) -> str:
    """제목 추출"""
    # 첫 번째 # 제목
    m = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if m:
        return m.group(1).strip()[:80]
    # 파일명
    return filepath.stem.replace("-", " ").replace("_", " ").title()

def create_wiki_page(filepath: Path, content: str) -> dict:
    """파일 → 위키 페이지 생성"""
    result = {"file": str(filepath), "status": "error", "slug": ""}
    
    try:
        today = date.today().isoformat()
        title = extract_title(content, filepath)
        slug = slugify(f"{filepath.parent.name}-{filepath.stem}")
        tags = auto_tag(content, filepath)
        fhash = file_hash(content)
        
        # 원본 저장
        raw_dir = RAW_DIR / detect_category(filepath)
        raw_dir.mkdir(parents=True, exist_ok=True)
        raw_path = raw_dir / f"{slug}-{today}.md"
        
        raw_fm = (
            f"---\n"
            f"source_file: {filepath}\n"
            f"ingested: {today}\n"
            f"sha256: {fhash}\n"
            f"category: {detect_category(filepath)}\n"
            f"original_title: {title}\n"
            f"---\n\n"
        )
        raw_path.write_text(raw_fm + content, encoding="utf-8")
        
        # 컨셉 페이지 생성
        concept_path = CONCEPTS_DIR / f"{slug}.md"
        
        # 본문 정리 (frontmatter 제거, 너무 긴 건 잘라기)
        body = re.sub(r"^---\s*\n.*?\n---\s*\n", "", content, flags=re.DOTALL)
        if len(body) > 3000:
            body = body[:3000] + "\n\n...(내용 생략)..."
        
        concept_fm = (
            f"---\n"
            f"title: {title}\n"
            f"created: {today}\n"
            f"updated: {today}\n"
            f"type: concept\n"
            f"tags: [{', '.join(tags)}]\n"
            f"sources: [raw/local/{raw_path.parent.name}/{raw_path.name}]\n"
            f"source_file: {filepath}\n"
            f"confidence: high\n"
            f"---\n\n"
        )
        
        concept_body = (
            f"# {title}\n\n"
            f"> 📁 원본: `{filepath}`\n"
            f"> 📅 수집: {today}\n"
            f"> 🏷️ 카테고리: {detect_category(filepath)}\n\n"
            f"## 내용\n\n"
            f"{body}\n"
        )
        
        concept_path.write_text(concept_fm + concept_body, encoding="utf-8")
        
        result["status"] = "ok"
        result["slug"] = slug
        result["title"] = title
        result["tags"] = tags
        
    except Exception as e:
        result["error"] = str(e)
    
    return result

def update_index():
    """index.md 업데이트"""
    pages = []
    for d in [CONCEPTS_DIR, ENTITIES_DIR, WIKI_PATH / "comparisons", WIKI_PATH / "queries"]:
        for f in d.glob("*.md"):
            content = f.read_text(encoding="utf-8")
            title_m = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
            title = title_m.group(1).strip() if title_m else f.stem
            pages.append((f.stem, title))
    
    lines = [
        "# Wiki Index",
        "",
        f"> Last updated: {date.today().isoformat()}",
        f"> Total: {len(pages)} pages",
        "",
    ]
    for slug, title in sorted(pages, key=lambda x: x[1]):
        lines.append(f"- [[{slug}]] — {title}")
    
    INDEX_FILE.write_text("\n".join(lines), encoding="utf-8")

def append_log(action: str, subject: str):
    today = date.today().isoformat()
    with open(LOG_FILE, "a") as f:
        f.write(f"\n## [{today}] {action} | {subject}\n")

def main():
    print("=" * 60)
    print("📥 PC 마크다운 파일 일괄 수집")
    print("=" * 60)
    
    files = collect_files()
    progress = load_progress()
    
    print(f"\n수집 대상: {len(files)}개")
    print(f"이미 수집됨: {len(progress['ingested'])}개")
    print(f"건너뛸 파일: {len([f for f in files if file_hash(f.read_text(encoding='utf-8', errors='ignore')) in progress['ingested']])}개")
    print()
    
    success, skip, fail = 0, 0, 0
    
    for i, f in enumerate(files, 1):
        try:
            content = f.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            fail += 1
            continue
        
        fhash = file_hash(content)
        
        # 중복 체크
        if fhash in progress["ingested"]:
            skip += 1
            continue
        
        # 진행률
        rel = f.relative_to(Path.home())
        print(f"  [{i}/{len(files)}] {rel} ({len(content)//1024}KB)", end=" ")
        
        result = create_wiki_page(f, content)
        
        if result["status"] == "ok":
            progress["ingested"].append(fhash)
            success += 1
            print(f"✅ {result['title'][:40]} [{', '.join(result['tags'][:2])}]")
        else:
            progress["failed"].append(str(f))
            fail += 1
            print(f"❌ {result.get('error', 'unknown')[:50]}")
        
        # 10개마다 진행 저장
        if i % 10 == 0:
            save_progress(progress)
    
    # 최종 저장
    save_progress(progress)
    update_index()
    append_log("batch_ingest", f"PC files: {success} new, {skip} skip, {fail} fail")
    
    print(f"\n{'=' * 60}")
    print(f"✅ 수집 완료!")
    print(f"   새로 수집: {success}개")
    print(f"   건너뜀: {skip}개")
    print(f"   실패: {fail}개")
    print(f"   전체 위키 페이지: {len(progress['ingested'])}개")

if __name__ == "__main__":
    main()
