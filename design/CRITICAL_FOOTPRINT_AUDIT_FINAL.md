# Critical footprint audit — final pre-routing pass

Date: 2026-08-21
Decision: **CLOSED FOR ROUTING; USB CONNECTOR CAD OVERLAY REMAINS A RELEASE GATE**

No fabrication-critical item remains `LIBRARY_ONLY` or `UNRESOLVED`. The
classifications below mean either manufacturer land-pattern authority was
checked directly or the package was checked against the manufacturer
datasheet/reference layout. This is not a final PCBA quote or stencil release.

| Ref / part | Active footprint / status | Classification | Evidence and remaining process note |
|---|---|---|---|
| J1 / Amphenol 74221-101LF | `SXM2_74221-101LF_MANUFACTURER_DERIVED`; 400 pads, 1.27 mm grid | **MANUFACTURER_VERIFIED** | Manufacturer drawing/spec/application spec; see SXM2 land-pattern signoff. Hidden joints require X-ray/AOI and stencil review. |
| J2A, J2B / Amphenol 10164227-1004A1RLF | `CM5_10164227-1004A1RLF_MANUFACTURER_DERIVED`; 2 × 50-pad rows, 0.4 mm pitch | **MANUFACTURER_VERIFIED** | Official 10164227 drawing; 0.20 × 1.50 mm lands, row centers ±1.19 mm in model; instances deliberately rotated 90° mechanically, not mirrored. |
| J3, J4 / Molex 39301082 | `MiniFitJr_8_RA` placement footprint; 2 × 4 positions at 4.20 mm pitch | **DATASHEET_DERIVED_AND_CHECKED** | Molex product/drawing data checked for 8-circuit right-angle family, keying and through-hole assembly intent. Final cable-entry and solder-fill review remains required. |
| J3/J4 mating / Molex 39012085 | cable housing, no PCB land pattern | **DATASHEET_DERIVED_AND_CHECKED** | Mating-housing record checked; it is not a PCB footprint. |
| U1 / TI TPSM63606RDLR | `TPSM63606RDLR_MANUFACTURER_DERIVED`; 20 pads with central PGND 17–20 | **DATASHEET_DERIVED_AND_CHECKED** | TI RDL package drawing and reference layout checked. Thermal-via array and paste segmentation are intentionally deferred to routing/assembly phase. |
| U2, U3 / TI LM74700QDBVRQ1 | `LM74700_DBV` SOT-23-6 | **DATASHEET_DERIVED_AND_CHECKED** | TI DBV package/pin numbering checked. |
| Q1, Q2 / TI CSD19536KCS | `CSD19536KCS_TO220` | **DATASHEET_DERIVED_AND_CHECKED** | TI TO-220 pin order and body/lead orientation checked; heatsink/assembly envelope remains a manufacturing note. |
| F1, F2 / Littelfuse 178.6165.0001 | `ATO_FLR_1786165_0001_MANUFACTURER_DERIVED`; 8 solder holes + central retention NPTH | **DATASHEET_DERIVED_AND_CHECKED** | Official 1786165 drawing checked: 1.4 mm solder holes at ±5.8/±2.3 mm and ±1.25 mm; 2.4 mm retention hole. Eight duplicate-numbered pads are the deliberate parallel-leg grouping for the two-pin fuse symbol. |
| C1, C2 / Murata GRM21BR71H224KA01# | 0805 / 2012 metric | **DATASHEET_DERIVED_AND_CHECKED** | Murata 0805 land-pattern class checked; voltage/DC-bias/SI suitability remains a circuit review item. |
| J5–J7 / Molex 22-23-2041 intent | `Fan_2x2_2.54mm`, 1 × 4 at 2.54 mm pitch | **DATASHEET_DERIVED_AND_CHECKED** | Pin order is documented GND/+12V/TACH/PWM; final shroud/key choice must be confirmed with assembly vendor. |
| J8 / JST B4B-PH-K-S intent | `UART_1x04`, 1 × 4 at 2.0 mm pitch | **DATASHEET_DERIVED_AND_CHECKED** | JST PH pitch and 1×4 land pattern checked; cable/keying remains a harness detail. |
| J9/J10 / Amphenol 10137064-00011LF | `USB_C_FAST_10137064`, 24 contacts, 0.5 mm contact pitch | **DATASHEET_DERIVED_AND_CHECKED** | Official Amphenol product page and drawing URL establish USB3 Gen2, 24P, 5A VBUS, 1.5A GND, 0.8mm PCB and 10k cycles. Local placement model uses the manufacturer drawing family; obtain the vendor CAD overlay before release. |
| J11 / Amphenol 10171746-00021LF | `USB_C_SERVICE_10171746`, 16 contacts | **DATASHEET_DERIVED_AND_CHECKED** | Official Amphenol product page and drawing URL establish USB2 Type-C 16P, 5A, 0.60mm PCB and 10k cycles. Local placement model preserves A/B duplicated USB2 contacts; obtain the vendor CAD overlay before release. |
| U4/U8 / TI TPS25821DSSR | `TPS25821_DSS`, WSON/DSS 12 | **DATASHEET_DERIVED_AND_CHECKED** | TI pin configuration, DSS body and exposed-pad requirements checked from official datasheet. |
| U5/U9 / TI HD3SS3212IRKSR | `HD3SS3212_RKS`, VQFN/RKS 20 | **DATASHEET_DERIVED_AND_CHECKED** | TI RKS pin configuration and high-speed channel numbering checked from official datasheet. |
| U6/U7/U10/U11 / TI TPD4EUSB30 | `TPD4EUSB30_DQA`, USON/DQA 10 | **DATASHEET_DERIVED_AND_CHECKED** | TI package/pinout and two orientation-branch arrays per reversible FAST port checked. |
| U17/U18 / TI TPD2EUSB30A | `TPD2EUSB30A_DQA`, USB2 ESD 10-pad model | **DATASHEET_DERIVED_AND_CHECKED** | TI USB2 companion-pair package/pinout and connector-side placement checked. |
| U12 / TI TUSB320LAIRWBR | `TUSB320LAI_RWB`, X2QFN/RWB 12 | **DATASHEET_DERIVED_AND_CHECKED** | TI package/pinout and DRP/ID behavior checked. |
| U13 / TI TPS2553DBVR | `TPS2553_DBV`, SOT-23/DBV 6 | **DATASHEET_DERIVED_AND_CHECKED** | TI DBV package/pinout and ILIM pin checked. |
| U14 / TI SN74LVC1G04DCKR | `SN74LVC1G04_DCK`, SC70/DCK 5 | **DATASHEET_DERIVED_AND_CHECKED** | TI DCK package/pinout checked. |
| U15 / TI TPD2EUSB30A | `TPD2EUSB30A_DQA` | **DATASHEET_DERIVED_AND_CHECKED** | TI USB2 ESD package family checked; exact vendor CAD overlay remains a release gate. |
| U16 / TI TPSM63606RDLR | `TPSM63606_USB` | **DATASHEET_DERIVED_AND_CHECKED** | Same manufacturer-derived RDL0020 package basis as U1; dedicated USB rail placement added without changing U1 topology. |
| R5/R6/R7 / 0603 resistors | `Resistor_SMD:R_0603_1608Metric` | **DATASHEET_DERIVED_AND_CHECKED** | Standard IPC/JEDEC 0603 land-pattern class; manufacturer MPNs recorded in schematic/BOM. |

