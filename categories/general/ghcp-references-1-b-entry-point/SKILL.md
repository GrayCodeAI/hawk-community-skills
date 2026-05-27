---
name: ghcp-references-1-b-entry-point
description: 'Skill: ghcp-references-1-b-entry-point'
license: MIT
tags:
- general
---

## Output: `pixie_qa/01-entry-point.md`

Write your findings to this file. Keep it focused — only entry point and execution flow.

### Template

```markdown
# Entry Point & Execution Flow

## How to run

<Command to start the app, required env vars, config files>

## Entry point

- **File**: <e.g., app.py, main.py>
- **Type**: <FastAPI server / CLI / standalone function / etc.>
- **Framework**: <FastAPI, Flask, Django, none>

## User-facing endpoints / interface

<For each way a user interacts with the app:>

- **Endpoint / command**: <e.g., POST /chat, python main.py --query "...">
- **Input format**: <request body shape, CLI args, function params>
- **Output format**: <response shape, stdout format, return type>

## Environment requirements

| Variable | Purpose | Required? | Default |
| -------- | ------- | --------- | ------- |
| ...      | ...     | ...       | ...     |
```
