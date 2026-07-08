"""Tests for tools/init_skill.py."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))

from init_skill import KEBAB_RE, get_categories, get_existing_skills, validate_name

# ---------------------------------------------------------------------------
# validate_name
# ---------------------------------------------------------------------------


class TestValidateName:
    def test_valid_name(self):
        assert validate_name("my-cool-skill", set()) is None

    def test_single_word(self):
        assert validate_name("python", set()) is None

    def test_with_numbers(self):
        assert validate_name("skill-v2", set()) is None

    def test_already_exists(self):
        existing = {"my-skill", "other-skill"}
        err = validate_name("my-skill", existing)
        assert err is not None
        assert "already exists" in err

    def test_uppercase_rejected(self):
        err = validate_name("MySkill", set())
        assert err is not None
        assert "kebab-case" in err

    def test_underscore_rejected(self):
        err = validate_name("my_skill", set())
        assert err is not None

    def test_starts_with_number(self):
        err = validate_name("1skill", set())
        assert err is not None

    def test_starts_with_hyphen(self):
        err = validate_name("-skill", set())
        assert err is not None

    def test_empty_string(self):
        err = validate_name("", set())
        assert err is not None

    def test_spaces_rejected(self):
        err = validate_name("my skill", set())
        assert err is not None


# ---------------------------------------------------------------------------
# KEBAB_RE
# ---------------------------------------------------------------------------


class TestKebabRe:
    @pytest.mark.parametrize(
        "name",
        ["a", "abc", "my-skill", "skill-v2", "a-b-c-d"],
    )
    def test_valid_kebab(self, name: str):
        assert KEBAB_RE.match(name), f"Expected '{name}' to be valid kebab-case"

    @pytest.mark.parametrize(
        "name",
        ["", "A", "my_skill", "-bad", "bad-", "1bad", "has space", "UPPER"],
    )
    def test_invalid_kebab(self, name: str):
        assert not KEBAB_RE.match(name), f"Expected '{name}' to be invalid kebab-case"


# ---------------------------------------------------------------------------
# get_existing_skills
# ---------------------------------------------------------------------------


class TestGetExistingSkills:
    def test_finds_existing_skills(self, tmp_path: Path):
        import init_skill as mod

        original = mod.CATEGORIES_DIR
        try:
            cats = tmp_path / "categories"
            cats.mkdir()
            (cats / "python" / "flask-skill").mkdir(parents=True)
            (cats / "python" / "django-skill").mkdir(parents=True)
            (cats / "go" / "gin-skill").mkdir(parents=True)
            mod.CATEGORIES_DIR = cats

            result = get_existing_skills()
            assert result == {"flask-skill", "django-skill", "gin-skill"}
        finally:
            mod.CATEGORIES_DIR = original

    def test_empty_categories(self, tmp_path: Path):
        import init_skill as mod

        original = mod.CATEGORIES_DIR
        try:
            cats = tmp_path / "empty"
            cats.mkdir()
            mod.CATEGORIES_DIR = cats
            assert get_existing_skills() == set()
        finally:
            mod.CATEGORIES_DIR = original


# ---------------------------------------------------------------------------
# get_categories
# ---------------------------------------------------------------------------


class TestGetCategories:
    def test_lists_categories(self, tmp_path: Path):
        import init_skill as mod

        original = mod.CATEGORIES_DIR
        try:
            cats = tmp_path / "categories"
            cats.mkdir()
            (cats / "python").mkdir()
            (cats / "go").mkdir()
            (cats / "rust").mkdir()
            mod.CATEGORIES_DIR = cats

            result = get_categories()
            assert result == ["go", "python", "rust"]
        finally:
            mod.CATEGORIES_DIR = original

    def test_ignores_files(self, tmp_path: Path):
        import init_skill as mod

        original = mod.CATEGORIES_DIR
        try:
            cats = tmp_path / "categories"
            cats.mkdir()
            (cats / "python").mkdir()
            (cats / "README.md").write_text("hello")
            mod.CATEGORIES_DIR = cats

            result = get_categories()
            assert result == ["python"]
        finally:
            mod.CATEGORIES_DIR = original

    def test_empty_categories(self, tmp_path: Path):
        import init_skill as mod

        original = mod.CATEGORIES_DIR
        try:
            cats = tmp_path / "empty"
            cats.mkdir()
            mod.CATEGORIES_DIR = cats
            assert get_categories() == []
        finally:
            mod.CATEGORIES_DIR = original
