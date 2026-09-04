# Phase 3 status

Current state: `PISXME_REVA_CLEAN_PHASE19_SATA_ROUTING_IN_PROGRESS`;
Phases 17–18 are closed with inherited-baseline qualifications. Phase 18
native netlist and USB3 route proofs pass. Phase 19 storage authority is
closed, but two SATA routing candidates are rejected by native DRC for
pad-field and frozen-PCIe-trunk interactions. The next experiment moves the
M.2 corridor beyond the PCIe trunk endpoint; no Phase 20+ work has started.

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
