---
name: ghcp-references-versioning-strategy
description: 'Skill: ghcp-references-versioning-strategy'
license: MIT
tags:
- general
---

## 11. PyPA Release Commands

The canonical sequence from code to user install.

```bash
# Step 1: Tag the release (triggers CI publish.yml automatically if configured)
git tag -a v1.2.3 -m "Release v1.2.3"
git push origin v1.2.3

# Step 2 (manual fallback only): Build locally
python -m build
# Produces:
#   dist/your_package-1.2.3.tar.gz   (sdist)
#   dist/your_package-1.2.3-py3-none-any.whl  (wheel)

# Step 3: Validate
twine check dist/*

# Step 4: Test on TestPyPI first (first release or major change)
twine upload --repository testpypi dist/*
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ your-package==1.2.3

# Step 5: Publish to production PyPI
twine upload dist/*
# OR via GitHub Actions (recommended):
# push the tag → publish.yml runs → pypa/gh-action-pypi-publish handles upload via OIDC

# Step 6: Verify
pip install your-package==1.2.3
python -c "import your_package; print(your_package.__version__)"
```
