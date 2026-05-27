---
name: ag-git-pr-review
description: Generate a concise and structured PR description from commit history
  with minimal token usage
license: MIT
tags:
- general
risk: safe
source: community
source_type: community
date_added: 2026-05-03
author: community
---

## Summary
Adds authentication flow and resolves session persistence issues.

## Changes
- authentication: added JWT middleware and login flow
- session: fixed expiration handling
- user: refactored user service logic

## Impact
Improves security and fixes inconsistent login behavior.
