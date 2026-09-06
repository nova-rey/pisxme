# RTL9210B disposable PCB fixture — rejected route experiment

Date: 2026-09-06

## Result

`PHASE24_RTL9210B_NATIVE_FIXTURE.kicad_pcb` loaded under KiCad 10.0.5 and
native DRC completed. It is **REJECTED** and is not Path-B authority.

Receipt: `PHASE24_RTL9210B_NATIVE_FIXTURE-drc.rpt`

- 102 DRC violations;
- 0 unconnected items;
- multiple F.Cu track crossings;
- at least one shorting condition involving a control net and an unrelated
  QFN pad;
- additional clearance/courtyard/metadata findings.

The fixture used straight point-to-point segments as a connectivity
discriminator. It was not an obstacle-aware high-speed route and did not
encode the complete RTL9210B support circuit. Its failure is therefore a
`ROUTE_IMPLEMENTATION_FAILURE` plus incomplete-fixture limitation, not a
rejection of the RTL9210B architecture.

## Disposition

The PCB, generator, and raw native DRC report are retained as rejected
evidence. They must not be used as production CAD or as proof that the
RTL9210B pinout/auto-selection concept fails.

The delegated KiCad review independently produced
`analysis-artifacts/path-b-rtl9210b-qualification-20260906/`, recommending a
plan-only standalone bring-up fixture until exact support values, M-key
sideband handling, isolation/power timing, and virgin-chip provisioning are
bounded. That recommendation is accepted for the next experiment.

The next fixture must be authored only after those facts are captured, use
the corrected SMD footprint, include the complete support network and test
access, and route with native pad/net identity and ordinary via transitions.
