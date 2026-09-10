# MIC2545A Path-B integration trial — rejected route implementation

Date: 2026-09-10  
Candidate: `PHASE24_RTL9210B_PATHB_MIC2545A_ISOLATEB.kicad_pcb`  
Generator: `phase24_rtl9210b_add_mic2545a.py`  
Raw report: `PHASE24_RTL9210B_PATHB_MIC2545A_ISOLATEB-drc.rpt`

## Verdict

`REJECTED_ROUTE_IMPLEMENTATION`

This was a disposable integration trial. It does not invalidate the accepted
RTL9210B V1517/0° orientation, the V1603 six-net launch, or the corrected
MIC2545A support topology.

## Evidence

Native KiCad DRC found 22 violations and 4 unconnected items. The failures
are localized to the attempted integration geometry:

- the new U1.12 `ISOLATEB` escape was authored across the crowded adjacent
  U1 control/power pad row and crossed existing `RTL_5V`, `RTL_1V1`, and
  `CLKREQ_N` copper;
- the long B.Cu `SSD_3V3` return crossed existing `PERST_N`, SPI, and ground
  return geometry and landed on a ground-via corridor;
- local U3 ground support was not joined to a valid nearby ground endpoint;
- the attempted trial therefore cannot be used as evidence against the
  MIC2545A circuit or against the frozen RTL9210B orientation.

The corrected disposable support fixture remains the valid support evidence:
native DRC 0/0/0, explicit physical `IN` 5/7 and `OUT` 6/8 joins, and a
passing trace-removal negative control. See
`PHASE24_MIC2545A_SUPPORT_FIXTURE_RECEIPT.md` and
`PHASE24_MIC2545A_DFM_AUDIT.json`.

## Resumption rule

Do not promote this trial or reuse its copper. The next integration attempt,
when authorized by the support-closure sequence, must co-author a short U1.12
source escape and a local ground-return endpoint against the accepted V1603
corridors before adding the SSD_3V3 launch. No orientation search or broad
macro-floorplan reopening is justified by this failed trial.

