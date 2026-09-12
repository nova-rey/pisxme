# Phase 24 U14 storage-select short repair receipt

Candidate: `PHASE24_STORAGE_MKEY_USB3_EAST_SUPPORT_V6_U14_REPAIR_20260912.kicad_pcb`

The V6 storage USB3 candidate contained a genuine local power/control routing
defect inherited from its base: the `STORAGE_3V3` track ran from U14 pad 5 at
(211.1,149.05) through U14 pad 4 `STORAGE_SEL` at (211.1,150.95) to the
downstream via. The repair removes only that vertical segment and detours the
rail around the east side of U14 through (212.5,149.05), (212.5,152.05), and
(211.1,152.05).

Native KiCad 10.0.5 after refill reports 426 violations / 421 unconnected
items, down from 428/421. The actual-pad ten-link USB3 audit passes unchanged,
and the shorting-class `STORAGE_SEL`/`STORAGE_3V3` finding is absent. Remaining
DRC/open findings are not waived; this is a storage-local repair candidate,
not full Phase 24 closure.
