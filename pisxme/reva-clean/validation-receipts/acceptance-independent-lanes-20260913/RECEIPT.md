# Phase 24 independent acceptance-lane census

- Work package: `acceptance_independent_lanes`
- Owner: `/root/acceptance_independent_lanes`
- Job: `AIL-20260913-01`
- Candidate/source state: Git `acdc52c47d520b053e791b030945d6fa95d5348a`
- PCB SHA-256: `75d2d37063818093429b44dbe4197005c2f94b23554a34947a68acaaa181bf7c`
- Toolchain context: qualified KiCad 10.0.6 Light image `sha256:37d60e6797eaa14ea393de005b9793af5d9b5e7464aac1e4d58bec1b7803b4a9`; this receipt is a read-only evidence census using already retained native outputs.

This receipt keeps independent acceptance work moving while MPA owns the blocked
storage/power placement/corridor problem. It does not modify the schematic or
PCB and does not close any acceptance row.

## Current source/ERC lane

Fresh retained ERC JSON `validation-receipts/erc-context-737b8191-20260913/erc.json`
(SHA-256 `ecd982cbf0e02d14bf5209cbb23163d99843e1a402faa864444f181dba1f372a`)
contains 293 findings: 126 `isolated_pin_label`, 121 `endpoint_off_grid`, 24
`same_local_global_label`, and 22 `multiple_net_names`. It has no reported errors,
but the acceptance requirement is zero findings and remains OPEN.

The lane is independently actionable through one bounded source producer based on
the retained root-cause map: regenerate the hierarchy contract from one explicit
port/grid model, then compare native netlist, ERC, and PCB parity before any
promotion. Existing historical probes are not closure evidence. The producer must
return base SHA, changed source scope, native ERC/netlist output, and parity; it
must not touch V100/PCB geometry or rename nets to reduce counts.

## Current DFM/mechanical lane

Fresh retained integrated DRC JSON
`validation-receipts/gateb-integrated-validation-47364e6d-20260913/drc.json`
(SHA-256 `6debb3d31c1537268cf14eb09faf8c13aa85420094a39effc482dc07fe48307a`)
contains 300 violations, 499 unconnected items, and zero `shorting_items`. The
mechanical and edge findings are classified as follows:

| Finding family | Current evidence | Lane disposition |
|---|---|---|
| `courtyards_overlap`: C5/C6, C7/C8, L10/U11 | six overlap records total; C5/C6 and L10/U11 are power/storage cohorts | `WAITING_ON MPA` / power owner; no local edit |
| `courtyards_overlap` and `pth_inside_courtyard`: J3/J8 vs `MECH_M2_2280` | M-key and mode-header contacts intersect the explicit M.2 envelope | `WAITING_ON` storage/mechanical authority; envelope must not be shrunk |
| `courtyards_overlap`: J7/C14 | CM5 and power support geometry at `(35,130)` / `(70,120)` | `WAITING_ON` power/mechanical authority; verify underside/access before disposition |
| `copper_edge_clearance`: CM5_5V at bottom edge | power return/trunk geometry | `WAITING_ON` power/MPA |
| `copper_edge_clearance`: C48-C51 pads at y=180 | four Ethernet center-tap capacitor pads on board edge | independently reviewable, but requires Ethernet/DFM authority before any movement |
| `tracks_crossing`: JMS_AVDDL vs USB_RXN1 | two B.Cu crossings at the U11/USB corridor | `WAITING_ON` storage/SI corridor authority; not an independent cleanup |
| `track_dangling` / `via_dangling` | remaining items include power (`CM5_5V`, `PG_CM5_5V`, `RT_CM5_5V`, `STORAGE_3V3`) and PCIe/USB endpoints | classify only after MPA and route integration; no deletion of required copper |

The old DFM receipt at `validation-receipts/dfm-mechanics-19a/RECEIPT.json` is
not current (candidate `19a1390a`, 433 violations); it remains historical. The
BOM receipt at `validation-receipts/bom-integrated-ee0ee5db/` is also from an
earlier candidate and records 117 schematic references versus 131 PCB references,
with TP1-TP13 and `MECH_M2_2280` requiring explicit disposition. A fresh BOM and
assembly/3D-model manifest belong in the post-MPA material-candidate gate.

## SI/reference, firmware, and hostile-review lanes

- The fresh USB3 geometry census at
  `validation-receipts/si-layer-census-current-head-20260913/` is reusable scoped
  evidence for lengths, layers, vias, and skew proxies. It does not establish
  controlled impedance or return-path closure; those remain independently
  actionable documentation/evidence tasks.
- The regulator reference-overlay packet and the power audit are retained, but
  U4/U5 physical support and FB/RT/PG routes are in the power/placement
  dependency subtree. No overlay disposition is promoted from the packet alone.
- Path-A component/library authority is retained in private Library commit
  `ae9132d6072f1557a709f47c542fe3c6d9baac38`; RTL9210B Path B remains isolated
  and unpromoted. Release/provisioning, authorized supply, and firmware/hash
  evidence remain OPEN and can be pursued by Librarian without CAD edits.
- The hostile review at
  `validation-receipts/hostile-review-cdd5a381-20260913/RECEIPT.md` remains a
  failed/open review of an earlier integrated state. Prepare the review command
  and checklist now; rerun only after MPA's material integrated candidate is
  validated.

## Workstream ledger

| Owner/job | Scope | Dependency | State | Next action |
|---|---|---|---|---|
| `/root/acceptance_independent_lanes` / `AIL-20260913-01` | ERC source root causes and exact acceptance classification | current exact source/PCB baseline | ACTIVE, read-only census complete | Root dispatches one isolated bounded hierarchy-source producer when capacity permits |
| `/root/acceptance_independent_lanes` / `AIL-20260913-02` | Ethernet C48-C51 edge-clearance disposition | Ethernet/DFM authority and current integrated candidate | WAITING_ON authority; no safe edit inferred | request bounded authority review; preserve pads/edge contract |
| Librarian / existing Library service | firmware/provenance and SI/reference evidence | private Library corpus; external research only for named gaps | ACTIVE independently | return provenance/index packet; no public reference-copying |
| Root / MPA storage-power owner | C5-C8, L10/U11, J3/J8 envelope, crossings and power dangling items | binding placement/corridor decision and isolated implementation | BLOCKED DEPENDENCY, not campaign blocker | integrate MPA producer then fresh Light validation |
| Root / final hostile validator | integrated hostile review | material candidate after MPA and source/DFM changes | WAITING | rerun one fresh exact-head review at final closure gate |

No contractor was dispatched from this context: the read-only census and evidence
classification were bounded enough to perform directly, and no overlapping CAD
workspace is justified before MPA integration.

## Acceptance classification

- **Dependent on blocked geometry:** native DRC, physical opens/shorts, storage
  mode behavior, physical power/current/transient/thermal, regulator overlays,
  most DFM/mechanics, and final hostile review.
- **Independently actionable:** bounded ERC/source producer; surplus-pad and
  exclusion/alias coverage audit; SI/reference/return evidence; firmware and
  procurement provenance acquisition; Ethernet edge-clearance authority review;
  fresh BOM/model/assembly manifest preparation.
- **Closed scoped evidence only:** native netlist generation, expected-pad
  ownership (`814` nodes / `1262` pads / zero expected mismatches), J1 package
  identity, and isolated RTL9210B Path-B evidence. None of these closes the
  integrated acceptance rows.

Recommended next action is one source-only ERC producer and parallel Librarian
provenance/SI packets while MPA's single placement/corridor implementation is
validated. Do not start another speculative storage/power routing variant.
