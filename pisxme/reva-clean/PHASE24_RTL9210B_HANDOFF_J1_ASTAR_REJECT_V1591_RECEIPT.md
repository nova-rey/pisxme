# RTL9210B handoff-to-J1 launch diagnostic — V1591

Date: 2026-09-10

Starting with the accepted V1590 six-net west QFN handoff primitive, V1591
removed only the six disposable high-speed nets and searched native F.Cu/B.Cu
ordinary-via paths from explicit handoff pads at x=85 mm to the actual J1/M.2
contacts. The fixed U1 orientation, package escape, and unrelated geometry
were unchanged.

The search found paths for `REFCLK_P`, `LANE0_TXN`, `LANE0_RXP`, and
`LANE0_RXN`, then found no legal remaining path for the next REFCLK/lane
launch. No complete candidate was saved or promoted. This isolates the
remaining route-implementation constraint to the combined M.2/J1 launch
field and available two-layer corridors; it is not evidence against the
accepted V1590 QFN escape. Native DRC rules and the approved layer contract
were unchanged.
