# RTL9210B crystal escape experiments V1549–V1553

## Current disposition

All five disposable rotated-QFN escape variants are **REJECTED**. They are
isolated source-field experiments only; none is a production RTL9210B layout.
Path A and the accepted Path-B V1523/V1526/V1534 evidence are unchanged.

## Evidence

| Variant | Native DRC violations | Unconnected items | Failure class | Disposition |
|---|---:|---:|---|---|
| V1549 opposite-direction | 4 | 17 | XTAL_OUT enters exposed-pad field; native shorts/hole clearance | rejected |
| V1550 both south | 7 | 17 | source-field removal succeeds, but transitions are too close and shelves interfere | rejected |
| V1551 wide dogbones | 5 | 17 | source dogbones approach adjacent supply pads; B shelves still violate | rejected |
| V1552 separated shelves | 13 | 17 | source shorts remain; 0.15-mm width violates board minimum | rejected |
| V1553 0.20-mm wide escape | 4 | 17 | XTAL_IN→RTL_3V3 and XTAL_OUT→RTL_1V1 native shorts at QFN source row | rejected |

The reports were produced by KiCad 10 native DRC. The 17 unconnected items
are expected in these deliberately stripped fixtures and are not claimed as
support-circuit validation.

## Engineering conclusion

The tested rotated source class is not valid at the current ordinary
0.20-mm minimum trace rule. The failure is a local QFN fanout/authoring
problem, not evidence that RTL9210B is electrically unusable. Further work
must change the source-escape class (for example a manufacturer-recommended
package orientation/escape or a properly authoritative fine-pitch fanout)
before coauthoring the complete support field. No board-rule relaxation is
accepted by this receipt.
