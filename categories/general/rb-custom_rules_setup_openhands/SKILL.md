---
name: rb-custom_rules_setup_openhands
description: 'Skill: rb-custom_rules_setup_openhands'
license: MIT
tags:
- general
---

### Usage Summary

- Create a `.openhands/microagents/` directory in the root of your repository and add `.md` files containing guidelines or specialized knowledge.
- Use general microagents for always-loaded repository context and keyword-triggered microagents for instructions that activate on specific keywords.
- Place microagent files in a `.openhands` repository (or `openhands-config` on GitLab) to apply them across an organization, or in `~/.openhands/microagents` for user-level customizations.
- Use repository scripts (`setup.sh` and `pre-commit.sh`) to customize runtime behaviour and enforce standards.
