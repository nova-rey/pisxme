# Path-B RTL9210B qualification fixture plan

Status: `PLAN_ONLY_NATIVE_FIXTURE_NOT_AUTHORIZED`

This is a disposable, read-only-first qualification artifact for the
RTL9210B-CG Path-B comparison. It is not production CAD, does not replace
Path A, and contains no copied or modified Path-A schematic/PCB content.

## Decision

Do not author a complete native Path-B KiCad fixture yet. The retained
community material is sufficient to state a narrow pin-identity contract, but
not sufficient to safely encode the support circuit, M-key sideband behavior,
power/isolation behavior, or virgin-chip provisioning assumptions. A partial
fixture would risk turning community guesses into electrical authority.

The smallest next fixture is a standalone RTL9210B bring-up board, authored
only after the gates in `fixture-plan.md` are closed. It must remain outside
the production project and must expose SPI-flash, UART/JTAG, reset, power,
mode, and M-key sideband test access.

## Artifact contents

- `fixture-plan.md` — bounded scope, facts, unknowns, gates, and acceptance plan.
- `pin-fact-boundary.csv` — machine-readable known/unknown boundary.
- `next-fixture-spec.json` — proposed smallest future standalone fixture.
- `baseline.md` — tool, stackup, correspondence, and fresh ERC/DRC evidence.
- `evidence-manifest.json` — source hashes and provenance boundaries.

No `.kicad_sch`, `.kicad_pcb`, library, project, rule, or production output is
authored by this artifact.
