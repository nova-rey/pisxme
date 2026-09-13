# Phase 24 SI, return-path, and Path-A provenance evidence receipt

Date: 2026-09-13  
Workstream: `/root/si_provenance_lane`  
Scope: documentation-only evidence closure from committed base `72df93fc`. No
schematic, PCB, library, rule, or configuration file was edited.

## Four-state identity

- **Baseline:** `72df93fc8ec6af6ee595df13d6e9b30369676550`, selected board
  `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`, board SHA-256
  `75d2d37063818093429b44dbe4197005c2f94b23554a34947a68acaaa181bf7c`.
- **Producer candidate:** none; this lane made no CAD candidate.
- **Integration candidate:** none; Root controls serialized integration.
- **Validation result:** read-only source/geometry census completed. A fresh
  qualified-Light DRC context check was attempted but the disposable clone
  exhausted host disk before KiCad started; no result is promoted from that
  attempt.

The raw geometry artifact is `geometry-census.json` in this directory.

## Stack, layers, and saved return topology

The board declares the approved six-layer contract:

| Layer | Serialized role | Intended use |
|---|---|---|
| F.Cu | signal | component/signal layer |
| In1.Cu | signal named `In1.GND` | solid ground reference |
| In2.Cu | signal named `In2.PWR` | power distribution |
| In3.Cu | signal named `In3.PROTECTED_12V` | protected 12-V distribution |
| In4.Cu | signal named `In4.GND` | solid ground reference |
| B.Cu | signal | component/signal layer |

The exact stack authority is `PHASE13_STACK_RECEIPT.md` (SHA-256
`0ada791776daa3ce97e8ebee462df2e46cc7bd4077039e25b6236e5090c0005a`) and the
reproducible JLC input record
`authority-inventory/primary-docs/jlc/JLC06161H-7628_IMPEDANCE_INPUTS.md`
(SHA-256 `ff4a4d904dde588d9d5deb17e39cee5a146de0ce68583edfa2c5b54b8161295a`).
That authority assigns L2/In1 and L5/In4 as GND references, ordinary through
vias, and 90-ohm targets for PCIe/USB3/USB2 with 0.13208-mm (5.2-mil) starting
width; SATA/Ethernet target 100 ohms. Its calculator API response is retained
at `authority-inventory/primary-docs/jlc/JLC06161H-7628-stack-api-20260830.json`,
SHA-256 `d05b35679338f41986ca756bafe88ee655775b37a86a07cf2bbc107fbb6e58e0`.
A fabrication coupon and measured board impedance remain required evidence.

A read-only parse of the exact selected board found 329 segments, 90 through
vias, and 3 POWER_GND zones. Signal segments are 216 F.Cu and 113 B.Cu; no
signal segment was found on In1/In2/In3/In4. POWER_GND has 47 segments, 11
vias, and 173.491568 mm of saved track length, with zones on F.Cu/In1.Cu/In4.Cu.
The detailed pair counts and widths are in `geometry-census.json`.

This supports the intended adjacent-reference topology at the saved-object
level: F.Cu routes can reference In1 GND and B.Cu routes can reference In4
GND. It does not prove that every transition has a local return via, that zone
fills are continuous after refill, or that the routes meet impedance/skew/SI
limits. The SI/layer/return acceptance row remains **OPEN**.

## Rule-context binding and scope

The exact source files are:

- project sidecar `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pro`, SHA-256
  `f965a4a405f1f2c0fa54a96a22d4bffaa0ee04e5787ad21db31c9c3bcf990143`;
- board-local rules `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_dru`, SHA-256
  `d5473e6262fdf3b53d5de051626f0ed76dedf7257ba591f79ab8ad55f5b411ec`;
- selected schematic `PiSXMe_RevA_Clean.kicad_sch`, SHA-256
  `6eef63bd3d2b0b9fafc0150d3c34f636ce24a48b2ecbd3d28a5f0bfec167e9f1`.

