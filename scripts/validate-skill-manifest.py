#!/usr/bin/env python3
"""Validate SKILL.md frontmatter against manifest-schema.toml.

Usage:
    python3 scripts/validate-skill-manifest.py path/to/SKILL.md [...]

Exits 0 if all manifests are valid, 1 otherwise.
Designed to be called from CI (lefthook, GitHub Actions).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

ROOT = Path(__file__).parent.parent

# ── Schema (hand-coded from manifest-schema.toml for zero-dep validation) ─────

REQUIRED = {"name", "description", "version", "author", "license", "domain", "tags"}

DOMAIN_ENUM = {
    "coding", "cybersecurity", "data-science", "devops",
    "documentation", "research", "testing", "other",
}

LICENSE_ENUM = {
    "MIT", "Apache-2.0", "GPL-3.0", "BSD-2-Clause",
    "BSD-3-Clause", "CC0-1.0", "MPL-2.0",
}

PHASE_ENUM = {"localize", "repair", "validate", "review", "planning", "any"}

MODEL_ENUM = {"haiku", "sonnet", "opus", "any"}

NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]{2,79}$")
VERSION_RE = re.compile(r"^\d+\.\d+(\.\d+)?$")


def parse_frontmatter(path: Path) -> Tuple[Optional[Dict[str, Any]], str]:
    """Extract YAML frontmatter from a Markdown file.

    Returns (parsed_dict, error_message). On success error_message is empty.
    """
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None, "no YAML frontmatter (file must start with ---)"
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, "malformed frontmatter (no closing ---)"
    try:
        data = yaml.safe_load(parts[1])
    except yaml.YAMLError as e:
        return None, f"YAML parse error: {e}"
    if not isinstance(data, dict):
        return None, "frontmatter must be a YAML mapping"
    return data, ""


def validate(data: Dict[str, Any], path: Path) -> List[str]:
    """Return a list of validation error messages, or an empty list if valid."""
    errors: List[str] = []

    # Required fields
    for field in REQUIRED:
        if field not in data:
            errors.append(f"missing required field: {field!r}")

    name = data.get("name", "")
    if name and not NAME_RE.match(str(name)):
        errors.append(f"name {name!r} must match ^[a-z0-9][a-z0-9-]{{2,79}}$")

    desc = data.get("description", "")
    if desc and len(str(desc)) > 280:
        errors.append(f"description exceeds 280 chars ({len(str(desc))})")

    version = data.get("version", "")
    if version and not VERSION_RE.match(str(version)):
        errors.append(f"version {version!r} must match semver (e.g. '1.0' or '2.3.1')")

    domain = data.get("domain", "")
    if domain and domain not in DOMAIN_ENUM:
        errors.append(f"domain {domain!r} not in {sorted(DOMAIN_ENUM)}")

    license_ = data.get("license", "")
    if license_ and license_ not in LICENSE_ENUM:
        errors.append(f"license {license_!r} not in {sorted(LICENSE_ENUM)}")

    tags = data.get("tags", [])
    if not isinstance(tags, list):
        errors.append("tags must be a list")
    elif len(tags) < 1:
        errors.append("tags must have at least 1 item")
    elif len(tags) > 12:
        errors.append(f"tags must have at most 12 items, got {len(tags)}")

    phase = data.get("phase")
    if phase is not None and phase not in PHASE_ENUM:
        errors.append(f"phase {phase!r} not in {sorted(PHASE_ENUM)}")

    min_model = data.get("min_model")
    if min_model is not None and min_model not in MODEL_ENUM:
        errors.append(f"min_model {min_model!r} not in {sorted(MODEL_ENUM)}")

    ctx = data.get("context_tokens")
    if ctx is not None:
        if not isinstance(ctx, int) or ctx < 256 or ctx > 200_000:
            errors.append(f"context_tokens must be an integer in [256, 200000], got {ctx!r}")

    return errors


def main(argv: List[str]) -> int:
    if not argv:
        print("usage: validate-skill-manifest.py <SKILL.md> [...]", file=sys.stderr)
        return 1

    all_ok = True
    for arg in argv:
        path = Path(arg)
        if not path.exists():
            print(f"ERROR {path}: file not found")
            all_ok = False
            continue
        data, err = parse_frontmatter(path)
        if err:
            print(f"ERROR {path}: {err}")
            all_ok = False
            continue
        errors = validate(data, path)
        if errors:
            all_ok = False
            for e in errors:
                print(f"ERROR {path}: {e}")
        else:
            print(f"  OK  {path}")

    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
