---
name: ghcp-references-requirements_pipeline
description: 'Skill: ghcp-references-requirements_pipeline'
license: MIT
tags:
- general
---

## After the pipeline: review and refinement

The pipeline produces a solid baseline, but AI isn't 100% reliable. The skill provides two standalone tools for iterative improvement:

### Requirements review (`quality/REVIEW_REQUIREMENTS.md`)

An interactive or guided review of requirements organized by use case. Three modes:
- **Self-guided**: Pick use cases to drill into
- **Fully guided**: Walk through use cases sequentially
- **Cross-model audit**: A different model fact-checks the completeness report

Progress and feedback are tracked in `quality/REFINEMENT_HINTS.md`. See the generated `quality/REVIEW_REQUIREMENTS.md` for the full protocol.

### Requirements refinement (`quality/REFINE_REQUIREMENTS.md`)

Reads `quality/REFINEMENT_HINTS.md` and updates `quality/REQUIREMENTS.md` to close identified gaps. Can be run with any model. Backs up the current version, bumps minor version, reports all changes. See the generated `quality/REFINE_REQUIREMENTS.md` for the full protocol.

### Multi-model refinement

Users can run refinement passes with different models to catch different blind spots. Each pass: backup → refine → version bump → log in VERSION_HISTORY.md. Run as many models as desired until diminishing returns.
