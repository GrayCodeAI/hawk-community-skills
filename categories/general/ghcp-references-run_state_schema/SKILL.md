---
name: ghcp-references-run_state_schema
description: 'Skill: ghcp-references-run_state_schema'
license: MIT
tags:
- general
---

## Format invariants (enforced by `bin/run_state_lib.py` validators)

1. `_index` is line 1.
2. Every line is valid JSON (one object per line).
3. Every event has `ts` and `event` fields.
4. Every `event` value appears in `_index.event_types`.
5. Append-only: events are added, never edited. Editing a prior event is a schema violation.
6. `phase_start` and `phase_end` events for a given phase appear at most once per run (no out-of-order or duplicate phase markers).
7. `run_start` is the second line (after `_index`); `run_end` is the last line if the run completed.

Validators are read-only checks. They surface violations as findings; they don't auto-correct.
