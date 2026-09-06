# Phase 24 RTL9210B-CG Path-B qualification

Status: **CONTINUE BOTH**. Path A remains the fallback/reference and is not
modified. Path B is a credible isolated prototype candidate, but is not yet
authorized for destructive replacement or production integration.

## Decision summary

The retained RTL9210B-CG Rev. 1.1 document says the controller combines USB,
PCIe and SATA hosts and automatically switches USB-to-PCIe or USB-to-SATA via
the M.2 PEDET interface. It supports USB 3.1 Gen 2, USB 2.0, UASP, PCIe Gen3
x2, SATA Gen1/2/3, SPI flash, and a 25 MHz reference. This directly addresses
the main reason Path A has four high-speed controllers/switches.

The practical unresolved item is not the SATA/NVMe topology. It is
productization of a virgin RTL9210B: exact Realtek-approved production
firmware/configuration package, licensing/redistribution rights, and a
repeatable initial-programming path for a bare QFN part. Community tools and
binary artifacts prove that the ecosystem exists, but do not close those
rights or variant-compatibility questions.

## Exact proposed Path-B mapping

```text
CM5 USB3 TX/RX + USB2 D+/D-
        -> RTL9210B-CG USB_TXP0/N0, USB_RXP0/N0, HSDP/HSDM
RTL9210B SATA_TXOP/TXON (68/67) -> M.2 SATA B pair
RTL9210B SATA_RXIP/RXIN (64/65) <- M.2 SATA A pair
RTL9210B PCIe_TXOP/TXON_0 (68/67) -> M.2 PETp0/PETn0
RTL9210B PCIe_RXIP/RXIN_0 (64/65) <- M.2 PERp0/PERn0
RTL9210B PCIE_REFCLKP/N (61/62) -> M.2 REFCLKP/N
RTL9210B PERSTBPIN (14) -> M.2 PERST#
RTL9210B CLKREQB (13) <-> M.2 CLKREQ# with required pull-up
RTL9210B GPIO6/PEDET (8) <- M.2 contact 69 / CONFIG1, per verified socket convention
```

The chip pad 69 is the exposed ground pad. It is not M.2 contact 69. The
shared lane-0 assignments above are explicit in the retained pin tables.
PCIe lane 1 (56-59) is not required for a single-lane M-key NVMe design and
must be left according to the final Realtek application circuit, not guessed.

## Support-circuit audit

Closed from the retained Rev. 1.1 document at the qualification level:

- 25 MHz crystal/reference: pins 53/54, clock supply pin 52.
- SPI flash: CS 24, CLK 19, SI 18, SO 23, optional quad pins 21/22.
- Reset: active-low RST_INPIN pin 3.
- Mode: PEDET pin 8, `1 = PCIe`, `0 = SATA`.
- PCIe: REFCLK 61/62, PERSTB 14, CLKREQB 13, hot-plug pin 10.
- Internal rails: 5 V input pins 33/17; internal 3.3 V and 1.1 V outputs
  are for the controller only. External 3.3 V/1.1 V rail connections and
  decoupling must follow the latest approved application circuit.
- RSET pin 51 and exposed ground pad 69 are required design items.
- `ISOLATEBPIN` pin 12 controls PCIe main power in PCIe mode and SATA power
  in SATA mode; SSD 3.3 V power/inrush remains a board-level requirement.
- USB supports SuperSpeed and USB 2.0; no USB-C connector or CC circuit is
  needed for this fixed internal CM5 connection.

Still open for production implementation: exact BOM values/layout from the
latest Realtek application circuit, M.2 socket sideband handling, SSD
3.3-V/inrush budget, thermal measurement, and validation of nonselected
interface behavior when the socket is empty or unpowered.

KiCad 10.0.5 successfully exported native XML netlists from the retained
community `RTL9210b_0.kicad_sch` and `M.2_0.kicad_sch`; those receipts are in
`authority-inventory/rtl9210b/RTL9210B_0.xml` and `M.2_0.xml`. This confirms
the CAD sources parse natively and that their RTL9210B pin names and M.2
PEDET contact are inspectable. It is not a PCB connectivity or ERC/DRC pass.

The support portion of `RTL9210B_0.xml` was independently audited by
`phase24_rtl9210b_corroborating_support_audit.py`. The extracted native
evidence now confirms the WIP source contains USB2/USB3, shared lane-0,
REFCLK/PERST/CLKREQ, PEDET, ISOLATEB, 25-MHz crystal, SPI-flash connector,
RSET, switched rails, and explicit unused-pin records. The detailed extraction
is in `authority-inventory/rtl9210b/RTL9210B_CORROBORATING_SUPPORT_NETLIST.md`.
This narrows B1 and the future fixture plan, but does not close B1–B5: the
source remains a WIP community implementation and still does not establish
PiSXMe M-key sideband ownership, released land-pattern authority, SSD
power/inrush validation, or authorized virgin-chip provisioning.

