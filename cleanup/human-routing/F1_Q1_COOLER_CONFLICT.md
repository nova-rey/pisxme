# F1/Q1 cooler conflict

## Contract

The topside cooler-owned XY reservation is `x=10..160 mm`,
`y=22.5..117.5 mm`. The active footprints are on the top side.

| Ref | Center | Documented body outline | Intrusion |
|---|---:|---:|---:|
| F1 | `(80,116)` | 22 x 8 mm | reaches `y=120`; enters the reservation by 1.5 mm |
| Q1 | `(110,116)` | 10 x 6 mm | reaches `y=119`; enters the reservation by 1.5 mm |

F1 is the 15 A fuse holder and Q1 is the high-current protection MOSFET. This
is not a cosmetic courtyard warning: both are tall/service-relevant parts in
the cooler's reserved XY footprint. The south-side F2/Q2 row is outside the
reservation and is not part of this specific conflict.

## Root cause

The protection row was placed at the boundary of the original power region
without reserving the full cooler-owned XY envelope. The resulting current
path is electrically plausible but mechanically under-constrained.

## Required correction

Move the complete affected branch-A protection group far enough south to leave
positive clearance from `y=117.5`, while keeping the raw-input connector,
fuse, protection controller, MOSFET, and protected-rail transition short and
wide. The move must be accompanied by a local high-current reroute and a
thermal/current recheck. Do not amend the cooler contract merely to preserve
the existing placement.
