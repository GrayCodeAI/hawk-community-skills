---
name: ag-monte-carlo-prevent
description: Surfaces Monte Carlo data observability context (table health, alerts,
  lineage, blast radius) before SQL/dbt edits.
license: MIT
tags:
- data-observability
- dbt
- schema
- monte-carlo
- lineage
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

## Session markers

These markers coordinate between the skill and the plugin's hooks. Output each
on its own line when the condition is met.

### Impact check complete

After the engineer confirms (High/Medium) or after presenting the synthesis (Low),
output one marker per assessed table. **IMPORTANT: use only the table/model name, not the full MCON:**

<!-- MC_IMPACT_CHECK_COMPLETE: <table_name> -->

(Use the model filename without .sql extension — NOT "acme.analytics.orders" or "prod.public.client_hub")

How many markers to emit depends on how the assessment was triggered:

**Hook-triggered** (the pre-edit hook blocked an edit and instructed you to run
the assessment): Be strict — only emit markers for tables whose lineage **and**
monitor coverage were fetched directly via Monte Carlo tools in this session. If
the engineer describes changes to multiple tables but only one was formally
assessed, emit only one marker. The pre-edit hook will gate the other tables and
prompt for their own Workflow 4 runs.

**Voluntarily invoked** (the engineer proactively asked for an impact assessment):
Be looser — emit markers for all tables the assessment meaningfully covered, even
if some were assessed via lineage context rather than direct MC tool calls. The
engineer is already safety-conscious; don't force redundant assessments for tables
they clearly considered.

### Monitor coverage gap

When Workflow 4 finds zero custom monitors on a table's affected columns, output:

<!-- MC_MONITOR_GAP: <table_name> -->

Use only the table/model name (NOT the full MCON). This allows the plugin's hooks
to remind the engineer about monitor coverage at commit time. Only output this
marker when the gap is specifically about the columns or logic being changed —
not for general table-level monitor absence.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
