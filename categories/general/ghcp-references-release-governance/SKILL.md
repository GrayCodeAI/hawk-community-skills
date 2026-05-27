---
name: ghcp-references-release-governance
description: 'Skill: ghcp-references-release-governance'
license: MIT
tags:
- general
---

## 8. Full `publish.yml` with Governance Gates

Complete workflow combining tag validation, author check, TestPyPI gate, and production publish.

```yaml
# .github/workflows/publish.yml
name: Publish to PyPI

on:
  push:
    tags:
      - "v[0-9]+.[0-9]+.[0-9]+*"

jobs:
  publish:
    name: Build, validate, and publish
    runs-on: ubuntu-latest
    environment: release
    permissions:
      id-token: write
      contents: read

    steps:
      - name: Validate release tag format
        run: |
          if [[ ! "${GITHUB_REF}" =~ ^refs/tags/v[0-9]+\.[0-9]+\.[0-9]+(a[0-9]*|b[0-9]*|rc[0-9]*|\.post[0-9]*)?$ ]]; then
            echo "::error::Invalid tag format: ${GITHUB_REF}"
            exit 1
          fi

      - name: Validate tag author
        run: |
          ALLOWED_USERS=("your-github-username")
          if [[ ! " ${ALLOWED_USERS[*]} " =~ " ${GITHUB_ACTOR} " ]]; then
            echo "::error::${GITHUB_ACTOR} is not authorised to release."
            exit 1
          fi

      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install build tooling
        run: pip install build twine

      - name: Build
        run: python -m build

      - name: Validate distributions
        run: twine check dist/*

      - name: Publish to TestPyPI
        uses: pypa/gh-action-pypi-publish@release/v1
        with:
          repository-url: https://test.pypi.org/legacy/
        continue-on-error: true   # Non-fatal; remove if you always want this to pass

      - name: Publish to PyPI
        uses: pypa/gh-action-pypi-publish@release/v1
```

### Security checklist

- [ ] PyPI Trusted Publishing configured (no API token stored in GitHub)
- [ ] GitHub `release` environment has branch protection: tags matching `v*` only
- [ ] Tag format validation step is the first step in the job
- [ ] Allowed-users list is maintained and reviewed regularly
- [ ] No secrets printed in logs (check all `echo` and `run` steps)
- [ ] `permissions:` is scoped to `id-token: write` only — no `write-all`
