---
name: neo-plan-task
description: Refine, parallelize, and verify a draft task specification into a fully
  planned implementation-ready task
license: MIT
tags:
- general
argument-hint: Path to draft task file (e.g., ".specs/tasks/draft/add-validation.feature.md")
  [options]
---

## Error Handling

### Phase Agent Failure (Exception/Crash)

If any phase agent fails unexpectedly:

1. Report the failure with agent output
2. Ask clarification questions from user that can help resolve the issue
3. Launch the phase agent again with list of questions and answers to resolve the issue

### Judge Returns FAIL

If any judge returns FAIL (score < `THRESHOLD`):

1. **Automatic retry**: Re-launch the phase agent with judge feedback
2. **Human-in-the-loop check**: If phase is in `HUMAN_IN_THE_LOOP_PHASES`, trigger human checkpoint **before** the next judge retry (after implementation retry but before re-judging)
3. **After `MAX_ITERATIONS` reached**: **Proceed to next stage automatically** (do NOT ask user unless `--human-in-the-loop` includes this phase)
4. Log warning in completion summary: `⚠️ Phase X did not pass quality threshold (X.X/THRESHOLD) after MAX_ITERATIONS iterations`

### Retry Flow

```
Implementation → Judge FAIL → Implementation Retry → Judge Retry
                                                          ↓
                              PASS → Continue to next stage
                              FAIL → Repeat until MAX_ITERATIONS
                                          ↓
                              MAX_ITERATIONS reached → Proceed to next stage (with warning)
```

### Retry Flow with Human-in-the-Loop

When phase is in `HUMAN_IN_THE_LOOP_PHASES`:

```
Implementation → Judge FAIL → Implementation Retry
                                    ↓
                    🔍 Human Checkpoint (optional feedback)
                                    ↓
                              Judge Retry
                                    ↓
                    PASS → Continue | FAIL → Repeat until MAX_ITERATIONS
                                                    ↓
                              MAX_ITERATIONS → 🔍 Final Human Checkpoint
                                                    ↓
                                    User confirms → Proceed to next stage
```
