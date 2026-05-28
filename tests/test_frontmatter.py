"""Tests for tools/frontmatter.py - shared YAML frontmatter parsing."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))

from frontmatter import parse_frontmatter, parse_frontmatter_dict


# ---------------------------------------------------------------------------
# parse_frontmatter
# ---------------------------------------------------------------------------


class TestParseFrontmatter:
    def test_valid_frontmatter(self):
        content = "---\nname: my-skill\ndescription: A useful skill\nlicense: MIT\n---\n\nBody text here."
        fm, body = parse_frontmatter(content)
        assert fm == {"name": "my-skill", "description": "A useful skill", "license": "MIT"}
        assert "Body text here." in body

    def test_no_frontmatter_returns_original(self):
        content = "# Just a heading\n\nNo frontmatter here."
        fm, body = parse_frontmatter(content)
        assert fm is None
        assert body == content

    def test_missing_closing_delimiter(self):
        content = "---\nname: broken\nNo closing delimiter"
        fm, body = parse_frontmatter(content)
        assert fm is None
        assert body == content

    def test_malformed_yaml(self):
        content = "---\n: [[[\n---\nBody"
        fm, body = parse_frontmatter(content)
        assert fm is None
        assert body == content

    def test_non_dict_yaml_returns_none(self):
        """YAML that parses to a list (not a dict) should return None."""
        content = "---\n- item1\n- item2\n---\nBody"
        fm, body = parse_frontmatter(content)
        assert fm is None

    def test_empty_frontmatter_returns_none(self):
        content = "---\n---\nBody"
        fm, body = parse_frontmatter(content)
        assert fm is None

    def test_frontmatter_with_colons_in_values(self):
        content = '---\nurl: "https://example.com"\ntime: "10:30:00"\n---\n\nBody'
        fm, body = parse_frontmatter(content)
        assert fm is not None
        assert fm["url"] == "https://example.com"
        assert fm["time"] == "10:30:00"

    def test_frontmatter_with_multiline_body(self):
        content = "---\nname: x\n---\n\nLine 1\n\nLine 2\n\nLine 3"
        fm, body = parse_frontmatter(content)
        assert fm == {"name": "x"}
        assert "Line 1" in body
        assert "Line 3" in body

    def test_frontmatter_body_preserved(self):
        """Body content after the closing --- should contain all the original text."""
        content = "---\nname: x\n---\n\n# Heading\n\nSome content\n\n- list item\n"
        fm, body = parse_frontmatter(content)
        assert fm == {"name": "x"}
        assert "# Heading" in body
        assert "Some content" in body
        assert "- list item" in body

    def test_frontmatter_with_list_values(self):
        content = "---\ntags:\n  - python\n  - testing\n---\n\nBody"
        fm, body = parse_frontmatter(content)
        assert fm == {"tags": ["python", "testing"]}

    def test_frontmatter_with_boolean_values(self):
        content = "---\nname: x\npublic: true\n---\n\nBody"
        fm, body = parse_frontmatter(content)
        assert fm["public"] is True

    def test_closing_delimiter_not_confused_with_value(self):
        """A --- inside a quoted YAML value should not close the frontmatter."""
        content = '---\nname: test\ndescription: "has --- inside"\n---\n\nBody'
        fm, body = parse_frontmatter(content)
        assert fm is not None
        assert fm["name"] == "test"

    def test_empty_string_input(self):
        fm, body = parse_frontmatter("")
        assert fm is None
        assert body == ""

    def test_only_whitespace(self):
        fm, body = parse_frontmatter("   \n  \n")
        assert fm is None


# ---------------------------------------------------------------------------
# parse_frontmatter_dict
# ---------------------------------------------------------------------------


class TestParseFrontmatterDict:
    def test_returns_dict_for_valid(self):
        content = "---\nname: x\nlicense: MIT\n---\n\nBody"
        result = parse_frontmatter_dict(content)
        assert result == {"name": "x", "license": "MIT"}

    def test_returns_none_for_no_frontmatter(self):
        result = parse_frontmatter_dict("# Just a heading")
        assert result is None

    def test_returns_none_for_malformed(self):
        result = parse_frontmatter_dict("---\n: [[[\n---\nBody")
        assert result is None

    def test_returns_none_for_list_yaml(self):
        result = parse_frontmatter_dict("---\n- a\n- b\n---\nBody")
        assert result is None

    def test_equivalent_to_first_element_of_parse_frontmatter(self):
        content = "---\nname: y\n---\n\nContent"
        dict_result = parse_frontmatter_dict(content)
        tuple_result, _ = parse_frontmatter(content)
        assert dict_result == tuple_result
