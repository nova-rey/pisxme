# PiSXMe firmware, configuration, procurement, licensing, and empirical-risk packet

Package: `P24-PROVENANCE-FIRMWARE`  
Base state: `c06876d2bb3c244d29ad04e883a253eefd35c265`  
Scope: evidence and release classification only; no schematic, PCB, rule, or configuration edits.  
Acceptance rows: `INV-FIRMWARE`, `IF-FIRMWARE-CONFIG-BASELINE`, `component_firmware_provenance`.

## Result

The selected production implementation remains Path A: TI `TUSB9261IPVP` for
SATA plus JMicron `JMS583-QHFA3A` for NVMe, with the selected switch and M-key
topology. The evidence establishes component identity, the baseline firmware
policy, and the distinction between design authority and release evidence. It
does not establish production provisioning, current lot traceability, firmware
rights, or fabricated-hardware behavior. Those items remain `UNPROVEN` and
must stay open in Phase 24 acceptance; no claim of vendor authorization or
hardware operation is made.

RTL9210B Path B remains an isolated, unpromoted alternative. Its community
firmware/configuration artifacts are retained only as qualification evidence;
they are `NOT_APPLICABLE` to the selected production contract and must not be
used to close Path-A firmware or procurement rows.

## Evidence identity

| Item | Evidence identity |
|---|---|
| PiSXMe source base | `nova-rey/pisxme`, branch `reva-clean`, base `c06876d2bb3c244d29ad04e883a253eefd35c265` |
| Schematic | `PiSXMe_RevA_Clean.kicad_sch`, SHA-256 `6eef63bd3d2b0b9fafc0150d3c34f636ce24a48b2ecbd3d28a5f0bfec167e9f1` |
| Selected PCB | `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`, SHA-256 `75d2d37063818093429b44dbe4197005c2f94b23554a34947a68acaaa181bf7c` |
| Project/rules | `PiSXMe_RevA_Clean.kicad_pro` SHA-256 `ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356`; `PiSXMe_RevA_Clean.kicad_dru` SHA-256 `38e5c7521d964bfa91ee610dc6b7ca39b767b04b8990e94ea91dfe826d21f6a3` |
| Private Library reference | Prior receipt records `PiSXMe-Library` branch `Library` at `b521af194da4e1455c776132e77f282f5247841c`, brief `ae9132d6072f1557a709f47c542fe3c6d9baac38`; checkout is unavailable in this worker, so those values are retained as prior provenance, not freshly re-read here. |

## Invariant and evidence register

