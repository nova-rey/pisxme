# Phase 24 RTL9210B-CG parallel comparison

Checked 2026-09-09. This is an isolated Path-B qualification record. Path A
(`HD3SS6126` + `TUSB9261`/`JMS583` + `HD3SS3412`) remains the fallback and is
not modified by this comparison.

## Decision

**CONTINUE BOTH pending a narrowly defined Path-B provisioning/application-
circuit experiment.** RTL9210B-CG is a serious candidate because it can
collapse the two bridge devices and the storage-side high-speed selector into
one USB-to-SATA/PCIe controller. It is not yet production authority: the
remaining risks are provisioning and documentation provenance, not a quick
rejection based on the unfinished community PCB.

## Path-B proposed implementation

```text
CM5 USB2 + USB3
        |
        v
 RTL9210B-CG (U1, QFN-68, 8 x 8 mm, 0.4 mm pitch, exposed chip pad 69)
        |
        +-- shared SATA/PCIe lane 0
        |     U1.68 TXOP -> M.2 49 PETp0 / SATA-A+
        |     U1.67 TXON -> M.2 47 PETn0 / SATA-A-
        |     U1.64 RXIP -> M.2 43 PERp0 / SATA-B-
        |     U1.65 RXIN -> M.2 41 PERn0 / SATA-B+
        +-- U1.61/62 -> M.2 55/53 REFCLK in NVMe mode
        +-- U1.14/13 -> M.2 PERST#/CLKREQ# in NVMe mode
        +-- U1.8 GPIO6/PEDET <- M.2 contact 69 / CONFIG1
        +-- local SPI flash, 25-MHz reference, rails, reset, VBUS sense
```

The M.2 contact 69 is not U1 exposed pad 69. Lane-0 polarity and the SATA
B-side naming are taken from the retained corrected platform matrix, not from
the quarantined WIP root XML. PCIe lane 1 is intentionally not connected for
the Rev-A single-lane socket and requires an explicit no-connect review.

## Evidence and provenance

| Question | Current evidence | Result |
|---|---|---|
| Exact candidate | JLC current listing identifies Realtek `RTL9210B-CG`, C5143573, QFN-68, SMT, MSL 3 | Identity/procurement lead CLOSED; stock depth and price not reproduced |
| Package/CAD | Locally recreated `RTL9210B-CG_QUALIFICATION`, 69 SMD pads, 4.8-mm EP; native package audit V440 | Technical package basis CLOSED; authorized production drawing still OPEN |
| Pin map | retained Rev 1.1 technical document, native XML, symbol audit, M.2 mapping audit | Cross-checked candidate map CLOSED for disposable work |
| USB | U1.37/38 USB2; U1.41/42/46/47 USB3 | CLOSED for topology; full routed channel OPEN |
| Shared storage | U1.68/67/64/65 and M-key 49/47/43/41 | CLOSED for proposed mapping; native integrated lane-0 route OPEN |
| Mode selection | U1.8 PEDET/CONFIG1 and U1.12 isolation evidence | Feasible, but exact power-off sequencing and empty-socket behavior OPEN |
| Reference/support | WIP HynixCJR native schematic/netlist plus retained local support audits | Corroborating only; application-circuit authority OPEN |
| Firmware | bensuperpc/rtl9210 tools/config ecosystem and damnnfo binaries | Technical ecosystem exists; rights, exact image, and virgin programming OPEN |
| Implementation | V35/V562/V661/V664 disposable source-field/rail work | Real progress; not a complete production or native-clean board |

Primary/corroborating sources are retained under
`authority-inventory/rtl9210b/`. External receipts include:

- JLCPCB: https://jlcpcb.com/partdetail/RealtekSemicon-RTL9210BCG/C5143573
- HynixCJR implementation: https://github.com/HynixCJR/LZ-1-Backplane
- firmware/config ecosystem: https://github.com/bensuperpc/rtl9210
- firmware artifact receipt: https://github.com/damnnfo/rtl9210b-firmware
- package/data-sheet recovery issue: https://github.com/bensuperpc/rtl9210/issues/6

The HynixCJR repository explicitly labels its PCB WIP. Its schematic, native
XML, support-netlist, and package geometry are corroborating evidence only.
Its source footprint's `through_hole` metadata is rejected; the local SMD
footprint was recreated and audited instead. Community firmware binaries and
configs are not copied into production release material and have no assumed
redistribution permission.

## Support-circuit audit

