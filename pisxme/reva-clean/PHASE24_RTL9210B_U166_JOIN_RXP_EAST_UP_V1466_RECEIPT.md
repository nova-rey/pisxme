# RTL9210B U1.66 GND / RXP escape receipt — V1466

Date: 2026-09-10
Base: `PHASE24_RTL9210B_ACCEPTED_PRIMITIVES_V1428.kicad_pcb`
Candidate: `PHASE24_RTL9210B_U166_JOIN_RXP_EAST_UP_V1466.kicad_pcb`

V1466 co-authors the native QFN source field using the actual loaded pad
centers. U1.64/`LANE0_RXP` departs east to x=95.00 mm, rises to y=70.00 mm,
then uses ordinary through-vias and the retained remote corridor. U1.66/GND
joins directly on F.Cu to the left/bottom edge of U1.69's 4.8 mm exposed pad.
No via-in-pad, plane-layer signal, clearance relaxation, or footprint change
was used.

Native KiCad 10.0.5 DRC: **0 violations / 9 inherited unconnected items**.
All four lane-0 endpoints pass native saved-board connectivity:
U1.64→J1.43, U1.65→J1.41, U1.67→J1.47, and U1.68→J1.49. U1.66→U1.69
also passes. The nine remaining opens are inherited incomplete support
items in the disposable parent; they are not waived by this receipt.

Saved-board negative controls remove the direct GND join and the RXP source
segment separately; each required connectivity assertion then fails. This
proves the result uses actual pads/tracks/vias rather than synthetic graph
edges.

Disposition: **accepted Path-B QFN escape primitive**. It supersedes V1461 as
the current U1.66/RXP local basis, but does not close RTL9210B support,
firmware/programming, integrated storage, or Phase 24.
