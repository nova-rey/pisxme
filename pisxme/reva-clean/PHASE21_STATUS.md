# Phase 21 status — low-speed/control

Status: IN PROGRESS — live control inventory captured from the Phase 20
service-routed board.

The authoritative inventory is `PHASE21_CONTROL_INVENTORY.md`. It identifies
the remaining unrouted control classes without changing the Phase 19 storage
or Phase 20 SERVICE geometry:

- power-input gate and VCAP pairs;
- bridge 3V3/1V1 feedback, RT, and PG islands;
- U7 bridge reset duplicate-pad tie;
- CM5 PERST and existing regulator controls for regression comparison.

Phase 21 routing must keep these nets local, use only F.Cu/B.Cu ordinary
routing, avoid high-speed/regulator switch-node exposure, and preserve the
validated PCIe, USB3, SATA, Ethernet, and SERVICE artifacts.

The accepted coordinated candidate is
`PHASE21_CONTROLS_REGULATOR_CONTROLS_GATES.kicad_pcb`. It carries forward the
accepted reset, PG, VCAP, and bridge-3V3 FB repairs, then completes bridge
3V3/1V1 RT and FB controls and both LM74700 gate nets. The gate FETs were
relocated as coherent local control blocks; their electrical nets and power
topology are unchanged. Native KiCad DRC reports 187 violations, with zero
`shorting_items`, `tracks_crossing`, `track_width`, or `pth_inside_courtyard`.
The focused delta is inherited mechanical and warning residue only. The
regression test `validation/phase3/test_phase21_control_candidate.py` checks
all required control endpoints and the focused DRC census.

Phase 21 is CLOSED for progression to Phase 22.

The separate gate-corridor experiment `PHASE21_CONTROLS_VCAP_GATES.kicad_pcb`
is rejected: its long B.Cu routes intersect existing protected-12-V copper
and create true shorts/crossings. The gate controls remain open for a local
power-entry island repair; no layer or power-topology relaxation is made.
