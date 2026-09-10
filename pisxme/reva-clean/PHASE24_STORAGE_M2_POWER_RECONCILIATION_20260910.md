# Phase 24 M.2 power-source reconciliation — 2026-09-10

## Live finding

The preferred Path-A V75 PCB has J3 power contacts on `M2_3V3`, but no
source-owned pad, track, or zone on that net. `STORAGE_3V3` is the existing
regulator-owned rail used by the storage bridge/selectors. This is a genuine
source-authority gap; no PCB-only copper was promoted.

## Disposable source-level proof

`phase24_reconcile_m2_power_source.py` produced
`phase24_m2_power_reconcile_fixture/` by changing only the nine saved J3
instance labels from `M2_3V3` to `STORAGE_3V3`, and by changing the storage
hierarchy port and root sheet boundary from `M2_3V3` to `STORAGE_3V3`. The
embedded connector pin names remain the reviewed M.2 semantic names.

Results:

- dual-mode schematic audit: PASS;
- mode-contract audit: PASS;
- native root ERC: 501 violations, with no `M2_3V3` hierarchy finding; the
  fixture still inherits the project's broader hierarchy/label findings;
- no production schematic or PCB was changed by this experiment.

## Disposition

The reconciliation is technically plausible but not promoted in this
checkpoint because the project-wide source regeneration path and power-budget
review must consume the renamed rail together. V75 remains the preferred
disposable routing parent. The current open gate is a source-level storage
power-owner correction followed by regenerated PCB connectivity, not another
PCB-only trace probe.
