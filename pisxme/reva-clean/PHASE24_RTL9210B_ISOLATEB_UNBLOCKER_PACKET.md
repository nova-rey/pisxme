# Unblocker packet — RTL9210B `ISOLATEB` source escape

Blocker ID: `ISOLATEB_SOURCE_ESCAPE`  
Date: 2026-09-10  
State: recoverable local routing blocker; Path-B remains active.

## Evidence

The accepted candidate is `PHASE24_RTL9210B_PATHB_V1603_V1517_INTEGRATED.kicad_pcb`.
U1.12 is a 0.2×0.9-mm pad in a 0.4-mm-pitch south pad row. Its neighboring
owned departures are `CLKREQ_N` (pad 13), `PERST_N` (pad 14), `RTL_1V1`
(pad 16), and `RTL_5V` (pad 17). The accepted candidate's native DRC is
clean before adding the MIC2545A support network.

The corrected MIC2545A support fixture is also native DRC-clean and proves
the corrected duplicated-pin `IN`/`OUT` topology. The first complete support
integration had 22 DRC violations/4 opens; the shifted and dogbone source
probes had 17, 2, and 4 violations respectively; the first coupled local
departure reroute had 12 violations; and the source-row coupled escape had
11 violations, all with zero opens. The latest source-row evidence is in
`PHASE24_RTL9210B_SOURCE_ROW_COUPLED_ESCAPE-drc.rpt`.

The repeated failure is not the MIC2545A circuit or RTL9210B orientation. It
is the collision between the new `ISOLATEB` source escape and already-owned
U1-row control/power departures, vias, and the nearby SPI/PEDET corridors.

## Bounded continuation paths

1. **Recommended — local source-row co-route.** Reopen only the U1 south-row
   departures. Keep the existing remote endpoints and nets, but regenerate
   `ISOLATEB`, `CLKREQ_N`, `PERST_N`, and `RTL_5V` together. Reserve their
   staggered F.Cu pad-end escapes and B.Cu corridors first, moving the local
   `RTL_1V1` via/branch only if required. Refill zones and run native DRC,
   endpoint parity, and the existing negative controls.
2. **Local support relocation.** Keep the source escape primitive but move
   only the nearest low-speed support/via fields (not U1 orientation or the
   V1603 high-speed launch) to free a clean B.Cu handoff corridor. Revalidate
   the affected support groups.
3. **Isolated implementation fixture.** Prove the co-routed source-row
   primitive against a reduced native U1/support fixture before applying it
   to the integrated candidate. This is a tooling/routing aid, not a relaxed
   production gate.

No option changes the RTL9210B orientation, MIC2545A topology, Path-A
fallback, or accepted V1603 high-speed launch. Do not promote any rejected
probe copper.

