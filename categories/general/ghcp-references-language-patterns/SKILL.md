---
name: ghcp-references-language-patterns
description: 'Skill: ghcp-references-language-patterns'
license: MIT
tags:
- general
---

## Rust

```rust
// Unsafe blocks — flag for manual review
unsafe {
    // Reason for unsafety should be documented
}

// Integer overflow (debug builds panic, release silently wraps)
let result = a + b;  // use checked_add/saturating_add for financial math

// Unwrap/expect in production code (panics on None/Err)
let value = option.unwrap();  // prefer ? or match

// Deserializing arbitrary types
serde_json::from_str::<serde_json::Value>(&user_input)  // generally safe
// But: bincode::deserialize from untrusted input — can be exploited
```
