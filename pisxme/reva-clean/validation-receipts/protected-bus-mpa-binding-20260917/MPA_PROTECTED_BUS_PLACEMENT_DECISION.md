# Protected 12-V bus Macro Placement Authority decision

- **Originating work package:** `P24-PROTOTYPE-POWER-BUS-PRODUCER`
- **Decision ID:** `PISXME-P24-PROTOTYPE-POWER-BUS-MPA-20260917-R1`
- **Authority:** Macro Placement Authority, with the signed Product / Power Authority source-bus contract as the electrical basis
- **Decision state:** `BINDING_DECISION`
- **Current design base:** `31b30dc0ccb28fe341f9bffb26005b5f50cd7641`
- **Selected PCB:** `PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb`
- **Selected PCB SHA-256:** `75d2d37063818093429b44dbe4197005c2f94b23554a34947a68acaaa181bf7c`
- **Board state:** untouched integrated baseline; this record is an authority artifact, not a producer candidate or an integrated validation result.

## Evidence reconciled

The source-bus contract is `validation-receipts/prototype-source-bus-contract-20260917/PROTOTYPE_SOURCE_BUS_CONTRACT.md` (revision 1.0.0). It binds a protected common 12-V bus, a 300 W sustained V100 envelope, a 330 W / 100 ms design peak, 40 A continuous and 45 A / 100 ms source capability, an 11.4--12.6 V source window, an 11.05/11.00 V protected-bus minimum, and a complete positive-plus-return source-to-J1 resistance cap of 10.0 mOhm.

The current board census and Unblocker report establish the physical problem: `12V_IN_B` and `FUSED_12V_B` have zero routed segments/vias, `12V_PROTECTED` has no bus-wide copper or zone, and the fresh baseline reports 300 DRC violations and 499 unconnected items. Existing Branch-A copper is a long 2.0 mm B.Cu run (`12V_IN_A` from the J5 area to the F1 area) and is not accepted as resistance or thermal closure. Existing protected-net stubs are not closure evidence.

The board has three existing return zones: F.Cu `POWER_GND`, In1.Cu GND, and In4.Cu GND. The stack names In2.Cu `PWR` and In3.Cu `PROTECTED_12V`; In3 currently has no protected-bus zone. The 130 mapped `12V_PROTECTED` J1 contacts occupy columns 22, 23, 25, 26, 28, 29, 31, 32, 34, 35, 37, 38, and 40, with global bounds x=125.235--148.095 mm and y=84.285--95.715 mm. The J1 contact assignment and unknown/no-connect states remain authoritative and are not changed by this decision.

## Binding placement

The external connectors and SXM2 receptacle remain fixed. The source and protection cohort is relocated into two compact, vertically separated left-entry rows. All positions are in board coordinates in millimetres, top-side footprints, and the listed rotation is the KiCad footprint rotation.

| Reference | Decision | Position / rotation | Function and edge facing |
|---|---|---:|---|
| `J5` | **FIXED anchor** | `(12.00, 25.00)`, `0°`, top | Input-A external connector; pad 1 faces the local eastward input corridor, pad 2 is the dedicated return. |
| `J6` | **FIXED anchor** | `(12.00, 45.00)`, `0°`, top | Input-B external connector; pad 1 faces the local eastward input corridor, pad 2 is the dedicated return. |
| `F1` | **MOVE and freeze** | `(32.00, 22.00)`, `0°`, top | Input-A fuse holder; west pads receive `12V_IN_A`, east pads deliver `FUSED_12V_A`. |
| `F2` | **MOVE and freeze** | `(32.00, 54.00)`, `0°`, top | Input-B fuse holder; west pads receive `12V_IN_B`, east pads deliver `FUSED_12V_B`. |
| `D1` | **MOVE and freeze** | `(49.00, 8.00)`, `0°`, top | Input-A TVS; pad 1 is the local fused positive node and pad 2 returns directly to `POWER_GND`. |
| `D2` | **MOVE and freeze** | `(49.00, 70.00)`, `0°`, top | Input-B TVS; pad 1 is the local fused positive node and pad 2 returns directly to `POWER_GND`. |
| `U1` | **MOVE and freeze** | `(49.00, 22.00)`, `0°`, top | Input-A LM74700 stage; the input, fused, gate, protected, and ground pad group faces the A row. |
| `U2` | **MOVE and freeze** | `(49.00, 54.00)`, `0°`, top | Input-B LM74700 stage; the input, fused, gate, protected, and ground pad group faces the B row. |
| `Q1` | **MOVE and freeze** | `(61.00, 22.00)`, `0°`, top | Input-A high-side stage; source/fused pad faces U1 and protected drain faces the eastward bus. |
| `Q2` | **MOVE and freeze** | `(61.00, 54.00)`, `0°`, top | Input-B high-side stage; source/fused pad faces U2 and protected drain faces the eastward bus. |
| `J1` | **FIXED anchor** | `(150.00, 90.00)`, `0°`, top | SXM2 mechanical/electrical anchor; its mapped power field is the protected-bus destination. |

