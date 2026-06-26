---
title: Weather Orchestrator Command
created: 2026-06-01
updated: 2026-06-13
type: concept
tags: [ai-ml, programming, research]
sources: [raw/local/ai-ml/commands-weather-orchestrator-2026-06-01.md]
source_file: /Users/bearj/projects/.claude/commands/weather-orchestrator.md
confidence: high
links: [[orchestration-workflow-orchestration-workflow|Weather System Orchestration Workflow]], [[commands-research-to-ppt|Research to PPT Command]]
---

# Weather Orchestrator Command

> 관련: [[agents-weather-agent|Weather Agent]], [[orchestration-workflow-orchestration-workflow|오케스트레이션 워크플로우]]를 참고하세요.

> 📁 원본: `/Users/bearj/projects/.claude/commands/weather-orchestrator.md`
> 📅 수집: 2026-06-01
> 🏷️ 카테고리: ai-ml

## 내용

# Weather Orchestrator Command

This command demonstrates the Command → Agent → Skill pattern for Claude Code.

## Description
Asks user for temperature unit preference (Celsius or Fahrenheit), then orchestrates a weather agent to fetch temperature data and create an SVG weather card.

## Usage
`/weather-orchestrator`

## Behavior
1. Prompts user: "Enter temperature unit (C for Celsius, F for Fahrenheit):"
2. Based on response, invokes the weather-agent with unit parameter
3. The weather-agent fetches temperature using its preloaded weather-fetcher skill
4. Then invokes the weather-svg-creator skill to generate SVG output
5. Results are written to orchestration-workflow/weather.svg and orchestration-workflow/output.md

## Example Interaction
```
User: /weather-orchestrator
Claude: Enter temperature unit (C for Celsius, F for Fahrenheit):
User: C
Claude: [invokes weather-agent agent]
Claude: [weather-agent fetches temperature in Celsius]
Claude: [weather-agent invokes weather-svg-creator skill]
Claude: Weather data saved to orchestration-workflow/weather.svg and orchestration-workflow/output.md
```
