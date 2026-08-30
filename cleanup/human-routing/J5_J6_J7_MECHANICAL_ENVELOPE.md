# J5/J6/J7 mechanical envelope

## Active footprint evidence

J5, J6, and J7 use the same 4-pin Molex 22-23-2041-style header footprint.
The active drawing outline is `x=-5..5 mm`, `y=-2..2 mm`, or 10 x 4 mm per
header. Centers are:

| Ref | Center | Center pitch to next |
|---|---:|---:|
| J5 FAN1 | `(205,12)` | 8 mm to J6 |
| J6 FAN2 | `(205,20)` | 8 mm to J7 |
| J7 PUMP/AUX | `(205,28)` | -- |

At 8 mm center pitch, adjacent documented outlines overlap by 2 mm. The
current placement is therefore not physically valid even before considering a
latch, cable strain relief, or finger/tool access.

## Housing/model status

The project contains the header footprint and electrical MPN intent, but not a
verified mating housing STEP or final cable bend model. The commonly used
2.54 mm fan connector housing is wider than the contact pitch; the final
choice must be checked against the manufacturer's drawing.

## Acceptance envelope

Use at least 12--14 mm center spacing for independent 10 mm body outlines,
then add the actual housing/latch and cable-bend envelope. The pump header
must be separately identified and should not be hidden behind either fan
harness. Final placement must remain outside the cooler-owned area and keep
the latch face/tool approach accessible from the board edge.
