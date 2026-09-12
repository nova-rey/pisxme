# PiSXMe Phase 24 Successor Handoff

## Authority

- Repository: `nova-rey/pisxme-private` (Git remote currently `nova-rey/pisxme.git`)
- Branch: `reva-clean`
- Design checkpoint: `772b342c3107340abcfcc381ac83031d90f8035d`
- Status: `INCOMPLETE / ACTIVE`
- Phase: 24
- Phase 25 has **not** begun.
- Final succession tip: the commit containing this packet after finalization; its full SHA is supplied in the final response. The packet's design authority is the design checkpoint above.

This packet is the current map for a fresh Root Foreman. The append-only `bible.md`, raw reports, and disposable evidence remain historical/supporting evidence, not competing current instructions.

## Purpose

PiSXMe is a CM5 carrier/acres board integrating Ethernet, PCIe to an SXM2/V100 endpoint, dual-mode storage, service USB, and power delivery. Phase 24 is the final integrated validation/repair stage before the Phase 25 freeze; it is not closed.

## Frozen decisions

- Selected `SWAP_ETH_STORAGE` topology-first macro-floorplan; preserve CM5, V100/SXM2, Ethernet, storage, SERVICE, and unrelated regulator anchors.
- Six-layer board and current layer contract; ordinary through-vias; no ordinary signal routing on plane layers.
- PCIe architecture/corridor and Phase 16 result remain closed, with bounded Rev-A empirical risk.
- CM5 USB storage architecture remains dual-mode and storage-local: Path A `CM5 USB -> HD3SS6126 -> TUSB9261/JMS583 path -> HD3SS3412 -> shared M-key socket`; Path B is the preserved RTL9210B alternative. Do not consume native CM5 PCIe or another CM5 USB host port.
- RTL9210B Path-B orientation is closed: top side, 0 degrees, pin 1 southwest, V1517 lineage.
- Accepted USB3 topology/source corridor and CM5 source geometry remain closed.
- JMS583 U11 orientation and authoritative local support cohort (Y10/crystal, VDDREG/LXO and related support) remain closed. The authorized local fine-pitch escape is implementation detail only.
- Ethernet CM5IO-derived electrical topology, ESD, MagJack mapping, and connector support remain closed.
- Power architecture, dual 12-V input/protection concept, regulator choices/topologies, V100/SXM2 placement, and cooler contract remain closed.
- M-key Socket 3 flat 2280 storage concept and SATA/NVMe shared-contact ownership remain closed.

## Passing gates and current authority

| Gate | Result | Evidence / candidate |
|---|---|---|
| Live ten-child hierarchy contract | PASS | `phase24_live_contract_map.py`; fresh Light output: `PASS ... 10 children` |
| Schematic-to-PCB pad parity | PASS, 814 schematic nodes / 1262 PCB pads / 0 mismatches | `PHASE24_FRESH_SOURCE_PCB_PARITY_RECEIPT_20260912.md`; current native XML export |
| U5 actual layered connectivity + negative controls | PASS | `phase24_u5_layer_connectivity_audit.py`; actual pads/tracks/vias, not synthetic edges |
| Isolated dual-mode storage USB3 endpoint audit | PASS, 10/10 | `PHASE24_FRESH_LIGHT_STORAGE_USB3_RECHECK_RECEIPT_20260912.md` |
| Isolated JMS583 support cohort and trace-removal negative control | PASS | `PHASE24_JMS583_FINE_ESCAPE_RECEIPT_20260912.md` |
| Path-B RTL9210B isolated authority/DFM rechecks | PASS in isolation | `PHASE24_PATHB_AUTHORITY_LIGHT_RECHECK_RECEIPT_20260912.md`, `PHASE24_PATHB_DFM_FINAL_RECHECK_RECEIPT_20260912.md` |
| Phase 16 PCIe ancestor | PASS with bounded Rev-A risk | Existing Phase 16 receipts/status; do not reopen without structural evidence |

These are subsystem or parity passes. They do not imply integrated Phase 24 completion.

