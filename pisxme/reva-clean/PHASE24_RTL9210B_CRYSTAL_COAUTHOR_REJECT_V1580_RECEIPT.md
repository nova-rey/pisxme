# RTL9210B fixed-orientation crystal coauthor V1580

Status: REJECTED route implementation

V1580 kept Claude's accepted 0° top-side RTL9210B orientation and regenerated
XTAL_IN and XTAL_OUT together in the west support pocket using separate F.Cu
lanes. The test retained the package-local 0.15 mm clearance treatment and
did not change the global rule, layer contract, or U1 placement.

Native KiCad DRC found 17 violations / 2 REFCLK endpoint opens, including
real XTAL_IN shorts to RTL_3V3 and RSET and a real XTAL_OUT short to RTL_1V1.
The same-layer coauthor class is rejected. The fixed orientation remains
valid; the next route must separate crystal nets with a permitted layer
transition and co-author the neighboring rail/return field accordingly.
