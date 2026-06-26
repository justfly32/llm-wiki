#!/usr/bin/env python3
"""
LLM Wiki — Karpathy's Personal Knowledge Base CLI
Based on: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

Usage:
    python3 wiki.py ingest <url_or_file>     # Ingest a source
    python3 wiki.py query <question>          # Query the wiki
    python3 wiki.py lint                      # Health check
    python3 wiki.py index                     # Rebuild index
    python3 wiki.py search <term>             # Search pages
    python3 wiki.py status                    # Wiki status
"""
import sys
import os
import re
import json
import hashlib
import subprocess
from pathlib import Path
from datetime import datetime, date
from dataclasses import dataclass, field

# ── Configuration ──────────────────────────────────

WIKI_PATH = Path(os.environ.get("WIKI_PATH", Path.home() / "wiki"))
RAW_DIR = WIKI_PATH / "raw"
ENTITIES_DIR = WIKI_PATH / "entities"
CONCEPTS_DIR = WIKI_PATH / "concepts"
COMPARISONS_DIR = WIKI_PATH / "comparisons"
QUERIES_DIR = WIKI_PATH / "queries"
ARCHIVE_DIR = WIKI_PATH / "_archive"
SCHEMA_FILE = WIKI_PATH / "SCHEMA.md"
INDEX_FILE = WIKI_PATH / "index.md"
LOG_FILE = WIKI_PATH / "log.md"

# ── Data Classes ────────────────────────────────────

@dataclass
class WikiPage:
    path: Path
    title: str = ""
    page_type: str = "concept"
    created: str = ""
    updated: str = ""
    tags: list = field(default_factory=list)
    sources: list = field(default_factory=list)
    confidence: str = "high"
    contested: bool = False
    contradictions: list = field(default_factory=list)
    body: str = ""
    wikilinks: list = field(default_factory=list)

    @staticmethod
    def parse(path: Path) -> "WikiPage":
        page = WikiPage(path=path)
        if not path.exists():
            return page

        content = path.read_text(encoding="utf-8")

        # Parse frontmatter
        fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
        if fm_match:
            fm_text = fm_match.group(1)
            page.body = content[fm_match.end():]

            for line in fm_text.splitlines():
                line = line.strip()
                if line.startswith("title:"):
                    page.title = line.split(":", 1)[1].strip().strip('"').strip("'")
                elif line.startswith("type:"):
                    page.page_type = line.split(":", 1)[1].strip()
                elif line.startswith("created:"):
                    page.created = line.split(":", 1)[1].strip()
                elif line.startswith("updated:"):
                    page.updated = line.split(":", 1)[1].strip()
                elif line.startswith("tags:"):
                    tags_str = line.split(":", 1)[1].strip()
                    page.tags = [t.strip() for t in re.findall(r'[\w-]+', tags_str)]
                elif line.startswith("sources:"):
                    src_str = line.split(":", 1)[1].strip()
                    page.sources = [s.strip() for s in re.findall(r'[\w./\-]+', src_str)]
                elif line.startswith("confidence:"):
                    page.confidence = line.split(":", 1)[1].strip()
                elif line.startswith("contested:"):
                    page.contested = line.split(":", 1)[1].strip().lower() == "true"
                elif line.startswith("contradictions:"):
                    c_str = line.split(":", 1)[1].strip()
                    page.contradictions = [c.strip() for c in re.findall(r'[\w\-]+', c_str)]
        else:
            page.body = content

        # Extract wikilinks
        page.wikilinks = re.findall(r'\[\[([\w\- ]+)\]\]', content)
        page.title = page.title or path.stem.replace("-", " ").title()

        return page

    def save(self):
        """Save page to disk"""
        frontmatter = [
            "---",
            f"title: {self.title}",
            f"created: {self.created or date.today().isoformat()}",
            f"updated: {date.today().isoformat()}",
            f"type: {self.page_type}",
            f"tags: [{', '.join(self.tags)}]",
        ]
        if self.sources:
            frontmatter.append(f"sources: [{', '.join(self.sources)}]")
        if self.confidence != "high":
            frontmatter.append(f"confidence: {self.confidence}")
        if self.contested:
            frontmatter.append("contested: true")
        if self.contradictions:
            frontmatter.append(f"contradictions: [{', '.join(self.contradictions)}]")

        frontmatter.append("---\n")
        content = "\n".join(frontmatter) + self.body
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(content, encoding="utf-8")

    def to_dict(self) -> dict:
        return {
            "path": str(self.path),
            "title": self.title,
            "type": self.page_type,
            "created": self.created,
            "updated": self.updated,
            "tags": self.tags,
            "sources": self.sources,
            "confidence": self.confidence,
            "contested": self.contested,
            "wikilinks": self.wikilinks,
        }


