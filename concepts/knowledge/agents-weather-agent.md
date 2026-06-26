---
title: Weather Agent
created: 2026-06-01
updated: 2026-06-13
type: concept
tags: [ai-ml, programming, research]
sources: [raw/local/ai-ml/agents-weather-agent-2026-06-01.md]
source_file: /Users/bearj/projects/.claude/agents/weather-agent.md
confidence: high
links: [[commands-weather-orchestrator|Weather Orchestrator 명령어]], [[orchestration-workflow-orchestration-workflow|Orchestration 워크플로우]], [[best-practice-claude-subagents|Claude Subagents 모범 사례]], [[projects-claude|CLAUDE.md]], [[docs-hermes_beginner_guide|Hermes 초보자 가이드]]
---

# Weather Agent

> 관련: [[commands-weather-orchestrator|Weather Orchestrator 명령어]], [[orchestration-workflow-orchestration-workflow|오케스트레이션 워크플로우]], [[projects-claude|CLAUDE.md]]를 참고하세요.

> 📁 원본: `/Users/bearj/projects/.claude/agents/weather-agent.md`
> 📅 수집: 2026-06-01
> 🏷️ 카테고리: ai-ml

## 내용

# Weather Agent

This agent fetches weather temperature using its preloaded weather-fetcher skill and then invokes the weather-svg-creator skill to create an SVG weather card.

## Description
Fetches temperature data and creates an SVG weather card. Used by the weather-orchestrator command.

## Tools
Read, Write, Bash (for fetching weather data via curl or similar)

## Model
haiku

## Skills
- weather-fetcher
- weather-svg-creator

## Permission Mode
plan

## Max Turns
5

## Context
fork

## Agent
general-purpose

## Memory
project

## Background
false

## Effort
medium

## Isolation
 (not set)

## Color
 (not set)
