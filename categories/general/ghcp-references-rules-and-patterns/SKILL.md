---
name: ghcp-references-rules-and-patterns
description: 'Skill: ghcp-references-rules-and-patterns'
license: MIT
tags:
- general
---

## C++ and Engine Integration Notes

When the task touches engine or host code:

- Inspect the user's codebase before making assumptions about layout, reflection, resource binding, or runtime dispatch.
- Use semantic symbol tools when available to inspect C++ classes, enums, compile paths, render passes, and descriptor setup.
- Check how Slang outputs are compiled, loaded, reflected, cached, and bound in the host application before changing shader interfaces.
- Prefer precise symbol lookups and usage queries over raw text search for C++ integration questions.
- Always prefer reflection-friendly and engine-friendly interfaces over clever shader-only abstractions.

### Slang CMake integration snippet
```cmake
find_package(slang REQUIRED PATHS ${CMAKE_INSTALL_PREFIX} NO_DEFAULT_PATH)
target_link_libraries(yourLib PUBLIC slang::slang)
```

### Slang compile targets (slangc CLI)
```bash
# SPIR-V for Vulkan
slangc shader.slang -target spirv -o shader.spv

# DXIL for D3D12
slangc shader.slang -target dxil -o shader.dxil

# GLSL
slangc shader.slang -target glsl -o shader.glsl

# CUDA
slangc shader.slang -target cuda -o shader.cu

# Row-major matrices (important for xMath-style engines)
slangc shader.slang -target spirv -matrix-layout-row-major -o shader.spv
```
