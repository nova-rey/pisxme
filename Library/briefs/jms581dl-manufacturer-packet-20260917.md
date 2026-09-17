# JMS581DL manufacturer design-in packet — indexed 2026-09-17

**Owner:** Librarian / Storage Reference Supervisor
**Evidence tier:** 1, restricted first-party manufacturer design-in material
**Source:** JMicron Technology Corporation / Smart Cube design-in channel, Gmail thread `1a07744f40afaf44`; attachment message `1a09fe9fdf65159a` from `kevin_c@smartcube.com.tw` received 2026-09-14; follow-up `1a0a39a716d94efa` received 2026-09-15.
**Private corpus:** `Library/sources/restricted/jmicron-jms581dl-design-in-20260914`
**Access:** Original vendor bytes are retained in the private Library companion only. No public-repository copy or redistribution authorization is asserted.

## Provenance and integrity

The seven received originals are preserved under the private source directory. `SHA256SUMS` beside them is the authoritative byte manifest. The packet was delivered through the JMicron/SmartCube design-in correspondence initiated by the PiSXMe inquiry on 2026-09-06. JMicron sales routed the request to Smart Cube; Smart Cube supplied the packet and later confirmed the demo/quotation/EVB context.

| Original filename | Revision/date | Bytes | SHA-256 |
|---|---|---:|---|
| `JMS581DL_1 Lun_Reference_Bus-Power_V1.00_SCH.zip` | V1.00 | 707611 | `9a1294389c09eac421326c448865e088faa766a3feb156ef00baabecbdac8cdb` |
| `PDS-00000028 JMS581DL Datasheet (Rev.1.02).pdf` | Rev.1.02 / PDS-00000028 / 2026-04-28 | 781853 | `a8056ad689671611e2ec97c5da4ca4c4c354b9da7cfecabcd33e0e0bbb31d578` |
| `JMS581-Series Layout Guide_V1.02.pdf` | V1.02 / LOG-00000004 / 2024-02-21 | 391071 | `a6ac1fa8222106865cd684cfcb76511b6e4b304e7f3d64c1743f516bda44144a` |
| `JMS581DL-DB-01-02_SCH_V1.00.zip` | V1.00 / 2026-04-15 (embedded reference schematic) | 711397 | `466e2b504dafd05f21baca3d7440306b0e9590eb8d31d708b88161bdbb3ccbca` |
| `JMS581DL-DB-01-02_PCB_V1.00.zip` | V1.00 | 691700 | `ec87c8c8ed635b884d759c5f191d0c7ea072655b1a359b969c1180b102f707ee` |
| `SPI-00000004 JMS581 SPI List (Rev. 1.05)_20250825.pdf` | Rev.1.05 / SPI-00000004 / 2025-08-25 | 147031 | `02442d21f7e3ca42ce7749b7fc793569ce78cf06a88f3442ace9e88c4f99922c` |
| `JMS581DL-DB-01-02_BOM_V1.00.pdf` | V1.00 | 100492 | `9284a01c8818f89bd9b6b8eeda4be9690ca41b5e77c4e8df4efde20777dbceed` |

## Manufacturer evidence

The datasheet identifies JMS581DL as a 144TFBGA 9 x 9 mm USB 3.2 Gen2 to SATA 6 Gb/s and PCIe Gen3 x2 bridge with 3.3-V I/O, external 25 MHz timing, external SPI support, and automatic USB-to-SATA/PCIe mode behavior. Its stated device rails are VCCO/XAVDDH 3.0–3.6 V and VCCK/AVDDL 1.0–1.1 V; USB VBUS is 4.5–5.5 V. The USB3+SATA typical-current table reports VCCO 1.9 mA, VCCK 378.9 mA, XAVDDH 2 mA, and AVDDL 705.5 mA. The power-on table gives T5V rise <=20 ms, 3V3/1V0 sequencing windows, reset release 120–500 ms, and clock startup <=5 ms.

