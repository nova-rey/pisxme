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
below 4 A/mm2, the worst single-branch envelope below 8 A/mm2, and the
conservative 75 mm sheet-resistance drop bound below 120 mV. These are
geometry-backed design bounds, not measured temperature or connector-contact
results; the script is a prerequisite regression for the remaining gate.
At the 12.625 A balanced branch envelope, 65 power contacts per branch would
carry 0.194 A/contact versus the Amphenol published 0.45 A/contact rating.
That calculation assumes the public reverse-engineered row classification and
balanced sharing; both still require continuity/current measurements on the
actual V100 assembly.

The same analysis applies the CSD19536KCS datasheet maximum 62 C/W
junction-to-ambient metric at a 40 C design ambient: the shared-branch FET
estimate is 66.7 C junction and the one-branch fault estimate is 146.6 C,
both below the 175 C absolute maximum. This is a datasheet/test-board bound,
not a fabricated-board thermal measurement; copper spreading, airflow,
package mounting, and sustained sharing remain explicit Rev-A validation
items.

The candidate intentionally has no tracks: the acreage placement is not yet a
production-routed placement, and provisional branch legs would cross adjacent
fuse-holder/connector/CM5 pads. The frozen six-layer `JLC06161H-7628` basis
and ordinary through-via-compatible layer policy remain in force; no Phase
16+ high-speed routing is added.
