---
name: ag-skill-creator-ms
description: Guide for creating effective skills for AI coding agents working with
  Azure SDKs and Microsoft Foundry services. Use when creating new skills or updating
  existing skills.
license: MIT
tags:
- general
risk: unknown
source: community
date_added: 2026-02-27
---

## Checklist

Before completing a skill:

**Prerequisites:**
- [ ] User provided SDK package name or documentation URL
- [ ] Verified SDK patterns via `microsoft-docs` MCP

**Skill Creation:**
- [ ] Description includes what AND when (trigger phrases)
- [ ] SKILL.md under 500 lines
- [ ] Authentication uses `DefaultAzureCredential`
- [ ] Includes cleanup/delete in examples
- [ ] References organized by feature

**Categorization:**
- [ ] Skill created in `.github/skills/<skill-name>/`
- [ ] Symlink created in `skills/<language>/<category>/<short-name>`
- [ ] Symlink points to `.github/skills/<skill-name>`

**Testing:**
- [ ] `references/acceptance-criteria.md` created with correct/incorrect patterns
- [ ] `tests/scenarios/<skill-name>/scenarios.yaml` created
- [ ] All scenarios pass (`pnpm harness <skill> --mock`)
- [ ] Import paths documented precisely

**Documentation:**
- [ ] README.md skill catalog updated
- [ ] Instructs to search `microsoft-docs` MCP for current APIs

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
