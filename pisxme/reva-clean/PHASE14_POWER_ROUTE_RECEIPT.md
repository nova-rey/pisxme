# Phase 14 V100 power-route candidate

Status: `CANDIDATE_IN_PROGRESS`

`phase14_power_route.py` creates `ACREAGE_POWER_PHASE14.kicad_pcb` from the
validated native-netlist materialization. It adds one broad F.Cu
`12V_PROTECTED` zone over the Q1/Q2-to-SXM2 corridor and filled inner-layer
return-reference zones on In1 and In4. The protected zone reaches both branch
FET outputs and all 130 explicit SXM2 power contacts, so the candidate does
not create a single guessed endpoint contact or single-neck feed.

This is not Phase 14 closure. The remaining gate evidence is binding:
branch-sharing and fuse/connector contact analysis, thermal loss
and temperature margin, and hostile DRC/clearance review. The 130/70 endpoint
row map is still `REV_A_EMPIRICAL_RISK` and requires continuity confirmation
against the actual V100 module before fabrication.

`validation/phase3/phase14_power_analysis.py` samples the filled protected
polygon across the complete Q1/Q2-to-SXM2 window. Its current candidate has a
minimum 98 mm copper span; using the 1 oz basis, the shared-branch envelope is
below 5 A/mm2, the continuous single-branch envelope below 9 A/mm2, and the
conservative 75 mm sheet-resistance drop bound below 120 mV. These are
geometry-backed design bounds, not measured temperature or connector-contact
results; the script is a prerequisite regression for the remaining gate.
Using the canonical repository power budget (`28.5 A` continuous, `34.3 A`
peak, two `15 A` branch fuses), the balanced continuous branch is 14.25 A and
65 power contacts per branch would carry 0.219 A/contact versus the Amphenol
published 0.45 A/contact rating.
That calculation assumes the public reverse-engineered row classification and
balanced sharing; both still require continuity/current measurements on the
actual V100 assembly.

The same analysis applies the CSD19536KCS datasheet maximum 62 C/W
junction-to-ambient metric at a 40 C design ambient: the shared-branch FET
estimate is 74.0 C junction below the 175 C absolute maximum. The 34.3 A
one-branch peak produces a 237 C steady-state θJA bound and therefore must be
cleared by the 15 A branch fuse; it is not claimed thermally safe as a
sustained single-branch condition. This is a datasheet/test-board bound,
not a fabricated-board thermal measurement; copper spreading, airflow,
package mounting, and sustained sharing remain explicit Rev-A validation
items.

The candidate intentionally has no tracks: the acreage placement is not yet a
production-routed placement, and provisional branch legs would cross adjacent
fuse-holder/connector/CM5 pads. A subsequent via/neck experiment also exposed
incorrect hierarchical-net assignment in the KiCad Python ABI and was
rejected. The frozen six-layer `JLC06161H-7628` basis
and ordinary through-via-compatible layer policy remain in force; no Phase
16+ high-speed routing is added.

The previous Phase 14 DRC baseline exposed a local Molex footprint defect: the
generated 0039300020 pattern's mechanical holes overlapped its electrical
hole-clearance envelope. This is now corrected and closed as a footprint
sub-gate: the local pattern follows Molex SD-5569-002 for 5569-02A2*-* (pad 1
at 0.00 mm, pad 2 at 5.50 mm, one 3.00 mm NPTH peg at -7.30 mm). Fresh native
DRC has no J5/J6 hole-clearance or solder-mask-bridge violation. The remaining
DRC and unconnected-item counts are broader pre-existing acreage-candidate
debt and do not constitute Phase 14 closure.

A second footprint authority gap is now recorded for the selected Littelfuse
`178.6165.0001` holder. The local four-pin pattern has overlapping pad/hole
geometry at F1/F2; native DRC reports those violations. Littelfuse drawing
`CVP-PE40-0006 Rev A` is the authority, so the holder remains
`LAND_PATTERN_REVIEW_OPEN` and power routing/release is held until its four
holes are regenerated from the 5.8 mm/3.5 mm manufacturer layout.
