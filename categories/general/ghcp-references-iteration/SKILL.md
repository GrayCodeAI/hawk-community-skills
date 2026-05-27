---
name: ghcp-references-iteration
description: 'Skill: ghcp-references-iteration'
license: MIT
tags:
- general
---

## Strategy: `adversarial` — challenge the previous run's conclusions

Re-investigate what the previous run dismissed, demoted, or marked SATISFIED. This strategy assumes the previous run made Type II errors (missed real bugs by being too conservative) and systematically challenges those decisions.

**Why this strategy exists:** In benchmarking, the triage step reliably demotes legitimate findings by demanding excessive evidence, marking ambiguous cases as "design choice," or accepting code-review SATISFIED verdicts without deep verification. The adversarial strategy specifically targets these failure modes.

1. **Load previous decisions.** Read these files from the previous run (use divide-and-conquer — section headers first, then targeted deep reads):
   - `quality/EXPLORATION_MERGED.md` — specifically the `## Demoted Candidates` section (this is your primary input — it contains structured re-promotion criteria for each dismissed finding)
   - `quality/BUGS.md` — what was confirmed (to avoid re-finding the same bugs)
   - `quality/spec_audits/*triage*` — what was dismissed or demoted during triage, and why
   - `quality/code_reviews/*.md` — Pass 2 SATISFIED/VIOLATED verdicts
   - `quality/EXPLORATION.md` — just the `## Candidate Bugs for Phase 2` section to see which candidates didn't become confirmed bugs
   - Write a summary to `quality/ITERATION_PLAN.md` listing: (a) demoted candidates from the manifest with their re-promotion criteria, (b) additional dismissed triage findings not yet in the manifest, (c) candidates that weren't promoted, (d) requirements marked SATISFIED that had thin evidence

2. **Re-investigate dismissed findings with a lower evidentiary bar.** The adversarial strategy uses a deliberately lower evidentiary standard than earlier strategies. The baseline and gap strategies rightly demand strong evidence to avoid false positives during initial discovery. But by the adversarial iteration, remaining undiscovered bugs are precisely the ones that conservative triage keeps rejecting — they look ambiguous, they could be "design choices," they lack dramatic runtime failures. For these findings:
   - A code-path trace showing observable semantic drift (output differs from what spec or contract requires) is sufficient to confirm — you do not need a runtime crash or dramatic failure
   - "Permissive behavior" is not automatically a design choice — check whether the spec, docs, or API contract defines the expected behavior. If the code deviates from a documented contract, it's a bug regardless of whether the deviation is "permissive"
   - If the Demoted Candidates Manifest includes re-promotion criteria, attempt to satisfy those criteria specifically. Each criterion was written to be actionable — follow it
   - Read the specific code location cited in the finding
   - Trace the code path independently — do not rely on the previous run's analysis
   - Make an explicit CONFIRMED/FALSE-POSITIVE determination with fresh evidence
   - Update the Demoted Candidates Manifest: change status to RE-PROMOTED or FALSE POSITIVE with the iteration attribution

3. **Challenge SATISFIED verdicts.** For each requirement the code review marked SATISFIED with thin evidence (single-line citation, no code-path trace, or grouped with 3+ other requirements under one citation):
   - Re-verify the requirement by reading the cited code and tracing the behavior
   - Check whether the requirement is actually satisfied or whether the review took a shallow pass

4. **Explore adjacent code.** For each re-confirmed or newly confirmed finding, explore the surrounding code for related bugs — bugs cluster. If a function has one bug, its callers and siblings likely have related issues.

5. Write all findings to `quality/EXPLORATION_ITER{N}.md`. Each finding must include: the original source (triage dismissal, candidate demotion, or SATISFIED challenge), the fresh evidence, and the new determination.
