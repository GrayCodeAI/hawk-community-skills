---
name: mdc-entity-class-conventions
description: "Sets the standards for entity class design including annotations, ID generation strategies, and relationship configurations for database interaction."
license: MIT
tags: [cursor-rules]
---

- Must annotate entity classes with @Entity.
- Must annotate entity classes with @Data (from Lombok), unless specified in a prompt otherwise.
- Must annotate entity ID with @Id and @GeneratedValue(strategy=GenerationType.IDENTITY).
- Must use FetchType.LAZY for relationships, unless specified in a prompt otherwise.
- Annotate entity properties properly according to best practices, e.g., @Size, @NotEmpty, @Email, etc.