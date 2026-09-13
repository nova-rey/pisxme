# P24-THERMAL-MECHANICS bounded invariant packet

- **Package:** `P24-THERMAL-MECHANICS`
- **Base:** `c06876d2bb3c244d29ad04e883a253eefd35c265`
- **Scope:** read-only thermal, cooler, mechanical-envelope, assembly/service, fabrication and DFM evidence.
- **Boundary:** no CAD, schematic, rules, library, queue, or Phase 26 work.
- **PCB:** `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`
- **PCB SHA-256:** `75d2d37063818093429b44dbe4197005c2f94b23554a34947a68acaaa181bf7c`
- **Schematic SHA-256:** `6eef63bd3d2b0b9fafc0150d3c34f636ce24a48b2ecbd3d28a5f0bfec167e9f1`
- **Rules SHA-256:** `d5473e6262fdf3b53d5de051626f0ed76dedf7257ba591f79ab8ad55f5b411ec`
- **Checker:** KiCad Light 10.0.6, `pisxme-kicad-light:v1`, image `sha256:37d60e6797eaa14ea393de005b9793af5d9b5e7464aac1e4d58bec1b7803b4a9`.

## Disposition

The package is complete as an evidence packet. It does not close the Phase 24 mechanical, thermal, or DFM acceptance rows. The current board has real mechanical DRC contradictions and fabrication-geometry defects; thermal and release evidence remain unproven. No finding is waived or converted to PASS by absence of a model or measurement.

| Existing invariant / acceptance row | State | Exact current evidence | Required owner and closure evidence |
|---|---|---|---|
| `INV-THERMAL` / `power_current_transient_thermal` | **UNPROVEN** | Prior TI-derived screen at 50 C ambient / 90% efficiency leaves 19.8 C (U3), 50.7 C (U4), and 71.0 C (U5) to a 125 C junction limit using 33.1 C/W. This is a design screen only. Current integrated copper, Branch-B delivery, effective capacitance at DC bias/temperature, ambient/airflow, connector/fuse/harness rise, and transient/load-step behavior are not closed. | Power/PI + Thermal Authority must bind exact loads, ambient/airflow, copper and thermal-via geometry, capacitor derating, protection/harness losses, and transient budget; retain model inputs and independent validation. No fabricated-board or bench thermal PASS is claimed. |
| `THERM-MECH-001` / cooler contract | **UNPROVEN** | Authority `V100_COOLER_BACKPLATE_AUTHORITY.md` closes only the contract that Rev A uses a module-mounted air/liquid cooler and has no authoritative carrier-mounted cooler/backplate or generic underside keepout. No proprietary cooler CAD, carrier thermal result, or module/standoff/cooler assembly proof is retained. | Mechanical/Thermal Authority must provide the exact supported cooler/module/standoff/access envelope and thermal evidence for release. The removed generic 150 x 95 mm carrier reservation is not reinstated. |
| `INV-MECHANICAL` / `mechanical_3d_assembly_service` | **FAIL** | Fresh Light native DRC: 300 violations, 499 unconnected items, 0 shorting items. Mechanical classes: 6 `courtyards_overlap`, 5 `pth_inside_courtyard`, 15 `copper_edge_clearance` (the prior receipt also conservatively referenced 16 edge items across the broader census). Overlaps are C5/C6, C7/C8, J3/MECH_M2_2280, J8/MECH_M2_2280, J7/C14, and L10/U11. J3/J8 M.2 pads intersect the explicit 2280 envelope; envelope must not be shrunk to hide it. | Mechanical/DFM Authority must resolve exact body, mounting, M.2 retention, cable, cooler, and service access on the integrated candidate, then fresh Light native DRC and assembly review must show no required mechanical violations. |
| `J1-MECH-001` / SXM2 package assembly | **UNPROVEN** | J1 identity is closed as Amphenol/FCI `74221-101LF`; manufacturer geometry basis is 400 contacts, 10x40, 1.27 mm pitch, 4.0 mm mated height, 0.584–0.635 mm lands, >=0.15 mm mask clearance, no vias in lands, and 5.10 mm perimeter rework guidance. Exact local overlay, courtyard, hidden-joint SMT access, and exact 3D model are not closed. | Package/DFM Authority must complete pad-by-pad overlay, mask/paste/courtyard, orientation, hidden-joint process and service/rework evidence on final integrated SHA. Electrical unknowns remain unknown. |
| `INV-MECHANICAL` model/assembly subgate | **UNPROVEN** | Native model census is byte-applicable to this PCB: 131 footprints, only 3 with 3D model records, 128 without. Major connectors J1/J2/J3/J4/J5/J6/J8 and most ICs/passives lack exact model records. Existing CM5 model does not close the assembly. | Mechanical/DFM must acquire or dimension-check exact models where needed, and retain assembly drawing/CPL/placement evidence. Generic/donor models cannot be used as exact geometry authority without comparison. |
| `INV-FAB` / `FAB-GEO-001` | **FAIL** | Approved normal basis is >=0.20 mm width/clearance, with 0.10 mm only in the named JMS583 XIN/XOUT local escape. Retained integrated storage evidence records U11 0.15 mm fanout outside that authorized region; DRC has 118 track-width and 138 clearance violations. | Storage + Fabrication/DFM Authority must rework or re-author the affected geometry under the scoped exception and normal net-class rules elsewhere; no global relaxation. |
| `FAB-STACK-001` | **PASS (design basis only)** | PCB declares six signal layers, 1.6 mm nominal thickness, F.Cu/In1.GND/In2.PWR/In3.PROTECTED_12V/In4.GND/B.Cu; selected JLC06161H-7628 authority records 1 oz outer / 0.5 oz inner basis and ordinary through-vias. | Preserve this basis unless a higher invariant forces a new fab decision. Actual fabrication thickness/copper remains release evidence, not this PASS. |
| `FAB-STACK-002` / `INV-IMPEDANCE` | **UNPROVEN** | Targets are 90 ohm PCIe/USB and 100 ohm SATA/Ethernet, but no current order-specific coupon, returned stack tolerance, or integrated return/field-solver closure is retained. | SI/Fabrication Authority must bind stack tolerance, controlled geometry, coupon/order data, and return-path validation against the integrated SHA. |
| `DFM-REL-001` / `dfm` | **UNPROVEN** | No current integrated Gerbers, drills, CPL/position file, assembly drawings, panelization/fab job, or complete model/revision set is retained. Regenerated BOM/exclusion receipts are scoped evidence only; TP1–TP13 and MECH_M2_2280 still need explicit final disposition. | DFM/Release Authority must generate and hash all release artifacts from one validated integrated SHA, with explicit exclusions and assembly sequence. |
| `SAFE-PROT-001` thermal/protection portion | **UNPROVEN** | Exact fuse/TVS/LM74700 families exist, but branch thermal path, fuse I²t, TVS energy, MOSFET SOA, harness/contact derating, ambient, and shutdown/inhibit behavior are not jointly closed. | Power/Safety + Thermal Authority must sign the system protection/thermal budget after input architecture is corrected. |

