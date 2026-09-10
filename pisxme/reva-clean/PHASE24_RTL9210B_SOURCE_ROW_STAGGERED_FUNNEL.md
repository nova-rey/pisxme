# Source-row staggered-funnel probe

Date: 2026-09-10  
Candidate: `PHASE24_RTL9210B_SOURCE_ROW_STAGGERED_FUNNEL.kicad_pcb`  
Generator: `phase24_rtl9210b_source_row_staggered_funnel.py`

## Verdict

`REJECTED_ROUTE_IMPLEMENTATION_WITH_STRUCTURAL_HANDOFF_EVIDENCE`

This disposable probe reserves five explicit 1.0-mm-spaced via rows and
parallel B.Cu handoff corridors. It keeps the accepted RTL9210B orientation
and V1603 launch unchanged and does not promote any probe copper.

## Native evidence

KiCad native DRC reports 9 violations and 4 unconnected items. The reserved
lower corridors are separated, but the source escape still has two real
violations at the adjacent 0.4-mm-pitch U1 row: the `ISOLATEB` and `CLKREQ_N`
pad-end escapes cannot diverge with the current 0.20-mm trace/0.20-mm
clearance envelope. The remaining unconnected items are intentionally
stripped remote support continuations in this source-row fixture; the two
via-dangling findings are inherited remote endpoints, not synthetic graph
edges. Silkscreen overlaps are fixture-only.

This materially different funnel therefore confirms that the lower channel
capacity is adequate but the first handoff out of the QFN row is not. It
supports the smallest upstream repair already identified in
`PHASE24_RTL9210B_ENVELOPE_BLOCKER.md`: re-author a legally spaced staggered
source breakout/handoff, or obtain an explicitly approved finer local escape
geometry. It does not invalidate U1 orientation, the Path-B architecture,
or the V1603 launch.

Raw native report: `PHASE24_RTL9210B_SOURCE_ROW_STAGGERED_FUNNEL-drc.rpt`.
