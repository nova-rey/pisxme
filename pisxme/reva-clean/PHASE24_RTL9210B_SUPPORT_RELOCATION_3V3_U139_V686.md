# RTL9210B Path-B V686 — rejected U1.39 inner branch

V686 extended the V685 3V3 source vertically through the QFN field. Native
KiCad DRC found one RTL_1V1/RTL_3V3 short at the existing via (99.2,63.5).
Reject this route; it reduced the open count but violated the physical rule.