| Function | Current Path-B treatment | State |
|---|---|---|
| USB2/USB3 | CM5 fixed USB connection to U1.37/38 and U1.41/42/46/47 | OPEN route/termination validation |
| Clock | 25-MHz crystal/reference network on U1.52-54 | Local source-field primitives pass; complete authority/value review OPEN |
| SPI | external flash on U1.18/19/21/22/23/24 with accessible programming boundary | Native support primitives pass; virgin programming OPEN |
| Reset/VBUS | U1.3 reset and documented VBUS-detect path | support implementation OPEN |
| PEDET/CONFIG1 | U1.8 to M.2 contact 69, power-off mode decision | technically plausible; debounce/settling and empty socket OPEN |
| REFCLK/PERST/CLKREQ | U1.61/62, .14, .13 to M.2 NVMe sidebands | route, coupling, pull-state, and unpowered-state checks OPEN |
| Rails | U1 5-V input, local 3.3/1.1-V support, SSD 3.3-V delivery | rail source primitives pass; complete current/inrush/thermal budget OPEN |
| SATA | shared U1 lane 0 to M.2 SATA contacts | mapping CLOSED; SATA OOB/native route validation OPEN |
| NVMe | single PCIe lane 0, no lane 1 | mapping CLOSED; receiver-detect/electrical-idle and boot validation OPEN |

## Firmware/programming decision

The evidence distinguishes five cases. Updating a known-working enclosure is
technically plausible from the community updater/config ecosystem. It does
not prove that a virgin RTL9210B-CG plus blank SPI flash can be provisioned.
The current minimum experiment is therefore: obtain a traceable chip lot and
an authorized image/config package; populate a disposable board with named
SPI flash and test pads; record the tool/version, chip marking, image/config
hashes, USB descriptors, SATA/NVMe behavior, reset, recovery, and empty-socket
states. Do not use a community binary as production firmware without a rights
decision. This is a narrow external-artifact experiment, not a request to
change architecture.

## Apples-to-apples comparison

| Criterion | Path A: TUSB9261/JMS583 + selectors | Path B: RTL9210B-CG |
|---|---|---|
| Major bridge/switch ICs | 2 bridges plus USB and SATA/PCIe selectors | 1 bridge; no external high-speed storage selector proposed |
| High-speed routing | More devices and two selector boundaries | Fewer boundaries; one USB-to-storage channel and shared lane |
| Acreage | Larger support field and more routing | Smaller controller island, but dense QFN escape |
| BOM/assembly | Higher IC count; documented TI/JMicron mix | Lower IC count; QFN-68 0.4-mm escape and SPI flash required |
| Documentation confidence | Higher for TI; JMS583 firmware/supply remains a risk | Pin/package/support corroborated, but Realtek production pack is less public |
| Firmware risk | TUSB9261 path has documented TI tooling; JMS583 provisioning remains open | Real firmware ecosystem exists, but virgin provisioning/rights remain open |
| Procurement | Path-A exact JLC leads plus mainstream TI paths | JLC exact identity is current; no verified second bare-chip distributor |
| Auto SATA/NVMe | External control and selectors required | Native PEDET/CONFIG1 concept may remove both selectors |
| Performance | TUSB9261 SATA capped at 3 Gb/s; NVMe path separate | USB 5-Gbps fixed-board bottleneck; SATA/NVMe controller path unified |
| Validation burden | Mode-aware two-bridge isolation and selector timing | One controller, but firmware, PEDET, sideband, and lane-0 validation are new |
| Productization | More conventional public documentation | Lower artifact provenance and firmware-rights confidence |

## Open/closed ledger

**CLOSED for isolated comparison:** exact JLC identity; corrected SMD package
basis; candidate pin map; shared lane-0 map; USB2/USB3 presence; PEDET and
SPI support existence; native symbol/package/mapping/netlist audits; multiple
native source-field and rail connectivity primitives with negative controls.

**OPEN:** authorized package/application circuit; complete support-field route;
REFCLK/PERST/CLKREQ electrical states; SATA OOB and NVMe receiver-detect
behavior; SSD 3.3-V transient/inrush/thermal budget; exact stock/price/lead
time; traceable lot; virgin-chip programming; exact PiSXMe firmware/config;
recovery run; firmware licensing; integrated native ERC/DRC and mode-aware
hardware validation.

## Recommendation and next action

Keep Path A as the fallback and continue Path B. The next discriminating
experiment is not another scalar QFN routing nudge: recover an authorized
application/provisioning package or a traceable programmed module, then run a
complete disposable RTL9210B fixture using the corrected footprint and the
mapping above. If that experiment closes provisioning and the native fixture
passes all modes, prepare a reviewed migration plan before any production-CAD
replacement. Until then, Path B remains isolated qualification work.
