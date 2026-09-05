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
validated PCIe, USB3, SATA, Ethernet, and SERVICE artifacts. No Phase 21
closure is claimed yet.
