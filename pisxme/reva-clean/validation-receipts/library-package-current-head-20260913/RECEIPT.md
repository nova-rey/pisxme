# Phase 24 library/package current-head receipt — 2026-09-13

- Source commit: `be0c6dbce84e3a20effd9dab60d9e33316afeb8b`
- Candidate state: **baseline/current integrated candidate evidence only**; no producer or integration mutation
- CAD scope: no schematic, PCB, footprint, or library-table edits

## Result

**DONE_WITH_OPEN_CONTEXT_GAPS** for the assigned bounded package: 115 non-J1 instances resolve to exact project-local footprint files; two U6/U9 instances use the declared `Package_SON` system library; thirteen TP instances are embedded board-only footprints with no project `TestPoint` source/table entry. Electrical pad sets match local project footprint files for all checked project-local instances. Four connector/fuse groups omit only the local `MP1` non-plated mechanical pad, which is explicitly dispositioned.

## Inputs and context

- PCB `pisxme/reva-clean/PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb` SHA256 `75d2d37063818093429b44dbe4197005c2f94b23554a34947a68acaaa181bf7c`
- Schematic `pisxme/reva-clean/PiSXMe_RevA_Clean.kicad_sch` SHA256 `6eef63bd3d2b0b9fafc0150d3c34f636ce24a48b2ecbd3d28a5f0bfec167e9f1`
- `fp-lib-table` SHA256 `864698c14e65cd70a5b5a08d23a22477919bf29f167d26fc0eda73dd43b3be61`
- `sym-lib-table` SHA256 `3bb180e251be1f62b2be5bbe486b29263c56c6a49b7a26103a27bef29b80c311`
- Private corpus: `/home/nyx/PiSXMe-Library` (`Library/indexes/library-index.json`, `Library/provenance/sources.json`, U11/U12 geometry brief/index). Reference material remains private metadata/extracted facts only.

## Census

- `pcb_footprint_instances_total`: 131
- `non_j1_instances`: 130
- `unique_non_j1_footprints`: 28
- `project_local_exact_instances`: 115
- `system_declared_instances`: 2
- `embedded_missing_project_source_instances`: 13
- `electrical_pad_mismatches`: 0
- `mechanical_pad_omission_groups`: 2
- `testpoint_embedded_instances`: 13

## Non-J1 package/pin mapping

The complete machine-readable per-footprint/per-reference map, source hashes, pad counts, and dispositions is `mapping.json`. Local project footprint pad identifiers were compared against each corresponding PCB instance. The only four set differences are expected omissions of source-library `MP1` non-plated mechanical pads on F1/F2/J5/J6; electrical identifiers are equal.
- U11 JMS583_QFN64_8x8: 65 board pads (64 signal plus EP 65), local source hash 11918576998884d5885debb500966b20804f7d14394212379fad31d0e5669c05; package basis established, paste/mask/courtyard production review remains open.
- U12 HD3SS6126_RUA0042A: 43 board pads (42 signal plus EP 43), local source hash 9490928521cf2d8677da7bf188fc265664095d99978ae7c1f038da07adf33ffd; retained 0.40-mm pitch conflicts with TI RUA0042A 0.50-mm published pitch; no correction made.
- U13 HD3SS3412_RUA0042A: 43 board pads; project-local geometry recorded, with storage architecture unchanged.
- U7 TUSB9261IPVP_PVP0064A: 65 board pads; project-local 64-pin plus exposed-pad geometry recorded; pin/net contract remains subject to integrated acceptance.
- U6/U9 Package_SON:USON-10_2.5x1.0mm_P0.5mm: 10 pads each; table-declared system library reference, no table mutation made.
- TP1-TP13: one pad each, embedded in PCB, marked exclude_from_bom and exclude_from_pos_files; missing external TestPoint table/source is a context/documentation gap, not a net assignment change.

## Open context items

- U12 retained 0.40-mm pitch versus TI RUA0042A 0.50-mm evidence remains an existing package-authority conflict; no correction is justified here.
- U11 paste/mask/courtyard production review remains open.
- U6/U9 system-library resolution should continue to be proven only in the qualified Light project context; no global table mutation is proposed.
- TP1–TP13 are embedded, BOM/position-excluded probe footprints; adding or changing a library source would be a separate bounded decision.

## Limits and next action

- This receipt is a current-head static package/library result, not native ERC/DRC or manufacturing closure.
- Existing fresh Light/netlist/parity receipts remain scoped evidence for native and semantic checks.
- Recommended queue state: close this package as `DONE_WITH_OPEN_CONTEXT_GAPS`; keep the listed gaps visible as acceptance dependencies. No CAD candidate is returned.
