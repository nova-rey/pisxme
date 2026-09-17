# Protected-bus canonical integration scope

## State

This directory records the serialized integration of the accepted protected-bus
producer candidate into the selected integrated PCB. The source candidate was
produced from the exact MPA base board at `31b30dc0ccb28fe341f9bffb26005b5f50cd7641`
and is retained at
`validation-receipts/protected-bus-producer-candidate-20260917/`.

The producer PCB SHA-256 is
`4160dd609cfba58dcb03ae241d4c62f0a768c1276f7602f43eb1f90a4557c33b`. The
pre-integration canonical board SHA-256 is
`75d2d37063818093429b44dbe4197005c2f94b23554a34947a68acaaa181bf7c`.

## Integration boundary

The canonical board file `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`
was replaced with the accepted KiCad-generated producer board, while the
canonical schematic, project file, external rule file, libraries, board
outline, J5/J6/J1 anchors, mapped J1 contact contract, and unrelated circuitry
remain unchanged.

A semantic S-expression comparison against the pre-integration board found:

- all 131 footprint UUIDs retained;
- only the eight MPA-authorized local references moved: F1, F2, D1, D2, U1,
  U2, Q1, and Q2;
- J5, J6, J1 and all other footprint positions retained;
- all existing non-footprint graphics retained;
- the three existing return zones retained with their defining geometry;
- one new `12V_PROTECTED` In3.Cu zone added;
- 103 new routed segments, 26 replaced/removed power segments, 47 new vias,
  and 6 replaced/removed power vias, all within the producer's named
  raw/fused/protected/return scope;
- no schematic, rule, or project-file mutation.

The changed board is an integration candidate, not validation closure. The
producer DRC report is retained separately and remains diagnostic evidence.

## Baseline tool context

Fresh detached KiCad Light baseline was run before integration on the exact
current HEAD. The worker image reported KiCad 10.0.6. The retained baseline
reports are in `baseline/`; they cover the selected PCB and canonical
`PiSXMe_RevA_Clean.kicad_sch`. Baseline counts were 282 DRC violations and 395
unconnected items, plus 293 ERC findings. These counts are a fresh Light
reproduction under the current embedded/project rule context and are not
compared directly to older 300/499 or 440/265 censuses without context.

## Required next state

The integration candidate must receive a fresh detached KiCad Light validation
from its committed SHA. Validation must record exact source SHA, toolchain,
project/rule/library identities, native ERC/DRC, opens/shorts/connectivity,
protected In3 plane and return-layer checks, and resistance/thermal extraction.
