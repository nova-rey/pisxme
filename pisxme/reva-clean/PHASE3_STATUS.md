# Phase 3 status

Current state: `PISXME_REVA_CLEAN_PHASE19_SATA_ROUTING_IN_PROGRESS`;

Phase 19 coordinated storage authoring repair (2026-09-04): corrected the
generic KiCad 10 generator to replace donor C30-C33 footprints and preserve
explicit socket-side SATA net codes across serialization. A fresh U7/J3
coordinated candidate serialized the correct split mapping but measured 262
native DRC violations and was rejected; Phase 19 remains active.

The subsequent coordinate-derived USB3 escape refinement measured 200 native
DRC violations in USB-only V3 testing, with inherited CM5/PCIe corridor
crossings remaining; it was rejected and Phase 19 remains active.

The coordinated V3 corridor refinement measured 206 native DRC violations,
with one J3 auxiliary-pad short and two remaining corridor crossings; it was
rejected and Phase 19 remains active.

The latest synchronized corridor refinement (`PHASE19_LIVE3`) measured 207
native DRC violations with zero shorting items but one remaining USB3 crossing
plus inherited clearance/hole/unconnected debt; it was rejected and Phase 19
remains active.
Phases 17–18 are closed with inherited-baseline qualifications. Phase 18
native netlist and USB3 route proofs pass. Phase 19 storage authority is
closed, but three SATA routing classes are rejected by native DRC for
pad-field, frozen-trunk, or long-corridor interactions. The next experiment
must keep the SATA corridor local to open acreage; no Phase 20+ work has
started.

Created: native root project shell, ten named child-sheet files, isolated
`PiSXMeRevAClean` symbol/footprint tables, architecture contract, interface
ledger, net-class ledger, source-authority manifest, and deterministic
extractors for approved CM5IO and child-sheet contract definitions. Each child
sheet now has native local contract pins wired to its interface labels. The
generated architecture contains no placement or routing and is not yet a
production schematic.

The Phase 3 exit gate is closed. Selected production assets are isolated in
the clean namespace: CM5 is 200 pins to 200 pads and EDAC
`A70-112-331N126` is 18 electrical pins to 18 pads. EDAC shield features are
mechanical/non-plated holes per its manufacturer layout; donor-only shield
pins 19/20 are explicitly removed by the extractor rather than counted as
electrical pads.

Historical closure evidence: KiCad 10.0.5 native ERC reported zero violations
on the root and all ten children before the current Phase 17 CM5IO label
regeneration. The generic authoring defect was an embedded contract
symbol appended outside the child `lib_symbols` section; the corrected path
inserts it inside that section, negates library-pin row Y coordinates, and
generates real root wires to sheet pins. The regression
`validation/phase3/test_native_hierarchy_authoring.py` reproduces the
generation and native ERC check.

The current-source revalidation after the Phase 17 global-MDI-label correction
reports 644 warning-only ERC findings on the root, dominated by pre-existing
off-grid/unconnected scaffold endpoints and library metadata warnings; no
root hierarchy-association error is present. The focused Ethernet hierarchy
authority regression and native netlist mapping pass. This current warning
baseline is recorded in `PHASE17_NATIVE_ROOT_ERC_CURRENT.rpt` and must be
resolved or explicitly reviewed before final Phase 24 closure.

The later `ROOT_HIERARCHY_ASSOCIATION` continuation experiment is also
closed: a native KiCad-authority CM5 promotion now parses the source's two
100-pin units separately, preserves all 200 pin numbers, and passes clean-root
native ERC with zero errors. Regression coverage is in
`validation/phase3/test_phase14_cm5_native_authority.py`; the clean candidate
materializer consumes the resulting J7 netlist component.

Exit evidence is recorded in `validation/phase3/PHASE3_EXIT_RECEIPT.md`.
Phase 4 schematic-only work is complete and is recorded in
`validation/phase3/PHASE4_V100_RECEIPT.md`. Placement and routing remain
prohibited by the approved plan; Phase 5 is the next permitted phase after
the Phase 4 checkpoint. Phase 5 is now closed with explicit
`REV_A_EMPIRICAL_RISK` for routed-board and fabrication confirmation; Phases
6–13 schematic/mechanical contracts audit green, and the approved Phase 14/15
power-routing sequence is complete. Phase 16 PCIe routing is closed with
`PHASE16_PCIE_ROUTING_RECEIPT.md`; its two named CM5 breakout clearances are
explicit Rev-A empirical risk. Phase 17 is now the next permitted phase; no
Phase 18+ routing has started.

