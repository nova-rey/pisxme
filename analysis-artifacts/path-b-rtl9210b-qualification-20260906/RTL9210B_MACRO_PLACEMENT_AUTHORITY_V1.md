# RTL9210B-CG Path-B macro placement authority decision

Date: 2026-09-10  
Authority agent: `macro_placement_authority`  
Status: `AUTHORITATIVE`

## Evidence submitted

- Package: the V1517 native QFN-68 footprint has its exposed-pad centroid at
  `(98.00, 70.00) mm`; its KiCad footprint anchor is `(18.00, 8.00) mm`. At
  0 degrees, pin 1 is south-west at `(94.05, 68.00) mm`.
- Pin-edge facts: pins 64/65 and 67/68 are the shared lane-0 receive/transmit
  pairs; pins 61/62 are REFCLK; pins 52-54 are the crystal supply and pair;
  pins 18-24 are SPI; pins 8, 13, and 14 are PEDET, CLKREQ#, and PERST#;
  exposed pad 69 and the perimeter power pads require local return/decoupling.
  The retained pin-boundary record is
  `pin-fact-boundary.csv`.
- Surroundings: the selected topology places the M-key endpoint and lane/REFCLK
  corridor west of U1, the crystal/RSET support pocket west of U1, SPI flash
  east of U1, rail decoupling and pull-ups north-east, and control destinations
  south of U1.
- Routing evidence: V1517 is the accepted local support baseline. Its saved-board
  native rerun reports zero DRC violations, six documented endpoint opens, and
  zero footprint errors. The U1.55-to-U1.63 rail audit and source-removal
  negative control pass. V1549-V1558 reject a local source/fanout class under
  the ordinary-via and 0.20 mm rule; they do not establish an orientation fault.
- Rejected variants: the 90-degree and 180-degree orientation families are
  retained as rejected/disposable evidence. They did not produce an equivalent
  complete support chain. They have no authority.

## Decision

PLACE RTL9210B-CG U1 on F.Cu at the V1517 footprint anchor `(18.00, 8.00) mm`,
with exposed-pad centroid `(98.00, 70.00) mm`, at `0 degrees` unrotated. Pin 1
remains south-west at `(94.05, 68.00) mm`.

Package-edge ownership is fixed as follows:

- West: crystal, RSET, REFCLK, and lane-0 corridor. Keep the proven
  east-then-north local escape where required; do not force direct west vias.
- East: SPI flash and rail departures. U2 stays close to pins 18-24 with direct
  tracks that do not weave vias through the SPI source field.
- North-east: C3/C4/C5 decoupling plus PEDET/CLKREQ pull-ups, staged outside
  the SPI and lane corridors.
- South: RESET_N, PEDET, CLKREQ_N, PERST_N, and ISOLATEB control departures.
  Retain the exposed-pad-69 and pad-66 validated return strategy.

This orientation makes the high-priority lane/REFCLK and clock/RSET groups face
their corridors, keeps SPI and local rail support on their own edge, and avoids
interleaving support parts with critical escapes.

## Implementation constraints

Use ordinary through-vias only; do not use via-in-pad, microvias, or plane-layer
signals. Preserve the approved 0.20 mm global routing rule. Keep XTAL_IN and
XTAL_OUT separate and keep REFCLK away from both. Preserve the fixed edge
assignment during route maturation. The six inherited endpoint opens and a normal
route failure are implementation work, not a placement reopen.

## Reopen protocol

Only `macro_placement_authority` can reopen this baseline. An implementer must
submit a structural-contradiction packet naming the exact geometry and package
edge, the manufacturing or channel rule, the affected mandatory interface, the
unavoidable shared corridor or support-distance failure, and multiple materially
different routing methods that fail for the same reason. A high immature DRC count,
one bad route, a theoretical shorter path, or another agent preference is not a
contradiction.

PLACE U1 AT THE FROZEN V1517 POSITION WITH 0-DEGREE ROTATION. WEST OWNS
CLOCK/LANES, EAST OWNS SPI/RAILS, NORTH-EAST OWNS DECOUPLING, AND SOUTH OWNS
CONTROLS. THIS IS THE AUTHORITATIVE PATH-B BASELINE.
