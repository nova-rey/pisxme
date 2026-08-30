# PiSXMe Rev A Verified Redesign Work Package

## 1. Verification summary

Audit basis: active branch `codex/usb-a-active-migration`, KiCad 10.0.5. Active-source hashes were captured before review. A disposable copy was opened, zone-refilled, saved by KiCad, and checked without changing the project: 49 DRC violations, 56 unconnected records, 308 schematic/PCB parity records, and 44 ERC violations. Forty-five unconnected records are zone/plane context; eleven are genuine signal discontinuities.

Important corrections:

- “Five GND vias” is literally accurate, although 16 additional GND connector/shell through-hole pads exist.
- The reported blind vias are false positives. All 165 active vias normalize as ordinary through vias.
- FAST-B really uses In3 in the current USB-A design.
- Eleven true signal gaps exist, caused by incorrect ESD symbol/footprint assumptions.
- U16 is a verified P0.
- Additional verified P0s exist in the TPS2553, TUSB320, USB ESD, and LM74700/MOSFET pin maps.
- No contradictory V100 evidence was found; the PCIe concern is empirical, not architectural.

## 2. PCIe design-basis disposition

Retain CM5 → V100 PCIe Gen2 x1 and treat the SXM2 interface as an ordinary PCIe endpoint on a non-standard connector. Absence of private NVIDIA sequencing documentation is not contradictory evidence. Track exact SXM2 pin mapping, common-clock/SSC behavior, reset timing, and V100 power sequencing as `REV_A_EMPIRICAL_RISK`; require external review and first-hardware enumeration evidence, but do not reopen the architecture without new contradictory evidence.

## 3. Corrected severity table

| Finding | Disposition | Priority | Decision |
|---|---|---:|---|
| U16 incomplete regulator | Confirmed | P0 | Rebuild complete TPSM63606 circuit |
| Q1/Q2 source/drain orientation | Confirmed | P0 | Correct LM74700/MOSFET topology |
| TPS2553 U4/U8/U13 pin maps | Confirmed | P0 | Correct symbol/footprint mapping; U13 removed |
| TUSB320 U12 pin map | Confirmed | P0 | Remove under fixed-device SERVICE decision |
| U6/U10 USB3 ESD topology | Confirmed | P0 | Correct DQA mapping and routes |
| U15/U17/U18 package mismatch | Confirmed | P0 | Replace with TPD2EUSB30A DRT |
| Eleven endpoint records | Confirmed true gaps | P0 | Close all signal gaps |
| F1/Q1 cooler intrusion | Confirmed | P0 mechanical | Relocate |
| J5/J6/J7 overlap | Confirmed | P0 mechanical | Re-space |
| U1 | Functional, layout concern | P1 | Keep placement; rebuild local support |
| Signals on In1/In4 | Confirmed | P1 | Make both layers solid GND |
| FAST-B on In3 | Confirmed | P1 | Reroute off In3 |
| USB2 asymmetry | Confirmed | P1 | Reroute all three pairs |
| PCIe transition returns | Confirmed | P1 | Repair PET0/REFCLK transition fields |
| 12 V TVS/bulk/inrush | Partial | P1 | Cold-plug policy; coordinated protection |
| Main 12 V neck-downs | Confirmed | P1 | Widen bulk-current trunks |
| Test/debug access | Confirmed insufficient | P1 | Add rail/control test pads |
| V100 sequencing uncertainty | Confirmed, reduced | REV_A_EMPIRICAL_RISK | External review and first hardware |
| Blind-via count | False positive | — | Normalize to through vias |
| Historical D1/USB-C/mux records | Stale active references | P2 | Purge during regeneration |

## 4. Verified layer/via facts

### GROUND_VIA_VERIFICATION

