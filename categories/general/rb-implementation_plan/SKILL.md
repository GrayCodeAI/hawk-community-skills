---
name: rb-implementation_plan
description: 'Skill: rb-implementation_plan'
license: MIT
tags:
- general
---

### Phase 4: The Ecosystem - Contributor Tooling

**Objective:** To set up the external infrastructure needed for the community to thrive.

1.  **Task: Create the Public Index GitHub Repository**
    *   This codebase ships a template under `community-index/` containing `packs.json`, `README.md`, and `CONTRIBUTING.md`.
    *   To publish it, run `git init`, commit the files, and push to a new public GitHub repository (e.g., `rulebook-ai-community/index`).

2.  **Task: Implement the CI Validation Workflow**
    *   The template includes `.github/workflows/validate.yml` and `scripts/validate_index.py`.
    *   The workflow runs on pull requests and clones each referenced pack to verify required files and `manifest.yaml` name alignment.

**Outcome of Phase 4:** The community has a place to submit packs and a clear, automated process for validating their submissions, completing the ecosystem loop.
ing the ecosystem loop.
