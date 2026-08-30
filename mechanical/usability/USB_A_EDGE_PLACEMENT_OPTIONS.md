# USB-A edge-placement options

## Decision frame

The goal is two independently usable 5 Gbps host ports with mouths normal to
an enclosure wall. USB-A is already selected for the simplified FAST-A/B
architecture; this study is about physical orientation and port grouping, not
about reopening the USB protocol choice.

## Options

| Option | Description | Electrical impact | Mechanical assessment | Status |
|---|---|---|---|---|
| A | Two separate Würth 692122030100 receptacles on the right edge, retained at the current 0° orientation | No signal change; the manufacturer STEP shows the mouths facing +X; only the enclosure plug envelope remains to be checked | 38 mm center spacing gives generous simultaneous-plug clearance; simple rectangular panel cutouts | Preferred |
| B | One dual-stacked USB3 Type-A receptacle | Requires new dual-port footprint, schematic/BOM/CPL migration, and new USB breakout | Compact and visually neat, but increases mechanical/assembly dependency on one part and exact panel height | Not selected |
| C | Two separate ports on bottom edge | Requires moving the existing USB paths and changes enclosure cable direction | Possible, but cables would compete with the power-input edge and reduce coherent service access | Rejected |
| D | One right edge and one top edge | Splits the product I/O edge and makes enclosure routing less predictable | No advantage over a right-edge pair | Rejected |

## Preferred local geometry

Keep J9 at `(211.5,72)` and J10 at `(211.5,110)` at `0°`. The official Würth
STEP rendered against the active footprint places the mating faces at the
right board edge. A disposable 90/270-degree rotation test was rejected: the
footprint's mixed SMT/PTH contact rows overlap when rotated, so that is not a
manufacturable orientation for this specific part.

The two independent connectors are preferred over a dual-stack part because
they preserve the already selected, manufacturer-documented Würth land
pattern, 5,000-cycle retention, and independent routing/serviceability. A
dual-stack remains a Rev-B packaging option rather than a reason to delay the
current usability correction.

## Panel guidance

For two separate outward-facing ports, use two rectangular openings centered on
the connector axes, with a nominal 22 x 12 mm keep-clear per opening until the
selected enclosure wall and plug family are dimensioned. Retain at least 6 mm
of web between openings. Final wall cutouts must be checked against the actual
connector front flange and the chosen cable's molded head, not only the PCB
footprint.
