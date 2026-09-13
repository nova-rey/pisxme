# Phase 24 SI, power-return, and regulator-reference package

Date: 2026-09-13  
Work package: `P24-SI-POWER-REFERENCE`  
Status: `CANDIDATE_EVIDENCE_READY; ACCEPTANCE_ROWS_REMAIN_OPEN`

This package refreshes the independent SI/layer/return and regulator overlay
evidence at the exact current documentation head. It makes no schematic, PCB,
library, rules, configuration, or zone edits. Storage/Branch-B route geometry,
the 15 Path-A opens, and the Branch-B power endpoints remain owned by Hard
Problem Queue Issue #2 and are excluded from this package.

## Four-state identity

| State | Identity | Result |
|---|---|---|
| Baseline | Canonical `reva-clean` head `61085fe076d83e356900ce8703e773308fb2397f`; selected PCB SHA-256 `75d2d37063818093429b44dbe4197005c2f94b23554a34947a68acaaa181bf7c` | Current integrated acreage input; no CAD delta |
| Producer candidate | None | No placement or route candidate produced |
| Integration candidate | None | Root controls serialized canonical integration |
| Validation result | Fresh detached `pisxme-kicad-light:v1` checkout from current HEAD | KiCad `10.0.6`; native DRC 300 violations / 499 unconnected items; DRC exit code 5 |

The current source files bound by this package are:

| Input | SHA-256 |
|---|---|
| `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb` | `75d2d37063818093429b44dbe4197005c2f94b23554a34947a68acaaa181bf7c` |
| `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_dru` | `d5473e6262fdf3b53d5de051626f0ed76dedf7257ba591f79ab8ad55f5b411ec` |
| `PiSXMe_RevA_Clean.kicad_sch` | `6eef63bd3d2b0b9fafc0150d3c34f636ce24a48b2ecbd3d28a5f0bfec167e9f1` |
| `PiSXMe_RevA_Clean.kicad_pro` | `ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356` |

## Librarian and authority inputs

Librarian's existing private corpus was sufficient; no new Researcher request
was required for this bounded package. The consulted private Library HEAD is
`b521af194da4e1455c776132e77f282f5247841c`, with the power dossier
`Library/subsystems/power-protection.md` (SHA-256
`14474c1af63917cd8085fc712495364aed869fda70b8289a1f55a478a4137483`) and
the selected-component provenance brief
`Library/briefs/pisxme-component-firmware-provenance-20260913.md` (SHA-256
`03172b16ec5fd865f6394dc217cd504cdaeba12df62a864b15d71e558735d12a`).

The binding project authority records used here are:

- `authority-inventory/primary-docs/power/TPSM63606_SUPPORT_AUTHORITY.md`,
  SHA-256 `6bc179162c0d42d089b6df0fd9cd2823ce77c1f5b9587d4b7178cac297d9341d`;
- `PHASE15_TI_LAYOUT_OVERLAY.md`, SHA-256
  `13f2ded1b9d3f7ba8f0622dfa12fe757391553ae53ea46c0d2594fdfe526cf05`;
- `PHASE15_REGULATOR_LAYOUT_RECEIPT.md`, SHA-256
  `8d4f48134eb9b524cc8c5d6dfe9562af727aa64eded0fb6d80d6f4d8be3541ed`;
- `PHASE13_STACK_RECEIPT.md`, SHA-256
  `0ada791776daa3ce97e8ebee462df2e46cc7bd4077039e25b6236e5090c0005a`;
- `authority-inventory/primary-docs/jlc/JLC06161H-7628_IMPEDANCE_INPUTS.md`,
  SHA-256 `ff4a4d904dde588d9d5deb17e39cee5a146de0ce68583edfa2c5b54b8161295a`;
- `authority-inventory/primary-docs/jlc/JLC06161H-7628-stack-api-20260830.json`,
  SHA-256 `d05b35679338f41986ca756bafe88ee655775b37a86a07cf2bbc107fbb6e58e0`;
- local `PiSXMe_RevA_Clean.pretty/TPSM63606RDLR_RDL0020.kicad_mod`, SHA-256
  `be0541e2a1de26e301ebdc9e1e42930a0ee16e5e6f43a7b515753d0a7bd7c152`.