## Open gates / initial work graph

1. **Integrated PCB DRC/connectivity closure.** Current basis is `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`: fresh Light 10.0.6 reports 440 violations and 265 unconnected items, including 156 track-width, 117 clearance, 80 silk-over-copper, 28 text-height, 16 edge-clearance, 9 dangling tracks, 9 co-located holes, 7 dangling vias, 6 courtyard overlaps, 5 PTH-in-courtyard, 3 silk overlaps, 2 track crossings, and 2 footprint issues. Owner: Supervisor with KiCad/PCB and DFM specialists; Light worker. Close only with native DRC, real connectivity, and no waived required connections.
2. **Power/ground/rail delivery and PDN closure.** POWER_GND, bridge rails, 12-V entry/protection, and JMS local returns still have incomplete delivery/return evidence. Owner: power-integrity specialist; Light worker. Close with current capacity, voltage-drop/transient/thermal and physical return evidence.
3. **JMS583 integrated support/escape closure.** Isolated U11 support passes, but selected local ground-return variants were rejected for native pad-field shorts. Owner: PCB implementation plus DFM validation; Light worker. Close integrated XIN/XOUT/VDDREG/LXO, USB3, rails, returns, native DRC and negative controls.
4. **Integrated storage routing and mode-aware validation.** Isolated USB3 passes; board-wide switched SATA/NVMe paths, inactive-state isolation, M-key mapping, and final routes remain open. Owner: storage/KiCad specialist; Light worker.
5. **Full Path-B RTL9210B integration.** Isolated Path-B is 0/0 in its own candidate, but full-acreage integration, firmware/provenance, and final parity are open. Owner: storage supervisor/Librarian; Light worker for CAD.
6. **Canonical schematic ERC cleanup.** Fresh Light 10.0.6 has 0 errors and 355 total findings, of which 299 are electrical warnings; do not claim clean ERC. Owner: Supervisor split by non-overlapping root-cause clusters: grid, labels/hierarchy, aliases/net names, library integrity. Canonical integration must be serialized.
7. **Footprint/land-pattern/impedance closure.** Two integrated footprint issues remain; critical USB selector footprints are not fully verified, and controlled-impedance evidence is incomplete against the current six-layer fabrication basis. Owner: footprint/library + SI/DFM specialists.
8. **Mechanical, serviceability, and assembly closure.** Courtyards, holes, silkscreen, cable access, connector mating, SSD clearance, and assembly access remain open. Owner: mechanical/DFM specialist.
9. **Reference-set and release readiness.** Final integrated reference audit, bring-up plan, and release receipts are not closed. Owner: hardware auditor/validator.
10. **Source/export hygiene.** The checked-in root `PiSXMe_RevA_Clean.xml` is stale SATA-era output; regenerate native XML for future parity. The current source-of-truth schematic/PCB and current native export must be named explicitly in every new receipt.

A blocked lane must not stop independent lanes. Recommended ownership is one owner per workstream, parallel candidate development, serialized canonical merges, and fresh Light validation of every material candidate.

## ERC state at exact design checkpoint

Fresh KiCad Light 10.0.6 validation was run from design checkpoint `772b342c3107340abcfcc381ac83031d90f8035d` in `validation-phase24-successor-freeze-validation-20260912T153259Z`.

- Native ERC: 0 errors; 355 total findings.
- Electrical warning total: 299.
- Authoritative warning classes: `endpoint_off_grid` 121; `isolated_pin_label` 126; `same_local_global_label` 30; `multiple_net_names` 22.
- Other total findings: `lib_symbol_issues` 53 and `footprint_link_issues` 3.
- Older 300-warning maps and earlier reports are historical snapshots; do not use them as current totals.

## PCB/DRC state

The current integrated repair basis is `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb` at the design checkpoint lineage. Fresh Light 10.0.6 reports 440 DRC violations and 265 unconnected items. No shorting-items class was reported; two track crossings are inherited. The retained original `PHASE24_JMS583_FINE_QFN_ESCAPE.kicad_pcb` is a distinct 612/409 baseline, and `PHASE24_ALL_AUTHORITATIVE_PARTS.kicad_pcb` is a distinct 680/406 candidate. Those numbers must not be compared as if they were one board. Isolated fixture DRC passes are not integrated-board passes.

