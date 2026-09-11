# Phase 24 ERC root-cause remediation map — 2026-09-11

Source: fresh native KiCad 10.0.5 report
`PHASE24_CLEAN_SCHEMATIC_ERC_LIVE_RECHECK_20260911_v3.rpt`, SHA-256
`53efcb9244ebe6e77f93d95713f54666f3f133c509ea73f79b4896d05ed9308a`.
Total: 851 warnings, zero errors.

This map groups repeated findings by authoring mechanism. Counts are warning
records, not independent electrical faults. No warning is waived by this map.

| Cluster | Count | Location/pattern | Likely shared cause | Confidence | Proposed repair | Electrical-risk / independence | Expected reduction |
|---|---:|---|---|---|---|---|---:|
| Endpoint grid | 416 | Root and child contract endpoints; repeated 25/60/95/130 mm and 3 mm pitch signatures | Hierarchy scaffold mixes metric coordinates and separately calculated 1.27/2.54 mm coordinates | High | Regenerate root sheets, child labels, contract pins, and wires from one native-grid model | Medium; must preserve explicit live-port mapping; independent of PWR_FLAG repair | Up to 416 |
| Isolated contract labels | 232 | Root sheet; repeated contract labels and live child labels | Live children gained ports after embedded contract symbols were emitted; child/root/instance mapping is stale | High | Explicit per-child mapping: root sheet pin ↔ child label ↔ contract pin ↔ instance pin ↔ wire | High if names/order guessed; independent once mapping is explicit | Up to 232 |
| Dangling contract wires | 147 | Root/child hierarchy wire endpoints | Root and child wire families use independent formulas; root second-row pitch differs from sheet placement | High | Same coherent regeneration as grid/contract repair; do not snap one layer alone | Medium; coupled to grid cluster | Up to 147 |
| Local/global label collisions | 30 | Mostly root, with 5 `CORE_CM5` and 2 `STORAGE` | Same signal names intentionally appear as global and local labels at hierarchy boundary | High | Review ownership; replace redundant same-name boundary labels only when native netlist comparison proves unchanged | High; separate controlled naming repair | Up to 30 |
| Multiple net names | 24 | `STORAGE` child | Shared-storage labels/aliases accumulated across SATA/NVMe support edits | Medium | Build native net-name inventory and resolve only proven aliases; preserve intentional mode/isolation names | High; independent of geometry | Up to 24 |
| Dangling no-connect | 0 | `CORE_CM5` | Closed: 11 stale duplicate records removed after native pin/UUID correlation | High | No further action; regression probe preserves the bounded cleanup | None; closed | 11 |
| Library symbol mismatch | 2 | Root; standard `PWR_FLAG` instances | Embedded standard-library unit serialization differs from current installed library | High | Native unit-compatible repair or retain explicit embedded authority; compare netlist before promotion | Medium; independent of hierarchy geometry | 2 |

## Priority and ownership

1. **Hierarchy contract regeneration** owns the 795 geometry/contract findings
   (416 + 232 + 147). It must be tested as one disposable transformation;
   order-only or coordinate-only edits are rejected by existing receipts.
2. **Label/net-name ownership** owns the 54 naming findings (30 + 24). It
   follows a native netlist comparison and must not rename nets for count
   reduction.
3. **CM5 no-connect authority** is closed: the 11 records were individually
   correlated to stale duplicates and removed; retained NC records remain
   untouched.
4. **Library integrity** owns the two PWR_FLAG mismatches and requires a
   unit-compatible native representation.

## Current discriminator

The next valid experiment is a disposable generator-level regeneration with
an explicit live-port table. Every child port must be represented consistently
in all five places: root sheet pin, child hierarchical label, embedded contract
symbol pin, contract-instance pin UUID, and connecting wire. All coordinates
must derive from one native-grid placement model. The actual circuit symbols,
component geometry, and net names remain unchanged.

Acceptance for promotion is native reopen, full ERC comparison, zero new
hierarchy `pin_not_connected` errors, matching native netlist, and exact
candidate PCB parity. A lower warning count alone is insufficient.

## Non-goals

This map does not alter the canonical schematic, suppress ERC severity, waive
warnings, reopen RTL9210B placement/architecture, or treat the passing
disposable hierarchy fixture as live-source closure.
