---
name: ghcp-instructions-cpp-language-service-tools.ins
description: 'Skill: ghcp-instructions-cpp-language-service-tools.ins'
license: MIT
tags:
- general
---

## Summary

**The golden rule**: When working with C++ code, think "tool first, manual inspection later."

1. **Symbol usages?** → `GetSymbolReferences_CppTools`
2. **Function calls?** → `GetSymbolCallHierarchy_CppTools`
3. **Symbol definition?** → `GetSymbolInfo_CppTools`

These tools are your primary interface to C++ code understanding. Use them liberally and often. They are fast, accurate, and understand C++ semantics that text search cannot capture.

**Your success metric**: Did I use the right C++ tool for every symbol-related task?
