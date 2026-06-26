---
source_file: /Users/bearj/projects/best-practice/claude-subagents.md
ingested: 2026-06-01
sha256: 85961ca3ed40
category: ai-ml
original_title: Claude Code Subagents Best Practices
---

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
This runs the agent in a temporary git worktree, preventing accidental changes to the main working directory.

### 7. Define Clear Lifecycle Hooks
Use hooks to customize agent behavior at key points:
- `SubagentStart`: Log when agent begins, set up resources
- `PreToolUse`: Validate tool usage before execution
- `PostToolUse`: Process results after tool execution
- `SubagentStop`: Clean up resources, log completion

## Common Subagent Patterns

### Code Reviewer Agent
```yaml
name: code-reviewer
description: PROACTIVELY reviews code for potential issues
tools: Read, Bash(grep, lint), Write
model: sonnet
permissionMode: acceptEdits
maxTurns: 5
skills: [lint-runner, security-scanner, style-checker]
hooks:
  PreToolUse: |
    # Validate that we're only reading files, not modifying unexpectedly
    if [[ "$TOOL_USE_NAME" == "Write" || "$TOOL_USE_NAME" == "Edit" ]]; then
      echo "Warning: Code reviewer attempting to modify files"
    fi
```

### Test Generator Agent
```yaml
name: test-generator
description: Generates unit tests for given code
tools: Read, Write, Bash
model: haiku
permissionMode: plan
maxTurns: 3
skills: [test-framework-detector, mock-generator, assertion-creator]
context: fork
isolation: worktree
```

### Documentation Agent
```yaml
name: doc-writer
description: Creates and updates documentation
tools: Read, Write, Bash(pandoc, markdownlint)
model: haiku
permissionMode: acceptEdits
maxTurns: 4
skills: [markdown-formatter, diagram-generator, link-validator]
memory: project
```

## Anti-Patterns to Avoid

### Overly Permissive Tools (avoid)
```yaml
# DON'T do this - gives too much access
tools: *
```

### Unlimited Turns (avoid)
```yaml
# DON'T do this - can lead to infinite loops
maxTurns: 100
```

### Vague Descriptions (avoid)
```yaml
# DON'T do this - unclear when to use the agent
description: Helper agent for various tasks
```

### Ignoring Context (avoid)
```yaml
# DON'T do this for file-modifying agents
# (unless you specifically want direct file modification)
isolation:  # Missing - defaults to direct modification
```

## Testing Subagents

1. **Unit Test Skills First**: Ensure each skill works in isolation
2. **Test Agent in Isolation**: Run the agent with simple, well-defined tasks
3. **Check Tool Usage**: Verify the agent only uses declared tools
4. **Validate Hook Execution**: Ensure hooks fire at expected times
5. **Test Error Handling**: Make sure agents handle failures gracefully

## Related Documentation
- `best-practice/claude-commands.md`: For creating commands that invoke subagents
- `.claude/rules/markdown-docs.md`: Documentation standards
- `reports/claude-agent-memory.md`: Understanding agent memory scopes