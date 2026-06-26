---
title: 🛡️ Hermes Agent 초보자 완벽 가이드
created: 2026-06-01
updated: 2026-06-13
type: concept
tags: [hermes, ai-ml, tool, python, devops]
sources: [raw/local/hermes/docs-hermes_final_guide-2026-06-01.md]
source_file: /Users/bearj/projects/hermes_ops/docs/hermes_final_guide.md
confidence: high
links: [[docs-hermes_beginner_guide|Hermes 초보자 가이드]], [[docs-hermes_slides|Hermes 슬라이드]], [[docs-guide|Hermes 설치 가이드]], [[docs-openclaw_beginner_guide|OpenClaw 가이드]], [[best-practice-claude-subagents|Claude Subagents 모범 사례]], [[hermes-guide-beginner_guide|Hermes 가이드 문서]]
---

# 🛡️ Hermes Agent 초보자 완벽 가이드

> 관련: [[docs-hermes_beginner_guide|초보자 가이드]], [[docs-hermes_slides|슬라이드 가이드]], [[docs-openclaw_beginner_guide|OpenClaw 가이드]]도 참고하세요.

> 📁 원본: `/Users/bearj/projects/hermes_ops/docs/hermes_final_guide.md`
> 📅 수집: 2026-06-01
> 🏷️ 카테고리: hermes

## 내용

# 🛡️ Hermes Agent 초보자 완벽 가이드

**Nous Research** | 자기-학습형 AI 에이전트

---

# 📋 목차

| 순서 | 주제 |
|------|------|
| 01 | 설치 (Installation) |
| 02 | Quickstart — 첫 실행 |
| 03 | Configuration — 설정 가이드 |
| 04 | 주요 기능 (Features) |
| 05 | 초보자 필수 명령어 |
| 06 | FAQ |
| 07 | 메신저 연동 (Gateway) |
| 08 | 업데이트 및 제거 |

---

# 01. 설치 (Installation)

## Linux / macOS / WSL2 (권장)

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

> 💡 **Tip**: Android(Termux)에서도 동일한 명령어 사용 가능

---

## Windows (PowerShell) — 초기 베타

```powershell
irm https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1 | iex
```

설치 프로그램이 자동 처리:
- `uv` — Python 패키지 관리자
- **Python 3.11** + **Node.js 22**
- `ripgrep`, `ffmpeg`, **PortableGit**

> ⚠️ **중요**: 설치 후 반드시 **터미널을 재시작**해야 `hermes` 명령어가 PATH에 등록됩니다.

---

## 설치 후 확인

```bash
hermes --version
```

추가 의존성 설치 + 초기 설정:

```bash
hermes postinstall
```

---

# 02. Quickstart — 첫 실행

## 핵심 원칙: Rule of Thumb

> 🚨 **가장 중요한 규칙**: Hermes가 **기본적인 대화조차 완료하지 못한다면**, 다른 기능(Gateway, Cron, Skills 등)을 절대 추가하지 마세요. 먼저 깨끗한 대화 하나를 성공시키세요.

---

## 목표별 시작 경로

| 목표 | 먼저 할 것 | 그다음 할 것 |
|------|-----------|-------------|
| 내 컴퓨터에서 사용 | `hermes setup` | 실제 대화 테스트 |
| Provider를 알고 있음 | `hermes model` | 설정 저장 후 대화 |
| 봇/상시 가동 설정 | CLI 작동 확인 | `hermes gateway setup` |
| 로컬 모델 사용 | `hermes model` → 커스텀 엔드포인트 | 엔드포인트 확인 |
| 멀티 Provider 폴백 | `hermes model` 먼저 | 대화 성공 후 라우팅 |

---

## 누구를 위한 가이드인가?

- Hermes를 처음 접하고 가장 빠르게 작동시키고 싶은 분
- Provider 변경 중이고 설정 실수로 시간 낭비하고 싶지 않은 분
- 팀, 봇, 상시 가동 워크플로우를 위해 설정 중인 분
- "설치는 됐는데 아무것도 안 돼요"에 지친 분

---

# 03. Configuration — 설정 가이드

## 디렉토리 구조

```
~/.hermes/
├── config.yaml     # 설정 (모델, 터미널, TTS, 압축 등)
├── .env            # API 키 및 시크릿
├── auth.json       # OAuth 인증 정보
├── SOUL.md         # 에이전트 정체성
├── memories/       # 영구 메모리
├── skills/         # 에이전트가 생성한 스킬
├── cron/           # 예약된 작업
├── sessions/       # 게이트웨이 세션
└── logs/           # 로그
```

---

## 설정 관리 명령어

```bash
hermes config              # 현재 설정 보기
hermes config edit         # config.yaml을 편집기로 열기
hermes config set KEY VAL  # 특정 값 설정
hermes config check        # 누락된 옵션 확인
hermes config migrate      # 누락된 옵션을 대화형으로 추가
```

---

## 설정 예시

```bash
hermes config set model anthropic/claude-opus-4
hermes config set terminal.backend docker
hermes config set OPENROUTER_API_KEY sk-or-...
```

> 💡 **자동 라우팅**: API 키는 `.env`에, 그 외 설정은 `config.yaml`에 자동 저장

---

## SOUL.md — 에이전트 정체성 설정

`~/.hermes/SOUL.md` 파일은 에이전트의 **성격, 말투, 행동 방식**을 정의

```
너는 따뜻하고 친절한 비서야. 항상 한국어로 답변하고,
사용자를 '고객님'이라고 불러줘.
불필요한 기술 용어는 피하고, 항상 차근차근 설명해.
```

---

# 04. 주요 기능 (Features)

## Tools & Toolsets — 70개 이상의 내장 도구

- **Core**: 터미널, 파일 읽기/쓰기, 검색, 패치
- **Automation**: 브라우저, 크론잡, 위임 작업
- **Media & Web**: 이미지 분석, 웹 검색, 비디오
- **Management**: 메모리, 스킬 관리, 세션 검색
- **Advanced**: MCP, 코드 실행, 음성(TTS)

---

## Memory System — 영구 메모리

- **USER.md**: 사용자에 대한 정보 (이름, 선호도, 시간대 등)
- **MEMORY.md**: 환경, 프로젝트 규칙, 도구 특이사항 등

> 매 대화 턴마다 컨텍스트에 

...(내용 생략)...
