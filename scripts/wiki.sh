#!/bin/bash
# Wiki Quick Commands — bash aliases/functions
# Usage: source this file → source ~/wiki/scripts/wiki.sh
# Or run directly: bash ~/wiki/scripts/wiki.sh <command>

WIKI_PATH="$HOME/wiki"
WIKI_PY="$WIKI_PATH/wiki.py"

wiki-ingest() {
    if [ -z "$1" ]; then
        echo "Usage: wiki-ingest <URL or file> [title]"
        return 1
    fi
    echo "📥 Ingesting: $1"
    python3 "$WIKI_PY" ingest "$1" "$2"
    echo "✅ Done. Wiki updated."
}

wiki-search() {
    if [ -z "$1" ]; then
        echo "Usage: wiki-search <query>"
        return 1
    fi
    python3 "$WIKI_PY" search "$@"
}

wiki-lint() {
    echo "🔍 Linting wiki..."
    python3 "$WIKI_PY" lint
}

wiki-status() {
    echo "📊 Wiki Status"
    echo "─────────────"
    python3 "$WIKI_PY" status
}

wiki-index() {
    echo "📋 Rebuilding index..."
    python3 "$WIKI_PY" index
}

wiki-query() {
    if [ -z "$1" ]; then
        echo "Usage: wiki-query <question>"
        return 1
    fi
    python3 "$WIKI_PY" query "$@"
}

wiki-save() {
    cd "$WIKI_PATH"
    git add -A 2>/dev/null
    local count=$(git diff --cached --numstat 2>/dev/null | wc -l)
    if [ "$count" -gt 0 ]; then
        git commit -m "wiki auto-save: $count files ($(date '+%Y-%m-%d %H:%M'))" --quiet 2>/dev/null
        echo "💾 Git saved: $count files"
    else
        echo "💾 No changes."
    fi
}

wiki-daily() {
    echo "🔄 Running daily wiki update..."
    local today=$(date '+%Y-%m-%d')
    local log_file="$WIKI_PATH/.daily_last_run"
    if [ -f "$log_file" ] && [ "$(cat $log_file)" = "$today" ]; then
        echo "Already ran today ($today). Skip."
        return 0
    fi
    echo "$today" > "$log_file"
    echo "📚 Collecting arXiv papers..."
    python3 "$WIKI_PATH/scripts/collect_arxiv.py" 2>&1
    echo "🔥 Collecting Hacker News..."
    python3 "$WIKI_PATH/scripts/collect_hn.py" 2>&1
    echo "🔍 Linting..."
    python3 "$WIKI_PY" lint 2>&1
    wiki-save
    echo "✅ Daily wiki update complete!"
}

wiki-help() {
    echo "📖 Wiki Commands"
    echo "─────────────────────────────"
    echo "wiki-ingest <URL> [title]  — URL/파일 수집"
    echo "wiki-search <query>        — 검색"
    echo "wiki-lint                  — 린트"
    echo "wiki-status                — 현황"
    echo "wiki-query <question>      — 질의응답"
    echo "wiki-save                  — Git 자동 저장"
    echo "wiki-daily                 — 일일 자동 수집"
    echo "─────────────────────────────"
}
