# Phase 24 native-clean U12 target-field receipt — V154

Date: 2026-09-10  
Base: `PHASE24_STORAGE_USB3_R80_RELOCATED_V127.kicad_pcb`  
Fixture: `PHASE24_STORAGE_SUPPORT_U12_COAUTHOR_TX_RX_FAR_V154.kicad_pcb`

V154 is the transform-aware, native-pad-derived U12 target-field primitive.
RX transitions are outside the U12 field, RX final legs are on F.Cu, TX
transitions are above the six-pad row, and ordered support trunks use B.Cu
with ordinary through-vias. Disposable moved-capacitor silk is omitted only
from this fixture; the production library is unchanged.

Native KiCad 10 DRC: 0 violations. All six local endpoint assertions pass.
The saved-board removed-track negative control passes by failing connectivity
after removal of a necessary `JMS_USB3_TXN` track. No via-in-pad, plane-layer
signal, severity change, production PCB, or schematic change was used.

The fixture intentionally omits CM5/J7 continuation and non-USB3 support,
leaving 32 expected opens. V154 is accepted as a local routing primitive,
not integrated Phase 18/24 closure.
