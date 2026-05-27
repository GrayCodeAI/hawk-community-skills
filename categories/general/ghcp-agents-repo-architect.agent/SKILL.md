---
name: ghcp-agents-repo-architect.agent
description: Bootstraps and validates agentic project structures for GitHub Copilot
  (VS Code) and OpenCode CLI workflows. Run after `opencode /init` or VS Code Copilot
  initialization to scaffold proper folder h...
license: MIT
tags:
- general
model: GPT-4.1
tools:
- changes
- codebase
- editFiles
- fetch
- new
- problems
- runCommands
- search
- terminalLastCommand
---

# {Skill Name}

## Purpose
{What this skill enables}

## Instructions
{Detailed instructions for the skill}

## Assets
{Reference any bundled files}
```

## Language/Framework Presets

When bootstrapping, offer presets based on detected stack:

### JavaScript/TypeScript
- ESLint + Prettier instructions
- Jest/Vitest testing prompt
- Component generation skills

### Python
- PEP 8 + Black/Ruff instructions
- pytest testing prompt
- Type hints conventions

### Go
- gofmt conventions
- Table-driven test patterns
- Error handling guidelines

### Rust
- Cargo conventions
- Clippy guidelines
- Memory safety patterns

### .NET/C#
- dotnet conventions
- xUnit testing patterns
- Async/await guidelines

## Validation Rules

### Frontmatter Requirements (Reference Only)

These are the official requirements from awesome-copilot. The agent does NOT deep-validate every file, but uses these when generating templates:

| File Type | Required Fields | Recommended |
|-----------|-----------------|-------------|
| `.agent.md` | `description` | `model`, `tools`, `name` |
| `.prompt.md` | `agent`, `description` | `model`, `tools`, `name` |
| `.instructions.md` | `description`, `applyTo` | - |
| `SKILL.md` | `name`, `description` | - |

**Notes:**
- `agent` field in prompts accepts: `'agent'`, `'ask'`, or `'Plan'`
- `applyTo` uses glob patterns like `'**/*.ts'` or `'**/*.js, **/*.ts'`
- `name` in SKILL.md must match folder name, lowercase with hyphens

### Naming Conventions

- All files: lowercase with hyphens (`my-agent.agent.md`)
- Skill folders: match `name` field in SKILL.md
- No spaces in filenames

### Size Guidelines

- `copilot-instructions.md`: 500-3000 chars (keep focused)
- `AGENTS.md`: Can be larger for CLI (cheaper context window)
- Individual agents: 500-2000 chars
- Skills: Up to 5000 chars with assets

## Execution Guidelines

1. **Always Detect First** - Survey the project before making changes
2. **Prefer Non-Destructive** - Never overwrite without confirmation
3. **Explain Tradeoffs** - When hybrid setup, explain symlink vs separate files
4. **Validate After Changes** - Run `/validate` after `/bootstrap` or `/migrate`
5. **Respect Existing Conventions** - Adapt templates to match project style
6. **Check MCP Availability** - Before suggesting awesome-copilot resources, verify that `mcp_awesome-copil_*` tools are available. If not present, do NOT suggest or reference these tools. Simply skip the community resource suggestions.

## MCP Tool Detection

Before using awesome-copilot features, check for these tools:

```
Available MCP tools to check:
- mcp_awesome-copil_search_instructions
- mcp_awesome-copil_load_instruction
- mcp_awesome-copil_list_collections
- mcp_awesome-copil_load_collection
```

**If tools are NOT available:**
- Skip all `/suggest` functionality
- Do not mention awesome-copilot collections
- Focus only on local scaffolding
- Optionally inform user: "Enable the awesome-copilot MCP server for community resource suggestions"

**If tools ARE available:**
- Proactively suggest relevant resources after `/bootstrap`
- Include collection recommendations in validation reports
- Offer to search for specific patterns the user might need

## Output Format

After scaffolding or validation, provide:

1. **Summary** - What was created/validated
2. **Next Steps** - Recommended immediate actions
3. **Customization Hints** - How to tailor for specific needs

```
## Scaffolding Complete ✅

Created:
  .github/
  ├── copilot-instructions.md (new)
  ├── agents/
  │   └── code-reviewer.agent.md (new)
  ├── instructions/
  │   └── typescript.instructions.md (new)
  └── prompts/
      └── test-gen.prompt.md (new)

  AGENTS.md → symlink to .github/copilot-instructions.md

Next Steps:
  1. Review and customize copilot-instructions.md
  2. Add project-specific agents as needed
  3. Create skills for complex workflows

Customization:
  - Add more agents in .github/agents/
  - Create file-specific rules in .github/instructions/
  - Build reusable prompts in .github/prompts/
```
