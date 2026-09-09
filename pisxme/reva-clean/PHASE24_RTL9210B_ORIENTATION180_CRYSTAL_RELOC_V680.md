# RTL9210B Path-B V680 — rejected crystal relocation

V680 moved Y1/C1/C2 to an upper storage-field shelf and used two separated
ordinary-via B.Cu corridors. Native DRC found 11 violations, including
multiple crossings and XTAL_IN shorts to RTL_3V3 and GND, with 20 incomplete
opens.

Disposition: reject this relocation/routing implementation. It does not
invalidate the support architecture or the orientation-180 local rail basis.
