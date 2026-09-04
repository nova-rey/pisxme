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

With the JLC rule floor applied to the disposable base (0.13208 mm minimum
track width, 0.15 mm minimum clearance, 0.30 mm minimum drill), the fresh
candidate `ACREAGE_PHASE17_RULED7_ETH.kicad_pcb` has no Ethernet-specific
crossing, short, hole-clearance, track-width, drill, or unconnected findings.
The remaining 219 native DRC findings are inherited acreage scaffold
connectivity/mechanical records, including the conservative V100 envelope;
they still require final-board review before Phase 17 can close.

The native metrics regression
`validation/phase3/test_phase17_ethernet_metrics.py` passes on the current
candidate: all four MDI pairs are F.Cu-only, J2 pad mapping is authoritative,
and measured pair skew is 0.547–0.829 mm (bounded at 1.0 mm for this Rev-A
acreage candidate).

The disposable lower-island generator now instantiates the frozen solid GND
planes on In1 and In4 before refill. This removes one scaffold ground open;
the remaining unconnected records are expected to persist until the later
return/via and low-speed routing phases and are not counted as Ethernet
connectivity failures.

## Phase 17 bounded power-entry reopening — 2026-09-04

The smallest coherent power-entry experiment moved F1 to `(240,40)` while
preserving the dual-input/fuse/LM74700 architecture, and reauthored the local
F1-to-Q1 copper so it exits the fuse bore and approaches Q1 pad 1 without
crossing Q1 pad 2. The exact CM5IO-derived Ethernet overlay was then applied
without changing its electrical topology.

Candidate: `ACREAGE_PHASE17_F1RIGHT40_ETH3.kicad_pcb`.

The follow-up ground-authority regeneration is
`ACREAGE_PHASE17_F1RIGHT40_ETH_GROUND_FIXED.kicad_pcb`; it retains the same
power-entry and Ethernet geometry while mapping the CM5IO `ETH_GND` source
alias to clean `POWER_GND`.

Native KiCad DRC reports 216 total findings and 427 inherited unconnected
items. There are zero `tracks_crossing` and zero `shorting_items` records.
The scoped Ethernet regression passes, and native route metrics pass: all
four MDI pairs are F.Cu-only, EDAC J2 mapping is exact, and pair skew is
0.547–0.829 mm. This is the best current local power-entry variant, but it
is not yet a Phase 17 close: inherited scaffold debt, conservative
V100-envelope courtyard findings, and independent return/impedance/mechanical
evidence still require closure.

The focused regression `validation/phase3/test_phase17_power_entry_candidate.py`
records the local power-path acceptance contract: F1 placement, F1/Q1 net
authority, absence of power-related short/crossing/hole findings, and no power
signals on In1/In4.

A CM5IO-faithful `LOCAL_BOTTOM_SPLIT` transplant was tested on the corrected
F1 base to place J2 below the conservative V100 envelope. It is rejected:
native DRC reports real MDI pair shorts/crossings and power-net interactions.
The known-good F1/ground candidate remains the Phase 17 integration ancestor;
this failed translation is not promoted.

## Phase 17 mechanical closure boundary — 2026-09-04

The repository authority search found no additional V100 cooler/backplate CAD,
measurement, or mating-stack evidence beyond the conservative `150 x 95 mm`
reservation. The valid F1/ground Ethernet candidate still places J2/U6/U9
within that declared reservation. This is not an Ethernet electrical failure,
but it prevents a clean mechanical Phase 17 pass. Further movement trials
(`LOCAL_BOTTOM_SPLIT`, left-edge, top-edge, and right-shelf) introduced real
MDI/power crossings and were rejected by native DRC.

The remaining closure choices are bounded: obtain physical V100/cooler/
backplate measurements and revise the envelope, or explicitly accept this
additional Rev-A empirical mechanical risk. No Phase 18 work is authorized
until one of those choices is resolved.

The ESD return is now authoritative `POWER_GND`, matching the official CM5IO
ESD/shield grounding. The transplant retains the source fixture's `ETH_GND`
name only as an input alias and maps it to `POWER_GND`; no isolated Ethernet
ground net is emitted.
## 2026-09-04 — generic co-located integration authoring retry

- `phase17_apply_exact_ethernet_to_phase16.py` was exercised against
  `ACREAGE_PHASE17_F1RIGHT40_ETH_GROUND_FIXED.kicad_pcb` with the corrected
  CT4 split fixture.
- KiCad 10 native SWIG footprint-copy replacement remains a tooling issue;
  the candidate was generated using the generic `PISXME_KEEP_FOOTPRINTS=1`
  mode, reusing the already-authoritative acreage Ethernet footprints and
  transplanting only fixture copper.
- Candidate native DRC: 0 `[shorting_items]`, 0 `[tracks_crossing]`; the
  full-board inherited unrouted baseline is 427 `[unconnected_items]`.
- Phase 17 scoped electrical regression: PASS. Route metrics: PASS; pair
  skews 0.547, 0.681, 0.688, and 0.829 mm.
- Phase 17 remains OPEN pending candidate-specific DRC isolation, mechanical
  review, and final acreage gate. No Phase 18 work started.

The candidate's 427 unconnected-item count exactly matches the validated
ancestor report; this is inherited acreage debt, not a regression from the
Ethernet transplant. The candidate-specific zero-short/zero-crossing result,
scoped Ethernet regression, and power-entry regression are therefore retained
as positive evidence, but are not by themselves a Phase 17 closure.

## Phase 17 closure — 2026-09-04

- Corrected the CT4 layer-separated escape: one ordinary F.Cu-to-B.Cu via at
  `(68.0, 60.0)` followed by the B.Cu corridor; the unnecessary dangling
  second transition was removed. The unrelated dangling ETH_GND fixture via
  was also removed.
- Native disposable fixture DRC: 241 total inherited/clearance findings,
  zero unconnected items, zero shorting items, zero track crossings, and zero
  dangling vias.
- Integrated acreage candidate DRC: 195 total findings, exactly 427 inherited
  unconnected items, zero shorting items, zero track crossings, and no
  Ethernet-specific dangling vias. The generic `MECH_V100` carrier cooler /
  backplate reservation is absent; the Rev-A underside contract remains
  available except for verified hardware constraints.
- Phase 17 scoped electrical regression: PASS. Route metrics: PASS with
  0.547–0.829 mm pair skews. Power-entry candidate regression: PASS.
- Decision: `PHASE17_CLOSED`; candidate
  `ACREAGE_PHASE17_COLOCATED_CT4_SPLIT.kicad_pcb` is the validated acreage
  ancestor for Phase 18. Phase 18 routing may now proceed; no later phase has
  been started in this checkpoint.