A secondary-hosted RTL9210 68-pin V203 demo schematic also explicitly lists
an RTL9210B-CG variant and corroborates candidate support values including a
2.2-uH regulator inductor and 12-kOhm RSET. It is retained as
`authority-inventory/rtl9210b/RTL9210B_DEMO_CORROBORATION.md`, but remains
non-authoritative because it is a different host design and does not close
the M-key sideband, SSD power, firmware-rights, or released-land-pattern
gates.

## Firmware and programming

The community firmware repository contains RTL9210B-specific configurations,
firmware binaries, a Windows `UTHSB_MPtool` flow, device configuration dumps,
and an SPI-flash recovery method. It also documents device-specific configs,
Windows-only updater limitations, and known stability-sensitive firmware
versions. This closes technical feasibility of update/recovery research, but
not legal provenance or repeatable virgin-chip provisioning.

Required bring-up experiment before Path-B promotion:

1. Obtain a traceable RTL9210B-CG lot and Realtek/OEM-authorized firmware,
   configuration, and updater package.
2. Assemble an isolated board with accessible SPI flash pads and UART/JTAG
   test pads; program a known-good image/config into a virgin part.
3. Record chip marking, flash MPN, image/config hashes, updater version, and
   USB descriptors in SATA and NVMe modes.
4. Exercise reset, empty socket, forced mode if supported by firmware,
   Linux UASP/TRIM/SMART, sustained I/O, suspend/resume, and recovery.
5. Only then generate production RTL9210B symbol/footprint and integrate it.

## Risk ledger

| Item | State | Evidence / next action |
|---|---|---|
| SATA/PCIe auto-selection | CLOSED at technical qualification | Rev. 1.1 mode table explicitly specifies PEDET and polarity |
| Shared lane-0 pin identity | CLOSED at technical qualification | Rev. 1.1 PCIe and SATA tables agree on 64/65/67/68 |
| USB2/USB3 bridge function | CLOSED at technical qualification | Rev. 1.1 USB table and feature summary |
| QFN-68 package existence | CLOSED, corroborated | Rev. 1.1 package statement plus JLC listing |
| Land pattern | OPEN | Community SMD footprint is useful but has bad `through_hole` metadata; recreate and audit |
| Exact support BOM/layout | OPEN | Need current Realtek-authorized application circuit |
| Bare-chip procurement | MEDIUM/OPEN | JLC lists C5143573, QFN-68, SMT; stock/price not exposed in the retrieved page |
| Firmware exists | CLOSED, corroborating | Retained configs/binaries and firmware ecosystem |
| Virgin initial programming | OPEN/HIGH | Community flow targets working enclosures and device-specific configs; run isolated experiment |
| Firmware rights/provenance | OPEN/HIGH | Do not redistribute community binaries without authorization |
| Linux/UASP/TRIM/SMART | MEDIUM | UASP is documented; validate kernel behavior on hardware |
| SSD 3.3-V/inrush/thermal | OPEN | Recalculate for selected SSD envelope and measure |
| Path-A preservation | CLOSED | No Path-A schematic/PCB files were changed |

## Path A vs Path B

| Criterion | Path A: TUSB9261 + JMS583 + 2 selectors | Path B: RTL9210B-CG |
|---|---|---|
| Major bridge/switch ICs | 4 | 1 |
| Native auto SATA/NVMe | External mode control and selectors | PEDET-native, firmware-dependent |
| High-speed routing | USB selector + two bridge branches + socket selector | One USB bridge to socket |
| BOM/assembly | Higher count, more QFN/QFN-like escapes | Lower count, QFN-68 plus flash/support |
| Documentation confidence | Higher for TI parts; JMS583 still open | Strong technical PDF, weaker public provenance |
| Firmware risk | TUSB9261 documented; JMS583 config risk remains | High: initial programming and rights |
| Procurement | JMS583 stock risk; selectors sourceable | JLC identity/SMT listing, current stock/price unresolved |
| Performance | CM5 USB-limited; TUSB9261 SATA <=3 Gb/s | CM5 USB-limited; SATA Gen3/PCIe bridge capability |
| Validation burden | Mode isolation across two switches/bridges | Firmware, mode, and unpowered-state behavior |
| Productization | More conventional/documentable | Smaller but dependent on Realtek/OEM package rights |

Recommendation: **CONTINUE BOTH pending one narrowly defined experiment** —
traceable virgin-chip programming and mode bring-up, plus acquisition of the
current Realtek application circuit. If that experiment closes, Path B is the
preferred migration candidate because it removes both external high-speed
selectors and the second bridge. Until then Path A remains the protected
implementation path.

## Sources

- Realtek RTL9210B-CG Rev. 1.1 PDF, retained under `authority-inventory/rtl9210b/community-lz1/rtl9210b.pdf`.
- [JLCPCB C5143573 listing](https://jlcpcb.com/partdetail/RealtekSemicon-RTL9210BCG/C5143573).
- [HynixCJR/LZ-1-Backplane](https://github.com/HynixCJR/LZ-1-Backplane), corroborating WIP CAD.
- [bensuperpc/rtl9210](https://github.com/bensuperpc/rtl9210), firmware/configuration and recovery evidence.
- [damnnfo/rtl9210b-firmware](https://github.com/damnnfo/rtl9210b-firmware), firmware/config artifacts.
