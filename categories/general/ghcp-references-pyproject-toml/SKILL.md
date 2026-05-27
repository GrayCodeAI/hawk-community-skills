---
name: ghcp-references-pyproject-toml
description: 'Skill: ghcp-references-pyproject-toml'
license: MIT
tags:
- general
---

## 8. Typed Package (PEP 561)

A properly declared typed package means mypy, pyright, and IDEs automatically pick up your type
hints without any extra configuration from your users.

### Step 1: Create the marker file

```bash
# The file must exist; its content doesn't matter — its presence is the signal.
touch your_package/py.typed
```

### Step 2: Include it in the wheel

Already in the template above:

```toml
[tool.setuptools.package-data]
your_package = ["py.typed"]
```

### Step 3: Add the PyPI classifier

```toml
classifiers = [
    ...
    "Typing :: Typed",
]
```

### Step 4: Type-annotate all public functions

```python
# Good — fully typed
def process(
    self,
    data: dict[str, object],
    *,
    timeout: int = 30,
) -> dict[str, object]:
    ...

# Bad — mypy will flag this, and IDEs give no completions to users
def process(self, data, timeout=30):
    ...
```

### Step 5: Verify py.typed ships in the wheel

```bash
python -m build
unzip -l dist/your_package-*.whl | grep py.typed
# Must show: your_package/py.typed
```

If it's missing, check your `[tool.setuptools.package-data]` config.
