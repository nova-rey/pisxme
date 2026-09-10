# Phase 24 coherent cap/PERST transplant receipt — V158

Date: 2026-09-10  
Base: `PHASE24_STORAGE_USB3_R80_RELOCATED_V127.kicad_pcb`  
Fixture: `PHASE24_STORAGE_SUPPORT_COHERENT_CAP_PERST_V158.kicad_pcb`

V158 tested a bounded integrated coauthoring class: C86/C87 relocation,
source-aware RX transitions, TX target transitions outside the PERST endpoint,
and the ten-net USB3/support route. All ten native endpoint assertions pass.
Native DRC reports 153 violations / 499 incomplete-board opens, including
new source-field crossings and a PERST/BRIDGE_3V3 short. This is rejected
route/transplant evidence; the local V154 primitive and all electrical
authority remain valid.

No schematic, production PCB, PCIe route, layer contract, or DRC severity was
changed. The next attempt must coauthor the live PERST/source boundary rather
than translate the V154 copper as a rigid island.
