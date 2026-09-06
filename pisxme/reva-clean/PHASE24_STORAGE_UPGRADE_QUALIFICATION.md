# Phase 24 storage-island upgrade qualification

Checked 2026-09-06. This is a bounded qualification record, not a production
schematic or PCB approval.

## Required architecture

`CM5 USB3 + USB2 -> local USB A/B selector -> TUSB9261 SATA bridge or NVMe
bridge -> local SATA/PCIe selector -> one M-key Socket 3 -> 2280 module`.
The mode control is intended to be `AUTO / FORCE SATA / FORCE NVMe`, with
power-off mode changes only. All new circuitry must remain inside the existing
storage acreage.

## Candidate results

| Function | Candidate and exact variant | Evidence | Status | Decision |
|---|---|---|---|---|
| SATA bridge | TI `TUSB9261IPVP`, 64-HTQFP/PVP | TI Rev-I datasheet, implementation guide, DEMO guide, SLLC416/SLLC421 firmware pages, FlashBurner page, DigiKey/Mouser records | CLOSED | Retain. USB 5 Gb/s, SATA Gen1/Gen2 up to 3 Gb/s, UASP/BOT. Do not claim SATA 6 Gb/s. |
| USB A/B switch | TI `HD3SS6126RUAR`, 42-pin RUA WQFN | TI datasheet Rev A and product/order page | QUALIFIED FOR DESIGN REVIEW | It switches USB3 TX/RX and USB2 D+/D-. Active lifecycle; TI page was out of stock at check, while DigiKey/Mouser records showed orderable stock snapshots. Final exact distributor snapshot is required before BOM release. |
| SATA/PCIe switch | TI `HD3SS3412RUAR`, 42-pin RUA WQFN | TI datasheet Rev F / `HD3SS3412A` pinout and product page | QUALIFIED FOR DESIGN REVIEW | Four bidirectional differential channels, 3.3 V, common-mode and amplitude limits documented. SATA OOB and inactive NVMe electrical-idle behavior still require a complete mode-state review before pad assignment. |
| M.2 socket | JAE `SM3ZS067U215BMR1500`, 67-position, 0.5 mm, 2.15 mm M-key | JAE SM3-series manufacturer page and family drawing references; DigiKey exact-family evidence | IDENTITY/PROCUREMENT CLOSED; LAND PATTERN PENDING | This is the correct M-key variant direction. The exact released drawing/ECAD capture and pad-by-pad comparison must still be saved before replacing J3. The existing `SM3ZS067U410ABR1000` is B-key-only and cannot be reused for NVMe. |
| NVMe bridge | ASMedia `ASM2362`, QFN64 9 x 9 | ASMedia official product page only | BLOCKED | No public exact pinout/land pattern, reference circuit, firmware/configuration package, programming procedure, or authorized major-distributor order record was found. Do not invent a symbol/footprint or implement it. |
| NVMe alternatives | JMS583/JMS586/JMS580, RTL9210B, ASM2364/ASM2464 | Prior repo authority, bounded web search, and independent read-only review | REJECTED FOR THIS GATE | No candidate simultaneously exposed manufacturer-authoritative pin/land-pattern, reference schematic, firmware/configuration/programming, and traceable prototype procurement evidence. Marketplace availability does not close the authority gap. |

## Authoritative electrical facts captured

- TI identifies `TUSB9261` as ACTIVE, USB 3.0 5 Gb/s to SATA, SATA 1.5/3.0
  Gb/s, with UASP/BOT and SPI EEPROM application firmware. TI also exposes
  firmware resources and FlashBurner tooling.
- TI identifies `HD3SS6126RUAR` as ACTIVE, 42-pin RUA, with three bidirectional
  differential switch channels suitable for USB3 and USB2, 3.3 V supply,
  10-Gbps-class bandwidth, and published insertion-loss/isolation data.
- TI identifies `HD3SS3412A` as a 42-pin RUA four-channel bidirectional
  differential switch with SEL choosing Port B or C from Port A. Its published
  limits include 3.3 V +/-10%, differential amplitude below 1.8 Vpp, and
  common-mode below 2 V; the final SATA/NVMe state table must apply those limits
  to both selected and unselected ports.
- JAE identifies the SM3 series as a 67-position, 0.5-mm PCI-SIG M.2 family
  supporting SATA and PCIe with multiple key variants. The manufacturer page
  specifically lists `SM3ZS067U215BMR1500` as key M and
  `SM3ZS067U410BBR1000` as key B. The current project’s B-key J3 is therefore
  not an M-key combo solution. JAE's current product listing identifies
  `SM3ZS067U215BMR1500` specifically as key M, 2.15 mm, SMT, 67 position.
- ASMedia identifies ASM2362 as a PCIe Gen3 x2 to USB 3.1 Gen2 NVMe bridge,
  QFN64 9 x 9, with SPI external ROM, GPIO/I2C/UART, 25 MHz crystal, UAS,
  TRIM, and a 1.05 V supply. Those marketing-level facts do not provide the
  package pin ownership or a buildable authorized design package.

## Mode/control and validation work that remains gated

Before production edits, the authoritative design must still establish the
exact M-key contact map for SATA, PCIe x1/lane 0, REFCLK, PERST, CLKREQ, WAKE,
PEDET, power and ground; selector SEL polarity; safe inactive states; mode
latching/debounce; empty-socket PEDET behavior; bridge reset/flash/VBUS sense;
SSD 3.3-V current/inrush budget; and physical 2280 screw/height clearance.
The mode-aware fixture must pass forced SATA, forced NVMe, AUTO, empty socket,
reset/startup, and inactive-path contention checks before integration.

## Procurement snapshot

The exact TUSB9261 and existing SATA socket procurement records remain in
`authority-inventory/primary-docs/bridge/` and `authority-inventory/primary-docs/m2-jse/`.
The exact TI switch pages and distributor observations are recorded in the
source receipt below. No purchase was made. The requested +$20--30 planning
delta is not a quote and cannot be asserted until the NVMe bridge and added
support BOM are qualified.

## License/provenance

TI, JAE, and ASMedia material is retained as linked manufacturer reference
material under the suppliers’ terms; no proprietary firmware binary is copied.
Distributor pages are procurement evidence, not design authority. The local
PCB footprint for the existing JAE B-key part is project-derived and remains
reference-only for the requested M-key replacement until exact M-key drawing
parity is demonstrated.
