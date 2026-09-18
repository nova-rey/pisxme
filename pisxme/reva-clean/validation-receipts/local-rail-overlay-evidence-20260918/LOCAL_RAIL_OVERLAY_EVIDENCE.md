# P24 local regulator overlay and support evidence

- **Package:** `P24-LOCAL-RAIL-OVERLAY-EVIDENCE`
- **Scope:** U3/U4/U5 TPSM63606 local support, capacitance, current/thermal evidence, and vendor-reference geometry.
- **Scope fence:** No protected-bus, J5/J6/J9, Branch-B, source-topology, J1, high-speed-corridor, schematic, footprint, rule, or PCB edit was made.
- **Result:** `EVIDENCE_READY; INTEGRATED_REGULATOR_OVERLAY_REMAINS_OPEN`
- **Assurance:** design evidence only; no fabricated-board measurement or production qualification claim.

## Exact source identity

The package was dispatched with a recorded base of `2d6e3ea4cfd08f587d42be66cc37a77838e5641a`; the dispatch message also named `45f78de5`. The live checkout advanced to `c6d32e28` (`c6d32e28c0d4a...` is abbreviated here only in prose; the full SHA is in the JSON). No CAD source file changed between the recorded base, `45f78de5`, and the live HEAD for this evidence. The exact integrated inputs are:

| Input | SHA-256 |
|---|---|
| `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb` | `75d2d37063818093429b44dbe4197005c2f94b23554a34947a68acaaa181bf7c` |
| `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_dru` | `d5473e6262fdf3b53d5de051626f0ed76dedf7257ba591f79ab8ad55f5b411ec` |
| `PiSXMe_RevA_Clean.kicad_sch` | `6eef63bd3d2b0b9fafc0150d3c34f636ce24a48b2ecbd3d28a5f0bfec167e9f1` |
| `PiSXMe_RevA_Clean.kicad_pro` | `ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356` |
| `REGULATORS.kicad_sch` | `2b0a6adf1469f832548f2016b90c3d5baa501323b9d08efd6c86bc30a3b9992d` |
| `TPSM63606RDLR_RDL0020.kicad_mod` | recorded in `SHA256SUMS` |

The board source is unchanged from the exact-head Light validation receipt
`validation-receipts/si-power-reference-current-head-61085fe0/`, so that
qualified result is reusable within its exact source scope. A fresh host
KiCad 10.0.5 check was also run for cross-checking; it is not substituted for
the qualified Light toolchain.

## Four-state identity

| State | Identity | Result |
|---|---|---|
| Baseline | Live HEAD `c6d32e28`; board SHA above | Selected integrated acreage board; no package CAD delta |
| Producer candidate | None | This package is evidence-only; no isolated CAD producer was created |
| Integration candidate | None | Root retains serialized canonical integration authority |
| Validation result | Host KiCad 10.0.5 plus retained fresh KiCad Light 10.0.6 at the same board SHA | Both report 300 DRC violations and 499 unconnected items; counts are not a closure pass |

## Authority and evidence basis

The binding package/layout sources are:

- `authority-inventory/primary-docs/power/TPSM63606_SUPPORT_AUTHORITY.md` (TI TPSM63606 revision B, SLVSGB4B; local support authority);
- `PHASE15_TI_LAYOUT_OVERLAY.md` and `PHASE15_REGULATOR_LAYOUT_RECEIPT.md`;
- retained TI EVM guide/archive named and hashed in `SHA256SUMS`.

They require VIN1/VIN2 local bypass, VOUT1/VOUT2 local output bypass, a
localized top-side PGND return, a lower-layer VOUT feed, short feedback,
a solid ground reference below the module, four ordinary PGND thermal vias,
and copper adequate for the junction-temperature limit. The TI EVM's 5.85 mm
maximum regulator-to-output-capacitor center distance is a reference sanity
measurement, not a PiSXMe hard threshold. The 1.1 V rail is not a TI 1.0 V
table row; its output-capacitance and switching-frequency choice needs an
explicit engineering calculation.

## Current integrated geometry

