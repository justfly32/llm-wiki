---
title: 🐾 Hermes Agent
created: 2026-06-01
updated: 2026-06-13
type: concept
tags: [hermes, ai-ml, tool, api, web]
sources: [raw/local/hermes/docs-hermes_beginner_guide-2026-06-01.md]
source_file: /Users/bearj/projects/hermes_ops/docs/hermes_beginner_guide.md
confidence: high
links: [[docs-hermes_final_guide|Hermes 완벽 가이드]], [[docs-guide|Hermes 설치 가이드]], [[docs-openclaw_beginner_guide|OpenClaw 가이드]], [[hermes-guide-beginner_guide|Hermes 가이드 문서]], [[docs-hermes_slides|Hermes 슬라이드]], [[agents-weather-agent|Weather Agent]]
---

# 🐾 Hermes Agent

> 관련: [[docs-hermes_final_guide|완벽 가이드]], [[docs-guide|설치 가이드]], [[docs-openclaw_beginner_guide|OpenClaw 가이드]]도 참고하세요.

> 📁 원본: `/Users/bearj/projects/hermes_ops/docs/hermes_beginner_guide.md`
> 📅 수집: 2026-06-01
> 🏷️ 카테고리: hermes

## 내용

# 🐾 Hermes Agent
## 설치부터 활용까지 — 초보자 가이드

**Bear J's Hermes Ops** | 2026

---

# 📋 목차

| 순서 | 주제 |
|------|------|
| 01 | Hermes Agent란? |
| 02 | 설치하기 |
| 03 | 첫 실행 & 설정 |
| 04 | 기본 사용법 |
| 05 | 게이트웨이 (메신저 연동) |
| 06 | 스킬 시스템 |
| 07 | 크론 & 자동화 |
| 08 | 다중 에이전트 |
| 09 | 문제 해결 |
| 10 | 다음 단계 |

---

# 01. Hermes Agent란?

## 오픈소스 AI 에이전트 프레임워크

**Nous Research**에서 개발

- 터미널, 메신저, IDE에서 실행
- Claude Code, Codex와 같은 카테고리
- 어떤 LLM 제공자든 사용 가능

> 💡 **LLM**이란? Large Language Model — GPT, Claude, Gemini 같은 대규모 언어 모델

---

## 핵심 차별점 ①

| 기능 | 설명 |
|------|------|
| 🧠 **자기 개선** | 스킬로 경험을 저장, 점점 더 똑똑해짐 |
| 💾 **영구 메모리** | 세션 간 사용자 정보·환경 기억 |
| 🌐 **멀티 플랫폼** | Telegram, Discord, Slack 등 10+ 플랫폼 |

---

## 핵심 차별점 ②

| 기능 | 설명 |
|------|------|
| 🔀 **제공자 독립** | 모델/제공자 자유롭게 교체 |
| 📦 **확장성** | 플러그인, MCP, 웹훅, 크론 |
| 👤 **프로필** | 독립된 설정·세션·스킬 관리 |

> 💡 **MCP**란? Model Context Protocol — 외부 도구 연결 표준
> 💡 **크론**이란? 정해진 시간에 자동으로 작업을 실행하는 스케줄러

---

# 02. 설치하기

## macOS / Linux

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

## 설치 확인

```bash
hermes --version    # 버전 확인
hermes doctor       # 종합 진단
```

---

## Windows

```powershell
# 동일한 설치 스크립트 실행 후
hermes doctor
```

## 설치 후 확인 사항

```bash
hermes doctor
```

✅ 의존성 확인
✅ API 키 확인
✅ 설정 파일 확인

> 💡 **Tip**: 문제가 생기면 가장 먼저 `hermes doctor`를 실행하세요.

---

# 03. 첫 실행 & 설정

## 인터랙티브 채팅 시작

```bash
hermes
```

→ 대화형 프롬프트가 나타납니다. 자유롭게 질문해보세요!

## 설정 마법사

```bash
hermes setup
```

단계별 안내:
1. **모델** 선택 (Claude, GPT, Gemini 등)
2. **터미널** 설정
3. **게이트웨이** 설정
4. **도구** 설정
5. **에이전트** 설정

---

## 모델 선택

```bash
hermes model
```

→ 사용 가능한 모델 목록에서 선택

## API 키 설정

```bash
# ~/.hermes/.env 파일에 저장
OPENROUTER_API_KEY=sk-or-xxxxxxxx
```

> 💡 **API 키**란? 서비스 접근 권한을 부여하는 비밀 문자열

---

# 04. 기본 사용법

## 단일 질문 (비인터랙티브)

```bash
hermes chat -q "프랑스의 수도는?"
hermes chat -q "오늘 날씨 알려줘"
hermes chat -q "이 폴더의 파일 목록 보여줘"
```

## 세션 관리

```bash
hermes sessions list      # 세션 목록
hermes sessions browse    # 인터랙티브 선택
hermes --continue         # 최근 세션 이어하기
hermes --resume 세션ID     # 특정 세션 이어하기
```

> 💡 **세션**이란? 대화의 단위. 각 세션은 독립된 맥락을 가집니다.

---

## 슬래시 명령어 ①

세션 내에서 `/`로 시작하는 특수 명령어

| 명령어 | 기능 |
|--------|------|
| `/new` | 새 세션 시작 |
| `/model` | 모델 변경 |
| `/tools` | 도구 관리 |
| `/skills` | 스킬 검색/설치 |
| `/cron` | 크론 관리 |

---

## 슬래시 명령어 ②

| 명령어 | 기능 |
|--------|------|
| `/help` | 전체 명령어 목록 |
| `/status` | 세션 정보 |
| `/usage` | 토큰 사용량 |
| `/verbose` | 상세 출력 전환 |
| `/yolo` | 위험 명령 승인 생략 |

---

# 05. 게이트웨이 (메신저 연동)

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

## 게이트웨이 설정 & 실행

```bash
# 플랫폼 설정
hermes gateway setup

# 포그라운드 실행
hermes gateway run

# 백그라운드 서비스 등록
hermes gateway install

# 서비스 제어
hermes gateway start
hermes gateway stop
hermes gateway restart
```

---

## 홈 채널 설정

```
/sethome
```

→ 현재 채널을 알림·기본 발송 대상으로 지정

## 연결 상태 확인

```
/platforms
```

→ 모든 플랫폼의 연결 상태를 확인

> 💡 **

...(내용 생략)...
