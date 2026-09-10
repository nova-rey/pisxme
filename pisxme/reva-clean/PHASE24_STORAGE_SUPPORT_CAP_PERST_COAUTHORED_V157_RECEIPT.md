# Phase 24 cap/PERST coauthored integration receipt — V157

Date: 2026-09-10  
Base: `PHASE24_STORAGE_USB3_R80_RELOCATED_V127.kicad_pcb`  
Fixture: `PHASE24_STORAGE_SUPPORT_CAP_PERST_COAUTHORED_V157.kicad_pcb`

V157 coauthored C86/C87 placement, TX source transitions, RX source
transitions, and target trunks around the local PERST boundary. All ten
USB3/support endpoint assertions pass. Native DRC remains 155 violations /
499 incomplete-board opens, including a PERST/BRIDGE_3V3 short and several
new source-field crossings. The failure is local route implementation, not
a schematic, Path-B, PCIe, or architecture result.

Disposition: rejected. V154 remains the native-clean local U11/U12 support
primitive; V157 is retained to document that moving every local segment
without a route-aware source escape is insufficient.
