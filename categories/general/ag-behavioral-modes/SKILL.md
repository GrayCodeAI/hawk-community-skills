---
name: ag-behavioral-modes
description: AI operational modes (brainstorm, implement, debug, review, teach, ship,
  orchestrate). Use to adapt behavior based on task type.
license: MIT
tags:
- general
risk: unknown
source: community
date_added: 2026-02-27
---

## Manual Mode Switching

Users can explicitly request a mode:

```
/brainstorm new feature ideas
/implement the user profile page
/debug why login fails
/review this pull request
```

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
