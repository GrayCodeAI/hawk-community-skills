---
name: arezv-pr-review-expert
description: Use when the user asks to review pull requests, analyze code changes,
  check for security issues in PRs, or assess code quality of diffs.
license: MIT
tags:
- general
---

## Best Practices

1. Read the linked ticket before looking at code — context prevents false positives
2. Check CI status before reviewing — don't review code that fails to build
3. Prioritize blast radius and security over style
4. Reproduce locally for non-trivial auth or performance changes
5. Label each comment clearly: "nit:", "must:", "question:", "suggestion:"
6. Batch all comments in one review round — don't trickle feedback
7. Acknowledge good patterns, not just problems — specific praise improves culture
