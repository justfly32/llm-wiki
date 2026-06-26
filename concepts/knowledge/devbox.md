---
title: devbox - Claude Code의 CPU
created: 2026-06-13
updated: 2026-06-13
type: knowledge
tags: [devbox, claude-code, gcp, infrastructure, tmux]
links: [[docs-guide|Hermes Agent 가이드]]
---

# devbox - 내 Claude Code의 'CPU'

> 항상 켜진 중앙 실행 거점. 로컬 PC는 단말기, 실제 실행은 GCP VM에서.

## 왜 만들었나

Claude Code를 로컬 PC에서 돌리면 작업이 해당 PC에 묶인다:
- PC가 켜져 있고, 슬립 안 하고, 재부팅 안 해야 함
- 5시간 작업 중 Sonnet이 rate limit에 걸리거나 멈추면 세션이 자동 복구 안 됨
- `claude --resume`는 로컬 CLI 기능이라 맥북에서만 동작

**해결:** 항상 켜진 VM에서 tmux 세션으로 실행. PC는 리모트 컨트롤러.

## 주요 기능

| 기능 | 설명 |
|------|------|
| 상시 실행 거점 | 코드는 항상 켜진 devbox VM에서 실행. PC는 단말기 |
| 어디서나 이어받기 | `claude.ai/code` (Remote Control)로 원격 접속 |
| 프로젝트별 격리 | tmux 세션 + Claude 인스턴스 + 전용 git worktree |
| 부팅 자동 동기화 | systemd user + linger로 서버 재부팅 후에도 세션 유지 |
| 사용량 한도 가드레일 | 5시간 자동 종료, 재시작 시 자동 복구, Discord 알림 |
| 세션 인계 커맨드 | `/wip`, `/next` 등으로 세션 상태 저장/복원 |
| 워크트리 자동 정리 | Remote Control이 4개 격리 worktree 자동 생성 |
| 닫힌 네트워크 | Tailscale만 허용, 공개 접근 0 |
| repo = VM 정의 | terraform + setup.sh + sync.sh로 VM 재현 가능 |

## 상태 (2026-06-10)

- 안정적 사용 중
- Phase 0-2 테스트 완료
- Remote Control 환경 구축 완료
- tmux로 세션 그룹핑

## 관련 문서

- `docs/architecture.md` — 아키텍처 상세
- `docs/open-items-runbook.md` — 운영 런북
