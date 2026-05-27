---
name: ghcp-quality-playbook-skill
description: Run a complete quality engineering audit on any codebase. Derives behavioral
  requirements from the code, generates spec-traced functional tests, runs a three-pass
  code review with regression tests,...
license: Complete terms in LICENSE.txt
tags:
- general
metadata: None
version: 1.5.6
author: Andrew Stellman
github: https://github.com/andrewstellman/quality-playbook
---

## Reference Files

Read these as you work through each phase:

| File | When to Read | Contains |
|------|-------------|----------|
| `references/exploration_patterns.md` | Phase 1 (explore) | Pattern applicability matrix, deep-dive templates, domain-knowledge questions |
| `references/defensive_patterns.md` | Step 5 (finding skeletons) | Grep patterns, how to convert findings to scenarios |
| `references/schema_mapping.md` | Step 5b (schema types) | Field mapping format, mutation validity rules |
| `references/requirements_pipeline.md` | Phase 2 (requirements) | Five-phase pipeline, versioning protocol, carry-forward rules |
| `references/constitution.md` | File 1 (QUALITY.md) | Full template with section-by-section guidance |
| `references/functional_tests.md` | File 2 (functional tests) | Test structure, anti-patterns, cross-variant strategy |
| `references/review_protocols.md` | Files 3–4 (code review, integration) | Templates for both protocols, patch validation, skip guards |
| `references/spec_audit.md` | File 5 (Council of Three) | Full audit protocol, triage process, fix execution |
| `references/iteration.md` | Iterations (after Phase 6) | Four iteration strategies: gap, unfiltered, parity, adversarial |
| `references/verification.md` | Phase 6 (verify) | Complete self-check checklist (45 benchmarks) including structured output, patch gate, skip guard validation, pre-flight discovery, version stamps, bug writeups, enumeration completeness, triage executable evidence, code-extracted enumeration lists, mechanical verification artifacts, source-inspection test execution, contradiction gate, seed check execution, convergence tracking, sidecar JSON schema validation, script-verified closure gate, canonical use case identifiers, and writeup inline fix diffs |