All three modules are `TPSM63606RDLR_RDL0020`, 20 pads, top side, 0 degrees.
The support census is generated from the live board and native netlist and is
retained as `support-census.json` and `native-netlist.xml`.

| Module | Origin | VIN support | VOUT support | Closest / farthest support evidence | Current route evidence |
|---|---:|---|---|---|---|
| U3 / CM5_5V | (60,165) | C5/C6 at 8.004–8.246 mm | C7/C8 at 6.103–7.433 mm | C9 at 21.024 mm; R3–R6 at 9.434–30.017 mm | `12V_PROTECTED`: 6 segments/1 via; `CM5_5V`: 37 segments/9 vias |
| U4 / BRIDGE_3V3 | (225,105) | C14/C15 at 147.763–155.724 mm | C16/C17/C19 at 118.207–130.188 mm | C18 at 11.180 mm; controls at 11.180–14.142 mm | `BRIDGE_3V3`: 0 segments/0 vias; FB/RT/PG: no routed copper |
| U5 / BRIDGE_1V1 | (235,105) | C23–C25 at 118.431–132.098 mm | C26–C47 selected output bank at 27.459–105.802 mm | controls at 11.180–18.601 mm | `BRIDGE_1V1`: 0 segments/0 vias; FB/RT/PG: no routed copper |

The serialized board contains POWER_GND zones on F.Cu, In1.Cu, and In4.Cu,
but no POWER_GND via is within 4 mm of any U3/U4/U5 module center. The
board-wide POWER_GND count is 47 segments and 11 vias; this is not proof of
the required local thermal-via arrays or local return copper.

## Schematic support and capacitance

Native netlist values at this exact schematic source are:

| Rail | Input support | Output support | Nominal output sum | 90% nominal screen | TI minimum reference |
|---|---|---|---:|---:|---:|
| CM5_5V / U3 | C5/C6 = 2 × 10 uF, 50 V | C7/C8 = 2 × 22 uF | 44 uF | 39.6 uF | 30 uF effective at 5 V |
| BRIDGE_3V3 / U4 | C14/C15 = 2 × 10 uF, 50 V | C16/C17/C19 = 3 × 22 uF | 66 uF | 59.4 uF | 50 uF effective at 3.3 V |
| BRIDGE_1V1 / U5 | C23/C25 = 2 × 10 uF, 50 V; C24 = 1 uF | 16 × 22 uF (C26–C29, C34–C41, C44–C47) | 352 uF | 316.8 uF | no direct TI 1.1 V row; 1.0 V row is 300 uF and cannot be silently interpolated |

The 90% figures are a retained design screen, not a guaranteed operating-point
capacitance. TDK DC-bias and temperature derating, current demand, load-step
response, and board-specific thermal behavior remain open evidence.

## Acceptance disposition

This packet closes the independent evidence census and identifies the exact
integrated work still required. It does **not** close the Phase 24
`regulator_reference_overlays`, power-rail, thermal, or native integrated
connectivity rows.

Required next action for Root's queue is one authority-bound producer/integration
package after the protected-bus dependency resolves, or a narrow placement/
corridor authority decision if the current U4/U5 geometry is retained. That
package must preserve the existing six-layer roles and HPQ protected-bus fence,
add/verify local VIN/VOUT/FB/RT/PG corridors, local PGND copper, and four
PGND thermal vias per module, then run fresh KiCad Light validation at the
integrated SHA. No arbitrary capacitor deletion, global rule relaxation,
synthetic connectivity, or use of a subsystem pass as integrated closure is
permitted.

The current DRC census is retained only to bind the check:

- qualified KiCad Light 10.0.6: 300 violations / 499 unconnected;
- host KiCad 10.0.5 cross-check: 300 violations / 499 unconnected;
- violation classes: 138 clearance, 118 track-width, 15 copper-edge-clearance,
  9 dangling-track, 7 dangling-via, 6 courtyard-overlap, 5 PTH-inside-
  courtyard, and 2 crossings.

No fabricated-hardware, vendor-approval, production-qualification, or thermal
measurement claim is made.
