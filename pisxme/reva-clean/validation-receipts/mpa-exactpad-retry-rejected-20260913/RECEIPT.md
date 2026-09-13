# MPA exact pad implementation retry — 2026-09-13

- Base: `6ecacfbe`
- Worker: qualified `pisxme-kicad-light:v1`, native KiCad `10.0.6`, 1 CPU / 1 GiB, disposable workspace.
- Scope: one MPA-bound attempt only. U13/C30/C31/C32/C33 were placed at the binding locations; F2 moved to `(90,60)` and D2 to `(110,60)`. Routes were generated from native post-placement pad centers with unique through-vias and ordinary widths.
- Control contract: `STORAGE_SEL` = U12.9/U13.9/U14.4; `AUTO_PEDET` = J3.69/J8.2; `MODE_IN` = U14.2/J8.4. U14.2 was not routed to `AUTO_PEDET`.
- Targeted connectivity graph: all listed storage, control, and Branch-B endpoints are in one same-net component; see `targeted-connectivity.txt`. This is scoped graph evidence, not a clean-board claim.
- Native DRC after each incremental group: group 1 `490/499`; group 2 `572/499`; group 3 `655/499`; group 4 `742/499`; group 5 `760/499` (violations/unconnected items). Final classes include 22 `shorting_items`, 34 `tracks_crossing`, 324 `clearance`, 156 `track_width`; full data in `group-5-drc.json`.
- Result: rejected as a clean implementation candidate. The attempt demonstrates connectivity coverage but not legal copper. It does not establish a structural contradiction because the intermediate corridors were a single bounded implementation method and produced numerous collisions.