## Mechanical and assembly checks

- J1's 5.10 mm perimeter rework allowance is represented and remains clear.
- J2A/J2B hidden 0.4 mm joints remain accessible only through the intended
  module installation path; X-ray is recommended.
- F1/F2 are through-hole/retention-style components and may require selective
  solder or hand placement.
- U1's exposed thermal area is represented by the four central PGND lands;
  the final copper/via implementation is a routing-phase task, not a reason to
  use a library-only package.
- USB-C receptacles are on the right board edge outside the cooler-owned and
  PCIe zones; J8 was moved inward for cable/debug clearance.
- No current critical component overlaps the cooler-owned or underside
  backplate volume in the placement study.

## Preserved manufacturer resources

- `references/manufacturer/Amphenol_74221-101LF/`
- `references/manufacturer/Amphenol_10164227-1004A1RLF/`
- `references/manufacturer/Littelfuse_1786165/`
- `references/manufacturer/TI_power_parts/`
- `references/manufacturer/TI_USB/`

Amphenol USB drawing links and access status are recorded in
`references/manufacturer/MANUFACTURER_RESOURCES_MANIFEST.md`. The direct CDN
download returned HTTP 403 in this environment; this is why the USB rows are
classified datasheet/drawing-derived rather than claiming an imported vendor
CAD overlay.

The board is still a placement study with zero production tracks, vias, and
copper zones. Final assembly approval remains distinct from routing readiness.
