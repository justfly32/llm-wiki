#!/usr/bin/env python3
"""
LLM Wiki — 프로젝트 레지스트리 생성기 (2026-08-09)
===================================================
~/projects + home 직속 프로젝트 폴더 전체를 스캔해 위키 레지스트리 문서를 생성한다.

목적:
  - 코딩 요청 시 폴더 중복 생성 방지 (위치/이름/역할을 한눈에)
  - 비슷한 프로젝트가 이미 있는지 사전 확인 가능

사용법:
  python3 ~/wiki/scripts/generate_project_registry.py          # 생성/갱신
  python3 ~/wiki/scripts/generate_project_registry.py --dry    # 출력만 확인

출력:
  ~/wiki/concepts/projects/project-registry.md (덮어쓰기)
"""
import argparse
import json
import re
import subprocess
from datetime import datetime
from pathlib import Path

HOME = Path.home()
PROJECTS_DIR = HOME / "projects"
OUTPUT = HOME / "wiki" / "concepts" / "projects" / "project-registry.md"

# home 직속 추가 프로젝트 폴더 (projects/ 밖에 있는 것)
# 2026-08-09: justfly32.github.io → ~/projects/로 이동 완료 (더 이상 EXTRA_DIRS 불필요)
EXTRA_DIRS = []

# ⭐ 정본(canonical) 지정 — 중복 그룹에서 운영 정본 (2026-08-09 확정, "최신 것이 정본" 원칙)
CANONICAL = {
    "elderly-health-care": "노인 건강관리 정본 (4개 기능 구현, 커밋 f317391)",
    "code-edu-lab": "코딩 교육 정본 (4스택 9,700파일, 6/27 최신)",
    "simpli-gif-maker": "GIF 생성 정본 (Flask+기능 최다 4,239파일, 포트폴리오 서빙 중)",
    "pc-llm-dashboard": "PC 상태+LLM 사용량 통합 대시보드 정본 (3종 통합, React19+Vite+Express, 포트 5175/4010)",
    "enterprise-search": "사내 파일 검색 PoC (DRM 무관 Accessor 추상화 + 권한 ACL + 하이브리드 검색 + RAG, 포트 8091/3001)",
}

# 🗑️ 삭제된 비정본 (2026-08-09 휴지통 이동: ~/.Trash/hermes-removed-20260809/)
REMOVED = {
    "elderly-health": "create-next-app 초기 커밋만 있는 빈 껍데기 (git remote 없음)",
    "code-tutorial": "초기 4파일 버전 (Code Vibe, GitHub 원격에 백업 존재)",
    "code-express": "node_modules만 있는 빈 폴더",
    "stickman-gif-creator": "6/13 구버전 파이썬 구현",
    "simple-anim-maker": "빈 폴더",
    "animation-maker": "4파일 미니멀 버전",
    "simpli-video-maker": "2파일 미니멀 버전",
    "system-dashboard": "대시보드 구버전 (pc-llm-dashboard로 통합)",
    "system-monitor-dashboard": "대시보드 축소판 (시스템 모니터 탭만, pc-llm-dashboard로 통합)",
    "openclaw-token-dashboard": "대시보드 구버전 (리팩토링 코드를 pc-llm-dashboard 베이스로 사용)",
}

# 설명 추출 제외 키워드 (부트스트랩 기본 설명)
NOISE_DESC = {"this is a", "this template", "<div align", ">", "create-next-app"}


def run(cmd: list, cwd: Path) -> str:
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=10)
        return r.stdout.strip()
    except Exception:
        return ""


def get_git_info(d: Path) -> dict:
    remote = run(["git", "remote", "get-url", "origin"], d)
    remote = re.sub(r"git@github\.com:|https://github\.com/|\.git$", "", remote)
    last = run(["git", "log", "-1", "--format=%ad", "--date=short"], d)
    return {"remote": remote, "last": last or "-"}


def get_desc(d: Path) -> str:
    """README/package.json/pyproject에서 설명 1줄 추출"""
    readme = d / "README.md"
    if readme.exists():
        for line in readme.read_text(encoding="utf-8", errors="replace").splitlines()[:10]:
            line = line.strip()
            if not line or line.startswith("#") or line.startswith(">"):
                continue
            line = re.sub(r"[*_`>#]", "", line).strip()
            if line and line.lower()[:5] not in NOISE_DESC and len(line) > 10:
                return line[:120]
    pkg = d / "package.json"
    if pkg.exists():
        try:
            desc = json.loads(pkg.read_text(encoding="utf-8")).get("description", "")
            if desc and desc.lower()[:5] not in NOISE_DESC:
                return desc[:120]
        except Exception:
            pass
    pyproj = d / "pyproject.toml"
    if pyproj.exists():
        m = re.search(r'description\s*=\s*"([^"]+)"', pyproj.read_text(encoding="utf-8", errors="replace"))
        if m:
            return m.group(1)[:120]
    return ""


def clean_cell(text: str) -> str:
    """마크다운 테이블 셀 안전화: 파이프/줄바꿈 제거"""
    text = re.sub(r"\|", "/", text)
    return re.sub(r"\s+", " ", text).strip()


def count_files(d: Path) -> int:
    n = 0
    skip = {"node_modules", ".git", ".venv", "__pycache__", ".next", "dist", "build", ".pytest_cache", ".ruff_cache"}
    for p in d.rglob("*"):
        if p.is_file() and p.name != ".DS_Store":
            if any(part in skip for part in p.parts):
                continue
            n += 1
    return n


