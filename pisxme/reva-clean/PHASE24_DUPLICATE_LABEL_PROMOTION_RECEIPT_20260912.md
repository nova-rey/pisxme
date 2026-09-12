# Phase 24 duplicate hierarchy-label promotion receipt — 2026-09-12

## Promoted repair

In `REGULATORS.kicad_sch` and `STORAGE.kicad_sch`, only the later
circuit-facing duplicate records for `BRIDGE_3V3` and `BRIDGE_1V1` were
demoted from hierarchical labels to local labels. The original boundary
hierarchical labels, contract symbols, wires, and all circuit geometry remain
unchanged.

This gives each affected child one authoritative hierarchy label while the
local circuit label joins the existing contract net by name.

## Evidence

- Fresh KiCad Light disposable probe: zero severity-error ERC findings.
- Fresh Light probe netlist: 361 nets, zero missing/extra names, zero changed
  node sets against its unmodified baseline.
- Live contract identity map on the probe: PASS for all ten children.
- Native KiCad 10.0.5 on the promoted source: severity-error ERC PASS with
  zero findings; full ERC remains 311 warnings / 0 errors.
- Native structural hierarchy audit: PASS.

The unchanged warning count is expected: the remaining isolated/local-global
families are broader generated-authoring clusters. No warning severity was
changed or waived. Raw rejected alternatives remain in
`PHASE24_DUPLICATE_LABEL_PROBE_RECEIPT_20260912.md`.
