#!/usr/bin/env python3
"""Shared skill-directory discovery for all tools/scripts.

Every script that walks categories/ for skill directories should use
iter_skills() instead of re-implementing the sorted category/skill walk, so
the discovery rule (what counts as a "skill directory") lives in one place.
"""

from collections.abc import Iterator
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CATEGORIES_DIR = REPO_ROOT / "categories"


def iter_skills(categories_dir: Path = CATEGORIES_DIR) -> Iterator[Path]:
    """Yield every skill directory under categories_dir, in sorted order.

    A skill directory is a directory under a category directory that
    contains a SKILL.md file.
    """
    if not categories_dir.exists():
        return
    for category_dir in sorted(categories_dir.iterdir()):
        if not category_dir.is_dir():
            continue
        for skill_dir in sorted(category_dir.iterdir()):
            if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
                yield skill_dir
