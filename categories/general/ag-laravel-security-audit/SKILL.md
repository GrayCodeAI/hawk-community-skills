---
name: ag-laravel-security-audit
description: Security auditor for Laravel applications. Analyzes code for vulnerabilities,
  misconfigurations, and insecure practices using OWASP standards and Laravel security
  best practices.
license: MIT
tags:
- general
risk: safe
source: community
date_added: 2026-02-27
---

## Example Audit Output Format

Issue: Missing Authorization Check  
Risk: High

Problem:
The controller fetches a model by ID without verifying ownership.

Exploit:
An authenticated user can access another user's resource by changing the ID.

Fix:
Use policy check or scoped query.

Refactored Example:

```php
$post = Post::where('user_id', auth()->id())
    ->findOrFail($id);
```

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
