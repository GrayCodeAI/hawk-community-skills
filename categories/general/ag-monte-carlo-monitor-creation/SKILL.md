---
name: ag-monte-carlo-monitor-creation
description: Guides creation of Monte Carlo monitors via MCP tools, producing monitors-as-code
  YAML for CI/CD deployment.
license: MIT
tags:
- data-observability
- monitoring
- monte-carlo
- monitors-as-code
category: data
risk: safe
source: community
source_repo: monte-carlo-data/mc-agent-toolkit
source_type: community
date_added: 2026-04-08
author: monte-carlo-data
tools:
- claude
- cursor
- codex
---

## Common mistakes to avoid

- **NEVER guess column names.** Always get them from `getTable`.
- **NEVER skip the confirmation step** (Step 6).
- For metric monitors, `aggregate_time_field` MUST be a real timestamp column from the table.
- For validation monitors, conditions match INVALID data, not valid data.
- Always pass an MCON when possible. If only table name is available, also pass warehouse.
- **ALWAYS check table's `domains` BEFORE calling any creation tool.**
- ALWAYS use ISO 8601 format for datetime values.
- NEVER reformat YAML values returned by creation tools.
- Do not call creation tools before the validation phase is complete.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