- Total vias: 165.
- Literal `/GND` vias: 5.
- `/CHASSIS_GND` vias: 0.
- Additional GND connector/shell through-hole pads: 16.
- The five standalone vias are at approximately `(190.8,86.8)`, `(197.8,123)`, `(207.2,139)`, `(205.5,68.5)`, `(197.8,52.2)`.
- None is a close return transition for PCIe PET0 or REFCLK.

The previous “five GND vias” statement was accurate literally, but its functional classification was misleading.

### VIA_CONSTRUCTION_VERIFICATION

The source contains 141 F.Cu–B.Cu records, eight F.Cu–In1, eight F.Cu–In2, and eight F.Cu–In3 records. None is explicitly blind, buried, or microvia. KiCad normalizes all 165 as F.Cu–B.Cu through vias. Use standard through-via fabrication only.

### LAYER_USAGE_VERIFICATION

| Layer | Segments | Length | Actual role |
|---|---:|---:|---|
| F.Cu | 305 | 1484.090 mm | Components, local signals/power, PER0 |
| In1 | 14 | 220.177 mm | Long USB2/control signals inside GND zone |
| In2 | 32 | 680.472 mm | Mixed signals, VPROT, SERVICE, controls |
| In3 | 34 | 623.007 mm | VPROT plus FAST-B USB3 and controls |
| In4 | 45 | 911.025 mm | Long signals inside GND zone |
| B.Cu | 90 | 1266.603 mm | USB3, PET0/REFCLK, power/control |

FAST-A/B USB2 pairs use different inner layers; SERVICE USB2 spans F.Cu/In2/In3/B.Cu. These claims are verified.

## 5. Target layer policy

| Layer | Target role |
|---|---|
| F.Cu | Components, primary breakouts, PCIe/USB, short local signals and regulator loops |
| In1 | Uninterrupted GND only |
| In2 | CM5_5V, USB_5V and 3V3 power zones only |
| In3 | FUSED/VPROT 12 V power zones only |
| In4 | Uninterrupted GND only |
| B.Cu | USB3/PET0/REFCLK trunks and bounded low-speed overflow, referenced to In4 |

All vias remain normal through vias. No blind, buried, microvia, or via-in-pad process is planned.

## 6. Verified schematic fixes

### U16 TPSM63606 — P0

Add 2×10 µF/50 V input capacitors, 2×47 µF/10 V X7R output capacitors, 40.2 kΩ/10.0 kΩ feedback divider, 13.0 kΩ RT resistor, 100 nF VLDOIN bypass, and a 47 kΩ PG pull-up/test point. Correct VCC/NC handling and keep EN/SYNC policy explicit.

### U1 TPSM63606 — P1

The circuit is electrically complete. Keep U1 but place input/output capacitors directly at the module, move the divider adjacent to FB/AGND, and prove worst-case effective output capacitance is at least the TI minimum. Use 2×47 µF/10 V unless DC-bias data proves the existing parts sufficient.

### Q1/Q2 — P0

Connect FUSED_A/B to MOSFET source and VPROT to drain, consistent with LM74700 ANODE/source and CATHODE/drain.

### U4/U8 — P0

Correct TPS2553 DBV pin mapping: 1 IN, 2 GND, 3 EN, 4 FAULT, 5 ILIM, 6 OUT. Add 100 nF input bypass and port-side transient/bulk capacitance.

### USB ESD — P0

U6/U10 use TPD4EUSB30 DQA actual signal pads 1/2/4/5 and GND pads 3/8; pads 6/7/9/10 are NC. U15/U17/U18 use the actual three-pin TPD2EUSB30A DRT implementation.

### SERVICE — fixed recovery UFP

Remove U12 TUSB320, U13 TPS2553 and U14 inverter. Retain J11 as USB2 recovery/device-only port, add 5.1 kΩ Rd resistors from CC1 and CC2 to GND, select device mode explicitly, place 1 µF VBUS-to-GND at the connector, and never source VBUS.

## 7. Proposed floorplan

Use exact manufacturer bodies and mating housings before implementation.

