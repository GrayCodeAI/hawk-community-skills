---
name: arezv-api-test-suite-builder
description: Use when the user asks to generate API tests, create integration test
  suites, test REST endpoints, or build contract tests.
license: MIT
tags:
- general
---

## Best Practices

1. One describe block per endpoint — keeps failures isolated and readable
2. Seed minimal data — don't load the entire DB; create only what the test needs
3. Use `beforeAll` for shared setup, `afterAll` for cleanup — not `beforeEach` for expensive ops
4. Assert specific error messages/fields, not just status codes
5. Test that sensitive fields (password, secret) are never in responses
6. For auth tests, always test the "missing header" case separately from "invalid token"
7. Add rate limit tests last — they can interfere with other test suites if run in parallel
