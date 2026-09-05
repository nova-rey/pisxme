# Phase 24 clock-placement sweep receipt

Date: 2026-09-05

The sweep used `phase24_clock_position_sweep.py` against the Phase 23
serialized U7 ancestor and ran native KiCad DRC on each saved candidate. The
results below are comparison evidence only; no candidate is promoted unless
the complete clock block and inherited board gate pass.

| candidate | native DRC | clock shorts | clock crossings | unconnected |
|---|---:|---:|---:|---:|
| east | 212 | 1 | 13 | 395 |
| farwest | 250 | 5 | 3 | 395 |
| nearwest | 212 | 0 | 1 | 395 |
| nearwest-layer-split | 214 | 0 | 5 | 395 |
| nearwest-mixed | 224 | 2 | 14 | 394 |
| nearwest-ordered | 214 | 0 | 5 | 395 |
| nearwest-ordered2 | 215 | 0 | 9 | 394 |
| nearwest-rot90 | 214 | 0 | 5 | 395 |
| nearwest-sata-reroute | 252 | 5 | 19 | 394 |
| north | 230 | 1 | 15 | 395 |
| south | 220 | 1 | 7 | 395 |
| west | 220 | 1 | 7 | 395 |

The near-west candidate is the least-bad placement class: zero clock shorts
and one clock crossing. Its remaining crossing is between the VSSOSC and XO
source corridors near the U7 escape, so it is rejected until that route is
regenerated. The complete isolated fixture independently reports four clock
crossings, confirming the clock network still needs a topology-preserving
layer/perimeter repair before acreage integration.

The U5 native-connectivity audit and disposable trace-removal regression are
independent and passing; they do not waive this clock gate or any inherited
board DRC/unconnected records.