| Block | Approximate target |
|---|---|
| F1/Q1 | `(80,123)` / `(110,123)` below cooler boundary |
| F2/Q2 | `(80,134)` / `(110,134)` second row |
| J5/J6/J7 | Horizontal row near `(174,12)`, `(190,12)`, `(206,12)` |
| U1 | Keep near `(168,128)`; rebuild local field |
| U16 | Lower-right region near `(204,130)` |
| U4/U8 | Immediately beside FAST-A/B VBUS paths |
| U6/U17 | Within 5 mm of FAST-A connector pins |
| U10/U18 | Within 5 mm of FAST-B connector pins |
| SERVICE CC/ESD | Immediately beside J11 |
| Test pads | Board-edge accessible power/control corridors |

F1/Q1 currently intrude approximately 1.5 mm into the cooler keepout. J5/J6/J7 currently overlap at 8 mm pitch; 16 mm pitch is the minimum planning envelope pending housing verification.

## 8. Proposed power redesign

### 12 V input

Rev A is cold-plug bench-only using a regulated, current-limited 12 V source. Per branch:

`J3/J4 → 15 A fuse → post-fuse TVS/CIN → corrected LM74700/MOSFET → VPROT`

Use one branch TVS after each fuse. SMBJ15A-class footprints are the baseline only when the approved PSU maximum is below the TVS stand-off; final selection must keep clamp voltage below downstream absolute maximum. Add 100 nF plus 1 µF local ceramic input capacitance per LM74700 and two 470 µF/25 V low-ESR protected-bus bulk positions plus optional DNP positions. LM74700 EN is not complete forward-path isolation. Both 12 V connectors are mandatory for full V100 operation; single-branch operation is unsupported.

### V100

Preserve distributed SXM2 feeds. Use In3 and broad copper/via arrays, remove duplicate coincident records, widen bulk-current trunks, and validate connector/contact-field temperature and sharing using IPC-2152 and PI analysis.

### CM5 and USB 5 V

Keep separate rails. Complete U1/U16 circuits, use direct pin-adjacent capacitors, and feed each FAST port through corrected TPS2553 switches. Provide at least 120 µF effective port-side bulk per Type-A host path.

## 9. Proposed PCIe changes

- PER0: KEEP exactly; current 74.358/74.389 mm, zero vias, good skew.
- PET0 raw legs and C1/C2: KEEP.
- PET0 after AC capacitors: local transition fix only; colocate P/N transitions and add nearby symmetric GND return vias.
- REFCLK: local transition fix only; symmetric P/N transitions and nearby GND return vias.
- PERST#: clean in place on a permitted signal layer with a short observation branch.

Current PET0 return-via distances are approximately 52–63 mm; REFCLK distances are approximately 35–64 mm. SI, skew, reference continuity and via symmetry must be revalidated.

## 10. Proposed USB3 changes

Reroute FAST-A and FAST-B completely.

- Use F.Cu connector/CM5 breakouts and B.Cu trunks referenced to In4.
- Remove all USB3 routing from In3.
- Target two through vias per conductor: one down near CM5 and one up near the connector/ESD field.
- Add symmetric nearby GND return vias at every pair transition.
- Place ESD within 5 mm of connector pins.
- Route continuously through actual clamp pads; NC pads remain no-connect.
- Target ≤0.5 mm intra-pair mismatch, then validate with final stackup geometry.
- Derive 90 Ω geometry from the selected JLC stackup and solver.

## 11. Proposed USB2 changes

Reroute FAST-A, FAST-B and SERVICE USB2 on F.Cu over solid In1, with zero vias as the target. Keep each P/N pair on one layer/reference, target ≤1 mm mismatch, place corrected DRT ESD parts at the connectors, and avoid switch-node and PCIe transition fields.

## 12. Proposed ground/return redesign

