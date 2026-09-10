# PiSXMe Rev A Clean — current progress checkpoint

Date: 2026-09-10

## Paused state

The active work is Phase 24 RTL9210B Path-B implementation, isolated from
Path A and production CAD. Claude's accepted Path-B baseline remains U1
RTL9210B-CG at 0 degrees, top-side, pin 1 southwest, on the V1517 lineage.
The pause point is after the V1590 local QFN escape primitive and the V1591
handoff-to-J1 launch diagnostic.

## Evidence completed

- V1590: all six U1 high-speed source pads reach explicit west handoff pads;
  native connectivity and six trace-removal negative controls pass. Native
  DRC has zero shorts, crossings, and footprint errors; stripped-support
  warnings/opens are intentional fixture findings.
- V1591: starting from those handoffs, the native obstacle search placed four
  nets toward the actual J1/M.2 launch before no legal remaining launch was
  available. No incomplete route was promoted.
- Path-B authority, corroborating support, M.2 mapping, native netlist, and
  hierarchy-conflict audits remain passing. Path A and unrelated board work
  remain preserved.

## Current open gate

The bounded physical-envelope launch experiment is now successful as the
V1603 local primitive: all six U1-to-J1 high-speed nets are natively connected
with zero high-speed DRC errors and negative controls pass. The next work is
to integrate this launch with the complete Path-B support network and acreage
candidate, then rerun native DRC, connectivity, return/reference, and support
validation. Orientation search remains closed and no validation severity or
layer rule may be relaxed.

## Resume point

Resume from the pushed checkpoint containing this note. Historical rejected
experiments and raw evidence remain immutable; do not use the old V1517
overlay routes as current production authority.
