---
name: ghcp-learning-hub-agentic-workflows
description: Learn what GitHub Agentic Workflows are, how to use community workflows
  from Awesome Copilot, and how to contribute your own.
license: MIT
tags:
- general
title: Agentic Workflows
authors: None
lastUpdated: 2026-02-27
estimatedReadingTime: 7 minutes
relatedArticles: None
prerequisites: None
---

```

**Required fields**:
- `name` — human-readable workflow name
- `description` — concise summary of the workflow's purpose

**Workflow fields**:
- `on` — trigger configuration (schedules, events, slash commands)
- `permissions` — GitHub API scopes (use least-privilege)
- `safe-outputs` — guardrails for what the agent can create or modify

### Step 3: Write Clear Instructions

The body of the file contains the natural language instructions the agent follows. Be specific and structured:

```markdown
## Task Overview

Describe the main goal clearly.

## Steps

1. First, gather the relevant data
2. Then, analyze and summarize
3. Finally, create the output (issue, comment, etc.)

## Output Format

Describe the expected format of the result.
```

### Step 4: Validate and Test

```bash
# Validate the workflow compiles correctly
gh aw compile --validate --no-emit workflows/my-new-workflow.md
```

### Step 5: Submit Your Contribution

1. Fork the repository and create a new branch
2. Add your workflow `.md` file to the `workflows/` directory
3. Run `npm run build` to update the README
4. Submit a pull request targeting the `staged` branch

> **Important:** Only submit the `.md` source file. Do not include compiled `.lock.yml` or `.yml` files — CI will block them.

### Workflow Contribution Guidelines

- **Security first** — use least-privilege permissions and safe outputs instead of direct write access
- **Clear instructions** — write specific, unambiguous natural language in the workflow body
- **Descriptive names** — use lowercase filenames with hyphens (e.g., `daily-issues-report.md`)
- **Test locally** — validate with `gh aw compile --validate` before submitting
- **Document the purpose** — the `description` field should make it clear what the workflow does and when to use it

## Learn More

- **Official documentation**: [GitHub Agentic Workflows](https://gh.io/gh-aw) — full specification and reference
- **Browse workflows**: [Awesome Copilot Workflows](../../workflows/) — community-contributed collection
- **Contributing guide**: [CONTRIBUTING.md](https://github.com/github/awesome-copilot/blob/main/CONTRIBUTING.md#adding-agentic-workflows) — detailed contribution guidelines
- **Related**: [Automating with Hooks](../automating-with-hooks/) — deterministic automation for Copilot agent sessions
- **Related**: [Using the Copilot Coding Agent](../using-copilot-coding-agent/) — the agent that powers agentic workflows

---
