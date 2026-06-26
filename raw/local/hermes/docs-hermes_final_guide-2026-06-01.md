---
source_file: /Users/bearj/projects/hermes_ops/docs/hermes_final_guide.md
ingested: 2026-06-01
sha256: 1682e0e0dffc
category: hermes
original_title: 🛡️ Hermes Agent 초보자 완벽 가이드
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

> 매 대화 턴마다 컨텍스트에 주입 → 에이전트가 점점 더 잘 이해

---

## Skills System — 절차적 기억

에이전트가 경험을 통해 **재사용 가능한 스킬**을 생성하고 개선

```bash
hermes skills list       # 사용 가능한 스킬 목록
hermes skills view NAME  # 특정 스킬 내용 보기
```

---

## MCP Integration

Model Context Protocol(MCP) 서버를 연결하여 Hermes의 기능을 안전하게 확장

- MCP 서버의 도구를 필터링
- stdio 또는 HTTP를 통해 연결

---

# 05. 초보자 필수 명령어 모음

| 명령어 | 설명 |
|--------|------|
| `hermes setup` | 초기 설정 마법사 실행 |
| `hermes model` | 사용할 AI 모델 선택 및 설정 |
| `hermes config [set\|edit\|check]` | 설정 확인 및 변경 |
| `hermes postinstall` | 의존성 설치 + 초기 설정 한 번에 |
| `hermes gateway setup` | Telegram/Discord/Slack 등 메신저 연동 |
| `hermes skills list` | 사용 가능한 스킬 목록 표시 |
| `hermes tools` | 현재 활성화된 도구 목록 표시 |
| `hermes --version` | 설치된 Hermes 버전 확인 |

---

# 06. 자주 묻는 질문 (FAQ)

## Q: "hermes: command not found" 오류

**A:** 설치 후 터미널을 재시작하지 않은 경우입니다. 터미널을 완전히 종료했다가 다시 열어보세요. 그래도 안 되면 `source ~/.bashrc` 또는 `source ~/.zshrc`를 실행하세요.

---

## Q: 설치 후 대화가 전혀 작동하지 않아요

**A:** `hermes setup`을 실행하여 API 키와 Provider가 제대로 설정되었는지 확인하세요. `hermes config`로 현재 설정을 확인할 수 있습니다.

---

## Q: Windows에서 PowerShell 설치가 실패해요

**A:** Windows 네이티브 지원은 초기 베타입니다. 가장 안정적인 방법은 **WSL2**를 설치한 후, Linux 설치 방법(curl)을 사용하는 것입니다.

---

## Q: API 키는 어디에 저장되나요?

**A:** `~/.hermes/.env` 파일에 저장됩니다. `hermes config set PROVIDER_API_KEY 값` 명령어를 사용하면 자동으로 올바른 위치에 저장됩니다.

---

# 07. 메신저 연동 (Gateway)

## 지원 플랫폼

| 플랫폼 | 상태 |
|--------|------|
| Telegram | ✅ |
| Discord | ✅ |
| Slack | ✅ |
| WhatsApp | ✅ |
| Signal | ✅ |
| Matrix | ✅ |
| Email | ✅ |
| SMS | ✅ |

---

## Telegram 연동

### 필수 준비 사항
1. 스마트폰에 Telegram 앱 설치
2. @BotFather를 통해 봇 생성 및 토큰 획득

### 단계별 설정
1. **봇 생성**: @BotFather → `/newbot` → 이름/사용자명 입력 → 토큰 획득
2. **토큰 입력**: `hermes gateway setup` → Telegram 선택 → 토큰 입력
3. **테스트**: 봇을 찾아 `/start` → 응답하면 성공!

> 💡 그룹 채팅에서도 사용 가능 (@봇이름으로 호출)

---

## Slack 연동

### 필수 준비 사항
1. Slack 워크스페이스 관리자 권한
2. Slack 앱 생성 권한

### 단계별 설정
1. **앱 생성**: https://api.slack.com/apps → "Create New App" → "From scratch"
2. **권한 설정**: OAuth & Permissions에서 Bot Token Scopes 추가:
   - `channels:read`, `channels:history`, `chat:write`
   - `groups:read`, `im:read`, `mpim:read`
3. **앱 설치**: "Install to Workspace" 클릭
4. **토큰 복사**: `xoxb-`로 시작하는 Bot User OAuth Token
5. **Hermes 설정**: `hermes gateway setup` → Slack 선택 → 토큰 입력
6. **이벤트 구독**: Event Subscriptions 활성화 → bot events 구독
7. **테스트**: DM 또는 @언급 → 응답하면 성공!

---

## 일반적인 문제 해결

| 문제 | 해결 |
|------|------|
| 토큰 오류 | 토큰 재복사 (공백/줄바꿈 없이) |
| 방화벽/프록시 | 서버 인터넷 연결 확인 |
| 플랫폼 문제 | 봇 비활성화/삭제 여부 확인 |
| 로그 확인 | `hermes logs gateway` |

> 💡 처음에는 간단한 **polling 방식**을 먼저 시도하세요.

---

# 08. 업데이트 및 제거

## 업데이트

```bash
# git 기반 설치의 경우
git pull
```

## 제거

설치 스크립트가 생성한 디렉토리를 삭제하고 PATH에서 제거

> 📖 자세한 내용은 공식 문서 참조

---

# 🛡️ 시작할 준비 되셨나요?

```bash
hermes chat -q "안녕, 넌 누구야?"
```

**Hermes Agent와 함께 자동화의 세계로!**

---

> 본 가이드는 Hermes Agent 공식 문서를 기반으로 작성되었습니다.
> 최신 정보: https://hermes-agent.nousresearch.com/docs
> GitHub: https://github.com/NousResearch/hermes-agent
