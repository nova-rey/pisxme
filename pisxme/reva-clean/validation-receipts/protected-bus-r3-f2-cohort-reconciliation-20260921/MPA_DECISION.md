# MPA F2 cohort reconciliation

Decision ID: `PISXME-P24-R3-F2-COHORT-RECONCILIATION-20260921`
Work package: `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
Base: `c2aed9eb`; decision: `BINDING_DECISION`.

Reject `T_F2=(0,+11.25mm)`. Freeze F2 top-side at `(64.00,15.00,0deg)` with native raw pads `(57.60,13.75)`, `(57.60,16.25)`, `(61.10,13.75)`, `(61.10,16.25)` and fused pads `(66.90,13.75)`, `(66.90,16.25)`, `(70.40,13.75)`, `(70.40,16.25)`. F1/F3 and all other fuse rows remain fixed. Support cohort D1/C3/U1/Q1/U2/Q2/C4/D2/TP2 remains fixed at its current coordinates.

Route J5.2 raw through a short F.Cu escape and ordinary through-via into In2.Cu to the actual F2 west/raw pad field. Route F2 fused east pads in In2.Cu to the distributed join at x≈103.5..112. Route J5.5 as an independent In4.Cu return. F.Cu source-to-join trunk remains forbidden except local escapes/control loops. Preserve J1/J5/J6/J9 anchors, six-layer roles, high-speed corridors, protected copper, J7 keepout, and <=8.50mOhm path.

Acceptance: exact eight-pad geometry, no P2/P1/P3/12V_IN_A shorts, no F2/F5 courtyard overlap, nine-branch/27-net census, native Light DRC/connectivity, branch resistance and complete hot-path evidence.