Static inspection shows the project sidecar defines `Default` at 0.20-mm
track/clearance, `HS_PCIE_90R` and `HS_USB3_90R` at 0.13208-mm width with
0.2032-mm pair gap, and `PCIE_PERST_CONTROL` at 0.13208-mm single-ended
width. Its netclass patterns are limited to the named CM5/V100 PCIe, CM5
USB3, and CM5_PERST nets. The board-local `.kicad_dru` has one condition-gated
exception: XIN/XOUT only, 0.10-mm width and 0.10-mm clearance.

The static files therefore preserve the intended scope: localized JMS583
crystal escape; approved high-speed classes; and normal 0.20-mm/default rules
outside those scopes. They do not prove file loading. The earlier successful
scope audit is tied to another board SHA and cannot be transferred to this
post-GATE_B board. A fresh Light validation is required before Root promotes
this current-context claim. The attempt used the supported launcher against
`72df93fc`, but clone creation stopped with `No space left on device` before
KiCad ran; the named validation workspace was released and no raw DRC exists.

No rule severity, global minimum, short/open handling, or manufacturing check
was suppressed by this lane.

## Path-A component and firmware/provisioning provenance

The latest private Library HEAD is
`b521af194da4e1455c776132e77f282f5247841c` (`private/Library`), verified from
the configured `private` remote. Its Librarian brief
`Library/briefs/pisxme-component-firmware-provenance-20260913.md` records that
Path A is the selected production implementation and RTL9210B-CG Path B is an
isolated, unpromoted alternative whose production-integration gate is out of
scope for this campaign. The private J1 refresh is
`Library/briefs/sxm2-j1-refresh-20260913.md`; its indexed source map is
`Library/indexes/sxm2-benchoff-contact-map.json`.

Selected Path-A identities and local package evidence:

| Ref | Identity | Local footprint / evidence hash | Current disposition |
|---|---|---|---|
| U7 | TI `TUSB9261IPVP` / PVP0064A | `PiSXMe_RevA_Clean.pretty/TUSB9261IPVP_PVP0064A.kicad_mod`, `00b9475bc4e01d286f99d331e1b2aa4e6df8cce228cdc262936b5f56b5885c3a`; TI Rev-I package receipt | package/design basis closed; exact programming record remains open |
| U11 | JMicron `JMS583-QHFA3A`, QFN64 8x8 | `JMS583_QFN64_8x8.kicad_mod`, `11918576998884d5885debb500966b20804f7d14394212379fad31d0e5669c05`; JMicron PDB-18001/PDS-17001 records | mask-ROM baseline policy closed; PCB Value field is empty and should be corrected in the release BOM/manifest; procurement remains open/high |
| U12 | TI `HD3SS6126RUAR`, RUA0042A | `HD3SS6126_RUA0042A.kicad_mod`, `9490928521cf2d8677da7bf188fc265664095d99978ae7c1f038da07adf33ffd`; TI datasheet | identity/package source present; 0.40-mm project pitch versus 0.50-mm TI package-view pitch remains a live authority conflict |
| U13 | TI `HD3SS3412RUAR`, RUA0042A | `HD3SS3412_RUA0042A.kicad_mod`, `b08bbf124876cb5e121a83f9290548c234d4b062a315423532f2aac2036433e0`; TI datasheet | identity/package source present; final integrated validation remains open |
| U14 | TI `SN74LVC1G17DBVR` | project mode matrix and retained TI datasheet | no firmware; native mode behavior and release procurement remain open |

The Path-A design authority `authority-inventory/primary-docs/storage-upgrade/jms583/JMS583_DESIGN_AUTHORITY.md` (SHA-256 `5285cdf2e0e894970aee4565fe24d6f0d7b80b376bba6e51ceb58c3bd50f290a`) establishes the JMS583 pin map, package, factory mask-ROM baseline, optional DNP SPI NVRAM boundary, support values, and the rule that future updates require JMicron-authorized image/tool. `authority-inventory/primary-docs/tusb9261/TUSB9261_PVP_LAND_PATTERN_RECEIPT.md` (SHA-256 `d454a458743046ab8e60f694e912ac3b54e84333ae4db430040b6608c0afcc9b`) establishes the TI PVP0064A package. `authority-inventory/primary-docs/bridge/TUSB9261_FIRMWARE_RECEIPT.md` (SHA-256 `297154baa6ebfffd4230739081d0b5db5bc38c70d5b5712551ceee431731e04e`) records TI SLLC416/SLLC414 and the gated-download boundary.

