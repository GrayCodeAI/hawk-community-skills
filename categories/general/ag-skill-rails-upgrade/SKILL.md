---
name: ag-skill-rails-upgrade
description: Analyze Rails apps and provide upgrade assessments
license: MIT
tags:
- general
risk: safe
source: https://github.com/robzolkos/skill-rails-upgrade
date_added: 2026-02-27
---

### When to Use This Skill

Analyze Rails apps and provide upgrade assessments

Use this skill when working with analyze rails apps and provide upgrade assessments.
## Error Handling

- If `gh` CLI is not authenticated, instruct the user to run `gh auth login`
- If railsdiff.org doesn't have the exact versions, try with major.minor.0 versions
- If the app is already on the latest version, congratulate the user and note any upcoming releases
- If local customizations would be lost, ALWAYS stop and show the user what would be overwritten before proceeding

## Key Principles

1. **Never overwrite without checking** - Always check for local customizations first
2. **Preserve user intent** - Local customizations exist for a reason
3. **Minimal changes** - Only add what's necessary for the new Rails version
4. **Transparency** - Show the user exactly what will change before doing it
5. **Reversibility** - User should be able to `git checkout` to restore if needed

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
