# PiSXMe Phase 24 component, firmware, programming, and procurement evidence

**Scope:** selected integrated Path A dual-mode storage implementation and
critical supporting components for the Phase 24 acceptance row
`component_firmware_provenance`. **Retrieved:** 2026-09-13. **Owner:**
Librarian. This is an evidence brief; it does not make architecture or release
decisions.

## Authority result

The records agree that Path A is the selected production implementation:
TUSB9261 SATA plus JMS583 NVMe behind the HD3SS6126/HD3SS3412 selectors and
TE M-key socket. The RTL9210B-CG material is an isolated, unpromoted Path-B
alternative and is excluded from this acceptance row. No Path-B procurement,
firmware, or production-integration gate is required for Phase 24.

The current corpus is sufficient to identify the intended parts, package and
pin authorities, the baseline firmware policy, and the permitted programming
routes. It is not sufficient to close production procurement and provisioning
readiness. No purchase, authorization, hardware programming run, or vendor
approval is claimed.

## Evidence matrix

| Ref / function | Selected identity and evidence | Current disposition and remaining closure evidence |
|---|---|---|
| U7 SATA bridge | TI `TUSB9261IPVP`, 64-pin PVP/HTQFP. `SATA_BRIDGE_AUTHORITY.md`, TI Rev-I datasheet, Rev-E implementation guide, DEMO guide, `TUSB9261_FIRMWARE_RECEIPT.md`, and the TI product page establish identity, package, SATA Gen1/2, UASP/BOT, and the firmware resource family. The exact part has prior DigiKey/Mouser records. | Component authority and technical procurement basis are CLOSED at planning level. The Rev-A firmware policy is TI SLLC416 (U1/U2 disabled); SLLC414 is the FlashBurner utility. TI's E2E engineer states that SLLC416 lacks the SPI-valid header and must be formatted with FlashBurner for raw SPI programming, and that the correct no-swap image must match the board's SATA polarity. Before release, retain the permitted image/version metadata, formatted-image hash if lawfully retained, FlashBurner version, no-swap configuration, rights/access disposition, and a reproducible programming record. The gated TI downloads and absent board programming run remain OPEN. |
| U11 NVMe bridge | JMicron `JMS583-QHFA3A`, QFN64 8x8. JMicron PDB-18001 Rev 1.00 and PDS-17001 Rev 2.1 establish the pin map, package, mask-ROM baseline, support circuit, SPI-NVRAM purpose, and USB/PCIe behavior. `JMS583_DESIGN_AUTHORITY.md` is the project interpretation. | Firmware prerequisite for baseline operation is CLOSED: the selected mask-ROM device does not require project-supplied firmware; optional SPI NVRAM is DNP. Future updates require a JMicron-authorized image/tool. Exact JLC `C25701682` assembly identity is recorded, but captured stock was zero; broker listings are not authorized supply. Traceable prototype-quantity procurement, lifecycle/suffix confirmation, and any future image rights remain OPEN/HIGH. |
| U12/U13 selectors | TI `HD3SS6126RUAR` and `HD3SS3412RUAR`, both RUA0042A WQFN families with separate signal tables. `SELECTOR_PACKAGE_REVIEW.md` and retained TI datasheets provide package, pin, and truth-table authority. | No firmware or device programming is required. Exact identity and technical package evidence are present; distributor availability snapshots are dated planning evidence. Refresh exact-MPN procurement before BOM release. The separate U12 retained footprint's 0.40-mm pitch versus TI's 0.50-mm package drawing is a live package-authority conflict recorded in the storage geometry brief and must not be silently waived or treated as closed by this row. |
| U14 mode control | `SN74LVC1G17DBVR`, TI datasheet and project mode matrix. | No firmware/programming. Exact final BOM/procurement capture and native mode behavior remain implementation/validation work. |
| J3 M-key socket | TE `1-2199230-4`, TE application specification Rev C, customer DXF and `TE_MKEY_AUTHORITY.md`. | Mechanical/electrical identity is evidenced. Exact customer CAD/pad parity and current traceable procurement remain separate open gates; do not infer them from a nearby JAE or B-key part. |
| J1 SXM2 receptacle | Amphenol/FCI `74221-101LF`, product page and Rev-W drawing, plus private SXM2 reverse-engineering brief and project J1 reassessment. | Manufacturer identity/geometry and project net contract are recorded. Procurement has a prior medium/high snapshot; refresh before BOM release. Reverse-engineered electrical mapping is evidence, not NVIDIA authorization. V100 undocumented behavior remains `REV_A_EMPIRICAL_RISK`. |
| CM5 and service/ethernet connectors | Raspberry Pi CM5IO Rev 2 archive and component authority; Amphenol `10164227-1001A1RLF`; selected EDAC `A70-112-331N126`; Amphenol `10171746-00021LF`. | Identity and local reference evidence are present. Exact selected EDAC footprint/model and current selected-BOM procurement/assembly records must be reconciled at release. CM5 module firmware and host software are external product inputs and are not represented as passed hardware validation. |
| Power/protection | TI `TPSM63606RDLR`, `LM74700QDBVRQ1`, Microchip/Molex/Littelfuse/CSD/TVS records under `authority-inventory/primary-docs/`. | Manufacturer/package evidence exists for the selected families. Exact BOM values, lifecycle/lot traceability, current procurement, regulator reference-layout compliance, and physical rail validation remain owned by the corresponding Phase 24 rows. |

## Newly indexed provisioning clarification

TI E2E thread **TUSB9261 Flash Burner**, thread 538818, contains a response
from TI expert Jorge Llamas. It says the TUSB9261 EVM is not required for SPI
programming, the SLLC416 firmware download does not contain the header needed
for device recognition, and FlashBurner must generate the formatted image for
other SPI programming methods. It also warns that the firmware SATA polarity
must match the board and states a minimum reset interval. This is TI support
engineering guidance, not a replacement for the datasheet or an authorization
for redistribution. See source ID `ti-e2e-tusb9261-flashburner-538818`.

## Closure packet for the acceptance owner

To close `component_firmware_provenance` on the validated integrated
candidate, the acceptance owner must attach to the exact candidate SHA:

1. a selected-BOM manifest with exact MPN, package, footprint/model provenance,
   lifecycle and traceable procurement disposition for U7, U11, U12, U13, U14,
   J1, J3, J7, and the power/protection critical parts;
2. the TUSB9261 SLLC416/SLLC414 version metadata and access/rights record,
   explicit no-swap polarity choice, formatted-image hash or a documented
   lawful-retrieval command if the binary cannot be retained, and the
   reproducible programmer/tool version;
3. a statement and source citation that baseline JMS583 operation is mask-ROM
   and that the DNP SPI NVRAM is not a boot dependency;
4. explicit dispositions for dated distributor snapshots, broker-only stock,
   and all unresolved package conflicts; and
5. the resulting firmware/programming/procurement readiness receipt, which must
   separate design authority from fabricated-hardware and purchase evidence.

This packet permits the repair campaign to continue. It does not permit a
release claim while JMS583 authorized supply, TUSB provisioning access, and the
U12 pitch conflict remain unresolved. If the plan's approval policy accepts a
residual `REV_A_EMPIRICAL_RISK` disposition for non-hardware provisioning, the
acceptance owner must cite that exact policy rather than silently changing the
row status.

## Sources and boundaries

Project-derived records are in the public development repository under
`authority-inventory/`; the durable metadata and this brief are in the private
Library. Manufacturer and community material is not copied into public
history. Community RTL9210B firmware/configuration files remain isolated and
are not production evidence. Prices and stock are dated observations, not
quotes.
