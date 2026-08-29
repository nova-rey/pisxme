# PiSXMe reference index

This index is the handoff map for the Linux workstation. “Authoritative” means
manufacturer/standards-owner material; “secondary” means a real implementation
used to corroborate topology; “empirical” means community hardware evidence.
Copyright and license terms must be checked before redistributing anything not
already included in this repository.

## Raspberry Pi / CM5

| Reference | Local path | Source | Class / decision supported |
|---|---|---|---|
| Compute Module 5 datasheet | `references/cm5/cm5io-datasheet.pdf` | <https://datasheets.raspberrypi.com/cm5/cm5-datasheet.pdf> | Authoritative; CM5 pin, power, USB, Ethernet, PCIe and mechanical contracts. |
| Official CM5IO Rev 2 source | `references/RaspberryPi-CM5IO-rev2/` and `references/cm5/official-cm5io-rev2/` | <https://github.com/raspberrypi/cm5io> | Authoritative implementation; Ethernet/MagJack, USB, M.2, stackup and placement philosophy. |
| CM5IO high-speed schematics | `references/RaspberryPi-CM5IO-rev2/CM5_HighSpeed.kicad_sch`, `PCIe-M2.kicad_sch` | same repository | Authoritative; pair mapping and reference-plane practice. |
| CM5IO 3-D/footprint assets | `references/RaspberryPi-CM5IO-rev2/CM5IO.pretty/`, `CM5IO.3dshapes/` | same repository | Authoritative source files; retain upstream notices. |
| CM5IO datasheet/source manifest | `references/cm5/SOURCE_MANIFEST.md`, `references/cm5/official-cm5io-rev2/SOURCE_MANIFEST.md` | upstream repository | Provenance and checksum notes. |
| CM5MiniITX | `references/cm5/cm5MiniITX/` | upstream project linked from its README | Secondary validated CM5 carrier; use only to corroborate placement and serviceability. |
| ModuCard CM5 | `references/cm5/moducard-cm5-module/` | upstream URL in `README.md` | Secondary/open hardware; corroborates Ethernet and power patterns. |

## PCIe / V100 / SXM2

| Reference | Local path | Source | Class / decision supported |
|---|---|---|---|
| V100 datasheet | URL and retrieval details to be recorded before Linux work | NVIDIA V100 product documentation portal | Authoritative; package, power and thermal limits. The private standalone-SXM2 sequencing document is not available. |
| SXM2 connector manufacturer material | `references/manufacturer/Amphenol_74221-101LF/` | Amphenol product page (see local README) | Authoritative; land pattern, mating and assembly. |
| SXM2 pin and signal map | `references/SXM2_PIN_MAP.csv`, `SXM2_SIGNAL_MAPPING.json` | project-derived from connector/OEM evidence | Engineering record; verify against connector and platform evidence. |
| LiuXinyu SXM2-to-PCIe carrier | `references/LiuXinyu12378-SXM2_to_PCIE_adapter/` | upstream URL in `readme.md` | Empirical; supports the standard PCIe endpoint basis, not NVIDIA sequencing authority. |
| SXM2-to-PCIe open carrier | `references/SXM2toPCIe/` | upstream URL in `README.md` | Empirical/secondary; used for pin and mechanical corroboration only. |
| PiSXMe PCIe evidence | `design/PCIE_X1_*`, `design/V100_STANDARD_PCIE_DESIGN_BASIS.md` | project records | Engineering decision; preserve PER0 and the approved Gen2 x1 basis unless contradictory evidence appears. |

## USB, SATA and high-speed layout

| Reference | Local path | Source | Class / decision supported |
|---|---|---|---|
| TI USB high-speed layout guidance | `references/usb3/TIDA-00987/SLLA414A-high-speed-layout-guidelines.pdf`, `SLLA414-high-speed-layout-guidelines.pdf` | TI product documentation | Authoritative; impedance, return paths, via transitions and connector breakout. |
| TI TIDA-00987 design package | `references/usb3/TIDA-00987/` | TI reference design portal | Authoritative reference design; USB3 mux/ESD topology and layout methodology. |
| TPD4E05U06 / USB ESD | `references/manufacturer/TI_USB/derived-footprints/`, `tpd4eusb30.pdf`, `references/usb3/TIDA-00987/TPD4E05U06-datasheet.pdf` | TI | Authoritative; pin mapping, capacitance and connector-side placement. |
| EEWorld JMS578/M.2 board | `references/jms578-ee-world/` | <https://en.eeworld.com.cn/Reference_Designs/detail/5f3ad50c> | Secondary real hardware; JMS578 USB3-to-SATA, B-key M.2 mapping, power/reset/clock and routing pattern. |
| MiSaKa JMS578 cage | `references/jms578-misaka/` | <https://github.com/MiSaKa100039/2.5-inch-USB-SATA-HDD-Cage> | Secondary/empirical; corroborates JMS578 support, firmware/configuration, clock and reset practice. |
| JMS578 documentation | URL to be recorded with the exact vendor revision | JMicron product/support material | Authoritative where obtained; verify UAS, firmware, power and package availability. |
| ASM1153 alternative | URL/retrieval details to be recorded if evaluated | ASMedia product/support material | Authoritative fallback; do not select without current procurement and Linux evidence. |
| SATA-IO M.2 mapping | retrieval URL to be recorded with the licensed revision | <https://www.sata-io.org/> | Standards authority; B/B+M SATA pin mapping and keying. Do not infer SATA from an M-key NVMe socket. |
| M.2 socket manufacturer data | `references/RaspberryPi-CM5IO-rev2/CM5IO.pretty/M.2 M Key socket.kicad_mod` plus selected vendor datasheet to be added | connector vendor page | Authoritative for the exact selected socket; verify keying, height, retention and single/double-sided clearance. |

