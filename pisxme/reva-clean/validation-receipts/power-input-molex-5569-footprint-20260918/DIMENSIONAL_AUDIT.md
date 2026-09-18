# Molex 5569-06A2 / 0039300060 isolated footprint audit

Package: P24-POWER-INPUT-FOOTPRINT-RECONCILIATION
Status: isolated candidate only; no canonical CAD/library changes.
Candidate source: KiCad official kicad-footprints `Connector_Molex.pretty/Molex_Mini-Fit_Jr_5569-06A2_2x03_P4.20mm_Horizontal.kicad_mod`, generated with kicad-footprint-generator from the Molex 5569 drawing family.

## Drawing-to-candidate checks

| Field | Manufacturer evidence | Candidate | Result |
|---|---|---|---|
| Part identity | 5569-06A2; 39-30-0060 / 0039300060 | Description names 5569-06A2 and 39-30-0060 | PASS |
| Contact count/rows | 6 circuits, two rows | pads 1..6, two rows | PASS |
| Contact pitch | 4.20 mm | x = 0, 4.2, 8.4; y rows = 0, 5.5 | PASS |
| Row spacing | 5.50 mm for 5569 dual row | y = 0 and 5.5 | PASS |
| Contact finished hole | 1.80 ± 0.05 mm recommended hole | six PTH drills 1.80 mm | PASS |
| Mounting peg holes | 3.00 ± 0.03 mm; 7.30 ± 0.08 mm peg offset | NPTH at (0,-7.3) and (8.4,-7.3), drill 3.0 | PASS |
| Contact span/body A | 13.80 mm 6-circuit envelope; 8.40 mm pin span | x span 8.40; F.Fab body x -2.7..11.1 = 13.8 | PASS |
| PCB thickness | 1.78 mm recommended / drawing max 1.78 mm class | candidate does not encode thickness | REVIEW in fabrication stack |
| Pad copper | manufacturer specifies hole layout; pad size is PCB process choice | 2.7 x 3.7 mm oval/roundrect, derived annulus | DERIVED, authority review |
| Mask/paste | through-hole connector; manufacturer drawing does not prescribe mask expansion/paste | default KiCad mask, no paste | DERIVED, DFM review |
| Pin-1/polarity | Molex polarized/shrouded, pin 1 shown in drawing | roundrect pad 1 and pin-1 silk marker | PASS subject to symbol orientation |
| Connector body/mating keepout | right-angle body and mating envelope; avoid components in envelope | fab/crtyd boundary and silkscreen reserve envelope | DFM/mechanical review |
| 3D parity | Molex 5569 family model reference | KiCad standard 3D path for 5569-06A2 | model-file availability and orientation review |

## DFM/service notes

- Header is through-hole right-angle and is intended for wave/selective/hand solder; reserve solder access and inspectability on the bottom side.
- Keep the two 3.0 mm NPTH peg keepouts free of copper and vias unless the manufacturer/fabricator explicitly permits otherwise.
- Keep the full right-angle mating/cable envelope clear of the cooler, board edge obstructions, adjacent headers, and service harness bend radius.
- Do not credit contact-to-contact passive current sharing in the power contract. Each positive/return branch must have the authority-assigned protection and copper path.
- The 2.7 x 3.7 mm land is a derived fabrication choice, not a Molex claim; DFM must verify annulus, mask clearance, solder fillet, and the selected board thickness.
- The candidate does not establish connector, harness, fuse, thermal, or 15 A branch qualification.
