# Phase 24 Path-A SATA QFN escape V4 — 2026-09-06

## Classification

`ROUTE_IMPLEMENTATION_PROGRESS`, not integrated-board closure.

## Topology

The route author now uses native U7 pad coordinates and a coordinated escape
around the actual QFN field:

- TX_N: U7.56, B.Cu, right-side escape, then the C31 corridor.
- TX_P: U7.57, B.Cu, lower/right escape with an outer detour around the
  TX_N corridor, then the C30 corridor.
- RX_N: U7.59, F.Cu, left/down escape, then the C33 corridor.
- RX_P: U7.60, F.Cu, left/down escape, then the C32 corridor.

The layer assignment remains within the approved F.Cu/B.Cu signal policy with
ordinary through vias. No plane-layer signal routing or via-in-pad was added.

## Disposable native fixture evidence

Input: `PHASE24_U7_PROJECT_FOOTPRINT_ROUTE_20260906.kicad_pcb`.

The generated V4 fixture passes the native eight-endpoint SATA audit:

- U7.57 ↔ C30.2; U7.56 ↔ C31.2
- U7.60 ↔ C32.2; U7.59 ↔ C33.2
- C30.1 ↔ J3.49; C31.1 ↔ J3.47
- C32.1 ↔ J3.43; C33.1 ↔ J3.41

Native DRC on the unchanged 0.20 mm project basis reports 10 findings:
six clearance findings, four silkscreen warnings, zero shorts, and zero
track crossings. Applying the explicit disposable 0.15 mm rule basis reduces
this to four silkscreen warnings; the fixture still has 38 intentional
unconnected support pads.

The independent negative control
`phase24_sata_native_connectivity_negative_control_v4.py` removes a real
saved SATA track from the V4 board and confirms that native C30.1 -> J3.49
connectivity then fails. Expected endpoint tuples therefore remain assertions
only; they are not supplying graph edges.

## Integrated-source regeneration

The same author was applied to
`PHASE24_STORAGE_SATA_NET_AUTHORITY_REGEN_20260906.kicad_pcb`. Its eight SATA
endpoint assertions pass, but full-board native DRC remains 1,210 findings /
499 unconnected items. Those are inherited integrated-board debt and prevent
promotion. The generated board is preserved for comparison; no clean-board
authority was replaced.

The route author now rejects stale support-routed ancestors before emitting
copper: a direct run on the older board fails on `C31.1`'s superseded
`/STORAGE/SATA_M2_TX_N` net and explicitly requires
`phase24_regenerate_storage_sata_net_authority.py`. A canonical regenerated
ancestor then routes successfully. This prevents a PCB-only net-ownership
regression from being mistaken for a SATA geometry result.

## Decision

V4 replaces mono2 as the best disposable SATA escape topology. The next
repair is local clearance/rule reconciliation and then support/return
completion on the integrated storage island. Path A remains open; Path B
RTL9210B remains isolated and unchanged.
