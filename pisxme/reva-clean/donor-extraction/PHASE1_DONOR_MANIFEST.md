# PiSXMe Rev A clean rebuild — Phase 1 donor manifest

Status: `PHASE_1_DONOR_EXTRACTION_COMPLETE`

This is an extraction manifest, not a production schematic or PCB. The legacy
design under `pisxme/PiSXMe.*`, its `PiSXMe:` libraries, experiments, and
validation outputs remain donor/reference material only. No donor PCB geometry
or routed copper is promoted.

## Classification rules

- `KEEP`: fact or asset eligible for independent revalidation and transplant.
- `FIX_WHILE_TRANSPLANTING`: useful donor intent, but the source asset or
  record must be rebuilt/rechecked in the `PiSXMeRevAClean` namespace.
- `DISCARD`: prohibited architecture, stale geometry, proxy connectivity, or
  evidence that cannot support the clean design.

## PCIe / V100 / SXM2

| Classification | Donor item | Evidence and transplant boundary |
|---|---|---|
| KEEP | PER0 lane-0 raw topology; PET0 raw legs and transmitter-side AC capacitors; REFCLK; PERST architecture | `design/PCIE_X1_PROVENANCE.md`, `design/BOARD_ARCHITECTURE_V1.md`, and `audit/ARCHITECTURE_MINIMALITY_AUDIT.md`; retain only logical/topological intent and re-author connectivity. |
| KEEP | SXM2 connector identity and 400-position land-pattern requirement | `design/CRITICAL_FOOTPRINT_AUDIT_FINAL.md`; independently revalidate the Amphenol drawing, orientation, mask/paste and courtyard before use. |
| KEEP | Distributed V100 power concept and dual high-current input concept | `design/POWER_ARCHITECTURE_V1.md`; recalculate rails, current sharing and protection in Phase 5. |
| FIX_WHILE_TRANSPLANTING | `SXM2_74221-101LF` footprint and all SXM2 pin labels | `design/CRITICAL_FOOTPRINT_AUDIT_V2.md` explicitly leaves exact land pattern and K18/K19 auxiliary classification unresolved. Copy only after pin/pad and manufacturer-overlay closure. |
| FIX_WHILE_TRANSPLANTING | REFCLK/PERST/CLKREQ endpoint policy | Existing contract is a Rev-A hypothesis; preserve `REV_A_EMPIRICAL_RISK` for undocumented V100 endpoint behavior. |
| DISCARD | Any routed commercial/reverse-engineered PCB geometry, bend, fanout, via row or placement | Forbidden by `design/PCIE_X1_PROVENANCE.md`; references may supply logical observations only. |
| DISCARD | NVLink/x16 lanes, PCIe switch/redriver baggage, card-edge assumptions | Conflicts with the approved CM5 Gen2 x1 interface contract. |

## Mechanics and cooling

| Classification | Donor item | Evidence and transplant boundary |
|---|---|---|
| KEEP | Cooler-owned and underside backplate reservation as a contract | `design/BOARD_ZONES_AND_KEEPOUTS.md`; retain as a model/keepout requirement, not proof of fit for an unnamed cooler. |
| KEEP | V100/SXM2 mounting and assembly-order constraints | `mechanical/usability/ASSEMBLY_SERVICE_SEQUENCE.md`, `cleanup/human-routing/J5_J6_J7_MECHANICAL_ENVELOPE.md`; revalidate against exact models in Phase 9. |
| FIX_WHILE_TRANSPLANTING | `V100_MODULE_ENVELOPE.kicad_mod` and rectangular mechanical annotations | Study-only donor geometry; replace with exact STEP/outline/retention authorities before placement signoff. |
| FIX_WHILE_TRANSPLANTING | Provisional 220 × 140 mm outline and adjacent CM5 placement | `placement/HOSTILE_PLACEMENT_REVIEW.md` calls it provisional; Phase 10/11 must derive the clean acreage from envelopes. |
| DISCARD | Legacy 240 × 140 mm outline and any density-driven outline constraint | Explicitly rejected by the approved plan. |

## CM5 and conventional I/O

