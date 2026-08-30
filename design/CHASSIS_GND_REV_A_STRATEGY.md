# USB-C shield / chassis strategy for Rev A

## Selected strategy

`DIRECT_USB_C_SHELL_TO_GND`

J9, J10, and J11 S1/S2 shell pads are intentionally bonded to the board
`/GND` net. No separate `/CHASSIS_GND` copper trunk, RC link, or chassis
bridge component is used in Rev A.

## Why this is the selected closure

- All five prior shell connectivity relationships close without a new copper
  route through the USB3/USB2 connector fields.
- A direct-GND trial produced no new short, clearance, crossing, or pad
  overlap class relative to the final-plane baseline.
- `cm5MiniITX` provides working open-hardware precedent for USB-C shell pads
  tied directly to GND.
- The alternate isolated-shell and edge-trunk choices are not electrically
  complete in the current placement; the edge trunk crossed accepted
  high-speed/service geometry.

## Mechanical/EMI note

The board-level connection does not define the enclosure bonding method. A
metal enclosure should receive its own controlled mechanical bond if it is
used as a shield. A plastic enclosure has no enclosure return to bond. This
is a Rev-A simplification and a documented EMI risk, not an unresolved PCB
connectivity record.

## Verification gate

The six shell pads must appear on `/GND` in the active PCB, and the three
schematic shell labels must be `GND`. The final DRC may retain inherited
library/cosmetic/dangling findings, but it must contain no
`CHASSIS_GND` unconnected record and no new true electrical class.
