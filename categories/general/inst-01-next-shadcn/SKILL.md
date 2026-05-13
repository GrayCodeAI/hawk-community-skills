---
description: Guidelines for installing and configuring ShadCN UI
globs: **/*.ts, **/*.tsx, **/*.js, **/*.jsx
---

# Install & Configure ShadCN UI for Next.js 15 & React 19

## Overview

1. Add ShadCN UI to your Next.js 15 project.
2. Set up Tailwind CSS (v4 or latest).
3. Generate the ShadCN components (e.g., Sidebar, Button) you need.

## CRITICAL INSTRUCTIONS
- Use the latest ShadCN CLI.
- Avoid any deprecated or unverified ShadCN code.
- Ensure Tailwind is properly configured (tailwind.config.js, postcss.config.js) for your app folder.

## Key Steps

1. Install ShadCN CLI:
   ```bash
   npx shadcn@latest init
   ```
2. Tailwind Configuration:
   - Confirm your tailwind.config.js includes paths to app/**/*.{js,ts,jsx,tsx} and components/**/*.{js,ts,jsx,tsx}.
   - Make sure globals.css (or a similar file) imports Tailwind base, components, and utilities.
3. Add Components:
   ```bash
   npx shadcn add sidebar button
   ```
   This copies the sidebar, button, and other required files into your project's components folder.

## Verification Checklist
- Did you confirm your tailwind.config.js references the correct directories?
- Are you using the ShadCN CLI commands exactly as shown?
- No deprecated or custom-coded patterns outside the official ShadCN approach?

## AI MODEL RESPONSE TEMPLATE
When asked about ShadCN installation or setup:
1. Provide the npx shadcn@latest init command.
2. Show how to configure Tailwind for Next.js 15.
3. Emphasize using npx shadcn add for new components.