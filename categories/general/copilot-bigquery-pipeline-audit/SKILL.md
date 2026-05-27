---
name: copilot-bigquery-pipeline-audit
description: Audits Python + BigQuery pipelines for cost safety, idempotency, and
  production readiness. Returns a structured report with exact patch locations.
license: MIT
tags:
- general
---

## Final

**1. PASS / FAIL** with specific reasons per section (A to F).
**2. Patch list** ordered by risk, referencing exact functions to change.
**3. If FAIL: Top 3 cost risks** with a rough worst-case estimate
(e.g., "loop over 90 dates x 3 retries = 270 BQ jobs").
