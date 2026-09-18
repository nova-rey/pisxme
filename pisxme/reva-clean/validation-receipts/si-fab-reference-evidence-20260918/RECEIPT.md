# P24-SI-FAB-REFERENCE-EVIDENCE receipt

- **Package:** `P24-SI-FAB-REFERENCE-EVIDENCE`
- **Scope:** independent stack/layer, impedance/tolerance, return-reference, and non-protected interface evidence.
- **Base state:** `2d6e3ea4cfd08f587d42be66cc37a77838e5641a`
- **Audited current HEAD:** `8cd2ff8aa75636bdef44ef87285853bcdabe21bc`
- **Selected PCB:** `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`
- **PCB SHA-256:** `75d2d37063818093429b44dbe4197005c2f94b23554a34947a68acaaa181bf7c`
- **Project:** `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pro`
- **Rules:** `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_dru`
- **Schematic:** `PiSXMe_RevA_Clean.kicad_sch`
- **Qualified tool:** `pisxme-kicad-light:v1`, KiCad `10.0.6`, image digest `sha256:37d60e6797eaa14ea393de005b9793af5d9b5e7464aac1e4d58bec1b7803b4a9`

## Work performed

This was a read-only evidence and validation pass. No schematic, PCB, rule,
project, protected-bus, or global geometry edits were made. The current board
artifact is unchanged from the protected-bus baseline; the HEAD delta is queue
and campaign dispatch documentation.

A fresh detached Light checkout at the exact current HEAD ran native DRC with
all severities. The retained raw report is `current-head-drc.json`:

- 300 DRC violations;
- 499 unconnected items;
- five checker classes remain ignored in the report metadata; these are not
  accepted waivers;
- no schematic-parity items were emitted by this DRC invocation.

`current-head-geometry.json` is the read-only serialized geometry census. It
records 131 footprints, 329 segments, 90 vias, and 3 zones. `audit-metrics.json`
contains the reproducible derived metrics and status for every scoped row.

## Findings by acceptance requirement

| Requirement | Result | Evidence and disposition |
|---|---|---|
| `INV-STACKUP` / six-layer roles | **PASS — design basis only** | F.Cu/B.Cu carry signal segments; In1=GND reference, In2=PWR, In3=protected 12 V, In4=GND. The board has 216 F.Cu and 113 B.Cu segments and no serialized signal segments on inner layers. This does not prove an ordered/fabricated stack. |
| Released differential geometry | **PARTIAL / OPEN** | PCIe and CM5 USB3 nets use the released 0.13208 mm width. USB1/storage and service USB2 paths retain 0.15/0.20 mm or 0.20 mm geometry; JMS USB3 also remains 0.20 mm. Width matching is only a design proxy, not an impedance result. |
| `INV-IMPEDANCE` / tolerance | **UNPROVEN** | 90-ohm PCIe/USB3/USB2 and 100-ohm SATA/Ethernet targets and JLC06161H-7628 calculator inputs are retained as design basis. No order-specific stack tolerance, coupon, field-solver result, or hardware measurement is present. |
| `SI-FAB-REF-001` / return reference | **UNPROVEN** | POWER_GND zones are serialized on F.Cu, In1.Cu, and In4.Cu; 47 POWER_GND segments and 11 POWER_GND vias are present, with no inner-layer signal segments. Native refill, every transition, and local return-via continuity remain to be checked on the final integrated candidate. |
| `SI-FAB-VIA-001` | **UNPROVEN** | All 90 vias serialize F.Cu-to-B.Cu through-vias with 0.30 mm drill and 0.50/0.55/0.60 mm finished sizes. Package overlays, annular/clearance limits, and final fab order reconciliation remain open. |
| `INV-FAB` / normal geometry and DFM | **FAIL / OPEN** | Current native DRC reports 300 violations and 499 unconnected items. The retained U11 0.15 mm geometry outside the authorized JMS583 XIN/XOUT exception remains a real contradiction. No global relaxation was applied. |
| `layers_routes_impedance_return` | **OPEN** | This packet closes the independent design-basis census only. Final acceptance requires one integrated post-protected-bus candidate with fresh native refill, DRC/connectivity, route/netclass, return-transition, and order/coupon evidence. |

## Rule and protected-region boundary

The selected `.kicad_dru` contains one net-scoped 0.10 mm rule for XIN/XOUT.
Existing rule-context evidence shows the current XIN/XOUT geometry lies within
its localized board envelope, but the rule itself is not a geometric region
predicate. Normal 0.20 mm rules remain applicable to other nets. This packet
makes no rule-context correction and grants no exception outside the named
JMS583 escape.

The HPQ protected-bus region is fenced. No source/protection/J1 copper, power
plane, current path, or protected-bus placement is included in this result.
The next integrated validation must re-run all affected SI/fab checks after
that candidate is reconciled to current HEAD.

## Authority/provenance basis

- `PHASE13_STACK_RECEIPT.md` — selected six-layer and released differential
  starting geometry basis.
- `authority-inventory/primary-docs/jlc/JLC06161H-7628_IMPEDANCE_INPUTS.md` —
  calculator inputs and hash recorded in the foundational SI/Fab packet.
- `authority-inventory/primary-docs/jlc/JLC06161H-7628-stack-api-20260830.json` —
  stack response recorded in the foundational SI/Fab packet.
- `validation-receipts/foundational-invariants/si-fab-20260913/SI_FAB_INVARIANT_PACKET.md`
  and `.json` — scoped invariant definitions and acceptance boundaries.
- `validation-receipts/rules-context-fresh-acacc3a9-20260913/RECEIPT.md` —
  native rule loading and XIN/XOUT scope probe.
- `validation-receipts/si-reference-independent-3b70587d-20260913/RECEIPT.md`
  and `si-layer-census-current-head-20260913/RECEIPT.md` — prior scoped route
  census, retained as supporting evidence only.

No impedance measurement, fabricated-board result, vendor fabrication approval,
or production qualification is claimed.

## Result to Root

**CANDIDATE_READY (scoped evidence packet).** The independent stack/layer and
route metrics are reproducible at current HEAD. The acceptance row remains
OPEN because controlled impedance, return continuity, fabrication compliance,
and integrated DRC/connectivity are not closed. Root must carry this packet
through normal queue validation and re-run the listed checks on the final
integrated protected-bus candidate before marking the package or acceptance
row DONE.