- In1 and In4 become solid GND only.
- Every PCIe/USB3 transition receives symmetric local GND return vias.
- U6/U10 GND pads 3/8 each receive short local return paths.
- U15/U17/U18 each receive an adjacent GND via.
- USB shells tie directly to board GND with bounded connector-edge stitching.
- U1/U16 AGND/PGND and thermal-via patterns follow TI references.
- SXM2 ground pads connect to In1/In4 through distributed arrays aligned with feed corridors.
- Every added via receives a functional category; arbitrary via-count optimization is prohibited.

## 13. Proposed low-speed cleanup

After placement and high-speed work, simplify `PCIE_PWR_EN`, `PERST_N`, `CM5_VBUS_EN`, `FAN_PWM`, `FAN_TACH`, UART, `nRPIBOOT`, regulator PG, and USB switch faults. Use short F.Cu/B.Cu corridors, avoid In1/In4, and keep controls away from high-speed transitions and switch nodes.

## 14. Proposed mechanical fixes

Import fuse, TO-220, USB, fan/pump, J3/J4, J11, CM5 cooler, V100 cooler/backplate and enclosure models. Verify insertion/latch clearance, cable bend radius, fuse access, cooler installation order, UART/recovery access, and assembly sequencing before accepting M2.

## 15. Proposed test/debug additions

Add exposed SMT pads for `TP_RAW12_A/B`, `TP_FUSED12_A/B`, `TP_VPROT12`, `TP_CM5_5V`, `TP_USB_5V`, `TP_3V3`, `TP_CM5_PG`, `TP_USB_PG`, `TP_PERST_N`, `TP_PCIE_PWR_EN`, `TP_USB_A/B_EN`, `TP_USB_A/B_FAULT`, `TP_SERVICE_VBUS`, and several nearby GND pads. Retain J8 UART and TP3/nRPIBOOT. Replace TP1/TP2; do not add high-speed probe stubs.

## 16. Proposed DFM/manufacturing changes

Use standard six-layer through-via fabrication. Apply TI paste-window and thermal-via guidance for TPSM63606. Require X-ray for exposed-pad regulators, dense ESD packages, and inaccessible CM5/SXM2 joints. Review copper balance, warpage, connector mass, stencil apertures, panelization and THT/SMT sequencing with the assembler.

## 17. Preserve list

Preserve the macro outline, mounting holes, SXM2-left/CM5-right zoning, J1/J2 geometry subject to final pin-map check, PCIe Gen2 x1 architecture, PER0, PET0 raw legs/C1/C2, direct USB-A architecture, SERVICE connector location, J3/J4 concept, separate 5 V rails, distributed SXM2 feed, J8/TP3, and the six-layer stack family unless evidence changes.

## 18. Rip-up/rebuild list

Rebuild U16, Q1/Q2 protection, U4/U8, all USB ESD footprints and routes, all FAST-A/B USB3, all USB2 pairs, SERVICE DRP circuitry, all In1/In4 signals, all non-power In2/In3 signals, placement-dependent F1/Q1/F2/Q2 and J5/J6/J7 copper, TP1/TP2, and unjustified no-net keepouts.

## 19. Clean-in-place list

Keep and locally clean PER0, PET0/REFCLK trunks outside transition fields, U1 placement, the SXM2 feed concept, fan/UART/control routes after moves, zones after geometry stabilizes, and silkscreen/readability.

## 20. Dependency graph

```text
Approved PSU/cable envelope + mechanical models
                    |
                    v
M1 schematic/library truth
        |                     |
        v                     v
M2 floorplan          protection values locked
        |                     |
        +----------+----------+
                   v
               M3 power
                   |
                   v
             M4 layer policy
              /             \
             v               v
       M5 PCIe          M6 USB
              \         /
               v       v
             M7 controls/test
                   |
                   v
             M8 planes/returns
                   |
                   v
             M9 integrated validation
                   |
                   v
             M10 review package
```

## 21. Staged execution milestones

### M1 — Schematic and library truth

Modify schematic, symbol/footprint libraries, project rules and `bible.md`. Correct all P0 mappings and circuits, remove SERVICE DRP, and add test-point nets. Freeze PCB geometry. Pass requires zero ERC errors and an approved pin-map table.

