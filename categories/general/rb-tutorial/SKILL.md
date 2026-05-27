---
name: rb-tutorial
description: 'Skill: rb-tutorial'
license: MIT
tags:
- general
---

## Chapter 5: Managing Your Workspace

Here are a few essential commands for managing your `rulebook-ai` project.

*   **Check the current sync state:** See which profile or packs were last applied.
    ```bash
    rulebook-ai project status
    ```

*   **Remove a pack from your library:**
    ```bash
    rulebook-ai packs remove community-react-pack
    ```

*   **Clean generated rules:** If you want to reset the generated rules without touching your valuable `memory/` and `tools/` files:
    ```bash
    rulebook-ai project clean-rules
    ```

*   **Completely uninstall from a project:** This is a destructive action that removes all `rulebook-ai` related files and directories (`.rulebook-ai`, `memory`, `tools`, etc.). Use with care!
    ```bash
    rulebook-ai project clean
    ```

## Chapter 6: Becoming a Contributor

You now know how to use `rulebook-ai`! The next step is to contribute back to the community by creating your own pack.

`rulebook-ai` makes this easy by providing a pack that turns your AI into an expert on pack authoring.

**1. Add the Authoring Guide Pack**

```bash
uvx rulebook-ai packs add pack-authoring-guide
```

**2. Sync the Guide**

```bash
uvx rulebook-ai project sync --pack pack-authoring-guide
```

**3. Start Creating!**

Your AI now has all the specifications, guides, and validation tools in its context. You can now ask it to help you build a new pack. For example:

> *"Hey AI, using the rules from the `pack-authoring-guide`, help me create a new pack for Python development. Let's start with the `manifest.yaml` file."*

This workflow is the heart of `rulebook-ai`: using the tool to enhance the AI's capabilities to help you use the tool itself.
