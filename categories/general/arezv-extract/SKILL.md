---
name: arezv-extract
description: Turn a proven pattern or debugging solution into a standalone reusable
  skill with SKILL.md, reference docs, and examples.
license: MIT
tags:
- general
---

# <Skill Title>

> One-line summary of what this skill solves.

## Quick Reference

| Problem | Solution |
|---------|----------|
| {{problem 1}} | {{solution 1}} |
| {{problem 2}} | {{solution 2}} |

## The Problem

{{2-3 sentences explaining what goes wrong and why it's non-obvious.}}

## Solutions

### Option 1: {{Name}} (Recommended)

{{Step-by-step with code examples.}}

### Option 2: {{Alternative}}

{{For when Option 1 doesn't apply.}}

## Trade-offs

| Approach | Pros | Cons |
|----------|------|------|
| Option 1 | {{pros}} | {{cons}} |
| Option 2 | {{pros}} | {{cons}} |

## Edge Cases

- {{edge case 1 and how to handle it}}
- {{edge case 2 and how to handle it}}
```

### Step 6: Quality gates

Before finalizing, verify:

- [ ] SKILL.md has valid YAML frontmatter with `name` and `description`
- [ ] `name` matches the folder name (lowercase, hyphens)
- [ ] `name` does NOT contain reserved fragments `claude` or `anthropic` (use `cc-` prefix for Claude Code skills)
- [ ] Description includes "Use when:" trigger conditions
- [ ] Solutions are self-contained (no external context needed)
- [ ] Code examples are complete and copy-pasteable
- [ ] No project-specific hardcoded values (paths, URLs, credentials)
- [ ] No unnecessary dependencies

### Step 7: Report

```
✅ Skill extracted: {{skill-name}}

Files created:
  {{path}}/SKILL.md          ({{lines}} lines)
  {{path}}/README.md         ({{lines}} lines)
  {{path}}/reference/examples.md  ({{lines}} lines)

Install: /plugin install (copy to your skills directory)
Publish: clawhub publish {{path}}

Source: MEMORY.md entries at lines {{n, m, ...}} (retained — the skill is portable, the memory is project-specific)
```

## Examples

### Extracting a debugging pattern

```
/si:extract "Fix for Docker builds failing on Apple Silicon with platform mismatch"
```

Creates `docker-m1-fixes/SKILL.md` with:
- The platform mismatch error message
- Three solutions (build flag, Dockerfile, docker-compose)
- Trade-offs table
- Performance note about Rosetta 2 emulation

### Extracting a workflow pattern

```
/si:extract "Always regenerate TypeScript API client after modifying OpenAPI spec"
```

Creates `api-client-regen/SKILL.md` with:
- Why manual regen is needed
- The exact command sequence
- CI integration snippet
- Common failure modes

## Tips

- Extract patterns that would save time in a *different* project
- Keep skills focused — one problem per skill
- Include the error messages people would search for
- Test the skill by reading it without the original context — does it make sense?
