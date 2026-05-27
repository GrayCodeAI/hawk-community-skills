---
name: ghcp-references-language-reference
description: 'Skill: ghcp-references-language-reference'
license: MIT
tags:
- general
---

## slangc Command Line

```bash
# Basic
slangc shader.slang -target spirv -o shader.spv
slangc shader.slang -target dxil  -o shader.dxil
slangc shader.slang -target glsl  -o shader.glsl
slangc shader.slang -target cuda  -o shader.cu
slangc shader.slang -target metal -o shader.metal
slangc shader.slang -target cpp   -o shader.cpp

# Multi-target
slangc shader.slang -target spirv -o shader.spv -target dxil -o shader.dxil

# Entry point and stage
slangc shader.slang -target spirv -entry mainCS -stage compute -o out.spv

# Profile
slangc shader.slang -target glsl  -profile glsl_460 -o out.glsl
slangc shader.slang -target dxil  -profile sm_6_7   -o out.dxil

# Matrix layout (important for row-major engines like xMath)
slangc shader.slang -target spirv -matrix-layout-row-major -o out.spv

# Optimization
slangc shader.slang -O0   # no optimization
slangc shader.slang -O2   # standard
slangc shader.slang -O3   # aggressive

# Debug info
slangc shader.slang -g -o out.spv

# Include paths and macros
slangc shader.slang -I./include -DENABLE_SHADOWS=1 -o out.spv

# Capabilities
slangc shader.slang -capability spvShaderClockKHR -target spirv -o out.spv

# Vulkan-specific
slangc shader.slang -target spirv -fvk-use-entrypoint-name -o out.spv
slangc shader.slang -target spirv -fvk-use-gl-layout       -o out.spv

# Precompiled modules
slangc shader.slang -r prebuilt.slang-module -target spirv -o out.spv

# Emit IR
slangc shader.slang -emit-ir -o shader.slang-module
```

### Optimization Levels
| Flag | Effect                              |
|------|-------------------------------------|
| `-O0`| No optimization (debugging)         |
| `-O1`| Basic optimization                  |
| `-O2`| Standard optimization (default)     |
| `-O3`| Aggressive (may increase compile time)|

### Stage Names for `-stage`
`vertex` · `fragment` · `compute` · `hull` · `domain` · `geometry`
`raygeneration` · `closesthit` · `miss` · `anyhit` · `intersection` · `callable`