The latest Librarian brief strengthens, but does not close, `component_firmware_provenance`: TUSB9261 requires a lawful SLLC416/SLLC414 access/version/formatted-image/programming record and no-swap polarity choice; JMS583 baseline needs no project firmware, but exact traceable prototype supply and lifecycle/suffix confirmation remain open. No firmware binary, vendor authorization, procurement quote, or hardware programming run is claimed.

## J1 evidence linkage

The public reverse-engineering and manufacturer evidence is linked through the
private Library, without copying restricted/reference material into public
history. The exact records are:

- Library source IDs `sxm2-benchoff-article-20260912` and
  `sxm2-benchoff-repo-3173b02c`; pinned Benchoff repo commit
  `3173b02c085218d66c4a2a9e5492853fb53ee097`;
- Xiaoyu repository `xiaoyu9733/sxm2-pinout-definition` at
  `c05541e1846b47f51d05a2149ff044d4d2eba727`, which contains only a README and
  supplies no independent contact map;
- Amphenol/FCI `74221-101LF` product authority and Rev-W drawing metadata;
- patent `CN108280004B`, used for connector/topology corroboration only;
- low-confidence conflicting `3890p/SXM2-to-PCIE-Riser-card` at
  `85b0e248923ec4114ff464c2400e7cb6de5af40c`, retained as a conflict record.

The public implementation family is not treated as NVIDIA-official. The
private Library's mechanical parse establishes 400/400 identifier matches and
zero coordinate error between PiSXMe J1 and Benchoff's
`AMPHENOL_74221-101LF.kicad_mod`; the local J1 footprint is
`PiSXMeRevAClean_SXM2_74221_101LF.kicad_mod`, SHA-256
`d67e826c787d498b8459d51197d300904504ec3ace7c505fc08821d3c4d99305`.
The current physical block is 400 pads, 307 named nets, and 93 no-net pads;
the nine-pin schematic abstraction is not a 393-contact electrical symbol.

The approved bounded contract remains 130 `12V_PROTECTED` contacts, 170
`POWER_GND` contacts, selected x1/reference/reset contacts A2/A3, G1/G2,
E7/F7, and E18, with other published lanes and the 31 NC/project-unknown
contacts plus K18/K19 preserved unassigned. This is sufficient for the
bounded J1 package/net contract. J1 package identity and contact linkage are
therefore **CLOSED within scope**; full-board power/return, mechanical
land-pattern, fabrication, V100 undocumented behavior, and integrated DRC
remain open.

## Acceptance disposition and next actions

This receipt provides reusable scoped evidence; it does not close the full
Phase 24 rows:

- `layers_routes_impedance_return`: **OPEN**; run fresh Light on the exact
  current board/project/rule files after host disk is restored, then attach
  native DRC, rule-scope negative control, refill/return-path evidence, and
  final route metrics.
- `component_firmware_provenance`: **OPEN**; assemble exact-BOM/programming
  metadata, lawful TI access record, no-swap polarity, traceable JMS583
  supply/lifecycle evidence, and explicit U12 pitch disposition.
- `library_pin_mapping`: **OPEN** overall; J1 bounded contract is closed, but
  U12 pitch and final model/land-pattern/assembly checks remain open.
- `physical_opens_shorts`, `native_drc`, `power_current_transient_thermal`,
  `regulator_reference_overlays`, `storage_mode_behavior`, `dfm`, and
  `hostile_review`: remain open and depend on the canonical integrated
  candidate and fresh validation.

The immediate capability blocker is host storage, not missing engineering
knowledge. The supported Light validation requires a disposable clean clone;
with only 6.7 MB free, it cannot be rerun. Root should free enough space for
one fresh checkout while retaining the campaign archive and receipts, then
rerun the exact current-context validation once. No architecture change or
user decision is requested by this receipt.
