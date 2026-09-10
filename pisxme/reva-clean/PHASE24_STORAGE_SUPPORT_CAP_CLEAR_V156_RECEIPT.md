# Phase 24 integrated cap-shelf repair receipt — V156

Date: 2026-09-10  
Base: `PHASE24_STORAGE_USB3_R80_RELOCATED_V127.kicad_pcb`  
Fixture: `PHASE24_STORAGE_SUPPORT_CAP_CLEAR_V156.kicad_pcb`

V156 tested the smallest coherent C86/C87 shelf translation intended to
clear the live C26/BRIDGE_1V1 collision found when transplanting V154. The
complete ten-net USB3/support connectivity audit passes, but native KiCad
DRC rejects the integrated candidate at 155 electrical/mechanical findings,
including PERST crossings, TX support collisions/shorts, and storage-field
interactions. The moved caps also changed the source escape corridor without
coauthoring the surrounding PERST geometry.

Disposition: rejected integrated placement/transplant. V154 remains the
accepted local support routing primitive; the next integrated attempt must
coauthor capacitor placement and the affected PERST/source corridors together.
Path A schematic, Path B qualification, PCIe, and production CAD remain
unchanged.
