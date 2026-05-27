---
name: neo-decay
description: Manage evidence freshness by identifying stale decisions and providing
  governance actions
license: MIT
tags:
- general
---

## Common Workflows

### Weekly Maintenance
```
/fpf:decay                    # See what's stale
# For each stale item: refresh, deprecate, or waive
```

### Pre-Release
```
/fpf:decay                    # Check for stale decisions
# Either refresh evidence or explicitly waive with documented rationale
# Waiver rationales become part of release documentation
```

### After Major Change
```
# Dependency update, API change, security advisory...
/fpf:decay                    # See what's affected
# Deprecate obsolete decisions
# Start new hypothesis cycle for replacements
```
