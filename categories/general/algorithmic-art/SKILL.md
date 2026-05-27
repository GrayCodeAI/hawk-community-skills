---
name: algorithmic-art
description: Creating algorithmic art using p5.js with seeded randomness and interactive
  parameter exploration. Use this when users request creating art using code, generative
  art, algorithmic art, flow fields,...
license: Complete terms in LICENSE.txt
tags:
- general
---

## RESOURCES

This skill includes helpful templates and documentation:

- **templates/viewer.html**: REQUIRED STARTING POINT for all HTML artifacts.
  - This is the foundation - contains the exact structure and Anthropic branding
  - **Keep unchanged**: Layout structure, sidebar organization, Anthropic colors/fonts, seed controls, action buttons
  - **Replace**: The p5.js algorithm, parameter definitions, and UI controls in Parameters section
  - The extensive comments in the file mark exactly what to keep vs replace

- **templates/generator_template.js**: Reference for p5.js best practices and code structure principles.
  - Shows how to organize parameters, use seeded randomness, structure classes
  - NOT a pattern menu - use these principles to build unique algorithms
  - Embed algorithms inline in the HTML artifact (don't create separate .js files)

**Critical reminder**:
- The **template is the STARTING POINT**, not inspiration
- The **algorithm is where to create** something unique
- Don't copy the flow field example - build what the philosophy demands
- But DO keep the exact UI structure and Anthropic branding from the template