def scan() -> list:
    items = []
    for root in [PROJECTS_DIR] + EXTRA_DIRS:
        if not root.exists():
            continue
        for d in sorted([p for p in root.iterdir() if p.is_dir()]):
            name = d.name
            if name.startswith(".") or name in {"templates", "scripts", "docs", "images", "assets", "tests"}:
                continue  # 리소스/공용 폴더 제외
            git = get_git_info(d)
            items.append({
                "name": name,
                "path": str(d).replace(str(HOME), "~"),
                "desc": get_desc(d),
                "files": count_files(d),
                "git": "✅" if git["remote"] or git["last"] != "-" else "—",
                "remote": git["remote"] or "",
                "last": git["last"],
                "canonical": CANONICAL.get(name, ""),
            })
    return items


def render(items: list) -> str:
    now = datetime.now().strftime("%Y-%m-%d")
    active = sorted([i for i in items if i["git"] == "✅"], key=lambda x: x["last"], reverse=True)
    local = sorted([i for i in items if i["git"] != "✅"], key=lambda x: x["name"])

    lines = [
        "---",
        f"title: 프로젝트 레지스트리 (전체 폴더 현황)",
        f"created: {now}",
        f"updated: {now}",
        "type: projects",
        "tags: [registry, projects, folder-map, 중복방지]",
        "links: [[index]]",
        "---",
        "",
        "# 프로젝트 레지스트리 — 전체 폴더 현황",
        "",
        f"> **목적:** 새 코딩 작업 시작 전 반드시 이 문서를 확인해 폴더 중복 생성과 위치 혼란을 방지한다.",
        f"> 자동 생성: `python3 ~/wiki/scripts/generate_project_registry.py` (갱신 시 재실행)",
        f"> Last updated: {now}",
        "",
        "## 규칙 (중복 방지)",
        "",
        "- ❌ 같은 역할의 폴더가 이미 있으면 새로 만들지 말 것 (아래 목록에서 유사 항목 검색)",
        "- ❌ 프로젝트 폴더 위치: `~/projects/` 통일 (개인 사이트 포함, 2026-08-09 justfly32.github.io 이동 완료)",
        "- ✅ 새 프로젝트는 `~/projects/<kebab-case>` 로 생성 후 이 문서를 갱신",
        "- ✅ 비슷한 게 보이면 기존 폴더 확장 또는 이 문서에 병합/분리 사유 기록",
        "- ✅ 중복 그룹에서 **✅ 정본**만 운영, 비정본은 삭제 (2026-08-09 3개 그룹 7개 폴더 휴지통 이동 완료)",
        "",
        "## 정본 표시",
        "",
        "- **✅ 정본** = 운영 중인 최신 폴더 (새 작업은 여기서 진행)",
        "- **🗑️ 삭제된 비정본** = 구버전/빈 껍데기 → `~/.Trash/hermes-removed-20260809/` 보관 (아래 목록 참조)",
        "",
        "## 🟢 Git 프로젝트 (배포/히스토리 있음)",
        "",
        "| 폴더 | 설명 | remote | 최근 커밋 |",
        "|------|------|--------|----------|",
    ]
    for i in active:
        desc = clean_cell(i["desc"] or "-")
        badge = "✅" if i["canonical"] and not i["canonical"].startswith("NON") else ("⚠️" if i["canonical"] else " ")
        lines.append(f"| `{badge} {i['name']}` | {desc} | {i['remote'] or '-'} | {i['last']} |")

    lines += ["", "## 📦 로컬 전용 (git 없음)", "", "| 폴더 | 설명 | 파일 수 |", "|------|------|--------|"]
    for i in local:
        desc = clean_cell(i["desc"] or "-")
        badge = "✅" if i["canonical"] and not i["canonical"].startswith("NON") else ("⚠️" if i["canonical"] else " ")
        lines.append(f"| `{badge} {i['name']}` | {desc} | {i['files']} |")

    lines += [
        "",
        "## 정본/비정본 상세 (2026-08-09 확정 — 최신 것이 정본)",
        "",
        "| 폴더 | 상태 | 근거 |",
        "|------|------|------|",
    ]
    for i in sorted(items, key=lambda x: x["name"]):
        if i["canonical"]:
            badge = "✅ 정본" if not i["canonical"].startswith("NON") else "⚠️ 비정본"
            lines.append(f"| `{i['name']}` | {badge} | {clean_cell(i['canonical'])} |")

    lines += [
        "",
        "## 중복 유사 후보 (확인 필요)",
        "",
        "아래 이름이 비슷한 그룹은 병합/보존 판단이 필요할 수 있다.",
        "",
    ]
    groups = {
        "PPT/문서": ["html2pptx", "PPT_Generator"],
        "개인 사이트": ["personal-site", "post1", "justfly32.github.io"],
    }
    for gname, members in groups.items():
        exist = [m for m in members if any(i["name"] == m for i in items)]
        if len(exist) >= 2:
            lines.append(f"- **{gname}**: {', '.join(f'`{m}`' for m in exist)}")

    lines += ["", "## 🗑️ 삭제된 비정본 (2026-08-09)", "", "| 폴더 | 사유 |", "|------|------|"]
    for name, reason in sorted(REMOVED.items()):
        lines.append(f"| `{name}` | {clean_cell(reason)} |")
    lines.append("")
    lines.append("> 보존 위치: `~/.Trash/hermes-removed-20260809/` (복구 가능)")

    lines += ["", "## 관련", "", "- [[personal-sites]] — 개인 사이트 3개 폴더 상세", "- [[index]]", ""]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true")
    args = ap.parse_args()

    items = scan()
    md = render(items)
    if args.dry:
        print(md)
        return
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(md, encoding="utf-8")
    n_git = sum(1 for i in items if i["git"] == "✅")
    print(f"✅ 레지스트리 생성: {OUTPUT}")
    print(f"   총 {len(items)}개 폴더 (git {n_git}개 / 로컬 {len(items)-n_git}개)")


if __name__ == "__main__":
    main()
