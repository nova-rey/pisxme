# RTL9210B Path-B V684 — rejected 3V3 source route

V684 attempted a direct F.Cu/B.Cu source route from R2/R3 to an inner QFN
RTL_3V3 pad. Native KiCad DRC found nine violations, including a CLKREQ_N
short, RTL_1V1 crossings, and contact with the QFN pad field. Reject this
source route; no production or Path-A asset was changed.
