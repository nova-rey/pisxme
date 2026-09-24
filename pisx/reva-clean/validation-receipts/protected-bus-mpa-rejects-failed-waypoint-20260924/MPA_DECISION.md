# Macro Placement Authority — failed protected-bus waypoint

- Originating package: `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- Decision: reject waypoint `(24.514048,24.273596)` and its J5.2-to-F2.1 corridor.
- Evidence: fresh Light candidate `5acf732e30a7379eec73a7348150a277d8db0bb6` produced 926 DRC versus 919 baseline, including six new clearance violations and one new short between `PWR_SRC_J9_P1` and `12V_PROTECTED`.
- Preserve topology, layers, anchors, and global rules. No CAD edit authorized by this decision.
- Status: replacement legal corridor still required before another producer attempt.
