---
name: copilot-python-pypi-package-builder
description: End-to-end skill for building, testing, linting, versioning, and publishing
  a production-grade Python library to PyPI. Covers all four build backends (setuptools+setuptools_scm,
  hatchling, flit, po...
license: MIT
tags:
- general
---

## Where to Go Next

After understanding decisions and structure:

1. **Set up `pyproject.toml`** → `references/pyproject-toml.md`
   All four backend templates (setuptools+scm, hatchling, flit, poetry), full tool configs,
   `py.typed` setup, versioning config.

2. **Write your library code** → `references/library-patterns.md`
   OOP/SOLID principles, type hints (PEP 484/526/544/561), core class design, factory functions,
   `__init__.py`, plugin/backend pattern, CLI entry point.

3. **Add tests and code quality** → `references/testing-quality.md`
   `conftest.py`, unit/backend/async tests, parametrize, ruff/mypy/pre-commit setup.

4. **Set up CI/CD and publish** → `references/ci-publishing.md`
   `ci.yml`, `publish.yml` with Trusted Publishing (OIDC, no API tokens), CHANGELOG format,
   release checklist.

5. **Polish for community/OSS** → `references/community-docs.md`
   README sections, docstring format, CONTRIBUTING, SECURITY, issue templates, anti-patterns
   table, and master release checklist.

6. **Design backends, config, transport, CLI** → `references/architecture-patterns.md`
   Backend system (plugin/strategy pattern), Settings dataclass, HTTP transport layer,
   CLI with click/typer, backend injection rules.

7. **Choose and implement a versioning strategy** → `references/versioning-strategy.md`
   PEP 440 canonical forms, SemVer rules, pre-release identifiers, setuptools_scm deep-dive,
   flit static versioning, decision engine (DEFAULT/BEGINNER/MINIMAL).

8. **Govern releases and secure the publish pipeline** → `references/release-governance.md`
   Branch strategy, branch protection rules, OIDC Trusted Publishing setup, tag author
   validation in CI, tag format enforcement, full governed `publish.yml`.

9. **Simplify tooling with Ruff** → `references/tooling-ruff.md`
   Ruff-only setup replacing black/isort/flake8, mypy config, pre-commit hooks,
   asyncio_mode=auto (remove @pytest.mark.asyncio), migration guide.
