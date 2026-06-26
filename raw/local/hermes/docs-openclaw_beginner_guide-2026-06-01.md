---
source_file: /Users/bearj/projects/hermes_ops/docs/openclaw_beginner_guide.md
ingested: 2026-06-01
sha256: 9e481e3510b7
category: hermes
original_title: 🦞 OpenClaw 초보자 완벽 가이드
---

---
marp: true
theme: default
paginate: true
backgroundColor: #0d1117
color: #c9d1d9
style: |
  section { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans KR', sans-serif; }
  h1 { color: #58a6ff; font-size: 2em; border-bottom: 2px solid #30363d; padding-bottom: 0.5rem; }
  h2 { color: #79c0ff; font-size: 1.4em; border-left: 4px solid #79c0ff; padding-left: 0.8rem; margin-top: 1rem; }
  h3 { color: #3fb950; font-size: 1.1em; }
  h4 { color: #d29922; font-size: 1em; }
  code { background: #1c2128; color: #79c0ff; padding: 2px 6px; border-radius: 4px; font-family: 'SF Mono', 'Fira Code', 'Consolas', monospace; font-size: 0.9em; }
  pre { background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 1rem; color: #e6edf3; font-family: 'SF Mono', 'Fira Code', 'Consolas', monospace; font-size: 0.85em; }
  pre code { background: none; color: inherit; padding: 0; }
  strong { color: #e6edf3; }
  a { color: #79c0ff; }
  table { width: 100%; border-collapse: collapse; }
  th, td { border: 1px solid #30363d; padding: 0.4rem 0.7rem; text-align: left; }
  th { background: #161b22; color: #79c0ff; font-weight: 600; }
  ul, ol { margin-left: 1.2rem; }
  li { margin-bottom: 0.3rem; }
  blockquote { border-left: 4px solid #3fb950; background: #161b22; padding: 0.8rem 1rem; margin: 0.8rem 0; border-radius: 0 8px 8px 0; }
---

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

1. **앱 생성:** Discord Developer Portal → New Application
2. **Bot 토큰:** Bot → Reset Token → 복사
3. **Intent 활성화:** Message Content Intent ON
4. **토큰 입력:**
   ```bash
   openclaw channels add discord --token YOUR_BOT_TOKEN
   ```
5. **봇 초대:** OAuth2 URL로 서버에 초대
6. **테스트:** 채널에 메시지 → 응답하면 성공!

---

## Slack & WhatsApp

### Slack
1. Slack API에서 앱 생성
2. Bot Token Scopes 추가 (`channels:read`, `chat:write` 등)
3. Install to Workspace
4. Event Subscriptions 활성화
5. 채널에 봇 초대

### WhatsApp
1. `openclaw channels add whatsapp`
2. QR 코드 생성됨
3. WhatsApp 앱에서 QR 스캔
4. 완료!

> 💡 WhatsApp이 가장 간단 — QR 스캔만으로 완료

---

# 07. FAQ

## Q: "command not found" 오류
**A:** 터미널 재시작 또는 `source ~/.bashrc`

## Q: 대화가 안 됨
**A:** `openclaw onboard`으로 API 키 확인

## Q: 여러 메신저 동시 사용?
**A:** ✅ 하나의 게이트웨이로 여러 채널 동시 서비스

## Q: 데이터는 어디에?
**A:** 자신의 서버에 저장 — 셀프-호스팅

## Q: 무료인가요?
**A:** OpenClaw는 무료(MIT). API 사용료만 별도

---

# 08. OpenClaw vs Hermes Agent

| 항목 | OpenClaw | Hermes Agent |
|------|----------|-------------|
| 유형 | 메신저 게이트웨이 | AI 에이전트 프레임워크 |
| 핵심 | 메신저 ↔ AI 연결 | 자율 작업 수행 |
| 셀프-호스팅 | ✅ | ✅ |
| 오픈소스 | ✅ (MIT) | ✅ (MIT) |
| 스킬 | ClawHub | Skills |
| 메모리 | 세션 기반 | 영구 메모리 |

> 💡 함께 사용 가능: OpenClaw(메신저) + Hermes(작업 처리)

---

# 09. 업데이트 및 제거

## 업데이트

```bash
# npm
npm update -g openclaw

# 소스
cd ~/.openclaw && git pull
```

## 제거

```bash
npm uninstall -g openclaw
rm -rf ~/.openclaw  # 설정 파일 삭제
```

---

# 🦞 시작할 준비 되셨나요?

```bash
openclaw onboard
```

**OpenClaw로 어디서든 AI 비서와 대화하세요!**

---

> 📖 공식 문서: https://docs.openclaw.ai
> 💻 GitHub: https://github.com/openclaw-ai/openclaw
