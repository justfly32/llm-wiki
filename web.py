#!/usr/bin/env python3
"""
LLM Wiki Web UI — Obsidian-style web interface + RAG Query + LLM Summary + Related Pages
FastAPI server with markdown rendering, graph view, search, tags, AI chat, recommendations
"""
import os, re, json, hashlib, subprocess, sys
from pathlib import Path
from datetime import date, datetime
from typing import Optional

from fastapi import FastAPI, Request, Form, Query
from fastapi.responses import HTMLResponse, JSONResponse
import markdown
from markdown.extensions import toc, codehilite, tables, fenced_code

# Import RAG engine
sys.path.insert(0, str(Path(__file__).parent / "scripts"))
try:
    from wiki_rag import query_wiki, summarize_content, get_related_pages, search_relevant_pages
    RAG_AVAILABLE = True
except ImportError:
    RAG_AVAILABLE = False

# ── Config ──────────────────────────────────────────

WIKI_PATH = Path(os.environ.get("WIKI_PATH", Path.home() / "wiki"))
RAW_DIR = WIKI_PATH / "raw"
ENTITIES_DIR = WIKI_PATH / "entities"
CONCEPTS_DIR = WIKI_PATH / "concepts"
COMPARISONS_DIR = WIKI_PATH / "comparisons"
QUERIES_DIR = WIKI_PATH / "queries"
# New category folders inside concepts/
PROJECTS_DIR = CONCEPTS_DIR / "projects"
KNOWLEDGE_DIR = CONCEPTS_DIR / "knowledge"
LEARNINGS_DIR = CONCEPTS_DIR / "learnings"
DAILY_DIR = CONCEPTS_DIR / "daily"

CONCEPT_SUBDIRS = [CONCEPTS_DIR / d for d in ["daily", "knowledge", "learnings", "projects"] if (CONCEPTS_DIR / d).exists()]
ALL_DIRS = [ENTITIES_DIR, COMPARISONS_DIR, QUERIES_DIR] + CONCEPT_SUBDIRS

# Category display names
CATEGORY_LABELS = {
    "projects": "📁 Projects",
    "knowledge": "📚 Knowledge",
    "learnings": "💡 Learnings",
    "daily": "📅 Daily",
    "entity": "🏷️ Entities",
    "concept": "📄 Concepts",
    "comparison": "⚖️ Comparisons",
    "query": "❓ Queries",
}

# ── Markdown setup ──────────────────────────────────

def render_markdown(text: str) -> str:
    extensions = ['toc', 'tables', 'fenced_code', 'codehilite', 'md_in_html', 'attr_list', 'def_list']
    extension_configs = {'codehilite': {'css_class': 'highlight', 'linenums': False}}
    try:
        md = markdown.Markdown(extensions=extensions, extension_configs=extension_configs)
        html = md.convert(text)
        # Post-process: wikilinks → clickable spans
        def _wikilink_replacer(m):
            slug = re.sub(r"[^\w\-]", "-", m.group(1).lower())
            return f'<span class="wikilink" data-slug="{slug}">{m.group(1)}</span>'
        html = re.sub(r'\[\[([\w\- ]+)\]\]', _wikilink_replacer, html)
        return html
    except Exception:
        return f"<pre>{text}</pre>"

# ── Page parsing ────────────────────────────────────

def parse_page(path: Path) -> dict:
    result = {
        "path": str(path), "slug": path.stem,
        "title": path.stem.replace("-", " ").title(),
        "page_type": "concept",
        "created": "", "updated": "",
        "tags": [], "sources": [],
        "confidence": "high", "contested": False,
        "contradictions": [],
        "body": "", "html": "", "wikilinks": [],
    }
    if not path.exists():
        return result

    content = path.read_text(encoding="utf-8")
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if m:
        body_start = m.end()
        for line in m.group(1).splitlines():
            line = line.strip()
            if ':' not in line:
                continue
            key, _, val = line.partition(':')
            key = key.strip()
            val = val.strip()
            if key == 'title': result['title'] = val.strip('"').strip("'")
            elif key == 'type': result['page_type'] = val
            elif key == 'created': result['created'] = val
            elif key == 'updated': result['updated'] = val
            elif key == 'tags': result['tags'] = [t.strip() for t in re.findall(r'[\w-]+', val)]
            elif key == 'sources': result['sources'] = [s.strip() for s in re.findall(r'[\w./\-]+', val)]
            elif key == 'confidence': result['confidence'] = val
            elif key == 'contested': result['contested'] = val.lower() == 'true'
            elif key == 'contradictions': result['contradictions'] = [c.strip() for c in re.findall(r'[\w\-]+', val)]
        body = content[body_start:]
    else:
        body = content

    result['body'] = body
    result['html'] = render_markdown(body)
    result['wikilinks'] = re.findall(r'\[\[([\w\- ]+)\]\]', content)
    return result

def get_all_pages() -> list:
    pages = []
    type_map = {
        ENTITIES_DIR: "entity",
        COMPARISONS_DIR: "comparison",
        QUERIES_DIR: "query",
    }
    for cd in CONCEPT_SUBDIRS:
        type_map[cd] = cd.name  # daily, knowledge, learnings, projects
    for d, ptype in type_map.items():
        if not d.exists():
            continue
        for f in sorted(d.glob("*.md")):
            pg = parse_page(f)
            pg['page_type'] = ptype
            pages.append(pg)
    return pages

def get_backlinks(slug: str) -> list:
    backlinks = []
    for d in ALL_DIRS:
        for f in d.glob("*.md"):
            content = f.read_text(encoding="utf-8")
            if f"[[{slug}]]" in content or f"[[{slug.replace('-', ' ')}]]" in content:
                pg = parse_page(f)
                backlinks.append({"slug": f.stem, "title": pg["title"], "type": pg["page_type"]})
    return backlinks

def get_graph_data() -> dict:
    nodes, links, seen = [], [], set()
    type_map = {
        ENTITIES_DIR: "entity",
        PROJECTS_DIR: "project",
        KNOWLEDGE_DIR: "knowledge",
        LEARNINGS_DIR: "learning",
        DAILY_DIR: "daily",
        COMPARISONS_DIR: "comparison",
        QUERIES_DIR: "query",
    }
    for d, ptype in type_map.items():
        if not d.exists():
            continue
        for f in d.glob("*.md"):
            pg = parse_page(f)
            slug = f.stem
            if slug not in seen:
                nodes.append({"id": slug, "title": pg["title"], "type": ptype, "tags": pg["tags"], "group": ptype})
                seen.add(slug)
            for link in pg["wikilinks"]:
                link_slug = re.sub(r'[^\w\-]', '-', link.lower())
                links.append({"source": slug, "target": link_slug})
    return {"nodes": nodes, "links": links}

