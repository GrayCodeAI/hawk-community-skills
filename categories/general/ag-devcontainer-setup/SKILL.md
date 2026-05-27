---
name: ag-devcontainer-setup
description: Creates devcontainers with Claude Code, language-specific tooling (Python/Node/Rust/Go),
  and persistent volumes. Use when adding devcontainer support to a project, setting
  up isolated development e...
license: MIT
tags:
- general
risk: safe
source: vibeship-spawner-skills (Apache 2.0)
date_added: 2026-03-06
---

## User Instructions

After generating, inform the user:

1. How to start: "Open in VS Code and select 'Reopen in Container'"
2. Alternative: `devcontainer up --workspace-folder .`
3. CLI helper: Run `.devcontainer/install.sh self-install` to add the `devc` command to PATH

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