# ── Wiki Engine ─────────────────────────────────────

class WikiEngine:
    """Core wiki operations"""

    def __init__(self, wiki_path: Path = None):
        self.wiki_path = wiki_path or WIKI_PATH
        self._ensure_dirs()

    def _ensure_dirs(self):
        for d in [RAW_DIR, ENTITIES_DIR, CONCEPTS_DIR, COMPARISONS_DIR,
                  QUERIES_DIR, ARCHIVE_DIR]:
            d.mkdir(parents=True, exist_ok=True)

    # ── Status ──────────────────────────────────────

    def status(self) -> dict:
        stats = {
            "wiki_path": str(self.wiki_path),
            "total_pages": 0,
            "entities": 0,
            "concepts": 0,
            "comparisons": 0,
            "queries": 0,
            "raw_sources": 0,
            "orphan_pages": 0,
            "contested_pages": 0,
            "stale_pages": 0,
        }

        for d, key in [(ENTITIES_DIR, "entities"), (CONCEPTS_DIR, "concepts"),
                        (COMPARISONS_DIR, "comparisons"), (QUERIES_DIR, "queries")]:
            pages = list(d.glob("*.md"))
            stats[key] = len(pages)
            stats["total_pages"] += len(pages)

        stats["raw_sources"] = sum(1 for _ in RAW_DIR.rglob("*.md"))

        # Orphans
        all_pages = self._all_pages()
        linked = set()
        for p in all_pages:
            pg = WikiPage.parse(p)
            linked.update(pg.wikilinks)
        for p in all_pages:
            slug = p.stem
            if slug not in linked and not any(slug in l for l in linked):
                stats["orphan_pages"] += 1

        # Contested
        for p in all_pages:
            pg = WikiPage.parse(p)
            if pg.contested:
                stats["contested_pages"] += 1

        # Stale (>90 days)
        cutoff = date.today().toordinal() - 90
        for p in all_pages:
            pg = WikiPage.parse(p)
            if pg.updated:
                try:
                    d = date.fromisoformat(pg.updated)
                    if d.toordinal() < cutoff:
                        stats["stale_pages"] += 1
                except ValueError:
                    pass

        return stats

    # ── Search ──────────────────────────────────────

    def search(self, term: str, page_type: str = None) -> list:
        """Search wiki pages by content"""
        results = []
        term_lower = term.lower()

        for page_path in self._all_pages():
            if page_type and not str(page_path).startswith(str(self._type_dir(page_type))):
                continue
            try:
                content = page_path.read_text(encoding="utf-8").lower()
                if term_lower in content:
                    pg = WikiPage.parse(page_path)
                    # Find context
                    lines = content.splitlines()
                    context_lines = []
                    for i, line in enumerate(lines):
                        if term_lower in line:
                            start = max(0, i - 1)
                            end = min(len(lines), i + 2)
                            context_lines.extend(lines[start:end])
                    results.append({
                        "page": pg.to_dict(),
                        "context": "\n".join(context_lines[:5]),
                    })
            except Exception:
                pass

        return results

    def _all_pages(self) -> list:
        pages = []
        for d in [ENTITIES_DIR, CONCEPTS_DIR, COMPARISONS_DIR, QUERIES_DIR]:
            pages.extend(d.glob("*.md"))
        return pages

    def _type_dir(self, page_type: str) -> Path:
        return {
            "entity": ENTITIES_DIR,
            "concept": CONCEPTS_DIR,
            "comparison": COMPARISONS_DIR,
            "query": QUERIES_DIR,
        }.get(page_type, CONCEPTS_DIR)

    # ── Ingest ──────────────────────────────────────

    def ingest_url(self, url: str, title: str = None) -> dict:
        """URL에서 콘텐츠 수집"""
        result = {"url": url, "status": "error", "files_created": []}

        try:
            # web_extract 사용 (curl fallback)
            cmd = ["python3", "-c", f"""
import sys
sys.path.insert(0, "{Path(__file__).parent}")
try:
    from hermes_tools import web_extract
    r = web_extract(["{url}"])
    print(r["results"][0]["content"])
except Exception as e:
    print("ERROR:", e, file=sys.stderr)
    sys.exit(1)
"""]
            proc = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            if proc.returncode != 0:
                # curl fallback
                proc = subprocess.run(["curl", "-sL", url], capture_output=True,
                                     text=True, timeout=30)
                content = proc.stdout
            else:
                content = proc.stdout

            if not content or len(content) < 100:
                result["error"] = "No content extracted"
                return result

            # 파일명 생성
            from urllib.parse import urlparse
            parsed = urlparse(url)
            slug = re.sub(r'[^\w\-]', '-', parsed.netloc + parsed.path)[:60].strip("-")
            if not slug:
                slug = hashlib.md5(url.encode()).hexdigest()[:12]

            date_str = date.today().isoformat()
            filename = f"{slug}-{date_str}.md"
            raw_path = RAW_DIR / "articles" / filename

            # 원본 저장
            sha = hashlib.sha256(content.encode()).hexdigest()[:16]
            frontmatter = (
                f"---\n"
                f"source_url: {url}\n"
                f"ingested: {date_str}\n"
                f"sha256: {sha}\n"
                f"---\n\n"
            )
            raw_path.parent.mkdir(parents=True, exist_ok=True)
            raw_path.write_text(frontmatter + content, encoding="utf-8")
            result["files_created"].append(str(raw_path))

            # 요약 생성 (LLM 없이 기본 추출)
            summary = self._auto_summarize(content, url)
            summary_path = CONCEPTS_DIR / f"{slug}.md"
            page = WikiPage(
                path=summary_path,
                title=title or summary.get("title", slug.replace("-", " ").title()),
                page_type="concept",
                created=date_str,
                updated=date_str,
                tags=summary.get("tags", []),
                sources=[f"raw/articles/{filename}"],
                body=summary.get("body", content[:2000]),
            )
            page.save()
            result["files_created"].append(str(summary_path))

            # 엔티티 추출
            entities = self._extract_entities(content)
            for ent_name, ent_info in entities.items():
                ent_slug = re.sub(r'[^\w\-]', '-', ent_name.lower())[:40]
                ent_path = ENTITIES_DIR / f"{ent_slug}.md"
                existing = WikiPage.parse(ent_path) if ent_path.exists() else None

                if existing:
                    existing.body += f"\n\n## From {slug}\n{ent_info.get('context', '')}"
                    existing.updated = date_str
                    existing.sources = list(set(existing.sources + [f"raw/articles/{filename}"]))
                    existing.wikilinks = list(set(existing.wikilinks + page.wikilinks))
                    existing.save()
                else:
                    ent_page = WikiPage(
                        path=ent_path,
                        title=ent_name,
                        page_type="entity",
                        created=date_str,
                        updated=date_str,
                        tags=["entity"],
                        sources=[f"raw/articles/{filename}"],
                        body=f"# {ent_name}\n\n{ent_info.get('context', 'Auto-extracted entity.')}\n\n[[{slug}]]",
                    )
                    ent_page.save()
                result["files_created"].append(str(ent_path))

            # 로그
            self._log("ingest", f"{title or slug} from {url}")

            # 인덱스 업데이트
            self._update_index()

            result["status"] = "ok"
            result["entities_found"] = len(entities)

        except Exception as e:
            result["error"] = str(e)

        return result

    def ingest_file(self, filepath: str, title: str = None) -> dict:
        """로컬 파일 수집"""
        result = {"file": filepath, "status": "error", "files_created": []}
        try:
            path = Path(filepath)
            if not path.exists():
                result["error"] = "File not found"
                return result

            content = path.read_text(encoding="utf-8")
            date_str = date.today().isoformat()
            slug = re.sub(r'[^\w\-]', '-', path.stem)[:60]
            sha = hashlib.sha256(content.encode()).hexdigest()[:16]

            filename = f"{slug}-{date_str}.md"
            raw_path = RAW_DIR / "articles" / filename

            frontmatter = (
                f"---\n"
                f"source_file: {filepath}\n"
                f"ingested: {date_str}\n"
                f"sha256: {sha}\n"
                f"---\n\n"
            )
            raw_path.write_text(frontmatter + content, encoding="utf-8")
            result["files_created"].append(str(raw_path))

            summary = self._auto_summarize(content, filepath)
            summary_path = CONCEPTS_DIR / f"{slug}.md"
            page = WikiPage(
                path=summary_path,
                title=title or summary.get("title", slug.replace("-", " ").title()),
                page_type="concept",
                created=date_str,
                updated=date_str,
                tags=summary.get("tags", []),
                sources=[f"raw/articles/{filename}"],
                body=summary.get("body", content[:2000]),
            )
            page.save()
            result["files_created"].append(str(summary_path))

            self._log("ingest", f"{title or slug} from file: {filepath}")
            self._update_index()
            result["status"] = "ok"

        except Exception as e:
            result["error"] = str(e)

        return result

    def _auto_summarize(self, content: str, source: str) -> dict:
        """기본 자동 요약 (LLM 없이)"""
        lines = content.splitlines()

        # 제목 추출
        title = ""
        for line in lines[:20]:
            line = line.strip()
            if line.startswith("# "):
                title = line[2:].strip()
                break
        if not title:
            title = source.split("/")[-1][:60] if "/" in source else source[:60]

        # 첫 번째 단락
        body_lines = []
        in_code = False
        for line in lines:
            if line.startswith("```"):
                in_code = not in_code
                continue
            if not in_code and line.strip() and not line.startswith("#"):
                body_lines.append(line)
            if len("\n".join(body_lines)) > 1500:
                break

        body = "\n".join(body_lines[:30]) if body_lines else content[:1500]

        # 태그 추출 (간단 키워드 매칭)
        tags = []
        tag_keywords = {
            "ai-ml": ["ai", "machine learning", "neural", "model", "training", "llm"],
            "programming": ["code", "python", "javascript", "api", "function", "class"],
            "research": ["paper", "study", "experiment", "results", "methodology"],
            "health": ["health", "medical", "diet", "exercise", "sleep"],
            "business": ["business", "startup", "revenue", "market", "product"],
            "science": ["science", "physics", "chemistry", "biology", "research"],
            "history": ["history", "ancient", "war", "century", "empire"],
        }
        content_lower = content.lower()
        for tag, keywords in tag_keywords.items():
            if any(kw in content_lower for kw in keywords):
                tags.append(tag)

        return {"title": title, "body": body, "tags": tags[:3]}

    def _extract_entities(self, content: str) -> dict:
        """간단한 엔티티 추출 (대문자 시작 구문)"""
        entities = {}
        # 대문자로 시작하는 2-4단어 구문 추출
        pattern = r'\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\b'
        matches = re.findall(pattern, content)

        for match in matches:
            if match not in entities and len(match) > 3:
                # 문맥 추출
                idx = content.find(match)
                start = max(0, idx - 100)
                end = min(len(content), idx + len(match) + 200)
                context = content[start:end].strip()
                entities[match] = {"context": context}

        # 상위 10개만
        return dict(list(entities.items())[:10])

    # ── Index ───────────────────────────────────────

    def _update_index(self):
        """index.md 자동 재생성"""
        sections = {
            "Entities": (ENTITIES_DIR, "entity"),
            "Concepts": (CONCEPTS_DIR, "concept"),
            "Comparisons": (COMPARISONS_DIR, "comparison"),
            "Queries": (QUERIES_DIR, "query"),
        }

        lines = [
            "# Wiki Index",
            "",
            f"> Content catalog. Last updated: {date.today().isoformat()}",
            f"> Total pages: {sum(1 for _ in self._all_pages())}",
            "",
        ]

        for section_name, (dir_path, ptype) in sections.items():
            pages = sorted(dir_path.glob("*.md"), key=lambda p: p.stem)
            lines.append(f"## {section_name}")
            lines.append("")

            if not pages:
                lines.append("<!-- Empty -->")
            else:
                for p in pages:
                    pg = WikiPage.parse(p)
                    summary = pg.body[:100].replace("\n", " ").strip()
                    if len(summary) > 100:
                        summary = summary[:97] + "..."
                    lines.append(f"- [[{p.stem}]] — {summary}")

            lines.append("")

        INDEX_FILE.write_text("\n".join(lines), encoding="utf-8")

    # ── Log ─────────────────────────────────────────

    def _log(self, action: str, subject: str):
        """로그 항목 추가"""
        date_str = date.today().isoformat()
        entry = f"\n## [{date_str}] {action} | {subject}\n"

        if LOG_FILE.exists():
            content = LOG_FILE.read_text(encoding="utf-8")
            # 로테이크 체크 (500줄)
            if content.count("\n## [") > 500:
                archive = WIKI_PATH / f"log-{date_str}.md"
                archive.write_text(content, encoding="utf-8")
                content = content[:200]  # 헤더만 유지
            LOG_FILE.write_text(content + entry, encoding="utf-8")
        else:
            LOG_FILE.write_text(f"# Wiki Log\n{entry}", encoding="utf-8")

    # ── Lint ────────────────────────────────────────

    def lint(self) -> dict:
        """위키 건강 검사"""
        report = {
            "timestamp": datetime.now().isoformat(),
            "issues": [],
            "warnings": [],
            "ok": [],
        }

        all_pages = self._all_pages()

        # 1. 고아 페이지
        all_links = set()
        for p in all_pages:
            pg = WikiPage.parse(p)
            all_links.update(pg.wikilinks)

        orphans = []
        for p in all_pages:
            slug = p.stem
            if not any(slug in link for link in all_links):
                orphans.append(slug)

        if orphans:
            report["issues"].append({
                "type": "orphan_pages",
                "severity": "warning",
                "pages": orphans,
                "message": f"{len(orphans)} pages with no inbound links",
            })
        else:
            report["ok"].append("No orphan pages")

        # 2. 깨진 위키링크
        broken = []
        for p in all_pages:
            pg = WikiPage.parse(p)
            for link in pg.wikilinks:
                link_slug = re.sub(r'[^\w\-]', '-', link.lower())
                target = None
                for d in [ENTITIES_DIR, CONCEPTS_DIR, COMPARISONS_DIR, QUERIES_DIR]:
                    candidate = d / f"{link_slug}.md"
                    if candidate.exists():
                        target = candidate
                        break
                if not target:
                    broken.append(f"{p.stem} → [[{link}]]")

        if broken:
            report["issues"].append({
                "type": "broken_links",
                "severity": "error",
                "links": broken,
                "message": f"{len(broken)} broken wikilinks",
            })

        # 3. 인덱스 누락
        indexed = set()
        if INDEX_FILE.exists():
            index_content = INDEX_FILE.read_text()
            indexed = set(re.findall(r'\[\[([\w\- ]+)\]\]', index_content))

        missing_from_index = []
        for p in all_pages:
            if p.stem not in indexed:
                missing_from_index.append(p.stem)

        if missing_from_index:
            report["issues"].append({
                "type": "missing_from_index",
                "severity": "warning",
                "pages": missing_from_index,
                "message": f"{len(missing_from_index)} pages not in index.md",
            })

        # 4. 모순 페이지
        contested = []
        for p in all_pages:
            pg = WikiPage.parse(p)
            if pg.contested:
                contested.append({"page": p.stem, "contradictions": pg.contradictions})

        if contested:
            report["issues"].append({
                "type": "contested_pages",
                "severity": "warning",
                "pages": contested,
                "message": f"{len(contested)} pages marked as contested",
            })

        # 5. 오래된 콘텐츠
        cutoff = date.today().toordinal() - 90
        stale = []
        for p in all_pages:
            pg = WikiPage.parse(p)
            if pg.updated:
                try:
                    d = date.fromisoformat(pg.updated)
                    if d.toordinal() < cutoff:
                        stale.append({"page": p.stem, "updated": pg.updated})
                except ValueError:
                    pass

        if stale:
            report["warnings"].append({
                "type": "stale_content",
                "pages": stale,
                "message": f"{len(stale)} pages not updated in 90+ days",
            })

        # 6. 프론트매터 검증
        missing_fm = []
        for p in all_pages:
            content = p.read_text(encoding="utf-8")
            if not content.startswith("---"):
                missing_fm.append(p.stem)

        if missing_fm:
            report["issues"].append({
                "type": "missing_frontmatter",
                "severity": "error",
                "pages": missing_fm,
                "message": f"{len(missing_fm)} pages missing frontmatter",
            })

        # 7. 페이지 크기
        oversized = []
        for p in all_pages:
            lines = p.read_text(encoding="utf-8").splitlines()
            if len(lines) > 200:
                oversized.append({"page": p.stem, "lines": len(lines)})

        if oversized:
            report["warnings"].append({
                "type": "oversized_pages",
                "pages": oversized,
                "message": f"{len(oversized)} pages exceed 200 lines",
            })

        # 로그
        total_issues = len(report["issues"]) + len(report["warnings"])
        self._log("lint", f"{total_issues} issues found")

        return report


