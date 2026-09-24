# MPA Semantic Correction — Protected-Bus Corridor

- Package: `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- Date: 2026-09-24
- Status: binding corridor-text correction; no CAD edited.

The prior MPA text was internally contradictory: its first leg was diagonal while
diagonals were forbidden, and its clearance basis used fuse silkscreen bounds.
The corrected all-orthogonal F.Cu corridor is:

`J5.2 (16.20,25.00) -> (16.20,27.40) -> (50.00,27.40) -> (50.00,13.75) -> F2.1 (57.60,13.75)`

J5.2 and F2.1 are both `PWR_SRC_J5_P2`. Current-board courtyard evidence:
F1 is x=24.00..48.00, y=3.00..27.00; F2 is x=52.00..76.00, y=3.00..27.00.
The horizontal centerline y=27.40 leaves 0.40 mm from the courtyard edge and
0.30 mm copper edge clearance for a 0.20 mm track. The x=50.00 vertical is
2.00 mm from each courtyard edge and 1.90 mm copper-edge clearance.

No via, In2 raw lane, endpoint via, or diagonal is authorized. Preserve the
local `REV_A_TOP_POWER_GND_RETURN_FULL` clip, fixed `12V_PROTECTED` geometry,
In1/In4 returns, and all R3 electrical/current/thermal/DFM/DRC gates.