The authorities require local VIN/VOUT bypass, a short feedback route,
localized top-side PGND return copper, a lower-layer VOUT feed, a solid ground
reference below each module, and four PGND thermal vias per TPSM63606 module.
The retained EVM distance is a reference measurement, not a silent project
hard limit. No vendor thermal or impedance result is transferred to this
board.

## Exact-head Light validation and native rule context

The supported command was run in fresh detached workspace
`validation-si-power-reference-current-head-61085fe0-20260913T204605Z`:

```text
/home/nyx/pisxme-eda-workers/scripts/pisxme-worker validate \
  /home/nyx/PiSXMe HEAD si-power-reference-current-head-61085fe0 \
  bash -lc 'set +e; kicad-cli version > /workspace/output/kicad-version.txt 2> /workspace/output/kicad-version.stderr; vrc=$?; kicad-cli pcb drc --format json --severity-all --output /workspace/output/drc.json --exit-code-violations /workspace/project/pisxme/reva-clean/PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb > /workspace/output/drc.stdout 2> /workspace/output/drc.stderr; drc_rc=$?; printf "VERSION_RC=%s\\nDRC_RC=%s\\n" "$vrc" "$drc_rc" > /workspace/output/returncodes.txt; exit 0'
```

The qualified image is `pisxme-kicad-light:v1`, image identity recorded by the
launcher in `validation.json`, and the native tool reports `10.0.6`. Raw
outputs are retained here:

- `drc.json` — 300 violations and 499 unconnected items;
- `drc.stdout`, `drc.stderr`, `returncodes.txt` — native output and exact
  return codes (`VERSION_RC=0`, `DRC_RC=5`);
- `kicad-version.txt` — `10.0.6`;
- `geometry.json` — exact-board serialized geometry census;
- `SHA256SUMS` — hashes for every package artifact.

The DRC violation classes are 138 `clearance`, 118 `track_width`, 15
`copper_edge_clearance`, 9 `track_dangling`, 7 `via_dangling`, 6
`courtyards_overlap`, 5 `pth_inside_courtyard`, and 2 `tracks_crossing`.
Native DRC includes five ignored check keys (`missing_courtyard`,
`track_not_centered_on_via`, `tuning_profile_track_geometries`,
`footprint_filters_mismatch`, and `footprint_type_mismatch`). They remain
acceptance gaps and are not treated as waivers by this package.

## Six-layer and saved route evidence

The serialized board declares the approved six-layer contract:

| Layer | Serialized role |
|---|---|
| `F.Cu` | signal/component layer |
| `In1.Cu` | signal layer named `In1.GND`, ground reference |
| `In2.Cu` | signal layer named `In2.PWR`, power distribution |
| `In3.Cu` | signal layer named `In3.PROTECTED_12V`, protected-12-V distribution |
| `In4.Cu` | signal layer named `In4.GND`, ground reference |
| `B.Cu` | signal/component layer |

The exact-head serialized census finds 131 footprints, 329 segments, 90
through-vias, and three `POWER_GND` zones. Signal segments are 216 on F.Cu and
113 on B.Cu; no signal segments are serialized on inner layers. `POWER_GND`
has 47 segments, 11 vias, and 173.491568 mm of saved track length, with zones
on F.Cu/In1.Cu/In4.Cu. This supports the intended adjacent reference topology
at the saved-object level but does not prove filled-zone continuity, local
return-via effectiveness at every transition, or fabricated-board impedance.

Saved controlled-channel metrics (mm) are:

