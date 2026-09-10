# RTL9210B-CG Path-B orientation decision — V1575

Date: 2026-09-10  
Decision authority: Claude consultant review, session `4c0469ee-3364-4bea-98a5-6b6b170f8fdd`  
Status: ACCEPTED BASELINE DECISION

## Decision

Use RTL9210B-CG U1 at **0° / unrotated / top-side F.Cu**, with pin 1 at the
south-west corner. The implementation baseline is
`PHASE24_RTL9210B_U155_REHOME_V1517.kicad_pcb` and its accepted local support
lineage. Do not rotate or relocate U1 or reopen the orientation search.

## Immediate support arrangement

- West, close-in: Y1 25 MHz crystal and C1/C2 at XTAL_IN/XTAL_OUT; R1 RSET
  immediately north of that pocket.
- East, close-in: U2 SPI flash beside pins 18–24, with short direct tracks and
  no via woven through the source field.
- North-east: C3/C4/C5 rail decoupling and PEDET/CLKREQ pull-ups staged outside
  the SPI and lane corridors.
- West-side lane/REFCLK: preserve the accepted east-then-north escape around
  the package; do not force a direct west via.
- South-side control: keep RESET_N, PEDET, CLKREQ_N, PERST_N, and ISOLATEB on
  the control edge. Keep exposed pad 69 and GND pad 66 on the validated return
  strategy.

## Evidence basis

The accepted lineage contains the saved-board-audited U1.66 GND/RXP,
U1.63/RXN, GND-return, RSET, and U1.55↔U1.63 1V1 primitives. V1517 reports
zero native DRC violations with six inherited opens. The explored 90° and
180° families did not accumulate an equivalent complete support chain, while
the later V1549–V1558 failures are source-field/fanout failures under the
fixed QFN pitch and ordinary-via contract, not evidence that rotation helps.

## Implementation constraints

Keep USB on the north edge, SPI and rail departures on the east edge, control
signals on the south edge, and crystal/REFCLK/lane corridors on the west edge.
Keep XTAL_IN and XTAL_OUT as separate corridors; keep REFCLK away from them.
Preserve ordinary through-vias only, no via-in-pad/microvias, no plane-layer
signals, and the approved 0.20 mm global routing rule. This decision does not
close the remaining REFCLK, XTAL_IN, support, firmware, procurement, or
land-pattern gates.

## Handoff

Extend V1517 in one coordinated local implementation pass. Integrate the
already-proven support primitives first, then solve the remaining source-field
classes as multi-net escapes. Validate with native KiCad DRC, endpoint audits,
and saved-object connectivity. A normal route failure is an implementation
defect; only concrete physical impossibility should return to Claude.
