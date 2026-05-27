---
name: ghcp-references-ontology
description: 'Skill: ghcp-references-ontology'
license: MIT
tags:
- general
---

## Ontology Update Protocol

When processing extracted entities/relations from `ingestion.md`:

1. For each entity type:
   - Run through the synonym mapping
   - Call `ontology_store.normalize_type(type_name)` to get the canonical form
   - Call `ontology_store.add_type(canonical_type)` to register it

2. For each relation type:
   - Run through the synonym mapping
   - Call `ontology_store.normalize_relation(relation_name)` to get the canonical form
   - Call `ontology_store.add_relation(canonical_relation)` to register it

3. Use the **canonical** type/relation names when creating nodes and edges in the graph.
