# Phase 24 U5 native connectivity revalidation — V1559

Board audited: `PHASE24_PGND_CLUSTER_CURRENT.kicad_pcb`.

The audit `phase24_u5_layer_connectivity_audit.py` derives connectivity from
KiCad's saved pads, tracks, vias, and filled zones. Expected pad membership
is assertion-only; no synthetic graph edges are added.

Result: **PASS**.

- `/REGULATORS/BRIDGE_1V1`: U5.9 connected to C44.1, C45.1, C46.1, C47.1.
- `POWER_GND`: R20.2 and C44.2/C45.2/C46.2/C47.2 connected.
- Negative control: removing a necessary U5.9 trace caused the audit to fail
  as required (`trace_removal_fails: True`).
- The audit was corrected to exclude via objects from track signatures and to
  use safe native type/geometry discrimination. The rerun completes without
  the former `PCB_VIA::GetWidth` assertion warnings.
