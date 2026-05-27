---
name: ag-manage-skills
description: Discover, list, create, edit, toggle, copy, move, and delete AI agent
  skills across 11 tools (Cursor, Claude, Agents, Windsurf, Copilot, Codex, Cline,
  Aider, Continue, Roo Code, Augment)
license: MIT
tags:
- general
risk: critical
source: community
source_repo: umutbozdag/agent-skills-manager
source_type: community
---

# My New Skill

Instructions for the agent go here.
EOF

# For Windsurf/Cline/Continue/Roo (plain .md format)
mkdir -p ~/.windsurf/rules/my-new-rule
cat > ~/.windsurf/rules/my-new-rule/my-new-rule.md << 'EOF'
# My New Rule

Instructions go here.
EOF

# For single-file tools
cat > .github/copilot-instructions.md << 'EOF'
Instructions for Copilot go here.
EOF
```

### Enable / Disable a skill

Disabling renames the file to `.disabled` so the tool ignores it but the content is preserved:

```bash
# Disable
mv ~/.cursor/skills/my-skill/SKILL.md ~/.cursor/skills/my-skill/SKILL.md.disabled

# Enable
mv ~/.cursor/skills/my-skill/SKILL.md.disabled ~/.cursor/skills/my-skill/SKILL.md
```

### Copy a skill between tools

```bash
# Copy from Cursor to Claude
cp -r ~/.cursor/skills/my-skill ~/.claude/skills/my-skill

# Copy from Agents to Windsurf (adapt format)
mkdir -p ~/.windsurf/rules/my-skill
cp ~/.agents/skills/my-skill/SKILL.md ~/.windsurf/rules/my-skill/my-skill.md
```

### Move a skill

```bash
mv ~/.cursor/skills/my-skill ~/.agents/skills/my-skill
```

### Delete a skill

```bash
rm -rf ~/.cursor/skills/my-skill
```

### Copy a skill from global to project scope

```bash
cp -r ~/.cursor/skills/my-skill .cursor/skills/my-skill
```

### Search across all skills

```bash
# Search by name
find ~/.agents/skills ~/.cursor/skills ~/.claude/skills ~/.windsurf/rules ~/.cline/rules ~/.continue/rules ~/.roo/rules -maxdepth 1 -type d 2>/dev/null | sort

# Search by content
grep -rl "search term" ~/.agents/skills/ ~/.cursor/skills/ ~/.claude/skills/ 2>/dev/null
```

### Find disabled skills

```bash
find ~/.agents/skills ~/.cursor/skills ~/.claude/skills -name "*.disabled" 2>/dev/null
```

## Guidelines

- When the user asks to "manage skills", "list my skills", "create a skill", "copy a skill to X", or similar, use the paths and formats above.
- Always confirm before deleting skills.
- When copying between tools with different formats (e.g., Cursor SKILL.md to Windsurf plain .md), adapt the file naming accordingly.
- Project-scoped skills override global skills of the same name.
- For single-file tools (Copilot, Codex, Aider, Augment), editing means replacing the entire file content.
- When creating skills, use kebab-case for directory names (e.g., `my-new-skill`).

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
