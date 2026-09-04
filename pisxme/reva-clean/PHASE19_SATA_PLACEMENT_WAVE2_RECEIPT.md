# Phase 19 SATA placement wave 2

Date: 2026-09-04
Status: OPEN — all candidates rejected; Phase 19 remains active.

The validated Phase 18 ancestor was preserved. No Phase 16 PCIe, CM5, V100/SXM2,
power topology, stack, or layer-policy change was made. The generic underside
cooler/backplate reservation was not used as a constraint.

## Evidence

| Candidate | Change | Native DRC result | Decision |
|---|---|---:|---|
| `ACREAGE_PHASE19_SATA_LOCAL_OPEN` | J3 at (120,120), short local launch | 2 shorts, 1 crossing, 426 unconnected | reject: U7/J3 pad-field and PCIe hole interactions |
| `ACREAGE_PHASE19_SATA_TOP_EDGE` | J3 above the PCIe corridor | crossings with frozen PCIe/CM5 reference tracks and C4 | reject |
| `ACREAGE_PHASE19_SATA_POST_PER0` | lateral escape beyond CM5 PER0 endpoint | crossings/shorts at the U7 pad field and reference branch | reject |
| `ACREAGE_PHASE19_SATA_C4_ESCAPE` | local doglegs around C4 | C4/pad-field and frozen PER0/J1 interactions | reject |
| `ACREAGE_PHASE19_SATA_LEFT_TOP` | left/top J3 with C4 translated in disposable board | 209 total; SATA intersects frozen reference/PER0 and J3 overlaps Ethernet shield region | reject |
| `ACREAGE_PHASE19_STORAGE_TOP_ISLAND` | move U7/J3 to top acreage and rebuild USB3 | 332 total; USB3 crosses existing Ethernet and CM5 fanout geometry | reject: moving the whole island requires a coordinated USB3 launch |

The inherited acreage DRC debt remains present in these disposable boards. The
listed new shorts/crossings are candidate-introduced findings; they do not pass
the Phase 19 gate. No Phase 20 work started.

## Root cause refined

The active U7 placement has SATA pads on the top pad row, but C4 occupies the
direct RX escape and CM5 `PER0_P`/PCIe/reference trunks occupy the natural upper
corridor. Moving only J3 cannot remove the U7 escape obstruction. Moving U7
requires a coordinated USB3 re-route because the Phase 18 USB3 route is
placement-specific. This is a placement/routing integration problem, not a
storage schematic or M.2 authority failure.

## Next authorized experiment

Use a coordinated storage-island move: select an open acreage location for U7,
J3, and storage-local support, remove only the old placement-specific USB3/SATA
copper, and regenerate both USB3 and SATA launches together. Keep the connector
clear of J1/Ethernet bodies and keep all four SATA pairs on short, separated
F.Cu/B.Cu corridors with ordinary through-vias only.

Scripts and disposable boards are retained beside this receipt for reproducible
review. The consultant unblocker session timed out and was not treated as an
engineering result; a separate high-speed PCB review was dispatched.

## Wave 3 continuation

The open mid-acreage placement `(U7 120,140; J3 145,125, rotation 90)` removes
the frozen PCIe/CM5 corridor and mechanical collisions. A SATA-only routing
trial using pair-layer separation reduced the new failure to local launch
crossings/clearance at the U7 and connector pad fields (`205` total DRC
violations, `430` unconnected inherited/placement records). It is not yet a
pass because the SATA source and connector dogbones still need a non-crossing
ordering. The next experiment keeps this placement, reorders the orthogonal
pair exits, and then regenerates USB3 around the same island before promotion.
