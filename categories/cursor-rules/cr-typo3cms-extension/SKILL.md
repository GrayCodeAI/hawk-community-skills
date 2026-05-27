---
name: cr-typo3cms-extension
description: Cursor rules for typo3cms-extension
license: MIT
tags:
- cursor-rules
- tested
domain: engineering
version: 1.0
author: PatrickJS/awesome-cursorrules
---

### 4. Testing and Documentation

#### ✅ Testing Strategy

- Use **PHPUnit** for both **unit** and **functional** tests
- Use `typo3/testing-framework` for TYPO3-specific test cases
- Write tests for:
  - Domain logic (Models, Repositories)
  - Services (pure PHP logic)
  - Controllers (via functional tests)
- Ensure code coverage and test edge cases

#### 📚 Documentation Structure

- `README.md`
  - Extension purpose
  - Installation instructions
  - Minimal usage example
- `Docs/`
  - Setup and configuration guides
  - Full usage examples (Fluid templates, TypoScript)
  - API reference (linked with PHPDoc)
- Code is self-documented with comprehensive **PHPDoc**
