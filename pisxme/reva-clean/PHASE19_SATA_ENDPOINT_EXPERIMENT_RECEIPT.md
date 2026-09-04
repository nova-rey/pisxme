# Phase 19 SATA endpoint experiment

Status: `REJECTED`; Phase 19 remains active.

Candidate: `ACREAGE_PHASE19_SATA_RIGHT_EDGE.kicad_pcb`

This experiment moved J3 to the right-side acreage at (230,100) mm, rotation
90°, while retaining U7 and the validated Phase 18 USB3 corridor. SATA
authority remained unchanged: U7 57/56/60/59 to J3 1/2/3/4. The two SATA
pairs were split across F.Cu and B.Cu with ordinary through-vias outside the
U7 pad field.

Native DRC result: zero SATA shorting items, but six track crossings remain.
They are caused by the long corridor interacting with the frozen PCIe/PERST
geometry and by the pair turn columns near the connector launch. No Phase 19
candidate is accepted from this experiment. The next attempt must keep the
SATA route local to an actually open region instead of crossing the board,
while preserving the same authority and layer contract.
