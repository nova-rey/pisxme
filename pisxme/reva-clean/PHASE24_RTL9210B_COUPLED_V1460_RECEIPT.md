# RTL9210B coupled QFN escape receipt — V1460

Date: 2026-09-10  
Base: `PHASE24_RTL9210B_ACCEPTED_PRIMITIVES_V1428.kicad_pcb`

V1460 reallocated the complete `LANE0_RXN` source/corridor together with a
U1.66-to-exposed-pad GND escape. It preserved the active 0.2 mm track,
clearance, ordinary-through-via, and layer rules. Native DRC reported 15
violations / 10 unconnected items. The proposed GND path no longer failed at
the U1.66 pad itself, but collided with existing LANE0_TXP, LANE0_TXN, and
JTAG_TCK copper/field geometry.

Disposition: rejected route implementation. This is useful evidence that the
remaining Path-B issue is a coupled QFN source-field allocation, not a reason
to relax rules or alter Path A. V1428 remains the accepted isolated basis;
Path-B promotion remains OPEN.
