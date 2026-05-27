---
name: ghcp-references-requirements_review
description: 'Skill: ghcp-references-requirements_review'
license: MIT
tags:
- general
---

## REFINEMENT_HINTS.md format

The review protocol creates and maintains this file:

```markdown
# Refinement Hints

## Review Progress
- [x] Use Case 1: [name] — reviewed, no issues
- [x] Use Case 2: [name] — reviewed, see feedback below
- [ ] Use Case 3: [name]
- [ ] Use Case 4: [name]
...

## Cross-Cutting Concerns
- [ ] Threading model — not yet reviewed
- [ ] Null contract — not yet reviewed
- [ ] Error philosophy — not yet reviewed
- [ ] Backward compatibility — not yet reviewed
- [ ] Configuration composition — not yet reviewed

## Feedback

### Use Case 2: [name]
- REQ-NNN: [specific feedback about what's missing or wrong]
- General: [broader observation about this use case's coverage]

### Cross-Model Audit
[if Mode 3 was run]

## Additional hints
[freeform feedback from the user, not tied to a specific use case]
```

This file serves dual purpose: it tracks review progress (so the user can resume across sessions) AND accumulates feedback that the refinement pass reads.
```