## Ethernet

| Reference | Local path | Source | Class / decision supported |
|---|---|---|---|
| CM5IO Ethernet implementation | `references/RaspberryPi-CM5IO-rev2/CM5_HighSpeed.kicad_sch`, `CM5IO.kicad_pcb`, `TRJG0926HENL.kicad_mod` | Raspberry Pi CM5IO source above | Authoritative primary source; CM5 PHY pair ordering, MagJack center taps, ESD/shield and 100-ohm routing. |
| TRJG0926HENL MagJack model | `references/RaspberryPi-CM5IO-rev2/CM5IO.3dshapes/`, `CM5IO.pretty/` | Würth/connector manufacturer data as cited by CM5IO | Authoritative for the chosen footprint/body; recheck lifecycle and mechanical envelope. |
| Ethernet ESD guidance | selected vendor application note to be added with exact part | TI/Littelfuse/connector vendor | Authoritative; low-capacitance placement and shield/return strategy. |

## Power and protection

| Reference | Local path | Source | Class / decision supported |
|---|---|---|---|
| TPSM63606 datasheet | `references/manufacturer/TI_power_parts/TPSM63606.pdf` | TI | Authoritative; complete FB/RT/PG, decoupling, SW loop, AGND/PGND and thermal layout. |
| LM74700-Q1 | `references/manufacturer/TI_power_parts/LM74700-Q1.pdf` | TI | Authoritative; reverse-polarity/ideal-diode front end. |
| High-current MOSFET | `references/manufacturer/TI_power_parts/CSD19536KCS.pdf` | TI | Authoritative; conduction/thermal and gate-drive selection. |
| Mini-Fit Jr / power connectors | manufacturer docs summarized in `design/HIGH_CURRENT_COPPER_REQUIREMENTS.md` | Molex product documentation | Authoritative; current, mating, plating and mechanical support. |
| Fuse/holder | `references/manufacturer/Littelfuse_1786165/` | Littelfuse | Authoritative; holder land pattern, rating and service access. |
| TVS/bulk selection | `design/POWER_INPUT_FINALIZATION.md`, `design/POWER_BUDGET_AND_CURRENT_PATHS.md` | vendor datasheets to be cited per selected part | Engineering basis; do not add protection without a defined transient/inrush requirement. |

## Manufacturing and fabrication

| Reference | Local path | Source | Class / decision supported |
|---|---|---|---|
| JLC six-layer stackup | `references/manufacturer/JLCPCB_JLC06161H-7628/stackup-api.json`, `manufacturing/FAB_STACKUP_COMPARISON.md` | JLCPCB stackup/fabrication pages | Authoritative fabrication basis; impedance and plane roles. |
| Manufacturer-derived footprints | `references/manufacturer/` | component manufacturers | Authoritative for package-to-land-pattern checks; preserve README provenance. |
| JLC impedance/current guidance | `design/PCIE_IMPEDANCE_GEOMETRY.md`, `manufacturing/FABRICATION_PARAMETERS.md` | JLCPCB fabrication guidance | Authoritative/engineering record; revalidate against the selected order stackup. |
| IPC design practice | citations embedded in the approved plan and design reports | IPC standards portal | Standards authority; use the licensed current revision where a numerical acceptance limit is needed. |

## Software/tooling references

| Reference | Local path | Source | Class / decision supported |
|---|---|---|---|
| KiCad IPC developer documentation | external URL recorded in tooling report | <https://dev-docs.kicad.org/en/apis-and-binding/ipc-api/for-addon-developers/> | Authoritative; explains why current IPC is PCB-first and why schematic authority needs a separate path. |
| kicad-sch-api | dependency declaration in `pyproject.toml`, spike wheel in `work/sch-api-spike/` | <https://github.com/circuit-synth/kicad-sch-api> | Third-party tooling candidate; MIT; KiCad 10 and round-trip fidelity remain gates. |
| SKiDL | source fixtures in `experiments/skidl/` and `work/skidl_spike/` | <https://github.com/devbisme/skidl> | Third-party netlist generator; MIT; flat mapping worked, hierarchy/authority did not close on Mac. |

Large upstream archives, firmware binaries, generated Gerbers, lock files,
and virtual environments are intentionally not mirrored here. The source URL,
local checksum where available, and exact retrieval target must be recorded
before adding any such artifact.