The fresh parity run emitted KiCad enum-property assertions but completed with 0 mismatches and PASS; preserve that tool distinction rather than hiding it. Host/native historical checks used KiCad 10.0.5; the exact-checkpoint disposable validator used KiCad 10.0.6.

## JMS583 state

The U11/Y10 support cohort is authoritative and isolated support is proven: XIN/XOUT, JMS_VDDREG_5V, LXO, reset/rails, USB3 support, and the local 0.10-mm fine escape pass their focused audit and trace-removal negative control. Ordinary 0.60/0.30-mm through-vias remain preferred; the fine rule is local to the QFN escape. Two local ground-return experiments were rejected because native DRC found one USB_TXP1/JMS_AVDDL short and, in the explicit-via variant, nine U11 pad-field shorts involving LXO/PCIE_CLKREQ_N/JMS_VCCO; see `PHASE24_JMS_LOCAL_GROUND_ESCAPE_REJECT_RECEIPT_20260912.md`. Do not reopen U11 placement or architecture. The remaining task is integrated implementation/return validation, not authority discovery.

## Materially rejected approaches

- Zone-refill-only plane probe: changed 612/409 to 472/409 without removing opens and added findings; rejected.
- Full-acreage BRIDGE_1V1 F.Cu plane: no change from 440/265; rejected.
- JMS local ground zone and explicit pad-to-via returns: native shorts as documented above; rejected; do not reuse.
- NC alias deletion/renaming and M2_3V3 split: changed electrical meaning/netlist; rejected.
- Stale root XML parity: 79 apparent mismatches were export provenance, not design proof; regenerate native XML.
- RTL9210B orientation search and alternate Path-B placements: closed by authority; do not reopen for immature routing.

## Current tooling and operating rules

Root Foreman owns the goal; Supervisor owns substantial workstreams; Librarian supplies persistent precedent/provenance; Unblocker handles one bounded technical escalation; Macro Placement Authority makes binding placement/orientation decisions; specialists implement and validators validate. Use the current registry, not legacy Coordinator-era patterns.

Use `/home/nyx/pisxme-eda-workers/scripts/pisxme-worker`. Allocate one isolated workspace per meaningful workstream from a committed ref. Use `kicad-light` by default, `kicad-heavy` only for genuine GUI needs, and `skidl` for SKiDL generation. Canonical integration is serialized. Material candidates are validated in a fresh Light checkout. Preserve receipts before releasing workers; release idle disposable workers. Never silently copy active uncommitted Path-B state into a worker.

Ordinary bounded engineering choices should be made by the appropriate authority/specialist from project constraints, references, fabrication evidence, and objective validation. Escalate genuine product, architecture, material cost/risk, tooling-installation, or validation-boundary decisions only.

## Historical hazards

**CURRENT AUTHORITY:** this packet, design checkpoint, current authoritative schematic, `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`, and named current receipts.

**HISTORICAL ONLY:** old `PHASE24_STATUS.md` sections below its current override, stale root XML, raw rejected PCB variants, old DRC/ERC counts, disposable worker directories, and earlier candidate names. Raw reports and negative controls are immutable evidence; do not rewrite them. Mark any narrative contradiction as superseded rather than treating it as a TODO.

## First recommended successor workstreams (do not execute as part of this handoff)

1. ERC grid/geometry root-cause owner.
2. ERC label/hierarchy and alias/net-name owners with non-overlapping files.
3. Integrated DRC/unconnected-family classification and JMS583 support-return implementation.
4. Power/ground/rail delivery and DFM review.
5. Storage mode-aware full-board parity/routing and Path-B integration assessment.
6. Independent mechanical/footprint/impedance review.

These are recommendations derived from the final snapshot, not work performed by this succession handoff.
