---
title: Claude Code Subagents Best Practices
created: 2026-06-01
updated: 2026-06-13
type: concept
tags: [ai-ml, programming, research]
sources: [raw/local/ai-ml/best-practice-claude-subagents-2026-06-01.md]
source_file: /Users/bearj/projects/best-practice/claude-subagents.md
confidence: high
links: [[agents-weather-agent|Weather Agent]], [[commands-weather-orchestrator|Weather Orchestrator 명령어]], [[projects-claude|CLAUDE.md]], [[rules-presentation|발표 규칙]], [[docs-hermes_beginner_guide|Hermes 초보자 가이드]], [[docs-openclaw_beginner_guide|OpenClaw 가이드]]
---

# Claude Code Subagents Best Practices

> 관련: [[agents-weather-agent|Weather Agent]], [[projects-claude|CLAUDE.md]], [[rules-presentation|프레젠테이션 규칙]]도 참고하세요.

> 📁 원본: `/Users/bearj/projects/best-practice/claude-subagents.md`
> 📅 수집: 2026-06-01
> 🏷️ 카테고리: ai-ml

## 내용

# Claude Code Subagents Best Practices

This document provides best practices for creating and using subagents in Claude Code.

## Shared Policy First

Before applying repository-wide workflow or collaboration rules, read:

- `docs/ai/core-principles.md`

This document focuses on Claude-specific subagent design and runnable examples.

## Subagent Definition Structure

Subagents are defined in `.claude/agents/*.md` files with YAML frontmatter:

```yaml
name: agent-name
description: When to invoke (use "PROACTIVELY" for auto-invocation)
tools: Comma-separated allowlist of tools (inherits all if omitted). Supports Agent(agent_type) syntax
disallowedTools: Tools to deny, removed from inherited or specified list
model: Model alias: haiku, sonnet, opus, or inherit (default: inherit)
permissionMode: Permission mode (e.g., "acceptEdits", "plan", "bypassPermissions")
maxTurns: Maximum agentic turns before the subagent stops
skills: List of skill names to preload into agent context
mcpServers: MCP servers for this subagent (server names or inline configs)
hooks: Lifecycle hooks scoped to this subagent (all hook events are supported)
memory: Persistent memory scope — user, project, or local
background: Set to true to always run as a background task
effort: Effort level override: low, medium, high, max (default: inherits from session)
isolation: Set to "worktree" to run in a temporary git worktree
color: CLI output color for visual distinction
```

## Claude-Specific Best Practices

### 1. Use Descriptive Names
Choose clear, descriptive names that indicate the agent's purpose:
- `code-reviewer` - for code review tasks
- `test-generator` - for generating unit tests
- `doc-writer` - for documentation creation
- `refactorer` - for code refactoring tasks

### 2. Be Explicit About Tools
List only the tools the agent needs rather than inheriting all tools:
```yaml
tools: Read, Write, Bash, Agent(general-purpose)
```
This prevents the agent from using unnecessary tools that could cause confusion or security issues.

### 3. Preload Relevant Skills
Preload skills that the agent will frequently use:
```yaml
skills:
  - code-analyzer
  - test-creator
  - doc-formatter
```
This reduces the need for explicit skill invocation and makes the agent more efficient.

### 4. Set Appropriate Permission Modes
Choose permission modes based on the agent's risk level:
- `acceptEdits` - for agents that suggest edits requiring user approval
- `plan` - for agents that create plans but don't execute them
- `bypassPermissions` - only for trusted agents with well-understood behavior

### 5. Limit Turns Appropriately
Set `maxTurns` to prevent runaway agents:
- Simple tasks: 3-5 turns
- Moderate tasks: 5-10 turns
- Complex tasks: 10-20 turns (use with caution)

### 6. Use Context Isolation When Needed
For agents that modify files or run commands, consider using:
```yaml
isolation: worktree
```
This runs the agent in a temporary git worktree, preventing accidental changes to the main working

...(내용 생략)...
