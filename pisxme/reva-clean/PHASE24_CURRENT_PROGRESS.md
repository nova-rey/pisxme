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
integrating this launch with the complete Path-B support network and acreage
candidate. The current integrated candidate has zero V1603 launch DRC errors;
native integrated six-net connectivity and negative controls pass. Remaining
support-field warnings/opens are still open and must be closed before Phase 24
promotion. Orientation search remains closed and no validation severity or
layer rule may be relaxed.

The current baseline is now `PHASE24_RTL9210B_PATHB_V1603_V1517_INTEGRATED`:
it applies the accepted launch to the clean V1517 support board. Native DRC
has zero high-speed errors; seven support opens and two inherited warnings
remain. Continue by repairing RTL_1V1/XTAL_IN support in this local field,
then rerun the integrated audit.

The current generated candidate now passes the local repair: native DRC is
0 violations / 0 unconnected items, and the integrated six-net audit with
six negative controls passes. The generator uses the V1523 RTL_3V3 support
baseline, accepted V1603 launch, east-side RTL_1V1 closure, and V1534/V1526
crystal corridors. Continue with broader Path-B support, production parity,
and Phase 24 validation; do not reopen U1 orientation.

The V1523-source-hand-off trial is rejected: preserving the old RTL_1V1
corridor causes REFCLK_P crossings, while a near-QFN RXP via escape shorts
RXN/TXN under the production via envelope. This is a local source-field
implementation failure, not a contradiction of the frozen orientation or
V1603 launch. Continue from `21b6c1f0` with a co-authored 1V1/source-field
departure outside the QFN south-edge pair envelope.

## Resume point

Resume from the pushed checkpoint containing this note. Historical rejected
experiments and raw evidence remain immutable; do not use the old V1517
overlay routes as current production authority.
