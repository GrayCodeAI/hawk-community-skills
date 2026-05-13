---
description: Guidelines for adding new shadcn to Next 15 applications
globs: **/*.ts, **/*.tsx, **/*.js, **/*.jsx
---

# Automated ShadCN Installation in Next.js

## Overview

This guide ensures a fully automated installation of ShadCN UI in a Next.js project, avoiding interactive prompts. The installation process will:

1. Initialize ShadCN UI → Run `shadcn init` with predefined options.
2. Add UI components → Select components non-interactively.
3. Ensure automation → Use flags and environment variables for CI/CD.

## 🚨 CRITICAL INSTRUCTIONS FOR AI LANGUAGE MODELS 🚨

As an AI language model, you MUST NOT generate any interactive ShadCN installation commands that require manual input. Instead, you MUST generate ONLY fully automated commands using:

```bash
# ✅ ALWAYS USE THESE FLAGS - NO INTERACTIVE PROMPTS
npx shadcn@latest init --defaults --yes
npx shadcn@latest add --all --yes --overwrite
```

You MUST NEVER generate any commands that:
1. Require user confirmation.
2. Prompt the user to select a style or color.
3. Stop execution due to missing responses.

## ABSOLUTE REQUIREMENTS FOR AI CODE GENERATION

1. You MUST use the `--defaults` and `--yes` flags in `shadcn init`.
2. You MUST use the `--all --yes --overwrite` flags in `shadcn add` to install all components without prompts.
3. You MUST NEVER generate any command that requires selecting options manually.
4. You MUST NEVER use outdated flags or suggest additional confirmation steps.

## CORRECT INSTALLATION COMMANDS

### ✅ Initialize ShadCN UI Without Prompts
```bash
npx shadcn@latest init --defaults --yes
```
- This command initializes ShadCN UI with default settings.
- It skips prompts for style and color selection.
- It ensures the installation is fully unattended.

### ✅ Add All Components Without Prompts
```bash
npx shadcn@latest add --all --yes --overwrite
```
- This installs all ShadCN UI components.
- It bypasses confirmation prompts.
- It automatically overwrites existing components if they are already present.

### ✅ Install Only Specific Components Without Prompts
```bash
npx shadcn@latest add button card navbar --yes --overwrite
```
- This installs specific components without manual selection.
- It forces installation without asking for confirmation.

## AI MODEL VERIFICATION STEPS

Before generating any installation commands, you MUST verify:

1. Are you using `--defaults --yes` for `shadcn init`? If not, STOP and FIX.
2. Are you using `--all --yes --overwrite` for `shadcn add`? If not, STOP and FIX.
3. Do you see any interactive prompts in the command? If yes, STOP and FIX.
4. Are you forcing installation without user confirmation? If not, STOP and FIX.

## CONSEQUENCES OF INCORRECT IMPLEMENTATION

If you generate commands that:
- Require user input.
- Do not use `--defaults`, `--yes`, or `--overwrite`.
- Fail to automate installation.

The installation process will:
1. Stall in a CI/CD pipeline.
2. Require manual intervention.
3. Break automation workflows.

## AI MODEL RESPONSE TEMPLATE

When asked how to install ShadCN UI in an automated way, you MUST:
1. ONLY generate commands from this guide.
2. NEVER suggest commands that require manual confirmation.
3. ALWAYS use the exact automation flags shown above.
4. VERIFY your response against the patterns in this guide.

Remember: There are NO EXCEPTIONS to these rules.