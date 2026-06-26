#!/usr/bin/env python3
"""
Weekly Wiki Cleanup Script
매주 토요일 실행: 중복 탐지, 고아 페이지, 그래프 리포트
"""
import re
import json
from pathlib import Path
from datetime import date, timedelta
from collections import Counter

WIKI_PATH = Path.home() / "wiki"
ENTITIES_DIR = WIKI_PATH / "entities"
CONCEPTS_DIR = WIKI_PATH / "concepts"
COMPARISONS_DIR = WIKI_PATH / "comparisons"
QUERIES_DIR = WIKI_PATH / "queries"
RAW_DIR = WIKI_PATH / "raw"
LOG_FILE = WIKI_PATH / "log.md"
REPORT_DIR = WIKI_PATH / "_reports"
REPORT_DIR.mkdir(exist_ok=True)


def scan_pages():
    """모든 위키 페이지 스캔"""
    pages = {}
    for d, ptype in [
        (ENTITIES_DIR, "entity"),
        (CONCEPTS_DIR, "concept"),
        (COMPARISONS_DIR, "comparison"),
        (QUERIES_DIR, "query"),
    ]:
        for f in d.glob("*.md"):
            content = f.read_text(encoding="utf-8")
            # Frontmatter 파싱
            fm = {}
            fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
            if fm_match:
                for line in fm_match.group(1).splitlines():
                    line = line.strip()
                    if line.startswith("title:"):
                        fm["title"] = line.split(":", 1)[1].strip().strip('"')
                    elif line.startswith("tags:"):
                        fm["tags"] = [t.strip() for t in re.findall(r'[\w-]+', line.split(":", 1)[1])]
                    elif line.startswith("updated:"):
                        fm["updated"] = line.split(":", 1)[1].strip()
                    elif line.startswith("created:"):
                        fm["created"] = line.split(":", 1)[1].strip()

            wikilinks = re.findall(r'\[\[([\w\- ]+)\]\]', content)

            pages[f.stem] = {
                "path": str(f),
                "type": ptype,
                "title": fm.get("title", f.stem),
                "tags": fm.get("tags", []),
                "updated": fm.get("updated", ""),
                "created": fm.get("created", ""),
                "wikilinks": wikilinks,
                "content_preview": content[fm_match.end():][:200] if fm_match else content[:200],
            }
    return pages


def detect_orphans(pages: dict) -> list:
    """고아 페이지 (아무도 링크하지 않는 페이지)"""
    all_targets = set()
    for p in pages.values():
        for link in p["wikilinks"]:
            slug = re.sub(r"[^\w\-]", "-", link.lower().strip())
            all_targets.add(slug)

    orphans = []
    for slug, p in pages.items():
        if slug not in all_targets:
            orphans.append(p)
    return orphans


def detect_duplicates(pages: dict) -> list:
    """중복 후보 탐지 (제목 유사도)"""
    dupes = []
    page_list = list(pages.values())

    for i in range(len(page_list)):
        for j in range(i + 1, len(page_list)):
            p1 = page_list[i]
            p2 = page_list[j]

            # 제목 정규화 후 비교
            t1 = re.sub(r"[^\w]", "", p1["title"].lower())
            t2 = re.sub(r"[^\w]", "", p2["title"].lower())

            # 편집 거리 기반 (간단: 공통 부분 문자열 비율)
            if len(t1) > 5 and len(t2) > 5:
                common = len(set(t1) & set(t2))
                total = max(len(set(t1)), len(set(t2)))
                similarity = common / total if total > 0 else 0

                if similarity > 0.7:
                    dupes.append({
                        "page1": p1["title"],
                        "page2": p2["title"],
                        "similarity": round(similarity, 2),
                        "action": "review" if similarity > 0.9 else "monitor",
                    })

    return dupes


