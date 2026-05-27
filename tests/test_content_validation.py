"""Tests for tools/content_validation.py - skill content/body validation."""

from __future__ import annotations

import sys
import textwrap
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))

from content_validation import (
    BodyValidationResult,
    parse_frontmatter,
    _extract_headings,
    _strip_comments_and_whitespace,
    validate_content_body,
    REQUIRED_SECTIONS,
    RECOMMENDED_SECTIONS,
    VALID_LICENSES,
    MIN_BODY_LENGTH,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def good_skill(tmp_path: Path) -> Path:
    """A skill that should pass all content body checks."""
    d = tmp_path / "good-skill"
    d.mkdir()
    (d / "SKILL.md").write_text(
        textwrap.dedent("""\
        ---
        name: good-skill
        description: A fully valid skill
        license: MIT
        tags: [example, testing]
        ---

        # Good Skill

        ## Overview

        This skill does amazing things with data processing pipelines.
        It handles complex transformations and outputs clean results.

        ## When to Use

        Use this skill when you need to process data efficiently.

        ## Instructions

        1. Provide input data in CSV format
        2. Run the skill
        3. Collect the output

        The skill will automatically detect column types and apply
        appropriate transformations.

        ## References

        - [Data Processing Guide](https://example.com)
        """),
        encoding="utf-8",
    )
    return d


@pytest.fixture
def minimal_skill(tmp_path: Path) -> Path:
    """A skill with only the minimum required content."""
    d = tmp_path / "minimal-skill"
    d.mkdir()
    (d / "SKILL.md").write_text(
        textwrap.dedent("""\
        ---
        name: minimal-skill
        description: Minimal skill
        license: MIT
        tags: [test]
        ---

        # Minimal Skill

        ## Overview

        This is a minimal skill with just enough content to pass validation.

        ## Instructions

        Follow these steps to use the skill effectively. Do the thing.
        """),
        encoding="utf-8",
    )
    return d


# ---------------------------------------------------------------------------
# parse_frontmatter
# ---------------------------------------------------------------------------


class TestParseFrontmatter:
    def test_valid_frontmatter(self):
        content = "---\nname: x\nlicense: MIT\n---\n\nBody text"
        fm, body = parse_frontmatter(content)
        assert fm == {"name": "x", "license": "MIT"}
        assert "Body text" in body

    def test_no_frontmatter(self):
        fm, body = parse_frontmatter("# No frontmatter\n\nJust text")
        assert fm is None

    def test_malformed_yaml(self):
        fm, body = parse_frontmatter("---\n: [[[\n---\nBody")
        assert fm is None

    def test_non_dict_yaml(self):
        fm, body = parse_frontmatter("---\n- item1\n- item2\n---\nBody")
        assert fm is None


# ---------------------------------------------------------------------------
# _extract_headings
# ---------------------------------------------------------------------------


class TestExtractHeadings:
    def test_h1_and_h2(self):
        body = "# Title\n\n## Section One\n\ntext\n\n## Section Two"
        headings = _extract_headings(body)
        assert headings == ["Title", "Section One", "Section Two"]

    def test_no_headings(self):
        body = "\n\nJust plain text\nwith no headings\n"
        assert _extract_headings(body) == []

    def test_mixed_levels(self):
        body = "# H1\n## H2\n### H3\n#### H4"
        headings = _extract_headings(body)
        assert headings == ["H1", "H2", "H3", "H4"]

    def test_headings_with_extra_whitespace(self):
        body = "#   Spaced Heading   \n##\tTabbed"
        headings = _extract_headings(body)
        assert headings == ["Spaced Heading", "Tabbed"]


# ---------------------------------------------------------------------------
# _strip_comments_and_whitespace
# ---------------------------------------------------------------------------


class TestStripComments:
    def test_removes_html_comments(self):
        body = "Text <!-- comment --> more text"
        assert "comment" not in _strip_comments_and_whitespace(body)

    def test_multiline_comments(self):
        body = "Before\n<!--\nmultiline\ncomment\n-->\nAfter"
        result = _strip_comments_and_whitespace(body)
        assert "multiline" not in result
        assert "Before" in result
        assert "After" in result

    def test_strips_whitespace(self):
        body = "\n\n   content   \n\n"
        assert _strip_comments_and_whitespace(body) == "content"

    def test_empty_after_stripping(self):
        body = "<!-- just a comment -->"
        assert _strip_comments_and_whitespace(body) == ""


# ---------------------------------------------------------------------------
# BodyValidationResult
# ---------------------------------------------------------------------------


class TestBodyValidationResult:
    def test_passed_when_no_errors(self, tmp_path: Path):
        r = BodyValidationResult(tmp_path)
        assert r.passed is True

    def test_failed_when_errors(self, tmp_path: Path):
        r = BodyValidationResult(tmp_path)
        r.error("bad")
        assert r.passed is False

    def test_warnings_dont_fail(self, tmp_path: Path):
        r = BodyValidationResult(tmp_path)
        r.warn("just warning")
        assert r.passed is True


# ---------------------------------------------------------------------------
# validate_content_body - happy path
# ---------------------------------------------------------------------------


class TestValidateContentBody:
    def test_good_skill_passes(self, good_skill: Path):
        result = validate_content_body(good_skill)
        assert result.passed is True
        assert result.errors == []

    def test_minimal_skill_passes(self, minimal_skill: Path):
        result = validate_content_body(minimal_skill)
        assert result.passed is True


# ---------------------------------------------------------------------------
# validate_content_body - missing SKILL.md
# ---------------------------------------------------------------------------


class TestMissingSkillMd:
    def test_no_skill_md(self, tmp_path: Path):
        d = tmp_path / "no-file"
        d.mkdir()
        result = validate_content_body(d)
        assert result.passed is False
        assert any("SKILL.md not found" in e for e in result.errors)

    def test_invalid_utf8(self, tmp_path: Path):
        d = tmp_path / "bad-encoding"
        d.mkdir()
        (d / "SKILL.md").write_bytes(b"\x80\x81\x82")
        result = validate_content_body(d)
        assert any("UTF-8" in e for e in result.errors)


# ---------------------------------------------------------------------------
# validate_content_body - frontmatter issues
# ---------------------------------------------------------------------------


class TestFrontmatterValidation:
    def test_no_frontmatter(self, tmp_path: Path):
        d = tmp_path / "no-fm"
        d.mkdir()
        (d / "SKILL.md").write_text("# Skill\n\n## Overview\n\nContent here.\n", encoding="utf-8")
        result = validate_content_body(d)
        assert any("no valid YAML frontmatter" in e for e in result.errors)

    def test_valid_license(self, tmp_path: Path):
        d = tmp_path / "valid-license"
        d.mkdir()
        (d / "SKILL.md").write_text(
            "---\nname: x\nlicense: MIT\ntags: [a]\n---\n\n# X\n\n## Overview\n\nContent.\n\n## Instructions\n\nDo stuff.\n",
            encoding="utf-8",
        )
        result = validate_content_body(d)
        assert not any("License" in w for w in result.warnings)

    def test_unknown_license_warns(self, tmp_path: Path):
        d = tmp_path / "unknown-license"
        d.mkdir()
        (d / "SKILL.md").write_text(
            "---\nname: x\nlicense: Custom-License\ntags: [a]\n---\n\n# X\n\n## Overview\n\nContent here.\n\n## Instructions\n\nDo stuff.\n",
            encoding="utf-8",
        )
        result = validate_content_body(d)
        assert any("Custom-License" in w for w in result.warnings)


# ---------------------------------------------------------------------------
# validate_content_body - required sections
# ---------------------------------------------------------------------------


class TestRequiredSections:
    def test_missing_overview(self, tmp_path: Path):
        d = tmp_path / "no-overview"
        d.mkdir()
        (d / "SKILL.md").write_text(
            "---\nname: x\nlicense: MIT\ntags: [a]\n---\n\n# X\n\n## Instructions\n\nDo stuff with enough content to pass the length check.\n",
            encoding="utf-8",
        )
        result = validate_content_body(d)
        assert any("Overview" in e for e in result.errors)

    def test_missing_instructions(self, tmp_path: Path):
        d = tmp_path / "no-instructions"
        d.mkdir()
        (d / "SKILL.md").write_text(
            "---\nname: x\nlicense: MIT\ntags: [a]\n---\n\n# X\n\n## Overview\n\nThis skill does things and has enough content.\n",
            encoding="utf-8",
        )
        result = validate_content_body(d)
        assert any("Instructions" in e for e in result.errors)


# ---------------------------------------------------------------------------
# validate_content_body - recommended sections
# ---------------------------------------------------------------------------


class TestRecommendedSections:
    def test_missing_when_to_use_warns(self, tmp_path: Path):
        d = tmp_path / "no-wtu"
        d.mkdir()
        (d / "SKILL.md").write_text(
            "---\nname: x\nlicense: MIT\ntags: [a]\n---\n\n# X\n\n## Overview\n\nEnough content here to pass the length check easily.\n\n## Instructions\n\nDo things with this skill.\n",
            encoding="utf-8",
        )
        result = validate_content_body(d)
        assert any("When to Use" in w for w in result.warnings)

    def test_missing_references_warns(self, tmp_path: Path):
        d = tmp_path / "no-refs"
        d.mkdir()
        (d / "SKILL.md").write_text(
            "---\nname: x\nlicense: MIT\ntags: [a]\n---\n\n# X\n\n## Overview\n\nEnough content.\n\n## When to Use\n\nWhen needed.\n\n## Instructions\n\nDo things.\n",
            encoding="utf-8",
        )
        result = validate_content_body(d)
        assert any("References" in w for w in result.warnings)


# ---------------------------------------------------------------------------
# validate_content_body - body too short
# ---------------------------------------------------------------------------


class TestBodyTooShort:
    def test_empty_body(self, tmp_path: Path):
        d = tmp_path / "empty-body"
        d.mkdir()
        (d / "SKILL.md").write_text(
            "---\nname: x\nlicense: MIT\ntags: [a]\n---\n\n",
            encoding="utf-8",
        )
        result = validate_content_body(d)
        assert any("too short" in e for e in result.errors)

    def test_very_short_body(self, tmp_path: Path):
        d = tmp_path / "short-body"
        d.mkdir()
        (d / "SKILL.md").write_text(
            "---\nname: x\nlicense: MIT\ntags: [a]\n---\n\n# X\n\nShort.\n",
            encoding="utf-8",
        )
        result = validate_content_body(d)
        assert any("too short" in e for e in result.errors)


# ---------------------------------------------------------------------------
# validate_content_body - placeholder-only content
# ---------------------------------------------------------------------------


class TestPlaceholderOnly:
    def test_only_comments(self, tmp_path: Path):
        d = tmp_path / "placeholder"
        d.mkdir()
        (d / "SKILL.md").write_text(
            "---\nname: x\nlicense: MIT\ntags: [a]\n---\n\n# X\n\n<!-- Just a comment -->\n",
            encoding="utf-8",
        )
        result = validate_content_body(d)
        assert any("placeholder" in e.lower() or "too short" in e.lower() for e in result.errors)


# ---------------------------------------------------------------------------
# validate_content_body - duplicate headings
# ---------------------------------------------------------------------------


class TestDuplicateHeadings:
    def test_duplicate_heading_warns(self, tmp_path: Path):
        d = tmp_path / "dup-headings"
        d.mkdir()
        (d / "SKILL.md").write_text(
            "---\nname: x\nlicense: MIT\ntags: [a]\n---\n\n# X\n\n## Overview\n\nContent with enough length.\n\n## Instructions\n\nDo stuff.\n\n## Overview\n\nDuplicate section.\n",
            encoding="utf-8",
        )
        result = validate_content_body(d)
        assert any("Duplicate heading" in w for w in result.warnings)


# ---------------------------------------------------------------------------
# VALID_LICENSES constant
# ---------------------------------------------------------------------------


class TestValidLicenses:
    def test_common_licenses_included(self):
        assert "MIT" in VALID_LICENSES
        assert "Apache-2.0" in VALID_LICENSES
        assert "GPL-3.0" in VALID_LICENSES

    def test_not_empty(self):
        assert len(VALID_LICENSES) >= 3


# ---------------------------------------------------------------------------
# REQUIRED_SECTIONS constant
# ---------------------------------------------------------------------------


class TestRequiredSections:
    def test_overview_required(self):
        assert "overview" in REQUIRED_SECTIONS

    def test_instructions_required(self):
        assert "instructions" in REQUIRED_SECTIONS
