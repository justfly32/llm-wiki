---
source_file: /Users/bearj/projects/hermes_ops/docs/hermes_beginner_guide.md
ingested: 2026-06-01
sha256: 3237ae69dcc8
category: hermes
original_title: 🐾 Hermes Agent
---

---
marp: true
theme: default
paginate: true
backgroundColor: #1a1a2e
color: #eaeaea
style: |
  section { font-family: 'Pretendard', 'Noto Sans KR', sans-serif; }
  h1 { color: #e94560; font-size: 2.2em; }
  h2 { color: #0f3460; background: #e94560; padding: 8px 16px; border-radius: 8px; }
  h3 { color: #e94560; }
  code { background: #16213e; padding: 2px 6px; border-radius: 4px; }
  pre { background: #16213e; padding: 16px; border-radius: 8px; }
---

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

> 💡 **게이트웨이**란? 메신저 플랫폼과 Hermes를 연결하는 다리 역할

---

# 06. 스킬 시스템

## 스킬이란?

에이전트의 **절차적 메모리**

- 반복 작업의 노하우를 저장한 문서
- 스킬을 설치하면 에이전트가 해당 작업을 더 잘 수행
- 사용자 정의 스킬 생성 가능

> 💡 **절차적 메모리**란? "어떻게 하는지"에 대한 기억 (vs 사실적 메모리)

---

## 스킬 관리

```bash
hermes skills list              # 설치된 스킬 목록
hermes skills search weather   # 허브에서 검색
hermes skills install weather  # 스킬 설치
hermes skills update           # 업데이트
hermes skills browse           # 전체 탐색
```

---

## 세션에서 스킬 사용

```
/skill weather
```

→ 현재 세션에 스킬 로드

## 유용한 스킬 예시

| 스킬 | 기능 |
|------|------|
| `weather` | 날씨 확인 |
| `claude-design` | HTML 디자인 아티팩트 제작 |
| `github-pr-workflow` | GitHub PR 워크플로우 |
| `spotify` | Spotify 제어 |
| `notion` | Notion 페이지 관리 |

---

# 07. 크론 & 자동화

## 크론 잡 생성

```bash
# 30분마다
hermes cron create "30m"

# 매일 오전 9시
hermes cron create "0 9 * * *"

# 매주 월요일 오전 10시
hermes cron create "0 10 * * 1"

# 특정 날짜/시간
hermes cron create "2026-01-15T09:00:00"
```

> 💡 **크론 표현식**: `분 시 일 월 요일` 순서

---

## 크론 관리

```bash
hermes cron list      # 목록
hermes cron pause ID  # 일시정지
hermes cron resume ID # 재개
hermes cron run ID    # 즉시 실행
hermes cron remove ID # 삭제
```

---

## 자동화 예시

### 매일 메모리 → Notion 동기화

```bash
hermes cron create "0 0 * * *" \
  --name "Daily Memory to Notion" \
  --script "daily_memory_to_notion.py" \
  --no-agent
```

### 매시간 서버 상태 체크

```bash
hermes cron create "1h" \
  --name "Server Health Check" \
  --prompt "서버 상태를 확인하고 이상이 있으면 알려줘"
```

---

# 08. 다중 에이전트

## 서브에이전트 위임

에이전트가 자동으로 `delegate_task`를 호출하여 병렬 작업 수행

```
"백엔드 API 만들어줘" → 에이전트가 자동으로 여러 서브에이전트 생성
```

## 독립 에이전트 실행

```bash
# 일회성 작업
hermes chat -q "FastAPI 인증 서비스 구축"

# 백그라운드 (tmux)
tmux new-session -d -s agent1 'hermes'
tmux send-keys -t agent1 '작업 지시' Enter
```

---

## 멀티 에이전트 조율

```bash
# 백엔드 에이전트
tmux new-session -d -s backend 'hermes -w'
tmux send-keys -t backend 'REST API 구축' Enter

# 프론트엔드 에이전트
tmux new-session -d -s frontend 'hermes -w'
tmux send-keys -t frontend 'React 대시보드 구축' Enter
```

> 💡 `-w` (worktree 모드)로 git 충돌 방지

---

# 09. 문제 해결

## 자주 묻는 문제 ①

| 증상 | 해결 |
|------|------|
| 도구가 안 보임 | `hermes tools` → 활성화 → `/reset` |
| 모델 오류 | `hermes doctor` → API 키 확인 |
| 게이트웨이 다운 | `hermes gateway restart` |

## 자주 묻는 문제 ②

| 증상 | 해결 |
|------|------|
| 스킬 미표시 | `hermes skills config` → 플랫폼 확인 |
| 변경 미반영 | `/reset` 또는 재시작 |
| 음성 안 됨 | `stt.enabled: true` 확인 |

---

## 로그 & 디버그

```bash
# 게이트웨이 로그 확인
tail -20 ~/.hermes/logs/gateway.log
```

```
/debug
```

→ 시스템 정보 + 로그를 공유 가능한 링크로 업로드

## 주요 경로

| 파일 | 경로 |
|------|------|
| 설정 | `~/.hermes/config.yaml` |
| API 키 | `~/.hermes/.env` |
| 로그 | `~/.hermes/logs/` |
| 세션 | `~/.hermes/sessions/` |
| 스킬 | `~/.hermes/skills/` |

---

# 09-1. 프로필 관리

## 프로필이란?

독립된 Hermes 인스턴스 — 설정, 세션, 스킬, 메모리가 분리됨

```bash
# 프로필 생성
hermes profile create work
hermes profile create personal

# 프로필 전환
hermes profile use work

# 프로필 목록
hermes profile list
```

> 💡 용도별로 프로필을 나누면 맥락 혼방을 방지할 수 있습니다.

---

# 09-2. 보안 설정

## 명령 승인 모드

```bash
# 수동 승인 (기본 — 안전)
hermes config set approvals.mode manual

# 스마트 승인 (LLM이 판단)
hermes config set approvals.mode smart

# 승인 생략 (위험 — 비추천)
hermes config set approvals.mode off
```

## 시크릿 자동 마스킹

```bash
# API 키 등 민감 정보 자동 마스킹
hermes config set security.redact_secrets true
```

> ⚠️ 변경 후 새 세션(`/reset`)을 시작해야 적용됩니다.

---

# 09-3. 토큰 최적화

## 토큰이란?

LLM이 처리하는 텍스트 단위. 세션 내 대화가 길어지면 토큰이 많이 소모됩니다.

## 절약 설정

```bash
# 응답 길이 압축
hermes config set model.use_fewer_words true
hermes config set model.keep_new_words_at_end true

# 메모리 제한
hermes config set memory.memory_char_limit 1200
hermes config set memory.user_char_limit 800

# 온도 낮게 (일관된 응답)
hermes config set model.temperature 0.2
```

> 💡 토큰을 아끼면 비용 절감 + 긴 대화 가능

---

# 09-4. 음성 기능 (STT/TTS)

## 음성 → 텍스트 (STT)

```bash
# 로컬 Whisper (무료)
pip install faster-whisper

# 설정
hermes config set stt.enabled true
hermes config set stt.provider local
```

## 텍스트 → 음성 (TTS)

| 제공자 | 비용 |
|--------|------|
| Edge TTS | 무료 |
| ElevenLabs | 무료 티어 |
| OpenAI | 유료 |

```
/voice on      # 음성 대화 모드
/voice tts     # 항상 음성 출력
/voice off     # 음성 끄기
```

---

# 10. 다음 단계

## 학습 경로

1. ✅ 설치 & 기본 실행
2. 🔄 메신저 연동 (Telegram/Slack)
3. 📦 스킬 탐색 & 설치
4. ⏰ 크론 자동화 구성
5. 🤖 다중 에이전트 워크플로우
6. 🛠️ 커스텀 스킬 작성

---

## 유용한 링크

| 리소스 | 링크 |
|--------|------|
| 📖 공식 문서 | https://hermes-agent.nousresearch.com/docs |
| 💻 GitHub | https://github.com/NousResearch/hermes-agent |
| 🌐 스킬 허브 | `hermes skills browse` |

---

# 🐾 시작할 준비 되셨나요?

```bash
hermes chat -q "안녕, 넌 누구야?"
```

**Hermes Agent와 함께 자동화의 세계로!**
