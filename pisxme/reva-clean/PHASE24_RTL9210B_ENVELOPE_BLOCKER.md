# Phase 24 RTL9210B launch blocker

Date: 2026-09-10

## Result

The three authorized, materially different physical-envelope-aware launch
strategies were attempted and none passed native KiCad DRC. Further small
coordinate permutations are stopped. This is a routing-capacity blocker at
the accepted U1-handoff/J1 launch interface; it is not evidence that the
RTL9210B orientation or Path-B architecture is electrically invalid.

| strategy | topology | native DRC | fixture opens | disposition |
| --- | --- | ---: | ---: | --- |
| 1 | pair-owned F/B channels through existing support field | 86 | 30 | rejected: support-field crossings/shorts |
| 2 | north-perimeter reserved funnel | 15 | 30 | rejected: source-funnel crossings plus incomplete handoff implementation |
| 3 | south-perimeter reserved funnel | 40 | 30 | rejected: power/control-field crossings, pair shorting, via-dangling |

Raw reports and generated PCBs are preserved beside this report.

## Structural evidence

The native J1 high-speed contacts are on 0.5 mm pitch. The ordinary through
via used by the accepted routing contract is 0.60 mm diameter, with 0.20 mm
track width and 0.20 mm clearance. A via cannot be placed in the contact
pitch field while satisfying the clearance rule: the required center
separation from a 0.30 mm-wide contact is at least 0.65 mm, greater than the
0.50 mm contact pitch. Connector vias therefore must be outside the contact
row and use a physically reserved dogbone fanout.

The accepted JH1 handoff row is 0.4 mm pitch. That is exactly the minimum
center spacing for two 0.20 mm traces at 0.20 mm clearance, leaving no bend
or via envelope inside the row. The source ordering is
`REFCLK_P, REFCLK_N, RX_P, RX_N, TX_N, TX_P`; the J1 contact ordering is
`RX_N, RX_P, TX_N, TX_P, REFCLK_N, REFCLK_P`. The resulting permutation has
multiple inversions. With only F.Cu and B.Cu available for signals and no
plane-layer signal routing, the permutation needs a dedicated source/launch
reordering funnel; it cannot be safely inferred from centerlines.

The isolated connector primitive reached zero opens and zero shorting/crossing
errors after local corrections, but still had contact-clearance errors before
the three bounded strategies. That proves the connector can be approached
when isolated; it does not prove that the accepted tightly spaced U1 handoff
can be joined to it through the live support field.

## Required smallest upstream change

1. Replace/re-author the disposable-to-production handoff as a legally spaced
   staggered breakout footprint, co-designed with the J1 dogbone launch;
2. alternatively move/reorient the M.2 connector launch enough to provide a
   native ordered six-channel escape; or
3. authorize a third signal-routing layer / different stack contract.

Option 1 is the smallest change and preserves U1 orientation, Path-B support,
the connector, and board macro-placement. It requires explicit authority to
replace the current 0.4 mm handoff geometry. No native DRC-clean integrated
six-net route exists under the current envelope.

No production route, pad remap, design-rule relaxation, or closed upstream
decision was changed. Phase 24 remains open at the RTL9210B Path-B launch
gate.

## Final bounded source-row discriminator

The separated staggered-funnel probe reserved 1.0-mm-spaced via rows and
parallel B.Cu corridors. Both monotonic and directional pad-row fan-outs
were tried. The downstream corridor is adequate, but the first adjacent U1
pad escapes remain below the required clearance (2 violations in the
monotonic fan-out; 4 in the directional follow-up). This confirms the
remaining capacity problem is the 0.4-mm QFN source handoff itself, not
centerline search, downstream J1 capacity, or a missing board corridor.

Smallest required upstream change: re-author the source breakout as a
legally spaced staggered handoff using a documented manufacturable local
escape geometry, then reconnect the already-accepted V1603 launch. Do not
reopen U1 orientation or the Path-B architecture. If the existing 0.20-mm
trace/clearance and 0.60/0.30-mm ordinary-via contract must remain absolute,
this is a user-controlled handoff-rule/package-layout decision rather than
an additional route variant.
