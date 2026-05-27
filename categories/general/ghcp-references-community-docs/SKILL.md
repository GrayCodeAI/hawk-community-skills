---
name: ghcp-references-community-docs
description: 'Skill: ghcp-references-community-docs'
license: MIT
tags:
- general
---

## 8. Master Release Checklist

Run through every item before pushing a release tag. CI must be fully green.

### Code Quality
```
[ ] ruff check . — zero errors
[ ] ruff format . --check — zero formatting issues
[ ] mypy src/your_package/ — zero type errors
[ ] pytest — all tests pass
[ ] Coverage >= 80% (fail_under enforced in pyproject.toml)
[ ] All GitHub Actions CI jobs green (lint + test matrix)
```

### Project Structure
```
[ ] pyproject.toml — name, description, requires-python, license (SPDX string), authors,
    keywords (10+), classifiers (Python versions + Typing :: Typed), urls (all 5 fields)
[ ] dynamic = ["version"] set (if using setuptools_scm or hatch-vcs)
[ ] [tool.setuptools_scm] with local_scheme = "no-local-version"
[ ] setup.py shim present (if using setuptools_scm)
[ ] py.typed marker file exists (empty file in package root)
[ ] py.typed listed in [tool.setuptools.package-data]
[ ] "Typing :: Typed" classifier in pyproject.toml
[ ] __init__.py has __all__ listing all public symbols
[ ] __version__ reads from importlib.metadata (not hardcoded)
```

### Testing
```
[ ] conftest.py has shared fixtures for client and backend
[ ] Core happy path tested
[ ] Error conditions and edge cases tested
[ ] Each backend tested independently in isolation
[ ] asyncio_mode = "auto" in pyproject.toml (for async tests)
[ ] fetch-depth: 0 in all CI checkout steps
```

### CHANGELOG and Docs
```
[ ] CHANGELOG.md: [Unreleased] entries moved to [x.y.z] - YYYY-MM-DD
[ ] README has: description, install commands, quick start, config table, badges
[ ] All public symbols have Google-style docstrings
[ ] CONTRIBUTING.md: dev setup, test/lint commands, PR instructions
[ ] SECURITY.md: supported versions, reporting process with timeline
```

### Versioning
```
[ ] All CI checks pass on the commit you plan to tag
[ ] CHANGELOG.md updated and committed
[ ] Git tag follows format v1.2.3 (semver, v prefix)
[ ] No stale local_scheme suffixes will appear in the built wheel name
```

### CI/CD
```
[ ] ci.yml: lint + mypy + test matrix (all supported Python versions)
[ ] publish.yml: triggered on v*.*.* tags, uses Trusted Publishing (OIDC)
[ ] pypi environment created in GitHub repo Settings → Environments
[ ] No API tokens stored in repository secrets
```

### The Release Command Sequence
```bash
# 1. Run full local validation
ruff check . ; ruff format . --check ; mypy src/your_package/ ; pytest

# 2. Update CHANGELOG.md — move [Unreleased] to [x.y.z]
# 3. Commit the changelog
git add CHANGELOG.md
git commit -m "chore: prepare release vX.Y.Z"

# 4. Tag and push — this triggers publish.yml automatically
git tag vX.Y.Z
git push origin main --tags

# 5. Monitor: https://github.com/<you>/<pkg>/actions
# 6. Verify: https://pypi.org/project/your-package/
```