def generate_graph_stats(pages: dict) -> dict:
    """그래프 통계"""
    stats = {
        "total_nodes": len(pages),
        "total_edges": 0,
        "avg_connections": 0,
        "top_connected": [],
        "isolated_nodes": 0,
        "tag_distribution": Counter(),
    }

    connection_counts = {}
    for slug, p in pages.items():
        outgoing = len(p["wikilinks"])
        stats["total_edges"] += outgoing
        connection_counts[slug] = {"out": outgoing, "in": 0}
        for tag in p["tags"]:
            stats["tag_distribution"][tag] += 1

    for slug, p in pages.items():
        for link in p["wikilinks"]:
            link_slug = re.sub(r"[^\w\-]", "-", link.lower().strip())
            if link_slug in connection_counts:
                connection_counts[link_slug]["in"] += 1

    if pages:
        stats["avg_connections"] = round(stats["total_edges"] / len(pages), 1)

    # Top connected
    sorted_pages = sorted(
        connection_counts.items(),
        key=lambda x: x[1]["in"] + x[1]["out"],
        reverse=True,
    )
    stats["top_connected"] = [
        {"slug": slug, "in": c["in"], "out": c["out"], "total": c["in"] + c["out"]}
        for slug, c in sorted_pages[:10]
    ]

    stats["isolated_nodes"] = sum(
        1 for c in connection_counts.values() if c["in"] == 0 and c["out"] == 0
    )

    return stats


def generate_report(pages: dict, orphans: list, dupes: dict, graph: dict):
    """마크다운 리포트 생성"""
    today = date.today().isoformat()
    report_path = REPORT_DIR / f"weekly_report_{today}.md"

    lines = [
        f"# Wiki Weekly Report — {today}",
        "",
        f"> Auto-generated cleanup report.",
        "",
        "## 📊 Graph Stats",
        "",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Total pages | {graph['total_nodes']} |",
        f"| Total links | {graph['total_edges']} |",
        f"| Avg connections | {graph['avg_connections']} |",
        f"| Isolated nodes | {graph['isolated_nodes']} |",
        "",
        "### Top Connected Pages",
        "",
        "| Page | In | Out | Total |",
        "|------|----|-----|-------|",
    ]
    for p in graph["top_connected"]:
        lines.append(f"| {p['slug']} | {p['in']} | {p['out']} | {p['total']} |")

    lines.extend([
        "",
        "### Tag Distribution",
        "",
        "| Tag | Count |",
        "|-----|-------|",
    ])
    for tag, count in graph["tag_distribution"].most_common(15):
        lines.append(f"| {tag} | {count} |")

    lines.extend([
        "",
        "## 🏝️ Orphan Pages",
        f"",
        f"Pages with no inbound links: **{len(orphans)}**",
        "",
    ])
    for o in orphans[:20]:
        lines.append(f"- [{o['title']}]({o['path']}) `{o['type']}`")

    lines.extend([
        "",
        "## 🔁 Duplicate Candidates",
        "",
        f"Potential duplicates: **{len(dupes)}**",
        "",
    ])
    for d in dupes:
        lines.append(f"- `{d['page1']}` ↔ `{d['page2']}` (similarity: {d['similarity']}, {d['action']})")

    lines.extend([
        "",
        "## 📅 Recent Activity",
        "",
    ])

    # 최근 7일 활동
    cutoff = date.today() - timedelta(days=7)
    recent = []
    for slug, p in pages.items():
        if p.get("updated"):
            try:
                d = date.fromisoformat(p["updated"])
                if d >= cutoff:
                    recent.append(p)
            except ValueError:
                pass
    recent.sort(key=lambda x: x.get("updated", ""), reverse=True)
    lines.append(f"Updated in last 7 days: **{len(recent)}**")
    for p in recent[:20]:
        lines.append(f"- {p['updated']} — **{p['title']}** `{p['type']}`")

    lines.append("")
    report_content = "\n".join(lines)
    report_path.write_text(report_content, encoding="utf-8")

    return report_path


def main():
    print(f"🧹 Weekly Wiki Cleanup — {date.today().isoformat()}")
    print()

    pages = scan_pages()
    print(f"  Scanned {len(pages)} pages")

    orphans = detect_orphans(pages)
    print(f"  Orphans: {len(orphans)}")

    dupes = detect_duplicates(pages)
    print(f"  Duplicates: {len(dupes)}")

    graph = generate_graph_stats(pages)
    print(f"  Graph: {graph['total_nodes']} nodes, {graph['total_edges']} edges")
    print(f"  Avg connections: {graph['avg_connections']}")
    print(f"  Isolated: {graph['isolated_nodes']}")

    report_path = generate_report(pages, orphans, dupes, graph)
    print(f"\n  📄 Report: {report_path}")

    print("\n✅ Weekly cleanup complete!")
    print(f"\n📊 Summary:")
    print(f"  Total pages: {graph['total_nodes']}")
    print(f"  Total links: {graph['total_edges']}")
    print(f"  Orphans: {len(orphans)}")
    print(f"  Duplicates: {len(dupes)}")
    print(f"  Isolated: {graph['isolated_nodes']}")


if __name__ == "__main__":
    main()
