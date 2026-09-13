# Foundational Invariant Audit Packet — Fabrication, Thermal, Ground, Mechanical

**Package:** `P24-FOUNDATIONAL-FAB-MECH`  
**Base commit:** `c06876d2bb3c244d29ad04e883a253eefd35c265`  
**Board:** `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`  
**Board SHA-256:** `75d2d37063818093429b44dbe4197005c2f94b23554a34947a68acaaa181bf7c`  
**Boundary:** evidence only; no CAD, rules, queue, final matrices, Library corpus, or authority files edited.

## Result

This packet confirms a high-impact product/input contradiction and several downstream fabrication/mechanical gates. The exact current two-circuit input application basis is not a valid foundational capacity constraint for the user-mandated 300 W sustained / 330 W peak product envelope. The current six-layer declaration is internally consistent as a design basis, while order coupon, integrated impedance/return, thermal, body/access, package overlay, and release evidence remain unproven.

### High-impact findings

- **FAIL `PWR-ENV-001` / `PWR-CU-001`:** the current selected J5/J6 assembly is documented at 8 A per circuit for the standard two-circuit application (16 A screen before derating), while 300 W at 12 V is 25 A before board loads and 330 W is 27.5 A before board loads. The retained 90% worksheet gives 29.8796 A and 32.6574 A including 22.7 W low-voltage loads. The current census also records zero `12V_IN_B`/`FUSED_12V_B` copper/vias.
- **FAIL `FAB-GEO-001`:** retained storage evidence identifies U11 0.15 mm fanout outside the authorized JMS583 XIN/XOUT local escape; normal 0.20 mm geometry applies elsewhere.
- **FAIL `MECH-ENV-001`:** current integrated census has 6 courtyard overlaps, 5 PTH-in-courtyard findings and 16 edge-clearance findings; only 3/131 footprints have 3D models and no complete release package is retained.
- **UNPROVEN:** fabrication coupon/tolerances, actual controlled impedance/return closure, current/thermal capacity on the selected integrated board, regulator thermal margins, exact J1 package overlay/access, cooler/thermal result, and manufacturing release artifacts.

## Invariant register