| Net | Segments | Vias | Layers | Width(s) | Length |
|---|---:|---:|---|---|---:|
| `CM5_PER0_P/N` | 5 / 5 | 0 / 0 | F.Cu / F.Cu | 0.13208 / 0.13208 | 125.240 / 123.570 |
| `CM5_REFCLK_P/N` | 6 / 6 | 2 / 2 | F.Cu+B.Cu | 0.13208 / 0.13208 | 114.614 / 111.228 |
| `CM5_PET0_P/N` | 2 / 2 | 0 / 0 | F.Cu / F.Cu | 0.13208 / 0.13208 | 11.993 / 14.511 |
| `V100_PET0_P/N` | 7 / 7 | 2 / 2 | F.Cu+B.Cu | 0.13208 / 0.13208 | 121.888 / 121.278 |
| `CM5_USB3_RX_P/N` | 8 / 6 | 4 / 4 | F.Cu+B.Cu | 0.13208 / 0.13208 | 127.770 / 131.364 |
| `CM5_USB3_TX_P/N` | 6 / 7 | 3 / 4 | F.Cu+B.Cu | 0.13208 / 0.13208 | 122.560 / 123.360 |

Other saved USB3 channels retain widths of 0.15/0.20 mm (`USB_RX1` and
`USB_TX1`) or 0.20 mm (`JMS_USB3_TX`) and therefore do not establish the
approved 90-ohm starting geometry. The local controlled-impedance rule is
verified as a design input by the JLC authority, but no field solver, coupon,
TDR, eye, or other SI measurement is present. The
`layers_routes_impedance_return` row therefore remains OPEN. Storage USB3
route-dependent closure is `WAITING_ON #2`.

## Regulator reference overlay

The exact-head geometry census confirms U3, U4, and U5 use
`TPSM63606RDLR_RDL0020`, F.Cu, 0 degrees, 20 pads. U3 is at `(60,165)`, U4 at
`(225,105)`, and U5 at `(235,105)`. The central PGND thermal pads are present
in the local 1.58 x 0.50 mm package footprint; this package identity is
preserved, not corrected here.

Current center-distance observations to the authority-defined cohorts:

| Module | Cohort | Min distance | Max distance | Result |
|---|---|---:|---:|---|
| U3 | C5-C9, R3-R6 | 6.104 mm | 30.017 mm | local output/VIN support exists; full copper/thermal closure open |
| U4 | C14-C19, R11-R14 | 11.180 mm | 155.724 mm | input/output banks stranded; overlay mismatch |
| U5 | C23-C47, R19-R22 | 11.180 mm | 132.098 mm | input/output banks stranded; overlay mismatch |

The exact-head power summaries are:

- `12V_PROTECTED`: 6 segments, 1 via, 23.600 mm saved length, widths
  0.25/0.30 mm;
- `CM5_5V`: 37 segments, 9 vias, 225.029145 mm saved length;
- `BRIDGE_3V3`: 0 segments, 0 vias;
- `BRIDGE_1V1`: 0 segments, 0 vias;
- `POWER_GND`: 47 segments, 11 vias, 173.491568 mm saved length.

`FB_CM5_5V`, `FB_BRIDGE_3V3`, `FB_BRIDGE_1V1`, `RT_BRIDGE_3V3`,
`RT_BRIDGE_1V1`, `PG_BRIDGE_3V3`, and `PG_BRIDGE_1V1` are not evidence of
closed routed controls on the selected board; U4/U5 output feeds and local
PGND thermal-via arrays remain absent. This is a current-board observation,
not permission to move parts or change the regulator contract. The
`regulator_reference_overlays` row remains OPEN and any placement/corridor
decision belongs to Macro Placement Authority. The route-dependent regulator
power work is parked with the integrated corridor subtree while Issue #2 is
open; this package does not duplicate its investigation.

## Package disposition

This package closes the independent evidence-refresh task at exact current
head, but it does not close either acceptance row:

- `layers_routes_impedance_return`: **OPEN** — controlled impedance, complete
  return paths, storage corridor, and fabrication/SI evidence remain required.
- `regulator_reference_overlays`: **OPEN** — U4/U5 placement/corridors,
  regulator controls, VOUT feeds, local PGND returns, thermal vias, and fresh
  integrated validation remain required.
- `power_current_transient_thermal`: **OPEN** — current, transient, thermal,
  connector contact sharing, fuse/I²t, MLCC effective capacitance, and board
  measurements remain unproven.

No fabricated-hardware, vendor approval, thermal simulation, impedance
measurement, or DRC waiver is claimed. The producer/integration states remain
`none`; Root may link this receipt to the acceptance matrix and mark only the
independent evidence subtask done while retaining all required acceptance rows
OPEN.
