---
name: extra-swift-testing-playbook
description: Comprehensive guide for migrating from XCTest to Swift Testing with best
  practices from WWDC 2024
license: MIT
tags:
- cursor-rules
alwaysApply: false
---

## **Appendix: Evergreen Testing Principles (The F.I.R.S.T. Principles)**

These foundational principles are framework-agnostic, and Swift Testing is designed to make adhering to them easier than ever.

| Principle | Meaning | Swift Testing Application |
|---|---|---|
| **Fast** | Tests must execute in milliseconds. | Lean on default parallelism. Use `.serialized` sparingly. |
| **Isolated**| Tests must not depend on each other. | Swift Testing enforces this by creating a new suite instance for every test. Random execution order helps surface violations. |
| **Repeatable** | A test must produce the same result every time. | Control all inputs (dates, network responses) with mocks/stubs. Reset state in `init`/`deinit`. |
| **Self-Validating**| The test must automatically report pass or fail. | Use `#expect` and `#require`. Never rely on `print()` for validation. |
| **Timely**| Write tests alongside the production code. | Use parameterized tests (`@Test(arguments:)`) to easily cover edge cases as you write code. |