### M2 — Mechanical/floorplan

Modify PCB and `bible.md`. Move F1/Q1/F2/Q2, J5/J6/J7, U16, port support and test-pad reservations. Freeze macro outline, J1/J2, PER0, J3/J4 and connector locations. Pass requires full 3D/courtyard clearance.

### M3 — Power implementation

Modify PCB, rules and `bible.md`. Implement branch protection, TVS/CIN/bulk positions, U1/U16, USB switches and V100 distribution. Pass requires polarity audit, current-width worksheet, regulator layout review and preliminary PI/thermal checks.

### M4 — Layer-policy conversion

Evacuate In1/In4, restrict In2/In3 to power, normalize vias, remove stale keepouts and refill zones. Pass requires zero tracks on In1/In4, zero signal tracks on In2/In3, and zero non-through vias.

### M5 — PCIe transitions

Repair PET0 post-cap and REFCLK transition clusters; preserve PER0 and raw PET0. Pass requires skew, reference-plane, return-via and SI review.

### M6 — USB rebuild

Rebuild FAST-A/B USB3, all USB2, corrected ESD and fixed-UFP SERVICE. Pass requires no signal opens, documented impedance/via budgets and CM5IO comparison.

### M7 — Controls and debug

Clean low-speed controls, fan/UART/recovery and add test pads. Pass requires direct topology and no high-speed stubs.

### M8 — Zones/returns

Finalize GND planes, power zones, return vias, ESD returns, SXM2 return arrays and connector stitching. Pass requires a functional via census and no orphan copper.

### M9 — Integrated verification

Run ERC, DRC, parity, SI, PI/current, thermal, mechanical, DFM and 3D review. No generic waiver may hide a true signal defect.

### M10 — RC package

Only after M9, regenerate BOM/CPL/Gerbers/drill/renders/receipts, update `bible.md`, verify hashes/checksums and produce the external-review package. This is not fabrication authorization.

## 22. Validation matrix

| Milestone | Required evidence |
|---|---|
| M1 | ERC, pin-map parity, TI/manufacturer circuit review |
| M2 | Courtyard, 3D, mating-housing and cable review |
| M3 | DRC, IPC-2152/current, PI, regulator and thermal review |
| M4 | Layer/via census, zone and copper-balance review |
| M5 | PCIe skew, SI, return-path and reference review |
| M6 | USB DRC, impedance/skew/via review, CM5IO comparison |
| M7 | Low-speed topology, probe-access and stub review |
| M8 | GND/return walk-through, zone-island and stitching census |
| M9 | Full ERC/DRC/parity/SI/PI/thermal/mechanical/DFM review |
| M10 | Source/output parity, checksums, archive and receipt verification |

## 23. External-review gate

All P0s closed; ERC zero errors; no true DRC signal, short, clearance, hole, keepout or differential defect; every remaining plane-context record individually explained; parity clean except approved connector abstractions; coherent layer policy; complete regulators; deliberate high-speed return paths; collision-free mechanics; documented cold-plug and two-connector policy; sufficient bring-up access; no stale architecture baggage; P1 and empirical risks disclosed.

## 24. Remaining empirical Rev-A risks

V100 pin mapping, common-clock behavior, reset/power sequencing, SXM2 current sharing, TVS/bulk values, regulator effective capacitance/thermal behavior, PCIe/USB compliance, board warpage, and connector temperature remain first-hardware or external-review risks. Bring-up must use current-limited power and staged load.

## 25. Final recommendation

`BOARD_NEEDS_MAJOR_REWORK`

The macro architecture is salvageable. Major rework is required because of verified pin-map/package defects, true USB discontinuities, reversed LM74700/MOSFET orientation, incomplete U16 circuitry, mechanical collisions, and incoherent signal use of ground-reference layers. No design or release file is changed by this plan.

