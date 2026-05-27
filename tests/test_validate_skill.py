"""Tests for tools/validate_skill.py."""

from __future__ import annotations

import textwrap
from pathlib import Path

import pytest

# Add tools/ to path so we can import the module under test
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))

from validate_skill import (
    ValidationResult,
    parse_frontmatter,
    validate_skill,
    find_all_skills,
    REQUIRED_FIELDS,
    MAX_DESCRIPTION_LEN,
    TAG_PATTERN,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def skill_dir(tmp_path: Path) -> Path:
    """Create a minimal valid skill directory."""
    d = tmp_path / "test-skill"
    d.mkdir()
    (d / "SKILL.md").write_text(
        textwrap.dedent("""\
        ---
        name: test-skill
        description: A test skill
        license: MIT
        tags: [testing, example]
        ---

        # Test Skill

        ## Overview

        This is a test skill for unit testing.

        ## Instructions

        Do the thing.
        """),
        encoding="utf-8",
    )
    return d


# ---------------------------------------------------------------------------
# parse_frontmatter
# ---------------------------------------------------------------------------


class TestParseFrontmatter:
    def test_valid_frontmatter(self):
        content = "---\nname: foo\ndescription: bar\n---\n\nBody here"
        fm, body = parse_frontmatter(content)
        assert fm == {"name": "foo", "description": "bar"}
        assert "Body here" in body

    def test_no_frontmatter(self):
        content = "# Just a heading\n\nNo frontmatter"
        fm, body = parse_frontmatter(content)
        assert fm is None
        assert body == content

    def test_malformed_yaml(self):
        content = "---\n: invalid: yaml: [[[\n---\nBody"
        fm, body = parse_frontmatter(content)
        assert fm is None

    def test_empty_frontmatter(self):
        content = "---\n---\nBody"
        fm, body = parse_frontmatter(content)
        # Empty YAML parses as None, not a dict
        assert fm is None

    def test_frontmatter_with_multiline_body(self):
        content = "---\nname: x\n---\n\nLine 1\n\nLine 2\n\nLine 3"
        fm, body = parse_frontmatter(content)
        assert fm == {"name": "x"}
        assert "Line 1" in body
        assert "Line 3" in body


# ---------------------------------------------------------------------------
# ValidationResult
# ---------------------------------------------------------------------------


class TestValidationResult:
    def test_passed_when_no_errors(self, tmp_path: Path):
        r = ValidationResult(tmp_path)
        assert r.passed is True
        assert r.errors == []
        assert r.warnings == []

    def test_failed_when_errors(self, tmp_path: Path):
        r = ValidationResult(tmp_path)
        r.error("something broke")
        assert r.passed is False
        assert len(r.errors) == 1

    def test_warnings_d_not_affect_pass(self, tmp_path: Path):
        r = ValidationResult(tmp_path)
        r.warn("just a warning")
        assert r.passed is True
        assert len(r.warnings) == 1


# ---------------------------------------------------------------------------
# validate_skill - happy path
# ---------------------------------------------------------------------------


class TestValidateSkill:
    def test_valid_skill_passes(self, skill_dir: Path):
        result = validate_skill(skill_dir)
        assert result.passed is True
        assert result.errors == []

    def test_missing_skill_md(self, tmp_path: Path):
        d = tmp_path / "empty-skill"
        d.mkdir()
        result = validate_skill(d)
        assert result.passed is False
        assert any("SKILL.md not found" in e for e in result.errors)

    def test_no_frontmatter(self, tmp_path: Path):
        d = tmp_path / "no-fm"
        d.mkdir()
        (d / "SKILL.md").write_text("# Just a heading\n\nSome body text without frontmatter.\n", encoding="utf-8")
        result = validate_skill(d)
        assert result.passed is False
        assert any("no valid YAML frontmatter" in e for e in result.errors)

    def test_missing_required_fields(self, tmp_path: Path):
        d = tmp_path / "missing-fields"
        d.mkdir()
        (d / "SKILL.md").write_text(
            "---\nname: missing-fields\n---\n\nBody\n", encoding="utf-8"
        )
        result = validate_skill(d)
        assert result.passed is False
        error_text = " ".join(result.errors)
        assert "description" in error_text
        assert "license" in error_text

    def test_name_mismatch(self, tmp_path: Path):
        d = tmp_path / "dir-name"
        d.mkdir()
        (d / "SKILL.md").write_text(
            "---\nname: different-name\ndescription: x\nlicense: MIT\ntags: [a]\n---\n\nBody\n",
            encoding="utf-8",
        )
        result = validate_skill(d)
        assert any("does not match directory name" in e for e in result.errors)

    def test_description_too_long(self, skill_dir: Path):
        long_desc = "x" * 250
        (skill_dir / "SKILL.md").write_text(
            f"---\nname: test-skill\ndescription: {long_desc}\nlicense: MIT\ntags: [a]\n---\n\nBody\n",
            encoding="utf-8",
        )
        result = validate_skill(skill_dir)
        assert any("250 chars" in w for w in result.warnings)

    def test_no_tags(self, tmp_path: Path):
        d = tmp_path / "no-tags"
        d.mkdir()
        (d / "SKILL.md").write_text(
            "---\nname: no-tags\ndescription: x\nlicense: MIT\ntags: []\n---\n\nBody\n",
            encoding="utf-8",
        )
        result = validate_skill(d)
        assert any("at least 1 tag" in e for e in result.errors)

    def test_invalid_tag_format(self, tmp_path: Path):
        d = tmp_path / "bad-tags"
        d.mkdir()
        (d / "SKILL.md").write_text(
            "---\nname: bad-tags\ndescription: x\nlicense: MIT\ntags: [Bad_Tag!]\n---\n\nBody\n",
            encoding="utf-8",
        )
        result = validate_skill(d)
        assert any("invalid" in e.lower() for e in result.errors)

    def test_broken_internal_link(self, skill_dir: Path):
        (skill_dir / "SKILL.md").write_text(
            "---\nname: test-skill\ndescription: A test\nlicense: MIT\ntags: [a]\n---\n\n"
            "# Test\n\nSee [broken](nonexistent.md) for details.\n",
            encoding="utf-8",
        )
        result = validate_skill(skill_dir)
        assert any("Broken internal reference" in w for w in result.warnings)

    def test_script_missing_shebang(self, skill_dir: Path):
        scripts = skill_dir / "scripts"
        scripts.mkdir()
        script = scripts / "run.sh"
        script.write_text("echo hello\n", encoding="utf-8")
        script.chmod(0o755)
        result = validate_skill(skill_dir)
        assert any("missing shebang" in w for w in result.warnings)

    def test_script_not_executable(self, skill_dir: Path):
        scripts = skill_dir / "scripts"
        scripts.mkdir()
        script = scripts / "run.py"
        script.write_text("#!/usr/bin/env python3\nprint('hi')\n", encoding="utf-8")
        script.chmod(0o644)
        result = validate_skill(skill_dir)
        assert any("not executable" in w for w in result.warnings)

    def test_utf8_error(self, tmp_path: Path):
        d = tmp_path / "bad-encoding"
        d.mkdir()
        skill_md = d / "SKILL.md"
        skill_md.write_bytes(b"\x80\x81\x82\x83")
        result = validate_skill(d)
        assert any("UTF-8" in e for e in result.errors)


# ---------------------------------------------------------------------------
# TAG_PATTERN regex
# ---------------------------------------------------------------------------


class TestTagPattern:
    @pytest.mark.parametrize(
        "tag",
        ["python", "ai-ml", "web3", "a", "my-cool-tag"],
    )
    def test_valid_tags(self, tag: str):
        assert TAG_PATTERN.match(tag), f"Expected '{tag}' to be valid"

    @pytest.mark.parametrize(
        "tag",
        ["Python", "AI_ML", "-bad", "bad-", "1bad", "has space", "UPPER", ""],
    )
    def test_invalid_tags(self, tag: str):
        assert not TAG_PATTERN.match(tag), f"Expected '{tag}' to be invalid"


# ---------------------------------------------------------------------------
# find_all_skills
# ---------------------------------------------------------------------------


class TestFindAllSkills:
    def test_finds_skills_in_categories(self, tmp_path: Path):
        """Simulate categories/<cat>/<skill>/SKILL.md layout."""
        import validate_skill as vs

        original = vs.CATEGORIES_DIR
        try:
            cats = tmp_path / "categories"
            cats.mkdir()
            cat = cats / "python"
            cat.mkdir()
            skill = cat / "my-skill"
            skill.mkdir()
            (skill / "SKILL.md").write_text("---\nname: x\n---\n\nBody\n", encoding="utf-8")
            vs.CATEGORIES_DIR = cats

            found = find_all_skills()
            assert len(found) == 1
            assert found[0].name == "my-skill"
        finally:
            vs.CATEGORIES_DIR = original

    def test_empty_categories(self, tmp_path: Path):
        import validate_skill as vs

        original = vs.CATEGORIES_DIR
        try:
            cats = tmp_path / "empty-cats"
            cats.mkdir()
            vs.CATEGORIES_DIR = cats
            assert find_all_skills() == []
        finally:
            vs.CATEGORIES_DIR = original
