---
name: tl-coupling-analysis
description: Analyzes coupling between modules using the three-dimensional model (strength,
  distance, volatility) from "Balancing Coupling in Software Design". Use when asking
  "are these modules too coupled?", ...
license: MIT
tags:
- general
---

## Quick Reference: Pattern → Integration Strength

| Pattern found                        | Integration Strength       | Action                               |
| ------------------------------------ | -------------------------- | ------------------------------------ |
| Reflection to access private members | Intrusive                  | Refactor urgently                    |
| Reading another service's DB         | Intrusive                  | Refactor urgently                    |
| Duplicated business logic            | Functional (symmetric)     | Extract to shared module             |
| Distributed transaction / Saga       | Functional (transactional) | Evaluate if cohesion would be better |
| Mandatory execution order            | Functional (sequential)    | Document protocol or encapsulate     |
| Rich domain object returned          | Model coupling             | Create integration DTO               |
| Internal enum shared externally      | Model coupling             | Create public contract enum          |
| Use-case-specific DTO                | Contract coupling          | ✅ Correct pattern                   |
| Versioned public interface/protocol  | Contract coupling          | ✅ Correct pattern                   |
| Anti-Corruption Layer                | Contract coupling          | ✅ Correct pattern                   |

## Quick Heuristics

**For Integration Strength**:

- "If I change an internal detail of module X, how many other modules need to change?"
- "Was the integration contract designed to be public, or is it accidental?"
- "Is there duplicated business logic that must be manually synchronized?"

**For Distance**:

- "What's the cost of making a change that affects both modules?"
- "Do teams maintaining these modules need to coordinate deployments?"
- "If one module fails, does the other stop working?"

**For Volatility**:

- "Does this module encapsulate competitive business advantage?"
- "Does the business team frequently request changes in this area?"
- "Is there a history of many refactors in this area?"

**For Balance**:

- "Do components that need to change together live together in the code?"
- "Are independent components well separated?"
- "Where is there strong coupling with volatile and distant components?" (→ this is the main problem)

## Known Limitations

- **Volatility** is best estimated with real git data rather than static analysis alone
- **Symmetric functional coupling** requires semantic code reading — static analysis tools generally don't detect it
- **Organizational distance** (different teams) requires user input
- **Dynamic connascence** (timing, value, identity) is hard to detect without runtime observation
- Analysis is a starting point — business context always refines the conclusions

## Book References

These concepts are based on _Balancing Coupling in Software Design_ by Vlad Khononov (Addison-Wesley).
