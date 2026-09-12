# Phase 24 rolling worker validation — 2026-09-12

## Scope

Fresh disposable KiCad Light workspaces were prepared from committed
`f3d70555` so worker results do not silently include the dirty canonical
checkout. The qualified worker image is KiCad 10.0.6; the local canonical
toolchain is KiCad 10.0.5, so warning-count differences are version-qualified
evidence rather than replacement canonical baselines.

## Results

- Fresh schematic ERC on `PiSXMe_RevA_Clean.kicad_sch`: 368 warnings, 0
  errors. Classes were 132 `endpoint_off_grid`, 126
  `isolated_pin_label`, 30 `same_local_global_label`, 24
  `multiple_net_names`, 53 library-symbol issues, and 3 footprint-link
  issues. Raw report:
  `PHASE24_WORKER_KICAD10_6_ERC_FRESH_20260912.rpt`, SHA-256
  `16f3b9ebf34eaade833f963b15835942afcab7413c8e283af0a7abcb6a6795b9`.
- Fresh DRC on committed `ACREAGE_CANDIDATE.kicad_pcb`: 180 violations and
  468 unconnected items. Raw report:
  `PHASE24_WORKER_KICAD10_6_ACREAGE_DRC_FRESH_20260912.rpt`, SHA-256
  `14d23bd1bb2339fd3e987515dcbe86e1963b32bd21fe7646b3ab227b33008e3c`.
- Fresh U5 audit on `PHASE24_U5_INTEGRATED_LAYERED.kicad_pcb`: PASS from
  native saved pads/tracks/vias/zones, and the actual-trace-removal negative
  control failed as required. KiCad emitted benign enum/via-width assertions
  during the audit; the audit result remained PASS.
- Strict M.2 power-owner audit on committed
  `PHASE24_STORAGE_R81_POWER_V1570.kicad_pcb`: FAIL. U12.20, U12.30,
  U13.5, U13.13, U13.20, U13.30, R81.2, and U14.5 were not natively joined
  to the J3 source graph. This candidate is not a full-board closure
  artifact; no waiver or source change was made.

## Current interpretation

The worker ERC library/link findings are a KiCad 10.0.6 classification
difference from the local 10.0.5 canonical 312/0 census. The 132/126/30/24
classes match and therefore support the current cluster map. The DRC result
is candidate-scoped and remains open. The U5 gate is independently confirmed.
The storage result identifies a stale/disconnected candidate, not permission
to synthesize PCB-only copper or to relax the native connectivity gate.
