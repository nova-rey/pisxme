# PiSXMe Rev A clean rebuild — Phase 2 authority inventory

Date: 2026-08-29  
Status: `PHASE_2_BLOCKED_PENDING_EXACT_AUTHORITIES`

This inventory records what is authoritative, what is merely secondary, and
what remains insufficient to freeze a clean schematic. No production
connectivity or placement was created from these records.

## Materialized primary records

| Authority | Local evidence | Status / limitation |
|---|---|---|
| Raspberry Pi CM5 datasheet | `primary-docs/cm5io-datasheet.pdf`, SHA-256 `ca45baa18ff67d39ae58b05454f7ce229451ff077befdea606e7e708ecc83cb1` | AVAILABLE; use for CM5 pin, PCIe, USB and mechanical contracts. |
| Raspberry Pi CM5IO Rev 2 design archive | `cm5io-rev2/`, extracted from `references/recovered_online/CM5IO_rev2.zip`, archive SHA-256 `48b14a6757b0edc0ac110331445f35a4212b5ce432bdcec6605c99431b59496b` | AVAILABLE; 30-file archive includes source schematics/PCB, official reference symbols/footprints, CM5, MagJack and MTSSD03-67MSW337 models. It is reference authority, not clean-project geometry. |
| JMicron JMS578 product brief | `primary-docs/JMS578.pdf`, SHA-256 `3c59d77780a50314462e8967ec91e9fe532d1356becd31a7b9945b66410e1ae0` | AVAILABLE, revision 1.0.0; confirms USB 3.1 Gen1→SATA 6Gb/s, UASP, 30 MHz crystal, QFN48 and internal regulators. Firmware package, pin-level design guide, procurement and Linux UAS validation remain open. |
| TI regulator/protection/HS documents | `primary-docs/TPSM63606.pdf` (Rev B), `LM74700-Q1.pdf` (Rev G), `CSD19536KCS.pdf` (Rev C), `TPD4E05U06.pdf` (Rev O), `HD3SS3212.pdf` (Rev F) | AVAILABLE for package/electrical/layout requirements; selected BOM, exact footprints and vendor CAD still require independent clean-library validation. |
| NVIDIA V100 datasheet | `primary-docs/NVIDIA-Tesla-V100-datasheet.pdf` | AVAILABLE for product power/thermal context only; it does not close the standalone SXM2 PCIe endpoint/sequencing contract. |

## Authority status by required block

| Block | Status | Evidence and remaining gate |
|---|---|---|
| CM5 / CM5IO | `AVAILABLE_FOR_RECONCILIATION` | Official CM5IO Rev 2 source and CM5 datasheet are present. Extracted reference pin maps must be reconciled into a clean interface ledger without copying layout. |
| JMS578 bridge | `NOT_CLOSED` | JMicron brief is primary but incomplete for firmware/configuration, exact package land pattern, procurement/lifecycle and Linux UAS behavior. The EEWorld and MiSaKa captures are one secondary lineage and cannot fill those gaps. ASM1153E is not evaluated. |
| SATA/M.2 mapping | `NOT_CLOSED` | Public SATA-IO M.2 material establishes the format/keying context, but the exact licensed revision and selected B-key SATA socket data are not locally recorded. The CM5IO MTSSD03-67MSW337 model is an implementation clue, not vendor land-pattern authority. |
| M.2 socket / retention | `NOT_CLOSED` | CM5IO archive includes `MTSSD03-67MSW337.STEP` and `M.2 M Key socket.kicad_mod`, but no manufacturer drawing, stack-height/retention specification or confirmed 2280/2242-compatible part record. |
| SXM2 connector | `NOT_CLOSED` | Amphenol product authority identifies 74221-101LF as 400-position, 4 mm, 1.27 mm array; exact part drawing retrieval was HTTP 403 in this environment and the clean land-pattern overlay is still absent. K18/K19 remain unresolved. |
| CM5 mezzanine connector | `PARTIAL` | Official archive contains the reference footprint/STEP for 10164227-1001A1RLF; the selected 10164227-1004A1RLF variant needs exact drawing/height/orientation confirmation before transplant. |
| Ethernet MagJack | `PARTIAL` | Official CM5IO source contains TRJG0926HENL footprint/STEP and the vendor page identifies 10/100/1000Base-T; manufacturer drawing, lifecycle and exact shield/center-tap authority are not locally closed. |
| Ethernet ESD | `NOT_CLOSED` | TI high-speed ESD datasheet is present, but no exact Ethernet ESD MPN/application authority has been selected and recorded. |
| Power/protection | `PARTIAL` | TI controller/MOSFET/regulator authorities are materialized. Exact TVS, fuse/holder, connector terminal derating, current budget and selected BOM records remain open. |
| Cooler/backplate/mechanics | `NOT_CLOSED` | No exact V100 cooler, backplate, mating fastener or enclosure model is present. Existing rectangles are intentional contracts, not fit evidence. |
| Current JLC six-layer stack | `NOT_CLOSED` | JLC’s current public stackup/impedance guidance is recorded in the plan and live web references, but no selected current fabrication stackup/quote/coupon authority is locally frozen. |

## Primary-source URLs checked in this inventory

- Raspberry Pi CM5 datasheet: <https://datasheets.raspberrypi.com/cm5/cm5-datasheet.pdf>
- Raspberry Pi design files: <https://pip.raspberrypi.com/categories/1098-design-files>
- JMicron JMS578 product authority: <https://www.jmicron.com/products/list/1>
- JMicron JMS578 brief: <https://www.jmicron.com/file/download/1055/JMS578.pdf>
- Amphenol 74221-101LF product authority: <https://www.amphenol-cs.com/product/74221101lf.html>
- SATA-IO M.2 technical proposal: <https://sata-io.org/sites/default/files/TP_053v11_SATA31_Mdot2_Card_Format_for_SSDs.pdf>
- JLCPCB impedance guidance: <https://jlcpcb.com/impedance>
- JLCPCB calculator guidance: <https://jlcpcb.com/help/article/user-guide-to-the-jlcpcb-impedance-calculator>

## Gate decision

`BLOCKED_PENDING_EXACT_AUTHORITIES`. Phase 2 cannot pass yet because the
bridge firmware/procurement contract, exact B-key SATA socket authority, exact
SXM2 land pattern, cooler/backplate model, selected Ethernet ESD, and current
fabrication stackup are not all closed. Phase 3 clean schematic synthesis must
not begin until these gaps are resolved or an approved authority disposition
explicitly changes the gate.

## Native source verification

The extracted official CM5IO Rev 2 schematic exported a native KiCad netlist
successfully under KiCad 10.0.5. Native DRC parsed the extracted CM5IO board
and reported 76 violations and 0 unconnected items; this is an observation of
the upstream reference, not a cleanliness claim and not a reason to alter it.
The archive contains exactly 30 files and the materialized primary-documents
directory contains 8 PDFs.
