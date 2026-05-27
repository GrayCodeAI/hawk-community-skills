---
name: arezv-tdd-guide
description: Test-driven development skill for writing unit tests, generating test
  fixtures and mocks, analyzing coverage gaps, and guiding red-green-refactor workflows
  across Jest, Pytest, JUnit, Vitest, and M...
license: MIT
tags:
- general
---

## Limitations

| Scope | Details |
|-------|---------|
| Unit test focus | Integration and E2E tests require different patterns |
| Static analysis | Cannot execute tests or measure runtime behavior |
| Language support | Best for TypeScript, JavaScript, Python, Java |
| Report formats | LCOV, JSON, XML only; other formats need conversion |
| Generated tests | Provide scaffolding; require human review for complex logic |

**When to use other tools:**
- E2E testing: Playwright, Cypress, Selenium
- Performance testing: k6, JMeter, Locust
- Security testing: OWASP ZAP, Burp Suite
