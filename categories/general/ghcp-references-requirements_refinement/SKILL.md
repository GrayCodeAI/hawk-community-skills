---
name: ghcp-references-requirements_refinement
description: 'Skill: ghcp-references-requirements_refinement'
license: MIT
tags:
- general
---

## Running multiple refinement passes

Each pass follows the same protocol:
1. Read the latest REFINEMENT_HINTS.md (which now includes the previous pass's report)
2. Focus only on feedback items marked "not addressed" or new feedback added since the last pass
3. Backup, bump version, make changes, report

The user can add new hints between passes by editing REFINEMENT_HINTS.md directly. The next refinement pass picks them up automatically.

The user can also run a fresh cross-model audit (Mode 3 of the review protocol) between refinement passes to find new gaps that the previous refinement didn't catch. This creates a review → refine → review → refine cycle that converges on completeness.
```
