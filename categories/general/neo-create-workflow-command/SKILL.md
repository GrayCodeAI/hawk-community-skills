---
name: neo-create-workflow-command
description: 'Skill: neo-create-workflow-command'
license: MIT
tags:
- general
---

# Implement Feature

## User Input
\`\`\`text
$ARGUMENTS
\`\`\`

Create TodoWrite with workflow steps.

## Phase 1: Research

Launch general-purpose agent:
- **Description**: "Research feature requirements"
- **Prompt**:
  \`\`\`
  Read ${CLAUDE_PLUGIN_ROOT}/tasks/step-1-feature-impl-research.md

  Feature: $ARGUMENTS
  \`\`\`

**Extract**: Key findings, constraints, existing patterns

## Phase 2: Architecture

Launch general-purpose agent:
- **Description**: "Design feature architecture"
- **Prompt**:
  \`\`\`
  Read ${CLAUDE_PLUGIN_ROOT}/tasks/step-2-feature-impl-architecture.md

  Feature: $ARGUMENTS
  Research findings: <summary from Phase 1>
  \`\`\`

**Extract**: File structure, components, interfaces

## Phase 3: Implementation

Launch developer agent:
- **Description**: "Implement feature code"
- **Prompt**:
  \`\`\`
  Read ${CLAUDE_PLUGIN_ROOT}/tasks/step-3-feature-impl-implement.md

  Architecture: <summary from Phase 2>
  \`\`\`

## Completion

Mark todos complete. Report:
1. Files created/modified
2. Tests added
3. Remaining work
```

### Task File Example (step-1-feature-impl-research.md)

```markdown
# Step 1: Feature Research

## Context
You are the research phase of a feature implementation workflow.

## Goal
Thoroughly understand the feature requirements and existing codebase context before any implementation begins.

## Instructions

1. **Parse Feature Request**
   - Extract core requirements
   - Identify acceptance criteria
   - Note any constraints mentioned

2. **Codebase Analysis**
   - Search for similar existing features
   - Identify relevant patterns and conventions
   - Find reusable components/utilities

3. **Dependency Check**
   - What existing code will this feature interact with?
   - Are there breaking change risks?
   - What tests exist for related functionality?

4. **Gap Analysis**
   - What's missing from the request?
   - What clarifications might be needed?
   - What edge cases should be considered?

## Constraints
- Do NOT write any implementation code
- Do NOT modify any files
- Focus purely on research and analysis

## Expected Output

Return a structured research summary:

\`\`\`markdown
## Feature Understanding
- Core requirement: <summary>
- Acceptance criteria: <list>

## Codebase Context
- Similar features: <list with file paths>
- Patterns to follow: <list>
- Reusable code: <list with file paths>

## Dependencies
- Files affected: <list>
- Tests to consider: <list>

## Open Questions
- <Question 1>
- <Question 2>

## Recommendation
<Brief recommendation for architecture phase>
\`\`\`

## Success Criteria
- [ ] Feature requirements clearly articulated
- [ ] Relevant existing code identified
- [ ] No implementation attempted
- [ ] Clear handoff to architecture phase
```

## Known Limitations

| Limitation | Impact | Workaround |
|------------|--------|------------|
| No nested sub-agents | Sub-agents can't spawn Task tool | Keep all orchestration in main command |
| No skill auto-loading | Sub-agents don't trigger skills | Pass explicit file paths or inline context |
| Fresh context per agent | Each dispatch starts empty | Use resume pattern OR pass summaries |
| File read latency | Extra tool call per step | Acceptable trade-off for context savings |

## Validation Checklist

Before finalizing workflow command:

- [ ] Each step has clear, specific goal
- [ ] Task files are self-contained (sub-agent doesn't need external context)
- [ ] File paths use `${CLAUDE_PLUGIN_ROOT}` for portability
- [ ] Context passed between steps is minimal (summaries, not full data)
- [ ] Orchestrator command stays lean (<100 tokens per step dispatch)
- [ ] Error handling defined for step failures
- [ ] Success criteria measurable for each step

## Create the Workflow

Based on user input, create:

1. **Directories**:
   - `${CLAUDE_PLUGIN_ROOT}/tasks/` - All task files directly here
   - `${CLAUDE_PLUGIN_ROOT}/agents/` - (Optional) Custom agent definitions

2. **Task files**: Create in `tasks/` directory with naming pattern `step-N-<workflow>-<name>.md`
   - Example: `step-1-feature-impl-research.md`
   - Example: `step-2-feature-impl-architecture.md`
   - Shared context: `common-context.md` directly in `tasks/`

3. **Orchestrator command**: Lean dispatch logic in `commands/<workflow-name>.md`

4. **Custom agents** (Optional): If workflow needs specialized agent behavior in `agents/`

5. **Update plugin.json**: Add command to plugin manifest if needed

After creation, suggest testing with `/customaize-agent:test-prompt` command.
