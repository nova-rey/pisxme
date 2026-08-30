# Phase 14 V100 power-route candidate

Status: `CANDIDATE_IN_PROGRESS`

`phase14_power_route.py` creates `ACREAGE_POWER_PHASE14.kicad_pcb` from the
validated native-netlist materialization. It adds one broad F.Cu
`12V_PROTECTED` zone over the Q1/Q2-to-SXM2 corridor and filled inner-layer
return-reference zones on In1 and In4. The protected zone reaches both branch
FET outputs and all 130 explicit SXM2 power contacts, so the candidate does
not create a single guessed endpoint contact or single-neck feed.

This is not Phase 14 closure. The remaining gate evidence is binding:
field/current-density and voltage-drop extraction from the actual filled
geometry, branch-sharing and fuse/connector contact analysis, thermal loss
and temperature margin, and hostile DRC/clearance review. The 130/70 endpoint
row map is still `REV_A_EMPIRICAL_RISK` and requires continuity confirmation
against the actual V100 module before fabrication.

The route uses the frozen six-layer `JLC06161H-7628` basis and ordinary
through-via-compatible layer policy. No Phase 16+ high-speed routing is added.
