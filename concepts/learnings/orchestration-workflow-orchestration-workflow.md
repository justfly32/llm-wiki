---
title: Weather System Orchestration Workflow
created: 2026-06-01
updated: 2026-06-01
type: concept
tags: [document, ai-ml]
sources: [raw/local/general/orchestration-workflow-orchestration-workflow-2026-06-01.md]
source_file: /Users/bearj/projects/orchestration-workflow/orchestration-workflow.md
confidence: high
links: [[commands-weather-orchestrator|Weather Orchestrator Command]], [[commands-research-to-ppt|Research to PPT Command]]
---

# Weather System Orchestration Workflow

> 📁 원본: `/Users/bearj/projects/orchestration-workflow/orchestration-workflow.md`
> 📅 수집: 2026-06-01
> 🏷️ 카테고리: general

## 내용

# Weather System Orchestration Workflow

This document illustrates the **Command → Agent → Skill** architecture pattern used in the weather system example.

## Overview
The weather system demonstrates two distinct ways to organize and reuse functionality in Claude Code:

1. **Agent Skills Pattern**: Skills preloaded into an agent context
2. **Direct Skill Invocation Pattern**: Skills invoked directly via the `Skill` tool

## Complete Flow Diagram

```
┌─────────────────────────────┐
│ /weather-orchestrator       │   ← Command (entry point)
│ (.claude/commands/weather-  │
│  orchestrator.md)           │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│ weather-agent               │   ← Agent
│ (.claude/agents/weather-agent.md) │
│  ┌─────────────────────┐    │
│  │ weather-fetcher     │◄───┘│  ← Preloaded skill (agent skill pattern)
│  │ weather-svg-creator │    │  ← Preloaded skill (agent skill pattern)
│  └─────────────────────┘    │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│ weather-svg-creator         │   ← Skill (direct invocation)
│ (.claude/skills/weather-    │
│  svg-creator/SKILL.md)      │  ← Can also be invoked directly
└─────────────────────────────┘
              │
              ▼
┌─────────────────────────────┐
│ Output Files:               │
│ • orchestration-workflow/   │
│   weather.svg               │
│ • orchestration-workflow/   │
│   output.md                 │
└─────────────────────────────┘
```

## Pattern Comparison

### Agent Skills Pattern (Preloaded)
- **Where**: Defined in agent's `skills:` field
- **How**: Automatically available to the agent without explicit invocation
- **Use Case**: Core functionality tightly coupled to the agent's purpose
- **Example**: `weather-agent` uses `weather-fetcher` and `weather-svg-creator` as preloaded skills

### Direct Skill Invocation Pattern
- **How**: Explicitly invoked using the `Skill` tool
- **Use Case**: Reusable functionality that can be used by multiple agents or commands
- **Example**: The `/weather-orchestrator` command could also invoke skills directly if needed

## Key Architectural Points

### 1. Separation of Concerns
- **Command**: User interaction and workflow orchestration
- **Agent**: Business logic and skill coordination
- **Skill**: Atomic, reusable functionality units

### 2. Reusability
- Skills can be used by multiple agents
- Agents can be invoked by multiple commands
- Commands can be chained or reused

### 3. Context Isolation
- Agents run in `fork` context by default for isolation
- Skills inherit the agent's context when invoked internally
- Direct skill invocations can also use `fork` context

## Implementation Notes

### Skill Reusability
Both `weather-fetcher` and `weather-svg-creator` are designed to be reusable:
- `weather-fetcher` can be used by any agent needing weather data
- `weather-svg-creator` can create weather cards for any temperature source

...(내용 생략)...
