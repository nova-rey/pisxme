# Protected-bus R3 bounded corridor revision

- Decision: `BINDING_DECISION`
- Base: current HEAD `57332e98`
- F.Cu: local pad escapes and local fuse/protection/control loops only.
- In2.Cu: nine unique ordered fused-positive lanes from F1-F9 to the `12V_BRANCH_JOIN` field at x=103.5..112; no crossings/shared segments.
- In4.Cu: nine distinct ordered return lanes to `POWER_RETURN_JOIN` at x>=104.
- In3.Cu: sole post-protection `12V_PROTECTED` plane from U1/Q1 toward J1 at x≈116.5..124.
- Forbidden: F.Cu source-to-join trunk except local escapes; no star fanout, long raw/fused trunk, via-in-pad, or single-via high-current path.
- Preserved: J1/J5/J6/J9 anchors, 3x3 F1-F9 grid, six-layer stack, high-speed/timing corridors, GND/connector geography, 8.50 mOhm hot-path limit.
- Required checks: exact-SHA fresh Light; nine-branch census; zero branch shorts/crossings; machine-checkable F.Cu clip and unique In2/In4 lanes; per-branch resistance/thermal extraction; complete source-to-J1 <=8.50 mOhm proof.
