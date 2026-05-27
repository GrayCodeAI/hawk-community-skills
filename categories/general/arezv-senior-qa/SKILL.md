---
name: arezv-senior-qa
description: Generates unit tests, integration tests, and E2E tests for React/Next.js
  applications. Scans components to create Jest + React Testing Library test stubs,
  analyzes Istanbul/LCOV coverage reports to...
license: MIT
tags:
- general
---

## Common Commands

```bash
# Jest
npm test                           # Run all tests
npm test -- --watch                # Watch mode
npm test -- --coverage             # With coverage
npm test -- Button.test.tsx        # Single file

# Playwright
npx playwright test                # Run all E2E tests
npx playwright test --ui           # UI mode
npx playwright test --debug        # Debug mode
npx playwright codegen             # Generate tests

# Coverage
npm test -- --coverage --coverageReporters=lcov,json
python scripts/coverage_analyzer.py coverage/coverage-final.json
```
