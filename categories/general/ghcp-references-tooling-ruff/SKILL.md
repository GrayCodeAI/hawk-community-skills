---
name: ghcp-references-tooling-ruff
description: 'Skill: ghcp-references-tooling-ruff'
license: MIT
tags:
- general
---

## 8. Migration Guide — Removing black and isort

If you are converting an existing project that used `black` and `isort`:

```bash
# 1. Remove black and isort from dev dependencies
pip uninstall black isort

# 2. Remove black and isort config sections from pyproject.toml
# [tool.black]  ← delete this section
# [tool.isort]  ← delete this section

# 3. Add ruff to dev dependencies (see Section 2 for config)

# 4. Run ruff format to confirm existing code is already compatible
ruff format --check .
# ruff format is black-compatible; output should be identical

# 5. Update .pre-commit-config.yaml (see Section 4)
# Remove black and isort hooks; add ruff and ruff-format hooks

# 6. Update CI (see Section 7)
# Remove black, isort, flake8 steps; add ruff check + ruff format --check

# 7. Reinstall pre-commit hooks
pre-commit uninstall
pre-commit install
pre-commit run --all-files   # Verify clean
```