| ID | Requirement and quantitative/configuration boundary | Class | Provenance | Current state | Verification / owner |
|---|---|---|---|---|---|
| `IF-FIRMWARE-CONFIG-BASELINE` | Path-A SATA bridge shall use a traceable TI firmware/configuration path. The selected policy is TI `SLLC416`, version `01.00.00.0M`, U1/U2 disabled; `SLLC414`, version `01.00.00.0E`, is the FlashBurner utility. Raw `SLLC416` is not a release artifact until the gated download, image hash, rights, polarity/configuration record, and programming procedure are retained. | B | `authority-inventory/primary-docs/bridge/SATA_BRIDGE_AUTHORITY.md` SHA-256 `87b1ba01924480d2c8dbbe086d02bc979a780f5355ec1243f89177fd3ddc2fc1`; `authority-inventory/primary-docs/bridge/TUSB9261_FIRMWARE_RECEIPT.md` SHA-256 `297154baa6ebfffd4230739081d0b5db5bc38c70d5b5712551ceee431731e04e`; TI product/download records cited there. | **UNPROVEN for release; source policy established.** No gated binary, formatted image hash, rights record, exact FlashBurner run, or board programming receipt is retained. | Firmware/Provenance Authority: retain lawful image/config hash, tool/version, polarity, access/rights, and reproducible programming receipt; then validate USB/SATA behavior on the selected CM5/SSD. |
| `IF-FIRMWARE-JMS583-MASKROM` | Selected `JMS583-QHFA3A` uses its factory mask-ROM baseline; optional SPI NVRAM is DNP and is not a Rev-A boot dependency. No unverified project firmware image may be introduced. | B | `authority-inventory/primary-docs/storage-upgrade/jms583/JMS583_DESIGN_AUTHORITY.md` SHA-256 `5285cdf2e0e894970aee4565fe24d6f0d7b80b376bba6e51ceb58c3bd50f290a`; retained JMicron PDB/PDS records and `validation-receipts/firmware-provenance-independent-20260913/RECEIPT.md`. | **PASS for baseline design policy; UNPROVEN for release.** Exact suffix/lifecycle/prototype lot and functional SSD behavior remain open. | Storage/Firmware Authority: exact MPN/suffix/lot traceability, then actual bridge/SSD UASP/BOT/TRIM/reset/suspend/cold-cycle validation where required. |
| `INV-PATHA-PROCUREMENT-TRACEABILITY` | Every selected critical part must have exact MPN/suffix, lifecycle/source, lot or authorized prototype procurement, and a release-time BOM/assembly record. Dated distributor snapshots are planning evidence only. | B/C | `validation-receipts/firmware-provenance-independent-20260913/RECEIPT.md`; `authority-inventory/PHASE2_PROCUREMENT_MATRIX.md`; selected component authority records. | **UNPROVEN.** TUSB9261 has dated DigiKey/Mouser observations; JMS583 exact assembly identity is recorded but captured stock was zero; selectors/connectors require release refresh. | Procurement/Release Authority: refresh exact records at release and retain purchase/lot/assembly evidence. No broker listing substitutes for authorization. |
| `INV-FIRMWARE-RIGHTS` | PiSXMe may retain references and hashes, but may release or redistribute firmware/configuration only with documented lawful access and rights. | B/C | TI download pages are export-gated in `TUSB9261_FIRMWARE_RECEIPT.md`; community RTL9210B artifacts and rights limits are recorded in `authority-inventory/rtl9210b/RTL9210B_FIRMWARE_PROGRAMMING_MATRIX.md` SHA-256 `4a8ab55bbcc908fe4b8e88ad1f372bf39a1bb4251b4d3595846332c37198e3f0`. Manufacturer documentation is retained under its stated terms; no proprietary binary is copied into this packet. | **UNPROVEN.** No release authorization or redistribution grant is recorded for gated TI payloads, JMicron future images, or community Realtek artifacts. | Librarian + Release Authority: retain license/access disposition and release only lawful references or user-supplied authorized payloads. |
| `INV-EMPIRICAL-V100-BEHAVIOR` | Undocumented V100/SXM2 endpoint behavior remains `REV_A_EMPIRICAL_RISK`: power/reset timing and enumeration, actual PCIe endpoint operation, thermal/cold-cycle response, and any behavior absent from retained public authority require an explicitly bounded hardware validation or remain unproven. | B/F (with C product impact) | `validation/phase3/PHASE4_V100_RECEIPT.md`; `validation/phase3/PHASE4_SXM2_MAPPING_RECEIPT.md`; `PHASE14_MATERIALIZATION_STATUS.md`; `authority-inventory/primary-docs/mechanics/V100_COOLER_BACKPLATE_AUTHORITY.md`; current hostile/provenance receipts. | **UNPROVEN / accepted empirical-risk boundary.** No fabricated V100 carrier or vendor authorization is available in this lane; design analysis and source evidence do not equal bench proof. | V100/PCIe + Power/Thermal Authorities: bind documented tests and disposition; do not convert analysis, fixture, or reverse-engineered mapping into hardware PASS. |
| `INV-STORAGE-BRINGUP-BEHAVIOR` | Selected Path-A storage must eventually demonstrate the declared bridge/SSD behavior, including enumeration, UASP/BOT as applicable, TRIM/discard where claimed, reset, suspend/resume, and cold power-cycle recovery on the actual CM5 image and selected SSD. | B/D | `authority-inventory/primary-docs/bridge/TUSB9261_FIRMWARE_RECEIPT.md`; `authority-inventory/primary-docs/storage-upgrade/jms583/JMS583_DESIGN_AUTHORITY.md`; `PHASE24_STORAGE_UPGRADE_QUALIFICATION.md`; JMicron datasheet text documents capabilities but not PiSXMe operation. | **UNPROVEN.** Manufacturer capabilities and baseline policy are not an integrated or fabricated-board result. | Storage/Bring-up Authority: run only on an assembled candidate when available; retain commands, software/image identity, logs, and limits. |
| `INV-RTL9210B-PATHB-FIRMWARE` | RTL9210B firmware/configuration/procurement is not a dependency of selected Path-A production closure. | E (scope disposition; supported by B evidence) | `authority-inventory/rtl9210b/RTL9210B_PATHB_AUTHORITY.md` SHA-256 `428f30154052ca89a7dbd166b38efcfa8e918874976a6307dc2efad00474645f`; `authority-inventory/rtl9210b/RTL9210B_FIRMWARE_PROGRAMMING_MATRIX.md`; current Path-A/Path-B authority records. | **NOT_APPLICABLE** to selected production acceptance. Preserve isolated evidence; do not promote, merge, or use it to satisfy Path-A rows. | Root + Storage Authority: queue/scope review only. |

## Explicit boundary and queue consequence

Closed by this packet: selected Path-A identity, Path-A versus Path-B scope,
baseline TUSB9261 image/tool policy, baseline JMS583 mask-ROM policy, and the
provenance rule that manufacturer/community artifacts are not automatically
licensed release material.

Still open: exact lawful TUSB9261 download/provisioning record; exact JMS583
prototype procurement and lifecycle/suffix traceability; release-time exact
MPN/lot records for critical parts; integrated storage behavior; and empirical
V100/SXM2 behavior. These are `UNPROVEN` acceptance dependencies, not an
external claim that the engineering organization cannot proceed. They should
remain owned by firmware/provenance, procurement/release, storage bring-up,
and V100/power authorities respectively. No CAD implementation package is
unblocked by this evidence alone.

This packet does not close `INV-FIRMWARE`, `IF-FIRMWARE-CONFIG-BASELINE`, or
`component_firmware_provenance`; it narrows their exact closure criteria and
preserves the `REV_A_EMPIRICAL_RISK` boundary. It does not require RTL9210B
production work.

## Reproduction and non-claims

The evidence basis can be reproduced with:

```sh
git -C /home/nyx/PiSXMe/pisxme/reva-clean rev-parse HEAD
sha256sum PiSXMe_RevA_Clean.kicad_sch PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb \
  PiSXMe_RevA_Clean.kicad_pro PiSXMe_RevA_Clean.kicad_dru
sha256sum authority-inventory/primary-docs/bridge/TUSB9261_FIRMWARE_RECEIPT.md \
  authority-inventory/primary-docs/bridge/SATA_BRIDGE_AUTHORITY.md \
  authority-inventory/primary-docs/storage-upgrade/jms583/JMS583_DESIGN_AUTHORITY.md \
  authority-inventory/rtl9210b/RTL9210B_FIRMWARE_PROGRAMMING_MATRIX.md
```

No fabricated board, V100 module, current procurement transaction, vendor
authorization, firmware download entitlement, programming run, or hardware
measurement was observed or claimed. The packet is suitable as an invariant
audit input and does not assert Phase 24 or Phase 25 completion.
