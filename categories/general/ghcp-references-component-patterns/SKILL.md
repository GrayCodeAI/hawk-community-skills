---
name: ghcp-references-component-patterns
description: 'Skill: ghcp-references-component-patterns'
license: MIT
tags:
- general
---

## Loading States

### Loading Patterns

| Duration | Pattern |
| -------- | ------- |
| <1 second | No indicator (feels instant) |
| 1-3 seconds | Spinner or progress indicator |
| 3-10 seconds | Skeleton screens + progress |
| >10 seconds | Progress bar + explanation |

### Skeleton Screen

```text
┌─────────────────────────────────────┐
│ ░░░░░░░░░░░░ ░░░░░░░░░░           │
├─────────────────────────────────────┤
│ ░░░░░░░░░░░░░░░░░░░░░░░░░         │
│ ░░░░░░░░░░░░░░░░░░░               │
│ ░░░░░░░░░░░░░░░░░░░░░░░           │
└─────────────────────────────────────┘

```

- Match layout of loaded content
- Use subtle animation (shimmer/pulse)
- Show actual content structure
