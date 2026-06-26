---
title: CLAUDE.md
created: 2026-06-01
updated: 2026-06-01
type: concept
tags: [ai-ml, programming, research]
sources: [raw/local/ai-ml/projects-claude-2026-06-01.md]
source_file: /Users/bearj/projects/CLAUDE.md
confidence: high
links: [[projects-aider-chat-history|aider 채팅 이력]], [[docs-hermes_beginner_guide|Hermes 초보자 가이드]]
---

# CLAUDE.md

> 📁 원본: `/Users/bearj/projects/CLAUDE.md`
> 📅 수집: 2026-06-01
> 🏷️ 카테고리: ai-ml

## 내용

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Shared Core Policy (Read First)

Before applying repository conventions, read:

- `docs/ai/core-principles.md` (single source of truth shared across Claude and Cursor)

Claude-specific behavior should stay in this file and `.claude/`, while shared policy belongs in `docs/ai/core-principles.md`.

## Repository Overview

This is a best practices repository for Claude Code configuration, demonstrating patterns for skills, subagents, hooks, and commands. It serves as a reference implementation rather than an application codebase.

## Key Components

### Weather System (Example Workflow)
A demonstration of two distinct skill patterns via the **Command → Agent → Skill** architecture:
- `/weather-orchestrator` command (`.claude/commands/weather-orchestrator.md`): Entry point — asks user for C/F, invokes agent, then invokes SVG skill
- `weather-agent` agent (`.claude/agents/weather-agent.md`): Fetches temperature using its preloaded `weather-fetcher` skill (agent skill pattern)
- `weather-fetcher` skill (`.claude/skills/weather-fetcher/SKILL.md`): Preloaded into agent — instructions for fetching temperature from Open-Meteo
- `weather-svg-creator` skill (`.claude/skills/weather-svg-creator/SKILL.md`): Skill — creates SVG weather card, writes `orchestration-workflow/weather.svg` and `orchestration-workflow/output.md`

Two skill patterns: agent skills (preloaded via `skills:` field) vs skills (invoked via `Skill` tool). See `orchestration-workflow/orchestration-workflow.md` for the complete flow diagram.

### Skill Definition Structure
Skills in `.claude/skills/ /SKILL.md` use YAML frontmatter:
- `name`: Display name and `/slash-command` (defaults to directory name)
- `description`: When to invoke (recommended for auto-discovery)
- `argument-hint`: Autocomplete hint (e.g., `[issue-number]`)
- `disable-model-invocation`: Set `true` to prevent automatic invocation
- `user-invocable`: Set `false` to hide from `/` menu (background knowledge only)
- `allowed-tools`: Tools allowed without permission prompts when skill is active
- `model`: Model to use when skill is active
- `context`: Set to `fork` to run in isolated subagent context
- `agent`: Subagent type for `context: fork` (default: `general-purpose`)
- `hooks`: Lifecycle hooks scoped to this skill

### Presentation System
See `.claude/rules/presentation.md` — presentation work is delegated per-presentation to `presentation-vibe-coding` (for `presentation/vibe-coding-to-agentic-engineering/`) or `presentation-claude-gemini` (for `presentation/2026-04-25-gdg-kolachi-cli-claude-code-gemini/`).

### Hooks System
Cross-platform sound notification system in `.claude/hooks/`:
- `scripts/hooks.py`: Main handler for Claude Code hook events
- `config/hooks-config.json`: Shared team configuration
- `config/hooks-config.local.json`: Personal overrides (git-ignored)
- `sounds/`: Audio files organized b

...(내용 생략)...