Phase 17 continuation update (2026-09-04): native source audit found that
`CORE_CM5` exposed `CM5_POWER` but not `CM5_5V`. The missing child port and
root-to-regulator wire are now present. KiCad netlist export proves U3 pins
5/8/9 and J7 pads 77/79/81/83/85/87 share `/CORE_CM5/CM5_5V`; the Phase 15
authority and Phase 3 netlist regressions pass. A disposable no-copper/PCIe
boundary and coherent F1/U3 placement harness were added. The first
`F1=(100,20), U3=(90,165)` trial remains rejected by native DRC for local
regulator escape geometry and an inherited bridge-capacitor/CM5_PERST
placement conflict. The proven Ethernet island remains electrically closed;
Phase 17 is closed; Phase 18 USB3 routing is next and no Phase 18+ work has
started.

Phase 17 continuation update (2026-09-04, commit `fe8add3`): the official
CM5IO Rev 2 PCB was inspected directly. Its Module1 +5 V fanout uses the same
0.2 x 0.7 mm lands on 0.4 mm pitch and 0.20 mm F.Cu traces used by the clean
J7 authority. The lower U3/F1 candidate now uses that fanout width, an
ordinary 0.50/0.30 mm CM5 power transition, and a dedicated B.Cu corridor.
The best integrated disposable ancestor has zero native `shorting_items` and
zero `tracks_crossing` findings, but still has inherited unconnected acreage
records and Ethernet launch/center-tap mechanical findings. Phase 17 remains
closed; the clean PCB is not promoted. Phase 18 storage authority repair is
the current gate; no USB3 routing or Phase 19+ work has started.

Phase 19 placement wave 2 update (2026-09-04): Phase 18 storage authority and
USB3 routing remain valid, but the first four local SATA corridor variants and
two acreage relocations were rejected by native DRC. The failures are
candidate-introduced U7 escape, frozen CM5/PCIe/reference, connector-body, or
coordinated-USB3 placement interactions; the inherited acreage DRC baseline is
separately identified. Evidence is in
`PHASE19_SATA_PLACEMENT_WAVE2_RECEIPT.md`. Phase 19 remains in progress and
Phase 20+ has not started. A coordinated U7/J3/USB3 storage-island move is the
next authorized experiment.

Phase 19 continuation update (2026-09-04): the coordinated moved-U7 wave and
the smaller J3-only wave were rejected by native KiCad DRC for candidate
endpoint/pad-field geometry. The Phase 18 U7/USB3 ancestor remains the valid
frozen reference. A mid-acreage SATA V3 escape has no new short/crossing
category against its inherited baseline, but cannot close Phase 19 while its
moved U7 leaves USB3 stale. Evidence and the next bounded M.2 endpoint search
are recorded in `PHASE19_BLOCKER_REPORT.md`; Phase 20+ remains gated.

Phase 19 local-placement exhaustion update (2026-09-04): a local underside
M.2 candidate at `(115,125)` with U7 and Phase 18 USB3 preserved produced
244 native DRC violations / 430 unconnected items. The new failures are U7
pad-field conflicts, two SATA B.Cu crossings, and M.2 courtyard/clearance
interactions. Combined with the coordinated, J3-only, outboard, and prior
mid-acreage waves, the remaining repair requires reopening the frozen U7/PCIe
corridor and regenerating an affected high-speed ancestor. Phase 19 was
previously blocked at this boundary, but the user has explicitly reopened the
coherent U7/J3 storage island. A fresh coordinated candidate at U7 `(120,140)`
/ J3 `(145,125)` regenerated USB3 and SATA together and produced 208 native
DRC violations / 426 unconnected items; it is rejected for local USB3 landing
crossings and PERST interaction, while the PCIe ancestor remained unchanged.
Phase 19 is active again; Phase 20+ has not started.

Phase 19 generator-correction update (2026-09-04): restored validated CM5
USB3 source escapes and made moved-U7 landings coordinate-derived. An
above-PCIe candidate at U7 `(140,100)` / J3 `(180,90)` measured 410 native DRC
violations / 426 unconnected, including PCIe interactions and local SATA
shorts, and was rejected. Phase 19 remains active.

