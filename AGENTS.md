# AGENTS.md — hawk Community Skills

Community skill packages for hawk. Modular instruction packages that teach hawk specialized workflows.

## Design Principles

- **Markdown-based** — each skill is a markdown file with YAML frontmatter
- **Zero code** — skills are pure instructions, not executable code
- **Registry** — searchable, installable, version-controlled

## Build & Test

```bash
pytest                           # Run tests
pytest --cov --cov-report=term-missing  # Coverage
ruff check .                     # Lint
ruff format .                    # Format
python scripts/validate_skills.py  # Validate all skills
python scripts/update_registry.py  # Update skill registry
```

## Architecture

- `skills/` — Skill markdown files organized by category
- `registry.json` — Skill registry with metadata
- `scripts/validate_skills.py` — Skill validation (frontmatter, refs)
- `scripts/update_registry.py` — Registry update script
- `tests/` — Test suite for validation and registry tools
- `.cursor-plugin/` — Cursor plugin integration

## Conventions

- Python 3.10+
- `ruff` for linting and formatting
- Conventional Commits: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`
- No `Co-authored-by:` trailers
- Skill frontmatter must include: name, description, version, author
- Path traversal protection enforced in skill loading
- Prompt injection detection in skill content

## Common Pitfalls

- Duplicate registry names cause CI failure
- `@ref()` must reference existing files — orphaned refs fail validation
- Tag validation is strict — use lowercase kebab-case
- Frontmatter consolidation required — no duplicate keys

## Naming Conventions

- **Skill directories**: lowercase kebab-case, must match frontmatter `name` field (`cursor-redis`, `go-review`, `api-testing`)
- **Category directories**: lowercase, under `categories/` (`categories/database/`, `categories/workflows/`)
- **Skill files**: `SKILL.md` is the required entry point; optional files in `templates/`, `examples/`, `scripts/`
- **Tool scripts**: descriptive names in `tools/` (`validate_skill.py`, `update_registry.py`, `frontmatter.py`, `init_skill.py`)
- **Test files**: `test_` prefix matching the tool under test (`test_validate_skill.py`, `test_frontmatter.py`, `test_update_registry.py`)
- **Frontmatter fields**: lowercase snake_case (`name`, `description`, `license`, `tags`)
- **Tags**: lowercase kebab-case, regex `^[a-z][a-z0-9]*(-[a-z0-9]+)*$` (`python`, `ai-ml`, `web3`, `my-cool-tag`)
- **Registry entries**: camelCase for metadata fields (`isFeatured`, `isCurated`, `downloadCount`, `fileCount`, `hasScripts`)
- **Validation result class**: `ValidationResult` with `.errors`, `.warnings`, `.passed` properties

## API Patterns

### Frontmatter Parsing
`tools/frontmatter.py` provides `parse_frontmatter(content)` which returns `(dict | None, str)`. It splits on `---` delimiters, parses YAML with `yaml.safe_load`, and returns the body text. Returns `(None, original_content)` if no valid frontmatter is found. Always use `parse_frontmatter()` from this module — do not reimplement YAML parsing.

### Validation Pipeline
`tools/validate_skill.py` runs these checks in order:
1. `SKILL.md` exists and is valid UTF-8
2. Frontmatter is present and parseable
3. Required fields present: `name`, `description`, `license`
4. Description under 200 chars (warning, not error)
5. Tags: 1-5 items, lowercase kebab-case regex
6. `name` matches directory name
7. Internal markdown links resolve within skill directory (path traversal detection)
8. Scripts have shebang lines and executable bits
9. No non-asset files exceed 100KB

### Registry Generation
`tools/update_registry.py` walks `categories/<category>/<skill>/SKILL.md`, parses frontmatter, and writes `registry.json`. Duplicate names are silently skipped (first occurrence wins). Descriptions are truncated to 200 chars. Empty tags get a default from the category name.

### ValidationResult Pattern
Validation uses a `ValidationResult` object with `.error(msg)` and `.warn(msg)` methods. Errors fail validation; warnings do not. The `.passed` property returns `len(self.errors) == 0`.

## Testing Patterns

### Fixtures
Tests use `tmp_path` (pytest built-in) to create isolated skill directories. The `skill_dir` fixture creates a minimal valid skill:
```python
@pytest.fixture
def skill_dir(tmp_path: Path) -> Path:
    d = tmp_path / "test-skill"
    d.mkdir()
    (d / "SKILL.md").write_text(textwrap.dedent("""\
        ---
        name: test-skill
        description: A test skill
        license: MIT
        tags: [testing, example]
        ---
        # Test Skill
        ...
    """), encoding="utf-8")
    return d
```

### Module Path Setup
Tests add `tools/` to `sys.path` to import tool modules:
```python
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
from validate_skill import validate_skill, ValidationResult
from frontmatter import parse_frontmatter
```

### Monkeypatching Global Paths
`TestFindAllSkills` temporarily replaces `vs.CATEGORIES_DIR` to test against a temp directory, restoring the original in a `finally` block.

### Parametrized Tag Tests
`TestTagPattern` uses `@pytest.mark.parametrize` to test valid and invalid tag patterns:
```python
@pytest.mark.parametrize("tag", ["python", "ai-ml", "web3", "a", "my-cool-tag"])
def test_valid_tags(self, tag: str):
    assert TAG_PATTERN.match(tag)
```

## Key File Locations

| What | Where |
|------|-------|
| Skill directories | `categories/<category>/<skill-name>/SKILL.md` |
| Frontmatter parser | `tools/frontmatter.py` |
| Skill validator | `tools/validate_skill.py` |
| Registry generator | `tools/update_registry.py` |
| Skill initializer | `tools/init_skill.py` |
| Content validation | `tools/content_validation.py` |
| Reference/self-contained checks | `tools/check_references.py`, `tools/check_self_contained.py` |
| Version management | `tools/bump_version.py`, `tools/check_version_sync.py` |
| Marketplace sync | `tools/sync_marketplace.py` |
| Skill registry | `registry.json` |
| All test files | `tests/test_*.py` |
| Contributing guide | `CONTRIBUTING.md` |
| Skill format spec | `SKILL.md` (repo root) |
| Spec template | `plans/SPEC-TEMPLATE.md` |

## Refactoring Guidelines

- **Safe to refactor**: individual tool scripts — they are independent CLI entry points
- **Do not change**: `parse_frontmatter()` return type `(dict | None, str)` — all tools depend on it
- **Do not change**: `ValidationResult` interface (`.errors`, `.warnings`, `.passed`) — tests assert on it
- **Do not change**: `REQUIRED_FIELDS` set or `TAG_PATTERN` regex — they are the quality gate
- **Do not change**: `registry.json` schema — the hawk client parses it
- **Safe to extend**: add new validation checks in `validate_skill()` by appending to the function
- **Safe to extend**: add new tool scripts in `tools/` following the existing pattern (import frontmatter, use `REPO_ROOT`, use `rich` for output)
- **When adding new tools**: add corresponding test file in `tests/`, use `tmp_path` fixtures, import via `sys.path` manipulation
- **When modifying validation**: update both `validate_skill.py` and its test file `tests/test_validate_skill.py`
