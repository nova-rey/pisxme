# Phase 24 storage support-field trial — V196

Date: 2026-09-10
Base: `PHASE24_STORAGE_V75_COAUTHORED_V194.kicad_pcb`
Candidate: `PHASE24_STORAGE_V75_COAUTHORED_V196.kicad_pcb`

V196 regenerates the U11 JMS_AVDDL source handoff around the adjacent
JMS_AVDD33 field, using a native F.Cu-to-B.Cu transition and an outboard
return to C83. Saved native connectivity confirms U11.20-to-C83.1 and the
previous U11.51-to-Y10.2 XOUT connection.

USB3 ten-net connectivity, complete SATA endpoint connectivity,
schematic-to-PCB parity (814/1263/0), and the saved-board removed-track
negative control pass. Native DRC is 617 violations / 347 opens with zero
`shorting_items`; the earlier XOUT and STORAGE_SEL shorts are absent. V196 is
accepted as the current support-field basis, not Phase 24 closure. Remaining
crossings, opens, and manufacturing findings are not waived.