def search_pages(term: str) -> list:
    results = []
    term_lower = term.lower()
    for d in ALL_DIRS:
        for f in d.glob("*.md"):
            content = f.read_text(encoding="utf-8").lower()
            if term_lower in content:
                pg = parse_page(f)
                lines = content.splitlines()
                ctx = []
                for i, line in enumerate(lines):
                    if term_lower in line:
                        ctx.append(lines[max(0, i-1):i+2])
                results.append({
                    "slug": f.stem, "title": pg["title"], "type": pg["page_type"],
                    "context": " ... ".join([" ".join(c) for c in ctx[:3]])[:200],
                })
    return results

def get_tags() -> dict:
    tags = {}
    for d in ALL_DIRS:
        for f in d.glob("*.md"):
            pg = parse_page(f)
            for tag in pg.get("tags", []):
                tags[tag] = tags.get(tag, 0) + 1
    return tags

# ── App ─────────────────────────────────────────────

app = FastAPI(title="LLM Wiki", version="0.2.0")

# ── Routes ──────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def home():
    return HTMLResponse(content=get_index_html())

@app.get("/api/pages")
async def api_pages():
    return JSONResponse(get_all_pages())

@app.get("/api/page/{slug}")
async def api_page(slug: str):
    for d in ALL_DIRS:
        p = d / f"{slug}.md"
        if p.exists():
            pg = parse_page(p)
            pg["backlinks"] = get_backlinks(slug)
            # Add related pages
            if RAG_AVAILABLE:
                try:
                    pg["related"] = get_related_pages(slug, top_k=5)
                except Exception:
                    pg["related"] = []
            return JSONResponse(pg)
    return JSONResponse({"error": "Not found"}, status_code=404)

@app.get("/api/graph")
async def api_graph():
    return JSONResponse(get_graph_data())

@app.get("/api/search")
async def api_search(q: str = Query(..., min_length=1)):
    return JSONResponse(search_pages(q))

@app.get("/api/tags")
async def api_tags():
    return JSONResponse(get_tags())

@app.get("/api/backlinks/{slug}")
async def api_backlinks(slug: str):
    return JSONResponse(get_backlinks(slug))

@app.get("/api/categories")
async def api_categories():
    cats = {}
    type_map = {
        "entity": ENTITIES_DIR,
        "project": PROJECTS_DIR,
        "knowledge": KNOWLEDGE_DIR,
        "learning": LEARNINGS_DIR,
        "daily": DAILY_DIR,
        "comparison": COMPARISONS_DIR,
        "query": QUERIES_DIR,
    }
    for ptype, d in type_map.items():
        if d.exists():
            files = sorted(d.glob("*.md"))
            cats[ptype] = [{"slug": f.stem, "title": f.stem.replace("-", " ").title()} for f in files]
    return JSONResponse(cats)

@app.post("/api/page/{slug}")
async def api_save_page(slug: str, request: Request):
    data = await request.json()
    body = data.get("body", "")
    page_type = data.get("type", "concept")
    title = data.get("title", slug.replace("-", " ").title())
    tags = data.get("tags", [])
    type_dir = {"entity": ENTITIES_DIR, "concept": CONCEPTS_DIR, "comparison": COMPARISONS_DIR, "query": QUERIES_DIR}
    d = type_dir.get(page_type, CONCEPTS_DIR)
    path = d / f"{slug}.md"
    today = date.today().isoformat()
    fm = ["---", f"title: {title}", f"created: {today}", f"updated: {today}", f"type: {page_type}", f"tags: [{', '.join(tags)}]", "---", ""]
    content = "\n".join(fm) + body
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return JSONResponse({"status": "saved", "slug": slug})

@app.post("/api/ingest")
async def api_ingest(request: Request):
    data = await request.json()
    url = data.get("url", "")
    title = data.get("title", "")
    if not url:
        return JSONResponse({"error": "URL required"}, status_code=400)
    wiki_py = WIKI_PATH / "wiki.py"
    if wiki_py.exists():
        cmd = [sys.executable, str(wiki_py), "ingest", url] + (["--title", title] if title else [])
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        return JSONResponse({
            "status": "ok" if result.returncode == 0 else "error",
            "output": result.stdout[-500:],
            "error": result.stderr[-500:] if result.stderr else "",
        })
    return JSONResponse({"error": "wiki.py not found"}, status_code=500)

@app.get("/api/lint")
async def api_lint():
    wiki_py = WIKI_PATH / "wiki.py"
    if wiki_py.exists():
        result = subprocess.run([sys.executable, str(wiki_py), "lint"], capture_output=True, text=True, timeout=30)
        return JSONResponse({"output": result.stdout})
    return JSONResponse({"error": "wiki.py not found"})

# ── NEW: RAG Query API ──────────────────────────────

@app.post("/api/query")
async def api_query(request: Request):
    """RAG 질의응답 API"""
    if not RAG_AVAILABLE:
        return JSONResponse({"error": "RAG engine not available. Install wiki_rag.py dependencies."}, status_code=503)

    data = await request.json()
    question = data.get("question", "").strip()
    if not question:
        return JSONResponse({"error": "Question required"}, status_code=400)

    try:
        result = query_wiki(question)
        return JSONResponse(result)
    except Exception as e:
        return JSONResponse({"error": str(e), "status": "error"}, status_code=500)

# ── NEW: LLM Summarize API ──────────────────────────

@app.post("/api/summarize")
async def api_summarize(request: Request):
    """LLM 기반 콘텐츠 요약 API"""
    if not RAG_AVAILABLE:
        return JSONResponse({"error": "RAG engine not available."}, status_code=503)

    data = await request.json()
    content = data.get("content", "").strip()
    title = data.get("title", "")
    if not content:
        return JSONResponse({"error": "Content required"}, status_code=400)

    try:
        result = summarize_content(content, title)
        return JSONResponse(result)
    except Exception as e:
        return JSONResponse({"error": str(e), "status": "error"}, status_code=500)

# ── NEW: Related Pages API ──────────────────────────

@app.get("/api/related/{slug}")
async def api_related(slug: str):
    """연관 페이지 추천 API"""
    if not RAG_AVAILABLE:
        return JSONResponse({"error": "RAG engine not available."}, status_code=503)

    try:
        related = get_related_pages(slug, top_k=5)
        return JSONResponse({"related": related})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

# ── Main HTML (Obsidian-style SPA) ─────────────────

def get_index_html() -> str:
    return r"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>LLM Wiki</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
