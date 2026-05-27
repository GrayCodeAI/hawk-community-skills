---
name: arezv-spec-driven-workflow
description: Use when the user asks to write specs before code, define acceptance
  criteria, plan features before implementation, generate tests from specifications,
  or follow spec-first development practices.
license: MIT
tags:
- general
---

## Tools

| Script | Purpose | Key Flags |
|--------|---------|-----------|
| `spec_generator.py` | Generate spec template from feature name/description | `--name`, `--description`, `--format`, `--json` |
| `spec_validator.py` | Validate spec completeness (0-100 score) | `--file`, `--strict`, `--json` |
| `test_extractor.py` | Extract test stubs from acceptance criteria | `--file`, `--framework`, `--output`, `--json` |

```bash
# Generate a spec template
python spec_generator.py --name "User Authentication" --description "OAuth 2.0 login flow"

# Validate a spec
python spec_validator.py --file specs/auth.md --strict

# Extract test cases
python test_extractor.py --file specs/auth.md --framework pytest --output tests/test_auth.py
```
