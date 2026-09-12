# Phase 24 native hierarchy serialization probe — 2026-09-12

## Result

The disposable generator probe passed under fresh KiCad Light. The generated
ten-child hierarchy had zero severity-error ERC findings, passed the structural
hierarchy audit, and exported a netlist successfully.

## Serialization finding

The generated root child-sheet objects were missing the native KiCad
`(instances (project ... (path ... (page ...))))` record that KiCad stores on
each root `sheet` object. The existing regression did not catch this: it ran
ERC against the live canonical root rather than the disposable generated root.

The generic scaffold now emits one project/page association per root child,
using the root UUID path and the child page number. The regression now runs
native ERC against the isolated generated root and asserts all ten association
records and their page values.

## Evidence

- Producer base: committed `5047168c`.
- Worker: fresh `kicad-light`, workstream `phase24-hierarchy-probe`.
- Structural audit: PASS for all ten child label/contract/instance orders.
- Native generated-root ERC: PASS, zero severity-error violations.
- Netlist export: PASS.
- Existing native fixture showed the same root-sheet `instances` structure;
  this is corroborating native KiCad serialization evidence, not a synthetic
  graph edge.

## Scope

Only `phase3_scaffold.py` and its regression test changed. No canonical
production schematic, PCB, or live child-sheet circuitry was rewritten by this
probe. The live Phase 24 schematic remains open at its separately documented
311-warning / zero-error census.
