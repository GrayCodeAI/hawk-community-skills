"""Tests for scripts/validate-skill-manifest.py manifest schema validation."""

import importlib.util
import sys
import textwrap
from pathlib import Path

import pytest

# Load the validator from its hyphenated filename — not importable as a module name.
_script = Path(__file__).parent.parent / "scripts" / "validate-skill-manifest.py"
_spec = importlib.util.spec_from_file_location("validate_skill_manifest", _script)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
parse_frontmatter = _mod.parse_frontmatter
validate = _mod.validate


def skill_md(tmp_path: Path, frontmatter: str) -> Path:
    """Write a temporary SKILL.md with the given frontmatter."""
    p = tmp_path / "SKILL.md"
    p.write_text(f"---\n{textwrap.dedent(frontmatter)}---\n# Body\nContent.\n")
    return p


VALID_FRONTMATTER = """\
name: my-cool-skill
description: Does something useful for developers.
version: "1.0"
author: jdoe
license: MIT
domain: coding
tags: [python, refactoring]
"""


def test_valid_manifest(tmp_path):
    p = skill_md(tmp_path, VALID_FRONTMATTER)
    data, err = parse_frontmatter(p)
    assert err == "", f"unexpected parse error: {err}"
    errors = validate(data, p)
    assert errors == []


def test_missing_required_field(tmp_path):
    fm = VALID_FRONTMATTER.replace("license: MIT\n", "")
    p = skill_md(tmp_path, fm)
    data, err = parse_frontmatter(p)
    assert err == ""
    errors = validate(data, p)
    assert any("license" in e for e in errors)


def test_invalid_name_pattern(tmp_path):
    fm = VALID_FRONTMATTER.replace("name: my-cool-skill", "name: My Cool Skill!")
    p = skill_md(tmp_path, fm)
    data, _ = parse_frontmatter(p)
    errors = validate(data, p)
    assert any("name" in e for e in errors)


def test_invalid_domain(tmp_path):
    fm = VALID_FRONTMATTER.replace("domain: coding", "domain: magic")
    p = skill_md(tmp_path, fm)
    data, _ = parse_frontmatter(p)
    errors = validate(data, p)
    assert any("domain" in e for e in errors)


def test_invalid_license(tmp_path):
    fm = VALID_FRONTMATTER.replace("license: MIT", "license: WTFPL")
    p = skill_md(tmp_path, fm)
    data, _ = parse_frontmatter(p)
    errors = validate(data, p)
    assert any("license" in e for e in errors)


def test_description_too_long(tmp_path):
    long_desc = "x" * 300
    fm = VALID_FRONTMATTER.replace(
        "description: Does something useful for developers.",
        f"description: {long_desc}",
    )
    p = skill_md(tmp_path, fm)
    data, _ = parse_frontmatter(p)
    errors = validate(data, p)
    assert any("description" in e for e in errors)


def test_optional_phase_valid(tmp_path):
    fm = VALID_FRONTMATTER + "phase: review\n"
    p = skill_md(tmp_path, fm)
    data, _ = parse_frontmatter(p)
    errors = validate(data, p)
    assert errors == []


def test_optional_phase_invalid(tmp_path):
    fm = VALID_FRONTMATTER + "phase: nonexistent\n"
    p = skill_md(tmp_path, fm)
    data, _ = parse_frontmatter(p)
    errors = validate(data, p)
    assert any("phase" in e for e in errors)


def test_no_frontmatter(tmp_path):
    p = tmp_path / "SKILL.md"
    p.write_text("# No frontmatter here\n")
    _, err = parse_frontmatter(p)
    assert err != ""


def test_empty_tags(tmp_path):
    fm = VALID_FRONTMATTER.replace("tags: [python, refactoring]", "tags: []")
    p = skill_md(tmp_path, fm)
    data, _ = parse_frontmatter(p)
    errors = validate(data, p)
    assert any("tags" in e for e in errors)
