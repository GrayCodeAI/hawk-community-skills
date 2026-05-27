---
name: ghcp-instructions-azure-naming.instructions
description: 'Skill: ghcp-instructions-azure-naming.instructions'
license: MIT
tags:
- general
---

## Do NOT Do

- Do not use underscores unless the resource type requires it — use hyphens.
- Do not spell out the full resource type word (e.g., `storageaccount-myapp` → use `stmyapp001`).
- Do not use uppercase letters (resources are case-insensitive; lowercase is the convention).
- Do not include sensitive data (subscription ID, tenant ID, passwords) in names.
- Do not skip the environment segment — even for production.
- Do not use `#` — it breaks URL parsing in Azure Resource Manager.
- Do not use reserved words or trademarks in names for resources with public endpoints.
- Do not use more than two consecutive hyphens (e.g., `app--prod` is invalid).
