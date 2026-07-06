---
name: rb-02-error-documentation
description: "Document major failure points in this project and how they were solved."
license: MIT
tags: [general]
---

## Overview

Document significant failure points encountered during development, their root causes, and the solutions applied. Use this skill when:
- A bug or failure has already been resolved and you need to record what happened
- You're onboarding new team members and want them to learn from past incidents
- You need to create a post-mortem or incident report

## When to Use

This skill applies retroactively, after a problem has been identified and fixed. It is not a debugging guide (for that, see `categories/debugging/debugging-and-error-recovery/SKILL.md`). Instead, it focuses on documenting the resolution for future reference.

## How to Document

For each failure point recorded:

1. **Describe the failure** — What went wrong, in one sentence
2. **Root cause** — What caused it (be specific: wrong algorithm, race condition, incorrect config, etc.)
3. **Solution applied** — What was changed to fix it
4. **Prevention** — What should be done to prevent recurrence

### Example Format

```markdown
## Failure: Authentication token expiry too short

**Issue:** Users logged out after 15 minutes of inactivity, causing frustration.

**Root Cause:** Token expiry was set to 15 minutes but session activity timer was 30 minutes, creating a mismatch.

**Fix:** Unified expiry to 30 minutes and added a 5-minute buffer before token refresh.

**Prevention:** All token lifetimes now documented in `docs/security/token-lifetimes.md`.
```

## Verification

- [ ] Each entry includes description, root cause, fix, and prevention
- [ ] Entries are factual and concise
- [ ] Prevention steps are actionable

