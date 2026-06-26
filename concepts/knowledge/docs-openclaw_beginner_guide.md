---
title: 🦞 OpenClaw 초보자 완벽 가이드
created: 2026-06-01
updated: 2026-06-13
type: concept
tags: [hermes, ai-ml, tool, devops, api]
sources: [raw/local/hermes/docs-openclaw_beginner_guide-2026-06-01.md]
source_file: /Users/bearj/projects/hermes_ops/docs/openclaw_beginner_guide.md
confidence: high
links: [[docs-hermes_beginner_guide|Hermes 초보자 가이드]], [[docs-hermes_final_guide|Hermes 완벽 가이드]], [[docs-guide|Hermes 설치 가이드]], [[best-practice-claude-subagents|Claude Subagents 모범 사례]], [[docs-hermes_slides|Hermes 슬라이드]], [[hermes-guide-beginner_guide|Hermes 가이드 문서]]
---

# 🦞 OpenClaw 초보자 완벽 가이드

> 관련: [[docs-hermes_beginner_guide|Hermes 초보자 가이드]], [[docs-hermes_final_guide|Hermes 완벽 가이드]]도 참고하세요.

> 📁 원본: `/Users/bearj/projects/hermes_ops/docs/openclaw_beginner_guide.md`
> 📅 수집: 2026-06-01
> 🏷️ 카테고리: hermes

## 내용

# 🦞 OpenClaw 초보자 완벽 가이드

**셀프-호스팅 AI 에이전트 게이트웨이**

---

# 📋 목차

| 순서 | 주제 |
|------|------|
| 01 | 설치 (Installation) |
| 02 | Quickstart — 첫 실행 |
| 03 | 주요 기능 (Features) |
| 04 | 설정 (Configuration) |
| 05 | 필수 명령어 |
| 06 | 채널 연동 가이드 |
| 07 | FAQ |
| 08 | OpenClaw vs Hermes |
| 09 | 업데이트 및 제거 |

---

# 01. 설치 (Installation)

## 사전 요구 사항

- **Node.js** — v24 권장 (v22.16+ 지원)
- **API 키** — Anthropic, OpenAI, Google 등

```bash
# Node 버전 확인
node --version
```

> 💡 Windows는 WSL2 권장

---

## macOS / Linux

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

## Windows (PowerShell)

```powershell
irm https://openclaw.ai/install.ps1 | iex
```

## 기타 설치 방법

- **Docker:** 컨테이너 환경
- **Nix:** Nix 패키지 관리자
- **npm:** `npm install -g openclaw`

---

# 02. Quickstart — 첫 실행

## 핵심 원칙

> 🚨 기본 대화조차 안 되면 다른 기능 추가 금지!
> 먼저 깨끗한 대화 하나를 성공시키세요.

---

## 빠른 설정 4단계

| 단계 | 명령어 | 설명 |
|------|--------|------|
| 1 | `curl -fsSL https://openclaw.ai/install.sh \| bash` | 설치 |
| 2 | `openclaw onboard` | 온보딩 (모델/API키 설정) |
| 3 | `openclaw gateway start` | 게이트웨이 시작 |
| 4 | `openclaw chat` | 대화 시작 |

---

## 목표별 시작 경로

| 목표 | 먼저 할 것 | 그다음 |
|------|-----------|--------|
| 컴퓨터에서 사용 | `openclaw onboard` | 대화 테스트 |
| Provider 알고 있음 | `openclaw onboard` | 설정 후 대화 |
| 메신저 봇 설정 | CLI 확인 | 채널 연동 |
| 로컬 모델 | `openclaw onboard` → 커스텀 | 엔드포인트 확인 |

---

# 03. 주요 기능 (Features)

## 멀티-채널 게이트웨이

하나의 게이트웨이로 여러 메신저 동시 서비스

## 지원 플랫폼

| 플랫폼 | 연동 방법 |
|--------|----------|
| Telegram | 봇 토큰 |
| Discord | Bot 앱 생성 |
| Slack | Slack 앱 생성 |
| WhatsApp | QR 코드 스캔 |
| iMessage | macOS 전용 |
| Signal | Signal CLI |
| Matrix | 홈서버 설정 |
| Teams | Azure 앱 등록 |

---

## 에이전트 시스템

- **세션 관리:** 대화 맥락 유지
- **도구 사용:** 파일, 터미널, 브라우저
- **메모리:** 세션 간 정보 기억
- **멀티 에이전트 라우팅:** 작업별 에이전트 분배

## ClawHub — 스토어

```bash
openclaw hub search [검색어]
openclaw hub install [패키지명]
```

---

# 04. 설정 (Configuration)

## 디렉토리 구조

```
~/.openclaw/
├── config.yaml       # 메인 설정
├── .env              # API 키
├── agents/           # 에이전트 설정
├── channels/         # 채널 연동
├── sessions/         # 대화 세션
└── logs/             # 로그
```

---

## 설정 관리

```bash
openclaw config              # 설정 보기
openclaw config edit         # 편집
openclaw config set KEY VAL  # 값 설정
```

## 설정 예시

```bash
openclaw config set model anthropic/claude-opus-4
openclaw config set ANTHROPIC_API_KEY sk-ant-...
```

> 💡 API 키는 `.env`, 나머지는 `config.yaml`에 자동 저장

---

# 05. 필수 명령어 모음

| 명령어 | 설명 |
|--------|------|
| `openclaw onboard` | 초기 설정 마법사 |
| `openclaw gateway start` | 게이트웨이 시작 |
| `openclaw gateway stop` | 게이트웨이 중지 |
| `openclaw gateway status` | 상태 확인 |
| `openclaw chat` | 대화 모드 |
| `openclaw channels list` | 채널 목록 |
| `openclaw agents list` | 에이전트 목록 |
| `openclaw --version` | 버전 확인 |

---

# 06. 채널 연동 — Telegram

## 단계별 설정

1. **봇 생성:** @BotFather → `/newbot` → 이름/사용자명 → 토큰 획득
2. **토큰 입력:**
   ```bash
   openclaw channels add telegram --token YOUR_BOT_TOKEN
   ```
3. **테스트:** 봇에게 `/start` → 응답하면 성공!

> 💡 그룹에서도 사용 가능 (@봇이름으로 호출)

---

## Discord 연동


...(내용 생략)...
