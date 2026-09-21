# Macro Placement Authority R2 — R3 protected-bus corridor release

- **Originating work package:** `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- **Decision ID:** `PISXME-P24-PROTECTED-BUS-MPA-20260921-R2`
- **Decision type:** binding local placement/corridor revision
- **Authority:** Macro Placement Authority, with Product/Power R3 contract retained
- **Status:** `BINDING_DECISION_FOR_PRODUCER; REQUIRES_PROTOTYPE_VALIDATION`
- **Canonical evidence reviewed:** R1 full validation receipt, candidate `426bc7e1050e6edfe0f04387cb928aa26b2f53bf`, KiCad Light image `sha256:37d60e6797eaa14ea393de005b9793af5d9b4a...` (full image digest remains in the retained receipt)
- **CAD changed by this decision:** no
- **Hardware operated:** no

## Decision

The current R1 nine-branch placement is retained as the local placement baseline,
but the prior requirement that a full-board F.Cu `POWER_GND` return zone remain
continuous through the protected-bus corridor is **superseded**. The minimum
frozen constraint that must yield is:

> `REV_A_TOP_POWER_GND_RETURN_FULL` may not occupy the nine-branch source/fuse,
> protection-cohort, or protected-J1 approach corridors on F.Cu.

The producer shall replace that global F.Cu fill with scoped local F.Cu ground
copper only where it is geometrically legal and useful for pad/TVS/control
returns, stitched to the existing return hierarchy. In1.Cu and In4.Cu remain the
continuous POWER_GND return planes and retain their existing system role. This
is a corridor release, not a rule relaxation: native clearances, solder-mask
rules, hole/keepout rules, net classes, impedance rules, and fabrication limits
remain in force.

No additional same-geometry routing variant is authorized before this corridor
release is integrated. The prior R1 failures are not evidence that the nine-
branch contract is impossible; they establish that the global F.Cu return-zone
constraint consumes the pad and local escape corridor needed by the contract.

## Evidence for the minimum constraint change

The retained R1 report records **1220 DRC violations / 391 unconnected** on the
full nine-branch candidate. The report directly identifies repeated
`solder_mask_bridge` violations between the F.Cu POWER_GND zone and:

- F1/F2/F7/F9 branch PTH pads carrying raw or fused branch nets;
- connector/J9 source pads and local protected tracks;
- Q1/Q2 gate/control and protected-bus tracks;
- the protected approach to mapped J1 POWER_GND contacts;
- an existing CM5 REFCLK B.Cu corridor near the F9 region through the shared
  copper environment.

The zone declaration in the retained candidate is `REV_A_TOP_POWER_GND_RETURN_FULL`
on F.Cu with polygon `(1,1)-(299,1)-(299,179)-(1,179)`. It is therefore not a
local exception or a footprint-only issue. The same class of conflict persists
across the distinct attempts already recorded by Unblocker (997/383,
1013/364, 679/390, and 1220/391). The correction is to release this single
implementation constraint and preserve the actual return planes below it.

## Exact placement and protected geometry

The following anchors and local positions remain binding:

- J1 `(150,90)`, top side, 0 degrees.
- J5 `(12,25)`, J6 `(12,50)`, J9 `(12,75)`, top side, 0 degrees.
- F1 `(36,26.25)`, F2 `(64,26.25)`, F3 `(92,26.25)`.
- F4 `(36,51.25)`, F5 `(64,51.25)`, F6 `(92,51.25)`.
- F7 `(36,76.25)`, F8 `(64,76.25)`, F9 `(92,76.25)`.
- D1 `(108,10)`, C3 `(108,29)`, U1 `(108,34)`, Q1 `(111,42)`.
- U2 `(108,62)`, Q2 `(111,70)`, C4 `(108,77)`, D2 `(108,96)`, TP2 `(114,60)`.

The nine branch pairing remains J5/J6/J9 pads 1-3 positive to pads 4-6
returns, paired 1-4, 2-5, 3-6, through F1-F9. The R3 source/protected contract
remains 11.4–12.6 V, 300 W sustained, 330 W/100 ms, 40 A continuous, 45 A
peak, nine independent branch pairs, no passive-sharing credit, and complete
hot positive-plus-return resistance <=8.50 mOhm implementation cap.

## Layer and corridor binding

1. F.Cu is reserved for connector/fuse pad escapes, short local protection and
   control loops, and authorized probe access. The released global F.Cu zone
   shall be clipped out of these corridors; no F.Cu star fanout is permitted.
2. Raw branch positives use ordered In2.Cu lanes from each connector escape to
   the west fuse pads. Fused outputs use ordered In2.Cu lanes to the
   `12V_BRANCH_JOIN` at x=104–106. No raw/fused lane crosses a different
   branch pad, courtyard, or high-speed corridor.
3. Branch returns use ordered In4.Cu lanes to `POWER_RETURN_JOIN` at x>=104.
   In1.Cu remains the continuous reference/return plane. Local F.Cu ground
   copper is permitted only as a pad/TVS/control return island with explicit
   native clearance and stitching to In1/In4.
4. Q1 is the primary protection path. Its protected output transitions through
   a multi-via field at x>=115 to In3.Cu. In3.Cu alone approaches the mapped J1
   12-V field from x=116.5–124. No B.Cu J1 terminal, via-in-pad, unknown J1
   contact, or narrow F.Cu trunk is permitted.
5. The J1 high-speed, clock, USB3, Ethernet, storage, CM5, and validated return
   corridors remain protected. The producer may clip only the F.Cu global zone
   named above and may not edit unrelated copper.
6. U2/Q2/D2/C4 remain physically distinct and receive no passive parallel-bus
   or N-1 credit. Their electrical disposition remains controlled by the signed
   source contract; this decision does not add a second protection path.

## Implementation and stop condition

The producer shall implement the F.Cu zone clipping/local-return correction on
an isolated committed-base candidate, then run targeted native DRC and
connectivity for the nine-branch region. It must return the resulting zone
geometry, pad/net census, branch positive/return opens, and exact residual DRC
classes. A clean local result is still only a candidate and requires serialized
integration and fresh KiCad Light validation. A failure after the zone release
must identify the remaining physical contradiction; it does not authorize
reinstating the full-board F.Cu zone or replaying the four rejected geometries.

**AUTHORITATIVE BASELINE DECLARATION:** For
`P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`, retain the R1 component/anchor
coordinates and R3 electrical contract, and supersede only the full-board F.Cu
`POWER_GND` corridor occupancy. The legally available routing corridor is
F.Cu-local escapes plus In2 raw/fused lanes, In4 branch returns, In1 return
plane, and In3 protected J1 approach under native rules. This is the sole
binding R2 placement/corridor decision.
