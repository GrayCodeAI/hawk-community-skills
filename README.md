# hawk Community Skills

Community skill packages for [hawk](https://github.com/GrayCodeAI/hawk) — the AI coding agent.

## What are Skills?

Skills are modular instruction packages that teach hawk specialized workflows. Each skill is a markdown file with YAML frontmatter that hawk loads into its system prompt when activated.

## Usage

```bash
# From hawk REPL
/skills search <query>
/skills install <skill-name>
/skills use <skill-name>

# From CLI
hawk skills search api
hawk skills install go-review
hawk skills list
```

## Skill Format

Each skill is a directory containing a `SKILL.md`:

```markdown
---
name: skill-name
description: What this skill does
domain: engineering
tags: [tag1, tag2]
version: "1.0"
author: community
---

# Skill Title

Instructions that hawk follows when this skill is active...
```

## Categories

- **Engineering** — code review, testing, CI/CD, architecture
- **Security** — vulnerability scanning, pentesting, compliance
- **DevOps** — Docker, Kubernetes, cloud infrastructure
- **Data** — analytics, ML pipelines, databases
- **Web** — frontend, accessibility, performance

## Ecosystem Boundaries

- `hawk-community-skills` extends Hawk through public skill and plugin surfaces.
- Do not reference support engine repos such as `eyrie`, `yaad`, `tok`, `trace`, `sight`, or `inspect` as direct dependencies.
- Do not reference `hawk/internal/*` or removed legacy path `hawk/shared/types`.
- Skills should assume Hawk is the product boundary.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

## License

MIT — [GrayCode AI](https://github.com/GrayCodeAI)
