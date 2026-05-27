---
name: neo-reset
description: Reset the FPF reasoning cycle to start fresh
license: MIT
tags:
- general
---

# Session Archive: 2025-01-15

**Reset Reason**: User requested fresh start

## State at Reset

### Hypotheses
- L0: 2 (proposed)
- L1: 1 (verified)
- L2: 0 (validated)
- Invalid: 1 (rejected)

### Files Archived
- .fpf/knowledge/L0/hypothesis-a.md
- .fpf/knowledge/L0/hypothesis-b.md
- .fpf/knowledge/L1/hypothesis-c.md

### Decision Status
No decision was finalized.

## Notes

Session ended without decision. Hypotheses preserved for potential future reference.
```

2. **Move Active Work to Archive** (Optional)

If user wants to clear the knowledge directories:

```bash
mkdir -p .fpf/archive/session-2025-01-15
mv .fpf/knowledge/L0/*.md .fpf/archive/session-2025-01-15/ 2>/dev/null || true
mv .fpf/knowledge/L1/*.md .fpf/archive/session-2025-01-15/ 2>/dev/null || true
mv .fpf/knowledge/L2/*.md .fpf/archive/session-2025-01-15/ 2>/dev/null || true
```

3. **Report to User**

```markdown
## Reset Complete

Session archived to: .fpf/sessions/session-2025-01-15-reset.md

Current state:
- L0: 0 hypotheses
- L1: 0 hypotheses
- L2: 0 hypotheses

Ready for new reasoning cycle. Run `/fpf:propose-hypotheses` to start.
```

### Option 2: Hard Reset (Delete All)

**WARNING**: This permanently deletes all FPF data.

```bash
rm -rf .fpf/knowledge/L0/*.md
rm -rf .fpf/knowledge/L1/*.md
rm -rf .fpf/knowledge/L2/*.md
rm -rf .fpf/knowledge/invalid/*.md
rm -rf .fpf/evidence/*.md
rm -rf .fpf/decisions/*.md
```

Only do this if explicitly requested by user.

### Option 3: Decision Reset (Keep Knowledge)

If user wants to re-evaluate existing hypotheses:

1. Move L2 hypotheses back to L1 (re-audit)
2. Or move L1 hypotheses back to L0 (re-verify)

```bash
# Re-audit: L2 -> L1
mv .fpf/knowledge/L2/*.md .fpf/knowledge/L1/

# Re-verify: L1 -> L0
mv .fpf/knowledge/L1/*.md .fpf/knowledge/L0/
```
