---
name: ghcp-slang-shader-engineer-skill
description: Use when working with Slang shaders, shader modules, HLSL-compatible
  GPU code, graphics pipelines, compute shaders, tessellation, ray tracing, parameter
  blocks, generics, interfaces, capabilities, ...
license: MIT
tags:
- general
---

## When to Load Reference Files

**Load `references/language-reference.md` when:**

- Writing or reviewing type declarations, generics, interfaces, capabilities
- Answering questions about autodiff, modules, access control, or compilation targets
- Cross-compilation to a specific target (SPIR-V, GLSL, Metal, CUDA, CPU)
- Checking command-line options or CMake setup

**Load `references/rules-and-patterns.md` when:**

- Doing a code review or refactor
- Designing a new module or shader system architecture
- Answering "how should I structure this?" questions
- Looking for example prompts and patterns for complex tasks

**Load `references/slang-documentation-full.md` when:**
- The question is about specific syntax, semantics, or examples not covered in the language reference
- The user explicitly asks for official documentation details
- You need to verify a language feature or behavior that isn't clearly covered in the other references
- The user is asking for a comprehensive explanation of Slang features or usage patterns
- The user is asking for examples of Slang code that demonstrate specific features or best practices
