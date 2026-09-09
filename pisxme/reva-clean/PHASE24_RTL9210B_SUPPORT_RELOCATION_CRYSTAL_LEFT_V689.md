# RTL9210B Path-B V689 — rejected left crystal translation

V689 translated Y1/C1/C2 together by 3 mm and rebuilt both crystal nets and
their ordinary-via GND returns from native pad coordinates. Native KiCad DRC
found 11 violations, including XTAL_IN/XTAL_OUT/GND shorts and crossings, with
31 incomplete opens.

Disposition: reject this crystal relocation/routing implementation. Retain
the V683/V687 local crystal and rail bases; do not promote V689.