# ── CLI ─────────────────────────────────────────────

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="LLM Wiki — Personal Knowledge Base CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s status                    # Wiki status
  %(prog)s ingest https://example.com/article
  %(prog)s ingest ./my-notes.md --title "My Notes"
  %(prog)s search "transformer"
  %(prog)s query "What do I know about AI?"
  %(prog)s lint                      # Health check
  %(prog)s index                     # Rebuild index
  %(prog)s list [--type entity]      # List pages
        """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Command")

    # status
    subparsers.add_parser("status", help="Show wiki status")

    # ingest
    ingest_p = subparsers.add_parser("ingest", help="Ingest a source")
    ingest_p.add_argument("source", help="URL or file path")
    ingest_p.add_argument("--title", "-t", default=None, help="Page title")

    # search
    search_p = subparsers.add_parser("search", help="Search wiki")
    search_p.add_argument("term", help="Search term")
    search_p.add_argument("--type", default=None, help="Filter by type")

    # query
    query_p = subparsers.add_parser("query", help="Query the wiki")
    query_p.add_argument("question", help="Question to answer")

    # lint
    subparsers.add_parser("lint", help="Health check")

    # index
    subparsers.add_parser("index", help="Rebuild index")

    # list
    list_p = subparsers.add_parser("list", help="List pages")
    list_p.add_argument("--type", default=None, help="Filter by type")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    engine = WikiEngine()

    if args.command == "status":
        stats = engine.status()
        print(f"\n📚 LLM Wiki Status")
        print(f"   Path: {stats['wiki_path']}")
        print(f"   Total pages: {stats['total_pages']}")
        print(f"   Entities: {stats['entities']}")
        print(f"   Concepts: {stats['concepts']}")
        print(f"   Comparisons: {stats['comparisons']}")
        print(f"   Queries: {stats['queries']}")
        print(f"   Raw sources: {stats['raw_sources']}")
        if stats['orphan_pages']:
            print(f"   ⚠ Orphan pages: {stats['orphan_pages']}")
        if stats['contested_pages']:
            print(f"   ⚠ Contested: {stats['contested_pages']}")
        if stats['stale_pages']:
            print(f"   ⚠ Stale: {stats['stale_pages']}")

    elif args.command == "ingest":
        source = args.source
        if source.startswith("http://") or source.startswith("https://"):
            result = engine.ingest_url(source, args.title)
        else:
            result = engine.ingest_file(source, args.title)

        if result["status"] == "ok":
            print(f"\n✅ Ingested: {source}")
            for f in result.get("files_created", []):
                print(f"   📄 {f}")
            if "entities_found" in result:
                print(f"   🏷 Entities found: {result['entities_found']}")
        else:
            print(f"\n❌ Error: {result.get('error', 'Unknown')}")

    elif args.command == "search":
        results = engine.search(args.term, args.type)
        print(f"\n🔍 Search: '{args.term}' — {len(results)} results")
        for r in results:
            pg = r["page"]
            print(f"\n  📄 {pg['title']} ({pg['type']})")
            print(f"     {r['context'][:120]}...")

    elif args.command == "query":
        # 검색 기반 답변
        results = engine.search(args.question)
        print(f"\n💬 Query: {args.question}")
        if results:
            print(f"\n  Found {len(results)} relevant pages:")
            for r in results[:5]:
                pg = r["page"]
                print(f"  - [[{pg['path'].split('/')[-1].replace('.md', '')}]] {pg['title']}")
            print(f"\n  Read relevant pages for detailed answers.")
        else:
            print("  No relevant pages found. Try ingesting more sources.")

    elif args.command == "lint":
        report = engine.lint()
        print(f"\n🔧 Wiki Lint Report — {report['timestamp']}")

        if report["issues"]:
            print(f"\n  ❌ Issues ({len(report['issues'])}):")
            for issue in report["issues"]:
                print(f"    [{issue['severity'].upper()}] {issue['message']}")
                if "pages" in issue and isinstance(issue["pages"], list):
                    for p in issue["pages"][:5]:
                        if isinstance(p, str):
                            print(f"      - {p}")
                        elif isinstance(p, dict):
                            print(f"      - {p.get('page', p)}")

        if report["warnings"]:
            print(f"\n  ⚠ Warnings ({len(report['warnings'])}):")
            for w in report["warnings"]:
                print(f"    {w['message']}")

        if report["ok"]:
            print(f"\n  ✅ OK: {', '.join(report['ok'])}")

        total = len(report["issues"]) + len(report["warnings"])
        if total == 0:
            print("\n  🎉 Wiki is healthy!")

    elif args.command == "index":
        engine._update_index()
        print("✅ Index rebuilt")

    elif args.command == "list":
        pages = engine._all_pages()
        if args.type:
            pages = [p for p in pages if args.type in str(p)]
        print(f"\n📄 Pages ({len(pages)}):")
        for p in sorted(pages):
            pg = WikiPage.parse(p)
            print(f"  [{pg.page_type:10s}] {pg.title:40s} {p.stem}")


if __name__ == "__main__":
    main()
