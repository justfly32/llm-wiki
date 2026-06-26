---
source_file: /Users/bearj/projects/CLAUDE.md
ingested: 2026-06-01
sha256: 1b9a8afd0dc4
category: ai-ml
original_title: CLAUDE.md
---

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
- `sounds/`: Audio files organized by hook event (generated via ElevenLabs TTS)

Hook events configured in `.claude/settings.json`: PreToolUse, PostToolUse, UserPromptSubmit, Notification, Stop, SubagentStart, SubagentStop, PreCompact, SessionStart, SessionEnd, Setup, PermissionRequest, TeammateIdle, TaskCompleted, ConfigChange.

Special handling: git commits trigger `pretooluse-git-committing` sound.

## Development Workflow

### Common Commands
Since this is a configuration repository for Claude Code itself:
- **View current settings**: `cat .claude/settings.json`
- **Edit settings**: Use Edit tool on `.claude/settings.json` or `.claude/settings.local.json`
- **Test skills/commands**: Invoke them directly (e.g., `/weather-orchestrator`)
- **Validate YAML**: Use `/doctor` to check configuration validity
- **Reload configuration**: Restart Claude Code session after changes

### Configuration Testing
1. Create temporary skill/command files in `.claude/` directory
2. Test with `/skill-name` or `/command-name`
3. Check hook triggers in `.claude/hooks/scripts/hooks.py`
4. Verify audio feedback in `.claude/hooks/sounds/`

### Debugging
- Use `/doctor` for diagnostics
- Check hook execution via console logs
- Use browser automation MCPs (Claude in Chrome, Playwright) to inspect hook behavior
- Monitor `.claude/hooks/scripts/hooks.py` output

## Critical Patterns

### Subagent Orchestration
Subagents **cannot** invoke other subagents via bash commands. Use the Agent tool (renamed from Task in v2.1.63; `Task(...)` still works as an alias):
```
Agent(subagent_type="agent-name", description="...", prompt="...", model="haiku")
```

Be explicit about tool usage in subagent definitions. Avoid vague terms like "launch" that could be misinterpreted as bash commands.

### Subagent Definition Structure
Subagents in `.claude/agents/*.md` use YAML frontmatter:
- `name`: Subagent identifier
- `description`: When to invoke (use "PROACTIVELY" for auto-invocation)
- `tools`: Comma-separated allowlist of tools (inherits all if omitted). Supports `Agent(agent_type)` syntax
- `disallowedTools`: Tools to deny, removed from inherited or specified list
- `model`: Model alias: `haiku`, `sonnet`, `opus`, or `inherit` (default: `inherit`)
- `permissionMode`: Permission mode (e.g., `"acceptEdits"`, `"plan"`, `"bypassPermissions"`)
- `maxTurns`: Maximum agentic turns before the subagent stops
- `skills`: List of skill names to preload into agent context
- `mcpServers`: MCP servers for this subagent (server names or inline configs)
- `hooks`: Lifecycle hooks scoped to this subagent (all hook events are supported; `PreToolUse`, `PostToolUse`, and `Stop` are the most common)
- `memory`: Persistent memory scope — `user`, `project`, or `local` (see `reports/claude-agent-memory.md`)
- `background`: Set to `true` to always run as a background task
- `effort`: Effort level override: `low`, `medium`, `high`, `max` (default: inherits from session)
- `isolation`: Set to `"worktree"` to run in a temporary git worktree
- `color`: CLI output color for visual distinction

### Configuration Hierarchy
1. **Managed** (`managed-settings.json` / MDM plist / Registry): Organization-enforced, cannot be overridden
2. Command line arguments: Single-session overrides
3. `.claude/settings.local.json`: Personal project settings (git-ignored)
4. `.claude/settings.json`: Team-shared settings
5. `~/.claude/settings.json`: Global personal defaults
6. `hooks-config.local.json` overrides `hooks-config.json`

### Disable Hooks
Set `"disableAllHooks": true` in `.claude/settings.local.json`, or disable individual hooks in `hooks-config.json`.

## Answering Best Practice Questions

When the user asks a Claude Code best practice question, **always search this repo first** (`best-practice/`, `reports/`, `tips/`, `implementation/`, and `README.md`) before relying on training knowledge or external sources. This repo is the authoritative source — only fall back to external docs or web search if the answer is not found here.

## Workflow Notes (Claude-Specific)

Shared workflow, git, and collaboration policy is maintained in `docs/ai/core-principles.md`.

Keep this file focused on Claude-only behavior. For this repository, Claude-specific workflow guidance is:

- Keep `CLAUDE.md` concise (target under ~200 lines for reliability).
- `.claude/rules/*.md` with `paths:` frontmatter are lazy-loaded only for matching files.
- Prefer command-driven orchestration (`.claude/commands/`) for repeatable workflows.
- Use `/doctor` first when debugging Claude configuration behavior.

## Documentation

See `.claude/rules/markdown-docs.md` for documentation standards. Key docs:
- `best-practice/claude-subagents.md`: Subagent frontmatter, hooks, and repository agents
- `best-practice/claude-commands.md`: Slash command patterns and built-in command reference
- `orchestration-workflow/orchestration-workflow.md`: Weather system flow diagram