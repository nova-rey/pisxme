# RTL9210B XTAL_OUT trials: V1512-V1514

These disposable trials were run against V1508 RSET and V1502's single In1
GND field. V1512 used a north corridor; V1513 added an F.Cu/B.Cu hop around
the RTL_1V1 B.Cu barrier; V1514 jogged the source north before departure.
Native KiCad DRC rejected each for the live RTL_1V1/RTL_3V3 source-field
geometry. The lower corridor and crystal endpoint topology were not accepted
as production evidence. No rules, pin maps, or Path-A assets were changed.

Current accepted basis remains V1508. XTAL_OUT, XTAL_IN, REFCLK, and all full
Path-B gates remain OPEN.