<script src="https://d3js.org/d3.v7.min.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#0d1117;--bg-secondary:#161b22;--bg-tertiary:#21262d;
  --border:#30363d;--text:#c9d1d9;--text-muted:#8b949e;
  --accent:#58a6ff;--green:#3fb950;--red:#f85149;--yellow:#d29922;--purple:#a371f7;
  --sidebar-w:280px;--right-w:280px;--header-h:48px;
}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--text);height:100vh;overflow:hidden;font-size:14px;line-height:1.6}

/* Header */
.header{background:var(--bg-secondary);border-bottom:1px solid var(--border);height:var(--header-h);display:flex;align-items:center;padding:0 16px;gap:12px;flex-shrink:0}
.header .logo{font-weight:700;color:var(--accent);font-size:16px;cursor:pointer}
.header .search-box{flex:1;max-width:400px;position:relative}
.header .search-box input{width:100%;padding:6px 12px 6px 32px;background:var(--bg);border:1px solid var(--border);border-radius:6px;color:var(--text);font-size:13px}
.header .search-box input:focus{outline:none;border-color:var(--accent)}
.header .search-box::before{content:"🔍";position:absolute;left:10px;top:50%;transform:translateY(-50%);font-size:12px}
.header .actions{display:flex;gap:8px}
.header .btn{padding:6px 12px;background:var(--bg-tertiary);border:1px solid var(--border);border-radius:6px;color:var(--text);cursor:pointer;font-size:12px}
.header .btn:hover{background:var(--border)}
.header .btn.primary{background:var(--green);color:#fff;border-color:var(--green)}
.header .btn.ai{background:var(--purple);color:#fff;border-color:var(--purple)}

/* Layout */
.layout{display:flex;height:calc(100vh - var(--header-h))}

/* Sidebar */
.sidebar{width:var(--sidebar-w);background:var(--bg-secondary);border-right:1px solid var(--border);overflow-y:auto;flex-shrink:0;display:flex;flex-direction:column}
.sidebar-section{border-bottom:1px solid var(--border)}
.sidebar-section-title{padding:10px 16px;font-size:11px;font-weight:600;text-transform:uppercase;color:var(--text-muted);cursor:pointer;display:flex;justify-content:space-between;align-items:center}
.sidebar-section-title:hover{color:var(--text)}
.sidebar-section-title .count{background:var(--bg-tertiary);padding:1px 6px;border-radius:10px;font-size:10px}
.sidebar-section-content{display:none}
.sidebar-section-content.open{display:block}
.sidebar-item{padding:6px 16px 6px 24px;cursor:pointer;display:flex;align-items:center;gap:8px;font-size:13px;color:var(--text-muted)}
.sidebar-item:hover{background:var(--bg-tertiary);color:var(--text)}
.sidebar-item.active{background:var(--bg-tertiary);color:var(--accent)}
.sidebar-item .icon{font-size:14px}
.sidebar-item .tag-dot{width:8px;height:8px;border-radius:50%;flex-shrink:0}
.tag-entity{background:var(--accent)}.tag-concept{background:var(--green)}.tag-comparison{background:var(--yellow)}.tag-query{background:var(--purple)}

/* Tag cloud */
.tag-cloud{padding:8px 16px;display:flex;flex-wrap:wrap;gap:4px}
.tag-chip{padding:2px 8px;background:var(--bg-tertiary);border-radius:10px;font-size:11px;color:var(--text-muted);cursor:pointer}
.tag-chip:hover{background:var(--border);color:var(--text)}

/* Main content */
.main{flex:1;display:flex;overflow:hidden}
.content{flex:1;overflow-y:auto;padding:24px 32px}
.content-inner{max-width:800px;margin:0 auto}

/* Page header */
.page-header{margin-bottom:24px;padding-bottom:16px;border-bottom:1px solid var(--border)}
.page-header h1{font-size:28px;font-weight:700;margin-bottom:8px}
.page-meta{display:flex;gap:12px;flex-wrap:wrap;align-items:center;font-size:12px;color:var(--text-muted)}
.page-meta .tag{padding:2px 8px;background:var(--bg-tertiary);border-radius:10px;color:var(--accent)}
.page-meta .badge{padding:2px 8px;border-radius:4px;font-size:11px;font-weight:600}
.badge.entity{background:var(--accent);color:#fff}
.badge.project{background:var(--accent);color:#fff}
.badge.knowledge{background:var(--green);color:#fff}
.badge.learning{background:var(--green);color:#fff}
.badge.daily{background:var(--yellow);color:#000}
.badge.concept{background:var(--green);color:#fff}
.badge.comparison{background:var(--yellow);color:#000}
.badge.query{background:var(--purple);color:#fff}
.badge.contested{background:var(--red);color:#fff}

/* Markdown content */
.markdown-body h1,.markdown-body h2,.markdown-body h3{margin:24px 0 12px;font-weight:600}
.markdown-body h1{font-size:22px;border-bottom:1px solid var(--border);padding-bottom:8px}
.markdown-body h2{font-size:18px}
.markdown-body h3{font-size:16px}
.markdown-body p{margin:12px 0}
.markdown-body ul,.markdown-body ol{margin:12px 0;padding-left:24px}
.markdown-body li{margin:4px 0}
.markdown-body a{color:var(--accent);text-decoration:none}
.markdown-body a:hover{text-decoration:underline}
.markdown-body code{background:var(--bg-tertiary);padding:2px 6px;border-radius:4px;font-family:'Fira Code',monospace;font-size:13px}
.markdown-body pre{background:var(--bg-secondary);border:1px solid var(--border);border-radius:8px;padding:16px;overflow-x:auto;margin:16px 0}
.markdown-body pre code{background:none;padding:0;font-size:13px}
.markdown-body blockquote{border-left:3px solid var(--accent);padding:8px 16px;margin:16px 0;background:var(--bg-secondary);border-radius:0 4px 4px 0;color:var(--text-muted)}
.markdown-body table{border-collapse:collapse;width:100%;margin:16px 0}
.markdown-body th,.markdown-body td{border:1px solid var(--border);padding:8px 12px;text-align:left}
.markdown-body th{background:var(--bg-secondary);font-weight:600}
.markdown-body hr{border:none;border-top:1px solid var(--border);margin:24px 0}
.markdown-body img{max-width:100%;border-radius:8px}

/* Wikilink */
.wikilink{color:var(--accent);cursor:pointer;text-decoration:none;border-bottom:1px dashed var(--accent)}
.wikilink:hover{background:var(--accent);color:#fff;border-radius:2px}
.wikilink.broken{color:var(--red);border-bottom-color:var(--red);opacity:0.7}

/* Right panel */
.right-panel{width:var(--right-w);background:var(--bg-secondary);border-left:1px solid var(--border);overflow-y:auto;flex-shrink:0;padding:16px}
.right-panel h4{font-size:12px;font-weight:600;text-transform:uppercase;color:var(--text-muted);margin-bottom:12px}
.backlinks-list,.outgoing-list,.related-list{display:flex;flex-direction:column;gap:4px;margin-bottom:20px}
.backlink-item,.outgoing-item,.related-item{padding:6px 10px;background:var(--bg-tertiary);border-radius:6px;font-size:12px;cursor:pointer;color:var(--text-muted)}
.backlink-item:hover,.outgoing-item:hover,.related-item:hover{background:var(--border);color:var(--text)}
.related-item .score{font-size:10px;color:var(--accent);margin-left:4px}
.related-item .common{font-size:10px;color:var(--text-muted);margin-top:2px}

/* Graph view */
.graph-view{position:fixed;top:var(--header-h);left:var(--sidebar-w);right:0;bottom:0;background:var(--bg);z-index:10;display:none}
.graph-view.active{display:block}
.graph-view svg{width:100%;height:100%}
.graph-controls{position:absolute;bottom:16px;right:16px;display:flex;gap:8px}
.graph-controls button{padding:8px 16px;background:var(--bg-secondary);border:1px solid var(--border);border-radius:6px;color:var(--text);cursor:pointer;font-size:12px}
.graph-controls button:hover{background:var(--bg-tertiary)}

/* Search results */
.search-results{position:absolute;top:var(--header-h);left:50%;transform:translateX(-50%);width:500px;background:var(--bg-secondary);border:1px solid var(--border);border-radius:8px;box-shadow:0 8px 24px rgba(0,0,0,.4);z-index:20;display:none;max-height:400px;overflow-y:auto}
.search-results.active{display:block}
.search-result-item{padding:12px 16px;border-bottom:1px solid var(--border);cursor:pointer}
.search-result-item:hover{background:var(--bg-tertiary)}
.search-result-item .title{font-weight:600;margin-bottom:4px}
.search-result-item .context{font-size:12px;color:var(--text-muted)}
.search-result-item .type-badge{display:inline-block;padding:1px 6px;border-radius:4px;font-size:10px;margin-left:8px}

/* Editor */
.editor-overlay{position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,.7);z-index:30;display:none;justify-content:center;align-items:center}
.editor-overlay.active{display:flex}
.editor-modal{width:900px;height:80vh;background:var(--bg-secondary);border:1px solid var(--border);border-radius:12px;display:flex;flex-direction:column;overflow:hidden}
.editor-header{padding:16px;border-bottom:1px solid var(--border);display:flex;justify-content:space-between;align-items:center}
.editor-header h3{font-size:16px}
.editor-header .close-btn{background:none;border:none;color:var(--text-muted);font-size:20px;cursor:pointer}
.editor-body{flex:1;display:flex;overflow:hidden}
.editor-pane{flex:1;display:flex;flex-direction:column}
.editor-pane:first-child{border-right:1px solid var(--border)}
.editor-pane h4{padding:8px 16px;font-size:11px;text-transform:uppercase;color:var(--text-muted);border-bottom:1px solid var(--border)}
.editor-textarea{flex:1;background:var(--bg);border:none;color:var(--text);padding:16px;font-family:'Fira Code',monospace;font-size:13px;resize:none;outline:none}
.editor-preview{flex:1;padding:16px;overflow-y:auto;background:var(--bg)}

/* AI Chat Panel */
.ai-panel{position:fixed;top:var(--header-h);right:0;bottom:0;width:400px;background:var(--bg-secondary);border-left:1px solid var(--border);z-index:25;display:none;flex-direction:column}
.ai-panel.active{display:flex}
.ai-panel-header{padding:16px;border-bottom:1px solid var(--border);display:flex;justify-content:space-between;align-items:center}
.ai-panel-header h3{font-size:14px;color:var(--purple)}
.ai-panel-header .close-btn{background:none;border:none;color:var(--text-muted);font-size:18px;cursor:pointer}
.ai-chat{flex:1;overflow-y:auto;padding:16px;display:flex;flex-direction:column;gap:12px}
.ai-msg{padding:10px 14px;border-radius:8px;font-size:13px;line-height:1.5;max-width:90%}
.ai-msg.user{background:var(--accent);color:#fff;align-self:flex-end}
.ai-msg.assistant{background:var(--bg-tertiary);color:var(--text);align-self:flex-start}
.ai-msg .sources{margin-top:8px;font-size:11px;color:var(--text-muted)}
.ai-msg .sources a{color:var(--accent)}
.ai-input{padding:16px;border-top:1px solid var(--border);display:flex;gap:8px}
.ai-input input{flex:1;padding:10px;background:var(--bg);border:1px solid var(--border);border-radius:6px;color:var(--text);font-size:13px}
.ai-input input:focus{outline:none;border-color:var(--purple)}
.ai-input button{padding:10px 16px;background:var(--purple);color:#fff;border:none;border-radius:6px;cursor:pointer;font-size:13px}
.ai-input button:disabled{opacity:0.5;cursor:not-allowed}
.ai-loading{display:flex;gap:4px;padding:10px 14px}
.ai-loading span{width:6px;height:6px;background:var(--text-muted);border-radius:50%;animation:blink 1.2s infinite}
.ai-loading span:nth-child(2){animation-delay:.2s}
.ai-loading span:nth-child(3){animation-delay:.4s}
@keyframes blink{0%,80%,100%{opacity:.2}40%{opacity:1}}

/* Empty state */
.empty-state{display:flex;flex-direction:column;align-items:center;justify-content:center;height:100%;color:var(--text-muted);text-align:center}
.empty-state .icon{font-size:64px;margin-bottom:16px}
.empty-state h2{font-size:28px;margin-bottom:12px;color:var(--accent)}
.empty-state p{font-size:15px;max-width:420px;color:var(--text);line-height:1.7}
.empty-state .hint{font-size:13px;color:var(--green);margin-top:16px}
.empty-state .hint-mobile{font-size:14px;color:var(--yellow);margin-top:8px;display:none}
@media(max-width:700px){
  .empty-state .hint-mobile{display:block}
  .empty-state .icon{font-size:48px}
  .empty-state h2{font-size:22px}
  .empty-state p{font-size:13px}
}

/* Scrollbar */
::-webkit-scrollbar{width:6px;height:6px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:var(--border);border-radius:3px}
::-webkit-scrollbar-thumb:hover{background:var(--text-muted)}

/* Responsive */
@media(max-width:1100px){.ai-panel{width:320px}}
@media(max-width:900px){.right-panel{display:none}}
@media(max-width:700px){
  .sidebar{position:fixed;top:var(--header-h);left:0;bottom:0;z-index:15;display:none}
  .sidebar.active{display:flex}
  .header .logo{font-size:14px}
  .header .search-box{max-width:160px}
  .content{padding:16px}
  .header .btn{font-size:11px;padding:4px 8px}
  .header .btn.ai{display:none}
  .header .actions{gap:4px}
  .menu-btn{display:inline-flex!important}
}
@media(max-width:480px){
  .header{padding:0 8px;gap:6px}
  .header .search-box{max-width:100px}
  .header .actions .btn{font-size:10px;padding:3px 6px;white-space:nowrap}
  .content{padding:12px}
  .page-header h1{font-size:22px}
}
</style>
</head>
<body>
<div class="header">
  <button class="btn menu-btn" onclick="toggleMobileSidebar()" style="display:none;font-size:18px;padding:4px 8px;line-height:1">☰</button>
  <div class="logo" onclick="location.reload()">📚 LLM Wiki</div>
  <div class="search-box"><input type="text" id="search-input" placeholder="검색... (Ctrl+K)"></div>
  <div class="search-results" id="search-results"></div>
  <div class="actions">
    <button class="btn ai" onclick="toggleAI()">🤖 AI</button>
    <button class="btn" onclick="showGraph()">🗺️ 그래프</button>
    <button class="btn" onclick="showIngest()">➕ 수집</button>
    <button class="btn primary" onclick="createPage()">새 페이지</button>
  </div>
</div>

<div class="layout">
  <div class="sidebar" id="sidebar"></div>
  <div class="main">
    <div class="content" id="content">
      <div class="empty-state">
        <div class="icon">📚</div>
        <h2>LLM Wiki</h2>
        <p>사이드바에서 페이지를 선택하거나<br>AI에게 질문해보세요.</p>
        <div class="hint">Ctrl+K 검색  ·  Ctrl+G 그래프  ·  Ctrl+I AI</div>
        <div class="hint-mobile">☰ 메뉴를 눌러 페이지를 선택하세요</div>
      </div>
    </div>
    <div class="right-panel" id="right-panel" style="display:none">
      <h4>🔗 백링크</h4>
      <div class="backlinks-list" id="backlinks-list"></div>
      <h4>📤 아웃고잉</h4>
      <div class="outgoing-list" id="outgoing-list"></div>
      <h4>🔮 연관 페이지</h4>
      <div class="related-list" id="related-list"></div>
    </div>
  </div>
</div>

<!-- AI Chat Panel -->
<div class="ai-panel" id="ai-panel">
  <div class="ai-panel-header">
    <h3>🤖 AI 질의응답</h3>
    <button class="close-btn" onclick="toggleAI()">✕</button>
  </div>
  <div class="ai-chat" id="ai-chat">
    <div class="ai-msg assistant">위키 기반 AI 질의응답입니다. 위키에 수집된 내용으로 답변해드려요. 무엇이든 물어보세요!</div>
  </div>
  <div class="ai-input">
    <input type="text" id="ai-question" placeholder="질문을 입력하세요... (Enter)">
    <button id="ai-send-btn" onclick="askAI()">전송</button>
  </div>
</div>

<!-- Graph View -->
<div class="graph-view" id="graph-view">
  <svg id="graph-svg"></svg>
  <div class="graph-controls">
    <button onclick="filterGraphType('all')">전체</button>
    <button onclick="filterGraphType('entity')">개체</button>
    <button onclick="filterGraphType('daily')">일일</button>
    <button onclick="filterGraphType('knowledge')">지식</button>
    <button onclick="filterGraphType('project')">프로젝트</button>
    <button onclick="filterGraphType('learning')">학습</button>
    <button onclick="closeGraph()">닫기</button>
    <button onclick="resetGraphZoom()">리셋</button>
  </div>
</div>

<!-- Editor Overlay -->
<div class="editor-overlay" id="editor-overlay">
  <div class="editor-modal">
    <div class="editor-header">
      <h3 id="editor-title">새 페이지</h3>
      <button class="close-btn" onclick="closeEditor()">✕</button>
    </div>
    <div class="editor-body">
      <div class="editor-pane">
        <h4>✏️ 편집</h4>
        <textarea class="editor-textarea" id="editor-text" placeholder="마크다운으로 작성하세요..."></textarea>
      </div>
      <div class="editor-pane">
        <h4>👁️ 미리보기</h4>
        <div class="editor-preview" id="editor-preview"></div>
      </div>
    </div>
    <div style="padding:12px 16px;border-top:1px solid var(--border);display:flex;justify-content:flex-end;gap:8px">
      <button class="btn" onclick="closeEditor()">취소</button>
      <button class="btn primary" onclick="savePage()">저장</button>
    </div>
  </div>
</div>

<!-- Ingest Modal -->
<div class="editor-overlay" id="ingest-overlay">
  <div class="editor-modal" style="width:500px;height:auto">
    <div class="editor-header"><h3>➕ URL 수집</h3><button class="close-btn" onclick="closeIngest()">✕</button></div>
    <div style="padding:24px">
      <div style="margin-bottom:16px">
        <label style="display:block;margin-bottom:4px;color:var(--text-muted);font-size:12px">URL</label>
        <input type="text" id="ingest-url" placeholder="https://..." style="width:100%;padding:10px;background:var(--bg);border:1px solid var(--border);border-radius:6px;color:var(--text)">
      </div>
      <div style="margin-bottom:16px">
        <label style="display:block;margin-bottom:4px;color:var(--text-muted);font-size:12px">제목 (선택)</label>
        <input type="text" id="ingest-title" placeholder="자동 감지" style="width:100%;padding:10px;background:var(--bg);border:1px solid var(--border);border-radius:6px;color:var(--text)">
      </div>
      <div id="ingest-status" style="margin-bottom:12px;font-size:13px;color:var(--text-muted)"></div>
      <button class="btn primary" onclick="doIngest()" style="width:100%">수집 시작</button>
    </div>
  </div>
</div>

<script>
const API = '';
let pages = [], tags = {}, currentPage = null, editingSlug = null;
const typeColors = {entity:'#58a6ff',project:'#58a6ff',knowledge:'#3fb950',learning:'#3fb950',daily:'#d29922',concept:'#3fb950',comparison:'#d29922',query:'#a371f7'};
const typeLabels = {entity:'🏷️ Entities',project:'📁 Projects',knowledge:'📚 Knowledge',learning:'💡 Learnings',daily:'📅 Daily',concept:'📄 Concepts',comparison:'⚖️ Comparisons',query:'❓ Queries'};

// ── Init ──────────────────────────────────────────
async function init() {
  await loadPages();
  await loadTags();
  renderSidebar();
  setupSearch();
  setupKeyboard();
  setupAI();
}

async function loadPages() {
  try { const r = await fetch('/api/pages'); pages = await r.json(); } catch(e) { pages = []; }
}
async function loadTags() {
  try { const r = await fetch('/api/tags'); tags = await r.json(); } catch(e) { tags = {}; }
}

// ── Sidebar ───────────────────────────────────────
function renderSidebar() {
  const sb = document.getElementById('sidebar');
  const grouped = {};
  pages.forEach(p => { (grouped[p.page_type] = grouped[p.page_type] || []).push(p); });

  const categoryOrder = ['project','knowledge','learning','daily','entity','concept','comparison','query'];
  const categoryIcons = {project:'📁',knowledge:'📚',learning:'💡',daily:'📅',entity:'🏷️',concept:'📄',comparison:'⚖️',query:'❓'};

  let html = '';
  for (const type of categoryOrder) {
    const items = grouped[type];
    if (!items || !items.length) continue;
    const label = typeLabels[type] || type;
    const icon = categoryIcons[type] || '📄';
    html += `<div class="sidebar-section">
      <div class="sidebar-section-title" onclick="toggleSection(this)">
        <span>${icon} ${label}</span>
        <span class="count">${items.length}</span>
      </div>
      <div class="sidebar-section-content open">
        ${items.map(p => `<div class="sidebar-item" onclick="openPage('${p.slug}')">
          <span class="icon">${icon}</span>
          <span>${p.title}</span>
        </div>`).join('')}
      </div></div>`;
  }

  // Also render any types not in categoryOrder
  for (const [type, items] of Object.entries(grouped)) {
    if (categoryOrder.includes(type)) continue;
    const label = typeLabels[type] || type;
    html += `<div class="sidebar-section">
      <div class="sidebar-section-title" onclick="toggleSection(this)">
        <span>${label}</span>
        <span class="count">${items.length}</span>
      </div>
      <div class="sidebar-section-content open">
        ${items.map(p => `<div class="sidebar-item" onclick="openPage('${p.slug}')">
          <span>📄</span>
          <span>${p.title}</span>
        </div>`).join('')}
      </div></div>`;
  }

  const tagEntries = Object.entries(tags).sort((a,b) => b[1]-a[1]).slice(0,20);
  if (tagEntries.length) {
    html += `<div class="sidebar-section">
      <div class="sidebar-section-title" onclick="toggleSection(this)"><span>🏷️ 태그</span></div>
      <div class="sidebar-section-content open"><div class="tag-cloud">
        ${tagEntries.map(([t,c]) => `<span class="tag-chip" onclick="filterByTag('${t}')">${t} (${c})</span>`).join('')}
      </div></div></div>`;
  }

  sb.innerHTML = html || '<div style="padding:24px;color:var(--text-muted);text-align:center">페이지가 없습니다</div>';
}

function toggleSection(el) {
  el.nextElementSibling.classList.toggle('open');
}

// ── Page View ─────────────────────────────────────
async function openPage(slug) {
  try {
    const r = await fetch(`/api/page/${slug}`);
    if (!r.ok) return;
    const pg = await r.json();
    currentPage = pg;

    document.querySelectorAll('.sidebar-item').forEach(el => el.classList.remove('active'));
    event?.target?.closest('.sidebar-item')?.classList.add('active');

    const content = document.getElementById('content');
    const tagsHtml = (pg.tags||[]).map(t => `<span class="tag">${t}</span>`).join('');
    const typeBadge = `<span class="badge ${pg.page_type}">${typeLabels[pg.page_type]||pg.page_type}</span>`;
    const contestedBadge = pg.contested ? '<span class="badge contested">⚠ 모순</span>' : '';

    content.innerHTML = `<div class="content-inner">
      <div class="page-header">
        <h1>${pg.title}</h1>
        <div class="page-meta">
          ${typeBadge} ${contestedBadge}
          <span>📅 ${pg.updated||pg.created||'—'}</span>
          ${tagsHtml}
          <button class="btn" onclick="editPage('${slug}')" style="margin-left:auto">✏️ 편집</button>
        </div>
      </div>
      <div class="markdown-body">${pg.html}</div>
    </div>`;

    document.querySelectorAll('pre code').forEach(el => { try { hljs.highlightElement(el); } catch(e) {} });
    document.querySelectorAll('.wikilink').forEach(el => {
      el.addEventListener('click', () => openPage(el.dataset.slug));
    });

    // Right panel
    const rp = document.getElementById('right-panel');
    rp.style.display = 'block';

    const bl = pg.backlinks || [];
    document.getElementById('backlinks-list').innerHTML = bl.length
      ? bl.map(b => `<div class="backlink-item" onclick="openPage('${b.slug}')">${b.title}</div>`).join('')
      : '<div style="color:var(--text-muted);font-size:12px">없음</div>';

    const ol = pg.wikilinks || [];
    document.getElementById('outgoing-list').innerHTML = ol.length
      ? ol.map(l => { const s = l.toLowerCase().replace(/\s+/g,'-'); return `<div class="outgoing-item" onclick="openPage('${s}')">${l}</div>`; }).join('')
      : '<div style="color:var(--text-muted);font-size:12px">없음</div>';

    // Related pages
    const related = pg.related || [];
    document.getElementById('related-list').innerHTML = related.length
      ? related.map(r => `<div class="related-item" onclick="openPage('${r.slug}')">
          <div>${r.title} <span class="score">⭐ ${r.score}</span></div>
          ${r.common_links?.length ? `<div class="common">공통: ${r.common_links.join(', ')}</div>` : ''}
        </div>`).join('')
      : '<div style="color:var(--text-muted);font-size:12px">없음</div>';

  } catch(e) { console.error(e); }
}

// ── Editor ────────────────────────────────────────
function editPage(slug) {
  editingSlug = slug;
  const pg = pages.find(p => p.slug === slug);
  document.getElementById('editor-title').textContent = `편집: ${pg?.title||slug}`;
  document.getElementById('editor-text').value = pg?.body || '';
  updatePreview();
  document.getElementById('editor-overlay').classList.add('active');
}

function createPage() {
  editingSlug = 'new-page-' + Date.now();
  document.getElementById('editor-title').textContent = '새 페이지';
  document.getElementById('editor-text').value = '# 새 페이지\n\n내용을 입력하세요...';
  updatePreview();
  document.getElementById('editor-overlay').classList.add('active');
}

function closeEditor() {
  document.getElementById('editor-overlay').classList.remove('active');
  editingSlug = null;
}

async function savePage() {
  const body = document.getElementById('editor-text').value;
  const title = body.split('\n').find(l => l.startsWith('# '))?.slice(2).trim() || editingSlug;
  const tagMatch = body.match(/tags:\s*\[([^\]]+)\]/);
  const tags = tagMatch ? tagMatch[1].split(',').map(t => t.trim()) : [];
  try {
    await fetch(`/api/page/${editingSlug}`, {
      method: 'POST', headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({body, title, tags, type: 'concept'}),
    });
    closeEditor();
    await loadPages(); renderSidebar(); openPage(editingSlug);
  } catch(e) { alert('저장 실패: ' + e); }
}

function updatePreview() {
  const text = document.getElementById('editor-text').value;
  let html = text
    .replace(/^### (.+)$/gm, '<h3>$1</h3>')
    .replace(/^## (.+)$/gm, '<h2>$1</h2>')
    .replace(/^# (.+)$/gm, '<h1>$1</h1>')
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.+?)\*/g, '<em>$1</em>')
    .replace(/`(.+?)`/g, '<code>$1</code>')
    .replace(/\[\[(.+?)\]\]/g, '<span class="wikilink">$1</span>')
    .replace(/^- (.+)$/gm, '<li>$1</li>')
    .replace(/\n\n/g, '</p><p>');
  html = '<p>' + html + '</p>';
  document.getElementById('editor-preview').innerHTML = html;
}
document.getElementById('editor-text')?.addEventListener('input', updatePreview);

// ── Search ────────────────────────────────────────
function setupSearch() {
  const input = document.getElementById('search-input');
  const results = document.getElementById('search-results');
  let debounce = null;

  input.addEventListener('input', () => {
    clearTimeout(debounce);
    debounce = setTimeout(async () => {
      const q = input.value.trim();
      if (q.length < 2) { results.classList.remove('active'); return; }
      try {
        const r = await fetch(`/api/search?q=${encodeURIComponent(q)}`);
        const data = await r.json();
        if (!data.length) { results.innerHTML = '<div style="padding:16px;color:var(--text-muted)">결과 없음</div>'; }
        else { results.innerHTML = data.map(d => `<div class="search-result-item" onclick="openPage('${d.slug}');results.classList.remove('active')">
          <div class="title">${d.title}<span class="type-badge badge ${d.type}">${typeLabels[d.type]||d.type}</span></div>
          <div class="context">${d.context}</div>
        </div>`).join(''); }
        results.classList.add('active');
      } catch(e) {}
    }, 300);
  });

  input.addEventListener('keydown', (e) => { if (e.key === 'Escape') results.classList.remove('active'); });
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.search-box') && !e.target.closest('#search-results')) results.classList.remove('active');
  });
}

// ── Keyboard shortcuts ────────────────────────────
function setupKeyboard() {
  document.addEventListener('keydown', (e) => {
    if (e.key === 'k' && (e.ctrlKey || e.metaKey)) { e.preventDefault(); document.getElementById('search-input').focus(); }
    if (e.key === 'g' && (e.ctrlKey || e.metaKey)) { e.preventDefault(); showGraph(); }
    if (e.key === 'i' && (e.ctrlKey || e.metaKey)) { e.preventDefault(); toggleAI(); }
  });
}

// ── AI Chat Input ────────────────────────────────
function setupAI() {
  const input = document.getElementById('ai-question');
  let composing = false;
  let pending = null;

  input.addEventListener('compositionstart', () => { composing = true; });
  input.addEventListener('compositionend', () => {
    composing = false;
    if (pending) {
      input.value = pending.value;
      const fn = pending.fn;
      pending = null;
      fn();
    }
  });
  input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
      if (composing || e.isComposing) {
        pending = { value: input.value, fn: askAI };
        e.preventDefault();
      } else {
        askAI();
      }
    }
  });
}

// ── Graph View (Enhanced) ─────────────────────────
let graphData = null;
async function showGraph() {
  document.getElementById('graph-view').classList.add('active');
  try {
    const r = await fetch('/api/graph');
    graphData = await r.json();
    drawGraph(graphData);
  } catch(e) {}
}

function getNodeRadius(d, nodeDegrees) {
  const deg = nodeDegrees.get(d.id) || 1;
  return Math.min(12, Math.max(5, 3 + Math.sqrt(deg) * 1.8));
}

function getNodeColor(type) { return typeColors[type] || '#8b949e'; }

function drawGraph(data) {
  const container = document.getElementById('graph-view');
  const svg = d3.select('#graph-svg');
  svg.selectAll('*').remove();

  const W = container.clientWidth;
  const H = container.clientHeight;

  // Calculate node degrees for sizing
  const nodeDegrees = new Map();
  const nodeTypeMap = new Map();
  data.nodes.forEach(n => {
    nodeDegrees.set(n.id, 0);
    nodeTypeMap.set(n.id, n.type || 'concept');
  });
  data.links.forEach(l => {
    nodeDegrees.set(l.source, (nodeDegrees.get(l.source) || 0) + 1);
    nodeDegrees.set(l.target, (nodeDegrees.get(l.target) || 0) + 1);
  });

  const nodes = data.nodes.map(d => ({
    ...d,
    r: getNodeRadius(d, nodeDegrees),
    color: getNodeColor(d.type),
    deg: nodeDegrees.get(d.id) || 0
  }));
  const links = data.links.map(d => ({...d}));

  // Zoom support
  const g = svg.append('g');

  const simulation = d3.forceSimulation(nodes)
    .force('link', d3.forceLink(links).id(d => d.id).distance(d => 120 - Math.min(d.deg, 5) * 8).strength(0.3))
    .force('charge', d3.forceManyBody().strength(d => -80 - d.deg * 15))
    .force('center', d3.forceCenter(W/2, H/2))
    .force('collision', d3.forceCollide().radius(d => d.r + 8));

  // Links
  const link = g.append('g').selectAll('line').data(links).enter().append('line')
    .attr('stroke', '#30363d')
    .attr('stroke-width', d => Math.min(3, Math.max(0.5, (nodeDegrees.get(d.source.id || d.source) || 0) / 5)))
    .attr('opacity', 0.5);

  // Nodes
  const node = g.append('g').selectAll('g').data(nodes).enter().append('g')
    .call(d3.drag()
      .on('start', (e, d) => {
        if (!e.active) simulation.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
      })
      .on('drag', (e, d) => { d.fx = e.x; d.fy = e.y; })
      .on('end', (e, d) => {
        if (!e.active) simulation.alphaTarget(0);
        d.fx = null;
        d.fy = null;
      }));

  // Circle
  node.append('circle')
    .attr('r', d => d.r)
    .attr('fill', d => d.color)
    .attr('stroke', '#fff')
    .attr('stroke-width', 1.5)
    .style('cursor', 'pointer')
    .on('click', (e, d) => { closeGraph(); openPage(d.id); })
    .on('mouseenter', function(e, d) {
      d3.select(this).attr('stroke', '#58a6ff').attr('stroke-width', 2.5);
      showTooltip(e, d, nodeDegrees.get(d.id) || 0);
    })
    .on('mouseleave', function() {
      d3.select(this).attr('stroke', '#fff').attr('stroke-width', 1.5);
      hideTooltip();
    });

  // Label
  node.append('text')
    .attr('dx', d => d.r + 6)
    .attr('dy', 4)
    .text(d => d.title.length > 18 ? d.title.slice(0, 16) + '...' : d.title)
    .attr('fill', '#c9d1d9')
    .attr('font-size', d => Math.min(12, Math.max(9, 8 + Math.sqrt(d.deg) * 0.5)))
    .style('pointer-events', 'none');

  simulation.on('tick', () => {
    link
      .attr('x1', d => d.source.x)
      .attr('y1', d => d.source.y)
      .attr('x2', d => d.target.x)
      .attr('y2', d => d.target.y);
    node.attr('transform', d => `translate(${d.x},${d.y})`);
  });

  // Zoom
  const zoom = d3.zoom()
    .scaleExtent([0.1, 4])
    .on('zoom', (e) => { g.attr('transform', e.transform); });
  svg.call(zoom);

  // Tooltip element
  let tooltip = d3.select('#graph-tooltip');
  if (tooltip.empty()) {
    tooltip = d3.select(container)
      .append('div')
      .attr('id', 'graph-tooltip')
      .style('position', 'absolute')
      .style('background', '#1c2333')
      .style('color', '#c9d1d9')
      .style('padding', '8px 12px')
      .style('border-radius', '8px')
      .style('border', '1px solid #30363d')
      .style('font-size', '12px')
      .style('pointer-events', 'none')
      .style('opacity', 0)
      .style('z-index', 100)
      .style('max-width', '250px');
  }

  function showTooltip(e, d, deg) {
    tooltip
      .style('opacity', 1)
      .html(`<strong style="color:#58a6ff">${d.title}</strong><br/>
             <span style="color:#8b949e">${typeLabels[d.type] || d.type} · ${deg} connections</span>`)
      .style('left', (e.pageX - container.getBoundingClientRect().left + 15) + 'px')
      .style('top', (e.pageY - container.getBoundingClientRect().top - 10) + 'px');
  }
  function hideTooltip() { tooltip.style('opacity', 0); }
}

function closeGraph() { document.getElementById('graph-view').classList.remove('active'); }
function resetGraphZoom() {
  d3.select('#graph-svg').transition().duration(300)
    .call(d3.zoom().transform, d3.zoomIdentity);
}

// Graph filter functions
function filterGraphType(type) {
  if (!graphData) return;
  const nodes = graphData.nodes;
  const links = graphData.links;
  const filtered = type === 'all'
    ? nodes
    : nodes.filter(n => n.type === type);
  const filteredIds = new Set(filtered.map(n => n.id));
  drawGraph({
    nodes: filtered,
    links: links.filter(l => filteredIds.has(l.source) && filteredIds.has(l.target))
  });
}

// ── Ingest ────────────────────────────────────────
function showIngest() { document.getElementById('ingest-overlay').classList.add('active'); }
function closeIngest() { document.getElementById('ingest-overlay').classList.remove('active'); }

async function doIngest() {
  const url = document.getElementById('ingest-url').value.trim();
  const title = document.getElementById('ingest-title').value.trim();
  if (!url) { document.getElementById('ingest-status').textContent = 'URL을 입력하세요'; return; }
  document.getElementById('ingest-status').textContent = '수집 중...';
  try {
    const r = await fetch('/api/ingest', { method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({url,title}) });
    const data = await r.json();
    if (data.status === 'ok') {
      document.getElementById('ingest-status').textContent = '✅ 완료!';
      await loadPages(); await loadTags(); renderSidebar();
      setTimeout(closeIngest, 1000);
    } else { document.getElementById('ingest-status').textContent = '❌ ' + (data.error || '실패'); }
  } catch(e) { document.getElementById('ingest-status').textContent = '❌ ' + e; }
}

function filterByTag(tag) {
  document.getElementById('search-input').value = tag;
  document.getElementById('search-input').dispatchEvent(new Event('input'));
}

// ── Mobile sidebar ────────────────────────────────
function toggleMobileSidebar() {
  document.getElementById('sidebar').classList.toggle('active');
}
// Close sidebar when selecting a page on mobile
document.addEventListener('click', (e) => {
  if (window.innerWidth <= 700 && e.target.closest('.sidebar-item')) {
    document.getElementById('sidebar').classList.remove('active');
  }
});

// ── AI Chat ───────────────────────────────────────
function toggleAI() {
  const panel = document.getElementById('ai-panel');
  panel.classList.toggle('active');
  if (panel.classList.contains('active')) {
    document.getElementById('ai-question').focus();
  }
}

async function askAI() {
  const input = document.getElementById('ai-question');
  const btn = document.getElementById('ai-send-btn');
  const chat = document.getElementById('ai-chat');
  const question = input.value.trim();
  if (!question) return;

  // Add user message
  chat.innerHTML += `<div class="ai-msg user">${question}</div>`;
  input.value = '';
  btn.disabled = true;

  // Loading
  chat.innerHTML += `<div class="ai-msg assistant" id="ai-loading"><div class="ai-loading"><span></span><span></span><span></span></div></div>`;
  chat.scrollTop = chat.scrollHeight;

  try {
    const r = await fetch('/api/query', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({question}),
    });
    const data = await r.json();
    document.getElementById('ai-loading')?.remove();

    let sourcesHtml = '';
    if (data.sources?.length) {
      sourcesHtml = `<div class="sources">📚 출처: ${data.sources.map(s => `<a href="#" onclick="openPage('${s.slug}');return false">${s.title}</a>`).join(', ')}</div>`;
    }

    chat.innerHTML += `<div class="ai-msg assistant">${data.answer || data.error || '답변을 생성하지 못했습니다.'}${sourcesHtml}</div>`;
  } catch(e) {
    document.getElementById('ai-loading')?.remove();
    chat.innerHTML += `<div class="ai-msg assistant">오류: ${e}</div>`;
  }

  btn.disabled = false;
  chat.scrollTop = chat.scrollHeight;
}

// ── Start ─────────────────────────────────────────
init();
</script>
</body>
</html>"""


# ── Run ─────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn
    print(f"🌐 LLM Wiki Web UI starting...")
    print(f"   Wiki path: {WIKI_PATH}")
    print(f"   RAG engine: {'✅' if RAG_AVAILABLE else '❌'}")
    print(f"   Open: http://localhost:8090")
    uvicorn.run(app, host="0.0.0.0", port=8090, log_level="info")
