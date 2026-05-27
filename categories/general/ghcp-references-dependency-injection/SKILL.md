---
name: ghcp-references-dependency-injection
description: 'Skill: ghcp-references-dependency-injection'
license: MIT
tags:
- general
---

## Common mistakes

1. **Resolving children from inside a ViewModel constructor via `Ioc`.**
   Hides the dependency. Inject the child VM (or a factory) through the
   constructor instead.
2. **Registering everything as singleton.** A "per-document" ViewModel
   registered as singleton becomes shared state across all documents — a
   subtle data-corruption bug. Use `AddTransient` for per-instance VMs.
3. **Building multiple `ServiceProvider` instances.** Each
   `BuildServiceProvider()` is a fresh container — singletons aren't
   shared. Build once at startup, then reuse.
4. **Capturing the `IServiceProvider` itself in long-lived objects.**
   Indicates a service-locator pattern. Inject the specific dependencies
   you need.
5. **Forgetting to wire scope validation in development.** Use
   `Host.CreateDefaultBuilder()` (which sets `ValidateScopes` and
   `ValidateOnBuild` in development) so registration mistakes fail at
   startup, not at first use.
