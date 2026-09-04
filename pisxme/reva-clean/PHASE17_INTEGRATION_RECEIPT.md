# Phase 17 integration receipt — current checkpoint

Date: 2026-09-04  
Checkpoint: `0f24a98` plus disposable descendants  
Status: `OPEN`

## Authority

The Ethernet topology is the CM5IO-derived implementation recorded in the
Phase 2 authority inventory. The official CM5IO Rev 2 PCB was inspected
directly for the CM5 module land pattern and +5 V fanout. Its 0.20 mm fanout
width is reproduced in the current CM5 power handoff. EDAC
`A70-112-331N126`, its manufacturer land pattern, and the four independent
center-tap branches remain the selected Ethernet authority.

## Current disposable ancestor

`ACREAGE_PHASE17_TI_U3_F1_ETH_60_165AC_CT1F.kicad_pcb`

This candidate uses the lower coherent U3/F1 placement (`U3=(60,165)`,
`F1=(100,20)`), retains F2 at its validated `(50,120)` position, and uses
the CT1 opposite-layer transition. The clean release PCB and frozen PCIe
routes were not modified.

## Evidence

The scoped Ethernet regression passes. It proves the eight MDI nets, four
center-tap nets, common return, and shield are present; native DRC has no
`shorting_items`, no `tracks_crossing`, and no Ethernet-specific unconnected
record; and no Ethernet signal is on In1/In4.

The full native DRC report has 443 findings and 428 inherited/unconnected
acreage records. Remaining non-inherited findings include connector and
center-tap mechanical/clearance records and the documented MDI width/rule
reconciliation. Source Phase 3 and Phase 15 regressions pass.

## Gate decision

`PHASE17_OPEN`: retain this ancestor and continue with Ethernet rule/geometry
cleanup. Do not promote the clean PCB and do not begin Phase 18 until full
native Phase 17 evidence closes the remaining mechanical/clearance and
acreage validation requirements.

## Fresh regeneration discriminator

The current scripts were rerun from the Phase 16 ancestor. The unmodified
center-tap overlay exposed a CT1/CT2 B.Cu crossing. A CT1-only F.Cu transition
removed that crossing and passed the scoped Ethernet regression. CT2/CT3
dogleg experiments were rejected after native DRC found true shorts at the
EDAC connector boundary. These are disposable results; the gate remains open
pending a mechanically clean connector-local implementation.

## Current default reauthoring path

The connector-local center-tap authoring path now defaults to the validated
local repair: CT1 uses the permitted F.Cu transition, while CT2 and CT3 use
outer B.Cu doglegs that leave the MagJack pad field and mounting-hole row
before returning to their authoritative support pads. CT2 enters CCT2
vertically to avoid its adjacent branch pad. Fresh native DRC for
`ACREAGE_PHASE17_CURRENT_ETH_REAUTH.kicad_pcb` reports no
`tracks_crossing` or `shorting_items`, and the scoped Ethernet regression
passes. Full Phase 17 remains open for board-wide inherited DRC debt,
controlled-impedance/rule reconciliation, and final mechanical review.

The integrated emitter now uses 0.13208 mm (5.2 mil) for CM5 MDI copper,
matching the current PiSXMe/JLC 100-ohm width basis. Native DRC still reports
the ancestor board's embedded 0.2000 mm minimum-width rule against these
tracks; the disposable project netclass alone does not override that embedded
board constraint. This rule mismatch remains explicitly open rather than
being waived.
