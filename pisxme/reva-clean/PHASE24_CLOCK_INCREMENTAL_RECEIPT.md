# Phase 24 incremental clock probe receipt

Starting from `PHASE24_U7_CLOCK_SOURCE_ESCAPE.kicad_pcb`, the incremental
probes were composed in order:

| probe | result | native evidence |
|---|---|---|
| XI-only | accepted discriminator | 165 unconnected; zero short/crossing classes |
| XI + XO | accepted discriminator | 164 unconnected; zero short/crossing classes |
| XI + XO + first VSSOSC | rejected | 163 unconnected, two short and two crossing classes |

The XI branch uses the serialized source via `(124,125.5)` and reaches Y1.1
at the queried `(106.9,129.15)` pad. The XO branch uses its serialized
source via and a lower B.Cu launch to queried Y1.3. The first VSSOSC path
used an F.Cu perimeter through `(122.5,126.5) -> (116,126.5) -> (116,120)`;
native DRC shows that it crosses the inherited SATA-TX-N corridor and shorts
the XI launch and a POWER_GND pad. It is rejected. The next VSSOSC probe must
cross the SATA obstacle in a deliberate layer-separated location.

The follow-on `phase24_clock_passive_astar.py` search found no B.Cu path from
the serialized Y1.1 launch to R23.1 inside the current local corridor and
therefore emitted no candidate. This is rejected routing evidence, not a gate
relaxation; remaining work is coordinated passive-field routing or placement.