The two 32 mm fuse-holder rows leave at least 8 mm of vertical separation between their 24 mm courtyard envelopes. The connectors stay at the board entry edge. The local protection cohort is outside the J1 footprint and outside the existing storage/CM5 support regions. No other component is authorized to move under this package; a demonstrated courtyard or mechanical contradiction returns to this authority with evidence.

## Source and protection fanout

1. `J5.1 -> 12V_IN_A -> F1` and `J6.1 -> 12V_IN_B -> F2` remain separate from connector to fuse and are never joined. Each raw input path uses the shortest eastward local route from the fixed connector to the west fuse pads.
2. `F1 -> FUSED_12V_A` and `F2 -> FUSED_12V_B` remain separate through their TVS, LM74700, and high-side support cohorts. Use the local eastward pad-field routes; keep `GATE_A` and `GATE_B` inside their own rows and out of the protected-bus merge.
3. `D1` and `D2` return locally to the F.Cu `POWER_GND` field with nearby return-via stitching. Their positive pads connect only to their respective fused nodes.
4. `U1/Q1` and `U2/Q2` are two separately protected input stages. Their protected outputs remain electrically separate until their dedicated via arrays land on the common `12V_PROTECTED` inner-plane field east of x=66 mm. No passive sharing credit is taken before the protection stages.
5. The common bus begins at the post-protection via field. It feeds the J1 mapped 12-V contact field through a broad In3 plane and a short J1-side fanout. The J1 GND field uses the existing mapped GND contacts and a separate, equally low-impedance return network.

## Binding layers, corridors, and returns

- **Protected positive bus:** create the `12V_PROTECTED` field on **In3.Cu** (`In3.PROTECTED_12V`). Reserve a broad polygonal corridor from approximately `(66, 14)` to `(124, 74)`, then a J1 approach field from approximately `(122, 83)` to `(149, 98)`, clipped around the J1 signal/contact keepouts. The exact zone polygon is implementation-owned, but it must preserve these two connected regions and the same layer intent.
- **Branch output transitions:** each Q1/Q2 protected output uses a local F.Cu pad escape into an array of ordinary through-vias before the common merge. No single via is the sole 40 A path. Keep the A and B output via arrays separated until the post-protection merge boundary at x>=66 mm.
- **J1 connection:** use an In3 plane under the left-side mapped power field and a fanout/via ladder outside the SMD pad field. Do not use via-in-pad or assign any unknown J1 contact without a separate package/net authority decision. The implementation must connect all and only the mapped `12V_PROTECTED` contacts and preserve all mapped `POWER_GND` contacts.
- **High-speed preservation:** reserve the existing CM5 reference-clock corridors around B.Cu y=76/80 mm and the F.Cu CM5_PER0 route around y=82 mm. The protected bus may cross those geometries only on In3 with normal inter-layer clearance; no new F.Cu/B.Cu power route may cut through them. Preserve J1 PCIe/reference, USB3, Ethernet, storage, CM5, and clock copper and their return-via fields.
- **Return:** retain F.Cu `POWER_GND`, In1.Cu GND, and In4.Cu GND as the return hierarchy. Stitch J5/J6 returns, D1/D2 returns, U1/U2 ground pads, Q1/Q2 thermal/return structures, the protected-bus via arrays, and the J1 GND field into this hierarchy using ordinary through-vias. Do not use signal traces, shields, or a single shared neck as a high-current return.
- **Local input lanes:** use separate wide F.Cu/B.Cu copper or pours for each raw and fused branch. The producer must not retain the existing 222+ mm `12V_IN_A` route as the branch solution; it is replaced by the local cohort geometry.

## Copper, resistance, ampacity, and thermal constraints

- The complete source-to-J1 positive-plus-return path must close the signed **10.0 mOhm hot resistance cap**. Preserve the source-contract allocations: 4.0 mOhm source harness/connector loop, 2.0 mOhm fuse/reverse/fault-isolation loop, 2.5 mOhm PCB input positive-plus-return, and 1.5 mOhm J1 common-plane/spreading. The producer must return an extraction containing connector/crimp, fuse, protection, copper, vias, planes, and J1 spreading; placement alone is not proof.
- The source contract requires at least 40 A continuous and 45 A for 100 ms at the source assembly. The actual parallel-input assembly remains separately qualified; no nominal connector sharing is credited.
- No local positive/return neck may be narrower than the selected current-capacity calculation permits. As a starting geometric floor, use >=2.0 mm external copper for raw/fused high-current lanes wherever pad and clearance geometry permit, then prove the complete inner-plane/via network against actual copper thickness and via construction. Generic minimum-width rules must not replace the current/thermal calculation.
- The protected via arrays and every copper neck must be checked for at least 39.315 A continuous and 37.814 A for the bounded peak screen, with temperature rise <=30 degC above declared ambient or the lower component/assembly limit. The Q1/Q2 devices require >=20 degC junction margin under the 40 A screen and pulsed/SOA proof for the 100 ms event.
- The protected bus shall be wide/low-impedance by plane area and parallel transitions, not by a narrow F.Cu trunk. The implementation must not claim equal current through J1 contacts; it must prove the extracted contact-field and spreading budget.


