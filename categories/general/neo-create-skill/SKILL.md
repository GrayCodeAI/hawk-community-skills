---
name: neo-create-skill
description: Guide for creating effective skills. This command should be used when
  users want to create a new skill (or update an existing skill) that extends Claude's
  capabilities with specialized knowledge, w...
license: MIT
tags:
- general
---

# Skill Name

## Critical Guidlines
[Core principle in 1-2 sentences. Each start wit "You MUST ..."]

## How to Use
[Think in steps, use problem decomposition, etc.]

## Guide
[Procedures, patterns]

## Examples
[Examples of how to use the skill, include agent input and output]

## Troubleshooting
[Common mistakes and how to avoid them]

## Resources
[Scripts, references, assets]
```

3. Add resource subdirectories only if needed:
   - `scripts/` — reusable executable code
   - `references/` — documentation loaded on demand
   - `assets/` — files used in output (templates, images)

### Step 4: Edit the Skill

When editing the (newly-generated or existing) skill, remember that the skill is being created for another instance of Claude to use. Focus on including information that would be beneficial and non-obvious to Claude. Consider what procedural knowledge, domain-specific details, or reusable assets would help another Claude instance execute these tasks more effectively.

#### Start with Reusable Skill Contents

To begin implementation, start with the reusable resources identified above: `scripts/`, `references/`, and `assets/` files. Note that this step may require user input. For example, when implementing a `brand-guidelines` skill, the user may need to provide brand assets or templates to store in `assets/`, or documentation to store in `references/`.

Remove any resource subdirectories not needed for the skill. Most skills need only SKILL.md.

#### Update SKILL.md

**Writing Style:** Write the entire skill using **imperative/infinitive form** (verb-first instructions), not second person. Use objective, instructional language (e.g., "To accomplish X, do Y" rather than "You should do X" or "If you need to do X"). This maintains consistency and clarity for AI consumption.

To complete SKILL.md, answer the following questions:

1. What is the purpose of the skill, in a few sentences?
2. When should the skill be used?
3. In practice, how should Claude use the skill? All reusable skill contents developed above should be referenced so that Claude knows how to use them.

### Step 5: Validating the Skill

Before deploying, verify the skill meets requirements:

1. **Frontmatter** — YAML contains only `name` and `description` (max 1024 chars total)
2. **Name** — uses only letters, numbers, and hyphens
3. **Description** — starts with "Use when...", written in third person, includes specific triggers
4. **Structure** — `SKILL.md` exists at `skills/<skill-name>/SKILL.md`
5. **Resources** — any referenced scripts, references, or assets exist at their declared paths

### Step 6: Iterate

After testing the skill, users may request improvements. Often this happens right after using the skill, with fresh context of how the skill performed.

**Iteration workflow:**

1. Use the skill on real tasks
2. Notice struggles or inefficiencies
3. Identify how SKILL.md or bundled resources should be updated
4. Implement changes and test again
