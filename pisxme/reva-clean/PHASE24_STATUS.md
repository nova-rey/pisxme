# Phase 24 acreage validation status

Status: IN PROGRESS — native ERC and netlist pass; schematic↔PCB component
parity remains open.

## Closed in this checkpoint

- The clean project now resolves all 34 custom symbols through the assembled
  `PiSXMe_RevA_Clean_complete.kicad_sym` library.
- `phase24_repair_root_hierarchy.py` generically replaces the malformed root
  interior/diagonal wiring with outward sheet-edge stubs and named root
  associations, preserving child UUIDs and sheet instances.
- The CM5 sheet border is extended where the legacy final pin was outside its
  rectangle.
- Two unused MIPI1 D2 pins are explicitly marked no-connect; they are outside
  the Rev A interface contract.
- Native KiCad 10.0.5 ERC with `--severity-error` reports `Found 0 violations`.
- `validation/phase3/test_phase24_native_final_authority.py` passes.

## Netlist closure

The warning was caused by four regulator 22 uF capacitors retaining stale
`(instances)` references C30–C33 after their symbol properties were renumbered.
`phase24_repair_duplicate_refs.py` updates both serialized representations to
C44–C47.  KiCad 10.0.5 now exports a non-empty netlist with no annotation
warning.

Artifacts: `PHASE24_NATIVE_ERC_FINAL2.rpt`, `PHASE24_NETLIST_FINAL5.xml`, and
the Phase 24 native-authority regression.

## Remaining parity repair

Fresh comparison of `PHASE24_NETLIST_FINAL5.xml` against
`PHASE23_TEST_DEBUG_PADS_V5.kicad_pcb` found schematic components with no PCB
footprint: `Y1`, `R23`, `C42`, `C43`, and `C44`–`C47`.  These are real storage
clock and regulator support components, not optional debug artifacts.  The
first disposable clock graft was rejected because its historical hard-coded
U7 clock-row coordinates produced true shorts; it is retained only as failed
evidence.  Phase 24 stays open until a coordinate-derived, native-DRC-clean
materialization and parity check are complete.

The next coordinate-derived candidate, `PHASE24_SUPPORT_MATERIALIZED`, was
also rejected.  Its clock corridors crossed inherited SATA/USB copper and its
U5-side bulk-cap graft entered existing regulator pad/return geometry.  This
establishes that the missing support must be integrated by regenerating the
coordinated storage/regulator local routes, not by overlaying support copper
onto the Phase 23 ancestor.

The `PHASE19_RELOC_U270J190_COORD49_FULL` storage-only donor was then tested
as a coordinated transplant.  It contains USB3, SATA, and clock copper, but
its relocated USB3 corridor crosses the frozen V5 PCIe corridor after merge.
It was rejected.  The valid next class is to retain V5's proven U7/J3
high-speed placement and add an obstacle-aware clock route locally, followed
by a separately coordinated U5 bulk-cap island.

## Latest bounded experiment

`phase24_materialize_support_v2.py` generated `PHASE24_SUPPORT_V2.kicad_pcb`
from actual U7 pad coordinates, with the clock parts in open acreage and the
four schematic-authoritative U5 capacitors materialized. It was rejected by
native DRC (`234` violations, `409` unconnected items): the attempted common
B.Cu clock surface still crossed inherited SATA copper, crossed between clock
branches, and produced U7 pad-field shorts. This is not evidence against the
storage architecture. The next valid class is layer-separated clock fanout
with vias outside the U7 pad field, then an independent coherent U5
rail/return island. See `PHASE24_BLOCKER_REPORT.md`.

The first rotated-U7 discriminator was rejected as an authoring/tooling proof:
it changed U7 orientation but used a pre-rotation hard-coded clock endpoint
graph, producing pad mismatches. It is not a valid architecture failure. Any
next rotated-U7 experiment must query the post-rotation footprint and support
pad coordinates before creating tracks or vias.

The corrected rotated-U7 source-escape discriminator now derives post-rotation
U7 endpoints and produces zero native DRC `shorting_items` and
`tracks_crossing` records for the clock escape. It remains a disposable oracle
because the Y1/R23/C42/C43 branches and U5 C44-C47 island are not yet complete.

The latest bounded sweep (`phase24_clock_position_sweep.py`) improved the
clock-support search to a compact near-west underside candidate, but it still
has one localized B.Cu clock-lane crossing at the U7 escape. It remains an
unpromoted experiment; Phase 24 is still open.

The subsequent side-separated A* clock oracle reached zero clock-specific
crossing/shorting records in native DRC. A follow-on support materialization
was rejected at 240 native violations because the added Y1 passive branches
entered the crystal pad field and the C44--C47 placement overlapped existing
regulator support. The clock oracle is retained as evidence; support networks
must be placed and routed as independently bounded islands.

The complete clock-support topology also passes in the native-orientation
disposable fixture: `PHASE24_CLOCK_MINIMAL_ROT0-drc.rpt` reports zero
unconnected items, shorts, crossings, and footprint errors. This is an
isolation proof, not acreage closure; the remaining work is the rot180
coordinate transplant plus a separate U5 capacitor island.
