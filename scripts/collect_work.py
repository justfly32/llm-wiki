#!/usr/bin/env python3
"""
LLM Wiki — Work Change Collector (Phase 1)
============================================
LLM 작업 결과(파일 변경)를 감지하여 위키 동기화용 요약을 생성한다.

감시 대상:
  - ~/projects/           (프로젝트 전체)
  - ~/.hermes/            (Hermes 에이전트 하위 — 캐시/로그/세션 등 노이즈 제외)

동작:
  1. 마지막 스캔 시각(/tmp/.llm-wiki-work-sync) 이후 mtime이 변경된 파일 수집
  2. git 저장소는 최근 커밋 로그 추가 수집
  3. 파일을 유형별(코드/문서/설정/데이터/웹/이미지/기타)로 분류
  4. 요약을 stdout으로 출력 + 상세를 /tmp/llm_work_changes.json에 저장

크론(llm-wiki-daily-sync)이 이 스크립트를 실행하고, 출력 요약을 기반으로
concepts/daily/ 페이지를 갱신한다.
"""
import os
import json
import sys
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

HOME = Path.home()
SCAN_ROOTS = [HOME / "projects", HOME / ".hermes"]
SYNC_MARKER = Path("/tmp/.llm-wiki-work-sync")
OUTPUT_FILE = Path("/tmp/llm_work_changes.json")

# 제외 디렉토리 (캐시/로그/세션/의존성 등 작업 결과물 아님)
EXCLUDE_DIRS = {
    "node_modules", ".git", ".venv", "venv", "__pycache__", "dist", "build",
    ".next", ".cache", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".DS_Store",
    "logs", "cache", "audio_cache", "image_cache", "bootstrap-cache", "node",
    "lsp", "pastes", "sandboxes", "sessions", "rate_limits", "migration",
    "pairing", "profiles", "gateway", "mcp-env", "bin", "shared",
    "state-snapshots", "bootstrap-cache", "venvs", "output",
}

# 제외 파일 패턴 (Hermes 내부 상태 DB 등)
EXCLUDE_FILES = {
    "state.db", "state.db-wal", "state.db-shm",
    "verification_evidence.db", "models_dev_cache.json",
    "gateway_state.json", "channel_directory.json", "ticker_heartbeat",
    "ticker_last_success", ".tick.lock", ".jobs.lock",
}

# 파일 유형 분류
TYPE_MAP = {
    ".py": "code", ".js": "code", ".ts": "code", ".tsx": "code", ".jsx": "code",
    ".sh": "code", ".bash": "code", ".go": "code", ".rs": "code", ".java": "code",
    ".c": "code", ".cpp": "code", ".swift": "code", ".kt": "code", ".rb": "code",
    ".php": "code", ".sql": "code",
    ".md": "doc", ".mdx": "doc", ".txt": "doc", ".rst": "doc",
    ".docx": "doc", ".hwp": "doc", ".pdf": "doc",
    ".json": "config", ".yaml": "config", ".yml": "config", ".toml": "config",
    ".ini": "config", ".env": "config", ".plist": "config", ".conf": "config",
    ".xlsx": "data", ".csv": "data", ".db": "data", ".sqlite": "data",
    ".pkl": "data", ".parquet": "data", ".jsonl": "data",
    ".html": "web", ".css": "web", ".scss": "web",
    ".png": "image", ".jpg": "image", ".jpeg": "image", ".gif": "image",
    ".webp": "image", ".svg": "image", ".ico": "image",
}

def classify(path: Path) -> str:
    ext = path.suffix.lower()
    return TYPE_MAP.get(ext, "other")

def should_skip_dir(name: str) -> bool:
    return name in EXCLUDE_DIRS or name.startswith(".")

def scan_changed_files(since: float):
    """since 이후 mtime인 파일 수집. (경로, mtime, 크기, 유형, 루트명)"""
    changed = []
    for root in SCAN_ROOTS:
        if not root.exists():
            continue
        root_name = root.name  # 'projects' | '.hermes'
        for dirpath, dirnames, filenames in os.walk(root):
            # 제외 디렉토리 prunning
            dirnames[:] = [d for d in dirnames if not should_skip_dir(d)]
            for fname in filenames:
                if fname in (".DS_Store",) or fname in EXCLUDE_FILES:
                    continue
                fp = Path(dirpath) / fname
                try:
                    st = fp.stat()
                except OSError:
                    continue
                if st.st_mtime > since:
                    changed.append({
                        "path": str(fp),
                        "rel": str(fp.relative_to(root)),
                        "root": root_name,
                        "mtime": datetime.fromtimestamp(st.st_mtime).isoformat(timespec="minutes"),
                        "size": st.st_size,
                        "type": classify(fp),
                    })
    return changed

