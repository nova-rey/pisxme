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