| Classification | Donor item | Evidence and transplant boundary |
|---|---|---|
| KEEP | CM5 PCIe Gen2 x1, native Gigabit Ethernet, one USB3 storage path, USB2 SERVICE, controls and power | `design/BOARD_ARCHITECTURE_V1.md`, `design/CM5_USB_ARCHITECTURE.md`, and official CM5/CM5IO references indexed in `references/REFERENCE_INDEX.md`. |
| KEEP | Official CM5IO Ethernet pair mapping, MagJack center-tap/LED/shield topology, and CM5 pin authority | `references/cm5/official-cm5io-rev2/` and `audit/CM5IO_USB3_IMPLEMENTATION.md`; transplant logical/pin facts, not board geometry. |
| KEEP | CM5 connector identity and two-row 0.4 mm interface requirement | `design/CRITICAL_FOOTPRINT_AUDIT_FINAL.md`; exact vendor land pattern and body model remain a Phase 3/9 validation item. |
| FIX_WHILE_TRANSPLANTING | CM5 connector and body footprints | Existing records disagree in confidence across the V2/final audits; independently validate pad map, rotation, courtyard and STEP alignment. |
| FIX_WHILE_TRANSPLANTING | Ethernet ESD, MagJack and LED implementation | Use official CM5IO source mapping, then revalidate the selected connector/ESD parts and local library assets. |
| DISCARD | Dual external USB3, USB hub, USB Ethernet, 2.5GbE, unused PCIe lanes, NVLink, PCIe switch | Explicitly excluded by the approved interface contract. |
| DISCARD | CM5IO board placement/routing copied as geometry | The CM5IO archive is authority for electrical observations, not a layout template for the clean board. |

## Storage and SERVICE

| Classification | Donor item | Evidence and transplant boundary |
|---|---|---|
| KEEP | CM5 USB3 → selected bridge → SATA → B-key M.2 SATA-only path | Approved plan and `references/REFERENCE_INDEX.md`; bridge selection remains open until Phase 2 closes documentation, firmware/UAS, package and procurement. |
| FIX_WHILE_TRANSPLANTING | JMS578/M.2 topology, clock, reset and configuration records | `references/jms578-ee-world/` and `references/jms578-misaka/` are one secondary lineage; verify against JMicron authority before selection. Evaluate ASM1153E under the same gate if JMS578 fails. |
| KEEP | SERVICE USB2 UFP contract: DP/DM, connector ESD, two 5.1 kΩ Rd resistors, VBUS sense/test, no VBUS source | Approved plan; the older dual-role implementation is not authoritative for the clean UFP-only contract. |
| DISCARD | Legacy FAST-A/FAST-B external SuperSpeed ports and proxy USB/SATA nets | Prior disposable trials were rejected and cannot supply clean connectivity authority. |
| DISCARD | M-key/NVMe assumption or 12 V at M.2 | Contradicts the SATA-only and 3.3 V storage contract. |

## Power, protection and regulators

| Classification | Donor item | Evidence and transplant boundary |
|---|---|---|
| KEEP | Two mandatory regulated/current-limited 12 V inputs, protected merge and distributed V100 feed | `design/POWER_ARCHITECTURE_V1.md`; cold-plug-only is a locked Rev-A assumption. |
| KEEP | LM74700 reverse/reverse-current protection concept, fuse/TVS coordination, TPSM63606 regulator family | `design/POWER_ARCHITECTURE_V1.md`, `design/CM5_BUCK_FINAL_AUDIT.md`, and indexed TI datasheets; rebuild calculations and vendor-layout islands in Phase 5/15. |
| FIX_WHILE_TRANSPLANTING | Existing regulator, MOSFET, fuse and protection footprints | `design/CRITICAL_FOOTPRINT_AUDIT_V2.md` identifies package, thermal, or exact-land-pattern follow-up; copy only after individual pad/model audit. |
| FIX_WHILE_TRANSPLANTING | PG/fault/enable sequencing and V100 power-on behavior | Electrical intent exists, but undocumented V100 endpoint timing remains empirical and must not be presented as proven. |
| DISCARD | Legacy switch-node routes, arbitrary plane-layer signals, indiscriminate high-current via fields | Violates the approved layer/via contract or the `design/HIGH_SPEED_VIA_POLICY.md`. |

## Footprints and rules

| Classification | Donor item | Evidence and transplant boundary |
|---|---|---|
| KEEP | Manufacturer-derived package research and source links | `design/CRITICAL_FOOTPRINT_AUDIT_FINAL.md` and `references/REFERENCE_INDEX.md`; preserve source provenance per asset. |
| FIX_WHILE_TRANSPLANTING | All 30 recovered custom footprint files | Inventory is complete, but none may retain the `PiSXMe` identifier in the clean project. Revalidate each used asset's pads, pin map, courtyard, model and provenance under `PiSXMeRevAClean`. |
| FIX_WHILE_TRANSPLANTING | Six-layer ordinary-through-via rule basis | `design/HIGH_SPEED_VIA_POLICY.md` and `manufacturing/FAB_STACKUP_COMPARISON.md`; refresh current JLC stackup and solve geometry in Phase 13. |
| DISCARD | Legacy `PiSXMe:` library identifiers and machine-local table paths | Forbidden in clean schematic/PCB by the approved plan. |
| DISCARD | Historical DRC/ERC receipts treated as clean-design signoff | They are donor baselines only; clean native ERC/DRC must be generated from the clean source. |

## Explicit architecture disposition

The clean implementation starts from a new project and uses one connectivity
authority per block. Donor artifacts supply bounded observations and provenance
only. No donor PCB, routed trace, proxy net, or legacy library identifier is
eligible for direct promotion.

