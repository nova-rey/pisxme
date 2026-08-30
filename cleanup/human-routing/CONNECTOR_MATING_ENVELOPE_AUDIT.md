# Connector mating-envelope audit

| Interface | Active location/orientation | Evidence | Result |
|---|---|---|---|
| FAST-A J9 | `(211.5,72)`, 0° | Würth 692122030100 STEP; mouth faces +X/right | PASS with enclosure plug envelope |
| FAST-B J10 | `(211.5,110)`, 0° | Same manufacturer STEP; 38 mm center separation | PASS with enclosure plug envelope |
| SERVICE J11 | `(210.5,40)`, 0° | Footprint only; mating model not present | OPEN recovery-access check |
| Raw 12 V J3/J4 | `(30,130)/(58,130)`, 0° | Board-edge position; Mini-Fit Jr housing not modeled | PASS with housing/cable check |
| FAN1/FAN2/PUMP J5/J6/J7 | `(205,12)/(205,20)/(205,28)`, 0° | Active 10 x 4 mm outlines overlap | FAIL; placement correction required |
| UART J8 | `(214,81)`, 90° | Internal debug header; no external plug envelope required by contract | DEBUG-only, access guidance required |
| Recovery/reset | TP3/control region | Electrical access retained; TP3 is interior | PASS for bench use, not panel access |

## USB-A plug envelope

The 38 mm J9/J10 center separation leaves approximately 21.34 mm between
nominal 16.66 mm connector-width bands. Independent provisional panel
openings of 22 x 12 mm with 30 mm cable-head depth are non-overlapping. Final
signoff must use the selected cable/adapter head and enclosure wall thickness.

## Gate

The board cannot claim complete physical usability until SERVICE, power, and
cooling mating hardware is either modeled or dimensioned from the final
manufacturer drawings.
