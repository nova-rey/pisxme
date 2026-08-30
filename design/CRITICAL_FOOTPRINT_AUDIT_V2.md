# Critical footprint audit v2

Date: 2026-08-20

## Decision

The audit is **not a fabrication signoff**. The project-local footprints are structurally parseable, but several are synthetic placement-study footprints and the manufacturer land patterns have not all been matched to released drawings. No critical item is labelled `LIBRARY_ONLY`; unresolved items are explicitly `UNRESOLVED` rather than being promoted by assumption.

## Audit method

Each footprint was inspected in the KiCad source and compared with the manufacturer's public product page, datasheet/specification, or released drawing where available. The Amphenol CDN returned HTTP 403 to direct command-line downloads on this host, so the official URLs are preserved in `references/manufacturer/MANUFACTURER_RESOURCES_MANIFEST.md`; the PDFs were read through the official web publication where text extraction was available. A blocked download is not treated as a verified land pattern.

## Critical items

| Design item | MPN / local footprint | Local structural observation | Manufacturer evidence | Confidence |
|---|---|---|---|---|
| SXM2 receptacle J1 | Amphenol `74221-101LF` / `SXM2_74221-101LF` | 400 pads, 40×10 array, 1.27 mm nominal pitch, 0.64 mm circular pads; local footprint is a placement-study reconstruction | Official product/spec confirms 400-position 4 mm MEG-Array receptacle, 1.27 mm grid, 0.45 A/contact; the released GS-12-100 spec also defines its stated all-contact/single-contact test cases. Official drawing/app-spec links are preserved but the exact land-pattern/mask/paste/orientation match is not locally captured | **UNRESOLVED** |
| CM5 carrier connectors J2/J3 | Amphenol `10164227-1004A1RLF` / `CM5_1004` and embedded A/B variants | 100-position connector geometry is represented twice; local combined study footprint has 200 signal pads | Official CM5 datasheet specifies 100-pin connectors and this MPN as 4.0 mm stack height with 2.5 mm underneath clearance; the exact released Amphenol land pattern is not yet overlaid against the local footprint | **DATASHEET_DERIVED / RELEASE CHECK OPEN** |
| 12 V headers J3/J4 | Molex `39301082` / `MiniFitJr_8_RA` | corrected to 8 through-hole pads on 4.2 mm pitch, 12.6×4.2 mm contact-center rectangle; drill, shroud, locator, courtyard, and pin-1 orientation are still not matched to the released drawing | Official Molex page confirms 8 circuits, two rows, right-angle, polarized/shrouded, 4.20 mm pitch, 13 A/contact | **DATASHEET_DERIVED / RELEASE CHECK OPEN** |
| Cable housing | Molex `39012085` | no separate PCB footprint | Official Molex page confirms 8-circuit, two-row, 4.20 mm mating pitch; cable assembly still requires pin-1 keying review | **DATASHEET_DERIVED** |
| CM5 buck U1 | TI `TPSM63606RDLR` / `TPSM63606` | local 20-pad module footprint, 0.5 mm pad pitch, thermal/layout study footprint; schematic now references the local footprint | TI datasheet and reference layout are the authority; pad land, paste segmentation, exposed thermal area, and via pattern must be checked against the current datasheet revision before routing | **DATASHEET_DERIVED** |
| Ideal-diode controllers U2/U3 | TI `LM74700QDBVRQ1` / local `LM74700_DBV` available | local footprint has six pads; schematic uses the KiCad SOT-23 library footprint and needs one final library-vs-datasheet match | TI DBV package drawing is the authority; no manufacturer drawing locally preserved | **DATASHEET_DERIVED** |
| Protection MOSFETs Q1/Q2 | TI `CSD19536KCS` / local `CSD19536KCS_TO220` | three through-hole pads represented | TI package drawing and pinout are available; heatsink/assembly clearance not yet manufacturer-matched | **DATASHEET_DERIVED** |
| Fuse holders F1/F2 | Littelfuse `178.6165.0001` | study footprint is a generic two-pad holder outline | Manufacturer holder/fuse drawings and current interrupt/inrush selection not matched | **UNRESOLVED** |
| PCIe AC capacitors C1/C2 | Murata `GRM21BR71H224KA01#` | 0805 schematic footprint; two 220 nF coupling parts | Murata MPN/package authority is recorded; final DC-bias/SI and assembly land pattern still needs release check | **DATASHEET_DERIVED** |
| Buck capacitors C3–C6 | TDK/Murata selected MPNs | schematic references were corrected to installed KiCad `C_1206_3216Metric` for C3/C4 and `C_1210_3225Metric` for C5/C6 | component package families are consistent with selected MPN naming, but final vendor land/courtyard check remains | **DATASHEET_DERIVED** |
| Fan/pump J5–J7 | Molex `22-23-2041` intent / embedded `Fan_2x2_2.54mm` study footprint | 4-pin 2.54 mm concept; local library file is not present under that name | Standard fan pinout is known; exact selected MPN footprint is not yet matched to manufacturer drawing | **UNRESOLVED** |
| UART J8 | JST `B4B-PH-K-S` / `JST_PH_4` | local 4-pin study footprint | JST part/land pattern not independently matched in this phase | **UNRESOLVED** |
| Ethernet/USB J9 | study `USB3_HOST` | board contains a placement-study connector, not a frozen connector MPN | no selected manufacturer part | **UNRESOLVED** |

## Amphenol SXM2-specific finding

The local `74221-101LF` footprint passes the coarse structural checks: 400 pads exist, the pad centers are on a 1.27 mm grid, and the 40×10 naming spans the expected connector array. That is not equivalent to manufacturer land-pattern verification. The local pad diameter, solder-mask margin, paste aperture strategy, courtyard, and A1/orientation convention remain unverified against the Amphenol drawing. The official [MEG-Array GS-12-100 specification](https://cdn.amphenol-cs.com/media/wysiwyg/files/documentation/gs-12-100.pdf) supplies contact-performance test conditions, not a substitute for the part-specific land-pattern overlay. Because the connector is hidden BGA-style after reflow, this is a routing blocker.

## Molex correction

The previous local Mini-Fit study footprint had a 4×2 pad arrangement spread over 12.6×12.6 mm, inconsistent with Molex's official 4.20 mm two-row pitch. The local and embedded placement footprints were corrected to a 4×2 array at 4.20 mm pitch, with the 39301082 MPN in the local value. The contact-center geometry is now consistent with the official page, but exact drill, locator, shroud, and pin-number orientation still require the released Molex drawing.

## Corrections made in this phase

- The schematic and placement PCB now identify the selected buck footprint as
  `PiSXMe:TPSM63606`; the previous PCB-only `TI_RDL_20_5x5.5mm` name was a
  stale study identifier.
- The SXM2 audit now treats K19 as an unresolved auxiliary/pull-up contact,
  not GND, because the preserved reference schematic and article show a local
  +3V3 pull-up network.
- The Mini-Fit study footprint was corrected to the official 4.20 mm two-row
  contact geometry, but is not yet an assembly release footprint.

## Signoff gate

`74221-101LF`, the CM5 fine-pitch connectors, the fuse holders, fan headers, and the Ethernet/USB study connector are not yet manufacturer-verified. Do not route or release this board until each `UNRESOLVED` item is replaced by an approved manufacturer land pattern and the KiCad footprint is checked against it.
