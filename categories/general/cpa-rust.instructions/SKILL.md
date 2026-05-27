---
name: cpa-rust.instructions
description: "Skill: cpa-rust.instructions"
license: MIT
tags: [general]
---

# GitHub Copilot Instructions

These instructions define how GitHub Copilot should assist with this project. The goal is to ensure consistent, high-quality code generation aligned with our conventions, stack, and best practices.

## 🧠 Context

- **Project Type**: CLI Tool / Web API / WASM App / Embedded Program
- **Language**: Rust
- **Framework / Libraries**: Tokio / Actix Web / Axum / Serde / SQLx / Clap
- **Architecture**: Modular / Actor-Based / Clean Architecture / Hexagonal

## 🔧 General Guidelines

- Use idiomatic Rust and follow the [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/).
- Prefer `Result` and `Option` over `unwrap()` or panicking.
- Use pattern matching and `?` for concise error handling.
- Favor immutability—use `let` before `let mut`.
- Use `clippy`, `rustfmt`, and `cargo check` regularly.
- Document public functions and modules with `///` doc comments.
- Group related code into crates, modules, and traits.

## 📁 File Structure

Use this structure as a guide when creating or updating files:

```text
src/
  main.rs
  lib.rs
  config/
  handlers/
  models/
  services/
  db/
  utils/
tests/
  unit/
  integration/
migrations/
```

## 🧶 Patterns

### ✅ Patterns to Follow

- Use modules (`mod`) and public interfaces (`pub`) to encapsulate logic.
- Use `serde` for serialization and `thiserror` or `anyhow` for custom errors.
- Implement traits to abstract services or external dependencies.
- Structure async code using `async`/`await` and `tokio` or `async-std`.
- Prefer enums over flags and states.
- Use builders for complex object creation.
- Split binary and library code (`main.rs` vs `lib.rs`) for testability and reuse.

### 🚫 Patterns to Avoid

- Don’t use `unwrap()` or `expect()` unless absolutely necessary.
- Avoid panics in library code—return `Result` instead.
- Don’t rely on global mutable state—use dependency injection or thread-safe containers.
- Avoid deeply nested logic—refactor with functions or combinators.
- Don’t ignore warnings—treat them as errors during CI.
- Avoid `unsafe` unless required and fully documented.

## 🧪 Testing Guidelines

- Use `cargo test` with built-in testing tools.
- Use `#[cfg(test)]` and `#[test]` annotations for unit tests.
- Use test modules alongside the code they test (`mod tests { ... }`).
- Use `mockall`, `fake`, or trait-based mocking for services.
- Write integration tests in `tests/` with descriptive filenames.

## 🧩 Example Prompts

- `Copilot, implement a REST endpoint using Axum that returns a list of books as JSON.`
- `Copilot, write a Rust function that parses a config file using Serde and returns a struct.`
- `Copilot, create a struct for a User with id, name, and optional email, derived with Serde.`
- `Copilot, write unit tests for the calculate_price function with edge cases.`
- `Copilot, implement a CLI app using Clap that takes a --verbose flag and a file argument.`

## 🔁 Iteration & Review

- Always review Copilot output with `clippy` and `rustfmt`.
- Use inline comments to guide Copilot for generating clean and idiomatic code.
- Refactor boilerplate or verbose code into reusable utilities or traits.
- Check all dependencies for security advisories via `cargo audit`.

## 📚 References

- [The Rust Book](https://doc.rust-lang.org/book/)
- [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/)
- [Rust Style Guide](https://github.com/rust-dev-tools/fmt-rfcs)
- [Tokio Documentation](https://docs.rs/tokio/latest/tokio/)
- [Serde (Serialization Framework)](https://serde.rs/)
- [Actix Web Framework](https://actix.rs/)
- [Axum Web Framework](https://docs.rs/axum/latest/axum/)
- [Clap CLI Framework](https://docs.rs/clap/latest/clap/)
- [Rust Error Handling Patterns](https://docs.rs/anyhow/latest/anyhow/)
- [Rust Testing Guide](https://doc.rust-lang.org/book/ch11-00-testing.html)