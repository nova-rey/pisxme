# Phase 24 duplicate hierarchy-label probe receipt — 2026-09-12

## Removal strategy — rejected

The first balanced disposable probe removed only the early boundary label/wire
expressions for `BRIDGE_3V3` and `BRIDGE_1V1` in `REGULATORS` and `STORAGE`.
Native ERC produced four errors (`pin_not_connected` on the retained contract
symbols), and the netlist lost 168 nets/nodes. These records cannot be deleted
without reconnecting the contract model.

## Local-label strategy — not promoted

A second disposable probe converted only those early boundary labels to local
labels, retained their wires and contract symbols, and left the later
circuit-facing hierarchical labels unchanged. Fresh KiCad Light reported zero
severity-error findings and exact XML netlist parity: 361 nets, zero missing or
extra names, zero changed node sets. However, the warning census remained
unchanged (132 off-grid, 126 isolated-label, 30 local/global, 23 multiple-name
findings, plus KiCad 10.0.6 library-configuration warnings). It therefore does
not close the warning cluster and is not promoted.

Raw reports and netlists are retained as immutable evidence:

- `PHASE24_DUPLICATE_LABEL_REMOVE_PROBE_ERC_20260912.rpt`
- `PHASE24_DUPLICATE_LABEL_REMOVE_PROBE_ERRORS_20260912.rpt`
- `PHASE24_DUPLICATE_LABEL_LOCALIZE_PROBE_ERC_20260912.rpt`
- `PHASE24_DUPLICATE_LABEL_LOCALIZE_PROBE_ERRORS_20260912.rpt`
- `PHASE24_DUPLICATE_LABEL_BASE_NETLIST_20260912.xml`
- `PHASE24_DUPLICATE_LABEL_LOCALIZE_NETLIST_20260912.xml`

Canonical schematic and PCB were not modified by either probe.
