# RTL9210B U1.63 rail / RXN rehome receipt — V1469

Date: 2026-09-10
Base: `PHASE24_RTL9210B_U166_JOIN_RXP_EAST_UP_V1466.kicad_pcb`
Candidate: `PHASE24_RTL9210B_U163_RXN_REHOME_V1469.kicad_pcb`

V1469 co-authors the remaining lower QFN field. The existing U1.60
RTL_1V1 branch is retained; U1.63 at its native (94.05,71.20) center exits
west to x=92.80, transitions at y=69.80, and joins the existing x=88 rail.
U1.65/RXN is rehomed to an x=88.80 transition column so the new U1.63 rail
via does not collide with it. The V1466 direct U1.66-to-U1.69 GND join and
RXP escape are retained.

No via-in-pad, plane-layer signal, clearance relaxation, or footprint change
was used. Native KiCad 10.0.5 DRC reports **0 violations / 8 unconnected
items**. Native saved-board connectivity passes U1.66→U1.69, all four lane
endpoints (U1.64→J1.43, U1.65→J1.41, U1.67→J1.47, U1.68→J1.49), and the
complete U1.63 RTL_1V1 cohort to C4.1. Removing the U1.63 source segment or
RXN source segment in separate saved-board copies makes the corresponding
assertion fail.

V1467 and V1468 are retained rejected route-implementation evidence. V1469
is an accepted Path-B QFN/lane/rail primitive, not full RTL9210B, storage, or
Phase 24 closure. Remaining GND pad 45, RSET, crystal, REFCLK, firmware,
programming, procurement, and integrated mode gates remain open.
