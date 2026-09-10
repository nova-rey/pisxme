# Phase 24 Path-B V1603/V1517 integration receipt

Date: 2026-09-10  
Status: CURRENT PATH-B BASELINE; Phase 24 remains open

The accepted V1603 physical-envelope launch is applied to the clean V1517
support baseline. RTL9210B remains at the closed Claude orientation: top side,
0 degrees, pin 1 southwest. The six mappings are U1.61->J1.55, U1.62->J1.53,
U1.64->J1.43, U1.65->J1.41, U1.67->J1.47, and U1.68->J1.49.

Native DRC reports zero high-speed errors. Two inherited warnings remain: one
dangling local RTL_1V1 track and one dangling reference-clock transition via.
Seven support opens remain, covering RTL_1V1 and XTAL_IN support exposed by
the source-field reopening. They are open work, not waived findings.

The native audit derives connectivity from saved-board pads/tracks/vias and
passes all six U1-to-J1 links plus six source-track-removal negative controls.
