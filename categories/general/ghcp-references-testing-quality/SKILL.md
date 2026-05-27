---
name: ghcp-references-testing-quality
description: 'Skill: ghcp-references-testing-quality'
license: MIT
tags:
- general
---

## 6. Pre-commit Hooks

Pre-commit runs all quality tools automatically before each commit, so issues never reach CI.
Install once per clone with `pre-commit install`.

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.4.4
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  - repo: https://github.com/psf/black
    rev: 24.4.2
    hooks:
      - id: black

  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
      - id: isort

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.10.0
    hooks:
      - id: mypy
        additional_dependencies: [types-redis]  # Add stubs for typed dependencies

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-toml
      - id: check-merge-conflict
      - id: debug-statements
      - id: no-commit-to-branch
        args: [--branch, master, --branch, main]
```

```bash
pip install pre-commit
pre-commit install           # Install once per clone
pre-commit run --all-files   # Run all hooks manually (useful before the first install)
```

The `no-commit-to-branch` hook prevents accidentally committing directly to `main`/`master`,
which would bypass CI checks. Always work on a feature branch.
