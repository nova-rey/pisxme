# Phase 24 co-authored TX/RX target-field receipt — V150

Date: 2026-09-10  
Base: `PHASE24_STORAGE_USB3_R80_RELOCATED_V127.kicad_pcb`  
Fixture: `PHASE24_STORAGE_SUPPORT_U12_COAUTHOR_TX_RX_FAR_V150.kicad_pcb`

V150 combined the source-aware far RX transition with a staggered normal-
orientation TX target launch. All six local support endpoint assertions pass.
Native KiCad DRC reports 9 violations / 32 fixture opens and no
`shorting_items`; remaining errors are TX/RX final-field crossings and
clearances, plus fixture silkscreen/copper warnings.

Disposition: rejected, but retained as the best current route-development
basis. This is implementation evidence only. The native U12 pad field,
ordinary-via contract, layer policy, Path A schematic, and production CAD
were not changed.