The reference schematic/PCB/BOM show a standalone four-layer demo implementation using JMS581DL, MT3123B/FP6375/FP6381A regulators, MX25V8035F SPI flash, a 25 MHz source, USB-C, and M-key storage. The layout guide specifies continuous reference planes and nominal USB3 90-ohm, PCIe 100-ohm slot / 85-ohm M.2, and SATA 100-ohm guidance, with pair mismatch below 5 mil in the stated reference stackup. It recommends one 0.1-uF bypass per power pin and wider VCCK/AVDDL distribution. These are manufacturer reference constraints for JMS581 designs and require translation to PiSXMe’s six-layer stack.

The SPI list is useful component support evidence. It does not establish a PiSXMe firmware image, license, provisioning route, or production authorization.

## Current Path-A reconciliation

PiSXMe’s selected production implementation remains TUSB9261 SATA plus JMS583-QHFA3A NVMe behind HD3SS6126/HD3SS3412 selectors and one shared TE M-key socket, as recorded in the existing component/firmware authority brief. JMS581 is not promoted by this packet. The manufacturer demo topology uses its own USB-C, mode controls, power tree and M-key implementation; copying it would conflict with PiSXMe’s six-layer carrier, CM5 interface, shared M-key contract, product power architecture, mechanical envelope, and already-selected Path-A bridge topology.

| Area | Classification | Reconciliation |
|---|---|---|
| JMS581 144TFBGA package/ball contract | `CONFIRMED_BY_MANUFACTURER` | Strong evidence for a future candidate; current Path-A uses different bridge packages. Package authority must create any future native footprint/symbol contract. |
| JMS581 rails, current table, timing/reset | `CONFIRMED_BY_MANUFACTURER` | Applies to JMS581 only. No current Path-A power or sequencing change follows. |
| USB3/PCIe/SATA impedance and return guidance | `COMPATIBLE` | Useful reference evidence; six-layer PiSXMe stack, approved corridors and net classes still govern current work. |
| Reference four-layer PCB, placement and geometry | `PRODUCT_REQUIREMENT_OVERRIDES_REFERENCE` | Do not clone. Mechanical, CM5, SXM2 and selected storage constraints remain PiSXMe requirements. |
| Reference BOM/regulators/flash/clock | `COMPATIBLE` | Design-in evidence only; no direct substitutions into the selected BOM. |
| SPI support and mode records | `UNRESOLVED` | Supported flash families and demo controls are identified, but production firmware rights, image, provisioning and selected PiSXMe mode are open. |
| Prior “no complete JMS581 evidence” gap | `SUPERSEDED_BY_MANUFACTURER` | Datasheet, schematic, PCB, layout guide, BOM and SPI list now close the evidence-discovery gap. This does not change Path-A selection. |
| PiSXMe JMS581 footprint/net/thermal/procurement contract | `UNRESOLVED` | No promotion or CAD change is justified without Storage/Product, package, SI, firmware and procurement authority. |
| Path-A dual-bridge inactive-state isolation | `PRODUCT_REQUIREMENT_OVERRIDES_REFERENCE` | Preserve the current selected power-off/selectors contract; the single-controller demo does not silently replace it. |

The full machine-readable matrix is in `Library/indexes/jms581dl-manufacturer-packet-20260917.json`.

## Recommendations and boundaries

**Required before any JMS581 promotion:** Storage/Product Authority must decide whether an architecture change is desired; package authority must establish native 144TFBGA symbol/footprint and ball-to-net mapping; SI/Power must translate the guide to the PiSXMe six-layer stack and corrected system power envelope; Firmware authority must establish lawful image/provisioning provenance; DFM/procurement must qualify assembly and supply. Any resulting CAD must be an isolated producer candidate followed by serialized integration and fresh KiCad Light validation.

**Reference-only recommendations:** Retain the datasheet rail/timing/current facts, local bypass and reference-plane guidance, SPI support list, and manufacturer placement/transition observations as inputs to those authorities. Do not import the four-layer dimensions or reference-board topology verbatim.

No CAD was changed, no JMS581 was added to the public development repository, and no hardware operation, vendor authorization, or production readiness is claimed.
