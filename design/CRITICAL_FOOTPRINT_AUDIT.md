# Critical footprint audit

## Status

**Incomplete; not a fabrication signoff.** The project contains architectural/custom footprints and several critical manufacturer footprints whose pad numbering, mating height, or 3D model orientation has not been verified against current manufacturer drawings in the hydrated KiCad project.

| Item | Selected part | Audit result |
|---|---|---|
| SXM2 | Amphenol `74221-101LF` | Electrical identity and 400-position count corroborated; exact land pattern, module mating height, and 3D orientation still require manufacturer CAD/drawing review. |
| CM5 BTB | 2 × Amphenol `10164227-1004A1RLF` | 100-position, 0.4 mm, 4 mm stack verified from manufacturer page; exact STEP and final land-pattern review remain open. |
| 12 V header | Molex `39301082` | Corrected from the erroneous `39301062`; pad pitch/orientation and mating-housing clearance must be checked in the actual footprint. |
| 12 V receptacle | Molex `39012085` | Mating housing selected; cable/contact sourcing and assembly access remain to be validated. |
| Fuse | Littelfuse `178.6165.0001` + `0297015.U` | Rating choice documented; holder footprint, fuse extraction clearance, and thermal copper remain open. |
| Ideal diode | LM74700-Q1 + CSD19536KCS | Current schematic placeholder is not acceptable; exact symbol pin numbering, MOSFET orientation, and gate loop need replacement and review. |
| Buck | TPSM63606RDLR | TI pinout and layout requirements identified; current custom symbol must be corrected. |
| AC coupling | Murata `GRM21BR71H224KA01#` candidate | 220 nF/50 V/0805 verified from Murata; validate DC-bias and footprint before release. |
| Fan headers | Molex `22-23-2041` | 4-pin, 2.54 mm, vertical, partially shrouded, 4 A/contact from Molex data; use as standard PC-fan-compatible candidate. |

Critical footprints are not cleared until their actual pad numbering, courtyard, solder-mask/paste rules, 3D orientation, mating direction, and rework access are checked in KiCad and against the manufacturer drawing.

