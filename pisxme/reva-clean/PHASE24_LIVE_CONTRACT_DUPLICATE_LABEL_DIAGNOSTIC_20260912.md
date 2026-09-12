# Phase 24 live contract duplicate-label diagnostic — 2026-09-12

The current saved child sheets do not satisfy the older exact-set claim in
`PHASE24_LIVE_CONTRACT_MAP_RECEIPT_20260911.md`. Running the fail-closed
`phase24_live_contract_map.py` against the live source stops at
`REGULATORS.kicad_sch` because `BRIDGE_3V3` and `BRIDGE_1V1` each occur twice
as hierarchical labels.

The duplicates are two distinct serialized cohorts:

| child | boundary-style label | later circuit-style label |
|---|---|---|
| REGULATORS | `(5.08,20.32)` / `(5.08,22.86)` | `(5,157)` / `(5,207)` |
| STORAGE | `(5.08,22.86)` / `(5.08,25.4)` | `(5,101.25)` / `(5,103.75)` |

This is a live source-authoring contradiction, not a PCB or electrical-netlist
claim. The older exact-map receipt is retained as historical evidence. No
labels were deleted or renamed by this diagnostic. The next repair must map
these two cohorts by native connectivity and preserve the regulator/storage
net ownership before any promotion.
