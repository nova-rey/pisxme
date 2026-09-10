# Path-B RTL9210B orientation baseline validation — V1575

Date: 2026-09-10  
Baseline: `PHASE24_RTL9210B_U155_REHOME_V1517.kicad_pcb`  
Orientation: 0° unrotated, top-side, pin 1 southwest

The Claude-delegated orientation decision is applied as the single Path-B
baseline. No rotation or relocation was performed. Native KiCad 10.0.5 DRC
was rerun on the saved baseline and reports **0 violations / 6 unconnected
pads / 0 footprint errors**. The existing native U1.55↔U1.63 connectivity
audit passes, and removing the saved U1.55 source segment fails its negative
control as required.

The six opens are the already-documented XTAL_IN, XTAL_OUT, and REFCLK P/N
endpoint groups. This receipt validates the accepted baseline only; it does
not claim complete Path-B support, firmware, procurement, land-pattern, or
integrated-board closure. Subsequent work must preserve the fixed edge
assignment and solve remaining routes as coordinated local implementation
changes.

Raw rerun report: `PHASE24_RTL9210B_U155_REHOME_V1517-current-drc.rpt`.