## Power Integrity advisory boundary

Power Integrity confirms the source-contract screens at the 11.4 V source minimum: 31.452 A sustained and 34.376 A for the 100 ms peak, with protected-bus minima of 11.085 V and 11.056 V at the 10 mOhm path cap. The existing 222 mm, 2 mm `12V_IN_A` run is estimated at approximately 54.6 mOhm at 1 oz or 27.3 mOhm at 2 oz before its return is counted, so it cannot remain in the producer candidate.

The current J5/J6 footprint each presents one 12-V contact and one return contact. The producer shall make no 40/45 A source-assembly claim and no equal-split credit from these footprints. Exact connector, terminal, harness, crimp, fuse-holder, and protection qualification must prove the 40 A continuous / 45 A peak source contract; if the selected assembly cannot meet it, Product / Power / Package Authority must change the source-assembly contract before Phase 24 power acceptance can close. This is a source qualification dependency, not permission to reopen the placement decision or to route unqualified current through the present connectors.

## Protected existing copper and immutable boundaries

The following are protected from this work package:

- J5, J6, and J1 mechanical anchors, pad/net identity, and connector geography.
- The six-layer stack/layer roles, board outline, and the mapped J1 12-V/GND/unknown contract.
- Existing `POWER_GND` zones on F.Cu, In1.Cu, and In4.Cu, plus validated high-speed and timing corridors: PCIe/reference/reset, CM5 PER/REFCLK, USB3, Ethernet, storage differential pairs, and their return structures.
- Existing unrelated component placements and support cohorts outside the ten named power references.
- The existing `12V_IN_A` long run, six short protected stubs, and incomplete power objects are **not protected closure copper**; they are replaceable producer-era copper because they do not satisfy the current branch-B, plane, or 10 mOhm contract. Their deletion/replacement must be limited to the named power nets and validated by fresh DRC/connectivity.

The producer may move only the eight named local support references to the exact positions above and may edit only the associated power copper/zone/via geometry. It may not change schematic nets, J1 assignments, unrelated routes, rules globally, or any unknown/no-connect contact.

## Rationale and failed baseline hypotheses

The current placement strands the input paths: J5/J6 are at the left entry while F1 is at `(240,40)`, F2 at `(50,120)`, the ideal-diode/high-side cohorts are around `(20,75)/(30,78)` and `(20,95)/(10,108)`, and D1/D2 are at `(110,32)/(110,72)`. This creates long or absent input/fused corridors and leaves the common protected field without copper. The binding relocation makes each source path monotonic from the fixed left edge, places each protection cohort in the same row as its source, and leaves a single eastward protected-plane corridor to the J1 power field. It therefore addresses the actual failure geometry rather than replaying a route on the dispersed baseline.

The prior six-loop placement record is superseded by the signed conventional protected-bus architecture and is not reused. The baseline producer non-result and the 300/499 census prove incompleteness, not a topology impossibility. This decision does not authorize speculative route variants or any Phase 25/26 action.

## Required producer return

The isolated producer must return a candidate from the exact base SHA with the placement positions above, a changed-scope manifest, native DRC/connectivity results, positive/return plane and via census, complete resistance/drop/thermal calculations, and raw hashes. The candidate then goes through serialized canonical integration and fresh KiCad Light validation. A failed candidate returns one evidence packet to this authority; it does not authorize an orientation search or an unrestricted routing campaign.

## Authoritative baseline declaration

**For `P24-PROTOTYPE-POWER-BUS-PRODUCER`, the binding current-HEAD placement and corridor baseline is: J5 `(12,25,0°)` fixed, J6 `(12,45,0°)` fixed, J1 `(150,90,0°)` fixed; F1 `(32,22,0°)`, F2 `(32,54,0°)`, D1 `(49,8,0°)`, D2 `(49,70,0°)`, U1 `(49,22,0°)`, U2 `(49,54,0°)`, Q1 `(61,22,0°)`, and Q2 `(61,54,0°)` on top; separate A/B input and fused corridors; a post-protection merge at x>=66 mm; and a `12V_PROTECTED` In3.Cu plane/approach to the mapped J1 power field. This is the sole MPA placement/corridor plan for the producer.**
