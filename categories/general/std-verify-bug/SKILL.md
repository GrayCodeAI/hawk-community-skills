---
name: std-verify-bug
description: Post-merge UAT verification workflow. Walks JIRA reproduce steps, performs
  comparative audits (Before/After), attaches evidence to JIRA, and transitions status
  on PASS.
license: MIT
tags:
- general
metadata: None
triggers: None
keywords: None
---

## 🚫 Anti-Patterns

- **No Sequential Runs**: Verify all markets in parallel.
- **No Unnamed Sessions**: Traceability depends on `-s={TICKET}`.
- **No Mystery Failures**: Always include the Diagnostic Decoder result in FAIL comments.
- **No Orphan Comments**: Clean up "temp media" comments after posting the final verdict.
