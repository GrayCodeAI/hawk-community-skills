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
