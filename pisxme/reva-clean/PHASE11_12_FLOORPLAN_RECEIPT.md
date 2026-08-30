# PiSXMe Rev A Clean — Phases 11/12 floorplan receipt

Checked: 2026-08-30. Status: `PISXME_REVA_CLEAN_PHASE11_12_CLOSED`.

`ACREAGE_FLOORPLAN.kicad_pcb` records the first 300 x 180 mm acreage study
with no routing. The V100 cooler/backplate reservation remains central;
power and regulators occupy the left service edge; service/debug are kept at
the lower-left; Ethernet and storage bridge occupy the right edge; and the
M.2 2280 service envelope is kept at the lower-right outside the V100
reservation. The CM5 underside candidate remains the selected orientation.

The study deliberately uses drawing-layer neighborhoods and conservative
keepouts, not fabricated fit claims. Phase 12 hostile review found no
intentional crossing corridor, no board-edge violation in the named zones,
and no routing workaround. Native DRC reports one intentional vertical-stack
courtyard overlap where the SXM2 connector sits inside the cooler reservation;
this is not a board-edge or routing violation and requires physical stack
clearance confirmation. Actual mating, cable bend, fastener, and assembly
order remain required reviews before stack/routing freeze.

`validation/phase3/test_phase11_floorplan.py` proves the native acreage
artifact contains all seven neighborhoods and zero routing.
