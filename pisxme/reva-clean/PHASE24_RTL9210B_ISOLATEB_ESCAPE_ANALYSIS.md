# RTL9210B `ISOLATEB` source-escape analysis

Date: 2026-09-10  
Baseline: `PHASE24_RTL9210B_PATHB_V1603_V1517_INTEGRATED.kicad_pcb`

## Native geometry evidence

Native `pcbnew` inspection of U1 shows the relevant south pad row:

| Pad | Net | Center X (mm) | Center Y (mm) | Pad size (mm) |
|---:|---|---:|---:|---|
| 9 | JTAG_TDO | 98.0 | 73.95 | 0.20 × 0.90 |
| 10 | NC | 98.4 | 73.95 | 0.20 × 0.90 |
| 11 | NC | 98.8 | 73.95 | 0.20 × 0.90 |
| 12 | ISOLATEB | 99.2 | 73.95 | 0.20 × 0.90 |
| 13 | CLKREQ_N | 99.6 | 73.95 | 0.20 × 0.90 |
| 14 | PERST_N | 100.0 | 73.95 | 0.20 × 0.90 |
| 15 | NC | 100.4 | 73.95 | 0.20 × 0.90 |
| 16 | RTL_1V1 | 100.8 | 73.95 | 0.20 × 0.90 |
| 17 | RTL_5V | 101.2 | 73.95 | 0.20 × 0.90 |

The row pitch is 0.4 mm. With the current 0.25-mm route width and required
clearance, a lateral F.Cu departure from pad 12 is not a legal channel: the
adjacent pad envelopes consume the available gap. The first integrated trial's
native DRC confirms this with crossings and solder-mask bridges against pads
13–16.

## Engineering consequence

This is a source-escape problem, not evidence against the MIC2545A support
topology, the RTL9210B orientation, or the V1603 launch. A valid next repair
must leave pad 12 through its pad-end direction, reach an outboard clearance
point, and only then transition to B.Cu with an ordinary through-via. The
outboard path must be checked against existing `RTL_1V1`, `RTL_5V`,
`CLKREQ_N`, `PERST_N`, and PEDET corridors before connecting U3.

The rejected full integration trial remains preserved in
`PHASE24_MIC2545A_INTEGRATION_TRIAL_REJECT.md`. No additional route variant
is promoted by this analysis.

## Shifted-corridor probe

`PHASE24_RTL9210B_ISOLATEB_ESCAPE_PROBE.kicad_pcb` tested the same pad-end
escape with the first via shifted from (99.2, 76.0) to (99.2, 77.0) and the
handoff moved to (107.0, 82.0). Native DRC still found 17 violations, but the
failure class changed: the B.Cu handoff crosses the existing PEDET and
PERST_N corridors, while the via locations violate the existing ground-zone
and via-clearance envelope. This probe is rejected evidence, not a promoted
route and not evidence that the frozen orientation is impossible.

The latest opposite-side jog stayed vertical through the south pad-end exit,
then moved to x=101.8 mm before the outboard via. After refilling zones it
left zero opens and only two native crossings: the existing `RTL_5V` departure
at x=101.2 mm and the existing `PERST_N` departure at x=100.0 mm. This
confirms that the next repair must co-author those adjacent local departures
around the `ISOLATEB` escape. Repeating point perturbations is no longer a
useful route class.

## Final bounded escape probe in this class

The probe was then jogged to the opposite side of the pad-row segment,
through x=101.8 mm before the outboard via. After zone refill it had zero
opens and exactly two native crossings: the existing `RTL_5V` departure from
pad 17 and the existing `PERST_N` departure from pad 14. This exhausts the
simple source-escape coordinate class. The smallest remaining repair is to
reroute those neighboring local departures together with `ISOLATEB`, keeping
their existing endpoints and nets intact.
