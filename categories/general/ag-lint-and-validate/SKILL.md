---
name: ag-lint-and-validate
description: 'MANDATORY: Run appropriate validation tools after EVERY code change.
  Do not finish a task until the code is error-free.'
license: MIT
tags:
- general
risk: unknown
source: community
date_added: 2026-02-27
---

## Scripts

| Script | Purpose | Command |
|--------|---------|---------|
| `scripts/lint_runner.py` | Unified lint check | `python scripts/lint_runner.py <project_path>` |
| `scripts/type_coverage.py` | Type coverage analysis | `python scripts/type_coverage.py <project_path>` |

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
