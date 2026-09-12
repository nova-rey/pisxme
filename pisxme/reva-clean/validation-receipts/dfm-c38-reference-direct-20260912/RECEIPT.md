# C38 reference DFM repair — promoted — 2026-09-12

Producer base: `4440c83b`.
Only C38's F.SilkS reference moved from local (0,0) to (0,2.5). No pads,
nets, copper, vias, outline, schematic, rules, or footprint geometry changed.

Fresh Light JSON DRC on the producer candidate: **338 violations / 499
unconnected items**, with silk-over-copper findings reduced from 28 to 26.
The scoped repair is integrated into the canonical PCB; a fresh exact-head
validation is still required after commit.
