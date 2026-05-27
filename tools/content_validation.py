#!/usr/bin/env python3
"""Content/body validation for hawk-community-skills SKILL.md files.

Checks that the markdown body after frontmatter contains required sections
and follows expected formatting conventions.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml


# --- Constants ---

REQUIRED_SECTIONS = {"overview", "instructions"}
RECOMMENDED_SECTIONS = {"when to use", "references"}

# Display names for sections (avoids .title() capitalizing short words like "to")
_SECTION_DISPLAY: dict[str, str] = {
    "overview": "Overview",
    "instructions": "Instructions",
    "when to use": "When to Use",
    "references": "References",
}


def _section_display(name: str) -> str:
    """Return a nicely formatted display name for a section heading."""
    return _SECTION_DISPLAY.get(name, name.title())
VALID_LICENSES = {"MIT", "Apache-2.0", "GPL-3.0", "BSD-3-Clause", "CC-BY-4.0", "Unlicense"}
MIN_BODY_LENGTH = 50  # characters of real content (after stripping whitespace/comments)


class BodyValidationResult:
    """Result of validating the body/content of a SKILL.md file."""

    def __init__(self, skill_path: Path):
        self.skill_path = skill_path
        self.errors: list[str] = []
        self.warnings: list[str] = []

    @property
    def passed(self) -> bool:
        return len(self.errors) == 0

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)


def parse_frontmatter(content: str) -> tuple[dict[str, Any] | None, str]:
    """Extract YAML frontmatter and return (fm_dict, body_text)."""
    if not content.startswith("---"):
        return None, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, content
    try:
        fm = yaml.safe_load(parts[1])
        return fm if isinstance(fm, dict) else None, parts[2]
    except yaml.YAMLError:
        return None, content


def _extract_headings(body: str) -> list[str]:
    """Return a list of heading text (without # prefixes) from markdown body."""
    headings: list[str] = []
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            # Strip leading # and whitespace
            heading = re.sub(r"^#+\s*", "", stripped).strip()
            if heading:
                headings.append(heading)
    return headings


def _strip_comments_and_whitespace(body: str) -> str:
    """Remove HTML comments and collapse whitespace for length check."""
    no_comments = re.sub(r"<!--.*?-->", "", body, flags=re.DOTALL)
    return no_comments.strip()


def validate_content_body(skill_path: Path) -> BodyValidationResult:
    """Validate the content body of a SKILL.md file.

    Checks:
    - Frontmatter exists and contains required fields
    - Body has minimum content length
    - Body contains required sections (headings)
    - Body contains recommended sections (warning if missing)
    - Frontmatter license is valid
    - No duplicate headings
    - Body is not just placeholder text
    """
    result = BodyValidationResult(skill_path)
    skill_md = skill_path / "SKILL.md"

    if not skill_md.exists():
        result.error("SKILL.md not found")
        return result

    try:
        content = skill_md.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        result.error("SKILL.md is not valid UTF-8")
        return result

    frontmatter, body = parse_frontmatter(content)

    # --- Frontmatter checks ---
    if frontmatter is None:
        result.error("SKILL.md has no valid YAML frontmatter")
        return result

    # License validation
    license_val = frontmatter.get("license", "")
    if license_val and license_val not in VALID_LICENSES:
        result.warn(
            f"License '{license_val}' is not a common open-source license. "
            f"Common choices: {', '.join(sorted(VALID_LICENSES))}"
        )

    # --- Body checks ---
    clean_body = _strip_comments_and_whitespace(body)

    if len(clean_body) < MIN_BODY_LENGTH:
        result.error(
            f"Body content is too short ({len(clean_body)} chars, minimum {MIN_BODY_LENGTH}). "
            "Add meaningful instructions to your skill."
        )

    # Check for placeholder-only content
    placeholder_patterns = [
        r"^#+\s*\w+\s*\n\s*<!--.*?-->",
        r"^\s*<!--.*?-->\s*$",
    ]
    body_no_placeholders = re.sub(r"<!--.*?-->", "", body, flags=re.DOTALL).strip()
    if len(body_no_placeholders) < 20:
        result.error("Body appears to be only placeholder comments with no real content")

    # Extract headings and check sections
    headings = _extract_headings(body)
    heading_set_lower = {h.lower() for h in headings}

    for section in REQUIRED_SECTIONS:
        if section not in heading_set_lower:
            result.error(f"Missing required section: '{_section_display(section)}'")

    for section in RECOMMENDED_SECTIONS:
        if section not in heading_set_lower:
            result.warn(f"Missing recommended section: '{_section_display(section)}'")

    # Check for duplicate headings
    seen_headings: dict[str, int] = {}
    for h in headings:
        key = h.lower()
        seen_headings[key] = seen_headings.get(key, 0) + 1
    for h, count in seen_headings.items():
        if count > 1:
            result.warn(f"Duplicate heading: '{h}' (appears {count} times)")

    return result
