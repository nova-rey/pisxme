# RTL9210B clearance-aware handoff-to-J1 rejection — V1594

Date: 2026-09-10

V1594 used actual source and connector pad rectangles and an exact 0.4 mm
centerline reservation test while searching the six handoff-to-J1 nets on
F.Cu/B.Cu with ordinary through-vias. All six endpoint paths were generated.

Native KiCad 10.0.5 DRC rejected the result with **87 violations**, including
lane-0 P/N via shorting and multiple sub-0.2 mm track/via clearances. The
planner's centerline spacing model does not yet model via diameter and
connector launch separation sufficiently. No route was promoted and no rule
was relaxed. V1590 remains the accepted local QFN escape primitive.
