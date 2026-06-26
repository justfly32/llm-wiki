---
source_file: /Users/bearj/projects/.claude/agents/weather-agent.md
ingested: 2026-06-01
sha256: 57f6607ab1c0
category: ai-ml
original_title: Weather Agent
---

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