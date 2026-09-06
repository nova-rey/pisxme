# Phase 24 storage-island upgrade blocker

Status: `OPEN — implementation authorized; procurement evidence remains HIGH
risk` for the authorized SATA/NVMe upgrade only.
The prior SATA-only board is preserved.

## CURRENT LIVE STATE — 2026-09-06

This file is an open-risk record, not a terminal blocker. The authoritative
schematic already contains the JMS583 branch, both selectors, TE M-key J3,
JMS583 clocks/rails/reset/decoupling/USB-PCIe support, and J5/U14 mode
control. The current library audit passes for the 64-pad JMS583 QFN, TI
selector packages, and TE M-key contact pattern. Structural schematic,
mode-contract, and JMS583-support audits pass.

The active native route candidate is still unfinished. The corrected-package
USB3 fixture's latest report is
`PHASE24_DUAL_MODE_STORAGE_USB3_ISOLATED32-drc.rpt`: the authored paths have
no track-width or track-crossing findings, one TX source-via short, and 78
unconnected items
because the fixture intentionally omits most support circuitry. Native ERC,
complete switched-mode DRC/connectivity, TE pad/model parity, and integrated
storage validation remain open. No Phase 24 resumption or completion is
claimed.

Current blocker/risk classification:

- `JMS583_AUTHORIZED_PROTOTYPE_SUPPLY`: procurement risk remains HIGH/OPEN;
  JLC's retained exact listing showed zero stock, and broker listings are
  corroborating rather than authorized release supply.
- TE M-key pad/courtyard/model parity: implementation review remains OPEN;
  the B-key J3 has been replaced in schematic authority and the candidate
  footprint has passed only the structural contact-count audit so far.
- USB3/native storage routing and complete mode validation: active engineering
  gates, not external blockers.

The corrected JMS583 pin authority and 64-pad library supersede all earlier
42-pad/U11 geometry and route results; those artifacts remain historical
evidence only.

## SUPERSEDED HISTORICAL SNAPSHOT — not current instructions

## Exact unresolved items — historical snapshot at this checkpoint

`JMS583_AUTHORIZED_PROTOTYPE_SUPPLY`; TE M-key footprint authoring/parity is
the remaining local implementation gate.

ASM2362 is rejected, but it is no longer the only candidate. Bounded research
qualified JMS583's exact QFN64 pin assignment, land-pattern dimensions,
support values and power timing from JMicron's detailed Rev 2.1 datasheet.
JLCPCB lists exact `JMS583-QHFA3A` (`C25701682`, about $6.06 qty 1, minimum 1,
SMT), but currently reports zero stock; broker stock is corroborating only.

The firmware prerequisite is now closed for baseline operation: the
manufacturer ordering code includes a mask-ROM version, and the selected
device is factory programmed. External SPI NVRAM is documented for optional
VID/PID customization and is DNP in Rev A. Firmware update remains an
authorized future-maintenance path, not a design dependency. Authorized
prototype supply is still not demonstrated; JLC currently reports zero stock
and broker listings are not sufficient release evidence.

## Why production implementation stops

The NVMe bridge owns the USB and PCIe sides of the new path. JMS583's pads and
reference component values are now reviewable; baseline design may proceed
with factory mask-ROM operation. No mystery firmware or PCB-only repair is
permitted.

TE `1-2199230-4` is an eligible replacement: TE identifies it as Active, M
code, 67-position, 4.2-mm SMT and publishes application specification Rev C.
The exact TE customer CAD is now retained locally; native footprint pad,
courtyard and model parity must be completed before replacing J3. Existing
`SM3ZS067U410ABR1000` remains B-key-only.

## Sources checked

- JMicron official JMS583 product/solution page, official product brief,
  detailed Rev 2.1 datasheet, and official download center.
- JLCPCB exact JMS583-QHFA3A page and multiple broker stock snapshots.
- TE exact M-key product page, TE Rev C application/product specifications,
  and DigiKey exact MPN page.
- ASMedia ASM2362 official product page and JLCPCB assembly listing.
- JMicron's official JMS581DL product page/Product Brief and JLCPCB
  144TFBGA assembly listing were checked as a simpler one-chip alternative;
  its ball map/design pack/firmware path are not public.
