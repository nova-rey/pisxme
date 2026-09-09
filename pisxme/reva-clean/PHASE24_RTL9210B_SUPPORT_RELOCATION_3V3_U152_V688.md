# RTL9210B Path-B V688 — rejected U1.52 branch

V688 attempted a direct F.Cu U1.52-to-3V3-source branch. Native KiCad DRC
found three violations: the corridor contacted the C2 GND stitching via and
pad and reached the adjacent CLKREQ pull-up pad. Reject this route; the
crystal micro-island must be co-moved or re-escaped before another U1.52
attempt.
