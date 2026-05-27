---
name: ghcp-references-1-a-project-analysis
description: 'Skill: ghcp-references-1-a-project-analysis'
license: MIT
tags:
- general
---

## Output: `pixie_qa/00-project-analysis.md`

Write your findings to this file. **Complete all five sections before moving to sub-step 1b.** This document is referenced by every subsequent step.

### Template

```markdown
# Project Analysis

## What this software does

<One paragraph: what it does, in plain language. Not class names or file paths — what problem does it solve for its users?>

## Target users and value proposition

<Who uses it, why, what problem it solves that alternatives don't>

## Capability inventory

1. <Capability name>: <one-line description>
2. <Capability name>: <one-line description>
3. ...

## Realistic input characteristics

<What real-world inputs look like — size, complexity, messiness, variety. Be specific about scale and structure.>

## Hard problems and failure modes

1. <Failure mode>: <why it's hard, what goes wrong>
2. <Failure mode>: <why it's hard, what goes wrong>
3. ...
```

### Quality check

Before moving on, verify:

- The "What this software does" section describes the app's purpose in terms a non-technical user would understand — not just "it runs a graph" or "it calls OpenAI"
- The capability inventory lists at least 3 capabilities (if the project has them) — if you only found 1, you may have only looked at one part of the codebase
- The realistic input characteristics describe real-world scale and complexity, not the simplest possible input
- The failure modes are specific to this app's domain, not generic ("bad input" is not a failure mode; "malformed HTML with unclosed tags that breaks the parser" is)

### What to ignore in the project

The project may contain directories and files that are part of its own development/test infrastructure — `tests/`, `fixtures/`, `examples/`, `mock_server/`, `docs/`, demo scripts, etc. These exist for the project's developers, not for your eval pipeline.

**Critical**: Do NOT use the project's test fixtures, mock servers, example data, or unit test infrastructure as inputs for your eval traces or dataset entries. They are designed for development speed and isolation — small, clean, deterministic data that bypasses every real-world difficulty. Using them produces trivially easy evaluations that cannot catch real quality issues.

When you encounter these directories during analysis, note their existence but treat them as implementation details of the project — not as data sources for your QA pipeline. Your QA pipeline must test the app against real-world conditions, not against the project's own test shortcuts.
