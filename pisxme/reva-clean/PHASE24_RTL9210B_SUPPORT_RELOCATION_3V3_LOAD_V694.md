# RTL9210B Path-B V694 — rejected 3V3 load corridor

V694 attempted the U1.20-to-C3/U2 load corridor with a descent at x=102.5.
Native KiCad DRC found one SPISI/U1.20 source-field short. Reject this route
implementation; the downstream topology remains a valid target.