- Realtek RTL9210B community firmware/reference ecosystem and searches for
  manufacturer documentation; no better authoritative bare-chip path found.
- TI TUSB9261/switch authorities and existing project firmware records.

All captures are retained under `authority-inventory/primary-docs/storage-upgrade/`.
No purchase was made.

## Shortest human action

Obtain an authorized prototype quote or traceable factory-programmed
`JMS583-QHFA3A` supply. The baseline design can proceed without a firmware
binary; external SPI NVRAM remains optional/DNP. Finish the native TE M-key
footprint parity check for `1-2199230-4` before replacing J3.

## Continuation options

1. Recommended: obtain JMS583 prototype supply confirmation and finish TE
   customer-CAD footprint parity, then implement the storage island and resume
   Phase 24.
2. Use a factory-programmed complete USB-to-NVMe module only if its exposed
   interfaces, firmware provenance and socket-side integration are documented.
3. Dropping dual-mode storage would retain the old SATA-only board, but that
   is a user architectural decision and is not assumed.

## Current implementation audit — 2026-09-06

The implementation path has since been advanced in the working tree:

- `STORAGE.kicad_sch` contains the TE M-key socket, JMS583-QHFA3A, and the two
  TI selectors. The JMS583 embedded symbol now reflects the detailed table,
  including REXT pin 39, AVDD33 pin 19, all AVDDL/VCCO/VCCK pins, GPIO/SPI
  optional pins, reset, crystal, and LXO.
- `phase24_dual_mode_storage_schematic_audit.py`, the library audit, and the
  mode-contract net-label audit pass. A removed-label negative control fails.
- Native KiCad netlist export parses successfully. Native ERC still reports
  201 violations, so this is not a release schematic.
- The native PCB candidate is placement-only and remains unrouted; its last
  native report recorded 1,013 violations and 482 unconnected items. It is not
  an integrated-board PASS.

The remaining engineering blockers are now explicit rather than generic
documentation objections:

## Current implementation state — 2026-09-06

The documentation-only stop condition has been superseded by an authorized
implementation checkpoint. `ea8dfb6`/`7938f64`/`7dbf709` added the JMicron
support network, J5/U14 mode control, project-local support footprints, and
native audits. The latest structural audits and schematic netlist export pass.
Native ERC remains open at 407 findings, and the disposable PCB candidate is
placement-only with 1,074 DRC violations and 499 unconnected items. These are
active implementation gates, not a terminal blocker. The next required work
is a correct routed native fixture, mode-aware selected-path/inactive-state
validation, and exact TE CAD pad/courtyard/model parity.

The attempted consultant review could not run because the orchestration thread
limit is currently exhausted; no engineering decision is based on that
failure.

1. Contact 69 is named CONFIG1 in retained TP-053 and is identified as the
   PEDET/interface-detect contact by the older Socket 3 definition: SATA
   grounds it and PCIe/NVMe leaves it open. AUTO therefore needs the documented
   Schmitt-qualified, power-off mode-control implementation; DAS/DSS is not
   used as a detector.
2. At that earlier checkpoint, the JMS583 support network was represented as
pin authority but still needed
   native component instances and physical support routing: 25-MHz crystal,
   REXT, AVDD33 capacitor, LXO inductor, reset RC, VBUS divider, decoupling,
   and the documented AC coupling capacitors.
3. The complete switched-mode native fixture, including inactive-state
   isolation and forced SATA/NVMe cases, has not yet passed DRC/connectivity.
4. TE customer CAD is retained, but its pad-by-pad native coordinate audit,
   courtyard, and 3D model release review remain open.

This report therefore remains `OPEN`; no Phase 24 resumption or completion is
claimed. The corrected JMS583 pin authority also supersedes any earlier
intermediate map that called pin 12 REXT.
## Follow-up implementation evidence — 2026-09-06

Native inspection found inherited C44-C47 reference collisions in the
disposable acreage candidate. JMS583 support was moved to collision-free
references C80-C93, R80-R83, L10, and Y10; SERVICE J4 and storage mode J5 are
now distinct. A first disposable native support-routing pass saved 14
low-speed pad-to-pad connections and loaded natively. Its DRC reports 1,158
violations and 499 unconnected items because high-speed and remaining support
paths are unfinished. This is route implementation progress, not a blocker
claim or closure evidence.
