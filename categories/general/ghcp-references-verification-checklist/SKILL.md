---
name: ghcp-references-verification-checklist
description: 'Skill: ghcp-references-verification-checklist'
license: MIT
tags:
- general
---

## Phase 8 — Comparison HTML Report Structure (comparison outputs only)

These checks validate the HTML comparison report structure.

### 8.1 HTML Comparison Report Structure

- [ ] **Exactly 4 `<h2>` sections** — The HTML must have exactly these `<h2>` headings in order: "Executive Summary", "Threat Tier Distribution", "STRIDE-A Heatmap (with Delta Indicators)", "Comparison Basis — Component Mapping". ❌ Extra sections like "Overall Risk Shift", "Key Delta Metrics", "Metrics Overview", "Findings Diff" as `<h2>` → FAIL (these are either inline elements or removed). ❌ Missing any of the 4 → FAIL.
- [ ] **No Findings Diff section** — The HTML must NOT contain a "Findings Diff" `<h2>` section or any findings diff subsections (Fixed, Removed, Analysis Gaps, New, Changed, Unchanged). If present → FAIL.
- [ ] **No delta metric cards** — The HTML must NOT contain `.risk-delta` cards (Findings Fixed, New Findings, Net Change, Removed, Analysis Gaps, Code-Verified). If present → FAIL.
- [ ] **Risk shift and metrics bar as inline elements** — Risk shift and metrics bar (Components/Threats/Boundaries/Flows/Time) are inline card elements, NOT `<h2>` sections. If they appear as `<h2>` → FAIL.
- [ ] **Metrics bar includes trust boundaries** — The metrics bar MUST show trust boundary counts (e.g., `2 → 2`). If boundaries are missing from the metrics bar → FAIL. Components, Threats, Trust Boundaries, Findings, and Code Changes are the 5 required metric boxes.
- [ ] **Metrics bar 5th box is Code Changes** — The 5th metrics box MUST show commit count and PR count (e.g., `142 commits, 23 PRs`). ❌ "Time Between" → FAIL. The duration/dates are now in the comparison cards (Section 1), not the metrics bar.
- [ ] **Comparison cards structure** — Section 1 MUST contain a `comparison-cards` div with 3 sub-cards: Baseline (hash, date, rating), Target (hash, date, rating), Trend (direction, duration). ❌ Old-style `subtitle` div with `Baseline: SHA → Target: SHA` → FAIL. ❌ Separate `risk-shift` div → FAIL (merged into comparison cards).
- [ ] **No duplicate status indicators** — Status information (Fixed/New/Previously Unidentified counts) MUST appear in ONLY ONE place: the colored status summary cards. They MUST NOT also appear as small inline badges or text in the metrics bar. If the same counts appear in both the metrics bar AND colored cards → FAIL (remove from metrics bar, keep colored cards).
- [ ] **Tier labels match analysis reports** — The Threat Tier Distribution section in the HTML must use EXACTLY these labels: "Tier 1 — Direct Exposure", "Tier 2 — Conditional Risk", "Tier 3 — Defense-in-Depth". ❌ "Probable Exposure", "Theoretical", "High Risk", or any invented variant → FAIL.
- [ ] **Section title is "Comparison Basis" not "Architecture Changes"** — The component mapping section must be titled "Comparison Basis — Component Mapping", NOT "Architecture Changes".
- [ ] **Heatmap has 13 columns** — The STRIDE-A heatmap grid must have: Component | S | T | R | I | D | E | A | Total | divider | T1 | T2 | T3. If T1/T2/T3 columns are missing → FAIL. The heatmap title must include "(with Delta Indicators)".

### 8.2 Heatmap Accuracy (comparison outputs)

- [ ] **Heatmap not all zeros** — Sum all `baseline.Total` and `current.Total` in `stride_heatmap.components`. If either sum is 0 but corresponding inventory has threats → FAIL (heatmap computation bug).
- [ ] **No duplicate renamed component rows** — For every entry in `components_diff.renamed`, verify the heatmap has exactly ONE row for the renamed component (using current name), not TWO rows (one all-zero baseline, one all-zero current).
- [ ] **Heatmap anomaly detection executed** — For every heatmap row with `baseline.Total > 0, current.Total == 0` (disappeared) and every row with `baseline.Total == 0, current.Total > 0` (appeared): verify that fingerprint cross-checking was performed. If a disappeared-appeared pair shares source files, class names, or namespace → it's a missed rename and must be reclassified. The heatmap should NOT have matching all-zero/all-new pairs with shared source files.
- [ ] **Comparison confidence score present** — `diff-result.json` must contain `comparison_confidence` field ("high" or "low"). If more than 3 unresolved heatmap anomalies exist → confidence must be "low" with warning banner in HTML.
- [ ] **Per-component STRIDE arithmetic** — For each heatmap row: `S+T+R+I+D+E+A == Total` AND `T1+T2+T3 == Total` for both baseline and current. Any mismatch → FAIL.
- [ ] **Delta arrows match JSON data** — For each heatmap cell, `delta = current - baseline`. If delta == 0, no arrow. If delta > 0, ▲. If delta < 0, ▼. Spot-check at least 3 components.
- [ ] **Component removal source file verification** — For every component in `components_diff.removed`, verify its `source_files` are genuinely absent from the current commit. If source files still exist → reclassify as renamed or methodology gap.
