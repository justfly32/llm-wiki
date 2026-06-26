---
title: Presentation Rules
created: 2026-06-01
updated: 2026-06-01
type: concept
tags: [ai-ml, programming, research]
sources: [raw/local/ai-ml/rules-presentation-2026-06-01.md]
source_file: /Users/bearj/projects/.claude/rules/presentation.md
confidence: high
links: [[commands-research-to-ppt|Research to PPT Command]], [[commands-weather-orchestrator|Weather Orchestrator Command]]
---

# Presentation Rules

> 📁 원본: `/Users/bearj/projects/.claude/rules/presentation.md`
> 📅 수집: 2026-06-01
> 🏷️ 카테고리: ai-ml

## 내용

# Presentation Rules

Presentation work in this repository is delegated per-presentation to specialized agents:

## Delegation Rules

1. **`presentation/vibe-coding-to-agentic-engineering/`**
   - Delegated to: `presentation-vibe-coding` agent
   - Purpose: Presentation materials for vibe coding to agentic engineering talks

2. **`presentation/2026-04-25-gdg-kolachi-cli-claude-code-gemini/`**
   - Delegated to: `presentation-claude-gemini` agent
   - Purpose: GDG Kolachi CLI presentation on Claude Code and Gemini

## How Delegation Works

When Claude touches files matching these paths, it automatically loads the corresponding rule file which delegates presentation work to the specified agent.

## Agent Requirements

Presentation agents should:
- Be designed for creating presentation materials
- Have access to necessary tools for slide creation, diagram generation, etc.
- Understand the specific presentation context and audience