## Closure boundaries

- The module-mounted cooling contract is usable as a constraint correction: no generic carrier-board cooler/backplate keepout may continue to block acreage. It does not prove thermal sufficiency.
- The current mechanical FAIL is independent of Issue #2's storage/power corridor: it is based on existing placement/envelope geometry and should remain an owned closure package. The L10/U11 overlap is adjacent to blocked storage geometry and may require reconciliation after an authority placement decision.
- The 300/330 W product envelope makes the old dual 8-A input and any power-derived thermal/copper conclusion non-authoritative where contradictory. Thermal calculations must be rerun after Power Authority binds the corrected input topology.
- Do not use prior isolated fixture PASS or a model-count reduction as integrated-board acceptance.

## Source receipts

- `validation-receipts/mechanics-dfm-consolidated-61085fe0-20260913/RECEIPT.md`
- `validation-receipts/mechanics-dfm-consolidated-61085fe0-20260913/mechanics-dfm-census.json`
- `validation-receipts/mechanical-model-census-3a811eac-20260913/mechanical-census.txt`
- `validation-receipts/mechanics-envelope-current-0b65731e-20260913/RECEIPT.md`
- `validation-receipts/dfm-independent-census-20260913/RECEIPT.md`
- `authority-inventory/primary-docs/mechanics/V100_COOLER_BACKPLATE_AUTHORITY.md`
- `authority-inventory/primary-docs/jlc/JLC06161H-7628_IMPEDANCE_BASIS.md`
- `PHASE15_REGULATOR_LAYOUT_RECEIPT.md`
- `PHASE17_MECHANICAL_REOPEN_RECEIPT.md`

## Result to Root

`DONE` for this bounded evidence package. Keep `P24-THERMAL-MECHANICS` as an owned correction/closure package with dependency IDs `INV-THERMAL`, `THERM-MECH-001`, `INV-MECHANICAL`, `J1-MECH-001`, `INV-FAB`, and `DFM-REL-001`. It is independent of immediate speculative CAD routing, but mechanical closure must revalidate against the final integrated candidate after power/placement authority decisions. No user-owned decision is required by this packet.
