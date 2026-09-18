# Phase 24 library, pin, and provenance closure packet

- Package: `P24-LIBRARY-PIN-PROVENANCE-CLOSURE`
- Campaign: `phase24-phase25-acreage`
- Assigned base: `2d6e3ea4cfd08f587d42be66cc37a77838e5641a`
- Reviewed source: `8cd2ff8aa75636bdef44ef87285853bcdabe21bc`
- Scope: authority/evidence only; no protected-bus CAD edits; no global rule changes.

## Result

**WAITING**. The bounded audit closes the nonblocking identity/disposition rows, but cannot truthfully close the package because U12 has a proven package-identity contradiction and U11 still lacks manufacturer assembly land-treatment evidence.

## Authority matrix

| Item | State | Evidence-backed disposition |
|---|---|---|
| U12 `HD3SS6126RUAR` / `RUA0042A` | **BLOCKED** | The project-local footprint has 42 signal pads plus EP43 and matching land dimensions, but its perimeter centers advance at 0.40 mm. TI's RUA0042A authority specifies 0.50 mm pitch. The prior 0.50 mm correction candidate was rejected after fresh Light reported 401 DRC violations / 499 unconnected items and solder-mask bridge errors against existing routing. Do not route or promote either geometry until Package Authority supplies an intentional-variant explanation or a coordinated corrected producer is validated. |
| U11 `JMS583-QHFA3A` | **UNPROVEN** | Project/JMicron evidence establishes QFN64 8.0 x 8.0 mm, 0.40 mm pitch, 0.15–0.20 mm terminal width, and 4.46 mm EP. Manufacturer paste-windowing, mask expansion, and courtyard details are absent. Hold as an explicit assembly/DFM evidence gate; do not infer them from a generic library. |
| U6/U9 `Package_SON:USON-10_2.5x1.0mm_P0.5mm` | **AUTHORIZED_WITH_EXPLICIT_PROTOTYPE_DISPOSITION** | `fp-lib-table` declares the KiCad system library. A read-only current-head DRC context check with local KiCad 10.0.5 produced no Package_SON/library-resolution warning. This establishes project context resolution, not die identity or full release qualification. |
| TP1–TP13 | **AUTHORIZED_WITH_EXPLICIT_PROTOTYPE_DISPOSITION** | Each is one-pad `TestPoint_THTPad_D1.0mm_Drill0.5mm`, embedded in the board, with `exclude_from_bom` and `exclude_from_pos_files`. Existing BOM disposition confirms intentional probe-only use. No project TestPoint source is needed for the prototype board; release regeneration may add one later. |
| Path-A critical component/procurement records | **AUTHORIZED_WITH_EXPLICIT_PROTOTYPE_DISPOSITION** | Existing provenance packet closes selected Path-A technical identities and keeps RTL9210B Path B isolated/unpromoted. Procurement refresh, firmware/programming access, and fabricated-hardware behavior remain open owning rows; no evidence is fabricated. |

## Current context census

- PCB footprint instances: 131.
- U6/U9 system-library instances: 2.
- Embedded test probes TP1–TP13: 13, all intentionally excluded from BOM/position outputs.
- Current local KiCad 10.0.5 context check: 300 DRC violations / None unconnected items; no Package_SON/library/missing-footprint warning occurred in the native report. This is context evidence only, not integrated closure.
- Schematic, PCB, project, rules, and library hashes are recorded in `PROVENANCE_MATRIX.json` and `SHA256SUMS`.

## Next authority action

Package/Footprint Authority must resolve U12 with either an authoritative package-specific 0.40 mm explanation or a corrected 0.50 mm geometry plus coordinated fanout/zone rework. U11 needs manufacturer assembly land-treatment evidence or a signed prototype DFM disposition. No protected-bus CAD work is authorized by this packet.
