# RTL9210B coupled QFN field receipt — V1461

Date: 2026-09-10  
Base: `PHASE24_RTL9210B_ACCEPTED_PRIMITIVES_V1428.kicad_pcb`

V1461 co-authored the U1.66 exposed-pad GND escape with all four lane-0
source/corridor allocations. It preserved the 0.2 mm track/clearance rules,
ordinary through-vias, and the existing layer policy. Native DRC reported 19
violations / 14 unconnected items. The failures include an RXP/RXN
transition collision and exposed-pad GND conflicts with RTL_1V1 and RTL_3V3.

Disposition: rejected. This is route-implementation evidence, not a Path-B
architecture rejection or a reason to relax manufacturing rules. Path-A and
its V54 storage parent are unchanged.