| ID | Class | Requirement / quantitative basis | Current state | Responsible authority |
|---|---|---|---|---|
| `PWR-ENV-001` | C | PiSXMe Rev A shall support the documented V100/SXM2 300 W sustained operating envelope at the product input, retaining 330 W as the design peak allowance unless a higher authoritative requirement is found. **Basis:** 300 W sustained; 330 W peak allowance; 12 V product input; with board loads and declared conversion margin | **FAIL** | Power Authority with Root product decision recorded |
| `FAB-STACK-001` | B/C | The PCB design basis shall use the selected six-layer JLC06161H-7628 stack: nominal 1.6 mm finished board, 1 oz outer copper, 0.5 oz inner copper, with ordinary through-vias. **Basis:** 6 signal layers; 1.6 mm nominal; 0.035 mm outer copper; 0.0152 mm inner copper model; ordinary through-vias | **PASS** | Fabrication/DFM Authority |
| `FAB-STACK-002` | B/D | Fabrication tolerances and controlled-impedance values shall be verified with the selected fab order and coupon before release. **Basis:** 90 ohm PCIe/USB3/USB2; 100 ohm SATA/1000BASE-T; fab-returned coupon and dielectric/copper tolerances required | **UNPROVEN** | SI Authority / Fabrication Authority |
| `FAB-GEO-001` | D/B | Normal routes shall meet the approved 0.20 mm trace/clearance basis; the authorized 0.10 mm fine escape is limited to the named JMS583 XIN/XOUT region and normal geometry resumes outside it. **Basis:** Normal width and clearance >=0.20 mm; JMS583 XIN/XOUT local width/clearance 0.10 mm only | **FAIL** | Fabrication/DFM Authority with Storage Authority |
| `FAB-VIA-001` | B/D | Ordinary through-vias and connector/package land rules shall remain within the selected fabrication and package contract: no unapproved via-in-pad in SXM2 BGA lands, covered connector-side vias where required, and package-specific drill/annular limits. **Basis:** Current ordinary via basis commonly 0.50/0.30 mm; JLC capability record includes min drill 0.15 mm, min via diameter 0.25 mm; J1 lands 0.584-0.635 mm with >=0.15 mm mask clearance and no vias in lands | **UNPROVEN** | Package/DFM Authority |
| `REF-PLANE-001` | D/B | High-speed pairs shall route on outer layers over the adjacent solid GND reference planes: L1 over L2 and L6 over L5; inner-layer signal routing is excluded by the selected policy. **Basis:** L2=In1.GND; L5=In4.GND; PCIe/USB3/SATA/Ethernet targets 90/100 ohm as above | **UNPROVEN** | SI/Return Authority |
| `PWR-CU-001` | A/B/C/D | The input and protected-rail copper, vias, fuses, connectors, and returns shall be sized for PWR-ENV-001 with explicit current sharing, voltage-drop, temperature-rise, and transient margin. **Basis:** At 12 V, 300 W=25.0 A V100 load before board loads; 330 W=27.5 A before board loads; prior 90% worksheet including 22.7 W low-voltage loads gives 29.8796 A and 32.6574 A total respectively | **FAIL** | Power Authority / Power Integrity Engineer |
| `THERM-REG-001` | A/B/D | Regulator and power-switch junction temperatures shall remain below the selected component operating limits under the signed current, ambient, airflow, and transient budgets. **Basis:** TPSM63606 design screen: 125 C junction limit; prior 50 C ambient/90% screen margins 19.8 C (U3), 50.7 C (U4), 71.0 C (U5); CSD19536KCS -55..175 C operating range and prior theta-JA screen | **UNPROVEN** | Power Authority / Thermal Authority |
| `THERM-MECH-001` | C/E | Rev A cooling shall be module-mounted air or liquid cooling on the V100/SXM2; no undocumented carrier-board cooler/backplate or generic underside keepout may be assumed. **Basis:** V100 module cooling datum retained; carrier-mounted cooler geometry unavailable; underside is available except verified board hardware/access constraints | **UNPROVEN** | Mechanical Authority / Thermal Authority |
| `MECH-ENV-001` | B/C/D | All selected connectors, mounting features, SSD envelope, SXM2 package, and service-access envelopes shall be manufacturable and mutually clear on the integrated board. **Basis:** Board envelope approximately -0.05..300.05 x -0.05..180.05 mm; J1 at (150,90); M.2 2280 envelope bbox 219.95..300.05 x 148.95..171.05 mm; J3 at (220,165); manufacturer J1 perimeter rework recommendation 5.10 mm | **FAIL** | Mechanical/DFM Authority |
| `DFM-REL-001` | D | Phase 24/25 release shall include a reproducible manufacturing package: Gerbers, drills, BOM, CPL, assembly drawings, panel/fab job, models and explicit dispositions. **Basis:** Required package artifacts must exist and hash to one validated integrated PCB SHA | **UNPROVEN** | DFM/Release Authority |
| `SAFE-PROT-001` | A/B/C/D | Input protection shall include independently protected branches, reverse-current/reverse-polarity control, surge/TVS policy, fuse coordination, shutdown/inhibit behavior, and a declared supported source environment. **Basis:** Selected schematic families: 15 A fuse candidates, SMBJ18A candidates, LM74700-Q1 branches; regulated current-limited 12 V cold-plug boundary; no automotive load-dump claim without declared waveform/energy | **UNPROVEN** | Power/Safety Authority |
| `J1-MECH-001` | B | SXM2 J1 package geometry shall follow Amphenol/FCI 74221-101LF manufacturer land, mask, orientation, via and assembly constraints; electrical unknowns remain unknown. **Basis:** 400 contacts; 10 x 40; 1.27 mm pitch; 4.0 mm mated height; 0.584..0.635 mm copper-defined lands; >=0.15 mm mask clearance; no vias in lands; 5.10 mm perimeter rework recommendation | **UNPROVEN** | Package/DFM Authority |
| `HIST-IMPLEMENTATION-001` | E/F | Historical coordinates, generic cooler rectangles, prior trace widths and the 250 W dual-8 A input are implementation choices unless independently supported by A-D evidence. **Basis:** No independent numeric authority; retain only as provenance and candidate history | **NOT_APPLICABLE** | Root Foreman with relevant domain authority |

## Provenance and limits

The private Library was checked first. Relevant indexed briefs are `pisxme-reva-a.md`, `power-envelope-authority-reassessment-20260913.md`, `sxm2-j1-amphenol-rev-w-corpus-20260912.md`, `storage-geometry-u11-u12-20260912.md`, and `power-protection.md`. Repository authority records used include `PHASE13_STACK_RECEIPT.md`, `PHASE14_POWER_ROUTE_RECEIPT.md`, `PHASE15_REGULATOR_LAYOUT_RECEIPT.md`, `PHASE17_MECHANICAL_REOPEN_RECEIPT.md`, `PHASE5_POWER_CALCULATIONS.md`, the current power-envelope authority v1.1, the mechanics/DFM census, and the current acceptance matrix.

No new Researcher commission was necessary for this bounded fabrication/mechanical packet because the indexed corpus already contains the relevant source facts. Missing fab coupon, exact mating assembly, proprietary cooler geometry, complete model set and hardware measurements are recorded as `UNPROVEN`; this packet does not infer them.

## Supersession candidates

- `SUPERSEDED_BY_INVARIANT PWR-ENV-001`: historical 250 W design envelope and any frozen dual-8 A implementation constraint where it conflicts with the user product requirement.
- `SUPERSEDED_BY_INVARIANT THERM-MECH-001`: former generic 150 x 95 mm carrier cooler/backplate reservation as a universal underside constraint.
- `HIST-IMPLEMENTATION-001` remains Class E/F and is not foundational.

## Handoff

Root should include these IDs in `PROJECT_INVARIANTS.{md,json}` and `INVARIANT_COMPLIANCE_MATRIX.{md,json}`. The minimum dependent packages are power architecture correction, SI/fabrication contract closure, and mechanical/DFM closure. No package depending on an unresolved foundational FAIL or required UNPROVEN row should become READY.
