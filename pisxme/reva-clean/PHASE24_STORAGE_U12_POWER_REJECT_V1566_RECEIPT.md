# Path-A single-pad storage-rail discriminator — V1566

Date: 2026-09-10  
Parent: V1562  
Status: **rejected; QFN-field source escape is not clear**

One native U12 `STORAGE_3V3` pad was taken to an offset ordinary through-via
and a monotonic In2 handoff. J3 power connectivity and its negative control
remained passing. Native DRC was 620 violations / 341 unconnected items,
versus V1562's 603 / 342, with real shorts to U12 SPI/USB pads and the
existing B.Cu USB field.

This isolates the failure to the attempted U12 pad/via location and nearby
QFN/USB geometry. It does not reject the In2 concept or V1562. Raw evidence:
`PHASE24_STORAGE_U12_PAD13_V1566.kicad_pcb` and
`PHASE24_STORAGE_U12_PAD13_V1566-drc.rpt`.
