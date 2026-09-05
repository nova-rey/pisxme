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

The current coordinated candidate is
`PHASE21_CONTROLS_FB3V3_REFILLED.kicad_pcb`. It contains passing local repairs for the
U7 reset tie, bridge 3V3 PG, bridge 1V1 PG, CM5 5V PG, and both LM74700 VCAP
connections, plus the bridge-3V3 FB island. Native DRC reports 183 violations
with no new focused
short/crossing/width/clearance class. Gate/VCAP and remaining regulator
FB/RT/control routes still require completion; no Phase 21 closure is claimed
yet.

The separate gate-corridor experiment `PHASE21_CONTROLS_VCAP_GATES.kicad_pcb`
is rejected: its long B.Cu routes intersect existing protected-12-V copper
and create true shorts/crossings. The gate controls remain open for a local
power-entry island repair; no layer or power-topology relaxation is made.