Phase 19 coordinated placement sweep update (2026-09-04): open-acreage
candidates at U7/J3 `(140,140)/(170,125)` and related placements were tested
with native KiCad DRC. The best pre-refinement candidate measured 224
violations / 426 unconnected but retained real USB3/PERST and pair crossings.
A coordinate-derived SATA lane refinement measured 229 / 426 and was rejected
for new local SATA lane crossings. No PCIe geometry changed; Phase 19 remains
active.

Phase 19 staged-rail update (2026-09-04): a synchronized U7/J3 candidate with
final USB3 vertical transitions isolated by F.Cu staging hops remained at 229
native DRC violations / 426 unconnected and introduced new SATA/USB3 local
interactions. It was rejected; the next experiment changes island
orientation/relative placement rather than repeating the same rail geometry.

Phase 19 coordinated-base update (2026-09-04): reused the SATA V3 candidate
as a base and regenerated USB3 with synchronized moved-pad coordinates. Native
DRC measured 226 violations / 426 unconnected, with SATA/USB3 crossings and
pad-field interactions; the combination was rejected. Phase 19 remains
active.

Phase 19 orientation sweep update (2026-09-04): rotated storage-island
variants measured 277/415 and 265/408 native DRC violations and were
rejected. Phase 19 remains active; the next repair targets coupled U7
pad-field escape geometry.

Phase 19 native synchronization update (2026-09-04): the coordinated
generator now serializes/reloads after U7/J3 movement before reading pad
coordinates, removing the stale-pad-coordinate defect. Corrected candidates
at U7 `(140,130)` / J3 `(180,115)` measured 227 and 229 native DRC
violations / 426 unconnected across two SATA escape variants; both were
rejected for remaining local crossings. Phase 19 remains active.

Phase 19 USB3 isolation update (2026-09-04): removing SATA tracks from the
corrected U7 `(140,130)` candidate measured 211 native DRC violations / 430
unconnected. Three candidate-introduced shorts remain against regulator
support geometry and one crossing remains against the frozen PCIe B.Cu field;
the next local repair targets those corridors. Phase 19 remains active.

Phase 19 exact-source follow-up (2026-09-04): synchronized direct-F.Cu USB3
detour geometry reduced the isolated USB3 candidate to 202 native DRC
violations / 430 unconnected with no new USB3 shorts/crossings. The complete
east-edge J3 `(240,140)` SATA trial measured 228 / 426 and was rejected for
SATA connector/U7-field interactions. Phase 19 remains active.

Phase 19 orientation-aware update (2026-09-04): implemented the specialist
recommended U7/J3 `(170,140)/(205,120)` at `90°` with a horizontal USB pad-row
escape. Native DRC measured 378 violations / 426 unconnected; rejected for
remaining coordinated SATA/USB3 and local support interactions. Phase 19
remains active.

Phase 19 SATA-V3 reuse update (2026-09-04): disabled SATA regeneration and
reauthored only USB3 on the existing V3 SATA board. Native DRC measured 242
violations / 426 unconnected with four USB3 short/crossing findings against
preserved V3 copper. Simple overlay reuse was rejected; Phase 19 remains
active.

Phase 19 transform-audit update (2026-09-04): serialized U7 `(120,140)` at
`90°` places the USB row at `y=135.5` and SATA row at `x=124.5`, contrary to
the earlier predicted transform. The bottom-approach trial measured 219
USB-only DRC violations / 430 unconnected and was rejected for entering the
U7 body. Future routes use serialized coordinates.

Phase 19 regulator-support update (2026-09-04): translating only C18/C19 to
`(100,145)/(108,145)` removed the three USB3 `BRIDGE_3V3` shorts. The USB3
isolation candidate measured 202 native DRC violations / 430 unconnected,
matching the Phase 18 baseline class apart from one local clearance. Complete
Phase 19 remains gated by SATA launch geometry.

Phase 19 AC-coupling update (2026-09-04): the TI implementation guide
requires four inline <=0402 capacitors, one per SATA conductor, symmetrically
near J3, while the clean storage schematic currently contains none. Evidence
is recorded in `PHASE19_SATA_AC_CAP_RECEIPT.md`; Phase 19 remains active.
