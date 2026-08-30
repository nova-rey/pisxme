# Phase 14 V100 power-route candidate

Status: `CANDIDATE_IN_PROGRESS`

Frozen candidate identity for this receipt: `ACREAGE_POWER_PHASE14.kicad_pcb`,
SHA-256 `e7aa18f6804c4709dec9f49a78f119be906e7103d1dc6df71f29972d35ae5856`.

`phase14_power_route.py` creates `ACREAGE_POWER_PHASE14.kicad_pcb` from the
validated native-netlist materialization. It adds nineteen named-pad-resolved,
2.0 mm B.Cu power links for J5/J6 input-to-fuse and fuse-to-Q1/Q2 continuity,
one broad F.Cu `12V_PROTECTED` zone over the Q1/Q2-to-SXM2 corridor, and filled
inner-layer return-reference zones on In1 and In4. The protected zone reaches
both branch FET outputs and all 130 explicit SXM2 power contacts, so the
candidate does not create a single guessed endpoint contact or single-neck
feed.

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

The candidate intentionally has no high-speed tracks. The nineteen released power
links stay on B.Cu and resolve endpoints from the actual current placement;
their 2.0 mm width preserves the 0.2 mm clearance around the 2.54 mm fuse
holder pitch. A subsequent via/neck experiment also exposed incorrect
hierarchical-net assignment in the KiCad Python ABI and was rejected. The
frozen six-layer `JLC06161H-7628` basis
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

A second footprint authority gap was recorded for the selected Littelfuse
`178.6165.0001` holder. Independent exact-MPN review of drawing
`CVP-PE40-0006 Rev A` established eight solder holes plus a central spigot.
The local footprint now uses the manufacturer-derived eight-hole coordinates,
conservative central NPTH clearance, and maps pads 1-4 to input and 5-8 to
fused output. Fresh native DRC removes the holder self-overlap; remaining
placement/courtyard findings remain part of the open Phase 14 gate.

The latest native DRC run reports 215 violations and 305 unrouted connections
for the acreage candidate. There are no `shorting_items` in the current power
route report, and the remaining route-adjacent `unconnected_items` are the
deliberately unrouted regulator/control fanout and V100 control nets. The
focused regression `validation/phase3/test_phase14_power_drc.py` passes for
the frozen power-path references. This is
evidence for the power candidate only, not a board-wide DRC pass.