def collect_git_commits(since: str, max_commits: int = 20):
    """스캔 루트 내 git 저장소의 최근 커밋 로그 수집"""
    commits = []
    seen_repos = set()
    for root in SCAN_ROOTS:
        if not root.exists():
            continue
        for dirpath, dirnames, _ in os.walk(root):
            dirnames[:] = [d for d in dirnames if not should_skip_dir(d)]
            git_dir = Path(dirpath) / ".git"
            if git_dir.exists() and str(dirpath) not in seen_repos:
                seen_repos.add(str(dirpath))
                try:
                    r = subprocess.run(
                        ["git", "log", f"--since={since}", "--oneline", "-n", str(max_commits)],
                        cwd=dirpath, capture_output=True, text=True, timeout=10,
                    )
                    if r.returncode == 0 and r.stdout.strip():
                        lines = [ln.strip() for ln in r.stdout.strip().splitlines()]
                        commits.append({
                            "repo": str(Path(dirpath).relative_to(root)),
                            "root": root.name,
                            "count": len(lines),
                            "subjects": lines,
                        })
                except (subprocess.TimeoutExpired, OSError):
                    pass
                dirnames[:] = []  # git 저장소 내부는 재귀 방문 불필요
    return commits

def main():
    # 1. 기준 시각 결정
    if SYNC_MARKER.exists():
        try:
            since_ts = float(SYNC_MARKER.read_text().strip())
            since_dt = datetime.fromtimestamp(since_ts)
        except (ValueError, OSError):
            since_dt = datetime.now() - timedelta(hours=24)
    else:
        since_dt = datetime.now() - timedelta(hours=24)  # 최초: 최근 24시간
    since_ts = since_dt.timestamp()
    since_iso = since_dt.strftime("%Y-%m-%d %H:%M")
    now = datetime.now()

    # 2. 변경 파일 스캔
    changed = scan_changed_files(since_ts)
    # 프로젝트 규모가 크므로 코드/문서/설정 우선, 노이즈(이미지/기타 대량)는 캡
    code_docs = [c for c in changed if c["type"] in ("code", "doc", "config", "data", "web")]
    images = [c for c in changed if c["type"] == "image"]
    others = [c for c in changed if c["type"] == "other"]
    # 이미지/기타는 최대 20개만 요약에 포함
    capped_others = others[:20]
    kept = code_docs + images[:20] + capped_others

    # 3. git 커밋 수집
    commits = collect_git_commits(since_iso)

    # 4. 요약 집계
    by_type = {}
    for c in kept:
        by_type[c["type"]] = by_type.get(c["type"], 0) + 1
    by_root = {}
    for c in kept:
        by_root[c["root"]] = by_root.get(c["root"], 0) + 1
    by_project = {}
    for c in kept:
        if c["root"] == "projects":
            parts = Path(c["rel"]).parts
            proj = parts[0] if parts else "?"
            by_project[proj] = by_project.get(proj, 0) + 1

    # 5. 출력 파일 저장
    output = {
        "generated_at": now.isoformat(timespec="seconds"),
        "window": {"since": since_iso, "until": now.strftime("%Y-%m-%d %H:%M")},
        "total_changed_raw": len(changed),
        "total_kept": len(kept),
        "by_type": by_type,
        "by_root": by_root,
        "by_project": by_project,
        "git_commits": commits,
        "files": kept,
    }
    OUTPUT_FILE.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")

    # 6. stdout 요약 (크론이 읽는 형태)
    if not kept and not commits:
        print("오늘은 변경된 내역이 없습니다.")
        return

    print(f"📁 작업 변경 감지 ({since_iso} ~ {now.strftime('%H:%M')})")
    print(f"  총 {len(changed)}개 파일 변경 (요약 {len(kept)}개)")
    if by_type:
        print(f"  유형: {', '.join(f'{k} {v}개' for k, v in sorted(by_type.items()))}")
    if by_root:
        print(f"  루트: {', '.join(f'{k} {v}개' for k, v in sorted(by_root.items()))}")
    if by_project:
        top = sorted(by_project.items(), key=lambda x: -x[1])[:8]
        print(f"  프로젝트: {', '.join(f'{k} {v}개' for k, v in top)}")
    if commits:
        print(f"\n🔄 git 커밋 ({len(commits)}개 저장소)")
        for c in commits[:6]:
            print(f"  [{c['root']}/{c['repo']}] {c['count']}개 커밋")
            for s in c["subjects"][:5]:
                print(f"    - {s}")
    # 대표 파일 몇 개 표시
    print("\n  대표 파일:")
    for c in kept[:12]:
        print(f"    [{c['type']}] {c['root']}/{c['rel']} ({c['mtime']})")
    print(f"\n📄 상세: {OUTPUT_FILE}")

    # 7. 기준 시각 갱신 (성공 시에만)
    SYNC_MARKER.write_text(str(now.timestamp()))

if __name__ == "__main__":
    main()
