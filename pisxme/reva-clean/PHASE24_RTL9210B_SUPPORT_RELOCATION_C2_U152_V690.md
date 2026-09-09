# RTL9210B Path-B V690 — rejected C2-only repair

V690 moved only C2 three millimeters outboard and rebuilt XTAL_OUT, C2 GND,
and U1.52 RTL_3V3. Native KiCad DRC found 15 violations, including
XTAL_IN/XTAL_OUT shorts, RTL_3V3/CLKREQ interference, RTL_1V1/GND contact,
clearance, solder-mask, and hole-clearance failures.

Disposition: reject the C2-only placement/routing class. C2 cannot be moved
independently on this basis; the next attempt must co-author the complete
crystal/support micro-island with verified native pad geometry.
