# Rejected local-support relocation probe

Date: 2026-09-10  
Candidate: `PHASE24_RTL9210B_MIC2545A_SUPPORT_RELOCATED.kicad_pcb`  
Generator: `phase24_rtl9210b_mic2545a_support_relocated.py`

## Verdict

`REJECTED_ROUTE_IMPLEMENTATION`

This is the first bounded relocation-class experiment after the source-row
escape probes. It preserves the accepted RTL9210B 0-degree/top-side V1517
baseline and moves only the MIC2545A support island. It is not production
authority and its copper must not be promoted.

## Native evidence

KiCad native DRC reports 26 violations and 5 unconnected items. The failures
are concrete implementation defects: `ISOLATEB` still violates the U1
south-row clearance, the new `SSD_3V3` route collides with the existing
`PEDET`/`RTL_5V`/ground field, the `RTL_3V3` route crosses `PERST_N` and does
not join the intended baseline endpoint, and the local ground vias/joins are
not physically connected. The support island also has board-edge and
via-to-via spacing violations.

The result rejects this particular relocation geometry, not the MIC2545A
support topology or the frozen RTL9210B orientation. It demonstrates that a
support move without first reserving the U1 south-row and existing PEDET/
power corridors is insufficient.

Raw native report: `PHASE24_RTL9210B_MIC2545A_SUPPORT_RELOCATED-drc.rpt`.

## Next action

Stop point-perturbing this class. The next implementation must co-route the
U1 south-row departures and support control/rail handoffs as one physical
channel, or use a genuinely separate local support corridor with explicit
layer ownership and via envelopes. No orientation, Path-A, or architecture
decision is reopened.
