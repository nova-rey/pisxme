# Coordinated U1 local-departure repair — rejected

Date: 2026-09-10  
Candidate: `PHASE24_RTL9210B_LOCAL_DEPARTURE_REPAIR.kicad_pcb`  
Generator: `phase24_rtl9210b_local_departure_repair.py`  
Raw DRC: `PHASE24_RTL9210B_LOCAL_DEPARTURE_REPAIR-drc.rpt`

## Result

`REJECTED_ROUTE_IMPLEMENTATION`

This disposable candidate regenerated the U1.12 `ISOLATEB`, `CLKREQ_N`,
`PERST_N`, and `RTL_5V` pad-row departures together while preserving their
remote endpoints. Native DRC found 12 violations and zero unconnected pads.

## Failure classification

- the proposed PERST_N B.Cu corridor crossed the existing PEDET B.Cu branch;
- the CLKREQ_N via/escape was too close to the ISOLATEB F.Cu departure;
- the RTL_5V south escape collided with existing SPI and RTL_1V1 geometry;
- one local ISOLATEB handoff remained dangling because it was intentionally
  only a source-escape probe, not a complete support endpoint.

This is route implementation evidence. It does not invalidate the accepted
RTL9210B orientation, V1603 high-speed launch, MIC2545A topology, or Path-A
fallback. No copper from this candidate is promoted.

## Next bounded repair

The next useful attempt must keep the pad-end source escapes but reassign the
four local corridors as a coupled group, with PEDET and PERST_N separated
before either reaches B.Cu, and with the RTL_5V escape kept away from the U2
SPI field. Further single-net coordinate changes are not justified.

