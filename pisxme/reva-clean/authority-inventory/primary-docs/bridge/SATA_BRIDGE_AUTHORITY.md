# USB-to-SATA bridge authority

Date checked: 2026-08-29. This is an authority record, not a schematic.

## Selected item

Texas Instruments `TUSB9261IPVP`, active commercial part, 64-pin HTQFP/PVP,
nominal 7 x 7 mm exposed-pad package. It supports USB 3.0 5 Gb/s and one
SATA Gen1/Gen2 port up to 3 Gb/s, UASP and BOT, and is intended for HDD/SSD
bridging. The selected IPVP version is the ordinary commercial temperature
part; do not substitute `TUSB9261IPAPRQ1` without a package/temperature/BOM
review.

Local primary records:

- `TUSB9261-datasheet-revI.pdf`, SHA-256
  `a67457f3c9349bdc2a3b9eabb5f63a3b25d033afc62669fe91f8370ffb67bdec`.
- `TUSB9261-implementation-guide-revE.pdf`, SHA-256
  `a2ebc049ab266a6a81cc4ea83b8d75118d3cf22476f22798b8135a69ad6dffa5`.
- `TUSB9261DEMO-user-guide.pdf`, SHA-256
  `525f9d77d1984dcdb5ef43e66a0cedf95789fbf7fe72d9bc6d1bf19cd9b39007`.

## Firmware, configuration, and programming

TI publishes default firmware resources on the TUSB9261 product page:

- `SLLC416`, version `01.00.00.0M`, released 2018-09-03, U1/U2 disabled;
- `SLLC421`, version `01.00.00.0D`, released 2012-08-27, U1/U2 enabled;
- `SLLC414`, version `01.00.00.0E`, released 2013-10-24, TUSB926x
  FlashBurner Utility.

The TI download pages currently require export approval for the ZIP payloads;
the download page URLs and version metadata are retained below, and the HTML
error responses were deliberately not stored as fake ZIP files. Firmware is
stored in an attached SPI flash and loaded after reset. The default Rev-A
choice is the TI-provided U1/U2-disabled image; any custom descriptors or
GPIO behavior require a separate TI-supported firmware decision. The DEMO
guide supplies the SPI-flash, reset, crystal, USB/SATA wiring, and TI firmware
swap evidence.

## Required behavior evidence

TI documents UASP/BOT, SATA AHCI, USB firmware update through a TI application,
SPI firmware storage, and the reset sequence. The implementation guide gives
90-ohm USB and 100-ohm SATA differential targets, 2.5-mil SuperSpeed mismatch,
2.5-mil SATA mismatch, 40 MHz clocking, and required 1.1 V/3.3 V rails. The
datasheet requires at least 2 ms of global reset after supplies are valid and
describes SATA port reset/OOB link negotiation.

The TI documents do not promise Linux discard/TRIM semantics. Linux UAS/BOT
enumeration is credible from the standard USB mass-storage interfaces, but
TRIM/discard, suspend/resume, and host-bus reset must be tested on the chosen
firmware and SSD before hardware release. This is a validation gate, not a
reason to invent a firmware claim.

## Candidates considered

| Candidate | Result |
|---|---|
| JMicron `JMS578`, QFN48 6x6 | Rejected: LCSC exact listing is out of stock; no major-distributor buy path; public material exposes firmware utility/SPI NVRAM but no image/config package; Linux discard behavior is firmware-dependent in credible reports. |
| ASMedia `ASM1153E`, QFN48 6x6 | Rejected: weaker bare-chip procurement and firmware evidence; a real commercial module documents no TRIM. |
| JMicron `JMS580` | Rejected for this closure: JMicron explicitly advertises TRIM/UASP, but no dependable exact major-distributor procurement record or complete public firmware/configuration path was established. |
| TI `TUSB9260PVP` | Rejected: TI marks it not recommended for new designs and the available listing is out of stock. |
| TI `TUSB9261IPVP` | **Selected**: active exact DigiKey/Mouser records, TI reference design, implementation guide, firmware images, FlashBurner utility, EVM, documented USB/SATA behavior, and ordinary SMT package. |

## Procurement

DigiKey exact record `296-35545-ND` showed Active status, 2,107 in stock,
manufacturer standard lead time 26 weeks, MOQ 1, standard package 250, and
about USD 10.75 quantity 1, USD 8.40 quantity 10, USD 6.52 quantity 1,000.
Mouser exact `595-TUSB9261IPVP` showed 469 in stock, MOQ 1, factory lead time
26 weeks, and approximately USD 7.73 quantity 1, USD 5.98 quantity 10,
USD 5.06 quantity 100, and USD 4.55 quantity 1,000. DigiKey lists EDA/CAD
models; TI provides the package authority. LCSC/JLC exact stock was not
required because two major distributors have live stock. Sourcing risk:
MEDIUM due long factory lead, otherwise strong and multi-source.

## Decision

`CLOSED`. JMS578 is explicitly rejected as impractical for this bare-chip
design. TUSB9261IPVP closes the approved plan's bridge requirement, subject to
the required Phase 7 firmware/SSD Linux validation and no Phase 3 work in this
authority sprint. It closes the CM5 USB3 -> USB/SATA bridge -> SATA-only B-key
M.2 architecture without using the CM5 USB2 SERVICE link.

Provenance: TI product page, Rev-I datasheet, Rev-E implementation guide,
DEMO user guide, firmware download pages, and live DigiKey/Mouser records.
TI material is retained for design reference under its published terms.
