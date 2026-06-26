---
source_file: /Users/bearj/projects/.claude/commands/weather-orchestrator.md
ingested: 2026-06-01
sha256: d56871dd76ee
category: ai-ml
original_title: Weather Orchestrator Command
---

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