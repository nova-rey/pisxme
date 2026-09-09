# Phase 24 acreage validation status

## CURRENT STATE — documentation authority (2026-09-08)

This section is the current narrative authority for Phase 24. The live
dual-mode storage routing basis is
`PHASE24_STORAGE_J8_V5_VBUS_V1.kicad_pcb`; its source-owned J8 mode control,
USB3, SATA, JMS583 support, VBUS/sense endpoints, and schematic-to-PCB pad
parity are covered by the current native focused audits. Those focused gates
pass, including the saved-board negative controls where applicable. Native
full-board DRC and routing-quality closure remain OPEN: the latest accepted
baseline is still not a production-clean board and retains inherited opens,
clearance/width/crossing work, and complete Phase 24 power/ground closure.

The previously described missing-JMS583-support-network TODO is
SUPERSEDED. The support network has been authored and its native endpoint
audit plus negative control pass; remaining support-field route cleanup is a
routing gate, not an instantiation task. Likewise, old malformed footprint,
pre-J8 mode-control, stale parity, obsolete connector, and rejected-route
claims below are historical evidence only when explicitly labeled as such.
RTL9210B-CG Path B is an active parallel qualification candidate, not a
rejected alternative. The current comparison and evidence ledger are in
`PHASE24_RTL9210B_PATH_COMPARISON_20260909.md`; its corrected SMD package,
shared lane-0/PEDET mapping, native support primitives, and JLC identity are
retained, while authorized application-circuit/provisioning, complete
mode-aware route, firmware rights, and integrated validation remain open.
V667 and V668 are rejected SPI route allocations on the retained V595
source/rail field; V668 specifically tested separated staggered B.Cu
channels and confirms that the unchanged source/rail field needs coherent
island reallocation. V670 then tested the consultant-recommended V35/U2-left
lower-3V3 co-author and found 24 violations/21 opens from RSET/1V1/XTAL/SPI
interactions; it is likewise a rejected route implementation. These are
route-implementation results, not Path-B package or architecture rejections.
V671 then moved the RSET endpoint; its 15-violation/24-open result is also
rejected because the perimeter collided with lower RTL_1V1 and the board
edge. The next Path-B class is an interior co-authored RSET/lower-3V3 field.
V672 is the positive interior RSET basis (nine inherited warnings, no signal
violations). V673's lower-3V3 overlay is rejected at 12 violations/21 opens;
its remaining signal failures are the U1.52/RSET contact and U1.39/USB_DM
source escape. The next implementation must co-author those QFN departures.
V674's all-pad rotation discriminator confirms the 90° U1.39 escape is clean
at package level; its remaining integrated dependency is the adjacent
RTL_1V1 departure. Other rotations are rejected by native DRC and are not
preferred.
The current local routing basis is V23, a bounded co-authored
USB_TXP/USB_TXN/JMS_AVDDL/crystal route variant. The next action is to carry
this source-owned basis through complete storage-field regeneration, native
DRC, and the existing full-board gates. Path-B remains a separate isolated
qualification track; its next action is coherent support-island
reallocation, as recorded in `PHASE24_RTL9210B_SPI_CHANNELIZED_NATIVE_V668.md`.

V37 is the current best disposable CM5 USB3 source-field experiment layered
on the filled V32 VBUS basis. It regenerates all four J7 USB3 departures,
preserves the B.Cu handoffs, passes USB3/SATA/mode/JMS583/parity focused
audits, and has zero native shorting or footprint-error entries. Its 603 DRC
violations and 399 unconnected pads keep it out of production authority; the
full storage field still requires coordinated closure. See
`PHASE24_STORAGE_CM5_USB4_MONOTONIC_V37.md` and its raw native receipt.

A disposable V13-plus-support trial on 2026-09-09 joined the complete
JMS583 low-speed support cohort using native pad endpoints. Its focused
support audit and trace-removal negative control passed, but native DRC rose
from 730 to 778 findings (395 unconnected items). It is rejected as a route
implementation class; support connectivity passing does not justify adding
the direct joins over the congested lower field.

V23 is a disposable route variant with separated XOUT lower-field geometry.
A later native net-identity audit confirms that V13 already contained same-net
ordinary XIN/XOUT through-vias at the relevant layer changes; therefore V23
did not correct a missing-via authoring defect. V23 still passes the focused
JMS583 support audit and negative control, with native DRC at 724 findings /
400 unconnected items and two inherited unrelated shorting items. It remains
disposable evidence only, not production authority or full-board closure.

V22 is superseded route evidence: its changed crystal geometry created an
XIN/XOUT transition-via short. V24 tested an all-F.Cu crystal escape to avoid
the B.Cu SATA corridors; native DRC remained at 730 and introduced four
shorting items. Both are rejected route implementations. V23 remains the
best disposable crystal-field variant, but not a via-authority repair.

V25 moved both XIN/XOUT B.Cu transition corridors outside the inherited SATA
B.Cu field before crossing above it. Native DRC worsened to 745 findings and
introduced eight shorting items, so the outer-corridor class is rejected.
V23 remains the retained disposable basis.

V26 corrected V25's diagonal QFN departures to orthogonal exits before trying
outer crystal corridors. Native DRC still reported 746 findings and six
shorting items, including collisions with inherited V100/USB/SATA copper.
The corrected outer-corridor class is rejected; V23 remains current.

The filled-zone V23 candidate
`PHASE24_STORAGE_JMS583_CRYSTAL_VIAS_V23_FILLED.kicad_pcb` is now the current
saved-board validation basis. Native DRC reports 607 findings / 399
unconnected items, and the native JMS583 physical endpoint, USB3, SATA, and
mode-control audits all pass. Two inherited unrelated shorting items remain;
this does not close full-board routing or Phase 24.

Fresh native DRC recheck on 2026-09-09 reproduces the filled V23 baseline at
607 findings and 399 unconnected items. This receipt supersedes no raw
history; it establishes the stable comparison baseline for the next
coordinated storage-corridor repair.

V27–V30 tested bounded repairs for the two storage-local shorts found after
zone fill. V27 introduced seven native shorts; V28 removed the U13 pad-field
short but collided with USB_RXN1; V29 collided with JMS_AVDDL and failed the
mode-control audit; V30 passed mode-control but introduced a CM5 USB TX
pair short. All are rejected route implementations. The filled V23 board
remains the comparison basis.

V31 tested an F.Cu-only VBUS detour to remove the V23
`TUSB_SATA_TXP`/`VBUS` short. After native zone refill it removed that class
but introduced three other shorting classes (`MODE_IN`/`STORAGE_SEL`, CM5 USB
RX polarity, and TUSB SATA TX polarity). It is rejected; VBUS requires
coordinated local corridor allocation.

V32 is the best current disposable corridor basis for the storage-local
VBUS repair. Its left-exit VBUS route removes the V23 SATA/VBUS short; after
native zone refill, DRC reports 604 findings / 399 unconnected items and only
one remaining shorting item, a CM5 USB RX polarity collision. Native JMS583
physical endpoints, USB3, SATA, and mode-control audits pass. V32 is not
production authority or Phase 24 closure until the remaining native short and
full routing debt are resolved.

V33 tested an orthogonal staggered CM5 USB3 RX source escape on the V32
basis. Native DRC reported 594 findings / 401 unconnected items but six true
shorting classes, including RX polarity and TX/RX source-field collisions.
The lower count is not a valid improvement; V33 is rejected and the next
class must regenerate the complete four-net CM5 USB3 source field.

V34 regenerated all four CM5 USB3 source nets together with orthogonal
staggered F.Cu exits and existing B.Cu trunks. Native DRC reported 589
findings / 403 unconnected items but five true shorts, including a TX escape
into an adjacent no-net J7 pad and RX/XOUT field collisions. V34 is rejected;
the next source-field class must follow a reference-derived escape map.

V13 is the retained local routing basis. Its upper P-leg detour preserves the
V8 source ordering, reduces the USB_TXN1/USB_TXP1 skew proxy to 0.259 mm, and
keeps focused USB3, SATA, mode-control, JMS583-support, and pad-parity audits
passing with no native shorting class. Native DRC remains 730 findings; full
board closure is still open.

Fresh native validation of the actual VBUS parent on 2026-09-09 reproduces
USB3 10/10, SATA 12/12, mode-control 4/4, complete JMS583 support with its
negative control, and pad parity with zero mismatches. Its fresh native DRC
receipt reports 732 findings and 400 unconnected items; this is the current
parent baseline, while V13 remains a disposable local source-field basis.

V21 tested an outboard F.Cu escape for CM5_PERST to avoid storage USB
corridors. Native DRC rejected it: the new trunk terminates into no-net J1
pads and creates two true shorts, despite reducing the crossing count. It is
rejected low-speed route evidence. A native saved-board audit now confirms
that the intended CM5_PERST ownership is J7.109, TP8.1, and J1.E18, and that
the existing trunk already joins those three pads. V21 failed because its
outboard path crossed the no-net J1 pad field before reaching J1.E18; this is
not a source-authority defect and no further PERST reroute is needed.

V14 tested a small lateral shift of the TXN vertical leg. It retained all
focused endpoint/parity audits and reduced the TX skew proxy to 0.096 mm, but
native DRC found a 0.000 mm clearance violation from the diagonal escape into
U11 pad 23. V14 is rejected route-implementation evidence; V13 remains the
retained no-short local basis and no production copper changed.

V15 tested an ordinary through-via and B.Cu TXN escape from the U11 field. Its
focused USB3 endpoint audit passed, but native DRC rose to 746 and introduced
six TXP/TXN shorting findings plus additional support-field conflicts. V15 is
rejected route-implementation evidence. After the planar V14 and layer-
transition V15 failures, further isolated TXN nudges are stopped; the next
class must regenerate the complete native-pad-aware lower U11 field.

V16 tested a wider planar TXN dogleg. It removed the pad-23 clearance finding
and retained focused USB3 connectivity, but native DRC still found a 0.0925 mm
TXP/TXN source-field clearance violation. V16 is rejected route-implementation
evidence; V13 remains the retained basis pending coordinated lower-field
regeneration.

V17 regenerated both U11 USB TX nets together with the saved-board
obstacle-aware A* router. Endpoint connectivity passed and no native shorting
class was introduced, but the generated layer transitions raised native DRC
to 781 findings with 33 crossings and 281 clearance findings. V17 is rejected
route-implementation evidence; the A* method is not suitable for this dense
field without a complete hand-authored pad-field escape plan.

V20 moved the U11-to-C83 AVDDL branch through an ordinary-via B.Cu corridor.
It removed the prior AVDDL/USB-TX corridor crossing, but the new transition
via shorted to the existing USB_RXP1 B.Cu route; native DRC remained at 736.
V20 is rejected route-implementation evidence. AVDDL must be co-authored
with AVDD33 and the USB TX/RX escapes as one lower-field allocation.

V18 relocated C86/C87 into the U11/U12 gap and regenerated both sides of the
TX pair, but its direct U12 launch shorted into U12 POWER_GND pads; native DRC
reported 740 findings. V18 is rejected. V19 retained the proven U12-side
corridor while moving only the caps, but introduced real JMS_AVDD33/TX shorts
and 736 findings. V19 is also rejected; cap relocation alone is not a valid
escape class.

The first co-authored source-field trials are retained as route evidence. V3
kept USB3/SATA/mode/JMS583/parity focused gates passing and introduced no
shorting class, but native DRC identified two new local USB_TXP1/USB_TXN1
source-escape crossings. V4's asymmetric pair-layer handoff was worse at 734
DRC findings and retained crossing classes. Both are rejected implementation
variants; the VBUS V1 basis remains current and no production copper changed.

The consultant-recommended straight 0.20 mm pair test V5 removes the TX
self-crossing, but native DRC still reports a real `USB_TXP1`/`JMS_AVDDL`
short at the inherited AVDDL via. V6 moved that transition south and instead
introduced `USB_TXP1`/`JMS_AVDDL` and `USB_RXP1`/`JMS_AVDDL` shorts. Both retain
focused endpoint connectivity but are rejected route implementations. This
confirms that the next repair must allocate the complete U11 lower pad field
(USB2, USB TX/RX, AVDD33/AVDDL, and neighboring support) coherently.

The coherent C86/C87 relocation trial V1 is rejected route evidence. It kept
the focused USB3 and JMS583 support audits passing, but native DRC rose to
760 with real JMS_USB3_TXP/AVDD33 and JMS_USB3_TXN/USB_TXP1 shorts plus
additional crossings. Moving the coupling capacitors alone is therefore not
the complete-field solution; the VBUS V1 parent remains retained.

The coherent 180-degree JMS583/TX-island discriminator V1 is rejected route
evidence. Native DRC reports 805 findings with multiple QFN/support shorts,
and the focused USB3 audit loses the unchanged RX paths because the complete
local island was not regenerated. It does not alter Path A or the retained
VBUS parent; rotation remains a placement experiment, not production authority.

The QFN-neckdown V7 is rejected route evidence: a 0.15 mm package-edge
neckdown followed by normal-width USB TX routing preserves focused USB3
connectivity, but native DRC still finds a real USB_TXP1/JMS_AVDDL short at
the unchanged AVDDL via. Width-only variation is exhausted for this local
geometry; the next route must co-author the complete source-field/via map.

V8 is the retained local source-field basis. Its staggered, order-preserving
USB_TXP1/USB_TXN1 fanout keeps USB3, SATA, mode-control, JMS583 support, and
pad parity passing, with no native `shorting_items` class; native DRC reports
730 findings. It is not closure: inherited crossing/open/clearance/width and
full-board power/ground gates remain. No production copper changed.

The V10 local P-leg meander reduced the USB_TXN1/USB_TXP1 skew proxy to
0.259 mm, but native DRC found two real same-layer pair self-crossings. It is
rejected as route implementation evidence; pair matching must use a
layer-separated or shortened-leg corridor without weaving.

Saved-board route metrics show V8 leaves the CM5-side USB3 paths unchanged
and uses zero additional vias for USB_TXP1/USB_TXN1. Its local TX skew proxy
is 4.718 mm versus 4.400 mm on the VBUS V1 parent, so V8 is a clean-source
basis but not yet a pair-balance closure. The next candidate must preserve its
no-short local escape while co-authoring pair-length matching.

V9 is rejected as a micro-adjustment regression. Although focused USB3
connectivity remains passing, native DRC rises to 731 and introduces a real
`CM5_PET0_P`/`CM5_USB3_RX_N` short. V8 remains the retained parent.

The V11 shortened-TXN candidate is rejected: focused USB3 connectivity still
passes and TX skew proxy falls to 1.620 mm, but native DRC rises to 731 and
adds a CM5_USB3_RX_N/CM5_USB3_RX_P short. No production copper changed; this
also exposes serialization-safe whole-net regeneration as a prerequisite for
further local edits.

The installed storage USB3 router was also exercised against V8. Its focused
USB3 endpoint audit passes, but native DRC reports 734 findings with a real
`JMS_USB3_TXN`/`USB_RXP1` short. It is rejected route evidence; the router's
fixed channel assumptions are not suitable for this inherited corridor.

The USB3 negative-control run on V8 also passes: the intact native graph is
accepted, and removal of a required CM5 USB3 trace makes the audit fail as
required. This validates audit sensitivity, not Phase 24 closure.

## SUPERSEDED ROUTING SNAPSHOT — pre-VBUS/J8 basis

The following historical snapshot is retained for archaeology only. It is not
the current routing parent; the current parent is identified in the authority
section above.

The disposable `PHASE24_STORAGE_U12_EP_RX_PAIR_V6.kicad_pcb` is the latest
USB3 escape discriminator. It preserves the authoritative U11/Y10 clock
topology and re-escapes both U12 RX nets from ordinary B.Cu vias outside the
HD3SS6126 exposed-pad field, with F.Cu dogbones to U12. Native USB3
connectivity is PASS (10/10), SATA is PASS (12/12), JMS583 support is PASS,
and schematic-to-PCB pad parity is PASS (0 mismatches) against
`PHASE24_U12_EP_GROUND_V6.kicadxml`. Native DRC reports 684 violations / 403
unconnected items and no `shorting_items`; it is retained as the current
route basis, not yet a closure candidate. The mode-control native audit still
reports the inherited J3.69-to-J5.2 open, so mode routing remains an open gate.

The V1--V5 U12 RX escape and XOUT-corridor trials remain rejected route
evidence. V6 is the first candidate in this sequence that removes the U12
exposed-pad short without adding a native short; its raw PCB and DRC receipt
are retained. Next action: repair the mode-control route and then continue
native full-board closure from V6, preserving negative-control requirements.

The mode-control audit also exposed a genuine reference-identity defect in
the disposable integration: storage override J5 collided with the unrelated
power-input J5, leaving the saved PCB's J5 as the power header rather than
the mode jumper. The authoritative `STORAGE.kicad_sch` symbol is now J8,
and `PHASE24_STORAGE_MODE_J8.kicadxml` proves J3.69 and J8.2 share
`/STORAGE/AUTO_PEDET`. The next regenerated candidate must instantiate J8
and route J3.69/J8.2 and J8.4/U14.2; no PCB-only net relabel is promoted.

The first J8 materialization probes are rejected disposable implementations:
V1 overlapped the power-input J5, while V2 moved J8 outboard but still
introduced native mode/selector and inherited U12/connector short classes.
The native 4/4 mode graph passed in both, confirming the source fix; neither
route is promoted. V6 remains the clean routing basis while J8 and its mode
routes are regenerated with collision-aware placement.

The coordinated source-regenerated candidate
`PHASE24_STORAGE_NETLIST_REGENERATED_J8_V5.kicad_pcb` is now the current
storage routing basis. It materializes source-owned J8, routes AUTO_PEDET
and MODE_IN to J8, and regenerates the complete U12 CM5 USB3 quartet with
ordinary transitions outside the exposed-pad field. Native USB3 connectivity
passes 10/10, SATA passes 12/12, JMS583 support and its negative control
pass, mode control passes 4/4, and pad parity against
`PHASE24_STORAGE_MODE_J8.xml` is zero mismatches. Native DRC reports 708
violations / 403 unconnected items with zero `shorting_items`. This closes
the prior U12/J5 authority and shorting classes but remains open for the
unconnected-item, clearance, crossing, and full-board gates.

The focused VBUS/sense repair candidate
`PHASE24_STORAGE_J8_V5_VBUS_V1.kicad_pcb` is now the current storage basis
for the next closure pass. It routes U11 VBUS/sense to the source-owned R82/R83
divider with an explicit midpoint segment and passes the native VBUS audit plus
trace-removal negative control. USB3, SATA, mode control, and JMS583 support
audits also pass. Native DRC reports 732 violations / 400 unconnected items
with zero `shorting_items`. It is not closure: remaining storage support
opens, clearances, crossings, and full-board power/ground connectivity remain.

The disposable `PHASE24_STORAGE_J8_V5_STORAGE_SEL_V1` reroute passes the
4/4 native mode-control graph but is rejected: native reload exposes three
inherited short classes in CM5 RX and SATA/USB3 copper, while no reported
short is the intended selector corridor. This confirms that modifying a
single net on the inherited board is not a reliable closure method. The next
repair must regenerate the affected source-owned selector and neighboring
high-speed corridors together, with native post-save DRC as the authority.

An unchanged `PHASE24_STORAGE_J8_V5_VBUS_ROUNDTRIP` remains zero-short after
native save/reload, so this is not a generic serializer defect. The selector
V2 no-net-table-rebuild probe still exposes three inherited crossing shorts
after adding the new corridor. V1 and V2 are rejected; the VBUS basis is
unchanged and neighboring high-speed copper must be regenerated together.

The coordinated `PHASE24_STORAGE_J8_V5_COAUTHORED_SEL_USB3_V1` transaction
is rejected route evidence: USB3 endpoint connectivity passed, but native
DRC reported four true shorts, including `STORAGE_SEL` against the SATA
corridor and inherited USB3 source-field crossings. No copper was promoted;
the next credible class is a clean source-owned storage high-speed corridor
regeneration.

Selective width normalization was tested on storage high-speed nets. It
removed 34 width findings but left 147 inherited width findings and introduced
a real `JMS_AVDDL`/`USB_TXP1` short, so it is rejected. Global and selective
widening are not promoted; width cleanup must be co-authored with each local
support field and revalidated by native DRC.

The local `USB_TXP1` 0.20 mm escape probe is rejected as a complete route:
native USB3 connectivity passes and no shorting class is introduced, but the
new dogleg adds support-field crossings. Width cleanup must co-author both
USB_TXP/USB_TXN with the adjacent JMS_AVDDL field.

The bounded `PHASE24_STORAGE_J8_V5_GROUND_ZONE_V1` probe adds a storage-only
F.Cu `POWER_GND` zone and reduces native unconnected findings to 386 from
400, with zero native shorts. It is retained as a ground-access experiment,
not promoted yet: its effect on the approved reference-plane/layer contract,
signal impedance, and remaining clearance/DFM findings must be reviewed.

The source-driven J8 regeneration (`PHASE24_STORAGE_NETLIST_REGENERATED_J8_V1`
and V2) confirms J8 is materialized with the correct four source nets and the
native mode audit passes 4/4. Both are rejected routing candidates: V1 still
carried the inherited old-J5 mode track, and V2's corrected mode routes
re-exposed stale U12 TX pad-field shorts plus an AUTO_PEDET-to-socket-ground
collision. These are copper regeneration/escape defects, not a reason to
revert the source J8 correction or reject the storage architecture.

## CURRENT STATE — 2026-09-08

The Y10 local-crystal relocation trial is rejected route evidence: it rebuilt
the live U11/XIN-XOUT-to-Y10 neighborhood but produced 695 native DRC
violations and five true shorts. It passes the USB3 endpoint audit, but does
not improve the integrated corridor. The live source remains U11/XIN-XOUT to
Y10; no blind clock relocation is promoted.

The live source-authority repair for the HD3SS6126 USB selector is complete:
its QFN exposed pad 43 is now an explicit schematic `POWER_GND` pin, with a
matching U12 instance pin and source-generator mapping. Native KiCad export
`PHASE24_U12_EP_GROUND_V6.kicadxml` contains U12.43 on `POWER_GND`; native ERC
has no hierarchy-association errors. The corrected source-driven candidate
`PHASE24_STORAGE_NETLIST_REGENERATED_V5.kicad_pcb` assigns U12 pad 43 to
`POWER_GND`, has zero schematic-to-PCB pad-parity mismatches, and passes the
complete dual-mode USB3, SATA, and JMS583 support audits including the saved
board negative control. Its native DRC receipt reports 685 violations / 403
unconnected items and remains open routing evidence. It is not yet the
production acreage candidate. The next action is clean U12 source-field USB3
escape/rerouting against this corrected authority; no synthetic connectivity
or severity waiver is permitted.

The older V2/V3 regeneration paragraphs below are retained as superseded
route evidence only. They are not current TODOs or the current candidate.

The U12 RX_N target-escape trials against V5 are also route evidence only.
Trial 2 retained the U12 exposed-pad short; trial 3 moved the ordinary via
outside the exposed pad but still shorted/crossed the existing XOUT corridor;
trial 4's local B.Cu dogleg changed the conflict to an inherited USB3/SATA
crossing. All three pass the ten-net native USB3 connectivity assertions but
are rejected route implementations. The next attempt must change the local
source/target escape corridor rather than add another narrow dogleg.

The V5 all-four-net layer-aware A* trial is rejected route implementation
evidence: native endpoint connectivity passed, but the generated transitions
produced 841 DRC violations and 16 true shorts. Its clearance model is not
suitable for this dense inherited corridor; this does not reject the corrected
storage authority or macro-floorplan.

Clock-source reconciliation is closed at the source level: native export
`PHASE24_CLOCK_RECONCILED_V2.kicadxml` proves `U11.50/51` connect to the live
`Y10.1/2` crystal, with Y10's return pads on `POWER_GND`. The older Y1 clock
island remains separately aliased and is not paralleled. The regenerated V2
clock-reconciled board returns to the 685/403 baseline with the known U12
exposed-pad route short, so the attempted Y1 label join is rejected and is
not a current routing requirement.

## CURRENT OPEN GATES — 2026-09-08

### Latest source-regenerated routing basis

`PHASE24_STORAGE_NETLIST_REGENERATED_V2.kicad_pcb` is the latest disposable
source-regenerated storage candidate. It preserves the prior routed geometry,
adds the source-required Ethernet support passives, normalizes hierarchical
track names, and applies native schematic node ownership including the EDAC
J2 physical alias map. Its parity audit reports 0 expected-pad mismatches;
dual-mode USB3 reports PASS, SATA reports PASS for all 12 endpoints, and the
JMS583 support audit plus trace-removal negative control report PASS. Native
DRC reports 700 violations / 399 unconnected items and 7 true
`shorting_items`, caused by normalizing inherited hierarchical copper without
rerouting the affected corridors. It is rejected route evidence, not a
closure candidate; no V2 copper is promoted.

### Current source-authority repair

The disposable `PHASE24_STORAGE_USB3_SELECTOR_ASTAR_V1.kicad_pcb` trial is
rejected. Its obstacle-aware source-to-U12 search produced disconnected
launches and multiple pad-field shorts (802 native DRC violations); it used
an invalid via/pad escape model. It does not alter the source-authoritative
storage decision. The V3 netlist-regenerated candidate remains the cleanest
source-owned basis while the CM5 USB3 launch is re-authored with explicit
non-via-in-pad dogbones.

The follow-up `PHASE24_STORAGE_USB3_SELECTOR_ASTAR_V3.kicad_pcb` used explicit
F.Cu dogbones to ordinary vias and passes the ten-net native USB3 audit, but
native DRC still reports source-field via/adjacent-pad shorts (846 total
violations / 402 unconnected items). It is rejected as route evidence; the
next source escape must use the CM5IO-derived stagger/clearance geometry.

The FULL7 geometry transplant
`PHASE24_STORAGE_USB3_FULL7_SOURCE_REPAIRED_V1.kicad_pcb` was tested against
the source-regenerated V3 basis. The four-net native USB3 audit passes, but
donor geometry is not directly transplantable: native DRC reports 689
violations / 402 unconnected items with connector-body and inherited
cross-net shorts. It is rejected as donor evidence; transformed target pads
must be re-escaped locally using the same topology, not copied blindly.

The shifted CM5IO-style trial
`PHASE24_STORAGE_USB3_CM5IO_SHIFTED_V1.kicad_pcb` is rejected. It avoided
the SXM2 body but crossed existing REFCLK/XIN/XOUT and SATA corridors; native
DRC reports 708 violations / 402 unconnected items with true shorts. This
confirms the remaining issue is local corridor allocation, not endpoint or
source-net authority.

`CORE_CM5.kicad_sch` now exposes its 51 CM5 ground labels as native global
`POWER_GND` labels. This is a source-level repair for the previously observed
`/CORE_CM5/POWER_GND` versus board-plane `POWER_GND` split; no PCB-only merge
was promoted. Native export receipt
`PHASE24_CORE_CM5_GLOBAL_GROUND.xml` contains one `POWER_GND` net with 154
nodes, including J7 ground contacts. The matching ERC receipt has zero
hierarchy-error tokens and the same 23 pre-existing multiple-name warnings as
`PHASE24_ROOT_ERC_LIVE.rpt`. Disposable board-side reconciliation
`PHASE24_CM5_GROUND_FLATTENED_DISPOSABLE.kicad_pcb` retains zero shorting
items, but still has 499 unconnected items because it is not regenerated
authoritative copper. The remaining gate is to regenerate/validate the active
storage workbench from this source authority and re-run native full-board
connectivity; until then the ground repair is `SOURCE_VALIDATED,
PCB_REGENERATION_OPEN`.

The J7 ground-return-via probe `PHASE24_J7_GROUND_RETURN_VIAS_V1.kicad_pcb`
is rejected. It added 51 ordinary offset vias, but J7 lands use native
`/CORE_CM5/POWER_GND` while the existing planes use `POWER_GND`; PCB-only
flattened-net vias were not a valid authority-preserving repair. Native DRC
retained 499 unconnected items and added clearance/short findings. No ground
net merge or copper was promoted.

The endpoint-safe layer-aware search with selector-side copper retained,
`PHASE24_STORAGE_SATA_SAFE_EXITS_V2.kicad_pcb`, passes all 12 native SATA
endpoint assertions and avoids storage-local true shorts. It still has a U7
source-field crossing; native DRC reports 676 violations / 499 unconnected
items plus one inherited non-storage short. It is rejected as an integrated
candidate, while the safe-exit authoring method is retained.

The coherent storage-island transplant
`PHASE24_STORAGE_COHERENT_ISLAND_V1.kicad_pcb` was reauthored against the
live Path-A capacitor net ownership, but native SATA audit failed at
`TUSB_SATA_RXP` because its historical socket-side template did not terminate
on the current U13 pad geometry. Native DRC reports 802 violations / 499
unconnected items with multiple crossings and shorts. It is rejected stale
route evidence; no copper was promoted.

The latest bounded SATA source-field experiment,
`PHASE24_STORAGE_SATA_SOURCE_ORDER_V1.kicad_pcb`, is rejected route
implementation evidence. It used native U7 pad coordinates and an
order-preserving C30--C33 row; the corrected probe passes all 12 native SATA
endpoint assertions, but creates real selector-field shorts/clearances and
reports 612 DRC violations / 499 unconnected items. Its raw PCB and DRC
receipt are retained. It does not replace the active no-short
`PHASE24_STORAGE_VCCK_LOCAL_V1` basis.

The layer-aware native-pad A* SATA trial
`PHASE24_STORAGE_SATA_ASTAR_V1.kicad_pcb` is also rejected route
implementation evidence. It passes all 12 native SATA endpoint assertions
and corrects the search model to block pads only on their saved copper layers,
but native DRC reports 822 violations with real SATA-to-power/support shorts
and crossings. No A* copper was promoted; its raw PCB, report, and author are
retained for future routing work.

The post-escape SATA corridor trial
`PHASE24_STORAGE_SATA_POST_ESCAPE_V1.kicad_pcb` preserves the known-good U7
dogbones and changes only the B.Cu corridors. It passes all 12 native SATA
endpoint assertions and reduces the aggregate DRC count to 583, but native
DRC reports three true shorts, including TUSB SATA copper entering the
JMS_REXT/USB3 field. It is rejected route implementation evidence; no copper
was promoted.

The minimal TXN-via-spacing trial
`PHASE24_STORAGE_SATA_TXN_VIA_SPACING_V1.kicad_pcb` passes all 12 native
SATA endpoint assertions and reduces the aggregate DRC count to 575, but
native DRC finds a true TXP/TXN short at the U7 source-field escape. It is
rejected route implementation evidence; no copper was promoted. Repeated
source-field via nudges are exhausted as a solution class, so the next trial
must change the local escape topology or move the coherent U7/coupler
sub-island.

The latest integrated storage routing candidate is
`PHASE24_STORAGE_VCCK_LOCAL_V1.kicad_pcb`, derived from the corrected
source-authoritative workbench with M.2 launch V6, selector-side SATA escape
V4, native mode-control routing, corrected CM5 USB3 right-side launches, and
destination-only VCCO relocation plus the local VCCK corridor repair. It passes the topology-aware
dual-mode USB3 audit (10/10), SATA endpoint audit (12/12), mode-control audit
(4/4), schematic-to-PCB pad parity (0 mismatches), and JMS583 VDDREG/REXT
audits, with saved-board MODE_IN and VCCO negative controls that fail as
required. Native DRC remains open at 669 violations / 499 unconnected items; this is
the current routing workbench, not a closure candidate.
Fresh native recheck reproduces 669 violations / 499 unconnected items with
zero `shorting_items`; topology-aware USB3, SATA, and mode-control audits
remain PASS. The remaining work is not waived: crossings, clearances,
unconnected endpoints, and full-board closure remain open.

The live U13 source-authority regression is corrected. U13 pins 6/7 now own
`M2_SATA_B_P_PCIE_RXN0` / `M2_SATA_B_N_PCIE_RXP0`, matching J3 contacts 41/43;
the earlier lane-1 ownership was a superseded generator/source defect, not a
current SATA requirement. Fresh native export and regenerated PCB pad parity
report zero expected-pad mismatches. The SATA corridor author was also
corrected to anchor every selector escape at the saved native U13/J3 pads.
The disposable `PHASE24_DUAL_MODE_STORAGE_U13FIX_SATA_V2` candidate passes all
12 native SATA endpoint assertions. Its native DRC remains open at 734
violations / 499 unconnected items, so it is routing evidence and not a
Phase 24 closure candidate. Remaining gates include complete support-copper
integration, mode-aware switched connectivity, native ERC/DRC cleanup, and
full-board regression.

The refreshed live-authority workbench is
`PHASE24_STORAGE_AUTHORITY_CORRECTED_USB3_SATA.kicad_pcb`. It was regenerated
after the U13 source fix, carries the native JMS583 support author, and passes
all 12 SATA endpoint assertions. The native USB3 promotion path now resolves
child `/CORE_CM5/` names against either target spelling; its CM5 source
quartet is connected, while bridge-side USB3 endpoints still require the
remaining route promotion. Native DRC is 1,027 violations / 499 unconnected
items on this immature workbench. Do not compare that count to mature
historical candidates as a floorplan judgment.

The corrected source-authoritative rebuild is now
`PHASE24_STORAGE_MODEAUTH_USB3_ALIGNED_SATA_SUPPORT_ZONES_V1.kicad_pcb`.
It has zero schematic-to-PCB pad-net parity mismatches and passes the complete
ten-net USB3 audit, all 12 SATA endpoint assertions, and the complete JMS583
support audit with its negative control. Native DRC remains open at 681
violations / 499 unconnected items, including
inherited crossings and shorts; this is not a closure candidate.

The earlier 669-count workbench is superseded as a live basis because its
J3.69 and U12.9 PCB ownership predated the corrected embedded symbol
definitions.

The first native-pad-aware replacement of the four U13-to-J3 lane-0 launches
was tested as `PHASE24_STORAGE_M2_LAUNCH_V1/V2`. V2 reduced the total DRC
count to 647 but introduced true socket-ground collisions, a pair-to-pair
short at the B.Cu TX escapes, and adjacent support-field conflicts. Both
variants are rejected route implementations. The corrected
`PHASE24_STORAGE_MODEAUTH_USB3_ALIGNED_SATA_SUPPORT_ZONES_V1` workbench
remains the active basis; no M.2 launch copper was promoted.

Launch V3/V4 are additional rejected route implementations. V3 removed the
connector-ground collision class but retained a source-field pair short; V4
staggered source vias farther but crossed adjacent U13 pads. The current
disposable `PHASE24_STORAGE_M2_LAUNCH_V6` removes the M.2-specific short
classes and passes the 12-endpoint SATA audit, but remains evidence only.
The separate selector-side escape V3/V4 then reauthored all four C30--C33 to
U13 branches with actual capacitor-side F.Cu-to-B.Cu vias. V3 passes the
native 12-endpoint SATA audit; V4 is the latest candidate and still has
unrelated inherited USB3/support shorts and crossings. Neither is promoted.
V5 was a rejected multi-bend variant: it retained SATA endpoint PASS but
introduced additional same-layer route crossings and via/track conflicts.
The integrated VCCO source-transition V6/V7 trials are also rejected: V6
removed the C86 launch collision but retained the VCCO/VCCK field conflict;
V7 moved the source transition and increased native DRC to 677 while the
same VCCO/VCCK short remained. V4_MODE is superseded by the later
VCCK_LOCAL_V1 integrated workbench.
V8 rerouted VCCK around the VCCO transition but introduced new CM5_5V and
JMS_PCIE_TXP0 crossings/shorts and raised native DRC to 680; it is rejected.
An all-F.Cu VCCO V1 trial reduced the aggregate DRC to 670 but introduced
real U12 no-net/USB launch shorts and additional crossings; it is rejected.
VCCO destination V2 moved the source via down the QFN edge but introduced a
JMS_SPI_CS_N_DNP pad short and raised native DRC to 675; it is rejected.
The VCCK local V1 corridor removes the VCCO/VCCK and RESET_N/VCCK shorts,
retains both rail endpoint negative controls, and reduces native DRC to 669.
Selector-side V10/V11 tested separated upper/lower TXN/RXN corridors. They
removed the original selector pair crossing but introduced outboard
M.2/mode/ground conflicts and raised native DRC to 670; both are rejected.
U12 JMS USB3 TX fanout V1 retained the dual-mode USB3 endpoint audit but
introduced multiple U12 no-net/USB/M.2 short classes despite a numerical DRC
count of 664; it is rejected. The VCCK-local V1 basis remains current.
USB3 skew-tune V1 reduced RX proxy skew to 2.123 mm and TX proxy skew to
2.400 mm, but introduced real JMS support/selector shorts and crossings;
it is rejected pending a reserved support-via corridor.
Selector SATA RXN compact-jog V12 reduced the selector RX pair mismatch from
31.46 mm to 13.53 mm and passed native SATA with no shorting items, but it
remains a disposable geometry because pair balance and full DRC are open.
V13's added upper-field meander created M2 SATA and USB/support shorts and
was rejected.
SATA RXN balance V14 achieved a 3.66 mm RX mismatch and native SATA PASS,
but reintroduced two TUSB/USB-RX transition-via shorts; it is rejected.
USB RX endpoint-via relocation V1/V2 preserved USB and SATA endpoint PASS but
introduced U12 pad-43 and USB-RX pair shorts, raising native DRC to 681; both
are rejected. The VCCK-local no-short basis remains current.

Selector-side V9 moved only the TXP corridor above the inherited support
field; it removed the prior TXP/USB_RXN1 collision but introduced new XIN,
CM5_USB3, and support conflicts and raised DRC to 677. It is rejected.

The integrated REXT repair discriminator is complete as a bounded experiment.
V1's ordinary-via escape removed the original U11.40/U11.39 short but
introduced new QFN-ground/power clearances; V2's no-via perimeter escape
retained the 669-count DRC and still contacted the adjacent POWER_GND field.
Both are rejected route implementations. This historical discriminator is
superseded by the VCCK_LOCAL_V1 integrated workbench and its current open
gates above.

Mode-control source ownership is now corrected: J3 contact 69 and J5's AUTO
leg export on native `AUTO_PEDET`, and the regenerated mode-fix placement
passes pad parity and the mode-contract audit. A native mode-aware fixture
covering forced SATA, forced NVMe, AUTO, empty socket, reset, and inactive
paths is still required.

The selector-control source ownership is also corrected: U12 pin 9 now uses
the same `STORAGE_SEL` net as U13.9 and U14.4, eliminating the prior isolated
`USB_SEL` control. Fresh native export, mode audit, and regenerated placement
pad parity pass. The latest disposable physical mode-control fixture
`PHASE24_STORAGE_MODEFIX_MODE_ROUTE_V5.kicad_pcb` has native saved-board
connectivity for all four asserted control endpoint groups, and its negative
control fails after removal of a required `MODE_IN` track. Its native DRC is
still open at 832 violations / 499 unconnected items, including a genuine
`MODE_IN`/`STORAGE_SEL` crossing and inherited fixture findings; it remains
route evidence, not mode closure. The mode-aware inactive-state and full
integrated-board checks remain open.

After the USB3 coupling-capacitor alignment, the ten-net native USB3 audit
passes on the corrected support parent. The integrated
`PHASE24_STORAGE_AUTHORITY_CORRECTED_USB3_SATA_V3` trial also passes all 12
SATA endpoints. It is not promoted: the parent carries direct support routes
but not the earlier zone-backed AVDDL/VCCO/VCCK coverage, so those support
checks fail on missing physical copper. The SATA author was corrected to
preserve all non-SATA tracks/zones in integrated mode; only `MINIMAL=1`
fixtures scrub the board.

## AUTHORITATIVE CURRENT STATE — 2026-09-08

The JMS583 support-label authoring path was corrected and applied to the live
source: support labels now use the canonical `JMS_REXT`, `LXO`, `XIN`, and
`XOUT` nets with the native KiCad serialization order. The native endpoint
overlap repair removed stale generated label atoms at the U11 pin-12/pin-39
endpoints, and the shared-selector pin maps no longer override pin 39 with
`JMS_GPIO7_NC`. The regenerated `PHASE24_DUAL_MODE_STORAGE_PLACEMENT_NC39`
candidate now passes the native schematic-to-PCB pad-net parity audit with
zero expected-pad mismatches. Native ERC/DRC and complete routing remain
open; the current regenerated placement candidate's native DRC is 857
violations / 499 unconnected items, so parity PASS is not a Phase 24 pass.
The earlier 797-violation result belongs to a superseded candidate and is not
the current baseline.

The 203 duplicate generated label UUIDs have now been reconciled uniquely in
the live source. The schematic backend loads successfully. The earlier
two-item R80.1/U11.39 association mismatch is superseded by the endpoint
overlap repair and NC39 map correction; its raw probes remain historical
evidence. The migration is idempotent and fail-closed.

The native root schematic export `PHASE24_ROOT_NATIVE.xml` independently
resolves all four CM5 USB3 nets to canonical names and to J7 pins
128/130/140/142, U12 pins 16/15/12/11, and U7 pins 42/43/45/46. The reusable
PCB authoring path normalizes donor `/CORE_CM5/` aliases to those canonical
names before placement. This closes the aliasing ambiguity in the authoring
path; the disposable candidate is not claimed as fully connected.

Independent live-source checks currently pass: dual-mode schematic/library
authority, exact JMS583/selector/M-key pad counts, authoritative component
maps, selector truth table (`SATA=0`, `NVMe=1`), and mode contract. These
checks do not waive the still-open native copper/DRC closure.

Fresh native root schematic ERC on the current source reports 925 violations.
The older 927 count is retained only as historical evidence. The
post-fix report has no dangling M.2 labels; remaining findings are inherited
off-grid, same-label, symbol, footprint-link, and connectivity warnings. The
raw report is retained as an open ERC gate; the USB3 endpoint audit does not
waive it. The six isolated legacy M.2 labels named in the prior report were
removed from the child-sheet source, while the total remains 927 because the
independent inherited findings remain.

Saved-copper metrics for FULL7 are recorded in
`PHASE24_DUAL_MODE_STORAGE_NC39_USB3_FULL7-metrics.txt`. The source legs have
three vias each and measured length proxies of 149.160/145.160 mm (RX N/P)
and 141.960/137.960 mm (TX N/P); local bridge legs are shorter but unequal.
These are diagnostic measurements, not a controlled-impedance or skew pass.

The live USB3 map audit then found and corrected a second source-authority
defect: U12 TX pins 24/25 are the bridge-side `JMS_USB3_TXN/P` nets across
C87/C86, while U12 RX pins 22/23 remain direct `USB_RXN1/P` bridge links.
The regenerated `PHASE24_DUAL_MODE_STORAGE_NC39_USB3_FULL7` candidate passes
all ten native USB3 endpoint assertions. Its native DRC reports 827
violations / 499 inherited unconnected items; three inherited J1 launch
shorts and local track crossings remain, so it is routing evidence only.
FULL5 and FULL6 are superseded routing evidence.

The native-pad A* source-router trial `PHASE24_DUAL_MODE_STORAGE_NC39_ASTAR_FULL`
is rejected: endpoint connectivity passed 10/10 and crossings fell to 6,
but native DRC reported 929 violations and 25 shorts. It remains route
implementation evidence only; FULL7 is the active basis.

The coherent U12 translation trial `PHASE24_DUAL_MODE_STORAGE_U12_X148_FULL`
is rejected: native USB3 endpoint connectivity remained 10/10, but native
DRC reported 851 violations, 8 shorts, and 15 crossings. The translation is
preserved as negative placement evidence; FULL7 remains active.

The source-launch relocation trial `PHASE24_DUAL_MODE_STORAGE_NC39_USB3_FULL10`
is rejected: native connectivity still passed, but inward launch vias created
new shorts into J1 12V pads and the U11 ground pad. It is preserved as a
route-implementation negative result; FULL7 remains the active basis.

The U12 180-degree rotation trial `PHASE24_DUAL_MODE_STORAGE_NC39_U12_ROT180_FULL`
is rejected: all ten native USB3 endpoint assertions still pass, but native
DRC rises to 845 violations with six shorts and 19 crossings. Rotation is
therefore not promoted; FULL7 remains the active route basis.

The U11 180-degree rotation trial `PHASE24_DUAL_MODE_STORAGE_U11_ROT180_FULL`
is rejected: native USB3 endpoint assertions remain 10/10, but native DRC
reports 843 violations, 7 shorts, and 21 crossings. It is negative placement
evidence; FULL7 remains the active basis.

The TX source-launch relocation FULL14 is rejected: native USB3 endpoint
assertions remained 10/10, but moving the columns inward produced 832 DRC
violations, 5 shorts, and 19 crossings, including new J1/U11 collisions.
The source-launch generator is restored to the FULL7 columns.

The alternate CM5 source-layer trial `PHASE24_DUAL_MODE_STORAGE_NC39_USB3_ALT_FULL`
is rejected: native USB3 endpoint assertions passed 10/10, but native DRC
reported 851 violations, 4 shorts, and 18 crossings. The all-B.Cu source
escape is restored and FULL7 remains active.

TX dogbone trials FULL12/FULL13 are rejected route implementations. FULL12
reduced the DRC count to 830 but retained a local TXN/RXP-via short; FULL13
shifted the dogbone and produced four shorts with 832 DRC violations. The
active generator is restored to the FULL7 geometry.

`phase24_usb3_negative_control.py` validates the accepted FULL7 audit against
the saved PCB: baseline native connectivity passes, and removing one required
CM5_USB3_RX_N track makes the audit fail as required. This hardens the
connectivity evidence without treating the route as closed.

The local USB3 router was corrected to default to the saved FULL7 native
authority. A trial from the older canonical placement export was rejected by
native connectivity because U12.24/U12.25 still carried stale USB_TXN1/P net
ownership; no PCB-only ownership repair was applied. Re-running from FULL7
passes all ten native endpoint assertions and reports 830 DRC violations / 499
unconnected items. It is the current USB3 routing basis, not a Phase 24 pass.
The same candidate passes the saved-board USB3 negative control: removing a
required CM5_USB3_RX_N track makes the native connectivity check fail.

A disposable composite of the corrected USB3 basis with the existing JMS583
support-cohort author was rejected. The support endpoint audit and its
trace-removal negative control pass, but native DRC reports 870 violations /
499 unconnected items and new local conflicts where the hard-coded support
placement overlaps the USB3 field, including a JMS_USB3_TXN/USB_RXP1 short.
This is route/placement implementation evidence only; the clean USB3 basis
remains active and the support cohort must be co-authored around it.

The follow-up north-side support co-author was also rejected. Its native
support endpoint and trace-removal audits pass, but native DRC reports 924
violations / 499 unconnected items with new support-to-USB, XIN/AVDD33, and
XAVDDH return conflicts. This confirms that support placement and USB3 escape
must be allocated jointly with native obstacles; the north translation alone
is not a viable route.

The first native-pad A* support allocator was also rejected. After correcting
its obstacle model to retain every non-current endpoint pad, the allocator
needed a bounded 2 mm terminal halo to escape the dense QFN; native DRC then
reported 1,013 violations with real support-to-pad shorts. This is a router
model/escape-allocation failure, not an electrical or macro-placement result.
The next allocator must use per-pad legal escape corridors and preserve
neighboring QFN fields even within the active terminal halo.

Transplanting the verified JMS583 support primitive onto the unmodified FULL7
USB3 source basis was also rejected as an integrated route. Support endpoint
and negative-control checks pass, but native DRC reports 917 violations,
including the inherited CM5 findings, a real JMS_XAVDDH/CM5_USB3_TX_N
collision, and local XIN/XOUT via-clearance. The support primitive remains
valid in isolation; its three QFN edge exits must be regenerated in-place
around the USB3 copper.

The focused three-exit transplant (`PHASE24_DUAL_MODE_STORAGE_FULL7_THREE_EXITS`)
passes native XIN/XOUT/XAVDDH endpoint connectivity and the XIN removal
negative control, but is rejected as an integrated route: native DRC reports
851 violations / 499 unconnected items, including a real XAVDDH-to-
CM5_USB3_TX_N collision. The remaining repair is the in-place XAVDDH exit;
the crystal endpoint geometry itself is not the blocker.

The in-place left/up XAVDDH repair is promoted as the current support/USB3
integration basis: `PHASE24_DUAL_MODE_STORAGE_FULL7_XAVDDH_LEFT_EXIT`. Native
XIN/XOUT/XAVDDH connectivity and the XIN-removal negative control pass, all
ten USB3 endpoint assertions pass, and native DRC reports no authored
shorting or track-crossing class. The report still contains 853 total
violations / 499 unconnected inherited items, so this is not full Phase 24
closure.

The current support/USB3 basis now includes the native-pad-aware REXT and
JMS_RESET_N repairs as `PHASE24_DUAL_MODE_STORAGE_FULL7_RESET`. Native
U11.15-to-R81.1-to-C85.1 connectivity and the reset trace-removal negative
control pass; REXT, XIN/XOUT/XAVDDH, and all ten USB3 endpoint checks remain
passing. Native DRC reports 863 violations / 499 inherited unconnected items
with no authored shorting or track-crossing class. Remaining support rails,
SATA, mode-state, and full-board gates remain open.

The current basis also includes the validated lateral REXT addition as
`PHASE24_DUAL_MODE_STORAGE_FULL7_REXT`. Native U11.39-to-R80.1, XIN/XOUT/
XAVDDH, and all ten USB3 endpoint checks pass with their trace-removal
controls. Native DRC remains 853 violations / 499 inherited unconnected
items with no authored shorting or track-crossing class. This closes only the
REXT/three-exit/USB3 primitive, not the full support network or Phase 24.

The current basis now includes the upper native-pad-aware `JMS_AVDD33` repair
as `PHASE24_DUAL_MODE_STORAGE_FULL7_AVDD33`. U11.19-to-C80.1 connectivity and
the AVDD33 trace-removal negative control pass; REXT, RESET_N, XIN/XOUT/
XAVDDH, and all ten USB3 endpoints remain passing. Native DRC reports 876
violations / 499 inherited unconnected items with no authored shorting or
track-crossing class. Remaining support rails and storage gates remain open.

The current support-routing basis also includes the all-F.Cu `JMS_VCCK`
repair `PHASE24_DUAL_MODE_STORAGE_FULL7_VCCK_F_center.kicad_pcb`. Native
U11.2-to-C82.1 connectivity and its trace-removal negative control pass.
Native DRC reports 877 violations / 499 inherited unconnected items, with no
new VCCK short or crossing relative to the AVDD33 parent. Other support rails,
mode control, storage routing, and full Phase 24 gates remain open.

The native inventory confirms REXT, XIN, XOUT, RESET_N, AVDD33, and VCCK are
connected on this basis. The saved AVDDL/VCCO/VDDREG_5V/LXO support receipt
and local-zone candidates now cover the remaining rail endpoints; their first
failed corridors remain route-implementation evidence only. The support
primitive is not yet promoted as integrated production copper.

The VCCO path is now promoted through the local F.Cu power-copper candidate
`PHASE24_DUAL_MODE_STORAGE_FULL7_VCCO_rectangle_zone.kicad_pcb`. Native U11.6
to C81.1 connectivity and the zone-removal negative control both pass using
`phase24_jms583_vcco_zone_audit.py`. Native DRC reports 514 findings, with no
VCCO-authored short/crossing class; the remaining short and crossing classes
are inherited from the parent basis. This is power copper only, not a
signal-plane exception.

The VDDREG rail is now promoted on
`PHASE24_DUAL_MODE_STORAGE_FULL7_VDDREG_local_zone.kicad_pcb` as a local
F.Cu power-copper zone between native U11.1 and L10.2. The zone-aware native
audit and zone-removal negative control pass. Native DRC remains 514 findings
with no VDDREG-authored short/crossing class; the remaining support rails and
full storage gates remain open.

The shared inductor LXO path is promoted on
`PHASE24_DUAL_MODE_STORAGE_FULL7_LXO_below_vddreg.kicad_pcb`. The native
U11.64-to-L10.1 endpoint audit and trace-removal negative control pass. Native
DRC remains 514 findings with no LXO-authored short/crossing class. The
remaining support opening is AVDDL plus higher-level storage/mode/board gates.

The FULL11 attempt to cross the CM5_PERST corridor with local TX vias is
also rejected: it reduced some crossings but raised native DRC to 845 and
introduced additional local clearance/crossing findings. FULL7 remains the
best current USB3 basis.

The current native-pad support routing trial is rejected: native DRC reports
834 violations and 499 inherited unconnected items, including authored
support crossings. It remains disposable evidence only. The structural
JMS583 support audit and its removed-R80 negative control both pass after
updating the audit to the canonical `LXO`/`XIN`/`XOUT` names.
The corrected NC39 candidate was then replayed with the same direct support
author as `PHASE24_DUAL_MODE_STORAGE_NC39_SUPPORT_TRIAL.kicad_pcb`. Native DRC
reports 836 violations / 499 unconnected items, including a real
`JMS_REXT`-to-`JMS_AVDDL` short and authored support crossings. It is rejected
route evidence; the source/parity correction remains valid.
The subsequent coherent native-pad support cohort,
`PHASE24_DUAL_MODE_STORAGE_NC39_SUPPORT_COHORT.kicad_pcb`, passes all eight
support endpoint assertions and its trace-removal negative control. Native
DRC reports 820 violations / 499 unconnected items with zero authored
shorting items; the seven crossing findings are confined to inherited CM5
donor USB escape geometry. This is the strongest current JMS support routing
primitive, not full-board closure.
The follow-up `PHASE24_DUAL_MODE_STORAGE_NC39_LOCAL_CRYSTAL` trial moved Y10
into the storage island and regenerated separated XIN/XOUT escapes, but native
DRC reports 850 violations / 499 unconnected items with real XIN/XOUT shorts
against JMS support rails. It is rejected route implementation evidence; no
severity or layer-policy relaxation was made.
The V3 QFN escape repair then separated the XIN/XOUT B.Cu corridors and moved
the REXT transition outside the adjacent pad row. The complete-support audit
passes all ten native endpoint assertions and its trace-removal negative
control. Native DRC reports 852 violations / 499 unconnected items with no
storage-local short or crossing; the seven crossing records are inherited
CM5 donor USB geometry. This is a validated support-field primitive, not yet
the complete storage-island or Phase 24 pass.
The physically scoped U11-only reauthor probe is also rejected: native export
produced 20 mismatches and merged unrelated `JMS_AVDDL`/`BRIDGE_USB_VBUS`
ownership. The live source was restored to the stable two-mismatch state.

The active work item is the protected Path-A dual-mode storage implementation
and the remaining clean-board Phase 24 closure. RTL9210B Path B is rejected
for the current Rev-A package/DFM contract; its isolated artifacts remain
qualification evidence only. Path A, production/acreage CAD, and unrelated
Phase 24 work are preserved.
The accepted U11-west/J5-clear placement basis was checked with native KiCad
on 2026-09-08 at 843 DRC violations and 499 unconnected items. The regenerated
current candidate, after correcting the U11 map and moving support parts inside
the acreage outline, is recorded in
`PHASE24_DUAL_MODE_STORAGE_PLACEMENT_CURRENT_FIXED_GRID-drc.rpt` at 857
violations and 499 unconnected items. Neither is a Phase 24 pass. The
U11-west/J5-clear placement removes the prior real storage short classes
(`shorting_items` = 0); eight crossings and incomplete copper remain, so this
is a routing basis, not a Phase 24 pass. The V3 and J5-clear predecessors are
preserved as rejected evidence.
The first native-pad JMS583 support author was rejected: it created five real
shorts and seven crossings because support coordinates were spread across the
donor geometry. The support parts have since been co-located beside U11; the
follow-up local-anchor trial is separately rejected below. The support network
is electrically instantiated, while physical routing still requires
per-net native-pad escape allocation.
The isolated `JMS_RESET_N` direct-join discriminator is also rejected in
`PHASE24_JMS583_RESET_LOCAL_ESCAPE-drc.rpt`: the native path is present, but
its straight F.Cu corridor enters the local USB coupling field at 0.0379 mm
clearance. This confirms the next implementation must use an intentional
through-via/layer corridor, not a direct pad-to-pad segment.
The first such reset via corridor is rejected in
`PHASE24_JMS583_RESET_VIA_ESCAPE-drc.rpt`: its west B.Cu transition still
contacts the JMS XAVDDH/support field and produces a real reset short. The
next corridor must be allocated against the complete local support geometry.
The retained RSET sub-primitive (`phase24_jms583_rset_escape_probe.py`) uses
native U11.39/R80.1 pads and a short F.Cu escape. Native DRC reports no
shorting items and the RSET endpoint is connected; this does not close the
remaining support network. The corrected lateral QFN escape is retained as a
valid sub-primitive in `PHASE24_JMS583_RESET_SOUTH_PROBE_V3-drc.rpt`:
native U11.15-to-R81.1 connectivity passes, the trace-removal negative
control passes, and no local shorting/track-crossing class remains. The six
crossings in that report are inherited USB fixture artifacts at the donor
CM5 source region.
The `JMS_AVDD33` decoupler escape is likewise retained as a valid
sub-primitive in `PHASE24_JMS583_AVDD33_PROBE-drc.rpt`: U11.19-to-C80.1
native connectivity and the trace-removal negative control pass, with no
authored shorting/crossing class. Full rail and support-field routing remains
open. The VBUS divider probe is retained in
`PHASE24_JMS583_VBUS_DIVIDER_PROBE-drc.rpt`: both U11.16-to-R82.1 and
R82.2-to-R83.1 pass native connectivity and the paired trace-removal negative
control. No authored shorting class remains; the crossing findings are
inherited donor USB artifacts.
The right-side XAVDDH probe is retained in
`PHASE24_JMS583_XAVDDH_PROBE_V3-drc.rpt`: U11.52-to-C84.1 native
connectivity and the trace-removal negative control pass, with no authored
shorting/local crossing class. Remaining analog support and complete release
validation remain open.

The seven-net JMS support cohort was regenerated after the first XAVDDH
perimeter via landed in the U11.57 JMS_GPIO12_NC pad field. That V7 trial is
rejected as route implementation evidence. V8 exits U11.52 south from the
native pad at (138.2,131.4), transitions with ordinary through-vias outside
the QFN field, and reaches C84.1 without an authored shorting/crossing class.
Native DRC reports 878 total violations / 499 unconnected items, still
including inherited donor-board findings; it is not a Phase 24 pass. The
seven-net saved-board audit and trace-removal negative control pass. The
remaining JMS support cohort and full storage integration gate remain open.
The REXT follow-up was also tested on the retained V8 cohort. V1's direct
route shorted the XAVDDH field; the relocated-R80 V2/V3 route avoids that
short but still fails native clearance at U11.39 against adjacent QFN pads
and at the R80 approach. This is route/source-field evidence, not a pass:
the active 0.20 mm support width cannot be claimed manufacturable until the
JMS583 land-pattern/source-field authority is reconciled. Path A remains
open and no production CAD was promoted.

The JMS583 package-source reconciliation then corrected the local QFN64
footprint from the contradicted 0.22 mm terminal width/TI description to the
JMicron Rev 2.1 Figure 4 limits: 0.20 mm terminal width, 8.0 mm body basis,
and a nominal 4.46 mm grounded exposed pad. Regenerated V9 includes the
exposed pad and passes the seven-net native connectivity plus negative-control
audit; native DRC reports 811 violations / 499 unconnected items, with the
remaining zone/via and inherited donor findings still open. Paste/mask and
full manufacturing review remain open; this is not production closure.
After the QFN correction, the REXT V7 trial no longer reports the prior
U11.39 adjacent-pad failure. Its translated-R80 approach instead shorts the
U12 exposed pad and crosses the inherited CM5_PERST corridor, so V7 is
rejected as a placement implementation. REXT remains open for a corridor
that clears both neighboring islands; no routing rule was relaxed.
REXT V8 relocates R80 into the open U11/U12 gap at (148,130) and uses a
short orthogonal F.Cu path from U11.39. Focused native DRC reports no
JMS_REXT short/crossing and returns to the corrected cohort total of 811
violations / 499 inherited unconnected items. The dedicated endpoint and
trace-removal negative-control audit passes. V8 is retained as the current
REXT subprimitive; full support release validation remains open.
The accepted REXT V8 placement is now encoded in the live storage placement
generator (`R80 = 148,130`) and regenerated into the current Path-A
candidate. The refreshed seven-net cohort V10 remains at 811 violations /
499 inherited unconnected items, while the native endpoint and trace-removal
negative-control audit pass. This promotes placement authority only; full
support routing and Phase 24 closure remain open.
The cohort was expanded with the native U11.20-to-C83.1 `JMS_AVDDL` path.
V14 preserves connectivity and the combined trace-removal negative control
now passes for eight support nets. Its DRC reports 819 violations / 499
unconnected items; the new mixed-layer route has no JMS_AVDDL short or
crossing, but ordinary-via plane-clearance findings remain open with the
board's inherited plane evidence. Full support and manufacturing closure
remain open.
The reset-delay branch was added to the same cohort with R81.1 exiting on
its free side to C85.1. The first branch attempt shorted adjacent R81.2 and
was rejected; V16's corrected branch passes the native eight-net endpoint
audit including R81.1-to-C85.1 and the combined trace-removal negative
control. Native DRC remains 819 violations / 499 inherited unconnected
items, so this is support progress rather than Phase 24 closure.
The full local ground-stitch trial was corrected before retention: R81.2
(`STORAGE_3V3`) is no longer incorrectly tied to POWER_GND, and the AVDDL
B.Cu leg is clear of the C80 stitch. After native zone refill, C80/C81/C82/
C83/C84/C85/R80/R83/Y10 ground pads all join U11.63 in saved connectivity.
The filled V2 candidate reports 520 violations / 499 inherited donor opens,
with no authored JMS support short/crossing class. Remaining signal branches,
power returns, and Phase 24 closure remain open.
The retained eight-net cohort was refilled with KiCad's native zone filler;
the filled saved candidate reports 519 DRC violations / 499 inherited donor
unconnected items. This materially removes the unfilled-zone via noise, but
does not close the remaining inherited crossings, courtyard/silkscreen,
support branches, or full-board Phase 24 gate.
The paired ground-access probe adds ordinary through-vias at C80.2 and
U11.63 with native F.Cu escapes. After native zone refill, C80.2 is connected
to U11.63 in KiCad's saved connectivity; the focused DRC is 520 violations /
499 inherited donor unconnected items with no new JMS support short class.
This is the retained ground-return template; all remaining support returns
and full-board closure remain open.
The two-via REXT corridor V1 was then rejected: its lower transition lands
in the existing C90/R33 support field and its through-vias also incur the
saved-board plane-clearance findings. Native DRC reports 824 violations /
499 unconnected items, with no evidence that this corridor is promotable.
The next REXT V2 corridor left U11 orthogonally and used an upper/lower
ordinary-via path around the local support field, but native DRC still found
crossings with the inherited PCIe/LXO corridors and a C93 field clearance.
It is rejected route evidence (823 violations / 499 unconnected items).
The `JMS_AVDDL` decoupler probe is retained in
`PHASE24_JMS583_AVDDL_PROBE-drc.rpt`: U11.20-to-C83.1 native connectivity
and its trace-removal negative control pass, with no authored shorting/local
crossing class. Remaining AVDDL pins and complete rail routing remain open.
The rotated-L10 LXO probe is retained in
`PHASE24_JMS583_LXO_PROBE_V2-drc.rpt`: U11.64-to-L10.1 native connectivity
and the trace-removal negative control pass, with no authored shorting or
crossing class after moving Y10 out of the LXO corridor. The earlier Y10
collision variant remains rejected evidence.
The rotated-L10 rail probe is retained in
`PHASE24_JMS583_VDDREG_PROBE-drc.rpt`: U11.1-to-L10.2 native connectivity
and the trace-removal negative control pass, with no authored shorting/local
crossing class. The coupled LXO/inductor and remaining support routes remain
open.
The combined four-net cohort is retained in
`PHASE24_JMS583_SUPPORT_COHORT_V4-drc.rpt`: reset, AVDD33, VCCO, and VCCK
all remain natively connected with no authored shorting/crossing class, and
the combined trace-removal negative control passes. Remaining findings are
inherited donor/zone or JMS583 pad-field constraints; complete support-field
release validation remains open.
The expanded six-net cohort adds rotated-L10 `JMS_VDDREG_5V` and `LXO` to
the four previously validated support paths. Its native endpoint audit and
combined trace-removal negative control pass; `PHASE24_JMS583_SUPPORT_COHORT_V6-drc.rpt`
contains no authored shorting/crossing class. It remains disposable because
the complete support field and JMS583 production land pattern are not closed.
The complete reset-delay branch is retained in
`PHASE24_JMS583_RESET_DELAY_PROBE-drc.rpt`: U11.15-to-R81.1 and R81.1-to-C85.1
both pass native connectivity and the branch trace-removal negative control;
no authored shorting/local crossing class remains.
The VCCK decoupler probe is retained in
`PHASE24_JMS583_VCCK_PROBE-drc.rpt`: U11.2-to-C82.1 native connectivity and
the trace-removal negative control pass, with no authored shorting/crossing
class. Full rail-field routing remains open.
The VCCO decoupler probe is retained in
`PHASE24_JMS583_VCCO_PROBE_V2-drc.rpt`: U11.6-to-C81.1 native connectivity
and its trace-removal negative control pass, with no authored shorting or
crossing class. The earlier y=150 mm version is rejected for crossing the
CM5 PERST corridor.
The pad-width sensitivity candidate is recorded in
`PHASE24_JMS583_CRYSTAL_PAD20_NARROW-drc.rpt`: the disposable runtime
footprint uses 0.20 mm pitch-direction pads and 0.15 mm support traces, and
the XIN/XOUT endpoints pass the native audit plus trace-removal negative
control. This is evidence that the prior local clearance was footprint/escape
allocation driven; it is not production land-pattern approval.
The refilled split-layer crystal probe removes stale-zone and via-hole
diagnostics, but native DRC still finds the 0.20-mm source traces at adjacent
0.4-mm-pitch U11 crystal pads at approximately 0.19 mm clearance. Crystal
support therefore remains open at the strict board rule; no rule relaxation
or production promotion is claimed.
An authority audit found and corrected a generator mismatch: Y10 had been
assigned `JMS_XIN/JMS_XOUT` while U11 and the schematic use `XIN/XOUT`.
The generator now reuses the reviewed JMS map and keeps generated support
parts inside the board outline. The restored short-free crystal probe is
`phase24_jms583_crystal_netmap_fixed.rpt`; the later divergent probe remains
rejected evidence (`phase24_jms583_crystal_divergent_escape.rpt`). The USB3
endpoint audit remains PASS, while physical crystal escape clearance/crossing
work remains open.
The new `phase24_jms583_pcb_net_authority_audit.py` checks all 64 native U11
pad nets against the live schematic authority and passes after regeneration.
The local-anchor support trial is rejected in
`PHASE24_JMS583_SUPPORT_LOCAL_ANCHORS_V2-drc.rpt`: it removes the old
long-detour cause but direct all-net joins still create one real reset short,
six crossings, and dense pad-field clearance findings. It is useful placement
evidence only; the next author must allocate native-pad escapes per corridor,
not append straight joins.
The new `PHASE24_RTL9210B_QFN_ORIENTATION180_PROBE.kicad_pcb` is the current
disposable placement basis for the next QFN field pass: native DRC reports
four inherited warnings, and the U1.39-to-U2.8 RTL_3V3 corridor in
`PHASE24_RTL9210B_ORIENTATION180_U139_PROBE.kicad_pcb` is natively connected
with a trace-removal negative control. This closes only that route
sub-primitive; no production promotion is claimed.
V629 extends that basis with the second lower RTL_3V3 channel, U1.34-to-U2.3.
Both lower channels are natively connected on
`PHASE24_RTL9210B_ORIENTATION180_U134_PROBE.kicad_pcb`; removing all
RTL_3V3 tracks breaks both connections. Native DRC remains four inherited
warnings with no shorting or crossing class. This is still disposable
source-field evidence, not full support closure.
V630 tried a separated U1.33 RTL_5V transition and reduced the coordinated
rail probe to one real native DRC clearance violation: the 0.20-mm source
track leaves U1.33 within 0.0769 mm of adjacent U1.32 no-connect pad geometry.
The two lower RTL_3V3 channels remain connected, but the current QFN escape
field is not manufacturable at the enforced width. Reject V630; this is now
an alternate land-pattern/package authority problem, not a rule-relaxation
opportunity.
V631 is the retained coordinated rail field on the 180-degree basis. It
routes U1.17/U1.33/C5.1 RTL_5V and the U1.34/U2.3 and U1.39/U2.8 lower
RTL_3V3 channels with ordinary 0.60/0.30-mm vias. Native DRC reports only the
four inherited warnings, with no shorting, crossing, or clearance class.
Native connectivity passes all three endpoint groups, and removing all rail
tracks breaks all three. This remains a disposable support-field pass.
V632 is rejected: the first all-1V1 perimeter collector on V631 caused true
source-field shorts at U1.16/U1.17 and U1.36/U1.35, crossings with retained
5V/3V3 fields, a C4 ground collision, and edge-clearance findings. It is a
route-allocation failure; no routing rule or architecture was changed.
V633 is rejected: a bottom-edge U1.36/U1.40/U1.50 RTL_1V1 collector caused
a true U1.40 RTL_1V1 collision with the retained U1.39 RTL_3V3 transition,
plus additional source/edge findings. The experiment does not invalidate
V631; the next 1V1 pass must co-author its departures with the 3V3 transition
field rather than append a bottom collector.
V634 is the retained right-side 1V1 sub-primitive: U1.60 routes directly to
C4.1 on `PHASE24_RTL9210B_ORIENTATION180_1V1_U160_PROBE.kicad_pcb` using
F.Cu only. Native DRC remains at four inherited warnings with no shorting,
crossing, or clearance class; native connectivity passes and removing all
RTL_1V1 traces breaks the endpoint connection. This does not close the
remaining RTL_1V1 source-field group.
V635 extends the valid right-side 1V1 channel with U1.16. The saved-board
U1.16-to-C4.1 path is natively connected and its all-RTL_1V1 trace-removal
negative control breaks the path. Native DRC remains four inherited warnings
with no shorting, crossing, or clearance class. This is still a disposable
sub-primitive while the remaining 1V1 pins are open.
V637 extends the right-side 1V1 trunk with U1.50. The saved-board
U1.50-to-C4.1 path is natively connected; removing all RTL_1V1 traces breaks
it. Native DRC remains four inherited warnings with no shorting, crossing, or
clearance class. The U1.36/U1.40/U1.55/U1.63 source cluster remains open.
V638 adds the corrected right-edge U1.55/U1.63 1V1 extensions to the C4.1
trunk. Both native endpoint checks pass and removing all RTL_1V1 tracks breaks
both paths. Native DRC remains four inherited warnings with no shorting,
crossing, or clearance class. Only the U1.36/U1.40 source cluster remains in
this local 1V1 allocation.
V636 extends the 1V1 trunk with U1.25 using a north-of-QFN F.Cu departure.
U1.25-to-C4.1 native connectivity and the all-RTL_1V1 trace-removal
negative control pass; native DRC remains four inherited warnings with no
shorting, crossing, or clearance class. Remaining 1V1 pins remain open.
V639 is rejected: the first U1.40 continuation avoided the U1.41 USB_TXP0
clearance violation only by moving into the retained U1.39 RTL_3V3 source
departure. Native DRC reports one true crossing plus a solder-mask bridge;
the saved-board U1.40-to-C4.1 path is connected, but this is an independent
detour failure. U1.39/U1.40 must be co-authored as one adjacent-pad escape;
no routing rule or architecture is relaxed.
V640 retains a delayed-bend U1.40 departure beside the proven U1.39 exit.
The route remains on F.Cu only through the cleared pad-body envelope, then
uses ordinary through-vias and B.Cu to the existing 1V1 trunk. Native DRC
returns only the four inherited warnings, with no signal short, crossing, or
clearance violation; native U1.40-to-C4.1 and U1.39-to-U2.8 connectivity both
pass. This closes the U1.39/U1.40 local escape sub-primitive, not the full
RTL9210B support field; U1.36 remains the next open 1V1 source.
V641's first U1.36 continuation is rejected because its via occupied the
retained B.Cu RTL_3V3 collector. The corrected delayed-bend V2 moves the
1V1 via and trunk north of that collector: native DRC returns the four
inherited warnings only, with no signal short, crossing, or clearance class,
and U1.36-to-C4.1 native connectivity passes. The local QFN 1V1 source field
is now connected; remaining opens belong to other support groups.
V642 adds ordinary outboard GND return vias for U1.69, U1.66, and U1.45.
The first U1.45 via position was rejected for clearance to the retained
U1.40 via; the corrected outboard position leaves only three inherited
silkscreen warnings. Native zone refill connects all three QFN ground pads;
this is a retained ground-return sub-primitive, not full support closure.
V643 joins U1.20 RTL_3V3 into the lower same-net field using an ordinary
through-via and B.Cu west-side corridor. Native DRC remains at three inherited
silkscreen warnings. V644's first R2/R3 source extension is rejected because
its B.Cu trunk crosses the retained RTL_5V collector; the source join remains
open and requires a separate corridor allocation.
V645 completes the RTL_3V3 physical field: the corrected R2/R3 source route
joins the lower field from below the 5V collector, and the U1.52/C3 branch
joins through a separate B.Cu corridor. Native DRC has no RTL_3V3 findings and
remains at three inherited silkscreen warnings; 25 unrelated support opens
remain. This closes only the RTL_3V3 rail field.
V647's crystal-pair route is rejected: the direct F.Cu source escape crosses
the retained 1V1/3V3 transition field. A staggered B.Cu retry removes the
pair-to-pair contact but still conflicts with the nearby 3V3 via and retained
1V1 corridor. XTAL_IN/XTAL_OUT remain open for coordinated source allocation;
no rules or accepted rail geometry changed.
V651 is a fresh native reload/recheck of the retained RTL_3V3-field board:
KiCad DRC reports 3 inherited silkscreen warnings and 25 unconnected items.
The native inventory independently reports all 9 RTL_3V3 pads joined, while
SPISI, RSET, and XTAL_IN remain incomplete. This is the current reproducible
baseline for the next support-field pass.
V652 retains the corrected RSET lower-channel route: U1.51 exits to an
ordinary via at (102.5,76.0), crosses B.Cu to an outboard transition at
(108.4,80.0), and enters R1.1 without contacting R1.2/GND. Native DRC is
three inherited silkscreen warnings with no signal violation; the open count
falls to 24. RSET is locally closed, while full support remains open.
V653's local Y1/C1/C2 relocation is rejected. It reduces the crystal span but
creates C2/RTL_1V1 clearance and shorting findings, while XTAL_IN still
contacts the nearby RTL_3V3 transition. Crystal routing requires co-authored
source-field and capacitor placement.

## Current live source/parity correction — 2026-09-08

The previous 64-mismatch placement result and the 111-mismatch support-route
result are superseded historical probes. The authoritative U12.24/U12.25
instance labels were corrected in `STORAGE.kicad_sch` from stale `USB_TXN1/P1`
to `JMS_USB3_TXN/P`, matching the reviewed symbol/source map and C86/C87
bridge-side nets. A fresh native export and regenerated
`PHASE24_DUAL_MODE_STORAGE_PLACEMENT_CURRENT.kicad_pcb` now produce zero
expected-pad mismatches; the dual-mode mode contract also passes. Receipt:
`PHASE24_STORAGE_LIVE_PARITY_20260908.rpt`. This closes source pad-net parity
for the regenerated placement candidate, not copper routing, ERC, DRC, or
full Phase 24.

V4 is also rejected: its VBUS and USB3 endpoint audits pass, but native DRC
reports 512 findings / 499 inherited unconnected items and real RX_N/TX_N
shorting/crossing classes on the upper B.Cu detour. It remains negative route
evidence; validation rules and production authority are unchanged.

## Current VBUS/RX_N launch discriminator — V3 rejected (2026-09-08)

`PHASE24_DUAL_MODE_STORAGE_FULL7_VBUS_RXN_REPAIR_V3` is disposable
route-implementation evidence. It reroutes the CM5 USB3 RX_N launch around
J1, removing the earlier RX_N-to-J1 shorting class. Native VBUS connectivity
and its trace-removal negative control pass; complete JMS583 support and all
ten USB3 endpoint assertions also pass. Native DRC reports 509 findings / 499
inherited unconnected items, with an RX_N/refclk crossing, so it is rejected
for promotion. No production authority, Path A artifact, or RTL9210B Path-B
qualification changed.

The complete ten-net JMS583 support audit passes on
`PHASE24_DUAL_MODE_STORAGE_FULL7_AVDDL_local_zone.kicad_pcb`: REXT, XIN,
XOUT, RESET_N, AVDD33, AVDDL, VCCO, VCCK, VDDREG_5V, and LXO connect by
native pads/tracks/zones. Its combined negative control removes every support
track and zone and fails as required. Native DRC remains 514 inherited
findings; this closes the support connectivity primitive only.

The VBUS audit was strengthened to require U11.10 (`JMS_VBUS_SENSE`) in
addition to U11.16, R82, and R83. V10 is the latest complete-endpoint trial:
all three assertions and the trace-removal negative control pass, but native
DRC reports 532 findings with a real VBUS/JMS_VBUS_SENSE handoff short. VBUS
remains open and no route is promoted.

An independent parity run on the current AVDDL support-route candidate reports
111 expected-pad mismatches. Examples include J3/M.2 ownership, J1/J2 power
and Ethernet support, J4 service pins, J5 mode pins, and missing support
passive pads. This candidate is therefore disposable support evidence, not an
integrated schematic-authoritative board; no mismatch is waived.

The retained production-width crystal discriminator uses the same native
split-layer corridor but 0.20 mm tracks rather than the earlier sensitivity
probe's 0.15 mm tracks. Both U11 crystal endpoints pass native connectivity
and a trace-removal negative control; native DRC remains 519 violations / 499
inherited donor opens, so this does not close the support or Phase 24 gates.

The first combined support/crystal cohort is rejected: overlaying the
production-width XIN/XOUT escape on the retained XAVDDH support path raises
native DRC to 527 violations / 499 inherited opens, with authored B.Cu
crossings and an XOUT-to-XAVDDH short at the QFN-side transition. The crystal
endpoint proof remains valid in isolation; the next route must co-allocate
the crystal on the opposite side of the XAVDDH diagonal.

The left-side crystal relocation with restored stepped QFN dogbones was also
tested. It removes the crystal-corridor crossings, but native DRC still finds
one XOUT-to-XAVDDH source-field short (`PHASE24_JMS583_CRYSTAL_LEFT_CORRIDOR`:
527 violations / 499 inherited opens). Reject this route as a combined
solution; the next implementation must co-author the XAVDDH transition and
crystal escape rather than treating either source field as fixed.

The follow-up left-corridor source-field regeneration preserves the stepped
XIN dogbone and moves XOUT's transition farther west. It eliminates the
XIN/XOUT crossing and the prior XAVDDH B.Cu crossings, but native DRC still
reports one real XOUT-to-XAVDDH short at the adjacent QFN exits (527 total /
499 inherited opens). Reject it; the next trial must co-allocate all three
bottom-edge analog/crystal exits before any layer transition.

The co-authored three-exit candidate now passes native U11.50/XIN to Y10.1,
U11.51/XOUT to Y10.2, and U11.52/XAVDDH to C84.1 connectivity with a
trace-removal negative control. Native DRC is 522 violations / 499 inherited
opens, with no authored shorting class; the remaining crossing/dangling
records are donor-board artifacts. Retain this as the strongest JMS583
analog/crystal support-field basis, but do not call the full storage island
or Phase 24 closed.

The dual-mode storage library audit was corrected to match the live JMS583
authority: 64 numbered signal pads plus grounded exposed pad 65. The repaired
audit now passes JMS583, both selector packages, and the TE M-key contact/key
gap checks. This fixes validation coverage only; native ERC/DRC, physical
routing, mode-state, and full storage integration gates remain open.

Historical snapshot (superseded count): the live schematic netlist
`PHASE24_STORAGE_LIVE_NETLIST.xml` was exported
with KiCad 10.0.5 and compared against a freshly regenerated placement. The
complete M-key contact map and SATA coupling ownership reduced actionable
pad mismatches from 65 to 32. The remaining findings are not waived: eight
contacts are the intentional 59--66 M-key key gap, while the other findings
are genuine selector/support/JMS control ownership mismatches requiring
authoritative source repair. This 65-to-32 result is superseded by the
following five-mismatch source-authority audit; it remains archaeology, not a
current open-gate count.

The parity checker now excludes only the intentional non-board X7 contract
marker in addition to the TE key gap. With the complete U12/U13/U14 support
metadata regenerated from the live netlist, the disposable placement reaches
five real mismatches: the unresolved set is confined to JMS support-label/net
ownership (`L10`, `R80`, U11.39, `Y10`). A coordinate/UUID repair trial was
rejected after native export showed broad unconnected-net regressions; the
live schematic was restored to the last checkpoint. These five remain
fail-closed and require source-level reconciliation; no PCB-only alias is
being used to manufacture a pass.

A second exact-UUID support-label remap trial was also rejected: native export
increased the mismatch set from five to eight by introducing new JMS rail and
crystal ownership errors. It was reverted immediately. Label renaming alone
is not an acceptable repair; the remaining defect requires native
symbol-instance association repair.

The duplicate-label discriminator is retained as additional evidence. Keeping
the first generated copy produced 19 parity mismatches; keeping the final
generated copy returned five mismatches but changed their identities. A full
label-block reauthor from the shared maps produced 77 mismatches because the
legacy symbol-frame attachment semantics were lost. All three probes were
reverted. The current source remains the five-mismatch checkpoint, and the
next repair must be derived from a native KiCad-authored association fixture,
not from further label-name or duplicate-removal guesses.

The complete JMS583 support/co-author cohort now passes one native saved-board
audit: reset, AVDD33, AVDDL, VCCO, VCCK, VDDREG, LXO, XAVDDH, XIN, XOUT, and
reset-delay all reach their intended support pads. Removing the XIN copper
fails the complete-cohort negative control. This is the retained support-field
basis; native DRC remains non-clean from donor/integration findings.

The earlier JMS583 crystal DRC receipts, including divergent, split-layer,
pad-width, and net-name variants, are retained as raw historical evidence;
they are not current acceptance criteria and do not override the production-
width discriminator result.

2026-09-08 crystal fixture recheck: the saved `PHASE24_JMS583_CRYSTAL_ESCAPE_PROBE`
was regenerated and its native XIN/XOUT endpoint audit passes with the required
trace-removal negative control. Native DRC remains 519 violations / 499
unconnected donor items; this is route evidence only, not a promoted crystal
solution or Phase 24 closure.
SUPERSEDED HISTORICAL DFM NOTE: Native footprint geometry showed that a via
between U1.39/U1.40 cannot fit under the ordinary 0.60/0.30 mm via and
0.20-mm clearance contract; V663/V664 reproduced shorts/crossings for their
specific source-field allocations. V666 subsequently demonstrated a clean
separated planar escape on the same audited package with 0 DRC violations,
0 unconnected items, and 0 footprint errors. Do not read this older note as
a Path-B rejection; the complete integrated source-field route remains open.
V661 is the current retained rail-integration basis: native DRC has nine
inherited warnings and no shorting/crossing class after adding the proven
RTL_5V route to the V35 U2-left crystal/1V1/upper-3V3 field. It still has 23
unconnected pads and is not closure. The legacy RTL_5V negative-control helper
is invalid for this redundant route because it removes only the first same-net
track; it unexpectedly passes and is not used as evidence.
The corrected V661 audit removes every duplicate instance of the unique
RTL_5V trunk. The endpoint group passes and the trace-removal negative control
now fails as required.
V663 is rejected as the lower RTL_3V3 source-escape class: after moving the
U1.39 transition farther west, native DRC still reports a real RTL_3V3/
RTL_1V1 short at the QFN field. The candidate has 10 total findings and 21
unconnected pads. No rule or architecture change was made.
V664 is rejected: a diagonal U1.39 RTL_3V3 departure still produces a real
RTL_3V3/RTL_1V1 short and track crossings (13 findings, 21 opens). No rule,
architecture, Path-A, or production-CAD change was made.
V659 is rejected after a valid native rerun: the all-rail In2 collector on the
fresh V35 basis produced 56 violations, including rail-to-rail, rail-to-SPI,
and rail-to-crystal shorts/crossings. The helper defects encountered before
authoring were corrected and are not engineering results. The next candidate
must allocate rails and signal exits together with explicit local keepouts;
a shared broad collector is not a valid solution class.
V660 is rejected after a valid native rerun: relocating C3/C4/C5 with separate
In2 rail collectors produced 98 violations, including rail-to-crystal,
rail-to-SPI, rail-to-rail, and crossing classes. This confirms that the source
escape allocation must be regenerated jointly with the rail channels.
V658 is rejected after a valid rerun: its coordinated XTAL_IN/XTAL_OUT/RSET
field produced 31 native violations, including real XTAL pair, rail, and RSET
shorts/crossings. The pre-authoring helper error was corrected; no result was
taken from the malformed first run. The remaining Path-B issue is the complete
QFN lower source-field allocation.
The V658 native connectivity audit passes all XTAL_IN/XTAL_OUT/RSET endpoints
and its trace-removal negative control fails as required. Native DRC remains
the governing rejection. Consultant review recommends the next experiment
co-author the five SPI nets plus CLKREQ_N against the existing rail field, or
reopen the rail escapes as one complete lower-QFN allocation; isolated net
nudges are now exhausted as a solution class.
V656/V657 are rejected disposable SPI allocation trials. V656 moved U2 east
and regenerated all five SPI channels, but native DRC found 43 violations with
real shorts/crossings. V657's single-net west SPICS discriminator found seven
violations, including CLKREQ_N/SPICS shorting. These are route-implementation
failures; Path A, production CAD, and validation rules remain unchanged.
V654 corrected the disposable KiCad net-assignment helper to capture net
codes before adding tracks, eliminating its SWIG proxy failure. The rerun of
the co-authored U1.52/crystal candidate is rejected by native DRC: XTAL_OUT
crosses XTAL_IN and the retained 1V1 field, XTAL_IN crosses the shifted 3V3
transition, and a residual 3V3 segment dangles. No production CAD changed.
V655's joint U1.52/crystal field is rejected: native DRC reports an XTAL_IN /
XTAL_OUT source crossing, XTAL_OUT contact with the shifted 3V3 transition,
and a 3V3 return collision with the retained U1.40 1V1 corridor. The source
and support field now requires coherent local relocation/reauthoring.
V648's first SPISI source-to-U2.5 channel is rejected: its B.Cu corridor
crosses the retained RTL_3V3 source trunk and RTL_5V collector. Native DRC
still validates the rest of the fixture, but SPISI remains open for a separate
SPI corridor allocation.
V649's high B.Cu SPISI corridor is rejected: its x=91 transition column
crosses both retained RTL_3V3 and RTL_5V collectors. Preserve the rails and
allocate the next SPI transition west of that power fence.
V650 corrects the prior V645 wording: native DRC on the saved C3-join board
still reports separate RTL_3V3 physical components (U1.52/C3 and the QFN
lower/source branches). The earlier endpoint-only interpretation was
insufficient. RTL_3V3 is therefore reopened as an incomplete field until the
native same-net component is proven unified.
V646's first RSET escape is rejected: the native endpoint path is connected,
but its B.Cu diagonal crosses the retained U1.40 RTL_1V1 corridor. RSET
remains open for a separate channel allocation; accepted rail geometry and
rules are unchanged.
The historical V35 rotated-U1 support reference was re-saved through native
zone refill as `PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_NATIVE_REFILLED`.
Current native DRC is 4 inherited warnings, and the native five-net SPI plus
XTAL_IN/XTAL_OUT/RSET audits pass with trace-removal negative controls. This
is the current source-field/reference basis for the next implementation pass;
it is not yet production closure because rails, controls, USB, lane-0,
REFCLK, M.2, power, firmware, and integrated Path-B gates remain open.
V35-derived RTL_5V probes V1/V2 are rejected: V2 has 15 native DRC violations,
including RTL_5V crossings with SPISI/RTL_3V3, a QFN-edge contact, and
dangling segments. V4 is the retained RTL_5V sub-primitive: its native
U1.17/U1.33/C5.1 audit and trace-removal negative control pass, and native
DRC is back to four inherited warnings. This is route-allocation evidence
only, not full support closure. The detailed source-field checkpoint is
`PHASE24_RTL9210B_V35_SOURCE_FIELD_REPORT.md`; the next pass must co-author
all rails and QFN departures around V35's proven five-net field.
The first V35-derived RTL_1V1 lower-bus probe is rejected: native endpoint
connectivity and the negative control pass, but native DRC reports 21
violations from RSET/XTAL_OUT crossings, U2/C4 ground contacts, and occupied
via fields. The next 1V1 pass must relocate/co-author the support endpoint.
The U2-left coordinated relocation is rejected as a route implementation:
native SPI and 1V1 audits pass, but naïve regenerated SPI source channels
produce 14 native DRC violations, including five QFN-source shorts and an
XTAL_OUT crossing. It does clear the lower 1V1/U2 corridor; the next pass
must co-author U1 SPI source escapes and 1V1 departures.
The source-preserving U2-left candidate is now the retained coordinated basis:
native SPI and lower 1V1 audits pass, with no SPI crossing/short. Native DRC
has eight findings, reduced to two real local U1.55/XTAL_OUT conflicts plus
six inherited warnings. The next repair must co-author that crystal drop and
U1.55 escape.
The crystal co-author candidate now passes native SPI, XTAL_IN/XTAL_OUT/RSET,
and lower 1V1 audits with negative controls. Native DRC reports six inherited
warnings and no signal violations; 26 intended external/support opens remain.
Retain it as the strongest disposable basis while RTL_3V3/QFN, REFCLK, lane 0,
USB, controls, power, firmware, and full Path-B validation remain open.
The upper RTL_3V3 field also passes its native endpoint audit and negative
control with no signal DRC violations. Lower RTL_3V3 remains open: its trial
caused QFN/1V1/RSET contacts and violated the active 0.200 mm minimum width.
The upper RTL_3V3 field is independently valid with native endpoint and
negative-control audits and no signal DRC violations. Lower RTL_3V3 remains
open after the native nine-finding trial and its rejected 0.13208 mm retry;
the next attempt must use a new coherent QFN escape allocation.
V562 is the retained corrected support baseline: its native saved-board audit
connects the complete RTL_1V1 and RTL_3V3 support groups with a working
trace/zone-removal negative control. V563, V564, and V565 are rejected
RTL_5V route classes (west corridor, lower outboard, and In2 plane).
V566–V569 are rejected local/perimeter RTL_5V trials; V570 is the current
best RTL_5V candidate for further review, with native U1.17/U1.33/C5.1
connectivity and a trace-removal negative control, but it is NOT a pass:
native DRC reports 16 violations, including real QFN/pad-field and local
clearance findings. It has no `shorting_items` or `tracks_crossing` in the
report, but the remaining clearance/manufacturing/open-support findings keep
RTL_5V and full Path-B support open. Do not promote V570 to production CAD.

V571 is rejected: the attempted east U1.34 reallocation did not preserve the
complete 3V3 saved-board connectivity group and still retained QFN/pad-field
clearance and solder-mask violations. Its audit failure is preserved as a
negative result; V562 remains the retained baseline.
V572 corrects the missing 3V3 In2 bridge and replaces the V571 diagonal with
 a Manhattan U1.34-to-U1.39 handoff. Native 5V and 3V3 connectivity audits
 pass with independent trace-removal negative controls; native DRC improves
 to 14 findings with no shorting or crossing classes. V572 is the retained
 disposable candidate, not a production pass: QFN/pad-field clearances and
 inherited support findings remain open.

V573 moved only the lower RTL_5V transition away from pads 31/32, but
shorted the RTL_5V via into the retained RTL_3V3 In2 spine. V574 rerouted
that spine around the via and reduced native DRC to 12 findings with no
shorting or crossing classes, but its independent saved-board audit failed
the complete 3V3 endpoint group. Reject V573/V574; V572 remains the retained
electrically connected baseline.
V576 restores the two omitted physical In2 3V3 bridges on the V574 coupled
field. Native 5V and 3V3 endpoint audits pass with independent trace-removal
negative controls; native DRC remains at 12 findings with no shorting or
crossing classes. Retain V576 as the current connected disposable candidate,
not production closure.
V582 re-centered the lower RTL_3V3 In2 spine in the measured gap between
the neighboring RSET and 1V1 transitions. Native 5V/3V3 audits and both
trace-removal negative controls pass; native DRC falls to 10 findings with
19 opens and no shorting or crossing classes. Retain V582 as the current
Path-B rail candidate, not full support closure.
V583 moved only the upper RTL_5V B.Cu corridor from y=50.5 to y=49.5 to
clear the 3V3 via. Native 5V/3V3 audits and both trace-removal negative
controls pass; native DRC falls to 9 findings with 19 opens and no 5V
shorting/crossing or clearance class. Retain V583 as the current rail
candidate, not full Path-B closure.
V589 is rejected: a local B.Cu PEDET route from R2.1 toward U1.8 reduced the
saved-board open count by one, but native DRC found true PEDET crossings with
the retained RTL_5V vertical corridor and RTL_1V1 field. It is not evidence
against the PEDET function; the next valid experiment must relocate the local
PEDET source/escape or allocate a legal corridor around both fields.
V594 completes the PEDET endpoint path using an all-F.Cu outer perimeter:
J1.69→R2.1→U1.8 is natively connected and the trace-removal negative control
fails as required. Native DRC returns to 9 findings with no PEDET crossing;
the remaining findings are inherited/local support findings. Retain V594 as
the current PEDET-plus-rail disposable candidate, not production closure.
V595 adds the local R3.1→U1.13 CLKREQ escape on F.Cu. Native saved-board
connectivity and its trace-removal negative control pass; native DRC remains
at 9 findings with no new crossing. Retain V595 as the current PEDET/CLKREQ
plus-rail disposable candidate, not production closure.
V596 is rejected: its proposed SPICS transition landed on the existing
RTL_3V3 via field and the saved route was not a valid SPICS implementation.
V597 is also rejected: an all-F.Cu SPICS staircase crossed the 1V1 escape and
shorted SPICS into RTL_3V3. The next SPI attempt requires an allocated local
corridor or coherent support relocation.
V598 is rejected: its proposed SPICS B.Cu transition created true shorts to
the retained RTL_1V1 and RTL_5V fields. V599 is rejected: its direct F.Cu
outer departure crossed the PEDET/5V/3V3/CLKREQ source-field geometry. These
are implementation failures of scalar SPI escape allocation; the next pass
must co-author the shared QFN source field.
V600 is rejected: rotating/moving U2 and using direct F.Cu SPI lines ran
through U1's interleaved power/control pads. V601 is rejected because its
SPISI transition occupied the RTL_3V3 In2 field. V602 moves that transition
west; U1.18→U2.5 connectivity and the trace-removal negative control pass,
with native DRC at 10 inherited/local findings and no new short/crossing.
Retain V602 as the SPISI sub-primitive, not full SPI or Path-B closure.
V603 is rejected: the SPISO3 transition/endpoint entered the lower RTL_3V3
field and crossed the existing 1V1 branch. V604 moved that endpoint west but
crossed/shorted the retained SPISI launch. The next pass must allocate all SPI
source and endpoint channels together.
V605 is rejected: its SPISO3 channel crossed the retained SPISI vertical and
endpoint launch. V606 avoided that crossing but entered the lower 3V3/1V1
clearance envelope; V607 moved inward and collided with the SPISI endpoint
via. V608 coordinated two endpoint transitions but still collided at the U2
SPICLK pad field. The next pass must allocate U1 source and U2 endpoint
channels together.
V617 is rejected: its SPICLK source dogbone crossed SPISI and its endpoint
transition entered the lower 3V3 field. V618 separated the source transition
but still coupled to SPISI/3V3; V619 moved the channel above SPISI but its
source departure crossed the retained SPISI escape and RTL_5V via. These
results confirm that the next step is coordinated QFN SPI source-field
authoring, not more independent channel detours.
V616 is rejected: the proposed SPISO lower B.Cu corridor crossed the retained
SPISO3 source channel and SPISI bottom approach, and its source transition
violated the 3V3 clearance envelope. The remaining SPI work is a complete
five-net channel allocation or coherent U2 support relocation.
V609-V614 rejected successive coordinated SPISI/SPISO3 endpoint variants for
U2 ground, occupied-via, or lower-field contact/clearance. V615 lifts the
SPISI bottom dogbone; both SPISI and SPISO3 native connectivity audits and
trace-removal negative controls pass, with DRC at 10 inherited/local findings
and no new short/crossing. Retain V615 as the coordinated two-net SPI
sub-primitive.
V578 replaced the first U1.33 5V departure with an exact-horizontal segment.
Native saved-board connectivity then showed dangling 5V branches and DRC
still reported the pad-32 clearance violation. Reject V578; V576 remains the
best connected candidate and the strict QFN edge escape remains open.
V577 edited the existing V576 U1.34 handoff natively by 0.05 mm rather than
rebuilding the field. Native DRC rose to 13 findings and still reported the
strict pad-33/pad-34 source-field clearance (plus pad-35 clearance); it did
not improve the limiting geometry. Reject V577 and retain V576.
V575 shifted the U1.34 3V3 departure by 0.05 mm on the V574 lineage, but
native DRC retained strict source-field clearance and the regenerated 3V3
branches were dangling in saved-board connectivity. Reject V575; further
progress requires coordinated QFN escape authoring, not scalar coordinate
nudges.

V579 removes the V576/V578 diagonal source departure entirely: U1.33 runs
straight to an outboard transition, while the 3V3 field remains on the V576
coupled network. Native 5V/3V3 audits and both trace-removal negative
controls pass. Native DRC is 11 findings with 20 opens; the 5V source group
is no longer open, and the remaining findings are localized/inherited
support, return, and other Path-B endpoints. Retain V579 as the current
RTL_5V/3V3 candidate, not full Path-B closure.
V580 attempted ordinary-via returns for U1 exposed/ground pads 69, 45, and
66. Native DRC rejected the placement with true GND-to-USB/3V3 shorts and
clearance violations near the QFN lower field; do not use it. V579 remains
the retained rail candidate.

## SUPERSEDED CURRENT-STATE SNAPSHOT — HISTORICAL

The active gate is Path-A storage-island integration: route and validate the
live JMS583/TUSB9261 + selectors + M-key socket candidate from authoritative
schematic/library data. The support network is already instantiated and its
audit passes; the open issue is physical saved-board connectivity/DRC and
mode-aware validation, not support-network creation. RTL9210B Path B is
superseded for this Rev-A DFM contract and is not a current execution gate.

Documentation hygiene note: the live `STORAGE.kicad_sch` already contains the
JMS583 support network and its support-network audit passes. Any older prose
that says this network still needs to be instantiated is superseded
historical evidence, not a current gate. Raw reports and rejected fixtures
remain immutable evidence.

The current storage placement regeneration is
`PHASE24_DUAL_MODE_STORAGE_PLACEMENT_CURRENT.kicad_pcb`, produced by
`phase24_regenerate_storage_placement_current.py`. Its parity comparison has
only been run against the stale `STORAGE.xml` export and therefore remains an
open diagnostic, not a closure claim; native regeneration currently produces
no usable fresh XML from the child sheet alone. Do not use that stale-export
result to promote the placement.

## SUPERSEDED / HISTORICAL FINDINGS

The earlier V132–V154 prose below records valid historical experiments and
must not be read as the current promoted basis. V562 supersedes the old V137
rail narrative as the corrected support authoring baseline; V570 is only the
latest disposable 5V field experiment. Raw boards and native reports remain
immutable evidence.

## AUTHORITATIVE CURRENT STATE — 2026-09-07

The active work item is isolated RTL9210B Path-B support qualification; Path A,
production/acreage CAD, and unrelated Phase 24 work remain unchanged. The
V132–V136 RTL_5V trials are rejected route-allocation variants: each either
shorted/crossed retained control or 1V1 fields, or entered a ground/CLKREQ
via. V137 routes U1.33/U1.17/C5.1 through the lower C5 approach and passes
the focused native audit: saved connectivity joins C5.1/U1.17/U1.33, the
trace-removal negative control fails as required, and the native report has no
`shorting_items` or `tracks_crossing`. Promote V137 only as the disposable
RTL_5V sub-primitive; remaining rail, high-speed, USB, M.2, firmware, and full
Path-B validation gates remain open.
V138 and V139 apply the earlier U1.34 RTL_3V3 handoff to the promoted V137
rail basis. Both achieve native U1.34-to-C3/R2/R3/U1.20 connectivity, but V138
shorts the new RTL_5V source field and V139 collides with SPISO3 and retains a
track crossing. Reject both as route-allocation evidence; U1.34 remains open.
V140 shifts the U1.34 departure left and raises the B.Cu handoff above the
V139 SPISO3 via, but native DRC still reports three SPISO↔RTL_3V3 shorts and
one crossing. Reject V140; U1.34 needs a new shared QFN source-field
allocation rather than another blind endpoint tweak.
V141 joins the four shared M.2 `SSD_3V3` contacts on the V137 basis. Native
DRC has no shorting or crossing classes; the saved-board audit connects
J1.2/J1.4/J1.6/J1.8 and its trace-removal negative control fails as required.
This closes only the socket-contact collector; the actual SSD_3V3 source,
power-budget, and remaining high-speed Path-B endpoints remain open.
V142 is rejected: its high-clearance U1.34 B.Cu span still contacted SPICS.
V143 moves the U1.34 departure outside the V137 RTL_5V source corridor and
uses a higher outer B.Cu handoff. Native DRC has no `shorting_items` or
`tracks_crossing`; the saved-board audit joins U1.34/C3/R2/R3/U1.20 and its
trace-removal negative control fails. Promote V143 only as the disposable
U1.34 RTL_3V3 sub-primitive; high-speed links, USB, reset, SSD_3V3 source,
firmware, and full Path-B validation remain open.
V144 carries the promoted V141 M.2 contact-row join onto V143. The combined
native audit passes U1.34 RTL_3V3 and J1.2/J1.4/J1.6/J1.8 connectivity with a
negative-control failure; native DRC still has no shorting or crossing class.
The six remaining opens are the PCIe/shared high-speed endpoints. SSD_3V3
source/power and those high-speed channels remain open.
V145 is rejected as a REFCLK route implementation: the lower two-layer
corridors contacted XTAL/1V1/CLKREQ fields and connector sideband pads and
introduced six signal crossings. It does not reject the RTL9210B pinout or
the V144 placement basis; REFCLK needs an outer-corridor allocation.
V146/V147 are rejected REFCLK allocation trials. V146 avoided the inherited
CLKREQ corridor but entered the J1 TX pad field; V147 used separated outer
J1-side drops but still crossed the RTL9210B exposed GND pad. The pair's
remaining blocker is the inherited QFN lower-edge/RTL_1V1 source-field
allocation, so the next experiment must relocate that local support field.
V148/V149 test that relocation. V148 moves the lower RTL_1V1 collector to
B.Cu but crosses XTAL_IN; V149 adds an F.Cu overpass around the XTAL span but
still contacts XTAL_IN and C1 ground. Both are rejected local-support
allocations. The next repair must co-author XTAL_IN and the lower 1V1 field.
V150/V151 test the corrected below-XTAL collector. V150 has no signal
shorting/crossing but loses the existing 1V1 layer handoff; V151 restores the
handoff and passes the native 1V1 audit/negative control with no signal
shorting/crossing. V152/V153 then test REFCLK over that basis; V152 contacts
the XTAL_IN via and V153 contacts the 1V1 source field. V154 moves only the
1V1 handoff outboard, restores the full 1V1 group, and passes the focused
native audit with no signal shorting/crossing. Promote V154 as the current
REFCLK-ready local-support basis; XTAL_IN/REFCLK and remaining high-speed
endpoints remain open.
V155 is rejected: its split REFCLK_N escape still contacted U1 pad 65 and the
outboard 1V1 handoff, while REFCLK_P contacted the XTAL_IN endpoint. V154
remains the validated local-support basis; REFCLK requires a coordinated
endpoint/sideband allocation, not another uncoordinated split.
V156 moves only the CLKREQ_N J1 launch to x≈139 and passes the focused native
signal gate with the same six intended opens. V157 moves XTAL_IN outboard but
is rejected because its new endpoint crosses the retained XTAL_OUT vertical
span. REFCLK remains open; the next local support experiment must co-author
XTAL_IN and XTAL_OUT together.
V158 moves XTAL_IN's transition inward, left of XTAL_OUT. Native DRC has no
signal shorting/crossing classes; the crystal connectivity audit and negative
control pass. V160 removes the old F.Cu 1V1 handoff and joins the complete
1V1 group directly to the existing B.Cu rail. V162's first REFCLK attempt on
that basis is rejected for XTAL_OUT/legacy 1V1 contacts and two crossings.
The current coordinated-support basis is V160 plus V158's crystal routes;
REFCLK remains open.
V163 is rejected: moving XTAL_OUT to the proposed upper B.Cu span placed its
left transition too close to the exposed GND pad and the REFCLK-N launch
still entered the CLKREQ field. V164 separates the REFCLK source drops and
uses a moved XTAL_OUT, but native DRC retains six real crossing classes,
including the inherited 1V1/CLKREQ corridors and the J1 launch. V165 removes
the superseded 1V1 bridge and tries P on F.Cu/N on B.Cu; it still shorts the
REFCLK-P departure into U1 pad 62 and crosses the XTAL_OUT span. V166 moves
P to an upper B.Cu corridor, but native DRC reports REFCLK-P contacts with
the exposed GND/XTAL_OUT fields and the J1-side N via is too close to the
TXP pad. Reject V163-V166 as route-allocation evidence. They do not alter
the V158/V160 support basis or the RTL9210B authority; REFCLK remains open
and the next trial must allocate the QFN source escapes, XTAL_OUT transition,
and J1 launch as one cell.
V167 applies the measured QFN pad-gap dogbones, but the lower B.Cu exits
cross XTAL_IN/XTAL_OUT and the J1 transitions are shorted because both vias
were placed directly in the REFCLK contact row. V168 moves the J1 transitions
outboard and removes REFCLK-to-REFCLK shorts; remaining failures are XTAL
and SPI/RTL_5V/1V1 corridor ownership. V169 moves the pair above the SPI
fields and leaves only corridor crossings (no REFCLK-P/N shorting), making it
the best disposable topology so far, but it is not promoted: P/N endpoint
launches and the lower support exits still need native DRC closure. V170
puts the whole upper span on F.Cu and is rejected by RTL_3V3/lane/XTAL
contacts. V171 adds short F.Cu overpasses at the B.Cu trunk crossings and is
also rejected by XTAL/RTL_3V3/SSD_3V3 contacts. Preserve V167-V171 as raw
implementation evidence; V169 is the current experimental reference only,
while V158/V160 remain the last promoted support basis.
V172 keeps the V169 pair topology but moves the lower exits below the crystal
row; native DRC still finds the U2/SPISI/RTL3V3/RTL1V1/PEDET ownership
conflicts and one P/N endpoint crossing. It is rejected. The V169 saved-board
audit nevertheless passes native connectivity for U1.61→J1.55 and
U1.62→J1.53, and its trace-removal negative control fails as required; that
is connectivity evidence only, not a route PASS. The next repair should move
the directly conflicting local support geometry or allocate a distinct local
escape cell, not waive the crossings.
V173 translates U1/U2 and the local crystal/rail support upward by 8 mm and
regenerates REFCLK from the transformed U1 pads, but stale external local-net
copper remains and creates unrelated SPI/sideband findings. V174 repeats the
same coherent placement after globally scrubbing superseded local-net copper.
Native DRC then reports zero `shorting_items` and zero `tracks_crossing` for
the disposable fixture; the remaining findings are inherited zone,
manufacturing, and intentionally open support pads. The V174 native audit
passes U1.61→J1.55 and U1.62→J1.53, with a trace-removal negative control.
Promote V174 only as the translated REFCLK placement/topology sub-primitive;
the remaining RTL9210B rails, SPI, reset, USB, M.2, firmware, and full Path-B
gates remain open.
V176/V177 attempt to co-author the translated crystal routes without moving
the cluster and are rejected for XTAL/REFCLK source-field contacts. V178
was also rejected because it accidentally layered a second REFCLK route over
V174's existing copper; it is retained as an authoring negative. V179 is the
correct clean experiment: it removes the old local routes, moves Y1/C1/C2/R1
west of U1, and regenerates XTAL_IN/XTAL_OUT/RSET plus REFCLK once. Native
DRC now shows no REFCLK-to-crystal conflict; only four localized crystal/
RSET/QFN source defects remain. V179 is not promoted yet, but it is the best
translated support-placement basis for the next pad-aware source escape.
V175 restores the validated V158 crystal copper translated onto V174. Native
DRC exposes only the expected local co-allocation failures: REFCLK-P meets
the translated XTAL_IN transition and REFCLK-N crosses the translated
XTAL_OUT span. Reject V175 as a route implementation, not a placement or
authority failure; V174 remains the clean REFCLK-only basis. The next trial
must move the two REFCLK lower transitions around the translated crystal
field or co-author the crystal exits together.
The current promoted disposable RTL_5V/control basis is
`PHASE24_RTL9210B_RTL5V_BELOW_C5_V137.kicad_pcb`, layered on the V131
CLKREQ/PEDET support evidence. V97 moved
`XTAL_OUT` above the local support field and added U1.55; V98 and V99 are
rejected crossing variants; V100 routes `RTL_1V1` around the left endpoint of
the new XTAL_OUT span and restores the U1.55-to-existing-1V1 connectivity.
V101's first U1.36 handoff shorted the retained RTL_3V3 field and is rejected;
V102 routes U1.36 around the right side of that field and restores the
remaining 1V1 pad-group join. Native DRC has no `shorting_items` or
`tracks_crossing` class for V102.
V103/V104 then tested the next RTL_3V3 U1.34 handoff. V103 did not reach the
existing-layer endpoint and left U1.34 isolated; V104 reached the native
3V3 via and connected U1.34, but native DRC reported two track crossings.
Both are rejected route-allocation trials; the current promoted basis remains
V102 and RTL_3V3 U1.34 is still open.
V105 moved the handoff above the SPI channels but its B.Cu vertical still
crossed SPICLK and SPISI. V106 keeps the departure on F.Cu until clear of
those channels, then joins the existing 3V3 via field; native DRC reports no
`shorting_items` or `tracks_crossing`, and saved connectivity joins U1.34 to
the existing C3/R2/R3/U1.20 3V3 group. Promote V106 only as the disposable
U1.34 edge-group basis; full Path-B support remains open.
V107–V111 are rejected control-sideband route trials: V107 shorted adjacent
CLKREQ_N/PERST_N vias, V108/V109 crossed the retained RTL_1V1/RTL_3V3 field,
and V110/V111 retained companion-control or 1V1 crossings. These are
authoring/allocation failures, not evidence against the RTL9210B control
topology. The next control trial must use genuinely layer-separated launches.
V112 is the first genuinely layer-separated control attempt: it removes
control-control shorts, but native DRC still reports three crossings against
the inherited RTL_1V1/RTL_3V3/upper-rail fields. It is rejected as an
implementation trial; no architecture or layer-policy change follows.
V113 reduced the problem to one RTL_3V3 crossing; V114 removed that crossing
but left CLKREQ/PERST clearance contact. V115 widens the separation and passes
the focused control-pair gate: native connectivity joins U1.13→J1.52 and
U1.14→J1.50, with no `shorting_items` or `tracks_crossing`. Promote V115 only
as the disposable CLKREQ_N/PERST_N sub-primitive; PEDET and remaining Path-B
endpoints stay open.
V123/V124 joined R3.1 electrically but crossed the existing SPI/PEDET/1V1
fields. V125/V126 moved the return farther right but contacted the C5/RTL_3V3
field; V127/V128/V129 successively reduced the defect to the PERST elbow.
V130 reduced it to one upper-rail crossing. V131 overpasses that rail and
passes the focused CLKREQ audit: R3.1/U1.13/J1.52 are connected, with no
`shorting_items` or `tracks_crossing`; the route-removal negative control
fails as required. Promote V131 only as the disposable complete CLKREQ
sub-primitive; RESET_N, RTL_5V, high-speed links, and full Path-B validation
remain open.

## Current RTL9210B SPISI status — V201 rejected

V201 is rejected as a single-net route implementation. It connected U1.18
to U2.5 in saved native connectivity, but DRC found C1 ground contact at
the destination and conflict with the promoted SPICLK launch at the QFN
source. The next credible route must co-author SPICLK/SPISI source escapes
and the local destination support field together.

## Current RTL9210B crystal/SPICLK basis — V200

`PHASE24_RTL9210B_SPICLK_CRYSTAL_EAST_V200.kicad_pcb` is the promoted local
support basis. V198 was rejected for Y1.1 contact; V199 removed the shorts
but retained an RSET/XTAL_OUT crossing. V200 corrects the RSET transition.
Native KiCad DRC reports 318 findings / 26 unconnected items with zero
`shorting_items` or `tracks_crossing`; saved native connectivity and four
negative controls pass.

V200 is disposable support evidence only. Remaining SPI/control paths,
mode validation, and production integration remain open.

## Current RTL9210B crystal/SPI allocation — V197 rejected

V197 was the first coherent west shift of the complete Y1/C1/C2/R1 support
cluster. It passed saved connectivity and four negative controls, but native
DRC found 315 findings / 27 opens including XTAL_OUT/SPICS crossing and
SPISO/C2-ground contact. The shift is rejected as a placement class. The
remaining work is a coordinated SPI/crystal destination-field allocation;
Path A and production CAD remain unchanged.

## Current RTL9210B SPICLK status — V194–V196 rejected

V194–V196 were disposable SPICLK route trials from U1.19 to U2.6. V194
shorted adjacent SPISI and crossed XTAL_IN; V195's combined XTAL_IN
relocation introduced crystal/source conflicts; V196 retained the V193
crystal geometry but contacted C2 ground and crossed XTAL_OUT. These are
route-allocation failures, not a Path-B architecture rejection. The next
credible experiment must co-author the local crystal/SPI field or move the
small support cluster coherently. Path A and production CAD remain unchanged.
V116 adds the PEDET U1-to-M.2 launch on an independent F.Cu corridor. Native
 connectivity joins U1.8 to J1.69 and native DRC reports no
 `shorting_items` or `tracks_crossing`. Promote V116 only as the disposable
U1-to-socket PEDET sub-primitive; R2 source connection and remaining Path-B
endpoints stay open.
V117 electrically joined R2 but crossed two SPI traces. V118 moved the
source outboard but crossed the 1V1 return wall; V119 moved below that wall
but introduced PEDET/ground and PEDET/1V1 clearance/shorts. V120 removed the
field crossings but crossed XTAL_IN; V121 removed that crossing but left a
0.125-mm C2 clearance defect. V122 shifts the bottom return right and passes
the focused native PEDET audit: R2.1/U1.8/J1.69 are connected, and the
trace-removal negative control fails as required. Promote V122 only as the
disposable complete PEDET sub-primitive; remaining Path-B gates stay open.
Native saved-board inspection joins U1.55 with U1.16/U1.25/U1.40/U1.50/
U1.60/U1.63/C4.1, and a centerline scan finds no different-net track crossing
for the new escape. The disposable fixture still has 19 intentional/open
support connections and inherited manufacturing/zone findings; this is a
support sub-primitive promotion, not a Path-B or Phase 24 closure.

The direct current KiCad CLI report for V100 counts inherited zone, hole,
solder-mask, thermal, and other disposable-fixture findings in addition to
unconnected items. Those are retained evidence and are not waived. The
signal-specific result is recorded separately: no new short or track-crossing
class was found for the V100 escape. The next open Path-B support gate is the
remaining QFN support/control/power connectivity, followed by complete
USB/M.2/mode/firmware and integrated validation.

All later sections in this append-only file are historical experiment records;
their “current” wording is local to the checkpoint they describe and must not
override this section.

## Authoritative current state — 2026-09-07

V76 and V77 are rejected U1.40 RTL_1V1 edge-group trials from the promoted
V75 basis. V76 placed the transition at (92.8,68.8) and directly shorted the
RTL_3V3 left escape; native DRC reported 9 violations / 24 opens. V77 moved
the transition farther left to (90.8,68.8), but its B.Cu collector crossed
the retained RTL_3V3 diagonal and still shorted the RTL_3V3 via; native DRC
reported 8 violations / 24 opens. V78 tested an upper-perimeter transition
for U1.40 and is rejected at 14 violations / 24 opens: the F.Cu departure
crosses the RTL_3V3 field and adjacent U1 pads, while the B.Cu span collides
with SPICLK/RTL_3V3. These are local route-implementation failures, not a
Path-B electrical decision. V75 remains the promoted 1V1 sub-primitive;
U1.40 and the remaining 1V1 groups are open.

V79 reallocated the local RTL_3V3 escape before testing U1.40. It removed the
previous U1.40/3V3 short and reduced the signal failures to a U1.40 dogbone
clearance violation against adjacent pad 41 and a 3V3 clearance violation at
the no-net U1.35 field; native DRC reported 8 findings / 25 opens. V80 moved
the 3V3 segment again but left a dangling endpoint while retaining the U1.40
pad-field clearance defect; native DRC reported 8 findings / 25 opens. Both
are rejected route-allocation/authoring trials. This confirms that the local
3V3 corridor is the right decision surface, but the QFN edge escape still
needs a pad-aware dogbone and a completely connected 3V3 path.

V82 tested a pad-aware diagonal U1.40 escape against the V79 reallocated
3V3 field. Native DRC rejected it at 11 findings / 25 opens: the departure
shorts/crosses the U1.39/RTL_3V3 pad escape and also violates the adjacent
U1.38 solder-mask/clearance envelope. This is further evidence that U1.40
must be co-authored with the neighboring 3V3 source field, not added as an
isolated dogbone.

V83 is a diagnostic-only pad-width sensitivity trial from V79. It shrank the
68 perimeter pads in the disposable U1 footprint without changing copper,
rules, or nets; native DRC remained 8 findings / 25 opens, with the same
U1.40-to-U1.41 and RTL_3V3-to-U1.35 clearance failures. This does not justify
changing the land pattern or relaxing rules; authoritative package evidence
is still required before either could be considered.

V84/V85 tested a coordinated U1.39/U1.40 source-field reallocation using the
repository's validated JLC rule basis. V84 duplicated the U1.40 via and V85
removed the retained 3V3 via while replacing local tracks; both are rejected
authoring variants. V86 corrects those mutations, preserves the native 3V3
via, sets the disposable default netclass to 0.13208-mm minimum track / 0.15-mm
clearance, and joins U1.40 to the promoted RTL_1V1 collector. Native DRC is 6
inherited isolated-GND/silkscreen warnings with no signal violations, and
native connectivity joins U1.40/U1.16/U1.25/U1.50/C4.1. Promote V86 only as
the U1.40 edge-group sub-primitive; all remaining Path-B gates stay open.

V88–V94 are rejected U1.55/U1.60 bottom-edge trials. V88's U1.55 via
shorted the retained XTAL_OUT launch; V89/V90/V91 placed U1.60 transitions in
the XTAL_IN corridor; and V92–V94 exposed successive QFN/XTAL gap allocation
errors. V95 corrects the latter with an F.Cu dogleg to (103.0,73.8), a B.Cu
span above XTAL_IN, and a drop at x107.0. Native DRC is 8 inherited
isolated-GND/silkscreen warnings with no signal violations; native
connectivity joins U1.60 with U1.16/U1.25/U1.40/U1.50/C4.1. Promote V95
only as the U1.60 edge-group sub-primitive; U1.36/U1.55/U1.63 and other
Path-B support remain open.

V96 adds U1.63 to the promoted RTL_1V1 F.Cu launch. Native DRC remains 8
inherited isolated-GND/silkscreen warnings with no signal violations; native
saved connectivity joins U1.63 to C4.1 and the U1.16/U1.25/U1.40/U1.50/U1.60
group. The fixture falls from 24 to 23 opens. Promote V96 only as the U1.63
edge-group sub-primitive; U1.36/U1.55 and all non-1V1 Path-B gates remain
open.

V81 tested the same V79 U1.40 path with a 0.15-mm fine-pitch dogbone. Native
DRC rejected it at 10 findings / 25 opens: the escape still has only
0.1647-mm clearance to U1.41, the reallocated 3V3 segment remains 0.100 mm
from U1.35, and the 0.15-mm width violates the board's 0.200-mm minimum.
This closes the fine-width escape hypothesis; do not relax the board rule.

### RTL9210B source-field update — current

V26, V27, V28, V29, and V30 are rejected disposable source-field route
implementations. V31 is the best complete five-net SPI source/target
primitive so far: native KiCad reports 4 inherited findings / 39 unrelated
opens, with no SPI signal shorts, crossings, or clearance violations; the
saved-board SPI audit passes SPISI, SPICLK, SPISO3, SPISO, and SPICS, and its
trace-removal negative control fails. V31 is not full Path-B closure because
its V24 base omits the XTAL/RSET support joins. V32 attempted those joins and
is rejected at 11 violations / 35 opens for support-corridor crossings and
shorts. The next step is a coordinated support-field allocator based on the
V31 five-net result; production CAD and Path A remain unchanged.

V33 is also rejected as a support implementation: native KiCad reports 15
violations / 35 opens, including XTAL_IN/XTAL_OUT/RSET shorts and support-pad
crossings. Its B.Cu long-span concept does not clear the existing passive
cluster. The next candidate must relocate or reauthor the support island
coherently; no production CAD or Path-A asset changed.

V35 moves Y1/C1/C2/R1 together inside the fixture outline and separates the
U1-side handoff vias. Native KiCad reports 4 inherited findings / 34 opens,
with no signal violations. The saved-board SPI audit passes all five SPI
endpoints with its trace-removal negative control, and the V35 support audit
passes XTAL_IN, XTAL_OUT, and RSET with its XTAL_OUT negative control. This
closes the local moved-cluster support sub-gate only; RTL_1V1, RTL_3V3,
RTL_5V, controls, grounds, USB, M.2, and full Path-B validation remain open.

V37 tested explicit F.Cu pad-to-via access feeding shaped B.Cu rail fields.
It is rejected at 41 native violations / 34 opens: the via fanout collides
with neighboring rail pads and retained SPI/source-field geometry. This does
not invalidate V35; it rules out an indiscriminate shared via-field solution.
The next rail candidate must partition the rail escapes or move the local
decoupling pads coherently.

V36 tested broad F.Cu local zones for RTL_3V3, RTL_5V, and RTL_1V1. It is
rejected: native DRC still reports rail opens and an inherited GND thermal
finding, because the zones do not provide complete pad/via access around the
malformed disposable support footprints. No production CAD or Path-A asset
changed. The next rail candidate must use explicit native pad/via access and
preserve the V35 SPI/support geometry.

V38 normalized C3/C4/C5 to ordinary local-coordinate C_0603 footprints;
native DRC remained at the V35 inherited baseline with no new violations.
V39 added the RTL_5V branch against corrected C5, but is rejected at 7
findings / 32 opens because its B.Cu handoff crosses the retained RTL_3V3
trunk and SPISI transition. The corrected capacitor CAD is retained; the
next candidate must jointly allocate the 3V3/5V rail corridors.

V41 added an RTL_3V3 local fanout from the corrected-cap V38/V35 basis. It is
rejected at 7 native violations / 30 opens: one U1 pad-field clearance, one
XTAL_IN-adjacent via, and one RSET-via conflict on the U2 branch remain. The
trial did not alter SPI or XTAL/RSET copper; the next 3V3 pass must split the
local source fanout from its downstream U2 branch.

V42 partitioned RTL_3V3 source and U2 branches while restoring the validated
U1.20/C3 trunk. Native DRC improved to 6 findings / 31 opens and removed the
V41 U1 pad-field defect; one RSET-adjacent via/transition remains, so V42 is
not promoted. The source/downstream split is retained for the next rail-pad
join pass.

V44 removed the redundant V43 transition and returns the 3V3 branch to 4
inherited GND/silkscreen findings with no signal DRC violations. Saved-board
inspection shows U1.34/U1.39/U2.3/U2.8 are joined, while U1.20/C3 remains a
separate valid trunk and U1.52 is still unjoined. V45 attempted that U1.52
join and is rejected at 10 findings / 30 opens for repeated XTAL_IN-via
clearance violations. The next step must relocate the 3V3 support handoff or
co-author the U1.52/XTAL_IN source field; no production CAD changed.

V46 co-authored XTAL_IN and U1.52 from the V44 partial branch. It is rejected
at 9 native violations / 30 opens: the proposed transitions collide at the
0.4-mm QFN source pitch and XTAL_IN/RTL_3V3 short/cross. V44 remains the
cleanest partial 3V3 result; the next credible class is local U1/support
rotation or coherent support relocation, not further coordinate nudging.

V47 corrected a generator/authoring defect in the disposable RTL9210B U1
footprint frame. The footprint anchor was inconsistent with its saved pad
coordinates; V47 normalizes the frame while preserving every absolute pad
location. Reload inspection confirms U1.18/U1.20/U1.22 and U1.51-U1.54 retain
their intended physical coordinates. Native DRC is back to the V44 inherited
baseline (4 findings / 31 opens) with no new signal violations. V47 is the
current disposable Path-B authoring basis, not a full support-network PASS;
next work must reauthor the remaining rail/support fields from this corrected
frame.

V49 uses the corrected frame to co-author the U1.52 RTL_3V3 escape around the
existing XTAL_IN field. Native DRC returns to the 4 inherited warnings / 30
opens baseline, and saved-board connectivity joins U1.52 to U1.34/U1.39/U2.3/
U2.8 without a new signal violation. V49 is the current cleanest 3V3 handoff
basis. V50's direct R2/R3-to-U1.20/C3 rail join is rejected at 7 findings /
28 opens because the straight F.Cu rail crosses retained SPISO, SPICS, and
SPISO3 departures. The next class must allocate rail taps on another layer or
coherently reauthor the local support field; no production CAD changed.

V51 attempted a B.Cu collector for R2/R3, but is rejected at 15 findings /
28 opens. The pad escapes were authored toward the opposite-net resistor
pads (PEDET/CLKREQ_N), and the proposed B.Cu collector also shorts/crosses
the retained SPISO3 transition. This is a route-authoring failure; V49
remains the current cleanest basis and the next pass must verify resistor pad
orientation before selecting a separate collector corridor.

V52 normalizes the native R2/R3 footprint frames and derives pad-2 escapes
from the saved pad/net identities. The taps are collected on a B.Cu corridor
that approaches the existing U1.20/C3 trunk from the SPI-clear side. Native
DRC is 5 non-signal isolated-copper/silkscreen warnings / 28 opens, and the
saved-board connectivity audit joins all RTL_3V3 pads across U1, U2, R2, R3,
and C3. V52 is promoted as the current disposable RTL_3V3 rail basis; the
remaining Path-B support rails and controls are still open.

V57 completes the RTL_5V disposable rail primitive from the native U1/C5 pad
map. U1.33 escapes above the native SPI endpoints, U1.17 descends on the
right, and C5.1 launches from its right side with a cleared via. Native DRC is
5 non-signal isolated-copper/silkscreen warnings / 26 opens; saved-board
connectivity joins U1.17, U1.33, and C5.1. V53-V56 remain rejected routing
experiments. V57 is promoted as the current RTL_5V basis; RTL_1V1, controls,
ground, USB, M.2, and full Path-B validation remain open.

V59 is a valid RTL_1V1 sub-primitive for the native U1.16-to-C4.1 path. It
uses the right-edge U1 escape, a B.Cu dogleg below the 3V3 handoff, and a
right-side C4 launch that clears the adjacent C3 ground pad. Native DRC is 5
non-signal isolated-copper/silkscreen warnings / 27 opens with no new signal
violations. V58 is rejected for using the C3-adjacent launch. The remaining
RTL_1V1 U1 edge groups are still open.

V60 attempted a complete RTL_1V1 perimeter collector and is rejected at 35
native violations / 20 opens. The candidate crossed the existing XTAL_IN/
XTAL_OUT and RSET fields, entered the SPICS source transition, and placed a
left-edge via too close to the 3V3 escape. This is a route implementation
failure, not a supply-rail authority decision. V59 remains the only promoted
1V1 sub-primitive; the remaining edge groups require separate corridors.

V63 validates the U1.25-to-C4.1 RTL_1V1 sub-primitive. U1.25 exits left of
the SPICS via, rises to the upper perimeter, and joins the existing C4.1
right-side corridor without crossing retained copper. Native DRC is 5
non-signal isolated-copper/silkscreen warnings / 26 opens with no new signal
violations. V60-V62 remain rejected full/perimeter and upper-corridor trials;
the remaining RTL_1V1 U1 edge groups are still open.

V75 validates the U1.50 left-edge RTL_1V1 sub-primitive. Its B.Cu collector
runs below the RTL_3V3 vertical handoff and joins the existing C4.1 path
without signal crossings. Native DRC is 6 non-signal isolated-copper/
silkscreen warnings / 25 opens; saved-board connectivity joins U1.50 with
U1.16, U1.25, and C4.1. V74 is rejected for its RTL_3V3 crossing. Remaining
RTL_1V1 edge groups are still open.

V64 attempted the U1.60 bottom-edge RTL_1V1 group and is rejected at 8 native
findings / 26 opens. Its B.Cu drop entered the retained XTAL_OUT segment at
y=77 and the proposed offset also fell inside the XTAL/RSET corridor. V63
remains the cleanest promoted 1V1 basis; the remaining bottom/left groups need
a route around the native XTAL_OUT endpoint, not another direct drop.

V65 attempted U1.55 bottom-edge RTL_1V1 routing and is rejected at 15 native
findings / 26 opens. The rightward escape clipped adjacent no-net U1.56, and
the proposed transition was too close to the XTAL_OUT via/segment. This is a
local source-field allocation failure; V59 and V63 remain promoted 1V1
sub-primitives and U1.55 remains open.

V68 attempted U1.60 bottom-edge RTL_1V1 routing above the XTAL_OUT launch and
is rejected at 7 native findings / 26 opens because the F.Cu leg intersects
the retained XTAL_IN launch near x=107.5. The C4-side B.Cu join was otherwise
clear. U1.60 requires coherent XTAL/support-field relocation or an alternate
source-side layer escape; further direct bottom-edge nudging is not promoted.

V69 is a diagnostic discriminator: removing only the obstructing XTAL_IN
route allows the U1.60 RTL_1V1 corridor to run with no signal DRC violations.
The report has 6 findings / 28 opens, consisting of the intentionally
disconnected XTAL_IN/support path, one diagnostic dangling endpoint, and
inherited non-signal warnings. This confirms a local XTAL/support placement
collision rather than an impossible U1.60 rail route; V69 is not promoted.

V70 attempted a coherent Y1/C1/C2/R1 relocation with U1.60 1V1 routing and
is rejected at 18 native findings / 27 opens. The selected support island was
too close to the board edge, and the regenerated XTAL_IN/XTAL_OUT/RSET paths
collided locally. This is a placement/route implementation failure; V69 still
proves the U1.60 corridor when XTAL_IN is removed, and production CAD remains
unchanged.

A native 0-degree U1 orientation probe is now retained as the next coordinated
source-field basis. It uses transformed native pad coordinates, removes only
the disposable local support copper, and produces no signal DRC violations
(six inherited warnings; 45 expected opens). This is not support closure, but
it provides a materially different perimeter allocation for the complete
lower-QFN regeneration.

## Current RTL9210B SPISO slice — V193

`PHASE24_RTL9210B_SPISO_U123_U2_V193.kicad_pcb` is the promoted SPISO basis.
V190/V191 were rejected for real source/destination conflicts; V192 was
rejected for contacting the RSET support pad. V193 uses the corrected
threaded source and destination dogleg. Native DRC reports 308 findings /
26 unconnected items with zero `shorting_items` or `tracks_crossing`; saved
native connectivity and the trace-removal negative control pass.

The remaining SPI/control paths, mode validation, and production integration
remain open.

V72 tested the upper-right coherent XTAL/RSET relocation with U1.60 1V1 and
is rejected at 51 native findings / 30 opens. The placement margin was clear,
but the regenerated paths used incorrect post-transform support-pad
coordinates, causing local XTAL/RSET/rail/SPI collisions. This is an
authoring/route implementation failure; the next relocation must derive every
moved support pad from the saved native footprint after transform.

V73 regenerated the moved support paths using the actual post-transform native
pad coordinates, but is rejected at 32 native findings / 28 opens. The
remaining defects are route allocation: the long RSET perimeter crosses SPI/
3V3, and the U1-side XTAL_IN departure is too close to RTL_3V3. The
transformed-endpoint authoring issue is corrected; future support work must
use shorter local corridors or another coherent field allocation.

V40 jointly reauthored the 3V3/5V spines after correcting the rail-cap CAD.
It is rejected at 8 native violations / 32 opens: the outer 3V3 spine
collides with the retained SPISO3 source departure, while the 5V branch
still contacts the SPISI handoff and the corrected C5 transition. The next
candidate must preserve the validated V24 3V3 source departure and add rail
access in a partitioned local field.

Path B remains a disposable RTL9210B qualification path. The current best
combined support baseline is `PHASE24_RTL9210B_ROTATED_SUPPORT_RELOCATION_V8`
plus the validated RTL_5V V9 rail primitive. V8 native support and SPI audits
pass with negative controls; V9 natively connects U1.17/U1.33/C5.1. The
RTL_3V3 V10/V11 probes are rejected route implementations. Current open work
is a new 3V3/support corridor or coherent local-island reauthoring, followed
by remaining control/sideband, RTL_1V1, ground, USB, M.2, power, and full
Path-B validation. Path A, production acreage CAD, and approved architecture
remain unchanged.

The 90-degree mixed-layer V18/V19/V20/V21 source-field trials are retained
as disposable evidence. V20 reduced the candidate to 3 findings / 41 opens
by fixing SPISI transition proximity; V21 rejected a down/right RTL_3V3
departure because it entered adjacent U1 RTL_5V/RTL_1V1 pads and crossed
SPICLK. The next implementation must use a transformed-pad-aware escape cell
before downstream routing is regenerated.

The transformed-pad-aware V22 diagonal probe is rejected at 9 native
violations / 41 opens: RTL_3V3 collides with SPISO3/SPICS and crosses the
SPICLK B.Cu channel. V20 remains the best 90-degree implementation baseline;
V22 confirms that hand-placed diagonals are not a substitute for a formal
escape-cell construction.

`phase24_rtl9210b_escape_cell_map.py` now derives the rotated U1 pad centers,
orientations, dimensions, and package-center outward vectors from native
KiCad objects, saving `PHASE24_RTL9210B_ESCAPE_CELL_MAP_NATIVE_V15.txt`.
This is the authoritative geometry input for the next formal escape-cell
generator; no source coordinates are inferred from pad-number order.

## Current live Path-B step — 2026-09-07

### Current open gate

Path B remains a disposable qualification path. The latest fully scrubbed
rotated-U1 staggered-via SPI escape
`PHASE24_RTL9210B_ROTATE_U1_STAGGERED_SPI_V1` is rejected as a route
implementation: native KiCad reports 24 violations / 40 unconnected items,
including real SPI shorts/crossings and source-field clearance failures.
The subsequent left-relocation probe exposed and corrected a separate
authoring defect in the disposable U2 flash footprint: its anchor was at
`(20,18)` while its pad coordinates were effectively absolute. The corrected
coordinate-frame candidate `PHASE24_RTL9210B_U2_CORRECTED_FOOTPRINT_V1`
reports 53 violations / 39 opens because the test placement still overlaps
the rotated U1/source field and its SPI permutation is not yet routed
legally. This is footprint/route implementation evidence, not a Path-B
architecture rejection. The corrected footprint frame must be used for any
further U2 placement comparison.

The corrected-footprint left/90-degree placement
`PHASE24_RTL9210B_U2_CORRECTED_LEFT_ROT90_PLACEMENT_V1` is mechanically/native
placement-clean apart from the inherited six GND/footprint findings (6
findings / 44 opens) and introduces no signal short. A first mixed-layer SPI
route against its real transformed pads,
`PHASE24_RTL9210B_U2_CORRECTED_LEFT_ROT90_SPI_V1`, is rejected at 24
violations / 39 opens for source/target-field clearances and SPI shorts or
crossings. This separates the corrected footprint placement evidence from
the still-failing route implementation; no production CAD or Path-A asset
changed.

A focused source-breakout probe,
`PHASE24_RTL9210B_U1_QFN_SINGLE_DOGBONE_V1`, scrubbed retained XTAL/RSET
copper and tested SPISI alone with a 45-degree departure to a 0.6/0.3-mm
ordinary-via transition outside the pad field. Native KiCad reports 5
findings / 44 opens: no signal short, crossing, or clearance violation from
the dogbone; the findings are incomplete-probe dangling items and inherited
ground conditions. This validates the local departure geometry. The next
five-net trial must preserve that clearance and regenerate neighboring
XTAL/RSET routes independently.

The five-net source-field follow-up was regenerated with straight outward
departures before the staggered diagonals. It improves to 17 native
violations / 44 opens but remains rejected: the SPICLK/SPISO3 transitions
still short/collide at their 0.6-mm via spacing, with one additional source
clearance finding. This localizes the remaining defect to transition layout
after the pad envelope; it does not reject the validated single-net dogbone
or the RTL9210B architecture.

The complete corrected-U2 partition trial
`PHASE24_RTL9210B_COMPLETE_SPI_PARTITION_V1` is rejected at 12 native
violations / 39 opens. The corrected U2 footprint loads with the intended
0-degree pin map, but appending downstream routes to the source-only tails
causes SPISO/SPICS crossing at the F.Cu handoff and SPICLK/SPISO3 conflicts
with the B.Cu source tails. The next implementation must regenerate the
whole five-net branch in one pass; appending to the source-only probe is not
valid evidence of placement failure.

The fully regenerated V3 branch
`PHASE24_RTL9210B_FULL_REGENERATED_SPI_V3` is rejected at 8 native
violations / 40 opens. Removing the lower SPISO/SPICS B.Cu source tails
caused the SPICS F.Cu corridor to cross the regenerated source dogbones,
while SPICLK/SPISO3 still interact on the upper B.Cu departure. This
confirms the five-net source and downstream layer/channel plan must be
generated as one deliberately separated topology; neither Path A nor the
production board was changed.

The channelized full branch
`PHASE24_RTL9210B_CHANNELIZED_FULL_SPI_V1` is now the preferred SPI-route
baseline. Native KiCad reports 1 inherited isolated-GND warning / 40
unconnected support items, with no SPI shorts, crossings, or clearance
violations. `phase24_rtl9210b_spi_connectivity_audit.py` derives connectivity
from the saved native board and passes all five U1/U2 endpoints; its negative
control also fails after removal of a necessary SPISI trace. This closes the
RTL9210B SPI local route/connectivity sub-gate only; remaining support,
control, USB, M.2, power, and full Path-B validation remain open.

The rotated-U1 support relocation was subsequently re-authored through V8.
V8 places the XTAL_OUT transition beyond the U1 QFN pad envelope. Native
KiCad reports only two inherited findings (isolated B.Cu GND fill and a
silkscreen overlap), with no signal short, crossing, or clearance violation.
Saved-board native connectivity passes XTAL_IN (U1.53/Y1.1/C1.1), XTAL_OUT
(U1.54/Y1.2/C2.1), and RSET (U1.51/R1.1). The fixture still has 35 unrelated
unconnected items, so V8 is a local support-route PASS, not full Path-B
closure. Production CAD and Path A remain unchanged.

The V8 combined fixture was rechecked with the saved-board native SPI audit:
SPISI, SPICLK, SPISO3, SPISO, and SPICS all connect between the rotated U1
and corrected U2 pads, and the SPISI trace-removal negative control fails as
required. This confirms that the support relocation did not regress the
channelized SPI baseline. The next open class is remaining control/sideband,
rail-join, ground-access, USB, M.2, and power completion.

The RTL_5V V9 disposable rail probe connects U1.17, U1.33, and C5.1 using
ordinary transitions outside the QFN field. Native KiCad reports 4 inherited
findings / 33 unconnected items, with no new signal violation; saved-board
connectivity confirms all three RTL_5V endpoints. V9 is retained as a valid
rail primitive while the remaining RTL_1V1/RTL_3V3/control and support joins
remain open.

RTL_3V3 probes V10/V11 are rejected route implementations. V10 collided
with retained SPICLK/XTAL_IN escapes; V11 moved those transitions but its
lower B.Cu trunk crossed SPICS and the Y1 XTAL_IN launch, reporting 12 native
signal violations / 31 opens. The next 3V3 attempt must use a different
corridor topology.

The top/outer RTL_3V3 V12 probe is also rejected. Its U1.20 source departure
crosses the validated SPISI/SPICLK F.Cu escapes, while the U1.52 transition
still reaches the XTAL_IN/Y1 launch. Native KiCad reports 9 violations / 31
opens. The next attempt must co-author the rail with the QFN source escape
and preserved SPI.

The complete four-net QFN-field V14 probe regenerated SPISI, SPICLK, SPISO3,
and RTL_3V3 together but is rejected at 24 native violations / 31 opens.
Direct source departures cross the dense U1 pad field, the B.Cu channels
cross each other, and RTL_3V3 also collides with retained XTAL_IN. This is a
multi-net route implementation failure. The next class must change the U1 or
local-support placement/orientation and regenerate the field, not add more
coordinate-only vias.

Formal native-pad source field V24 is a local PASS: native KiCad reports no
signal shorts, crossings, or clearance violations, positive saved-board
connectivity passes SPISI/SPICLK/SPISO3/RTL_3V3, and the SPISI trace-removal
negative control fails as required. Remaining RTL9210B support is open.

The V25 completion probe added SPISO and SPICS to V24 but is rejected at 4
native violations / 39 opens: SPISO crossed the retained SPISO3 F.Cu escape
and the SPICS transition entered that source corridor. V24 remains the valid
four-net source baseline; the remaining channels need a source-field-aware
layer swap.

The 90-degree U1 placement/source-field V16 probe is rejected at 7 native
violations / 41 opens. Straight top-row departures are mechanically cleaner,
but the B.Cu channels still cross at the U2 handoff. The orientation remains
a placement alternative; the next route must stagger downstream drops outside
the horizontal channel envelope.

Mixed-layer 90-degree source-field V17 reduces the placement candidate to 5
native findings / 41 opens, but remains rejected: SPISI/SPICLK transition
proximity and their reversed B.Cu handoff still create real shorts/crossing.
This improves over V16 and confirms that one reversed-order channel must move
to an independent F.Cu corridor before the orientation can be evaluated.

Integrated source-escape V13 regenerated SPICLK with RTL_3V3 but is rejected
at 10 native violations / 31 opens. SPICLK still crossed the retained SPISI
departure, while the RTL_3V3 transitions collided with SPICLK and XTAL_IN.
The next candidate must regenerate a multi-net QFN field
(SPISI/SPICLK/SPISO3/RTL_3V3) together.

`phase24_rtl9210b_support_v8_audit.py` now provides a reusable saved-board
audit for the V8 support baseline. It derives XTAL_IN, XTAL_OUT, and RSET
connectivity from native KiCad connectivity and passes the required
XTAL_OUT-removal negative control.

The normalized rotated-support V3 route
`PHASE24_RTL9210B_ROTATED_SUPPORT_RELOCATION_V3` is rejected at 14 native
violations / 37 opens. XTAL_IN and RSET remain natively connected, but
XTAL_OUT is disconnected; the attempted outside transitions still enter the
rotated U1 right-side power field and create clearance/short/crossing
findings. V2 remains the better support-placement reference; V3 is route
implementation evidence only and does not alter Path A or production CAD.

The V3 source-transition spacing trial
`PHASE24_RTL9210B_U1_QFN_FIVE_DOGBONES_V3` remains rejected at 10 native
violations / 44 opens. Increasing the lower transition-row separation left
the same single SPISO-to-SPISO3 clearance violation (actual 0.100 mm versus
0.200 mm required), with no shorts or crossings. This identifies the next
required change as a different post-pad fanout shape, not more via-row
nudging.

The V4 lateral-transition source probe
`PHASE24_RTL9210B_U1_QFN_FIVE_DOGBONES_V4` is the first five-net source
escape with no signal violations. Native KiCad reports 9 findings / 44 opens;
the remaining findings are incomplete-probe dangling items and inherited
ground-zone conditions. Moving SPISO3 laterally removed the prior
SPISO/SPISO3 clearance defect. This closes the local five-net QFN source
escape sub-gate only; extension to corrected U2 and regenerated support is
still open.

The corrected-U2 SPISO3 handoff V2
`PHASE24_RTL9210B_SPISO3_CORRECTED_U2_V2` is rejected at 16 native
violations / 43 opens. Moving the handoff to a north-side F.Cu corridor
still crosses the neighboring SPISI/source-field geometry and retained
XTAL paths. The one-net result confirms that U1-to-U2 routing must be
co-designed as a complete five-net escape; no production CAD or Path-A
asset changed.

The transition-spacing micro-variant
`PHASE24_RTL9210B_U1_QFN_FIVE_DOGBONES_V2` was also rejected. Native KiCad
reports 10 violations / 44 opens, including one remaining SPISO/SPISO3
clearance violation and only expected incomplete-probe/inherited findings
otherwise. The change did not improve the V1 source-field result; no
production CAD or Path-A asset changed.

The corrected-footprint far placement with an order-preserving two-layer
partition, `PHASE24_RTL9210B_U2_CORRECTED_FAR_PARTITION_SPI_V1`, is rejected
at 30 violations / 40 opens. Native evidence shows the remaining failure is
the rotated U1 source-field escape: the long source dogbones and transition
vias still enter adjacent QFN pad clearances and cross the retained
XTAL_OUT/source region. The farther U2 placement did not itself create the
dominant defect. This class is not evidence against RTL9210B; the next
credible step is a native QFN breakout/footprint escape treatment (or a
different U1 orientation with source transitions outside the pad field), not
more target-row permutations.

The disposable `PHASE24_RTL9210B_QFN_SPI_POWER_PARTITION_V1` probe was
authored after correcting a KiCad Python net-handle defect. Native KiCad
reports 22 violations / 33 unconnected items. The candidate is rejected as a
route implementation: the proposed 1V1 collector still approaches U1.14,
XTAL_OUT, and SPICS, while the imported V7-style SPI corridors also conflict
with the staged crystal/RSET geometry. This is not an architecture or
placement rejection. The staged V4 rail/crystal/RSET baseline remains the
clean local baseline; the next distinct class is a native/reference-derived
QFN escape or a local U1/support relocation, not another collector jog.

The next distinct class is now a coherent local relocation discriminator.
`phase24_rtl9210b_support_relocation_v1.py` serializes away the old local
support copper, then moves U1, its crystal/RSET/decoupling support, and the
local PEDET/CLKREQ pull-ups by (+18,+18) mm. Native KiCad reports 9 findings /
45 opens: the findings are one intentionally dangling old RTL_1V1 trunk, an
isolated legacy zone, and non-production silkscreen overlaps; no signal
short/crossing is introduced by the placement change. This is placement-only
evidence and is not yet a routed or promotable support candidate. The next
route writer must regenerate the complete local support branch from the moved
native pads, with U2/C3-C5 destinations and the existing Path-A/production
CAD left untouched.

The (+18,+8) mm in-board relocation was then routed incrementally in
`PHASE24_RTL9210B_SUPPORT_RELOCATION_ROUTE_V2.kicad_pcb`. Native KiCad reports
4 findings / 32 opens, the same signal-clean baseline as staged V4; there are
no signal shorts or crossings. The saved-board native audit passes XTAL_IN,
XTAL_OUT, RSET, and all eight asserted RTL_1V1 endpoints. This closes only a
relocated local support sub-gate. Rails to C3/C5, SPI/control links to U2, and
the remaining RTL9210B support/bring-up checks remain open; no production CAD
or Path A artifact is changed.

The relocated rail slice `PHASE24_RTL9210B_SUPPORT_RELOCATION_RAILS_V1` now
connects U1.20 RTL_3V3 to C3.1 and U1.17 RTL_5V to C5.1 using separated
ordinary-via corridors and non-pad vias. Native KiCad reports 5 findings / 30
opens, with no signal shorts or crossings; saved-board endpoint checks pass
both rail pairs. The support branch is still incomplete: remaining rail-pad
parity, SPI/control links, and full Path-B mode/bring-up validation remain
open.

The additional U1 rail-pad escape probe
`PHASE24_RTL9210B_SUPPORT_RELOCATION_RAIL_PADS_V1` is rejected. It reduced
the native open count to 28 but introduced real RTL_3V3/RTL_5V and
RTL_1V1/RTL_5V shorts/clearances plus a B.Cu crossing. This is the second
failure of the ordinary-via additional-pad-fanout class; the next step must
change class to a native/reference escape arrangement or a further coherent
local support placement change. The clean rail baseline remains
`PHASE24_RTL9210B_SUPPORT_RELOCATION_RAILS_V1`.

The U2 co-location discriminator `PHASE24_RTL9210B_SUPPORT_RELOCATION_U2_V1`
moves the SPI flash destination into the relocated storage-local island.
Native KiCad reports 5 findings / 30 opens, matching the prior rail baseline,
with no new signal shorts or crossings. U2 SPI pads now form a local row at
approximately y=76 mm, materially reducing the source-to-destination span.
This is placement evidence only; SPI copper must still be regenerated from the
actual moved pads before the candidate can advance.

The isolated SPICS layer probe `PHASE24_RTL9210B_SPICS_LAYER_PROBE_V1`
confirms the current source-field barrier independently: native KiCad reports
11 violations / 29 opens for the near-transition variant, including a
SPICS/RTL_1V1 short and crossing at the 0.6/0.3-mm via beside U1.25. The
earlier far-transition form also failed. This is a QFN pad-field escape
implementation failure, not a U2 placement or Path-B architecture result;
the next trial must use a true pad-field dogbone/escape geometry.

The rotated-U1 SPI trial `PHASE24_RTL9210B_ROTATE_U1_SPI_V1` is rejected as
route implementation evidence. Native KiCad reports 38 violations / 39 opens:
the proposed left-side transition vias overlap at 0.4-mm source pitch, and
the B.Cu lanes cross retained XTAL/RSET corridors. The 180-degree placement
itself introduced no new placement short; a future attempt would need a
fully scrubbed rotated support baseline and a staggered source escape.

The first co-located SPI route trial
`PHASE24_RTL9210B_SUPPORT_RELOCATION_SPI_V1` is rejected as route
implementation evidence. Native KiCad reports 19 violations / 26 opens,
including source-pad crossings, rail/ SPI clearances, and an RTL_1V1/SPICS
short. The U2 co-location placement remains mechanically/native-clean at the
prior 5-findings / 30-opens baseline; the next SPI attempt must change layer
and escape ordering rather than repeat same-layer orthogonal routing.

The rail-cap co-location probe `PHASE24_RTL9210B_SUPPORT_RELOCATION_CAPS_V1`
then moved C3/C4/C5 coherently beside the relocated U1 and regenerated the
RTL_1V1 continuation to C4. Native KiCad reports 4 findings / 32 opens with
no signal shorts or crossings; a saved-board check confirms all nine asserted
U1/C4 RTL_1V1 endpoints are connected. This is now the preferred local
Path-B routing baseline. 3V3/5V, SPI/control, and remaining support checks
remain open; production CAD and Path A are unchanged.

The V11 crystal/support baseline was freshly rechecked with native KiCad:
6 violations and 25 unconnected items; XTAL_IN, XTAL_OUT, and the asserted
RTL_1V1 endpoints pass the saved-board connectivity audit, including its
negative control. The next implementation class is a coherent support-branch
relocation. Disposable candidate `PHASE24_RTL9210B_SUPPORT_BRANCH_RELOCATED_V1`
translates U2/C3/C4/C5/R2/R3 by 22 mm and scrubs only the affected serialized
tracks/vias before saving. Native DRC is 2 violations / 44 opens; the opens
are expected because the relocated branch is intentionally unrouted. This is
now a clean placement-only candidate, not a completion claim. Production CAD
and Path A remain unchanged.

The first reroute probe from the relocated pads,
`PHASE24_RTL9210B_SUPPORT_BRANCH_RELOCATED_SPI_V1`, is rejected as a route
implementation: native DRC reports 46 violations / 28 opens, dominated by
over-tight source-side SPI vias, corridor crossings, and U2 pad-field
interactions. It does not invalidate the relocation. The next route writer
will reuse the known-clean V6 source escape pattern and extend its corridors
to the relocated U2.

That V6-derived SPI extension is preserved as
`PHASE24_RTL9210B_SUPPORT_BRANCH_RELOCATED_SPI_V2`; native DRC reports 31
violations / 32 opens. It reduces the disconnected endpoint count but is
rejected for source-pad/corridor crossings and destination-side conflicts.
The failure is route implementation, not evidence against the 22 mm support
relocation. Further routing must separate the SPI and control corridors
before the remaining rail/support joins are attempted.

An outboard translation candidate was also tested: U2/support moved another
20 mm in X, with the same clean placement-only DRC baseline (11 violations /
37 opens). Its first extended SPI route is preserved as
`PHASE24_RTL9210B_SUPPORT_BRANCH_OUTBOARD_SPI_V3`; native DRC reports 40
violations / 33 opens. This is another route-implementation rejection, with
no evidence of a mechanical placement collision.

A further disposable V4 separated the SPI test from the inherited control
routes before routing. It still reports 32 native violations / 37 opens,
including source escape and lower-corridor conflicts, so it is rejected as
an implementation. The next pass must start from a truly SPI-scrubbed
placement candidate and use the native V6 escape geometry without retaining
any legacy SPI stubs.

The clean-V6-source reconstruction is preserved as
`PHASE24_RTL9210B_V6_SOURCE_OUTBOARD_SPI_V1`; native DRC reports 29
violations / 38 opens. It confirms the source geometry is recoverable, but
the destination lanes intersect inherited control corridors and the lower
SPISI branch. It is rejected as a complete route; the clean source escape is
retained as the next writer's oracle.

The isolated SPI-only lateral proof now passes its saved-board native endpoint
audit for all five SPI nets, including the required negative control after
serialized removal of SPICS copper. Its native DRC has 5 warnings / 45 opens;
the warnings are legacy dangling test branches, while the SPI route itself
has no short or crossing. U2 is translated 35 mm laterally to clear the J1
SSD-power field. This proves the V6 source escape plus a sufficiently
outboard destination can be electrically authored; the remaining work is
reintegrating rails, controls, crystal, flash support, and test access.

The rail-only lateral proof is now positive:
`PHASE24_RTL9210B_RAIL_ONLY_LATERAL_V1` has native DRC 0 violations and its
saved-board audit passes U1-to-C3/C4/C5 for RTL_3V3/RTL_1V1/RTL_5V. Removing
all serialized RTL_3V3 copper fails the negative control. This validates the
separated rail-spine geometry; U2 rail pads, control nets, and remaining
support circuitry are still open.

The RTL_3V3 extension to relocated U2 is now positive in
`PHASE24_RTL9210B_RAIL_ONLY_LATERAL_U2_V2`: native DRC reports 0 violations /
45 opens, and the saved-board audit proves U1.34/C3.1/U2.3/U2.8 connectivity.
This closes the local 3V3 support sub-gate only; 1V1/5V U2 support, controls,
crystal, flash support, and full integration remain open.

The full support placement candidate moves U2 35 mm and C3/C4/C5 20 mm
laterally. The proven SPI-only copper was transplanted by serialized
net-scoped block extraction into
`PHASE24_RTL9210B_FULL_LATERAL_SPI_INTEGRATED_V1`; its saved-board native
audit passes all five SPI endpoint pairs. Integrated native DRC is 17
violations / 40 opens; remaining findings are outside the SPI proof and this
candidate is not promoted until rails, controls, crystal, flash support, and
mechanical access are revalidated.

The combined lateral transplant,
`PHASE24_RTL9210B_FULL_LATERAL_SUPPORT_INTEGRATED_V2`, reports native DRC
18 violations / 34 opens. Its native audit passes all five SPI pairs plus
RTL_3V3 U1.34/C3.1/U2.3/U2.8 and the RTL_1V1/RTL_5V decoupler endpoints.
Remaining DRC and opens are control/crystal/flash/test-access work and are
not waived.

The V11 crystal routing is now transplanted into the combined candidate as
`PHASE24_RTL9210B_FULL_LATERAL_SUPPORT_CRYSTAL_V3`. Native DRC remains 19
violations but opens reduce from 34 to 30; a saved-board audit passes all
XTAL_IN/XTAL_OUT endpoints. The 19 DRC findings remain open and are not
waived.

Fixture-only TP1--TP8 were removed in the disposable V4/V5 candidates; this
reduces the report to 17 violations / 26 opens after removing one attached
test stub, but does not close any required RTL9210B support gate. The V5
combined native endpoint audit still passes SPI, crystal, and rail endpoints.
The remaining crossings, rail short/escape defects, QFN rail fanout opens,
and native manufacturing findings remain current and unwaived.

The V6 QFN rail-fanout probe is rejected as a production candidate. It
reduces native opens from 26 to 20 and preserves the combined endpoint audit,
but introduces 20 DRC violations including RTL_1V1/XTAL_OUT and
RTL_1V1/USB_TXP0 shorts. This is a route-implementation failure of the
attempted fanout geometry, not evidence against the RTL9210B support
architecture; V5 remains the clean baseline for the next independent rail
escape class.

The V7 RTL_1V1 perimeter-escape probe is also rejected. Replacing the prior
1V1 routes with a perimeter collector produced 31 DRC violations and 21
opens, including multiple new rail-to-rail shorts and edge-clearance errors.
The attempted perimeter path is therefore not a valid next baseline; V5 is
retained as the best combined candidate while a new, pad-field-aware escape
class is developed.

The V8 local RTL_1V1 F.Cu-zone probe is rejected as non-effective: native DRC
and opens remain 17 / 26, with no reduction in the missing QFN rail
connections. The zone did not establish the required pad-field continuity;
no validation rule was relaxed and V5 remains the baseline.

The V10 edge-normal QFN escape probe is rejected. It reduces the native open
count to 19 but produces 26 DRC violations, including XTAL_OUT, CLKREQ_N,
SPISO, GND, and RTL_5V conflicts plus a 0.0472-mm clearance. The result is
not promotable; V5 remains the current combined baseline and the next work
must use a native/reference-derived escape strategy.

The current V11 native escape-authority receipt is
`PHASE24_RTL9210B_QFN_ESCAPE_AUTHORITY_V11.md`. It records the loaded QFN
dimensions, interleaved pad ownership, exposed-pad geometry, current local
escape, and the explicit open authority boundary for the next fixture class.

The native source-authority RSET route from the separately validated oscillator
V7 fixture is now transplanted into V5 as
`PHASE24_RTL9210B_FULL_LATERAL_SUPPORT_CRYSTAL_V11_NATIVE_RSET`. Native DRC
improves to 16 violations / 25 opens; a saved-board native audit proves
U1.51/R1.1 and its serialized negative control fails as required. This closes
only the RSET local sub-gate; the full Path-B support gate remains open.

The isolated V1V1-native-fanout probe is rejected: after removing all prior
RTL_1V1 copper and rebuilding the fanout from the loaded QFN pad map, native
DRC reports 26 violations / 18 opens, including RTL_1V1 conflicts with GND,
RTL_3V3, XTAL_OUT, and existing corridor geometry. This independently
confirms that ordinary-via coordinate fanout is exhausted for this placement;
the next method must be a validated native/reference escape or a local
footprint/placement change within the disposable fixture.

The isolated `PHASE24_RTL9210B_1V1_PADFIELD_ISOLATION_V1` discriminator now
proves the complete RTL_1V1 fanout against the native U1 pad field and C4.1:
the saved-board audit passes all eight U1 rail pads plus C4.1. Native DRC is
1 violation / 37 opens, with the opens belonging to unrelated fixture
boundaries. This is positive evidence that V11 fails from neighboring-copper
integration congestion, not from an intrinsically impossible QFN escape.

The V12 combined transplant of the isolated 1V1 fanout is rejected as an
integration candidate. It reduces native opens to 18, but native DRC rises to
30 violations with CLKREQ_N, XTAL_OUT, RTL_3V3, RTL_5V, and clearance/crossing
conflicts. The isolated V1 fanout remains electrically valid; V11 remains the
combined baseline for support-corridor relocation rather than direct copper
transplant.

Staged V4 combines the audited full RTL_1V1 fanout with the proven crystal
and RSET routes while suppressing unrelated support copper. Native DRC is
4 findings: one existing C1 GND starved-thermal error and three isolated
GND-zone warnings; there are no signal crossings or shorts. The 32 opens are
unrelated PEDET/control/PCIe/fixture boundaries. V4 is therefore the current
local rail/crystal/RSET routing baseline, not a full-support pass.

Adding the previously audited lateral SPI copper to V4 was rejected as a
combined candidate: native DRC is 17 violations / 27 opens, with the main
new local defect being RTL_1V1 U1.25 via/track interaction with the SPICS and
SPISO QFN escapes. The V4 1V1+crystal+RSET baseline remains clean; this is a
QFN source-escape partitioning issue, not a rejection of the SPI topology.

The far-transition SPI source probe is rejected. Native DRC reports 32
violations, including SPICS/RTL_1V1 and adjacent SPI source-pad shorts plus
0.0403-mm clearances. Straight multi-net F.Cu escape at the current QFN
clearance contract is not viable; V4 remains the valid local baseline.

The QFN escape-map utility now inspects the latest integrated V11 saved board,
including the validated RSET transplant, instead of superseded V3/V5 fixture
states. `PHASE24_RTL9210B_QFN_ESCAPE_MAP_V5.txt` is retained as historical
V5 evidence; a V11 receipt is generated for current routing decisions.

The V9 pad-aware RTL_1V1 escape probe is rejected. Native DRC reports 32
violations / 22 opens, including new CLKREQ_N/RTL_1V1, RTL_3V3/RTL_1V1,
RTL_1V1/RTL_5V, and board-edge conflicts. The attempted serialized QFN
escape remains a route-implementation failure; V5 is retained and the next
class must use native/source-authority escape geometry rather than more
coordinate-only edits.

The rail layer rebalance is now verified: the rail-only/U2 branch returns to
native DRC 0 violations / 45 opens, and regenerating the combined candidate
reduces its native DRC to 18 violations / 34 opens with the combined endpoint
audit still passing. The improvement is limited to rail/SPI interaction; no
other subsystem has changed.

The next source-authority discriminator starts from V6 directly:
`PHASE24_RTL9210B_V6_LATERAL_SUPPORT_PLACEMENT_V2` moves only U2/C3/C4/C5
20 mm laterally and reports 8 violations / 43 opens before new copper. Its
SPI extension, `PHASE24_RTL9210B_V6_LATERAL_SPI_V3`, reports 22 violations /
38 opens and is rejected for destination/corridor implementation conflicts.
This separates the clean QFN escape from the still-unproven destination
fanout; no production CAD has changed.

The original isolated RTL9210B-CG bring-up fixture remains archived at
`PHASE24_RTL9210B_BRINGUP_FIXTURE.kicad_pcb`. It captures the corrected
QFN-68/M-key lane mapping, PEDET/sideband ownership, support-net boundary,
SPI/reset/UART test access, and SSD-power nets without changing production
CAD. Its authority audit and saved-track-independent negative control pass;
native DRC reports zero violations and 56 explicit unrouted items. That count
belongs to the original unrouted bring-up baseline; it is superseded for
current routing by the later SPI V7 plus GND-plane candidate below. The 56
opens remain historical evidence, not a current count or waived production
finding. Path B remains isolated and `CONTINUE BOTH`.

Two disposable support-route attempts are preserved in
`PHASE24_RTL9210B_SUPPORT_ROUTE_EXPERIMENTS_20260907.md`. The first all-F.Cu
fanout failed with crossings, shorts, undersized tracks, and solder-mask
bridges. The second ordered SPI B.Cu attempt eliminated that fanout class but
failed ordinary-via fabrication rules, clearances, and two shorts. Both are
route implementation failures; the next attempt must use the ordinary-via
basis and a larger pad-field escape.

Native KiCad inspection then found a fixture serialization defect: the layer
table declared inner layers as `power` and ordered `B.Cu` before the inner
layers, so numeric layer 2 loaded as `In4.GND`. The generator now matches the
native six-layer `signal` form and ordering. A support-local V2 placement
moved the crystal/RSET/flash/support parts coherently; its baseline is DRC
clean. The first native-coordinate oscillator/RSET route is still rejected at
4 violations / 52 opens from three local crossings and one RSET/XTAL
 interaction, with no via, drill, or track-width violations.

Two additional oscillator-route trials were preserved and rejected: V3 has
4 native DRC violations / 52 opens (two shorts, one crossing, one mask
bridge), while V4 regresses to 5 violations / 52 opens (two shorts and three
mask bridges). This remains a Path-B route-implementation gate. The V2
support-local placement and corrected native layer serialization remain the
current baseline; production CAD is unchanged.

The V7 oscillator/RSET route is the first clean local Path-B routing result:
native DRC reports 0 violations / 52 unconnected items, and its independent
saved-track audit passes. This closes only the oscillator/RSET local route
sub-gate. The rest of the support fixture remains unrouted and Path B remains
isolated with `CONTINUE BOTH`.

SPI V7 is the second clean local Path-B routing sub-gate: native DRC reports
0 violations / 52 unconnected items and the independent saved-track/net/via
audit passes. Earlier SPI variants remain preserved as route-development
evidence. The full RTL9210B fixture is still open for the remaining support
circuits and complete connectivity.

The current isolated Path-B routing baseline is
`PHASE24_RTL9210B_SPI_V7_GND_PLANES_V3.kicad_pcb`: native DRC is 0 and the
GND-plane/reference discriminator reduces the fixture to 45 unconnected
items. Those remaining opens are not waived; they are the next support,
power, sideband, and test-access routing gate. Production CAD remains
unchanged.

The RTL_3V3 support bus is now a clean local sub-gate in
`PHASE24_RTL9210B_3V3_SUPPORT.kicad_pcb`: U2 pins 3/8, C3, and the R2/R3
3V3 returns are saved on the actual named net, the independent audit passes,
and native DRC after zone refill reports 0 violations / 41 remaining opens.
The initial pre-refill clearance findings were rejected as stale zone-fill
state and are not used as current evidence.

The RTL_5V/C5 and RTL_1V1/C4 local support route now passes as V6:
`PHASE24_RTL9210B_5V_1V1_SUPPORT_V6.kicad_pcb` has native DRC 0 violations
after refill and leaves 39 unconnected items. V1–V5 are retained as rejected
route-method evidence; no production CAD changed.

The corrected separate RESET_N/PERST_N route passes its endpoint audit and
native DRC with 37 remaining opens. The first combined PEDET/CLKREQ trial is
rejected at 8 DRC violations / 33 opens due to same-layer corridor crossings,
two control-to-power interactions, and a J1 via clearance issue; it is not
used as current fixture evidence. Follow-up V2/V3/V4/V5/V6 control routes
remain rejected at 3/33, 5/33, 8/34, 3/34, and 4/33 respectively. The
relocated R2/R3 placement is retained as a valid disposable placement
experiment, but its V1/V2/V3 perimeter route candidates are also rejected at
6/34, 8/35, and 10/35 native DRC violations/unconnected-item counts. Their
failures are route-implementation/placement-corridor evidence, not a Path-B
architecture rejection. The clean RESET_N/PERST_N candidate remains the
current control baseline; PEDET/CLKREQ is the next open Path-B gate.

The subsequent coherent four-control regeneration trials are preserved as
V4/V5/V6/V7/V8. They report 16/34, 6/35, 3/36, 15/32, and 4/35 native
DRC-violation/unconnected-item counts respectively. V5 fixed the QFN-edge
diagonal-departure defect; V6 is the current disposable baseline with one
remaining RTL_5V/PEDET transition short. V7 proved that moving the inherited
RTL_5V transition through the QFN-side escape is the wrong class, and V8
showed that a PEDET-only B.Cu dogleg still conflicts with the local
3V3/RTL_5V transition field. None is promoted and none changes production
CAD or rejects the RTL9210B architecture.

V9 retained the V6 rail/control baseline and added a PEDET F.Cu dogleg around
the RTL_5V via; native DRC still reports 3 violations / 36 opens because the
dogleg intersects the inherited RTL_5V vertical. This closes the current
same-placement route class for evidence purposes. The next experiment must
relocate or coherently re-author the small RTL_5V/3V3/control support island;
additional coordinate-only PEDET detours are not promoted.

The corrected lower-left placement experiment was generated from native
footprint-local offsets: R2 pad 1 is `(69,78)` and R3 pad 1 is `(72,78)`.
Its first regenerated control/3V3 route reports 9 native DRC violations / 33
opens, including lower-corridor crossings, a GND-via collision, and one
QFN-edge departure clearance. The earlier lower baseline had a coordinate
frame error and is superseded by this corrected placement evidence. The
lower placement remains disposable and unpromoted; V6 remains the best
current route baseline.

Lower V3 re-authored the corrected lower placement with PEDET y=68,
CLKREQ y=74, PERST y=72, RESET on a separate bottom path, and an early C3
3V3 transition. Native DRC reports 10 violations / 33 opens, including
SPI/3V3 interference, lower control crossings, and a GND-via collision. It
is rejected as a route implementation; no placement or architecture is
promoted from this candidate.

V10 attempted a QFN-safe RTL_5V departure from U1 pad 17 while preserving
V6 controls and 3V3. Native DRC regressed to 14 violations / 35 opens from
RTL_1V1/RTL_5V crossings, PERST-via collisions, and an incomplete rail join.
It is rejected; moving only the rail departure is insufficient. The next
workstream may proceed independently while the Path-B support island remains
isolated.

Further control variants V4/V5/V6 were also rejected: V4 reports 8 DRC
violations / 34 opens, V5 reports 3 / 34, and V6 reports 4 / 33. Their
remaining findings are same-layer PEDET/CLKREQ/rail corridor crossings. This
coordinate-only B.Cu class is exhausted for now; the next control method must
separate the source/endpoint departures by layer rather than tune the same
parallel channels.

## Current live correction — 2026-09-06

The old V4 SATA claim is superseded for Path-A topology: its C30–C33 to J3
route bypassed U13 even though its old audit passed. The live source authority
now labels C30–C33 selector-side pins as `TUSB_SATA_*` and maps U13 A1 to the
shared M.2 SATA-B/PCIe-RX0 pair. A regenerated selector-inclusive disposable
route passes all twelve native endpoint assertions and its saved-track
negative control, but its first copper author still has real local DRC
crossings/shorts. Current gate is `ROUTE IMPLEMENTATION OPEN`; do not use the
old V4 receipt as evidence of a closed SATA selector path. Full-board and
combined USB3/SATA closure remain open.

A TX-only thermal-clear V4 was tested from the V3 saved board. It removes the
two original U13 thermal-pad shorts, but native DRC regresses to 136 findings
/ 52 opens with TXP/TXN launch-via spacing conflicts and inherited corridor
crossings. It is rejected as a route implementation; selector authority and
the U13 thermal-pad assignment remain unchanged.

An isolated U13-to-J3 lane-0 fixture was then generated with no inherited
selector/bridge copper. Its ordered split-corridor launch reports 84 native
DRC violations / 32 opens, including M.2 mounting-hole/ground interactions
and connector-side target-via conflicts. It is rejected as a launch
implementation; the remaining issue is connector-side mechanical/via
placement, not U13 selector pin authority.

See `PHASE24_PATHA_SATA_SELECTOR_CORRECTION_20260906.md` for the exact TI
pin/port basis and raw selector-inclusive fixture names.

The corrected PCB generator also assigns U13's exposed thermal pad 43 to
`POWER_GND`, as required by the TI RUA0042A package drawing. This converts the
former no-net pad artifact into a real routing constraint; the next disposable
route must clear that pad rather than crossing it.

The current regenerated V3 selector fixture does clear the source/net
authority issue and passes all twelve native endpoint assertions, but native
DRC remains open at 133 findings / 52 opens, including two real shorts and ten
crossings. The two shorts are localized to the U13 thermal-pad TXN corridor
and an M.2 final launch interaction. See
`PHASE24_PATHA_SATA_SELECTOR_ROUTE_V3_20260907.md`; this is route
implementation evidence, not a production-board pass.

The rotated U13 V3 follow-up is also rejected: its native endpoint audit
passes, but the saved report regresses to 204 findings / 52 opens with six
shorts and twelve crossings, versus 138 / 52 with six shorts and eleven
crossings for V2. This is a local launch/corridor implementation failure;
the rotated placement class remains unpromoted and Path A source authority
is unchanged.

A bounded U13 180-degree orientation experiment is also preserved in
`PHASE24_PATHA_SATA_SELECTOR_ROT180_20260907.md`. It improved the physical
Port-B/Port-A direction but its first via author failed at 180 findings / 52
opens with 23 shorts and 5 crossings. It is rejected for local via/escape
geometry, not for architecture; V3 remains the current route baseline.

## Current checkpoint — 2026-09-06

Latest focused routing-generator checkpoint: `5184b6f`. The deduplication
experiment recorded in `PHASE24_PATHA_SATA_ROUTER_DEDUP_20260906.md` is
rejected as route implementation failure; no integrated board was changed.

The next live finding is a source/net-authority correction recorded in
`PHASE24_PATHA_SATA_CONTACT_AUTHORITY_20260906.md`: the SATA router and audit
now use J3 contacts 49/47/43/41, and the child schematic coupling-cap outputs
were reconciled to the connector's canonical M.2 net names. Source audits pass;
native routed-board closure remains open. The hard-obstacle search was bounded
after it failed to produce a candidate, and no integrated board was changed.

The source-to-PCB SATA net-authority derivation and bounded-search result are
captured in `PHASE24_PATHA_SATA_REGEN_SEARCH_20260906.md`; the source mapping
passes native inspection, while routed-board closure remains open.

The follow-on local-corridor discriminator is recorded in
`PHASE24_PATHA_SATA_LOCAL_CORRIDOR_20260906.md`: source net ownership passes,
but the current unconstrained A* implementation cannot emit a local route.
This remains a route-method failure, not a storage-architecture rejection.

The subsequent canonical native corridor trial is recorded in
`PHASE24_PATHA_SATA_CORRIDOR_CANONICAL_20260906.md`. It derives U7 starts and
rotated J3 launch coordinates from native pads, and its assertion-only audit
passes all eight SATA endpoint pairs. Follow-up native-pad-derived fanout and
pair-layer trials remain rejected by native DRC (67 then 66 findings), with
the latest failure being shared-corridor crossings and inherited fixture
opens. This is an open route-implementation experiment, not a Phase 24 or
Path-A closure.

A minimal U7/C30–C33/J3 fixture then reduced the native DRC result to 59
findings while retaining the eight-endpoint audit PASS. This removes unrelated
board obstacles and confirms the remaining defect class is local escape and
pair ordering around the bridge/capacitor row. The raw report is
`PHASE24_PATHA_MINIMAL_SATA_CORRIDOR_20260906-drc.rpt`; no production route
was promoted.

The current best disposable candidate is the source-order-preserving
`PHASE24_PATHA_MINIMAL_SATA_CORRIDOR_MONO2_20260906.kicad_pcb`. Its native
endpoint audit passes all eight SATA pairs and native DRC reports 12 findings.
Only the TX source dogbone, one socket launch clearance, U7 footprint
clearances, and silkscreen fixture findings remain; no production storage
route has been promoted.

The subsequent explicit native-rule probe is recorded in
`PHASE24_U7_RULE_BASIS_PROBE_20260906.md`. It sets the disposable board's
global and default-netclass clearance to 0.15 mm, matching the documented
JLC multilayer capability, then reruns native DRC without severity changes or
exclusions. Findings reduce from 12 to 7: the four U7/socket clearance
findings disappear, while two real shorts and one real crossing remain, plus
the intentionally incomplete fixture's 38 opens. This is rule-basis
evidence, not a route PASS or an integrated-board rule change.

Two follow-on native pad-derived escape variants are preserved in
`PHASE24_PATHA_SATA_ESCAPE_REPAIR_REJECTED_20260906.md`. They are both
`ROUTE_IMPLEMENTATION_FAILURE`: the first produced 22 DRC findings and the
second 23, including new crossings/shorts in the U7 oscillator, power, and
adjacent RX escape field. The corridor author was restored to the committed
mono2 baseline; no architecture, production CAD, or integrated board changed.

The next coordinated V4 escape is now the best disposable topology. Its
native endpoint audit passes all eight SATA pairs and native DRC reports zero
shorts/crossings (10 findings on the 0.20 mm basis; six clearance and four
silkscreen). Under the explicit 0.15 mm disposable basis only the four
silkscreen findings remain, alongside 38 intentional fixture opens. The same
author applied to the source-regenerated integrated candidate preserves the
eight endpoint assertions but leaves full-board DRC at 1,210 findings / 499
unconnected items, so it is not promoted to clean-board authority.

The SATA route author now has a native guard against stale support-routed
ancestors: direct use of the older board fails on `C31.1`'s superseded
`/STORAGE/SATA_M2_TX_N` net and points to the source-derived net-authority
regeneration step. The canonical regenerated ancestor routes successfully.

The V4 native connectivity negative control also passes: removing one actual
saved SATA track disconnects C30.1 -> J3.49. This confirms the focused audit
uses saved pads/tracks/vias rather than synthetic expected edges.

The combined dual-mode storage high-speed fixture is recorded in
`PHASE24_DUAL_MODE_STORAGE_HS_FIXTURE_20260906.md`. Its single saved board
passes all ten USB3 and all eight SATA native endpoint audits, but native DRC
reports 576 findings / 187 unconnected items, including real USB3/SATA
crossings and shorts. It is therefore a route/placement discriminator only;
the dual-mode source architecture remains open and unaltered.

## Current Path-B qualification checkpoint — 2026-09-06

The isolated RTL9210B-CG candidate now has explicit authority and mode
matrices in `authority-inventory/rtl9210b/RTL9210B_PATHB_AUTHORITY.md` and
`RTL9210B_PATHB_MODE_MATRIX.md`. These are derived from the retained Rev. 1.1
technical document, native corroborating netlists, corrected M-key contact
mapping, and the locally recreated SMD QFN-68 footprint. They do not authorize
production replacement of Path A.

Current decision remains `CONTINUE BOTH`: Path B reduces the bridge/switch
count and can use native PEDET selection, while virgin-chip programming,
firmware provenance/rights, authorized application-circuit values, SSD power
budget, and hardware mode bring-up remain open. The rejected straight-line
RTL9210B fixture is route-implementation evidence only. Path A remains
preserved and Phase 24 closure is still open.

Latest private storage evidence checkpoint: `9e45a72`. The retained WIP
RTL9210B native XML support netlist now has a reproducible audit with
component, rail, clock, SPI, reset, RSET, PEDET, ISOLATEB, shared-lane, and
unused-pin assertions. Component-identity and PEDET-net mutation negative
controls both fail as intended. This is corroborating evidence only; no
production Path-B CAD was promoted and Path A remains intact. Open gates are
still the authorized/current application circuit, M-key sideband ownership,
released land pattern, SSD power/inrush/thermal budget, and traceable virgin
firmware/configuration programming.

The M-key lane-role review corrected the earlier ambiguous SATA labels: RTL
TX 68/67 goes to physical contacts 49/47 (platform PET, SATA-A), and RTL RX
64/65 returns from 43/41 (platform PER, SATA-B). The retained WIP root XML
reverses those associations, so it is explicitly negative corroboration and
must not seed Path-B CAD.

The rejected RTL9210B straight-line PCB fixture remains a
`ROUTE_IMPLEMENTATION_FAILURE`, not an architecture rejection. The next
bounded Path-B step is to close those evidence gates or author the standalone
bring-up fixture only after they are sufficiently documented. Unrelated whole-
board Phase 24 routing remains paused per the active storage amendment.

Fresh Path-A focused audit receipt: `PHASE24_PATHA_FOCUSED_AUDIT_20260906.md`.
The live schematic, library, mode-contract, and JMS583-support audits pass;
native DRC of the support-routed partial candidate reports 1,160 violations
and 499 unconnected items. Path A is therefore authoritative at source level
but remains open at PCB routing/native closure level.

## Active steering amendment — RTL9210B Path B

The dual-mode storage upgrade is still the active Phase 24 work item. Path A
(`CM5 USB -> HD3SS6126 -> TUSB9261/JMS583 -> HD3SS3412 -> M-key`) remains
preserved as the fallback/reference. Path B is now an isolated, serious
qualification candidate: `CM5 USB -> RTL9210B-CG -> one M-key socket`.

Path B evidence and its current gates are authoritative in
`PHASE24_RTL9210B_QUALIFICATION.md` and
`authority-inventory/rtl9210b/README.md`. The retained Rev. 1.1 technical
document establishes PEDET SATA/PCIe auto-selection, shared lane-0 pins,
USB2/USB3, SPI flash, clock, reset, PCIe sidebands, and power interfaces.
This does not yet authorize production replacement: exact current application
support, land-pattern release authority, virgin-chip programming, firmware
provenance/rights, and hardware mode bring-up remain open.

The previous SATA-only contract in the historical approved-plan assumptions
is superseded for this active storage-island qualification by the explicit
dual-mode steering. No whole-board floorplan or unrelated Phase 24 work may
resume until Path A is closed or the Path-B comparison reaches its defined
decision experiment.

## Current priority — dual-mode storage upgrade

Phase 24 routing experiments are paused at the user's direction. The active
work item is the storage-island upgrade, not further clock/SATA/USB3 repair.
JMS583-QHFA3A is the preferred NVMe candidate after bounded substitution
research; its factory mask-ROM baseline is now design-authorized, while
authorized prototype supply remains open. TE 1-2199230-4 is the preferred
M-key socket candidate; exact customer CAD/pad parity remains open. Resume
the preserved Phase 24 checkpoint only after the one-socket dual-mode island
is implemented and its mode-aware/native validation passes.

## Live storage-upgrade work — 2026-09-06

The dual-mode storage implementation remains the active task; unrelated Phase
24 routing is still paused. The authoritative child schematic now includes
the TE `1-2199230-4` M-key socket, retained TI TUSB9261 SATA bridge, JMS583
`QHFA3A`, TI HD3SS6126/HD3SS3412 selectors, a three-position power-off mode
override (`J5`: FORCE_SATA / AUTO_PEDET / FORCE_NVME), and U14
SN74LVC1G17DBVR buffering `MODE_IN` to `STORAGE_SEL`. JMS583 Rev 2.1 required
support is explicit: 25-MHz crystal, 12-kOhm REXT, 4.7-uH LXO inductor,
AVDD33/rail decoupling, reset RC, VBUS divider, and USB/PCIe TX coupling.

Evidence checkpoint: `phase24_dual_mode_storage_mode_audit.py` and
`phase24_jms583_support_audit.py` pass; native schematic netlist export exits
zero. Native ERC reports 407 findings and is not a pass. The disposable PCB
placement fixture loads natively and reports 1,069 violations / 499
unconnected items because it is not routed; it is not a pass. Remaining work
is to complete authoritative support footprints/placement, author a routed
mode-aware fixture with forced SATA/NVMe/AUTO/empty/reset/inactive-state
checks, reconcile native ERC/DRC and TE mechanical parity, then integrate.
JMS583 baseline firmware remains factory mask-ROM; prototype procurement is
still HIGH risk because the exact JLC listing is currently out of stock and
no verified major-distributor listing is retained.

The storage support reference namespace was corrected after native inspection:
the integrated ancestor already owns low-numbered C/R references, so JMS583
support now uses `C80–C93`, `R80–R83`, `L10`, and `Y10`. The regenerated native
candidate contains distinct SERVICE `J4`, storage mode `J5`, and all support
references. A disposable native low-speed support route pass saves 14
pad-to-pad connections; its DRC remains open at 1,158 violations / 499
unconnected items and is not promoted.

## Superseded historical dual-mode checkpoint — 2026-09-06

Latest private checkpoint: `7938f64` (`reva-clean`). The active storage
candidate is `JMS583-QHFA3A` plus retained `TUSB9261IPVP`, TI
`HD3SS6126RUAR`/`HD3SS3412RUAR`, TE `1-2199230-4`, and U14
`SN74LVC1G17DBVR`, all inside the storage island. JMS583 pin authority and
M-key contact 69 PEDET/CONFIG1 are corrected and structural audits pass.

The candidate was not release-ready at that checkpoint: native schematic ERC
reported 322 findings at full severity (13 errors on the child alone,
including inherited root hierarchy/dangling-label issues), and the native PCB
placement fixture remained unrouted with 1,013 DRC violations and 499
unconnected items. The former next action was to instantiate the
three-position SATA/AUTO/NVMe override and documented JMS583 support network.
That work is now superseded by the live state at the top of this document:
the support network is instantiated and audited; mode-aware routing and
release validation remain open. Phase 24 whole-board work remains paused.

## Authorized storage-island upgrade checkpoint — 2026-09-06

The Phase 24 route-development work was safely checkpointed at HEAD
`68aac08` before the authorized SATA/NVMe storage-island upgrade. The selected
`SWAP_ETH_STORAGE` macro, CM5 source topology, PCIe/Ethernet/SERVICE anchors,
and all rejected routing evidence remain preserved. The upgrade qualification
retains TI `TUSB9261IPVP` as the SATA bridge and qualifies the TI selector
families for design review, but does not yet authorize a schematic/PCB edit:
the ASM2362 NVMe bridge lacks a public exact pin/land-pattern, reference
circuit, firmware/configuration, programming, and traceable procurement
package. The existing J3 is B-key-only; JAE's M-key family direction is
recorded but its exact released drawing must still be captured and compared.
See `PHASE24_STORAGE_UPGRADE_CHECKPOINT_20260906.md`,
`PHASE24_STORAGE_UPGRADE_QUALIFICATION.md`, and
`PHASE24_STORAGE_UPGRADE_BLOCKER.md`. `PHASE24` remains `OPEN`.

## Mixed-layer regenerated clock-support milestone

`PHASE24_CLOCK_LAYERESC_XI_p5_1p0.kicad_pcb` is superseded by
`PHASE24_CLOCK_LAYERESC_DIRECT_XO.kicad_pcb`, generated from actual V26 pad
and net objects with XI/VSSOSC on B.Cu and XO on F.Cu. Native DRC reports 11
warnings only (silkscreen/text), 70 unrelated board opens, and zero
`shorting_items`, `tracks_crossing`, clearance, dangling-via, or dangling-
track classes. The strengthened native audit passes U7.52/U7.53/U7.54 plus
all Y1/R23/C42/C43 clock endpoints. This is promoted as the clock-support
milestone, not full Phase 24 closure: bridge rails, reset/configuration,
grounds/returns, and the remaining board-wide opens are still gated.

## Clock net-order permutation discriminator

The fresh common-region generator was run from clean copies under all six
XI/XO/VSSOSC tree-order permutations. None completed all three trees; each
failed at a different shared crystal/passive target. This exhausts net-order
selection for the current island placement without relaxing native DRC. No
candidate was promoted and the V26 SATA/USB3/PCIe copper remains unchanged.

## Reduced-envelope coordinated clock search

The common-region generator was rerun with actual pad envelopes plus a small
raster guard and ordinary through-via exits. It still authored complete XI
and XO trees but could not reach the VSSOSC tree after those two nets occupied
the shared B.Cu channel. The candidate was not emitted or promoted; native
DRC remains the acceptance authority. This rules out oversized pad boxes as
the sole cause and localizes the remaining repair to coordinated multi-net
channel allocation around the crystal field.

## Fresh common-region clock regeneration attempt

The new pad/net-derived generator placed a coherent clock island in the
measured open region. Its sequential obstacle search can author complete XI
and XO branches, but the remaining VSSOSC branch becomes unreachable when
the other two valid branches occupy their shared B.Cu channel. No candidate
was promoted and no V26 SATA/USB3 or PCIe copper changed. This is a
`ROUTE_IMPLEMENTATION_FAILURE` of sequential channel assignment; the next
step is coordinated multi-net escape planning using the native-valid clock
fixture as the topology oracle.

## Regenerated common-region clock search

The fresh common-region generator placed Y1/R23/C42/C43 as one coherent
island and derived all pad/net identity from the V26 board. Its native A*
search successfully authored complete XI and XO route trees before the third
VSSOSC tree became unreachable through the reserved/occupied B.Cu corridor.
The candidate was not emitted or promoted. This is a partial
`ROUTE_IMPLEMENTATION_FAILURE`: it validates the new island placement and
local net-authoring path, while identifying simultaneous three-net channel
assignment as the remaining issue. No SATA, USB3, PCIe, or schematic
authority changed.

## Reachable-region clock migration attempt

The measured common B.Cu region was exercised by translating the complete
clock island and invoking the native obstacle search for its U7 launches.
The translated support geometry itself did not introduce a new source-level
short, but the inherited clock-tail endpoint was blocked before the first
launch could reach it. This candidate is rejected as stale-tail geometry;
the next implementation must regenerate the passive-to-U7 paths from actual
pad locations rather than translate those tails. V26 SATA/USB3 and PCIe
remain unchanged.

## Common-region reachability discriminator

An actual-board reachability scan was run from ordinary via-exit points near
U7.52/.53/.54, using net-aware obstacles on B.Cu. All three clock nets share
a large reachable region; the earlier launch failures are therefore caused
by the chosen passive-island endpoint corridor and its reserved paths, not by
an inherently disconnected U7 escape. The next candidate should place the
complete passive island inside that common region and terminate each launch
with a local endpoint via before any detailed support routing is attempted.

## Coordinated-layer clock oracle placement basis

`PHASE24_CLOCK_COORDINATED_LAYERS.kicad_pcb` was identified as the strongest
native clock source: its XI/XO/VSSOSC graph is complete and native DRC has no
shorting or crossing classes, with only eight unrelated U7 opens. A bounded
transform using the actual V26 U7 frame, preserving fixture pad layer sets,
and placing the passive island west/south produced
`PHASE24_COORD_CLOCK_XM10_Y35_NO_LAUNCH.kicad_pcb`. Native DRC reports 14
violations consisting of three deliberate U7 launch tails and inherited
silkscreen warnings; there are no shorting, crossing, clearance, dangling-via,
or footprint classes. The candidate is not promoted until the three U7
launches and remaining support rails are connected.

## Clock source-oracle regression confirmation

`test_phase24_clock_fixture_v2.py` was rerun through native KiCad Python and
returned `Phase24 complete clock fixture V2: PASS`. All XI/XO/VSSOSC passive
endpoints remain natively connected and the source report has no clock
shorting or crossing classes. The unresolved Phase 24 defect is therefore
strictly the V26 transplant/launch integration; the source clock topology is
not under dispute.

## Coherent clock-island relocation search (rejected)

The complete V2 passive clock island was translated 20 mm west and 10 mm
south as a coherent block, preserving its native pad-layer topology. An
actual-board obstacle search was then used for the three U7 launches. The
first B.Cu launch could be explored, but no legal non-overlapping path was
found for the second B.Cu clock leg to its relocated tail. This candidate is
rejected as a route-implementation/corridor-capacity failure; no production
copper, PCIe routing, or V26 SATA/USB3 data routing changed.

## Layer-aware U7 clock launch search (rejected)

The actual saved-board obstacle search was rerun with the V2 layer split:
XI/XO on B.Cu and VSSOSC on F.Cu. It found an XI path but no legal VSSOSC
path in the inherited U7-to-clock-island corridor, even after expanding the
search window. No copper was promoted. This is a `ROUTE_IMPLEMENTATION_FAILURE`
localized to the launch corridor; the native-valid passive clock graph and
V26 SATA/USB3 routes remain preserved.

## Whole-board floorplan comparison and SATA route discrimination — 2026-09-06

## Clock launch obstacle-aware search (rejected)

The first obstacle-aware B.Cu search from the actual U7.52/.53/.54 pads to
the south-40 V2 fixture launch tails found a route for XI but no legal
non-overlapping path for the next VSSOSC leg within the local corridor. No
candidate was promoted. This rejects the all-B.Cu launch class as a capacity
problem; it does not reject the V2 clock topology or the V26 data route. A
layer-aware trial remains the next implementation class, preserving V2's
XI/XO B.Cu and VSSOSC F.Cu division.

The required whole-board macro-floorplan review was rerun through the
installed KiCad 10.0.5 native Python environment from the byte-verified live
basis `PHASE24_U7_3V3_CURRENT_LOCAL.kicad_pcb`. Five disposable candidates
were generated from native-transformed pad/body geometry. The comparison
uses source-to-island distance, same-net ratsnest, body overlap, connector
appropriateness, and corridor topology; it deliberately does not use the
mature historical board's accumulated DRC/open count.

`SWAP_ETH_STORAGE` remains selected. It reduces Ethernet source distance from
59.2 mm to 22.5 mm and storage from 65.9 mm to 49.5 mm, has zero coarse
major-body overlaps, and preserves the PCIe, SERVICE, power-entry, and
regulator anchors. `ETH_LOCAL_STORAGE_MID` is shorter but introduces four
body overlaps; the south/north exchange introduces two. The integrated
candidate is unchanged and the selected board remains disposable.

The SATA route authoring received a new separated-lane cycle. V7 removed the
old direct run through the M.2 field but still had a native U7 launch short,
an M.2 no-net-field short, and a crossing. V8 transitions beside each
coupling capacitor and stays on B.Cu through the connector field; native DRC
then exposed a B.Cu corridor crossing and two RX bridge vias with only 0.1 mm
hole clearance. Both are rejected as `ROUTE IMPLEMENTATION FAILURE`. These
results do not reject the selected macro floorplan; the next SATA cycle must
use a source-ordered connector launch with separated RX vias and no crossing
horizontal/vertical B.Cu corridors.

Consultant dispatch was attempted for the required independent review and was
unavailable because the orchestration service reported a thread-limit error.
The review was therefore completed locally from native-loaded objects; this
tooling availability issue is not treated as an engineering blocker.

## Native pad-layer correction and Ethernet V3 — 2026-09-05

The independent geometry review identified a real authoring assumption error:
the saved J7 Ethernet signal pads are F.Cu-only despite the footprint header
being on B.Cu. `phase24_route_corrected_ethernet_mdi.py` now derives every
source, ESD, and connector layer from the native pad layer set; it does not
hard-code J7 to B.Cu. The same review also identified a separate clock
footprint-side authority issue (U7 clock pads F.Cu versus B.Cu-only clock
passive pads), which remains gated before clock routing.

The corrected V3 Ethernet candidate completes all eight pair authoring paths,
but native DRC rejects it with 827 violations and 431 unconnected items,
including genuine pair-to-pair and pair-to-ground shorts plus via-dangling
findings. It is preserved as `ROUTE IMPLEMENTATION FAILURE`; no severity or
layer contract was relaxed. The next Ethernet class must use explicit
non-crossing reference corridors/rip-up around the J2 field. Phase 24 remains
open.

## Layered Ethernet escape V2 — 2026-09-05

The multipair layered search was rerun after fixing two authoring defects:
endpoint pads remain obstacles, and same-net vias are deduplicated. The
complete eight-pair candidate is reproducible as
`PHASE24_CORRECTED_ETHERNET_LAYERED_ESCAPE_V2.kicad_pcb`; native DRC reports
875 violations and 440 unconnected items, with real differential-pair
shorting records remaining. It is rejected. The result is useful evidence
that the current generic sequential A* escape still weaves pair lanes in the
dense CM5/ESD/MagJack geometry; it is not evidence against the corrected
macro floorplan. No validation severity or connectivity assertion was
relaxed, and no rejected copper was promoted.

The next implementation class is a reference-topology-preserving multipair
escape with explicit non-crossing pair corridors and controlled rip-up, rather
than another unconstrained sequential search. Phase 24 remains open.

## Ethernet launch-orientation experiment — 2026-09-05

The corrected-basis router was run against disposable J2 rotations 90 and 270
(`PHASE24_ETH_J2_ROT90_PLACEMENT.kicad_pcb` and
`PHASE24_ETH_J2_ROT270_PLACEMENT.kicad_pcb`). Both failed before saving a
complete route: the native-pad search could not find the second-stage
ESD-to-MagJack path after the first pair set occupied the local corridors.
This is a repeated `ROUTE IMPLEMENTATION FAILURE` in the current sequential
search/escape model, not a floorplan comparison and not permission to relax
pad clearance. The next class will use explicit alternating launch layers
and a pad-field-aware multi-pair escape/rip-up order on the same corrected
placement.

## Corrected-basis Ethernet routing development — 2026-09-05

The first complete eight-pair search candidate from
`phase24_route_corrected_ethernet_mdi.py` is rejected. Its native DRC report
(`PHASE24_CORRECTED_ETHERNET_MDI_ROUTE-drc.rpt`) found 925 violations and 438
unconnected items, including real MDI-to-CT/LED/GND pad-field shorts. The
initial false completion was caused by exempting all pads in endpoint
footprints; the generator now models only the active source/target as a
terminal and preserves every other endpoint pad as a copper obstacle.

With that correction, the same routing class fails to find a legal path for
the next pair after the first four pairs are placed. This is a
`ROUTE IMPLEMENTATION FAILURE`, not a macro-placement verdict: the search
model is conservative around the dense MagJack field and needs an explicit
connector-orientation/escape topology. No severity was changed, no crossing
was waived, and no rejected copper was promoted. The next experiment will
retain the corrected macro basis and test the connector launch orientation
and native pad-field escape before any full-board claim.

## Corrected macro basis native screen — 2026-09-05

`PHASE24_CORRECTED_MACRO_PLACEMENT.kicad_pcb` is the current disposable
coherent-neighborhood basis, generated by
`phase24_apply_corrected_macro.py` from the live integrated candidate. It
moves Ethernet J2/U6/U9 and the complete storage group U7/J3/C16/C17/C19,
C30–C33, and clock support together, and removes only affected saved copper.
The native DRC screen reports 267 total violations and 454 unconnected items;
its three courtyard overlaps are inherited C5/C6, C7/C8, and J7/C14. No new
moved-island courtyard overlap is present. This is placement/routing-basis
evidence, not a routed-board pass.

The earlier selected coordinates remain rejected due to native body/courtyard
conflicts. The corrected candidate is now the only promoted routing basis;
`ETH_WEST_OUTBOARD_STORAGE_CLEAR` remains the fallback experiment. Detailed
Ethernet/storage/clock routing resumes from this basis with native pad and net
identity, and must be validated as a coordinated neighborhood. PCIe, SERVICE,
power architecture, and the approved stack remain unchanged.

## Macro review correction and corrected routing basis — 2026-09-05

The independent consultant review found that the earlier exact
`ETH_WEST_LOCAL_STORAGE` coordinates were not promotable: native body checks
showed new J2/C4, J2/Q2, J2/U2, U6/U2, and U7/C17 conflicts (the exact list
depends on whether pad/body or courtyard geometry is used). It also found
that the previous metrics omitted U8 from SERVICE and C16/C17/C19 from the
complete storage island. Those omissions are corrected in
`phase24_whole_board_floorplan_discriminator.py`.

The corrected review uses signal-oriented same-net pad/ratsnest metrics and
includes U8 and the complete bridge support cluster. The exact old placement
is rejected as a placement candidate, not as a topology. The new
`ETH_WEST_CLEAR_STORAGE_MID` placement clears the moved-body screen and the
native DRC courtyard count remains at the baseline inherited count of three.
`PHASE24_CORRECTED_MACRO_PLACEMENT.kicad_pcb` is the disposable routing basis;
337/380 affected track items were removed from the two generator passes as
the selected affected-net set was expanded to include bridge power support.
The board is not yet routed or promoted as a Phase 24 pass.

`MACRO_FLOORPLAN_REVIEW = COMPLETE`, with the exact candidate corrected and
the placement decision now evidence-backed. The current implementation class
is `ROUTE DEVELOPMENT PENDING`; raw DRC on an unrouted/stale-copper
placement-only candidate is not a floorplan comparison. Next action is
native-pad, obstacle-aware regeneration of Ethernet/storage/clock on the
corrected macro basis, followed by separate revalidation of unaffected PCIe,
SERVICE, and power islands.

## Whole-board macro-floorplan review — 2026-09-05

Detailed net-by-net routing experiments are paused pending this discriminator.
The native-loaded integrated baseline is `PHASE24_U7_3V3_CURRENT_LOCAL.kicad_pcb`
(SHA-256 `48840a9e353249f43853547a891c5588cdc5254fd771ac7ddfdb21efaddd058e`).
The placement-only review in `PHASE24_WHOLE_BOARD_FLOORPLAN_REVIEW.md` and
`phase24_whole_board_floorplan_discriminator.py` maps the transformed J7
carrier-mating pads and compares multiple disposable coherent-island moves.
It deliberately excludes existing copper and raw DRC counts from floorplan
ranking, separating floorplan topology from immature route implementation.

The native launch centroids are Ethernet `(34.50,99.90)`, PCIe `(69.60,101.50)`,
USB3/storage `(70.04,105.30)`, and SERVICE USB2 `(66.96,99.30)` mm. The current
same-net ratsnest sums are 443.9, 490.8, 231.2, and 40.0 mm respectively for
Ethernet, PCIe/V100, USB3/storage, and SERVICE. The selected
`ETH_WEST_LOCAL_STORAGE` candidate reduces Ethernet to 88.7 mm and storage to
116.5 mm while leaving PCIe and SERVICE unchanged. `CM5_NEIGHBORHOODS` gives
the shortest Ethernet centroid but displaces the already-natural SERVICE
endpoint; `SWAP_ETH_STORAGE` improves both high-speed neighborhoods but is
weaker than the selected joint migration.

`MACRO_FLOORPLAN_REVIEW = COMPLETE`: retain `ETH_WEST_LOCAL_STORAGE` as the
working topology, preserve PCIe and SERVICE anchors, and regenerate affected
Ethernet/storage/clock neighborhoods coherently. Any early copper failure is
`ROUTE IMPLEMENTATION FAILURE`, not `MACRO-PLACEMENT FAILURE`, until the
selected placement receives a fair native-pad obstacle-aware routing cycle.
Phase 24 remains open.

Status: IN PROGRESS — native ERC/netlist and Ethernet support authority pass;
schematic↔PCB component parity and routed acreage closure remain open.

## Ethernet support authority closure

The production `ETHERNET.kicad_sch` now owns C48–C52 and R26–R31 with the
selected sourced MPNs and footprints. The opaque `GBE_LED` sheet pin was
removed. `ETH_LEDY` and `ETH_LEDG` are attached to the native CM5 endpoints
for J7 pads 17 and 15 respectively, matching the CM5IO source mapping.
Native KiCad 10.0.5 export is `phase24-production.xml`; native ERC is
`PHASE24_PRODUCTION_AFTER_ETHERNET_SUPPORT-erc.rpt` with `Errors 0`.
Regression: `validation/phase24/test_ethernet_support_production.py`.

## Ethernet PCB support materialization

`PHASE24_ETHERNET_SUPPORT_MATERIALIZED.kicad_pcb` is a disposable materialized
baseline from the immutable selected-macro parent. `phase24_ethernet_support_pcb_parity.py`
passes against `phase24-production.xml`: all 11 schematic-authoritative
support footprints and every pad net match. Native DRC reports 695 total
violations, 463 unconnected pads, 0 footprint errors, and no track-crossing
records; the added unconnected pads are expected until the local support
network is routed. This is `PCB_SUPPORT_MATERIALIZATION = PASS_WITH_ROUTING_OPEN`,
not full Phase 24 closure.

## Protected 12 V plane experiment

The candidate stack defines `In3.Cu` as `In3.PROTECTED_12V`, but the current
board had no protected 12 V fill. A disposable full-acreage In3 fill was
tested with native refill and DRC. It introduced no shorting or crossing
records and reduced missing connections only from 397 to 395: unresolved
surface regulator/capacitor pads still require explicit physical launches.
The plane-only candidate is rejected as insufficient; the layer role remains
available for a launch-mapped power repair.

## Closed in this checkpoint

- The clean project now resolves all 34 custom symbols through the assembled
  `PiSXMe_RevA_Clean_complete.kicad_sym` library.
- `phase24_repair_root_hierarchy.py` generically replaces the malformed root
  interior/diagonal wiring with outward sheet-edge stubs and named root
  associations, preserving child UUIDs and sheet instances.
- The CM5 sheet border is extended where the legacy final pin was outside its
  rectangle.
- Two unused MIPI1 D2 pins are explicitly marked no-connect; they are outside
  the Rev A interface contract.
- Native KiCad 10.0.5 ERC with `--severity-error` reports `Found 0 violations`.
- `validation/phase3/test_phase24_native_final_authority.py` passes.

## Netlist closure

The warning was caused by four regulator 22 uF capacitors retaining stale
`(instances)` references C30–C33 after their symbol properties were renumbered.
`phase24_repair_duplicate_refs.py` updates both serialized representations to
C44–C47.  KiCad 10.0.5 now exports a non-empty netlist with no annotation
warning.

Artifacts: `PHASE24_NATIVE_ERC_FINAL2.rpt`, `PHASE24_NETLIST_FINAL5.xml`, and
the Phase 24 native-authority regression.

## Remaining parity repair

Fresh comparison of `PHASE24_NETLIST_FINAL5.xml` against
`PHASE23_TEST_DEBUG_PADS_V5.kicad_pcb` found schematic components with no PCB
footprint: `Y1`, `R23`, `C42`, `C43`, and `C44`–`C47`.  These are real storage
clock and regulator support components, not optional debug artifacts.  The
first disposable clock graft was rejected because its historical hard-coded
U7 clock-row coordinates produced true shorts; it is retained only as failed
evidence.  Phase 24 stays open until a coordinate-derived, native-DRC-clean
materialization and parity check are complete.

The next coordinate-derived candidate, `PHASE24_SUPPORT_MATERIALIZED`, was
also rejected.  Its clock corridors crossed inherited SATA/USB copper and its
U5-side bulk-cap graft entered existing regulator pad/return geometry.  This
establishes that the missing support must be integrated by regenerating the
coordinated storage/regulator local routes, not by overlaying support copper
onto the Phase 23 ancestor.

The `PHASE19_RELOC_U270J190_COORD49_FULL` storage-only donor was then tested
as a coordinated transplant.  It contains USB3, SATA, and clock copper, but
its relocated USB3 corridor crosses the frozen V5 PCIe corridor after merge.
It was rejected.  The valid next class is to retain V5's proven U7/J3
high-speed placement and add an obstacle-aware clock route locally, followed
by a separately coordinated U5 bulk-cap island.

## Latest bounded experiment

`phase24_materialize_support_v2.py` generated `PHASE24_SUPPORT_V2.kicad_pcb`
from actual U7 pad coordinates, with the clock parts in open acreage and the
four schematic-authoritative U5 capacitors materialized. It was rejected by
native DRC (`234` violations, `409` unconnected items): the attempted common
B.Cu clock surface still crossed inherited SATA copper, crossed between clock
branches, and produced U7 pad-field shorts. This is not evidence against the
storage architecture. The next valid class is layer-separated clock fanout
with vias outside the U7 pad field, then an independent coherent U5
rail/return island. See `PHASE24_BLOCKER_REPORT.md`.

The first rotated-U7 discriminator was rejected as an authoring/tooling proof:
it changed U7 orientation but used a pre-rotation hard-coded clock endpoint
graph, producing pad mismatches. It is not a valid architecture failure. Any
next rotated-U7 experiment must query the post-rotation footprint and support
pad coordinates before creating tracks or vias.

The corrected rotated-U7 source-escape discriminator now derives post-rotation
U7 endpoints and produces zero native DRC `shorting_items` and
`tracks_crossing` records for the clock escape. It remains a disposable oracle
because the Y1/R23/C42/C43 branches and U5 C44-C47 island are not yet complete.

The latest bounded sweep (`phase24_clock_position_sweep.py`) improved the
clock-support search to a compact near-west underside candidate, but it still
has one localized B.Cu clock-lane crossing at the U7 escape. It remains an
unpromoted experiment; Phase 24 is still open.

The subsequent side-separated A* clock oracle reached zero clock-specific
crossing/shorting records in native DRC. A follow-on support materialization
was rejected at 240 native violations because the added Y1 passive branches
entered the crystal pad field and the C44--C47 placement overlapped existing
regulator support. The clock oracle is retained as evidence; support networks
must be placed and routed as independently bounded islands.

The native-orientation disposable fixture reports zero unconnected items,
shorts, crossings, and footprint errors, but it is not a complete support
topology: inspection shows that all passive branches are not routed to
R23/C42/C43. It remains a source-escape/footprint discriminator only. The
remaining work is a genuinely complete rot180 coordinate transplant plus a
separate U5 capacitor island.

The first strict complete-fixture implementation was rejected by native DRC
(24 violations: 5 crossings, 4 shorts, 8 disconnected pads). It is retained
as evidence that the next implementation must derive and reserve the actual
Y1 pad field rather than assume a generic three-bus geometry.

The subsequent launch-height refinement remained invalid (9 native DRC
violations, including 8 crossings). It is rejected; the next candidate must
use an obstacle-mapped proven support template.

The first obstacle-aware passive router found all six passive paths but was
rejected by native DRC (380 violations: 29 shorts and 13 crossings). The
remaining repair must regenerate the clock topology with branch reservations
before adding passive fanout.

The multi-net graph-anchor sweep found all six branch paths but was rejected
by native DRC (271 violations: 10 shorts and 4 crossings). The next repair
class is layer-separated passive dogbones with offset vias and short rail
joins.

A five-position coordinated-island sweep was also rejected: four placements
had no conservative route to a rail anchor and the best generated board had
322 native DRC violations. No candidate was promoted.

The rail-attachment variant was rejected by native DRC (268 violations: 12
shorts and 9 crossings). The remaining valid implementation class is a
single coordinated clock graph containing source escape, Y1, R23, C42, and
C43 before materialization.

Layer-separated passive dogbones with offset through-vias were also rejected
by native DRC (306 violations: 14 shorts and 6 crossings); four outboard
variants had no conservative path. A fresh coordinated clock graph is now
required for support integration.
The coordinated layer-owned disposable fixture now proves the complete
Y1/R23/C42/C43 clock-support graph: XI is carried on B.Cu, XO on F.Cu, and
VSSOSC on a separate B.Cu perimeter. Native DRC reports no clock crossings,
shorts, footprint errors, or clock unconnected records. Its eight remaining
unconnected records are deliberately isolated non-clock U7 pads in the
stripped fixture; acreage transplant and full Phase 24 parity remain open.
The first acreage support transplant was rejected: native DRC reported 218
violations, including clock-net crossings and a VSSOSC/XO short caused by
placing passive branches into inherited USB3 and clock corridors. This does
not invalidate the coordinated disposable topology. A separate U5 C44-C47
island trial has no shorting or crossing records, but retains inherited
unconnected/dangling cleanup and is not yet promoted.
The follow-up surface-only U5 support trial was also rejected: native DRC
reported 202 violations, including a rail/ground short and crossings. It is
not promoted; the U5 rail must be regenerated with a real return strategy and
clearance-aware source launch.
All eight previously missing schematic-authoritative references are now
materialized in the disposable `PHASE24_ALL_AUTHORITATIVE_PARTS` baseline.
The exact pad-net audit passes for Y1/R23/C42/C43/C44-C47. Native DRC reports
187 inherited violations and 406 unconnected pads, but no shorting or crossing
records; this closes the component-materialization discriminator only, not
routed Phase 24 closure.
The outboard U5 surface placement was rejected as the same failed solution
class: native DRC reported 203 violations, including a bridge-1V1/POWER_GND
short and crossings. Two surface-only placements have now failed; the next
repair must use a clearance-mapped ground-aware island rather than another
surface rail trunk.
The independent hardware audit confirms the eight-part materialization is
narrow evidence only: full-board parity, routing connectivity, source
ownership, and footprint-filter parity remain unproven. The ground-aware U5
V2 trial reduced the new problem to one localized rail/return crossing with
no new shorting record, but still has unconnected/inherited failures and is
not promoted. The next U5 repair must separate the source and return lanes by
layer or use a mapped return launch.
The latest U5 V2 source-escape refinement was rerun after moving the rail
launch around the regulator feedback corridor. Native DRC remains at 197
violations and 392 unconnected pads, with one source/return crossing and no
shorting record. It is retained as a rejected disposable result; the
ground-aware U5 island still needs a layer-separated source/return launch.
The current U5 V2 rerun uses a left-side source detour to avoid the feedback
segment, but native DRC still reports one crossing at the separate return
trunk and 392 unconnected pads. It remains a disposable negative result; no
production geometry has changed.
The stripped U5 layer fixture now proves the C44-C47 source/return topology:
ordinary through-vias launch 1V1 and POWER_GND, with separate B.Cu rail and
return corridors. Native DRC reports zero `shorting_items` and zero
`tracks_crossing`; its 499 unconnected records are deliberate non-target
fixture/U5 pads. This is a reusable topology oracle, not an acreage promotion.
The corrected U5 layer fixture was rerun after extending both layer-owned
trunks to the rotated capacitor pad rows. Native DRC still reports zero
shorting and zero crossing records; 499 unconnected pads are deliberate
non-target fixture/U5 pads. The separate graph-audit script exposed a
coordinate-join defect and is not used as closure evidence; acreage U5
integration remains open.
The U5 fixture regression audit now passes after correcting its serialized
via/track coordinate joins: all four C44-C47 rail pads connect to U5.9 and
all four return pads connect to R20.2. Native DRC remains zero shorts and zero
crossings for the fixture. This strengthens the topology proof only; acreage
integration and full-board parity remain open.
The PCB-only Ethernet alias filter removed CCT/CCT1-CCT4 and RCT1-RCT4 from
the materialized parity candidate. The candidate now contains all 78 native
schematic references plus only MECH_M2_2280 and TP1-TP13; the exact reference
set audit passes. Native DRC introduces no shorting or crossing records.
Electrical Ethernet return/support routing must still be reconciled before
this candidate can be promoted.
The filtered clean-reference candidate was revalidated after the alias removal:
the 78-reference audit still passes, and native DRC reports no shorting or
track-crossing records. It retains 201 DRC violations and 406 unconnected
pads, so it remains a parity/source candidate rather than a routed production
artifact.

## Integrated U5 layered launch

`phase24_u5_integrate_layered.py` applies the reviewed source/return topology
to the filtered acreage candidate using the existing authoritative C44-C47
footprints, ordinary through-vias, and refilled In1/In4 ground zones.
`phase24_u5_layer_connectivity_audit.py` passes: U5.9 joins C44-C47.1 and
R20.2 joins C44-C47.2. Native DRC reports 201 violations and 397 unconnected
pads, with zero `shorting_items` and zero `tracks_crossing`. This closes the
integrated U5 topology discriminator only; full Phase 24 routed parity remains
open.

## Rejected clock-oracle acreage transplant

`phase24_integrate_clock_oracle.py` attempted to transplant the proven
rotated-U7 clock copper from `PHASE19_PASS_CLOCK_ROT180_S20.kicad_pcb` onto
the integrated acreage candidate while reusing the existing Y1/R23/C42/C43
authoritative footprints. Native DRC rejected the overlay: 288 violations,
400 unconnected pads, multiple track crossings, and shorts between clock
nets and existing SATA/bridge copper. The standalone oracle remains valid;
its unmodified coordinate context cannot be overlaid onto this already-routed
acreage candidate. The experiment is retained as negative evidence, and its
KiCad via-width API call was corrected for reproducible reruns.

## Corrected clock-fixture transform rerun

The coordinate transform was corrected from the footprint-origin frame to the
serialized U7 pad frame: fixture U7.52 `(97,104.5)` maps to acreage U7.52
`(123,135.5)` under `x'=220-x, y'=240-y`. The rerun places the reused clock
footprints consistently and reproduces the fixture copper. It is still
rejected for acreage promotion: native DRC reports 227 violations, 393
unconnected pads, multiple crossings, and shorts between the clock return/XI
nets and existing SATA copper. This establishes that the proven clock topology
needs a locally regenerated corridor around the existing storage routes, not a
blind copper overlay.

## U5 physical-audit correction and negative controls

`phase24_u5_layer_connectivity_audit.py` was corrected to invoke KiCad's
native connectivity rebuild over serialized pads, tracks, vias, layers, nets,
and filled zones. Expected target membership is assertion-only; no synthetic
edges or XY-only nodes are used.
Against `PHASE24_U5_INTEGRATED_LAYERED.kicad_pcb` it passes for U5.9 to
C44-C47.1 and R20.2 to C44-C47.2. The disposable negative-control harness
removes an actually required C44 rail dogbone trace in a copied board; the
control correctly makes the audit fail. This native component has no
necessary via, so no via-removal claim is made. Native DRC has no
target C44-C47 unconnected finding, while the remaining 397 unconnected pads
are outside this local proof and keep full Phase 24 open.

## Native unconnected census

`phase24_native_unconnected_census.py` parses the native DRC report without
changing severity or filtering the gate. The 397 records are dominated by
146 `12V_PROTECTED`, 128 `POWER_GND`, and 50 `/CORE_CM5/POWER_GND` records;
smaller groups include bridge 1V1/3V3, input/fused 12 V, SATA RX-N, and the
clock nets. The complete table is in
`PHASE24_NATIVE_UNCONNECTED_CENSUS.md`. This identifies the next repair
classes while retaining every native connection as mandatory.

## U7 SATA RX-N pad-field repair

The U7 `BRIDGE_SATA_RX_N` repeated-pad group was repaired with four same-net
F.Cu pad-field links, an offset F.Cu/B.Cu via at `(127.5,140.5)`, a B.Cu
dogleg around the existing SATA-TX trunk, and an offset return via at
`(119.5,134.5)`. Native DRC on the resulting candidate reports 201
violations, zero `shorting_items`, zero `tracks_crossing`, and 392
unconnected pads versus 397 before the repair. No `BRIDGE_SATA_RX_N`
unconnected record remains. This is targeted storage evidence; full-board
parity remains open.

## U5 input-power field stitch experiment

`phase24_u5_input_power_stitch.py` tested the serialized U5 exposed-pad field
using only same-net F.Cu tracks. The 12V_PROTECTED chain joins U5 pads 1, 16,
and 14; its pad-14 leg doglegs around the explicit NC pad 15. The POWER_GND
chain joins the central exposed row and side pads. Native KiCad 10.0.5 DRC
reports 201 violations and 390 unconnected items, compared with 201 and 397
for the integrated-layered baseline; there are zero `shorting_items` and zero
`tracks_crossing`, and no remaining U5 12V_PROTECTED or POWER_GND unconnected
record. This is a valid targeted physical repair, not full Phase 24 closure:
the remaining missing connections are dominated by board-wide protected-12V,
global/CM5 ground, input/fused-12V, low-voltage, and clock/storage groups.

## Regulator-field follow-up

`phase24_regulator_power_field_stitch.py` generalized the serialized
TPSM63606 exposed-pad repair. The all-regulator trial was rejected: U4's
existing PG_BRIDGE_3V3 corridor occupies the direct 12V escape and native DRC
reported one crossing and three shorts. A bounded U3+U5 trial was then run
without U4. It reports the inherited 201 DRC violations, zero shorts, zero
crossings, and 384 unconnected items (down from 397). This promotes only the
U3/U5 local field evidence; U4 requires an obstacle-aware escape and the
board-wide power/ground distribution is still unresolved.

## B-side input fuse pad-field experiment

`phase24_f2_padfield_stitch.py` joins the four raw-side F2 pads and four
fused-side F2 pads as two separate same-net F.Cu fields. Native DRC remains at
the inherited 201 violations with zero shorts and zero crossings; unconnected
items fall from 397 to 391. The candidate is retained as targeted input
geometry evidence, but the F2 fields still need named connections to J6/U2/Q2
and the rest of the protected distribution.

The J1 bus was then combined with a full `In3.PROTECTED_12V` zone in
`phase24_j1_protected_plane.py`. Native DRC remains at 201 violations with
zero shorts and zero crossings; unconnected items improve 268 to 265. The
plane is therefore electrically compatible with the validated connector bus,
but does not replace explicit surface launches for the remaining regulators,
capacitors, input branches, and SXM2/ground populations.

The J1 POWER_GND field was then connected as seven serialized vertical F.Cu
columns, each entering the existing In1/In4 ground planes through an ordinary
via below the protected B.Cu bus. The first y=96.5 mm launch trial was
rejected for six native POWER_GND-to-12V_PROTECTED shorts at the bus. Moving
only those launches to y=98.0 mm removes the shorts: native DRC returns to 201
inherited violations with zero shorts/crossings and 195 unconnected items.
This is accepted J1 ground-field evidence; local ground launches elsewhere
and the separate CM5 ground net remain open.

## CM5 ground-launch experiment (rejected)

The CM5 connector ground net was tested with a dedicated local In1 plane
island and serialized J7 pad-to-via launches. A 0.85 mm outward offset
shorted adjacent signal pads; widening to 1.8 mm still produced new
clearance/short records, and a 3.0 mm perimeter variant reduced the native
unconnected count to 176 but produced 17 shorts, eight crossings, and 422
violations. All variants are rejected. CM5 ground must not be copper-bridged
to global POWER_GND; an obstacle-aware escape or authority correction is
required.

## Bridge low-voltage pad-field experiment

The first direct U4/U5 low-voltage joins crossed the intervening POWER_GND
pad and were rejected with two shorts. The corrected
`phase24_bridge_lv_padfields.py` exits each pad field around that ground pad,
then joins the bridge rail pads on F.Cu. Native DRC is 201 inherited
violations with zero shorts and zero crossings; the plane-based candidate's
unconnected count falls from 265 to 261. This is accepted targeted evidence;
remaining bridge capacitor distribution and control/clock connectivity still
require complete named routing.

## J1 protected-12V field bus experiment

The first J1 B.Cu-only bus was rejected because the saved connector pads are
surface pads and native DRC worsened to 214 violations. The corrected
`phase24_j1_protected_bus.py` derives all 13 protected-pad columns from the
serialized J1 footprint, joins each column on F.Cu, transfers each column
through one ordinary offset via below the final row, and joins the B.Cu bus.
Native DRC returns to the inherited 201 violations with zero shorts and zero
crossings; unconnected items fall from 397 to 268. This is strong targeted
evidence for the J1 protected field, but named attachment to the rest of the
protected distribution and the remaining ground/CM5/rail groups are still
required.

The analogous F1 A-side pad-field trial joins its raw and fused four-pad
groups independently. Native DRC remains at 201 violations with zero shorts
and zero crossings; unconnected items fall from 397 to 392. This is retained
as targeted evidence and preserves the dual-input architecture. The existing
F1/J5/Q1/U1 branch still needs complete named routing and plane launches.

The U4-specific left-side dogbone was rejected as well. It removed the U4
short class, but native DRC found four F.Cu crossings against the existing
PG_BRIDGE_3V3 corridor and U4 ground escape, leaving 390 unconnected items.
U4 therefore needs a layer-separated or locally regenerated corridor rather
than another same-layer coordinate tweak.

A later U4 perimeter reroute was also tested. The initial layer-separated
trial crossed the existing B.Cu feedback trunk; the corrected perimeter
variant moved the escape to y=100.5 mm and avoids that trunk. Native DRC is
back to the inherited 201 violations with zero shorts and zero crossings. It
is retained as a clean U4 local geometry experiment, but the remaining 390
native unconnected items are board-wide and still prevent Phase 24 closure.

The U3 POWER_GND exposed field was tested with a right-side perimeter escape
around the central thermal row and a lower side-pad rail. Native DRC remains
at 201 inherited violations with zero shorts and zero crossings; the prior
bridge candidate's unconnected count falls from 261 to 258. This is accepted
targeted regulator-return evidence; full ground-plane attachment remains
open.

The combined U4/U5 ground-field trial was rejected for two crossings against
the existing U4 PG_BRIDGE_3V3 corridor. A bounded U5-only follow-up retains
the clean U3 ground result and adds the U5 perimeter field: native DRC is 201
inherited violations with zero shorts/crossings and 255 unconnected items.
U4 remains intentionally excluded from this promoted local candidate until
its control corridor is regenerated.

## Global POWER_GND launch cluster

Following the independent PI review, `phase24_pgnd_launch_cluster.py` adds
short F.Cu dogbones and ordinary through-vias for U1.2, U2.2, J4's four
POWER_GND pads, and U8.3, feeding the existing In1/In4 planes. The first J4
bottom-left launch was rejected because its via hit the existing USB2 B.Cu
track; moving that one via to `(40.5,103.0)` corrected the collision. The
final native DRC candidate reports 201 inherited violations, zero shorts,
zero crossings, and 188 unconnected items versus 195 before the cluster.
CM5 `/CORE_CM5/POWER_GND` remains separate and untouched.

## Cumulative local-repair composition

`phase24_integrate_local_repairs.py` composes the validated J1 protected bus
and In3 plane, J1 ground columns, global U1/U2/J4/U8 returns, bridge
low-voltage perimeter escapes, U3/U5 protected-field escapes, U4's perimeter
protected escape, and separate F1/F2 raw/fused pad fields. The first
composition also added U3/U4/U5 ground-field copper and was rejected for
three native crossings between 12V and ground field routes. Removing those
overlapping ground additions yields a clean cumulative candidate: native DRC
201 inherited violations, zero shorts, zero crossings, and 168 unconnected
items. Ground-field additions remain separately validated and must be
reintegrated only with obstacle-aware layer separation.

## Cumulative U7 RX-N integration

`phase24_compose_u7_rxn.py` applies the previously validated U7
BRIDGE_SATA_RX_N pad-field stitch to the cumulative local-repair candidate.
Native DRC remains at 201 inherited violations with zero shorts and zero
crossings; unconnected items fall from 168 to 163. The storage correction
therefore composes cleanly with the accepted power/rail repairs. Clock and
the remaining SATA/control groups remain open.

## U7 clock-pad authority correction

Inspection of the cumulative candidate found U7 pads 52, 53, and 54
serialized without net assignments, despite the schematic mapping to
`BRIDGE_XI`, `BRIDGE_VSSOSC`, and `BRIDGE_XO`. The disposable
`phase24_assign_u7_clock_pads.py` materializes those exact net identities.
Native DRC remains at 201 violations with zero shorts and zero crossings;
the unconnected count changes from 163 to 166 because the now-authoritative
source pads correctly enter the native gate. Clock copper fanout remains
unresolved and will be routed from these real source pads.

## U7 BRIDGE_CFG join experiment (rejected)

The direct CFG pad join crossed U7 pad 24 (`BRIDGE_3V3`) and was rejected.
The attempted perimeter reroute around the pad field still introduced two
shorts and one crossing in native DRC. The CFG control net remains open and
must use a layer-separated, pad-frame-derived escape.

## U7 oracle-derived clock source escape

`phase24_u7_clock_source_escape.py` adds the rotated-U7 oracle's XI and
VSSOSC escapes plus a corrected XO dogleg below the SATA-TX corridor. The
first XO path was rejected for one crossing; the corrected disposable
candidate has zero shorts and zero crossings. Native DRC reports 204 total
inherited/placement violations and 166 unconnected items. This closes the
source-escape discriminator only; support-passive branches and end-to-end
clock connectivity remain open.

## Complete clock passive-branch trial (rejected)

`phase24_clock_passive_branches.py` attempted full XI/XO/VSSOSC branches on
B.Cu from the clean U7 source escape to Y1/R23/C42/C43. The candidate reduced
the unconnected census to 156, but native DRC found three shorts and ten
crossings where the branches entered adjacent passive pads and existing
storage copper. It is rejected; the useful result is that clock closure needs
isolated pad launches and layer-separated buses, not direct B.Cu pad-field
approaches.

## Isolated clock-launch trial (rejected)

`phase24_clock_isolated_launches.py` added offset through-vias at every
clock-support passive pad and separate F.Cu buses. Native DRC rejected the
candidate with 17 crossings and three shorts, including long XI/XO corridors
through existing SATA/USB copper and an XO approach into an unassigned U7
pad. The next valid class must use obstacle-aware layer-separated routing
from the serialized U7 pad field.

## Exact clock-oracle transplant comparison (rejected)

`phase24_clock_oracle_coordinated.py` moved the existing Y1/R23/C42/C43
footprints into the proven rotated-U7 oracle coordinates and copied only the
oracle's XI/XO/VSSOSC tracks and ordinary vias. The transplant is valid as a
reference comparison but is rejected on the cumulative acreage board: native
KiCad DRC reports 288 violations, including clock/SATA crossings and
clock-to-J3 shorts/clearances. This confirms the oracle topology is sound but
its fixed coordinate context must be locally regenerated around the current
storage launch.
## Exact coordinated oracle transplant — rejected

`phase24_clock_oracle_coordinated.py` moved Y1/R23/C42/C43 to the exact
rotated-U7 oracle positions/orientations and copied only clock-net tracks and
ordinary vias onto the current U7 authority candidate. Native KiCad DRC
reported 288 violations and 166 unconnected items, including clock/SATA
crossings, clock/J3 interactions, and shorts/clearance failures. Rejected for
acreage integration; the oracle topology remains valid and must be regenerated
around the current serialized U7/storage geometry.

## U5 connectivity audit corrected

`phase24_u5_layer_connectivity_audit.py` now uses KiCad's native connectivity
rebuild over the saved PCB and checks asserted target pads against native
connected-item components. It no longer creates graph edges from expected
connectivity. The saved U5 board passes, and the regression negative control
removes an actually connected U5.9 trace in a disposable board object; the
audit then fails as required. No validation severity was changed.

## Clock fixture V2 and acreage transform

`phase24_complete_clock_fixture_v2.py` produces a complete clock-specific
fixture with XI/XO on B.Cu and VSSOSC on an F.Cu perimeter. Its native
connectivity and clock-short/crossing regression passes. The transformed
acreage experiment is rejected at 226 DRC violations, including seven clock
shorts and 16 crossings; the fixture topology is retained, but the fixed
transform is not promoted.

## Incremental XI/XO/VSSOSC probes

The XI-only and XI+XO probes each have zero native short/crossing classes and
reduce the unconnected census from 166 to 165 and 164 respectively. The first
VSSOSC addition is rejected at 163 unconnected records because its F.Cu path
crosses the inherited SATA-TX-N corridor and shorts the XI launch and a
POWER_GND pad. The next repair is a layer-separated VSSOSC obstacle crossing;
XI/XO are retained unchanged.

The subsequent passive-field B.Cu search could not find a path from the
serialized Y1.1 launch to R23.1 within the current local bounds, so no
candidate was emitted. This further localizes the open work to coordinated
passive-field routing/placement.

## Complete clock composed on cumulative repairs

`phase24_apply_complete_clock.py` composed the complete native-clean clock
source (`PHASE24_CLOCK_COMPLETE_ASTAR_V2.kicad_pcb`) onto
`PHASE24_LOCAL_REPAIRS_U7_RXN.kicad_pcb`. Native pad-component checks pass for
XI (Y1.1/R23.1/C42.1), XO (Y1.3/R23.2/C43.1), and VSSOSC
(Y1.2/Y1.4/C42.2/C43.2). Native DRC reports 205 violations and 156
unconnected records, with zero `[shorting_items]` and zero
`[tracks_crossing]`. The clock is therefore promoted into the cumulative
ancestor; Phase 24 remains open for the unrelated board-wide connectivity
census.

## Bridge 1V1 capacitor-field continuation

`phase24_bridge_1v1_cap_chain.py` adds adjacent ordinary-via escapes from the
left-side rail pad of the spaced C26/C27/C28/C29 and C34-C41 fields, then joins
the escapes on B.Cu. Native DRC holds at 205 violations with zero
`[shorting_items]` and zero `[tracks_crossing]`; the unconnected census falls
from 156 to 145. The candidate is accepted as the next cumulative ancestor.
The remaining BRIDGE_1V1 records are isolated R19, R22, and C41 endpoints and
will be handled separately rather than assuming this field route closed them.

## Bridge 1V1 field joined to U5

`phase24_bridge_1v1_field_join.py` adds a B.Cu perimeter join from the
field's existing ordinary via to the C46.1/U5.5/U5.8/U5.9 output island.
Native DRC remains at 205 violations with zero `[shorting_items]` and zero
`[tracks_crossing]`; unconnected records fall to 144. Native connectivity
confirms the complete capacitor field and U5 output pads are one component.
R19.1 and R22.1 remain isolated endpoints for a separate local repair.

## Bridge 1V1 feedback endpoints

The R19.1 outboard B.Cu join and the short R22.1 local B.Cu join were tested
sequentially from the accepted field/output ancestor. Both pass native DRC
without shorting or crossing classes; the cumulative unconnected census falls
from 144 to 142. The BRIDGE_1V1 rail is now natively continuous for the
identified endpoints.

## Bridge 3V3 continuation

The C16/C17/C19 rail field was joined with ordinary pad-adjacent vias and a
B.Cu chain. R11.1 was joined directly to C18.2, and R14.1 was routed by a
right-side F.Cu dogleg into the existing U4 output island. Sequential native
DRC checks remain at zero shorting/crossing classes; the cumulative
unconnected census falls from 142 to 138.

## Power-input 12V_A bypass

`phase24_12va_c3_join.py` adds a short F.Cu dogleg from the isolated C3.2
bypass pad to U1.3 on `/POWER_INPUT/12V_IN_A`. Native DRC remains free of
shorting and crossing classes; the cumulative unconnected census falls from
138 to 137. The input topology and fuse/protection architecture are unchanged.

## U7 BRIDGE_CFG closure

`phase24_u7_cfg_join_current.py` regenerated the serialized U7
`/STORAGE/BRIDGE_CFG` pad-to-pad copper on the accepted ancestor. Native DRC
remains at zero shorting/crossing classes and the unconnected census falls
from 137 to 136. This closes the one remaining U7 configuration connectivity
record without changing the storage architecture.

The C5.2-to-C6.2 direct POWER_GND trial is rejected: fresh DRC reports 209
violations, 140 unconnected records, and one short. The one-record reduction
does not justify the introduced short; the clean 3V3-cap-chain ancestor is
retained.

## Fresh native DRC reconciliation

An independent auditor reran KiCad DRC on the exact serialized
`PHASE24_U7_CFG_JOIN_CURRENT.kicad_pcb` ancestor. The authoritative fresh
result is 235 total violations, 136 unconnected records, 4
`[shorting_items]`, and 7 `[tracks_crossing]` records. Earlier incremental
receipts that reported zero shorts/crossings used a parser scoped after the
unconnected section and therefore did not count those earlier report
sections. Those zero claims are superseded; no candidate is considered clean
until the complete report is clean.

The top-row-only J7 ground experiment is rejected: fresh DRC reports 134
unconnected records but 8 shorting and 10 crossing records. It is retained
only as negative geometry evidence.

The reconciliation receipt `PHASE24_DRC_RECONCILIATION_RECEIPT.md` establishes
`PHASE24_BRIDGE_1V1_CAP_CHAIN.kicad_pcb` as the latest clean working basis.
The later R22, U7 CFG, C3, and 3V3 dogleg candidates are not promoted until
they pass a full-report native rerun; the current serialized U7 CFG candidate
is explicitly rejected at 235 violations, including four shorts and seven
crossings.

The full-report rerun of `PHASE24_BRIDGE_1V1_R19_JOIN.kicad_pcb` is clean of
shorting/crossing classes at 208 violations and 143 unconnected records. From
that basis, `PHASE24_BRIDGE_3V3_CAP_CHAIN_V2.kicad_pcb` is also clean of
shorting/crossing classes at 208 violations and 141 unconnected records. These
are the current accepted working sequence; the R22, 3V3 support, C3, and CFG
joins are not promoted from contaminated ancestors.

## CM5 lower-bank ground comb

`phase24_cm5_ground_lower_comb.py` connects the J7 CM5-ground pads from
y=102.7 through y=117.9 using two outer F.Cu comb rails and same-row bridges.
The active upper Ethernet fanout rows y=98.7 through y=101.1 are deliberately
untouched. Fresh native DRC reports 208 violations, 127 unconnected records,
zero shorts, and zero crossings. This is accepted targeted progress; the
upper high-speed rows and the separate connector-to-plane CM5-ground launch
remain open.

The exact three-pad discriminator recommended by the KiCad review was tested
from the clean V2 basis: J7 pads 161/167/173 at (66.96,110.7),
(66.96,111.9), and (66.96,113.1) escape to x=65.50 and join at one ordinary
0.50/0.30 mm through-via. Fresh native DRC reports 209 violations, 139
unconnected records, zero shorts, and zero crossings. This is accepted
targeted CM5-ground progress; the remaining upper rows and plane attachment
are still open.

The accepted right-column collector was expanded incrementally from the
three-pad discriminator. The first expansion remains at 209 violations, 136
unconnected records, zero shorts, and zero crossings; adding the next four
right-column pads (y=102.3–105.9) yields `PHASE24_CM5_GROUND_RIGHT_COLUMN_EXPAND_V3`
at 209 violations, 130 unconnected records, zero shorts, and zero crossings.
No upper Ethernet-row copper or new via field was introduced.

The lower x=70.04 right-column group was then collected on an outer x=71.50
F.Cu rail for y=110.7–117.9. `PHASE24_CM5_GROUND_RIGHT_OUTER_V4` remains at
209 violations, reduces unconnected records from 130 to 124, and introduces
zero shorts or crossings. This lower collector is accepted; the remaining
J7 findings are the upper interleaved rows and the unconnected connector
attachment.

The upper same-row-only J7 ground bridges are rejected: fresh native DRC
reports 216 violations, 124 unconnected records, one short, and six
crossings. This confirms that the live Ethernet launch segments must be
regenerated before upper-row CM5-ground collection can proceed.

The upper-row comb extension is rejected: fresh native DRC reports 223
violations, 121 unconnected records, three shorts, and nine crossings. The
failure occurs in the live Ethernet launch rows, so the lower-comb candidate
remains the accepted basis and the next experiment must regenerate those
signal launches rather than extend the ground comb through them.

The same-row-only upper J7 ground bridges are also rejected: fresh native DRC
reports 216 violations, 124 unconnected records, one short, and six
crossings. Upper-row CM5-ground collection therefore requires regeneration of
 the existing Ethernet pad escapes; no further comb-only variant is promoted.

The accepted lower-right collector was extended with same-row F.Cu bridges
between the x=66.96 and x=70.04 J7 ground banks for y=109.5 through 117.9.
The serialized `PHASE24_CM5_GROUND_RIGHT_SAME_ROWS` candidate passes the full
native DRC classes relevant to this repair at 209 violations, 122 unconnected
records, zero shorts, and zero crossings. It is promoted as the current clean
CM5-ground working basis; no native finding or severity was waived.

A dedicated In1 `/CORE_CM5/POWER_GND` plane-attachment trial was rejected.
The first via location was correctly identified as dangling; after moving it
to the accepted outer collector and correcting the drill to the board minimum,
fresh native DRC still reports 210 violations and 122 unconnected records,
with zero shorts/crossings but no connectivity improvement. The zone/via
trial is not promoted and the 209/122/0/0 same-row basis remains authoritative.

An upper J7-ground outer-escape trial was also rejected. It escaped the three
upper rows to separate outer F.Cu columns without pad-field bridges, but fresh
native DRC reports 215 violations, 118 unconnected records, two shorts, and
three crossings. A specialist review confirms that the preserved upper
Ethernet lanes do not provide enough clearance for ordinary 0.50/0.30 mm
through-via transitions; no upper escape is promoted.

## Macro-floorplan review amendment

The live native-loaded integrated candidate is
`PHASE24_CM5_GROUND_RIGHT_SAME_ROWS.kicad_pcb`, checkpointed through
`4ace494`. Its transformed geometry places J7 on B.Cu at (35,130), with
Ethernet pads at (32.96/36.04, 99.1–100.7), U8 at (58,100), and J2 at
(77.5,53). U7/J3 storage is at (120,140)/(145,125); J4 SERVICE is at
(45,100); J1 PCIe/SXM2 is at (150,90); power/regulator islands occupy the
west, south, and east edges. Native-loaded group metrics are Ethernet 21.54
mm nearest-pad distance and 534.4 mm F.Cu copper, PCIe 55.39 mm and 704.5 mm,
USB3-storage 53.81 mm and 323.8 mm, and SERVICE 19.96 mm and 101.6 mm.

Three disposable no-major-body-overlap candidates were generated:
`PHASE24_MACRO_ETH_WEST`, `PHASE24_MACRO_ETH_SOUTH`, and
`PHASE24_MACRO_STORAGE_LOCAL`. They are placement-only studies; their
existing copper is intentionally not considered valid after movement. The
review establishes that the acreage macro-floorplan should be repaired as
coherent functional neighborhoods before further net-by-net Phase 24 repair.

Two outboard `POWER_GND` return experiments were rejected. A proposed
C14-to-C19 horizontal chain produced 219 violations, 118 unconnected
records, three shorts, and two crossings. Narrowing the trial to adjacent
C14-to-C15 still produced 212 violations, 121 unconnected records, and two
shorts. Neither return-row candidate is promoted; the clean same-row CM5
ground basis remains 209/122/0/0.

The earlier accepted J1 ground-column geometry was composed onto the current
cumulative basis as a disposable test. It does not transplant cleanly:
fresh native DRC reports 217 violations, 122 unconnected records, one short,
and two crossings. The current 209/122/0/0 same-row CM5-ground candidate is
retained; no J1 column geometry is promoted.

The cumulative U5 exposed-ground field stitch was tested from the accepted
same-row basis and rejected: native DRC reports 210 violations, 117
unconnected records, and one `POWER_GND`/`BRIDGE_1V1` short. Three
single-segment discriminators reproduce the same short class (210/119/1/0,
211/122/1/0, and 211/122/1/0). The corrected U5 native-connectivity audit
still passes independently; no U5 field copper is promoted.

## Macro-floorplan identity correction

The macro review's earlier `U8` Ethernet label was incorrect. Native-loaded
PCB identity is `U8` = SERVICE USB2 ESD (`Texas_DRT_3`), while Ethernet ESD is
`U6`/`U9` = `TPD4EUSB30`. Proposed Ethernet island moves apply to `U6`/`U9`
and `J2`; native geometry and candidate generation are corrected accordingly.
This is a documentation correction, not a validation waiver.

## ETH_WEST_OUTBOARD placement study

The initial ETH_WEST ESD coordinates were inside the native J7 body bbox and
were rejected mechanically. `PHASE24_MACRO_ETH_WEST_OUTBOARD.kicad_pcb` moves
U6/U9 to `(20,104)/(26,104)` and J2 to `(15,145)`. Native bbox inspection
shows no J7-body intersection for those three Ethernet bodies. It is not yet
an accepted routed candidate.

## ETH_WEST trial rejected

The independent review selected `ETH_WEST` as the best macro candidate. A
disposable rigid CM5IO-derived transplant moved native `J2/U6/U9` coherently,
but native DRC reported 571 violations, 123 unconnected records, 12 shorts,
and 20 crossings because translated copper entered unrelated acreage
geometry. The result is rejected; live-pad obstacle-aware regeneration is
required next.

The first west study's ESD coordinates were also identified as lying within
the native CM5 body bbox. A corrected `PHASE24_MACRO_ETH_WEST_OUTBOARD`
placement study puts U6/U9 west of that body at `(20,104)/(26,104)` while
retaining the west-edge J2. It is the current mechanically conservative
Ethernet placement candidate; no copper has yet been promoted.

The cross-class alternative `PHASE24_MACRO_ETH_EAST_ESD_WEST_JACK` keeps
U6/U9 east of J7 and moves only J2 west. It is retained for routing comparison
if the outboard-west ESD escape cannot preserve pair integrity without
entering the CM5 body.

The live-pad `ETH_EAST_ESD_WEST_JACK` routing discriminator was run with all
eight CM5IO-authoritative MDI nets after moving native U6/U9/J2 footprints.
Native DRC reported 569 violations, 131 unconnected records, 34 shorts, and
28 crossings. The focused failures include collisions with SERVICE/REFCLK
geometry, pair crossings at the east-side ESD escape, and crossing/shorting
via fanout. It is rejected; the west-outboard ESD candidate is the next
dedicated-corridor experiment.

The first west-outboard live-pad route was run with J2 rotated to zero so its
MDI row faces the incoming corridor. Native DRC reports 458 violations, 137
unconnected records, five shorts, and four crossings. Focused failures are
local U6/U9 pad-field fanout and MagJack support-pad approach geometry. The
route is rejected, while the mechanically valid placement remains the basis
for an orientation/escape refinement.

An orientation sweep of the same west-outboard hand-routed class was also
run. ESD rotations 0 and 180 with J2 rotation 0 produced respectively 468/141/5/8
and 456/143/7/4 (total DRC/unconnected/shorts/crossings). Neither passes;
the remaining defects are concentrated in the ESD pad-field and MagJack
launch. This class is closed for now in favor of an obstacle-aware/reference
pad-escape authoring method.

Independent PCB review confirms the west-outboard native body placement is
mechanically plausible in 2D: U6 `(16.075,103.040)–(21.750,104.935)`, U9
`(24.475,103.040)–(29.925,104.935)`, and J2
`(6.025,133.740)–(23.975,157.298)` do not intersect J7. The recommended
implementation is all-F.Cu MDI from J7 through flow-through U6/U9 to the J2
PTH pads, with no signal vias at the USON fields and an explicit J2 no-go
envelope around CT, LED, shield, and NPTH features. The review also identifies
the trial width mismatch (0.13208 mm versus the native 0.200 mm minimum rule)
as an unresolved rule/impedance materialization issue.

The monotonic-order candidate was tested with U9 (TD3/TD2) left, U6
(TD1/TD0) right, both outside J7, and J2 rotated 180 degrees. Native DRC
reported 497 violations, 135 unconnected records, 15 shorts, and 17
crossings. It is rejected; endpoint ordering alone does not solve the USON
output fanout or EDAC launch. The next class is direct reuse of the CM5IO
serialized pad-escape geometry with board-context corridors re-authored.

The serialized CM5IO MDI transplant was run on a disposable Phase 24 copy.
Focused native metrics pass all four pair-skew bounds (0.547–0.829 mm), and
the new native connectivity audit passes J7 → U6/U9 → J2 for all eight nets;
its negative control removes J7.12's necessary track and fails as required.
Native full-board DRC reports 449 violations, 122 unconnected records, zero
track crossings, and one unrelated POWER_GND/BRIDGE_1V1 short. Therefore the
MDI geometry is conditionally retained, but the board candidate is not
promoted until the unrelated inherited debt, support nets, impedance rule,
and complete mechanical checks are closed.

## Current native support and return audit — 2026-09-05

The clean `ETHERNET.kicad_sch` contains only the authoritative J2/U6/U9
symbols and the `ETH_CT1..4`, LED, and shield labels. It does not contain CT
termination capacitors/resistors or LED-current resistors. CM5IO and EDAC
remain support/topology authorities, but PCB-only addition of those parts is
not promoted without schematic-level authority.

The current U5 layered candidate was rechecked with native connectivity and
the trace-removal negative control; both pass. Native DRC remains `201`
violations and `397` unconnected records, so full-board closure is still
open. A fresh J7-derived CM5-ground launch/plane experiment was rejected:
`264` violations, `397` unconnected records, four shorts, and one crossing.
No severity or connection was waived.

The corrected U5 pair sweep tested C44.2-C45.2 and C46.2-C47.2 independently
from the accepted C5/C6 base. Both produced native DRC `201` violations and
`396` unconnected records with no shorts or crossings, but neither reduced
the census: the missing relationship is the capacitor island to its regulator
return, not pair-to-pair continuity. They are not promoted.

The next adjacent-row probe, C14.2 to C15.2, was rejected by native DRC:
although it reduced the raw unconnected census to `395`, the straight join
shorted `POWER_GND` to the neighboring `12V_PROTECTED` C15.1 pad and raised
total violations to `203`. It is not promoted; capacitor orientation and
neighboring power pads must be included in the next return-island route.

The next single-pair POWER_GND repair was derived from the saved candidate's
actual C5/C6 pad centers. Native DRC reduced the unconnected census from
`397` to `396` with no new shorts, crossings, or total-violation increase;
the U5 native audit and its trace-removal negative control still pass. This
is accepted incremental progress, not full-board closure.

The U7 `BRIDGE_CFG` discriminator was rejected. A direct F.Cu escape shorted
U7's no-connect/power pad field; two ordinary-via B.Cu variants removed
shorts but created SATA crossings, and a local early-via variant removed
crossings but raised native DRC from `201` to `207` without reducing the
`396` open census. No CFG copper was promoted.

The next source-authority correction assigns U7 pads 52/53/54 from the
native schematic netlist to `BRIDGE_XI`, `BRIDGE_VSSOSC`, and `BRIDGE_XO`.
Native DRC on the RX-N-improved basis reports `394` unconnected records with
zero shorts/crossings. This is a required pad-ownership correction; clock
routes are still absent and the candidate is not yet promoted to closure.

The current storage repair class is the native U7 SATA RX-N pad-field stitch.
All five repeated U7 RX-N pads now connect through the saved PCB's actual
tracks/vias to U7.59/C33.2. Native DRC reports `201` total violations and
`391` unconnected records, with zero shorts/crossings; the five dangling-via
warnings are inherited and unchanged. U5 connectivity, its negative control,
and the authoritative-part audit remain passing.

The U7 endpoint audit then found pins 30 and 31 also omitted from the PCB net
ownership. Assigning U7.24/U7.30/U7.31 to `BRIDGE_3V3` and retaining the
XI/VSSOSC/XO assignments is source-authority-correct, but it exposes five
real unrouted endpoint relationships: native DRC is `201` violations and
`396` unconnected records with zero shorts/crossings. This is not a pass; it
changes the next routing task from guessed CFG/clock geometry to complete
U7 power/clock support routing.

The U7 `BRIDGE_3V3` pad-field dogleg is accepted. Native connectivity joins
U7.24/U7.30/U7.31 to TP5.1 while bypassing the intervening no-connect pads;
native DRC remains `201` total violations with zero shorts/crossings, and
unconnected records fall `396` to `394`.

The corrected-layer A* clock discriminator was rejected on the integrated
candidate. Its tightened source/pad obstacle model removed the prior XO
no-net-pad crossings, but native DRC found signal-via/ground-zone clearance
violations and raised total violations to `217`; shorts/crossings were zero.
The route is not promoted. Clock transitions must next be explicitly
zone/antipad-aware or remain on a validated F.Cu corridor.

Native CLI `--refill-zones --save-board` rechecked the same XI graph. On a
like-for-like refilled comparison it reduces opens `394` to `392` and keeps
shorts/crossings at zero, but raises total DRC `429` to `434` through five
real transition-via/clearance and dangling-track findings. The earlier
non-refilled `217` report is stale-zone evidence and is not promotion proof.

The new `phase24_u7_pad_net_authority_audit.py` passes on the corrected U7
candidate for all 17 schematic-owned U7 endpoints and fails on the prior
integrated baseline for the five omitted clock/3V3 pads. This is now a
regression gate for subsequent support routing; it derives assertions from
serialized pad net identity and supplies no connectivity edges.

The clock-support footprint audit found a second authoring defect: top-side
Y1/R23/C42/C43 footprints had their SMD copper pads serialized on B.Cu. A
disposable correction restores their pads to F.Cu and passes the U7
pad-authority audit with native DRC reporting no shorts/crossings. With the
real pad obstacles preserved, bounded A* finds no legal XI path to R23.1;
this route is not promoted and the next clock island must move or use a
separately reserved corridor.

The first moved outboard clock-island trial was rejected after native CLI
refill: it reduced the open census to `384`, but introduced nine real F.Cu
crossings between clock lanes and the existing `BRIDGE_SATA_TX_N` launch.
The placement is not promoted; the next candidate must reserve the SATA
corridor and separate clock layers before routing.

## Whole-board macro-floorplan discriminator — 2026-09-05

Local clock/SATA experiments are paused pending this review. The current
native-loaded integrated candidate is `PHASE24_U7_3V3_CURRENT_LOCAL.kicad_pcb`.
The review script and disposable placement-only boards are
`phase24_macro_floorplan_review.py`, `PHASE24_MACRO_*.kicad_pcb`, and
`PHASE24_MACRO_FLOORPLAN_REVIEW.md`. They use KiCad-transformed pad positions
from J7's carrier mating view; moved copper is explicitly not accepted.

Native source launches are: Ethernet centroid `(34.50,99.90)`, PCIe
`(69.60,101.50)`, USB3 `(70.04,105.30)`, and SERVICE `(66.96,99.30)` mm.
Current island centroid distances are approximately Ethernet `59.2` mm,
PCIe `81.2` mm, USB3/storage `67.6` mm, and SERVICE `22.0` mm. The current
PCIe endpoint J1 is the closest validated high-speed anchor and remains the
preferred frozen anchor. SERVICE is the only already-local interface.

The CM5-neighborhood candidate reduces Ethernet source-to-island centroid
distance to `5.1` mm and storage to `51.0` mm; the ETH/storage swap candidate
reduces Ethernet to `22.5` mm and storage to `52.6` mm. The current upper
Ethernet placement and mid-acreage storage/clock placement are therefore
materially nonlocal and compete for the PCIe/power/SATA corridors. These
candidate boards are placement topology probes only; no island has been
promoted and no downstream routing has been regenerated yet. The next gate
is consultant/reviewer selection of a coherent macro-floorplan, followed by
fresh routing and full affected-subsystem validation.

Consultant dispatch was attempted but the collaboration service reported its
thread limit; this is not treated as an engineering blocker. The selected
placement-only candidate is `PHASE24_MACRO_ETH_WEST_LOCAL_STORAGE`: Ethernet
ESD/support stays outside the native J7 body envelope beside the GBE launch,
the MagJack is on the west edge, the complete U7/J3/clock island moves to the
USB3-side acreage, and PCIe J1 plus SERVICE J4 remain unchanged. This is not
a routing pass; affected Ethernet and USB3/SATA/clock copper must be
regenerated together and then closed by native DRC/connectivity and geometry
checks.

## Selected-macro storage regeneration rejected — 2026-09-05

The first coordinated selected-macro USB3/SATA trial was built from native
pad coordinates and rejected by refilled native DRC: `363` total violations,
`43` true shorting-item findings, `7` track crossings, and `444` unconnected
items. The principal SATA failure is an authority/generator mismatch exposed
by the saved board: U7 pads 56/57/59/60 serialize as
`BRIDGE_SATA_TX_N/TX_P/RX_N/RX_P`, while J3 pads 1/2/3/4 serialize as distinct
`SATA_M2_TX_P/TX_N/RX_P/RX_N` nets. The trial connected across those identities,
so it is invalid and is not promoted. The selected placement remains the
working macro basis; next action is to resolve the schematic/native net
authority or explicit connection boundary, then regenerate SATA and USB3 with
correct net identity. No validation severity was changed.

The follow-on retry corrected the conceptual SATA boundary by routing through
C30/C31/C32/C33: bridge-side `BRIDGE_SATA_*` nets terminate on capacitor pad 2
and M.2-side `SATA_M2_*` nets begin on pad 1. It still fails as a route trial
(`347` native refilled violations, `46` shorting items, `5` crossings, `437`
unconnected items), primarily from unplanned lane crossings, J3 NPTH/launch
clearance, and inherited non-storage copper near the new corridor. It is
rejected, but the net-authority diagnosis is retained for the next generator.

The selected-macro Ethernet regeneration was separately tested from native
J7/U6/U9/J2 pad centers using the CM5IO mapping, then rejected by refilled
native DRC (`409` violations, `55` shorting items, `22` crossings, `433`
unconnected items). Adjacent J7/ESD pad-field escapes and west-edge launch
lanes collided with neighboring power/storage copper. This hand-authored
compact route is rejected; the next Ethernet attempt must adapt the official
CM5IO escape topology or use obstacle-aware routing.

The next Ethernet experiment adapted the validated rotated-west CM5IO escape
(`phase24_regen_selected_ethernet_cm5io.py`) to the selected macro placement.
It improved the native refilled result to `384` violations, `18` shorting
items, `10` crossings, and `425` unconnected items, but is still rejected.
The remaining failures are concrete: copied J7 exit vias intersect the other
F.Cu source corridors, west-edge MagJack approach lanes enter adjacent
through-hole pads, and one existing SERVICE route crosses a new B.Cu lane.
The official topology is therefore directionally useful but its coordinates
must be regenerated against the live board's actual pad/obstacle geometry.

The existing reviewer threads were polled twice without completed responses;
local native evidence remains authoritative and this orchestration condition
is not a design blocker. The next bounded class is Ethernet-local endpoint
repositioning that retains the official split-layer topology but changes the
MagJack/ESD spacing relative to the J7 and power-entry pad fields before
rerouting.

The required whole-board functional-island floorplan discriminator is complete.
Native transformed J7 launch coordinates were compared with Ethernet,
PCIe/V100, complete USB3-to-SATA storage, SERVICE USB2, power-entry, and
regulator islands. Large translations and the Ethernet/storage swap were tested
as disposable placement candidates. `ETH_WEST_LOCAL_STORAGE` remains the best
joint basis: Ethernet and storage become less remote while PCIe and SERVICE
anchors remain unchanged. No moved copper was accepted. Phase 24 remains open
for coherent affected-neighborhood regeneration; detailed open repair resumes
only after that regeneration is validated.

## Immutable-parent and clean-neighborhood discriminator — 2026-09-05

Following independent review, the exact selected macro parent was snapshotted
as `PHASE24_SELECTED_MACRO_PARENT_20260905.kicad_pcb`, SHA-256
`da8c9012ddedf5feac774d96c8110e0e0ab7fba2b8ae04e0423727be613f8701`.
Inherited-only native refill/DRC on that immutable parent reported 450 total
violations, 22 shorting items, 0 track crossings, and 449 unconnected items.

The disposable `phase24_clean_eth_overlay.py` then removed only invalidated
Ethernet, USB3/storage, and clock copper, moved the Ethernet endpoint set to
the exact CM5IO oracle geometry, and transplanted the unmodified oracle MDI
tracks. Native refill/DRC reported 387 total violations, 2 shorting items, 0
track crossings, and 416 unconnected items. Both shorts are the inherited
U7/C17 `POWER_GND` versus `BRIDGE_SATA_RX_N/RX_P` pad-field defect; no Ethernet
short or crossing was found in this controlled overlay.

This establishes the next repair boundary: use immutable parent hashes for
every comparison, clear affected functional-neighborhood copper coherently,
and regenerate from native pads. The prior transformed Ethernet reports are
not comparable unless their exact parent is recorded. Phase 24 remains open;
the overlay is not an acreage pass because support circuitry and board-wide
connectivity are still incomplete.

The clean overlay is retained as a CM5IO top-oracle Ethernet routing-development
candidate. Its saved-board native evidence has 0 Ethernet crossings, 0 Ethernet
shorts, and pair skew below 0.83 mm; the only two shorting items are inherited
U7/C17 storage pad debt. This is not a macro-floorplan ranking: the selected
`ETH_WEST_LOCAL_STORAGE` floorplan remains the placement-metric choice, and its
15-short/13-crossing result is classified as route implementation failure until
it receives a fair obstacle-aware development cycle. Ethernet center-tap/LED/
shield/return support and mechanical review remain open.

For the same immutable parent, the existing CM5IO-adapted selected-placement
route was regenerated fresh. Native DRC reported 384 total violations, 15
shorting items, 13 crossings, and 425 unconnected items, versus the parent's
22 shorts and 0 crossings. It is rejected. The new findings are localized to
the hard-coded local escape/endpoint lanes, SERVICE-via interference, and
MagJack pad-field ordering; the comparison is now valid because parent hash
and output artifact are recorded. Consultant review therefore closes the
report-integrity ambiguity but does not close Ethernet routing.

The subsequent Ethernet regeneration probes were also preserved as disposable
evidence. A naive rigid translation into north-west acreage reported 448 total
violations, 2 shorts, 8 crossings, and 433 unconnected items; the crossings
were caused by moving the CM5IO branch geometry independently of the J7 launch.
A branch-preserving transform reduced the result to 434 violations, 2 shorts,
6 crossings, and 425 unconnected items, but still failed on real Ethernet
pair crossings. Rigid rotations of the complete oracle likewise failed the
integrated occupancy test (`+30°`: 578 violations/34 shorts/10 crossings;
`+45°`: 615/62/11; `-30°`: 547/28; the `-45°` report was not completed).
These are rejected routing probes, not evidence against the CM5IO electrical
architecture or against the macro review. The next implementation must clear
invalidated Ethernet/storage copper as a coherent neighborhood and regenerate
against the selected placement, rather than transform the oracle through live
obstacles.

## Ethernet support-authority audit — 2026-09-05 (superseded by closure below)

`phase24_ethernet_support_authority_audit.py` confirms that the clean
`ETHERNET.kicad_sch` has no schematic-owned `CCT*`/`RCT*` support references.
`ETH_CT1..4`, the four LED nets, and `GBE_SHIELD` are dead-end labels at the
current connector-side authority. The official CM5IO child provides real
`470R` LED resistors but exposes center taps to its PoE header; the EDAC
authority supplies the PiSXMe termination requirement of four `22 nF / 100 V`
to `75 ohm` series branches and a `1 nF / 2 kV` shield/ground termination.

Receipt: `PHASE24_ETHERNET_SUPPORT_AUTHORITY_RECEIPT.md`.

Historical decision: `PHASE24_ETHERNET_SUPPORT_AUTHORITY = OPEN_SCHEMATIC_REPAIR_REQUIRED`.
This is a schematic-authority gap, not a macro-placement failure or Ethernet
architecture failure. PCB-only historical support aliases remain excluded;
the next step is native schematic repair, ERC/netlist/parity validation, then
coordinate-derived PCB support regeneration.

The audit also found that the child/root hierarchy exposes one bundled
`GBE_LED` contract while the connector has four local LED nets. That interface
must be resolved in the same schematic repair; no four-net CM5 LED mapping is
being inferred from the donor.

The disposable native support fixture now passes root ERC with zero errors and
the saved netlist contains the complete EDAC CT branch/common/shield topology
and 470 ohm LED series elements. The fixture now uses selected commodity MPNs
for the 0603/0402/1206 parts; passive authority is recorded separately, while
production hierarchy mapping and parity remain open at the time of this audit.

## Ethernet support-authority closure — 2026-09-05

The historical omission and bundled LED mismatch are now repaired in the
production hierarchy. Native netlist `phase24-production.xml` contains C48–C52
and R26–R31, all four CT branches, the shield capacitor, and the two official
CM5 LED mappings: J7 pad 15 through R31 and J7 pad 17 through R30. Native ERC
`PHASE24_PRODUCTION_AFTER_ETHERNET_SUPPORT-erc.rpt` reports `Errors 0`.

Decision: `PHASE24_ETHERNET_SUPPORT_AUTHORITY = CLOSED`. PCB-side materialization,
component parity, and routed acreage closure remain open downstream.

## Fresh whole-board macro-floorplan discriminator — 2026-09-05

Because the earlier review was anchored to the pre-correction baseline, a
fresh placement-only discriminator was run from the native-loaded
`PHASE24_CORRECTED_MACRO_PLACEMENT.kicad_pcb`. It maps the actual transformed
J7 carrier-mating pad groups and reviews Ethernet, PCIe/V100, complete
USB3→U7→SATA→J3 plus clock support, SERVICE USB2, power/protection, and
regulator regions. The detailed evidence is
`PHASE24_WHOLE_BOARD_MACRO_REVIEW_20260905.md` and the reproducible generator
is `phase24_whole_board_macro_review_v2.py`.

The current corrected basis has source-to-island centroid distances of
Ethernet `32.7 mm`, USB3/storage `58.5 mm`, PCIe `81.2 mm`, and SERVICE
`22.0 mm`. Its topology-only straight source-to-first-endpoint screen found
12 apparent Ethernet crossings and no USB3 first-endpoint crossings. It does
not use existing copper or mature-board DRC for ranking.

The review generated five disposable macro candidates, including an explicit
Ethernet/storage swap, a separated south Ethernet/north storage arrangement,
and a PCIe exchange test. The CM5-neighborhood candidate reduced Ethernet to
`5.1 mm` and storage to `51.0 mm`, but native-transformed body screening found
9 external overlaps including J7/J4/regulator conflicts and its apparent
Ethernet crossing count rose to 23. The outboard and swap candidates also
retain external conflicts. The PCIe exchange increases the PCIe distance to
`119.0 mm` without a compensating global win.

Decision: `MACRO_FLOORPLAN_DISCRIMINATOR = COMPLETE` and
`SELECTED_TOPOLOGY = CURRENT_CORRECTED`. This is a topology decision, not a
routing pass. Existing failed routes remain classified as
`ROUTE IMPLEMENTATION FAILURE`; no candidate is rejected merely because a
first-pass generated route has immature DRC. Detailed Phase 24 repair may
resume only as coherent functional-neighborhood regeneration from this
selected basis. Phase 25/26 remain unopened.

## Selected-basis local Ethernet escape probe — 2026-09-05

The first post-discriminator routing probe tested a bounded U6 orientation
repair. U6 was rotated from `-90°` to `+90°` so its native pad order matches
the right-side J7 source-lane order; package, nets, placement region, and
electrical topology were unchanged. The focused disposable artifact is
`PHASE24_ETHERNET_LOCAL_ESCAPE_PROBE.kicad_pcb`, generated by
`phase24_ethernet_local_escape_probe.py`.

Native refilled DRC still reports `218` violations and `438` unconnected
items, including real Ethernet pad-field shorts and crossings. This is
classified as `ROUTE IMPLEMENTATION_FAILURE`: direct single-layer
source-to-ESD segments converge into adjacent SMD pads and cannot serve as
the accepted escape geometry. It is not evidence against `CURRENT_CORRECTED`
as a macro floorplan and does not justify moving any non-Ethernet island.

The next authorized routing-development class is the official CM5IO-style
split-layer escape: controlled F.Cu/B.Cu assignments, ordinary through-vias
outside J7/ESD pads, and native pad-field-aware dogbones, followed by the
complete ESD-to-MagJack launch. No detailed clock/SATA repair or Phase 25/26
work is being started from this failed probe.

## Official CM5IO topology transplant discriminator — 2026-09-05

As a separate routing-development oracle, the 189 MDI track/via items from
the saved official CM5IO Ethernet implementation were transplanted onto the
corrected acreage board using native net identities. The generated artifact is
`PHASE24_OFFICIAL_ETH_TRANSPLANT_CORRECTED_BASIS.kicad_pcb`, with reproducible
source `phase24_official_eth_transplant_corrected_basis.py` and native report
`PHASE24_OFFICIAL_ETH_TRANSPLANT_CORRECTED_BASIS-drc.rpt`.

Native DRC reports `367` total violations and `426` unconnected items, but
zero `shorting_items` and zero `tracks_crossing`. The five dangling vias are
inherited `CORE_CM5/CM5_5V` power vias at `(79.65,158.00)`, `(89.50,158.00)`,
`(85.50,158.00)`, `(80.50,167.00)`, and `(68.50,162.00)`; they are outside
the transplanted Ethernet MDI block. The unconnected items and unrelated
clearance/width findings are inherited acreage debt, so this is not an
integrated pass.

This controlled result is positive routing evidence: the official CM5IO MDI
topology can be represented natively without pair shorts or crossings on the
live board basis. The earlier local failures are therefore retained as
`ROUTE_IMPLEMENTATION_FAILURE`, specifically local escape/placement geometry
and generator handling, not as evidence that the selected macro floorplan or
Ethernet architecture is impossible. The next attempt must retain the
official route topology while regenerating its source escape against native
J7/U6/U9 pad fields; Phase 24 remains open.

## ESD vertical-pad-field escape probe — 2026-09-05

The next disposable probe oriented both local TPD4EUSB30 footprints at `0°`
and remapped only the symmetric protection channels so each four-channel
group presents a vertical monotonic order. This preserved the selected
Ethernet package/topology and changed no schematic net identity. Native
refilled DRC still reports `288` violations and `438` unconnected items,
including real Ethernet crossings and shorts at the converging package
entrances.

This is again `ROUTE_IMPLEMENTATION_FAILURE`, not
`MACRO-PLACEMENT_FAILURE`: monotonic endpoint order alone does not provide
the required pad-field clearance. The next valid class must add a wider
staging corridor and controlled split-layer transitions outside the J7/ESD
fields, or make a small Ethernet-local translation to create that corridor.

## Wider Ethernet-local staging probe — 2026-09-05

As the bounded local-placement follow-up, U6/U9 were moved coherently to
`(12,112)` and `(20,112)` and retained the vertical `0°` pad-field
orientation. J7, J2, storage, PCIe, power, and all logical net identities
were unchanged. The disposable output and native report retain the same
artifact names `PHASE24_ETHERNET_LOCAL_ESCAPE_PROBE.kicad_pcb` and
`PHASE24_ETHERNET_LOCAL_ESCAPE_PROBE-drc.rpt`.

Native refilled DRC again reports `288` total violations and `438`
unconnected items, with real Ethernet pad-field shorts/crossings. The result
does not improve the direct single-layer class and is classified as
`ROUTE_IMPLEMENTATION_FAILURE`. Two materially different direct-F.Cu
orientations plus this wider local staging move have now been exhausted;
further progress requires the official CM5IO-style staged split-layer escape,
ordinary through-vias outside the dense pad fields, and connector launch
regeneration.

## Hand-authored staged split-layer probe — 2026-09-05

The first hand-authored split-layer source-escape probe used native J7/U6/U9
pad identities, F.Cu departures, B.Cu staged corridors, and ordinary
through-vias outside the nominal pad fields. Native refilled DRC rejected the
probe with `317` violations and `456` unconnected items, including real
Ethernet shorts/crossings and dangling transitions. The disposable evidence
is `PHASE24_ETHERNET_STAGED_SOURCE_ESCAPE.kicad_pcb` with report
`PHASE24_ETHERNET_STAGED_SOURCE_ESCAPE-drc.rpt`.

This is `ROUTE_IMPLEMENTATION_FAILURE`: the proposed via/waypoint geometry
did not serialize as connected copper and the corridor was not pad-field
safe. It is not a macro-placement conclusion. The successful official
CM5IO transplant remains the route oracle; the next implementation must
derive its branch topology and transition ownership from that saved native
route rather than inventing another coordinate set.

## Official-placement Ethernet support materialization — 2026-09-05

The official MDI transplant was extended with the 11 production schematic-
owned Ethernet support footprints using `phase24_materialize_official_eth_support.py`:
C48–C52 and R26–R31. Native saved-board inspection confirms every support pad
has the intended CT, branch, common, shield, or LED net and is assigned to
B.Cu for the pending support route. J2 pads 11–20 and J7 LED pads 15/17 were
also reconciled to the production net contract.

The materialized candidate is `PHASE24_OFFICIAL_ETH_SUPPORT_MATERIALIZED.kicad_pcb`.
Native refilled DRC reports `378` inherited/unrouted violations and `443`
unconnected items, with no `shorting_items`, `tracks_crossing`, or footprint
mapping errors. This is a materialization boundary PASS, not a routed Ethernet
or acreage pass. Next action is native-pad-derived CT/LED/shield support
routing on this official-placement oracle, followed by comparison against the
selected corrected macro.

## Official-placement CT support route probe — 2026-09-05

The first support-copper attempt used the official-placement materialized
candidate, actual J2 CT pad locations, B.Cu staging lanes, local 75-ohm branch
connections, and one deliberate common bus. Native refilled DRC rejected the
child with `419` violations, `16` shorting items, `15` crossings, `5` inherited
power dangling vias, and `432` unconnected items. The parent materialization
had zero shorting/crossing records, so these new defects are attributable to
the hand-authored CT fanout and common-bus geometry.

This remains `ROUTE_IMPLEMENTATION_FAILURE`; the official MDI placement and
support footprint/net materialization remain valid. The next support attempt
must use obstacle-aware/topology-derived branch routing and preserve the
parent/child native DRC comparison.

## Complete CM5IO Ethernet fixture oracle — 2026-09-05

The existing CM5IO transplant authoring path was rerun from the archived
official PCB with `PISXME_DIRECT_J7=1 PISXME_CT_TIES=1`. The resulting saved
fixture contains the complete 189-item official MDI route, four CT capacitor
and 75-ohm branches, common termination, shield return, ESD ground treatment,
and native J7/J2/U6/U9 mappings.

Native refilled DRC reports `0` unconnected items, `0` shorting items,
`0` track crossings, `0` dangling vias, and `0` footprint errors. The report
contains 238 remaining clearance/width/edge warnings from the disposable
fixture rule environment; these are not connectivity failures and are not
being waived for the acreage board. This is the authoritative complete
Ethernet implementation oracle. Its exact branch/support geometry is now the
source for adapting the official placement candidate; local hand-authored
support routes remain rejected.

Repository regression checks were then run directly against the saved complete
fixture. `test_cm5io_transplant_fixture.py` passes all eight MDI mappings and
reports pair length differences of `0.680`, `0.829`, `0.547`, and `0.688 mm`
for TD0–TD3. `test_cm5io_transplant_native_drc.py` also passes, finding no
shorts, crossings, dangling vias, unconnected pads, or footprint errors. This
fixture gate is closed; it does not substitute for the integrated-acreage
gate.

## Official-placement LED support route probe — 2026-09-05

R30/R31 were added with the production `ETH_LEDY`/`ETH_LEDG` source nets,
physical EDAC cathode aliases, and ordinary B.Cu routes on a child of the
clean official MDI/CT support oracle. Native refilled DRC reports `214`
violations and `428` unconnected items, including one new short and five new
crossings. The parent had zero shorting/crossing records, so this child is
rejected as `ROUTE_IMPLEMENTATION_FAILURE`.

The new findings are localized to the hand-authored LED corridors: CT3/CT1
intersections, the J2 shield barrel field, and the two source-launch vias.
The production LED net mapping and resistor materialization remain valid;
the next attempt must use dedicated staged LED lanes or a support-local
placement change while preserving the clean MDI/CT parent.

## Official-placement complete support-route transplant — 2026-09-05

The complete CM5IO fixture support geometry was transplanted onto the
width-corrected official-placement MDI candidate by
`phase24_transplant_official_support_routes.py`. The operation recreates the
production C48–C52/R26–R29 support footprints at the exact oracle positions,
maps the saved native support tracks to the hierarchical production net
names, and legalizes the fixture's disposable 0.20 mm via drills to ordinary
0.30 mm through vias. MDI copper was not regenerated or altered.

The resulting `PHASE24_OFFICIAL_ETH_FULL_SUPPORT_ROUTE.kicad_pcb` has native
DRC counts of `197` total inherited/unrelated violations and `426`
unconnected acreage items, but zero `shorting_items`, zero `tracks_crossing`,
zero `track_width` violations, and zero `drill_out_of_range` findings. The
five dangling vias are inherited power vias outside the Ethernet block.

The new `phase24_official_eth_full_connectivity_audit.py` derives connectivity
from saved pads/tracks/vias/zones and passes all eight MDI nets, four CT nets,
four 75-ohm branches, common termination, and shield membership. Its
negative control removes one real CT1 track and fails as required. This closes
the complete official support-route oracle gate; it remains an adaptation
candidate, not an integrated-acreage pass. R30/R31 LED series parts and their
production routing are still required before final Ethernet promotion.

## Official-placement MDI width-corrected discriminator — 2026-09-05

Following the independent review, the official 189-item MDI geometry was
regenerated onto the disposable official endpoint placement with every track
width clamped to the board’s required `0.13208 mm` minimum. The focused native
Ethernet connectivity audit passes all eight J7→ESD→J2 net memberships.

Native refilled DRC reports `178` total inherited/unrelated violations and
`426` unconnected acreage items, with zero `shorting_items`, zero
`tracks_crossing`, zero `track_width` violations, and only five inherited
`CORE_CM5/CM5_5V` dangling vias outside the Ethernet block. The repository
fixture regression requiring `0.127 mm` is intentionally not used for this
candidate; its width assertion is specific to the disposable official
fixture, while this candidate obeys the live board rule.

This proves the official route can be adapted to legal board geometry without
Ethernet pair crossings or shorts. It remains a routing oracle/disposable
alternative: `CURRENT_CORRECTED` stays selected for board-level topology
because it is much closer to J7 and has better connector-edge access. Full
support parity, connector mechanics, and integrated-acreage closure remain
open.

## Official-placement LED mixed-side corridor probe — 2026-09-05

The next disposable LED experiment moved R30/R31 to a source-adjacent
top-side island, escaped ETH_LEDY/ETH_LEDG from J7 on separate F.Cu lanes,
and used separate B.Cu cathode corridors with ordinary F.Cu/B.Cu transitions.
This was a valid implementation experiment; it did not modify the validated
MDI, CT, common-termination, or shield copper in the parent.

Native refilled DRC reported 270 total violations and 428 inherited
unconnected items. The child introduced 20 shorting records and 21 crossing
records, including source-launch contact with adjacent J7 pads, LED corridor
intersections with inherited CM5/service/MDI copper, and cathode interaction
with the J2 power/shield/CT field. It is rejected as
`ROUTE_IMPLEMENTATION_FAILURE`, not as evidence against the official Ethernet
placement or electrical topology. The next experiment must use the actual
reference LED lane geometry or a dedicated low-speed support corridor with
pad-field-aware dogbones; no promotion to the acreage board has occurred.

## J2-west LED resistor staging probe — 2026-09-05

Following the consultant review, a disposable child placed R30/R31 at the
west side of J2 and used explicit pad-aware source escapes, two ordinary
through-via transitions, and separate B.Cu trunk seeds toward the CM5 launch.
The experiment preserved the validated official MDI/CT/common/shield parent.

Native refilled DRC reported 264 total violations and 428 unconnected items.
The child added 8 shorting records and 39 crossing records, primarily where
the resistor terminal lanes entered the official MDI escape corridor and
where the two J2 cathode exits met existing CT geometry. It is rejected as
`ROUTE_IMPLEMENTATION_FAILURE`; the official Ethernet placement remains
structurally unrefuted. Consultant review recommends either a fully
source-local J7-west LED island or an obstacle-aware low-speed corridor
generator with reserved tracks, rather than further direct dogbones through
the MDI field.
## J7-west source-local LED island probe — 2026-09-05

The second consultant-recommended class placed staggered R30/R31 immediately
west of J7, kept source traces on F.Cu, and used open left-edge B.Cu lanes for
the J2 cathode trunks with separate ordinary through-vias. This preserved the
official MDI/CT/common/shield parent and did not touch differential copper.

Native refilled DRC reported 241 total violations and 426 inherited
unconnected items. The child still introduced 13 shorting records and 15
crossing records, including J2 launch-field/pad-barrel interactions and
source-local terminal/via interactions. It is rejected as
`ROUTE_IMPLEMENTATION_FAILURE`. The measured result improves over the prior
J2-west attempt but does not yet constitute an Ethernet or Phase 24 pass; an
obstacle-aware router or a mechanically separated LED-support placement is
still required.

## J7-west rotated LED island probe — 2026-09-05

A third disposable child rotated and staggered the source-local R30/R31
resistors, used separate F.Cu terminal escapes, and dogboned J2.16/J2.18 on
F.Cu before entering two left-edge B.Cu trunks. The authoritative MDI, CT,
common-termination, and shield parent remained unchanged.

Native refilled DRC reported 258 total violations and 430 unconnected items,
with 20 shorting records and 15 crossing records. The added unconnected
items show that the fixed coordinate assumptions for the rotated terminal/via
transitions were not correct; this is rejected as
`ROUTE_IMPLEMENTATION_FAILURE`. No Ethernet architecture or official
placement conclusion is changed. Further work must first derive transformed
pad coordinates from the saved native footprint objects and use an
obstacle-aware route search, rather than continuing hand-authored coordinate
variants.

## Native obstacle-search LED probe — 2026-09-05

`phase24_led_obstacle_search_probe.py` was added as the first generator that
derives transformed endpoint coordinates from native pads and searches both
permitted copper layers while retaining saved tracks and pads as obstacles.
It completed both J7→R30→J2 and J7→R31→J2 paths with 426 inherited
unconnected items and no route-search failure.

Native DRC still reports 255 violations, including 4 shorting records and
16 crossing records. The remaining failures are concentrated in the dense
J7/J2 pad and mounting-hole fields: the search endpoint halo is not yet using
the full native hole-clearance envelope. This is a
`ROUTE_IMPLEMENTATION_FAILURE`, not a macro-placement failure. The next
revision will inflate NPTH/PTH obstacles from native hole and pad geometry
and preserve explicit pad-field dogbones before evaluating the route.

## Native obstacle-search LED trunk separation — 2026-09-05

The search was tightened to use native-sized pad/hole obstacles, reserve every
emitted route in the occupancy map, and force the long cathode trunks to B.Cu
after explicit F.Cu dogbones and ordinary vias. The resulting disposable
child has 426 unconnected items, zero shorting records, zero track-crossing
records, and no forbidden plane-layer signals. Native DRC retains 199
inherited/non-LED warnings; the two clearance records are inherited CM5
reference-clock findings, while LED-specific failures are absent.

`phase24_led_astar_connectivity_audit.py` passes the four LED net endpoint
assertions using KiCad `BuildConnectivity`; its negative control removes a
real ETH_LEDY trace and fails as required. This is the first LED-support
candidate that passes the focused connectivity/copper crossing gate, but it
remains a disposable official-placement oracle until native mechanical,
component-parity, and integrated-acreage checks are complete.

## Focused LED route promotion candidate — 2026-09-05

The obstacle-search generator was tightened further: native pad/hole
clearances are inflated in the occupancy map, all emitted direct segments are
reserved for subsequent searches, and long cathode trunks are forced to B.Cu
with explicit F.Cu dogbones and ordinary vias. On the saved
`PHASE24_OFFICIAL_ETH_LED_ASTAR_PROBE.kicad_pcb`, native refilled DRC retains
426 inherited unconnected items but reports zero `shorting_items` and zero
`tracks_crossing` records. The focused MDI/CT/common/shield and LED
BuildConnectivity audits both pass, including real-trace negative controls.

This is a focused Ethernet support pass, not a Phase 24 board pass. The
candidate still requires integrated-board mechanical, schematic/PCB parity,
power/return, DRC inheritance review, and promotion validation before the
official Ethernet implementation can replace the current acreage island.

## Whole-board functional-island macro-floorplan discriminator — 2026-09-05

Per the steering correction, detailed Phase 24 routing experiments were
paused and the live integrated candidate
`PHASE24_CM5_GROUND_RIGHT_SAME_ROWS.kicad_pcb` was re-read with KiCad 10.0.5.
The native carrier-mating J7 launch centroids are Ethernet `(34.50,99.90)`,
PCIe `(69.60,101.50)`, USB3 `(70.04,105.30)`, and SERVICE `(66.96,99.30)`.
The live endpoint centroids are Ethernet `(77.76,59.56)`, storage
`(130.65,131.04)`, PCIe `(150,90)`, and SERVICE `(46.88,100)`.

The fresh placement-only discriminator
`phase24_macro_floorplan_review_fresh.py` generated five disposable native
candidates. It intentionally excludes existing copper and mature DRC from
ranking. The coherent Ethernet migration candidate reduces Ethernet
same-net ratsnest from `443.9 mm` to `97.4 mm` and Euclidean source-to-island
distance from `59.2 mm` to `32.7 mm`, with no moved-body overlap in the
conservative screen. It is materialized as
`PHASE24_SELECTED_ETH_LOCAL_MACRO.kicad_pcb` with only Ethernet copper
removed, so it is a routing base, not a claimed routed pass.

The combined storage-local candidates reduce USB3 same-net ratsnest from
`231.2 mm` to `69.1 mm`, but the tested placements introduce M.2/body or
support overlap screens. They are rejected as placement candidates pending a
new mechanically clean storage arrangement, not because of immature routing.
PCIe/J1, SERVICE/J4/U8, power input, and regulator cores remain unmoved.
The external consultant dispatch was unavailable at the platform thread
limit; the available independent board reviewers were used instead. One
review independently confirmed the native pad map and the distinction
between the corrected placement basis and the older integrated artifact.

`MACRO_FLOORPLAN_DISCRIMINATOR = COMPLETE`
`SELECTED_MACRO_BASIS = PHASE24_CORRECTED_MACRO_PLACEMENT`
`PHASE24 = OPEN; DETAILED ROUTING PAUSED UNTIL SELECTED COHERENT-NEIGHBORHOOD REGENERATION`

### Macro-basis reconciliation

The fresh review intentionally began from the older integrated ancestor to
expose the native CM5-to-island topology. The single-Ethernet migration
`PHASE24_SELECTED_ETH_LOCAL_MACRO.kicad_pcb` is retained as a diagnostic, not
as the final selection. Independent native review reconciled the two current
file meanings and confirms that `PHASE24_CORRECTED_MACRO_PLACEMENT.kicad_pcb`
(SHA-256 `de316ff211675b514bd85d9064ccd4defd3486b73968033c2b4c0c4ce95c2f4a`)
is the superior coherent basis: Ethernet-west plus complete storage-mid,
approximately `97.4 / 145.1 mm` Ethernet/storage same-net topology, no newly
introduced conservative body-bbox overlap, and unchanged PCIe, SERVICE,
power, and regulator anchors. This does not use mature DRC as floorplan
evidence. Detailed routing resumes only from this corrected basis, with
affected Ethernet, USB3/SATA, and clock copper regenerated together.

### First matched Ethernet regeneration from selected macro — 2026-09-05

The native-pad Ethernet generator was run against the selected
`PHASE24_CORRECTED_MACRO_PLACEMENT.kicad_pcb`, producing
`PHASE24_SELECTED_MACRO_ETH_MDI_REGEN.kicad_pcb`. It completed all eight
source→ESD→MagJack searches, but native refilled DRC reports 497 violations
with real Ethernet shorting and crossing records. This is recorded as
`ROUTE_IMPLEMENTATION_FAILURE`: the generator's sequential occupancy/escape
model is not yet a valid implementation for the selected placement. It is
not evidence against the macro-floorplan. The candidate is preserved with
its native DRC receipt for the next obstacle-aware/reference-topology
regeneration cycle; no severity, layer policy, or connectivity assertion was
relaxed.

### Ethernet router endpoint-model correction probe — 2026-09-05

The generator was corrected in two generic ways: duplicate same-net ESD pads
are now attached independently to the selected terminal, and the search no
longer clears a broad five-cell halo around terminal centers. The first
change reduced the disposable candidate from 497 to 473 DRC violations but
still left real shorts/crossings. The second change correctly preserved
neighboring native pads, but the conservative occupancy model then found no
legal path from the ESD field to the MagJack entry. This remains
`ROUTE_IMPLEMENTATION_FAILURE` and identifies the next required fix:
pad-shape-aware terminal escape, not another macro-floorplan comparison.

### Ethernet pad-field and via-clearance routing cycle — 2026-09-05

The selected macro Ethernet router was further corrected to use native
rectangular pad dimensions, independently attach duplicate ESD pads, reserve
0.45 mm-via clearance from all native pads, and reserve emitted via fields.
V5 reduced the route to zero track crossings with one localized short; V6
reduced it to two localized shorts and zero crossings. The stricter V8
via-specific occupancy correctly refused a later path, and all-F / reverse
ordering trials likewise dead-ended before completion. These are
`ROUTE_IMPLEMENTATION_FAILURE` results from the current global-search model,
not evidence that the selected coherent macro placement is impossible. No
layer, clearance, severity, or connectivity gate was relaxed.

### Ethernet pad-aware escape refinement — 2026-09-05

The router now uses a separate native-pad-derived via occupancy map and
supports controlled all-F.Cu and reverse-order experiments. V6 produced zero
track crossings with two localized ESD/J7 shorts; V8 correctly rejected a
path under strict via clearance, and V9/V10 confirmed that layer assignment
or ordering alone does not solve the current terminal escape. These remain
route implementation results. The next implementation class is an explicit
CM5IO-derived pad-field departure template with reserved lanes, followed by
full native DRC/connectivity validation.

### Native ESD departure-cell audit — 2026-09-05

`phase24_native_escape_cell_audit.py` inspected all sixteen U6/U9 Ethernet
signal pads on the selected macro using transformed native dimensions. At a
0.25 mm cardinal grid step, every immediate departure cell is blocked by the
pad-field clearance envelope. This does not prove the package is unroutable;
it proves the next router must model continuous pad-edge dogbones and
directional escape corridors rather than treating pad centers as free grid
nodes. The audit is preserved as a generator requirement and no routing gate
was relaxed.

### CM5IO source-escape template trial — 2026-09-05

The existing CM5IO-derived source escape waypoint pattern was regenerated
from native J7 pads on the selected corrected macro. The disposable source
template produced 221 native DRC violations, including source-pair
crossings, shorts into SERVICE/power geometry, five dangling vias inherited
from the template basis, and 454 unconnected pads because only source escapes
were authored. It is rejected as `ROUTE_IMPLEMENTATION_FAILURE`: the old
waypoints cannot be transplanted unchanged into this local Ethernet
placement. The evidence narrows the next template to new local directional
lanes with explicit obstacle ownership.

### Directional ESD corridor refinement — 2026-09-05

The native escape audit was extended from the immediate cell to a 2.0 mm
cardinal dogbone scan. Valid N/S package-end departure seeds exist for every
U6/U9 signal pad; the earlier “none” result was only an immediate-cell
screen, not a package impossibility. These native seeds will drive the next
explicit route template and keep `ROUTE_IMPLEMENTATION_FAILURE` distinct from
`MACRO-PLACEMENT FAILURE`.

### Explicit top/bottom ESD dogbone routing — 2026-09-05

The router was changed to approach each ESD net at its upper native pad and
depart from its lower native pad using 0.75 mm dogbones. V11 completed all
eight searches and native DRC reported zero `shorting_items` and zero
`tracks_crossing` records, but the real connectivity audit found the J2
endpoint open. V12 also corrected the generic post-via emitter to begin the
next-layer segment at the serialized via; native DRC/connectivity remained
unchanged, isolating the remaining defect to the saved ESD-to-MagJack leg.
No candidate was promoted.

### Ethernet MDI focused regeneration pass — 2026-09-05

After snapping every routed seed/entry to the 0.25 mm search grid and
joining the native duplicate ESD pads from the upper approach terminal, V15
completed all eight selected-macro MDI routes. Native refilled DRC reports
`0` `shorting_items` and `0` `tracks_crossing`; the focused
`phase24_ethernet_native_connectivity_audit.py` also passes all J7→U6/U9→J2
net assertions. The report still contains 5 inherited dangling vias and 430
unconnected items from the incomplete selected-macro/full-board basis, so
this is a focused Ethernet MDI pass, not Phase 24 closure or promotion.

### Whole-board macro-floorplan discriminator — steering correction — 2026-09-05

The required whole-board functional-island review is complete before further
clock/SATA corridor repair. Native transformed CM5 carrier-mating pads were
mapped for Ethernet `(34.50,99.90)`, PCIe `(69.60,101.50)`, storage USB3
`(70.04,105.30)`, and SERVICE `(66.96,99.30)`; Ethernet, PCIe/V100,
complete storage, SERVICE, power/protection, and regulator islands were
compared using topology-only metrics and mechanical screening. Five
disposable macro candidates were generated, including explicit Ethernet and
storage local migrations and an island-swap candidate.

The comparison intentionally separates `A: IS THE FLOORPLAN BETTER?` from
`B: HAS THIS FLOORPLAN BEEN ROUTED WELL YET?`. Historical acreage DRC and
connectivity maturity were excluded from ranking. The selected basis remains
`PHASE24_CORRECTED_MACRO_PLACEMENT.kicad_pcb`: coherent Ethernet-west plus
storage-mid, with PCIe/SERVICE/power/regulator anchors retained. The new
candidate's early route defects remain `ROUTE IMPLEMENTATION FAILURE` unless
a valid routing-development cycle demonstrates a structural obstruction.

The temporary local-J2 Ethernet support translation was checked separately:
the full CM5IO MDI/CT/common/shield native connectivity audit passes and its
real-trace negative control fails as expected. This is route-development
evidence only; the incomplete selected macro still has inherited/open-board
DRC findings, so no Phase 24 closure is claimed. Further local Ethernet or
clock/SATA routing experiments are paused until the macro review decision is
accepted as the active basis.

### Current-basis topology metrics reconciliation — 2026-09-05

The independent review identified that the earlier candidate table was based
on an older integrated ancestor. That gap is closed by
`PHASE24_CURRENT_MACRO_TOPOLOGY_METRICS_20260905.md`, generated from a native
load of `PHASE24_SELECTED_MACRO_ETH_SUPPORT_V15_LOCAL.kicad_pcb`. It includes
the complete translated Ethernet support island and the complete storage
bridge/M.2/clock/support island. The selected basis measures Ethernet
97.45 mm same-net topology and storage USB3-source 145.11 mm same-net
topology, with source-to-island centroid distances of 35.45 mm and 57.10 mm.

This reconciliation strengthens the floorplan decision only; it does not
promote the incomplete routed candidate. `CURRENT_MACRO_TOPOLOGY_METRICS =
COMPLETE`, while native full-board electrical, return, mechanical, DFM, and
route-quality gates remain open.

### Coordinated-neighborhood route-development cycle — 2026-09-05

After the macro discriminator and direct-current topology reconciliation, a
fair disposable route-development cycle was run on the selected basis. The
CM5IO MDI/CT/common/shield connectivity audit passes on the local-J2 support
candidate, and the LED support path passes its native connectivity audit with
the real-trace negative control. These focused connectivity results do not
override native DRC.

The local LED placement trials were rejected as
`ROUTE_IMPLEMENTATION_FAILURE`: native DRC showed shorts/crossings where the
support block and J7 escape field competed. The shifted support-block trial
also increased native unconnected findings. A first selected-storage
regeneration was separately rejected as `ROUTE_IMPLEMENTATION_FAILURE`:
native DRC reported 67 shorts and 37 track crossings, including SATA-pair
corridor weaving and an invalid no-net U7 pad landing. These experiments are
preserved as evidence, not compared against the mature historical board and
not used to reject the macro placement.

The selected macro remains the active basis. The next implementation step is
a native-pad/net-aware coordinated storage generator that clears the J7/U7
fields and assigns separated SATA pair corridors; no Phase 24 closure, Phase
25 freeze, or Phase 26 compression has begun.

### Storage generator pad-authority correction — 2026-09-05

The first storage regeneration exposed a generic authoring defect: its broad
serialized cleanup removed valid U7 pads 6/7/9 because it assumed all pads
5–12 were stale donor fields. That cleanup was removed. A rerun from the
passing V15 MDI parent preserves the saved U7 pad/net assignments and no
longer produces the false no-net U7 USB3/SATA landing class.

The corrected north-escape trial remains unpromoted. Native DRC reports 5
shorts and 8 track crossings, principally among the SATA bridge/socket
corridors and one inherited PCIe-vs-storage corridor conflict. This is still
`ROUTE_IMPLEMENTATION_FAILURE`, not `MACRO-PLACEMENT FAILURE`; the selected
macro has received a materially different, native-pad-authoritative routing
cycle and remains the active basis for the next lane-ordering repair.

### Storage layer-separated socket-launch trial — 2026-09-05

The storage authoring path was extended with a native north escape for the
saved U7 rotation, explicit USB3 TX_P final pad-field avoidance, and a
layer-separated SATA socket launch. The best disposable result reduced the
isolated V15-parent candidate to 4 native shorts and 8 track crossings, with
the earlier broad U7 no-net landing defect removed. It remains
`ROUTE_IMPLEMENTATION_FAILURE`: the remaining records identify SATA
bridge-side escape ordering, socket-side pair ordering, and one USB3/clock
clearance interaction. The candidate is preserved but not promoted, and the
selected macro is unchanged.

### Storage U7 rotation and outboard translation trials — 2026-09-05

Two additional coherent storage experiments were run after the native
pad-authority correction. U7 rotation-270 reduced apparent crossings but
introduced bridge/USB3 pad-field shorts and was rejected. A farther-out
U7/J3 translation increased source/inter-island crossings and collided with
the frozen PCIe and clock corridors; it was also rejected. Both are
`ROUTE_IMPLEMENTATION_FAILURE` results from the current route templates,
not macro-placement conclusions. The corrected Ethernet-west/storage-mid
basis remains selected pending a better native obstacle-aware SATA escape.

### Storage native lane-order refinement — 2026-09-05

The coordinated storage generator now preserves all saved U7 pad/net fields,
supports a native north escape from the SATA edge, avoids the USB3 TX_P
landing through the opposite SATA pad field, and can test a separate
layer-separated M.2 socket launch. The best candidate from this cycle still
reports 4 native shorts and 8 crossings; the records are localized to SATA
bridge/socket ordering and one USB3/clock interaction. It is rejected as
`ROUTE_IMPLEMENTATION_FAILURE`, while the selected macro remains unchanged.

### Native-pad obstacle-aware SATA A* trial — 2026-09-05

The disposable SATA router was corrected to use KiCad's actual pad position,
size, drill, layer set, and saved net identity. Its occupancy map now retains
all U7, coupling-capacitor, and J3 pads as obstacles; only the active segment's
source/target halos are cleared, and those edits are local to the segment. The
trial also removes only inherited BRIDGE_SATA_/SATA_M2_ copper before emitting
new native tracks and ordinary through-vias, leaving USB3, PCIe, power, and
unrelated copper intact.

Native DRC on
`PHASE24_SELECTED_MACRO_SATA_ASTAR_NATIVE.kicad_pcb` reports zero
`shorting_items` and zero SATA net shorts; four localized track-crossing
records remain at the RX socket launch. The board still reports 430
unconnected items because this is a focused SATA trial on an incomplete
acreage ancestor, and 18 track-dangling records include the new A* terminals.
It is therefore rejected as `ROUTE_IMPLEMENTATION_FAILURE`, but it is a
materially improved native-pad route-development baseline. Remaining work is
pair-aware RX launch separation and full USB3/SATA integrated rerouting,
followed by native connectivity/parity and full-board closure.

The follow-on pair-corridor refinement biases RX_P and RX_N to opposite
launch corridors and prohibits layer transitions within 3 mm of the M.2
connector pads. Native DRC now reports zero shorting items and zero track
crossings, with hole-clearance violations reduced to eight. The focused
candidate still has 430 incomplete-board unconnected items and 19 dangling
tracks, so it remains an unpromoted `ROUTE_IMPLEMENTATION_FAILURE`; the
result is evidence that the remaining problem is local launch/DFM cleanup,
not a demonstrated macro-placement failure.

### NPTH-preserving terminal waypoint trial — 2026-09-05

The next disposable iteration restored drilled-hole keepouts after terminal
halo clearing and attempted explicit right-side waypoints for the J3 TX_N and
RX_N launches. The resulting native DRC removed the prior eight M.2
hole-clearance records, but introduced six shorting items and 15 ordinary
clearance violations in the dense connector pad field. Track crossings remain
zero and the incomplete-board census remains 428 unconnected items.

This candidate is rejected as `ROUTE_IMPLEMENTATION_FAILURE`: the waypoint
direct-terminal emitter is too coarse for the J3 pad field. The NPTH-aware
obstacle model is retained, and the next bounded experiment must add a
dedicated pad-escape/terminal corridor rather than direct diagonal copper.
No placement, storage architecture, PCIe ancestor, or validation threshold
has been changed.

### Native terminal-escape model follow-up — 2026-09-05

The router was further instrumented with explicit physical-hole preservation,
side-gated socket approaches, and source-via serialization. The resulting
trial remains rejected: native DRC reports 6 shorting items, 0 track
crossings, 0 M.2 hole-clearance items, 15 ordinary clearance items, and 428
incomplete-board unconnected items. The attempted direct terminal segments
are the cause of the new pad-field shorts; they are not promoted and do not
change the selected storage floorplan. The next implementation must model a
legal manufacturer-style pad escape, not emit diagonal copper across the J3
launch field.

### Separated pad-corridor waypoint trial — 2026-09-05

The next disposable trial separated the RX source escapes and moved TX_N to a
dedicated outboard column. Although the physical NPTH check remained clean,
native DRC regressed to one shorting item and eight track crossings, with 23
ordinary clearance violations and the same 428 incomplete-board unconnected
items. The candidate is rejected as `ROUTE_IMPLEMENTATION_FAILURE`; the
waypoint changes are not evidence against the storage macro. The prior
zero-short/zero-crossing A* result remains the comparison baseline while the
next implementation removes waypoint-generated diagonal/terminal geometry.

### Complete RX bridge-side layer-split trial — 2026-09-05

The next bounded experiment kept the M.2 launch on the prior native-pad
baseline but moved both bridge-side RX lanes to B.Cu with ordinary source
vias. Native DRC removed the bridge-side crossing class, but source-via/pad
escape interaction produced six shorting items, four hole-clearance items,
and 12 ordinary clearance items; 428 incomplete-board unconnected items
remain. The trial is rejected as `ROUTE_IMPLEMENTATION_FAILURE`. This does
not reject the macro-placement: the defect is localized to U7 source-via
escape geometry, and the prior zero-short/zero-crossing candidate remains the
active comparison baseline.

### U7 translation and J3 north-band placement trials — 2026-09-05

Two additional placement discriminators used the baseline native-pad escape
mode. Translating U7 west to `(100,124)` with J3 retained reproduced the
zero-short/zero-crossing class, with eight M.2 hole-clearance items. Combining
that U7 translation with an outboard J3 at `(165,125)` cleared the hole class
but retained two crossings and 14 clearances. A closer north-band J3 at
`(145,100)` produced two shorts, two crossings, 13 hole-clearance items, and
48 clearances. None is promoted: these results distinguish local launch
geometry from macro placement and remain `ROUTE_IMPLEMENTATION_FAILURE`.

### Outboard J3 placement discriminator — 2026-09-05

A disposable candidate moved only the authoritative J3 M.2 socket from
`(145,125)` to `(165,125)` while retaining U7, the selected macro, and the
baseline native-pad escape mode. Native DRC reported zero shorts, zero M.2
hole-clearance violations, two track crossings, 14 ordinary clearance
violations, and 428 incomplete-board unconnected items. The outboard move
therefore removes the socket NPTH constraint but does not solve the separate
U7 bridge-side escape crossing class. It is retained as a topology
discriminator, not promoted; this is still `ROUTE_IMPLEMENTATION_FAILURE`,
not evidence of a macro-placement failure.

### U7 top-edge split dogbone trial — 2026-09-05

The U7 escape was revised so the two bridge RX lanes left the QFN top edge
through opposite dogbone corridors before ordinary vias, rather than sharing
the prior west-side departure. Native DRC reported eight shorts, one track
crossing, zero M.2 hole-clearance items, and 20 ordinary clearance items,
with 428 incomplete-board unconnected items. The trial is rejected as
`ROUTE_IMPLEMENTATION_FAILURE`; the selected storage macro and electrical
architecture remain unchanged.

### U7 source dogbone escape trial — 2026-09-05

The next local experiment avoided via-in-pad at U7 by routing each bridge-side
RX lane on F.Cu to a separate dogbone point, placing an ordinary via there,
and continuing on B.Cu to the coupling capacitor. Native DRC reported seven
shorting items, two track crossings, one hole-clearance violation, and 23
ordinary clearance violations, with 428 incomplete-board unconnected items.
The trial is rejected as `ROUTE_IMPLEMENTATION_FAILURE`. The result is
localized to the chosen U7 escape coordinates competing with the pad/clock
field; it does not reject the storage macro or the native-pad routing method.

### Proven Phase 19 SATA-island transplant — 2026-09-05

The preserved `PHASE19_V3_USB_PROVEN_SPLIT_SATA_REFILL` candidate was used as
a native implementation oracle. A disposable transplant moved U7, J3, and
C30-C33 to the donor's coherent coordinates/orientations and copied only the
donor's actual BRIDGE_SATA_/SATA_M2_ tracks and ordinary vias onto the current
Phase 24 macro ancestor. The transplant script uses the base board's actual
net objects and preserves the full pad/layer identity; the U7 pad-net audit
passes.

Native DRC reports zero shorts, zero track crossings, zero M.2 hole-clearance
violations, and nine inherited ordinary clearance violations. Only five
storage unconnected records remain, all the known duplicate U7
`BRIDGE_SATA_RX_N` pad-field relationships; the complete board still has 428
unconnected records because USB3, clock/support, power, and other Phase 24
work remain incomplete. This is a materially improved storage route baseline,
not Phase 18/19 closure. The remaining U7 pad-field relationships must be
 resolved from schematic/footprint authority before promotion.

### Macro-floorplan discriminator and coordinated storage integration — 2026-09-05

The whole-board macro review was completed before further open-by-open repair.
The actual native CM5 launch regions, not schematic drawing order, were used:
Ethernet `(34.50,99.90)`, PCIe `(69.60,101.50)`, USB3 `(70.04,105.30)`, and
SERVICE `(66.96,99.30)`. Multiple disposable macro candidates, including
Ethernet/storage exchange and PCIe-exchange probes, were compared using
source-to-island topology, ratsnest/Manhattan distance, apparent corridor
crossings, island coherence, connector-edge suitability, and acreage. The
selected west-Ethernet/mid-storage macro has the lowest apparent Ethernet
crossing burden while retaining the validated PCIe/SERVICE anchors. The
comparison deliberately did not use the historical board's mature DRC count
against first-pass candidate routes; immature copper failures remain classified
as `ROUTE IMPLEMENTATION FAILURE` unless they follow inherently from placement.

The preserved Phase 19 native storage implementation was then transplanted as
a complete U7/J3/C30-C33 coherent island. Its USB3 and SATA copper is derived
from actual donor tracks/vias and the current board's actual net objects. The
U7 RX-N pad-field stitch passes the native U7 pad-net authority audit. The
coordinated top-side candidate had exactly two localized shorts: C17 and C19
bridge-3V3 pads occupied the donor USB3 TX corridors. A native obstacle-aware
USB3 A* rewrite was attempted and rejected: it introduced multiple shorts and
crossings and is not evidence against the macro placement.

The authorized local-support repair moved C16/C17/C19 together to a low-profile
B.Cu row at `(95,118)`, `(101,118)`, `(107,118)`, preserving values, nets, and
decoupling topology. Native KiCad DRC for
`PHASE24_SELECTED_MACRO_STORAGE_PROVEN_USB3_SATA_RXN_STITCH_CAPS_BOTTOM.kicad_pcb`
reports 0 `shorting_items`, 0 `tracks_crossing`, 0 M.2 hole-clearance errors,
419 inherited incomplete-board unconnected items, and 10 ordinary clearance
items. The three courtyard overlaps are inherited C7/C8, J7/C14, and C5/C6;
none involves the moved bridge caps. The U7 pad-net authority audit passes and
storage-specific unconnected count is zero for CM5 USB3, BRIDGE_SATA, and
SATA_M2 nets. This closes the coordinated storage route locally, but does not
close Phase 24: clock/support, power-delivery, and other board opens remain.
Consultant spawning was unavailable at the thread limit; the review was
performed locally against the saved native geometry and preserved evidence.

### Bridge regulator-support oracle overlay — 2026-09-05

The next coherent repair copied only the proven bridge regulator-support
copper from `PHASE24_U5_INTEGRATED_LAYERED.kicad_pcb` onto the promoted
storage baseline. No Ethernet, PCIe, USB3, or SATA copper was replaced. The
overlay uses the current board's actual net objects and KiCad-native track/via
geometry. Native DRC improves from 419 to 407 unconnected items, with zero
`shorting_items` and zero `tracks_crossing`. The affected open census changes
from 21 to 17 BRIDGE_1V1, 17 to 10 BRIDGE_3V3, 1 to 0 BRIDGE_RESET, 3 to 0
FB_BRIDGE_3V3, 2 to 0 PG_BRIDGE_3V3, and 1 to 0 RT_BRIDGE_3V3 records. Storage
specific unconnected count remains zero, and the U7 pad-net authority audit
passes. The candidate is promoted as the current Phase 24 integration basis;
the two additional ordinary clearances are retained for later local review.

### Complete clock-support transplant from passing V2 fixture — 2026-09-05

The passing `PHASE24_CLOCK_COMPLETE_ASTAR_V2` fixture was adapted onto the
current storage/power baseline using its serialized clock tracks and vias,
with the current board's native `/STORAGE/BRIDGE_XI`,
`/STORAGE/BRIDGE_XO`, and `/STORAGE/BRIDGE_VSSOSC` net objects. Y1/R23/C42/C43
were moved as one support island to the fixture's proven coordinates. Native
KiCad DRC reports 0 `shorting_items`, 0 `tracks_crossing`, and 397 total
unconnected items. Compared with the preceding 407-open basis, all clock
specific unconnected records (10) are removed; storage-specific unconnected
records remain zero. Clearance count remains 12 and courtyard count remains
3, identical to the preceding basis, so this transplant introduced no new
violation class. The U7 pad-net authority audit passes. The resulting
`PHASE24_CLOCK_COMPLETE_V2_ON_CURRENT.kicad_pcb` is promoted as the current
Phase 24 integration basis; full-board ground, power, service, and remaining
connectivity closure is still required.

### Local In3 power-entry planes — 2026-09-05

The second input block was tested using native In3 copper rather than an
F.Cu/B.Cu signal-layer detour. Two local filled regions feed the existing
`/POWER_INPUT/12V_IN_B` and `/POWER_INPUT/FUSED_12V_B` PTH entry networks;
no schematic net names or power topology were changed. Native DRC reports
0 shorts, 0 track crossings, and 390 unconnected items, down from 397. The
specific input-net open census improves from 6 to 2 for `12V_IN_B` and from
6 to 3 for `FUSED_12V_B`; `12V_PROTECTED` is unchanged at 146. The candidate
`PHASE24_POWER_INPUT_PLANES_PROBE.kicad_pcb` is promoted as the current basis.
The remaining input-side SMD launches and the distinct `12V_PROTECTED` load
distribution still require explicit routing/return validation.

### J1 protected-field bus on current basis — 2026-09-05

The validated 13-column J1 `12V_PROTECTED` field implementation was applied
to the current clock/storage/power basis. Column coordinates were derived from
the native J1 pads; each column uses F.Cu field copper, one offset ordinary
through-via below the connector field, and a B.Cu collector. Native KiCad DRC
reports 0 shorts, 0 track crossings, and 261 unconnected items, down from 390.
The `12V_PROTECTED` open census falls from 146 to 17 and J1-field records are
reduced from 201 to 70; storage-specific opens remain zero. The candidate
`PHASE24_J1_PROTECTED_FIELD_CURRENT.kicad_pcb` is promoted. The remaining
protected-load launches, power-return populations, and other board opens still
require closure.

### Global POWER_GND launch cluster on current basis — 2026-09-05

The previously validated U1/U2/J4/U8 global-ground launch cluster was applied
to the current J1/storage/clock basis. It uses short F.Cu dogbones and
ordinary through-vias at the native pad coordinates, with no CM5 scoped-ground
net merge. Native KiCad DRC reports 0 shorts, 0 track crossings, and 254
unconnected items, down from 261. POWER_GND-related open records fall from
181 to 174 while the 12V_PROTECTED count remains 17. The candidate
`PHASE24_PGND_CLUSTER_CURRENT.kicad_pcb` is promoted; remaining ground and
protected-load endpoints still require explicit closure.

### Native U5 audit recheck and rejected plane/link probes — 2026-09-06

The corrected U5 connectivity audit was rerun against both its saved native
U5 fixture and the current integrated `PHASE24_PGND_CLUSTER_CURRENT` board.
Both passed using KiCad `BuildConnectivity`; the disposable negative control
removed a real U5.9 trace and failed as required. No expected graph edges are
used by the audit.

Two subsequent disposable repairs were rejected against the same promoted
`e1f497d` basis. A global `POWER_GND` In1 plane with offset vias reduced native
unconnected records from 254 to 247 but created five shorts. A `/REGULATORS/
BRIDGE_1V1` In2 plane with offset vias reduced them to 242 but created four
shorts. A same-layer local ground-link probe reduced them to 248 but created
three shorts. None is promoted. These are `ROUTE IMPLEMENTATION FAILURE`
results; they do not invalidate the completed macro-floorplan discriminator,
U5 authority, Ethernet, PCIe, or coordinated storage neighborhoods. The
current integrated basis remains `PHASE24_PGND_CLUSTER_CURRENT.kicad_pcb`
with 0 shorting items, 0 track crossings, and 254 native unconnected items.

### Promote local POWER_GND capacitor links — 2026-09-06

The same-net capacitor-field repair was regenerated with dogbone geometry
around the opposite pads rather than straight pad-field crossings. Native
KiCad DRC reports 0 `shorting_items`, 0 `tracks_crossing`, 251 unconnected
items, and 12 clearance items, improving the promoted basis from 254 opens
and 13 clearance items. Native connectivity confirms C14.2-C15.2 and
C16.2-C17.2-C19.2 are connected on their actual copper layers. The U5 audit
and real-trace negative control still pass. The candidate
`PHASE24_GROUND_CAP_LINKS_CURRENT.kicad_pcb` is promoted; all remaining
full-board opens still require closure.

### Promote local Ethernet support-ground joins — 2026-09-06

The two isolated POWER_GND pads on each Ethernet support device were joined
with short same-layer F.Cu tracks only. The earlier cross-island probe was
rejected; this local-only geometry avoids the signal-pad corridors. Native
KiCad DRC reports 0 shorts, 0 track crossings, 249 unconnected items, and 12
clearance items. The Ethernet native connectivity audit and real-track
negative control both pass. `PHASE24_ETH_GROUND_LOCAL_CURRENT.kicad_pcb` is
promoted; remaining board-wide ground, power, service, and control opens are
still open.

### Promote local bridge 1V1 capacitor-bank plane — 2026-09-06

The broad bridge-rail plane was rejected because it shorted unrelated board
regions. A bounded In2 pour was then confined to the actual C26-C29/C34-C41
capacitor acreage, with offset ordinary through-vias and F.Cu dogbones at
each pad. Native connectivity places all 12 capacitor pads in one real
`/REGULATORS/BRIDGE_1V1` component. Native DRC reports 0 shorts, 0 track
crossings, 238 unconnected items, and 12 clearance items. The candidate
`PHASE24_BRIDGE_1V1_CAPBANK_PLANE_CURRENT.kicad_pcb` is promoted; its final
connection to the U5 output field remains a separate required repair.

### Promote U5 repeated-output field bridge — 2026-09-06

The first U5 field bridge was retained after the wider U5.5 dogbone was
rejected for introducing three new clearance violations. Its offset-via
geometry joins U5.8 to U5.9/C44-C47 without crossing the intervening QFN
control/ground pads. Native DRC reports 0 shorts, 0 track crossings, 237
unconnected items, and 12 clearance items. U5.5 remains explicitly isolated
and is not waived; it requires a later placement-aware escape. The candidate
`PHASE24_BRIDGE_1V1_U5_FIELD_CURRENT.kicad_pcb` is promoted.

### Promote U5 protected-input top-edge join — 2026-09-06

The combined U4/U5 input join was rejected because the U4 segment crossed an
existing PG_BRIDGE_3V3 escape. The isolated U5 top-edge join was then tested
alone. It connects U5.1 to U5.16 using their actual native `12V_PROTECTED`
pads, with no shorts or crossings. Native DRC reports 0 shorts, 0 crossings,
236 unconnected items, and 12 clearance items. The candidate
`PHASE24_REGULATOR_INPUT_TOP_PAD_CURRENT.kicad_pcb` is promoted; U4 and the
remaining U5.14 input pad remain explicit open repair targets.

### Rejected U4/U7 local escape variants — 2026-09-06

The U4 protected-input B.Cu bridge reduced the native unconnected count from
236 to 235 but added two clearance violations against the existing
PG_BRIDGE_3V3 geometry, so it was rejected. The U7
`/STORAGE/BRIDGE_1V1` outside-QFN dogbone reduced the count to 236 but added
one short and two track crossings, so it was rejected. Both are
`ROUTE IMPLEMENTATION FAILURE` results. The promoted basis remains
`PHASE24_REGULATOR_INPUT_TOP_PAD_CURRENT.kicad_pcb` with zero shorts and zero
crossings; neither U4 nor U7 architecture or placement is being waived.

### Promote regulator 3V3 capacitor-bank links — 2026-09-06

The three moved C16/C17/C19 regulator-side 3V3 pads were joined with a
same-net B.Cu dogbone routed below their opposite POWER_GND pads. The
distinct `/STORAGE/BRIDGE_3V3` U7 net was not merged. Native KiCad DRC
reports 0 shorts, 0 crossings, 234 unconnected items, and 12 clearance
items. `PHASE24_BRIDGE_3V3_CAPBANK_LINKS_CURRENT.kicad_pcb` is promoted;
the U4 regulator-side field remains to be connected.
### Promote F1 input-side PTH field — 2026-09-06

The four native F1 input pads on `/POWER_INPUT/12V_IN_A` were joined with a
wide B.Cu rectangular field. The field touches only the four same-net PTH
pads and preserves the separate fused-output group. Native KiCad DRC reports
0 shorts, 0 track crossings, 231 unconnected items, and 12 clearance items.
`PHASE24_F1_INPUT_PAD_FIELD_CURRENT.kicad_pcb` is promoted; the remaining
input/protection and regulator endpoints remain open.

### Rejected Q1/U1 protected launch — 2026-09-06

The direct F.Cu Q1.2-to-U1.4 `/12V_PROTECTED` launch reduced the native open
count from 225 to 224 but shorted an existing Ethernet trace. It is rejected
as `ROUTE IMPLEMENTATION_FAILURE`; the protected power net remains separate
and the promoted zero-short/crossing basis is unchanged.

### Promote F1 fused-output PTH field — 2026-09-06

The four F1 output-side PTH pads on `/POWER_INPUT/FUSED_12V_A` were joined
with a separate wide B.Cu rectangular field. The field does not touch the
input-side field or alter the fuse/protection topology. Native KiCad DRC
reports 0 shorts, 0 track crossings, 229 unconnected items, and 12 clearance
items. `PHASE24_F1_FUSED_OUTPUT_PAD_FIELD_CURRENT.kicad_pcb` is promoted;
Q1/D1/load distribution remains to be connected and validated.

### Promote Q1 fused-A local launch — 2026-09-06

The Q1 `/POWER_INPUT/FUSED_12V_A` PTH launch was connected to the existing
native B.Cu fused-A segment ending at `(22.5,80)` with one short local
segment. Native DRC reports 0 shorts, 0 track crossings, 228 unconnected
items, and 12 clearance items. The D1 long-bus trial was rejected because it
added a crossing without closing an open. `PHASE24_FUSED_Q1_LAUNCH_CURRENT.
kicad_pcb` is promoted; D1 and the remaining fused-A distribution endpoints
remain open.

### Promote D1 fused-A parallel launch — 2026-09-06

The first D1 bus path crossed the diagonal 12V_IN_A bus. The corrected
variant transitions from D1 on F.Cu at the pad launch, then uses an elevated
B.Cu corridor to the existing fused-A vertical. Native KiCad DRC reports 0
shorts, 0 track crossings, 227 unconnected items, and 12 clearance items.
`PHASE24_FUSED_D1_PARALLEL_LAUNCH_CURRENT.kicad_pcb` is promoted; Q2/F2 and
the remaining protected-load distribution are still open.

### Rejected B-input C4/U2 launch variants — 2026-09-06

The direct C4.2-to-U2.3 F.Cu launch shorted the existing `/POWER_INPUT/VCAP_B`
route. An offset-via B.Cu alternative was then tested; it reduced native
unconnected items from 227 to 225 but introduced three shorts, one crossing,
and three new clearance items. Both variants are rejected as
`ROUTE IMPLEMENTATION_FAILURE`; `/POWER_INPUT/12V_IN_B` remains open and its
VCAP_B separation is preserved.

### Promote obstacle-aware C4/U2 12V_IN_B launch — 2026-09-06

The corrected B-input route transitions at C4.2 and laterally at U2.3, then
uses B.Cu around the existing VCAP_B and Ethernet escapes. Native KiCad DRC
reports 0 shorts, 0 track crossings, 225 unconnected items, and 12 clearance
items. `PHASE24_12V_B_C4_U2_OBSTACLE_ROUTE_CURRENT.kicad_pcb` is promoted;
the remaining U2-to-F2 source connection is still open.
### Promote C14/C15 protected capacitor link — 2026-09-06

The same-net C14.1/C15.1 `/12V_PROTECTED` pads were joined around their
opposite POWER_GND pads with a short F.Cu dogbone. Native KiCad DRC reports
0 shorts, 0 track crossings, 224 unconnected items, and 12 clearance items.
`PHASE24_PROTECTED_C14_C15_LINK_CURRENT.kicad_pcb` is promoted; remaining
protected-load and regulator distribution endpoints remain open.

### Promote CM5 5V feedback dogbone — 2026-09-06

The native `FB_CM5_5V` chain C9.1–R3.2–R4.1 was routed around the opposite
CM5_5V/POWER_GND pads with an F.Cu dogbone. Native KiCad DRC reports 0
shorts, 0 track crossings, 220 unconnected items, and 12 clearance items.
`PHASE24_CM5_5V_FEEDBACK_DOGBONE_CURRENT.kicad_pcb` is promoted; the
remaining CM5 5V feedback/control and power-return endpoints remain open.

### Promote U7 storage 3V3 adjacent pad join — 2026-09-06

The adjacent U7.30/U7.31 `/STORAGE/BRIDGE_3V3` pads were joined with a short
F.Cu segment using their actual native net identity. The regulator-side
`/REGULATORS/BRIDGE_3V3` net was not merged. Native KiCad DRC reports 0
shorts, 0 track crossings, 219 unconnected items, and 12 clearance items.
`PHASE24_U7_STORAGE_3V3_ADJACENT_CURRENT.kicad_pcb` is promoted; the
remaining U7 storage 3V3 pad-field connection remains open.

### Promote U7 storage 3V3 pad-field completion — 2026-09-06

The remaining U7.24 `/STORAGE/BRIDGE_3V3` pad was connected to the joined
U7.30/U7.31 field using the native F.Cu dogbone around the QFN edge. Native
KiCad DRC reports 0 shorts, 0 track crossings, 218 unconnected items, and 12
clearance items. `PHASE24_U7_STORAGE_3V3_PAD24_CURRENT.kicad_pcb` is
promoted; the storage bridge 3V3 pad field is now complete.

### Rejected U3 protected-input bridge — 2026-09-06

The U3.14/U3.16 `/12V_PROTECTED` offset-via bridge reduced the native open
count from 222 to 221 in a disposable copy, but both via placements entered
the U3 central POWER_GND keepout and produced a native short/clearance defect.
It is rejected as `ROUTE_IMPLEMENTATION_FAILURE`; U3 remains an explicit
placement-aware repair target and the promoted zero-short/crossing basis is
unchanged.

### Promote C23-C25 protected capacitor field — 2026-09-06

The same-net C23.1/C24.1/C25.1 `/12V_PROTECTED` pads were joined with an
edge-side F.Cu dogbone around their opposite ground pads. Native KiCad DRC
reports 0 shorts, 0 track crossings, 222 unconnected items, and 12 clearance
items. `PHASE24_PROTECTED_C23_C25_LINK_CURRENT.kicad_pcb` is promoted;
connection to the U3 protected-input field remains open.

## Whole-board macro-floorplan review corrected for current accepted basis — 2026-09-06

The required macro-floorplan discriminator was rerun from the actual current
accepted integrated PCB `PHASE24_U7_STORAGE_3V3_PAD24_CURRENT.kicad_pcb`, not
from a historical disposable filename. The reproducible native-loaded script
is `phase24_macro_floorplan_review_fresh.py`; the evidence report is
`PHASE24_WHOLE_BOARD_MACRO_REVIEW_CURRENT.md`. All coordinates are extracted
after KiCad footprint transforms in the CM5 carrier-mating view. Existing
copper and mature-board DRC counts are excluded from candidate ranking.

Native J7 launch centroids are Ethernet `(34.50,99.90)`, PCIe
`(69.60,101.50)`, USB3 `(70.04,105.30)`, and SERVICE `(66.96,99.30)` mm.
The accepted current physical map is Ethernet `(18.48,128.42)` with a
32.71-mm centroid distance, PCIe `(150.00,90.00)` with 81.22 mm, storage
`(130.81,130.97)` with 65.97 mm, and SERVICE `(46.88,100.00)` with 20.09 mm.
Power-input/protection and regulator/load-delivery centroids are also recorded
in the report; their copper was not moved.

Five disposable placement candidates were generated and compared using
source-to-island Euclidean/Manhattan distances and native-pad same-net
ratsnest lengths. The accepted baseline has 231.2 mm of USB3/storage
same-net ratsnest. `STORAGE_LOCAL` and the joint
`ETH_OUTBOARD_STORAGE_LOCAL` candidate reduce that topology metric to 69.1
mm and storage centroid distance to 39.3 mm, while PCIe and SERVICE remain at
their baseline anchors. `ETH_EAST_STORAGE_NORTH` is a fallback with a 152.8-mm
Ethernet centroid distance. Body/courtyard overlaps in moved candidates are
reported separately as mechanical-screen findings; no route or DRC result was
used to reject a topology candidate.

Disposition: `MACRO_FLOORPLAN_DISCRIMINATOR = COMPLETE`.
`ETH_OUTBOARD_STORAGE_LOCAL` is selected as the next routing-development
basis because it tests the explicit Ethernet/storage neighborhood swap while
preserving the PCIe and SERVICE anchors. This is a topology selection, not a
routing pass. Any failed first-pass copper remains `ROUTE IMPLEMENTATION
FAILURE` unless a fair obstacle-aware development cycle demonstrates an
inherent placement obstruction. Detailed Phase 24 repair may resume only for
the complete affected storage/Ethernet neighborhoods from this basis.

Consultant dispatch was attempted for the required independent review but the
collaboration service returned `agent thread limit reached`; no engineering
conclusion was taken from that unavailable thread, and the review was completed
locally from native KiCad evidence.

## Macro candidate screen refined for mechanical clearance — 2026-09-06

The initial swap candidate shortened the storage ratsnest but overlapped J1
and local support bodies. A further placement-only sweep tested south and
center alternatives while moving U7, J3, clock support, decoupling, and SATA
coupling as one coherent storage island. `STORAGE_LOCAL_CLEAR2` places U7 at
`(90,120)` and J3 at `(125,120)` with its complete local support set moved
accordingly. Native transformed-body screening reports no moved-body overlap.

Its topology-only source metrics are storage centroid distance `39.9 mm`,
Manhattan distance `52.1 mm`, and USB3/storage same-net ratsnest `88.1 mm`,
versus `66.0 mm`, `86.4 mm`, and `231.2 mm` for the current accepted basis.
PCIe remains `81.2 mm` and SERVICE `20.1 mm`; the accepted Ethernet island,
power-input/protection, and regulator/load-delivery islands are unchanged.
The south-clear candidate was mechanically screened but leaves storage
same-net ratsnest at `192.0 mm`; the Ethernet-outboard variants introduce
power-entry body conflicts and are not selected.

Disposition superseding the prior topology-probe wording:
`MACRO_FLOORPLAN_DISCRIMINATOR = COMPLETE` and
`SELECTED_MACRO_BASIS = STORAGE_LOCAL_CLEAR2`.
The selected placement is saved as `PHASE24_MACRO_FRESH_STORAGE_LOCAL_CLEAR2.kicad_pcb`.
This is a placement decision only. No temporary candidate copper is accepted;
the next action is coordinated regeneration of USB3, SATA, clock, support,
reference, and return routing from the selected coherent storage island.
Historical-board DRC and first-pass candidate DRC remain excluded from this
floorplan ranking. Any later failed route is classified separately as route
implementation failure unless valid routing development demonstrates an
inherent placement obstruction.

## Selected storage-basis routing development — 2026-09-06

The selected placement was refined to `STORAGE_LOCAL_J3_EDGE`: U7 and its
clock, decoupling, and SATA-coupling support move toward the CM5 USB3 launch;
J3 retains the existing mechanically compatible edge position. The native
body screen reports no new moved-body overlaps after inherited overlaps are
excluded. This supersedes the earlier `STORAGE_LOCAL_CLEAR2` coordinate set,
whose moved support row intersected inherited PCIe/SERVICE copper.

The first USB3 A* regeneration was rejected as `ROUTE_IMPLEMENTATION_FAILURE`
because it left malformed terminal escape geometry: native DRC reported 27
shorts, 15 crossings, and 264 unconnected items. The first SATA continuation
from that malformed basis was likewise rejected with 37 shorts, 23 crossings,
and 248 unconnected items. Neither result is used as floorplan evidence.

A second, coherent manual reference-style USB3 probe removed all affected
USB3/SATA/clock copper before authoring explicit monotonic split-layer lanes.
The corrected native DRC result is 0 shorts, 0 crossings, 259 unconnected
items, and 15 clearance items. The zero-short/crossing result is useful route
development evidence, but the remaining native opens, dangling transitions,
and clearance findings prevent promotion. A follow-on manual SATA probe was
rejected with 13 shorts, 10 crossings, 249 unconnected items, and 21
clearance items; it is retained only as negative route evidence.

Disposition: the macro choice remains `STORAGE_LOCAL_J3_EDGE`, and all failed
probes are `ROUTE_IMPLEMENTATION_FAILURE`, not `MACRO-PLACEMENT FAILURE`.
No candidate copper is promoted. The next action is to adapt the already
proven Phase 24 storage route topology to this placement with native terminal
escapes and post-mutation reloads, then validate USB3 and SATA together before
clock/support reintegration.

## Storage route-method correction evidence — 2026-09-06

The selected-basis route probes were evaluated as saved native boards. The
initial generic A* USB3/SATA sequence is rejected because its terminal-halo
authoring created actual pad-field shorts/crossings. The corrected manual
USB3 sequence removes all affected USB3/SATA/clock tracks first and emits
explicit F.Cu/B.Cu lanes from native J7/U7 pad coordinates. Native DRC reports
0 shorts, 0 track crossings, 259 unconnected items, and 15 clearance items;
the remaining opens include dangling transitions, so it is not promoted.

The subsequent SATA probe is also rejected: native DRC reports 13 shorts, 10
crossings, 249 unconnected items, and 21 clearance items. The failures are
localized to U7's dense SATA pad field, coupling-pad boundary, and the
connector-side pair ordering. This is `ROUTE_IMPLEMENTATION_FAILURE`, not
`MACRO-PLACEMENT FAILURE`; the placement comparison remains based on native
pad topology and mechanical screening only. No route or validation severity
was waived, and Phase 18/19 remain open pending a proven-topology adaptation.

## USB3 transition-semantics correction — 2026-09-06

Inspection of the serialized manual probe found an authoring defect in the
disposable layer-transition emitter: a transition point with a changed XY
coordinate skipped the segment between the via and the next layer. The probe
was corrected to emit duplicate-coordinate transition points, preserving real
through-via contact on both copper layers. Fresh native DRC improved from 253
to 251 unconnected items while retaining 0 shorts; it still reports 3 track
crossings, 15 clearance items, 6 dangling vias, and 27 dangling tracks, so it
remains unpromoted. This confirms the prior failure was partly
`ROUTE_IMPLEMENTATION_FAILURE` in the generator, not a placement verdict.

Consultant dispatch was retried for the transition/escape review and again
returned `agent thread limit reached`; local native serialized-board evidence
remains the active basis. No validation severity or architecture constraint
was relaxed.

## Manual USB3 lane-order follow-up — 2026-09-06

A further no-via/transition-order correction was tested on the same selected
storage placement. Native DRC retained 0 shorts but exposed 7 crossings, 13
clearance items, 251 unconnected items, 6 dangling vias, and 27 dangling
tracks. The new crossings are at the CM5/PCIe launch corridor and the U7
approach; this confirms that hand-picked lane coordinates are not an adequate
authoring method for the integrated board. The probe is rejected as
`ROUTE_IMPLEMENTATION_FAILURE`; it does not change the topology-only
floorplan selection or the frozen PCIe architecture.

The next route class is therefore a native/reference-topology transplant with
explicit obstacle clearing and saved-board reload between mutation stages,
followed by independent native connectivity/DRC. No further same-class manual
lane sweep is promoted.

## Native storage-topology control — 2026-09-06

`phase24_storage_reference_control.py` was added as a disposable control. It
loads the selected macro board and the already-proven native storage route,
snapshots donor geometry before target mutation, restores the donor's coherent
U7/J3/support placement, and copies only the donor's actual USB3/SATA/clock
copper onto the target board's native net objects. KiCad 10's SWIG collection
must be snapshotted before target edits; otherwise donor track proxies become
invalid during mutation.

The saved control was checked with native KiCad DRC: 510 total violations and
258 unconnected items. It is rejected as a whole-board candidate. The result
does not rank the selected macro floorplan: the control intentionally changes
placement and retains the target board's inherited defects. It does establish
the next authoring boundary and preserves a reproducible native/reference
transplant path. The selected `STORAGE_LOCAL_J3_EDGE` placement remains the
development basis; adaptation must preserve native pad contact at its new U7
location and be independently rechecked.

Consultant dispatch remains unavailable because the agent thread limit is
reached. Local native evidence is used; no validation severity, layer policy,
architecture, or floorplan decision was relaxed.

## CM5IO-style USB3 launch correction — 2026-09-06

`phase24_usb3_reference_escape_probe.py` was corrected to place the initial
through-vias on the official CM5IO launch side of J7 before entering the
secondary B.Cu corridor. This reduced the launch-related shorts from six to
two, confirming that the first probe's opposite-side escape was an authoring
failure. The corrected saved board still fails native DRC with 537 total
violations and 259 unconnected items; the remaining real shorts include a
TX-pair interaction and an RX interaction with inherited bridge power, with
crossing/clearance findings also remaining. It is rejected as
`ROUTE_IMPLEMENTATION_FAILURE`. No copper was promoted and the selected
macro-floorplan is unchanged.

## USB3 dense-pad escape follow-up — 2026-09-06

A second CM5IO-style B.Cu corridor trial kept the corrected J7 launch but
moved the endpoint transitions to horizontal approaches at U7. Native DRC
found 12 shorts, 42 crossing findings, and 259 unconnected items; the shorts
are concentrated in the RX/TX pair approaches at the U7 pad field. This is
also rejected as `ROUTE_IMPLEMENTATION_FAILURE`. The two corrected launch
attempts have now demonstrated that further hand-authored corridor tuning is
low-value; the next attempt must transplant a proven dense-pad escape or use
native interactive routing semantics. The macro-floorplan remains unchanged.

## USB3 via-spacing correction — 2026-09-06

The next bounded correction spread the endpoint transitions outside the U7
pad-field diameter envelope. Native DRC reports zero shorting items but 9
`tracks_crossing` findings, 535 total violations, 259 unconnected items, and
42 clearance findings, including plane-clearance findings at the transition
vias and inherited board defects. The probe is therefore rejected and remains
`ROUTE_IMPLEMENTATION_FAILURE`; the zero-short result is retained as limited
route-development evidence, not as Phase 18 closure. The next correction is
deliberate local return-via and plane-clearance handling followed by
storage-specific connectivity audit. An earlier summary that called this
zero-crossing was a report-parser error and is superseded here.

The focused native `BuildConnectivity` audit nevertheless confirms all four
USB3 endpoint memberships in the saved v4 probe: J7.128↔U7.42,
J7.130↔U7.43, J7.140↔U7.45, and J7.142↔U7.46. This is endpoint-connectivity
evidence only; it does not waive the remaining native DRC crossings,
clearances, or whole-board opens.

## USB3 TX lane-order follow-ups — 2026-09-06

Two further native DRC trials attempted to remove the one USB3 TX-pair
crossing while preserving the selected U7 placement. The first retained 9
crossing findings; the second increased the result to 10 because the new TX_N
segment crossed both TX_P and the inherited SERVICE B.Cu corridor. Both are
rejected as `ROUTE_IMPLEMENTATION_FAILURE`. The focused native connectivity
audit still proves all four J7-to-U7 endpoint memberships, but no candidate
copper is promoted. Same-class hand-authored lane tuning is stopped; the next
route class must use a proven/reference dense-pad escape or native router
semantics with obstacle clearing.

## SERVICE-corridor discriminator — 2026-09-06

A disposable copy removed only inherited `SERVICE_RD_B` copper before
re-emitting the selected-placement USB3 escape. Native DRC improved to 540
total violations and 260 unconnected items, with 1 short, 4
`tracks_crossing` findings, and 35 clearance findings. The focused native
audit still passes all four J7-to-U7 USB3 endpoint memberships. This separates
an inter-island corridor conflict from the remaining USB3 pair-order escape
failure, but the candidate is rejected and no SERVICE or USB3 copper is
promoted. The selected macro-floorplan remains unchanged.

## Monotonic USB3 reference-channel result — 2026-09-06

A disposable channelized fanout then removed the artificial vertical-channel
crossings and used direct order-preserving B.Cu segments between source and
endpoint transitions. The saved native board has 0 shorting items, 0
`tracks_crossing` findings, 42 clearance findings, and 260 whole-board
unconnected items. The corrected 0.50 mm finished vias satisfy the board's
0.10 mm annular-width minimum. Independent native `BuildConnectivity` passes
all four J7↔U7 USB3 endpoint assertions. This is a successful USB3 route-
development result but not Phase 18 closure: clearance findings and inherited
opens remain, and SATA/clock/support integration is still outstanding. No
copper was promoted to the acreage candidate.

## Minimal USB3 fixture launch follow-up — 2026-09-06

The minimal native fixture isolated the J7/U7 geometry from inherited board
objects. Its wider source-via fanout reached 2 clearance findings, 0 shorts,
0 crossings, and 65 fixture opens; native `BuildConnectivity` passed all four
J7↔U7 endpoints. A subsequent full-width angular RX_P launch intended to
clear the adjacent J7 ground pad instead introduced RX pair shorts/crossings,
with 13 total DRC violations. It is rejected. The prior two-clearance
geometry remains the best isolated route reference; the angular launch is
retained only as negative evidence, and no integrated copper is promoted.

## Minimal USB3 source-via spacing result — 2026-09-06

The minimal native J7/U7 fixture was refined with wider pair-ordered source
via spacing and native endpoint coordinates. Native DRC now reports 1
clearance finding and 65 expected fixture opens, with no shorts, no
`tracks_crossing` findings, and no annular-width violations. Native
`BuildConnectivity` passes J7.128↔U7.42, J7.130↔U7.43, J7.140↔U7.45, and
J7.142↔U7.46. The sole remaining DRC error is the full-width RX_P escape
against adjacent fine-pitch J7 ground pad 132 (0.0709 mm actual clearance).
This is a connector-launch constraint issue; no severity or width rule was
relaxed, and the fixture is not an integrated-board promotion.

## Official CM5IO USB3 CAD extraction — 2026-09-06

The native Rev 2 CM5IO PCB source was inspected directly at
`authority-inventory/cm5io-rev2/CM5IO.kicad_pcb`. The reproducible extraction
receipt records the actual `Module1` ComputeModule5 footprint transform and
all four USB3-0 nets. The official source uses 0.147 mm segments on F.Cu and
B.Cu, with two ordinary through-vias on each RX pair and one on each TX pair;
no signal tracks are on In1/In4. The extracted native via positions and layer
census are saved in `PHASE24_CM5IO_USB3_REFERENCE_EXTRACT.md`. This is the
reference implementation oracle for the next PiSXMe adaptation, not a claim
that its absolute coordinates transplant unchanged.

## CM5IO versus PiSXMe launch-rule comparison — 2026-09-06

Native inspection confirms that the PiSXMe J7 USB3 pads and official CM5IO
ComputeModule5 USB3 pads both use 0.2 mm × 0.7 mm rectangular pads on 0.4 mm
pitch. The relevant board constraints differ: the official CM5IO native PCB
uses 0.125 mm minimum clearance, while the PiSXMe acreage board uses 0.150
mm. This explains why the PiSXMe minimal full-width RX_P launch retains a
0.0709 mm clearance finding even though the pad geometry is authoritative and
matching. It is a real connector-launch rule/geometry issue; it is not
evidence against U7 placement or the USB3 route topology. No constraint was
changed in this comparison.

## Divergent official-style launch negative control — 2026-09-06

A divergent full-width source escape was tested in the minimal native fixture
to move RX_P away from J7 ground pad 132 while retaining the board's existing
rules. Native DRC found 7 violations, including one RX_P short to frozen
J7/CM5 PCIe pad 124 and two RX pair crossings. It is rejected as
`ROUTE_IMPLEMENTATION_FAILURE`. The fixture was restored to the prior best
source-via spacing afterward; no integrated board or validation rule changed.

## Macro-floorplan discriminator checkpoint and CM5IO native DRC context — 2026-09-06

The current integrated candidate was snapshotted by SHA-256 as
`0466f93782dd535b6f02fed9a0492d77dce18ebe5eceb59a3df30c60fe96f92d` for
`PHASE24_U7_STORAGE_3V3_PAD24_CURRENT.kicad_pcb`. The whole-board review was
rerun from that native-loaded board and regenerated the disposable candidate
set recorded in `PHASE24_WHOLE_BOARD_MACRO_REVIEW_CURRENT.md`, including
`CURRENT`, `ETH_OUTBOARD`, `STORAGE_LOCAL`, `STORAGE_LOCAL_CLEAR2`,
`STORAGE_LOCAL_J3_EDGE`, south/center storage variants, and combined
Ethernet/storage variants. Ranking remains topology-only: native CM5 launch
coordinates, transformed-pad distances, same-net ratsnest lengths, corridor
competition, and mechanical body screening; mature historical DRC and
first-pass candidate DRC are excluded.

The discriminator remains complete and selects
`STORAGE_LOCAL_J3_EDGE` as the routing-development basis. This is a
`MACRO_FLOORPLAN` decision, not a claim that its affected routing is complete;
the current USB3 findings remain `ROUTE IMPLEMENTATION FAILURE` until a fair
reference/obstacle-aware development cycle closes them. The selected
placement snapshot hash is
`b03c8be8913d0103c7453d7e4976e3b21ccf1d0e9d3e9a294683d1130aa7ce71`.

The official native CM5IO Rev 2 board was also checked with KiCad 10 native
DRC and the full receipt is saved as
`PHASE24_CM5IO_OFFICIAL_NATIVE-drc.rpt`. It reports 76 findings: 26
`clearance`, 49 `lib_footprint_mismatch`, and 1 `courtyards_overlap`; it
reports zero `shorting_items`, zero `tracks_crossing`, zero
`unconnected_items`, and zero `annular_width` records. The clearance findings
are existing POE-tap/reference-board context and the library mismatches are
embedded-copy differences, so this result is an implementation oracle for
topology rather than a blanket claim of zero CM5IO DRC findings.

Consultant was retried for the required independent review and again could
not spawn because the collaboration service reported `agent thread limit
reached`. No conclusion was taken from that unavailable reviewer; local
review used the native-loaded evidence above. Phase 24 remains open and no
Phase 25/26 work has begun.

## CM5IO source-escape transplant authoring probe — 2026-09-06

A disposable fixture attempted to transplant the official CM5IO USB3 source
escape using the measured native pad-frame transform (`x' = x - 90.42`,
`y' = 203.5 - y`) and the official 0.147 mm source geometry. The oracle path
was snapshotted into scalar coordinates before target-board mutation, and the
RX_N path correctly identified seven source-side segments terminating at the
first official via. KiCad 10's `pcbnew` Python binding then exited with
`SIGSEGV` while adding that transformed via, before any fixture board was
saved or validated. This is classified as `ROUTE IMPLEMENTATION / TOOLING
FAILURE`, not `MACRO-PLACEMENT FAILURE` or Ethernet/USB3 electrical evidence.
The integrated candidate and all accepted copper remain unchanged. The next
attempt must use a safer native serialization/native-GUI path or a minimal
via-add mutation isolated from the transformed-track loop; no validation
gate or clearance rule is relaxed.

## CM5IO source-frame and layer-routing discriminators — 2026-09-06

The safe load-order correction (oracle snapshot first, target board loaded
last, target net codes and pad positions snapshotted before mutation) produced
a saved native fixture. The initial translated source escape was rejected
after it forced all copied tracks onto F.Cu and produced 12 shorts and one
crossing; retaining the official track layers removed that authoring defect.

The full mirrored carrier-frame transform then removed all shorts. Its native
fixture result was 17 total findings: 0 shorts, 8 crossings, 2 clearances,
and 65 expected fixture opens. A localized RX layer split was tested and
rejected at 15 findings including 7 shorts. The restored mirrored pair-order
variant, with TX routed around the J7 NPTH launch obstruction, remains a
disposable result at 6 findings: 0 shorts, 4 crossings, 1 clearance, 1 hole
clearance, and 65 expected fixture opens. In both saved variants, independent
native `BuildConnectivity` passes all four J7↔U7 USB3 endpoint assertions.

These experiments separate three classes of evidence: the first is a route
authoring defect, the mirrored frame is a real improvement in source-side
orientation, and the remaining crossings/clearance are incomplete endpoint
corridor development. No fixture copper is promoted to the integrated board;
no layer policy, clearance rule, or validation severity is relaxed.

## U7 orientation and CM5IO corridor refinement — 2026-09-06

The official-source fixture was extended with an authorized U7 orientation
probe. Native inspection showed that U7 at 0 degrees preserves the CM5IO
source pair ordering, whereas the selected 180-degree orientation reverses
the endpoint order and forces crossing dogbones. The 0-degree, spaced-via
candidate (`PHASE24_USB3_CM5IO_SOURCE_ESCAPE_U7_ROT0_SPACED.kicad_pcb`)
reduced the disposable fixture to 4 total DRC findings: 0 shorts, 2
crossings, 0 clearance, 0 via-dangling, 2 hole-clearance, and 65 expected
fixture opens; all four native USB3 endpoints passed.

A TX_P-only F.Cu continuation variant then removed the hole-clearance and
one crossing class, reaching 3 total findings: 0 shorts, 1 crossing, 0
clearance, 0 hole-clearance, 2 expected dangling TX_P transitions, and 65
expected fixture opens. A further TX_N endpoint dogleg was rejected because
it regressed to 7 findings with 2 clearances; the 3-finding variant remains
the best result and is saved as
`PHASE24_USB3_CM5IO_SOURCE_ESCAPE_U7_ROT0_TXP_FCU.kicad_pcb`.

This is still route-development evidence, not Phase 18 closure: the final
crossing and dangling transitions require correction, and the fixture omits
the remaining storage/support circuitry by design. No integrated copper was
promoted, and the 0-degree orientation is not yet promoted to the acreage
board until the complete USB3/SATA/clock/support island passes together.

## Moved-U7 corridor discriminator — 2026-09-06

To separate the long-corridor integration problem from the CM5IO source
escape, a disposable fixture moved U7 and its USB3 endpoint neighborhood to
`(100,90)` at 0 degrees. The direct local corridor plus restored source-side
NPTH dogleg produced 1 native crossing, 0 shorts, 0 clearance violations, 0
hole-clearance violations, 0 dangling-via findings, and 65 expected fixture
opens; all four native J7↔U7 endpoints passed. The remaining crossing is
between the two TX source dogbones at the B.Cu top channel.

A TX_P F.Cu continuation removed that crossing but shorted an existing U7
`BRIDGE_3V3` pad in the moved endpoint field, so it is rejected as a local
route implementation failure. The `(100,90)` candidate is not promoted yet:
the remaining crossing and the rest of the USB3/SATA/clock/support circuit
still require coordinated validation. No PCIe, power architecture, or
accepted acreage copper changed.

## Final USB3 endpoint-corridor discriminator — 2026-09-06

The TX_N local endpoint dogleg was tested against the best U7-at-0-degree,
TX_P-on-F.Cu candidate. It removed the previous endpoint approach crossing
class but introduced two crossings against the RX B.Cu lanes; it is rejected.
The best retained candidate remains
`PHASE24_USB3_CM5IO_SOURCE_ESCAPE_U7_ROT0_TXP_FCU.kicad_pcb`, with native
DRC counts of 0 shorts, 1 crossing, 0 clearance, 0 hole-clearance, 2
via-dangling warnings, and 65 expected fixture opens. Native
`BuildConnectivity` still passes all four USB3 endpoints. This remains a
route-implementation result, not a Phase 18 promotion; the final crossing
and dangling transitions must be resolved in a complete storage-island
context before acreage integration.

## USB3 cleanpass promotion and integrated collision screen — 2026-09-06

The native zero-DRC disposable source-escape fixture was promoted into a
disposable copy of the selected macro board by moving only U7 to 0 degrees
and copying its saved CM5IO-derived USB3 copper. The focused native endpoint
audit still passes all four J7↔U7 USB3 nets. Whole-board native DRC reports
536 findings, including 4 shorts, 7 `tracks_crossing`, 37 clearance, 9
`via_dangling`, 24 hole-clearance, and 259 unconnected records. The new
USB3-specific interactions include shorts/crossings against the frozen
CM5_PER0_P corridor, crossings against CM5_REFCLK_P and existing power
return copper, and via/zone interaction at the transformed source/end
transitions.

The candidate is rejected for integration as `ROUTE IMPLEMENTATION FAILURE`:
the isolated source escape passed, while the selected-board corridor needs
obstacle-aware reauthoring around PCIe, power, and references. This does not
invalidate the macro-floorplan discriminator or the 0-degree U7 ordering
finding. No accepted acreage copper or PCIe route was changed.

## Whole-board functional-island review re-run — 2026-09-06

Per the steering correction, detailed local USB3 repair was paused and the
whole-board discriminator was rerun against the native-loaded corrected basis.
The review mapped the actual J7 carrier-mating launch regions and compared
Ethernet, PCIe/V100, complete USB3→U7→SATA→J3 storage, SERVICE USB2, power,
and regulator/load-delivery islands. Five disposable macro candidates plus
the PCIe exchange test were generated without routing them.

The closest Ethernet migrations reduced centroid distance from 32.7 mm to
5.1 mm, but their native body envelopes intruded into J7/SERVICE/power
geometry. The outboard alternative reduced the body conflict but retained a
power-corridor conflict and worsened storage proximity. The PCIe exchange
worsened the sensitive PCIe source-to-endpoint distance from 81.2 mm to
119.0 mm. SERVICE is already source-local and is not an exchange target.

The complete placement-only record is
`PHASE24_WHOLE_BOARD_FUNCTIONAL_ISLAND_REVIEW_20260906.md`; generated
candidates and detailed metrics are retained beside it. No candidate was
ranked by mature-board DRC or by immature first-pass route counts.

`MACRO_FLOORPLAN_REVIEW = COMPLETE`
`SELECTED_MACRO = CURRENT_CORRECTED`
`PHASE24_DETAILED_ROUTING = RESUME_AFTER_DISCRIMINATOR`

The west U7 disposable remains a route implementation failure (two native RX
shorts plus two copper-sliver warnings), not macro-placement evidence.

## Reference-route development after macro discriminator — 2026-09-06

The first native-pad A* route on the selected macro was rejected. Although
all four J7↔U7 endpoint assertions passed, its generic 1.5 mm terminal halo
cleared neighboring J7 pads and native DRC reported 375 violations, including
USB3 shorts and crossings. This is a `ROUTE IMPLEMENTATION FAILURE` caused by
an invalid source-escape authoring model; no macro conclusion was drawn.

The already validated CM5IO-derived Phase 18 route was then promoted into a
disposable copy of the corrected macro. Native connectivity passed all four
USB3 endpoints, with zero `shorting_items` and zero `tracks_crossing`. The
candidate added two localized USB3 clearances: the TX_P/TX_N J7 launch
segments are too close, and the RX_N endpoint approach is too close to U7
pad 41. The remaining 450 unconnected records and 63 solder-mask records are
board-baseline/incomplete-board findings; the candidate is not yet a Phase
18 closure.

A bounded RX_N endpoint dogleg/via relocation was attempted after that
evidence. It preserved endpoint connectivity but regressed to six shorts and
one crossing, so it is rejected. This confirms that the next repair should
alter the source/endpoint escape geometry using the official reference
ordering and native pad-field clearances, rather than move the macro island.

Receipts:
`PHASE24_USB3_PHASE18_ORACLE_ON_CORRECTED_MACRO-drc.rpt`,
`PHASE24_USB3_PHASE18_ORACLE_RXN_DOGLEG-drc.rpt`, and
`phase24_usb3_obstacle_aware_native.py`.

## USB3 source/endpoint router discriminator — 2026-09-06

The validated CM5IO-derived route was checked again with `--refill-zones`;
this is required because unfilled full-board zones otherwise produce false
via/zone clearance records. The TX-launch-separated candidate then measured
three total clearance findings, all attributable to the remaining RX_N/U7
endpoint approach plus the two inherited J7 reference violations.

A selected-macro native A* continuation was attempted from explicit source
transition vias to landing vias outside the U7 pad field. It passed all four
native J7↔U7 endpoint assertions, but native DRC found 14 shorts and four
crossings. Inspection showed the authoring defect: source dogbone/via geometry
was not entered into the occupancy map before later lanes were searched, so
later paths entered earlier source transitions. It is rejected as
`ROUTE IMPLEMENTATION FAILURE`; it is not evidence against the macro.

The exact failed candidate is
`PHASE24_USB3_SELECTED_SOURCE_ESCAPE_ASTAR.kicad_pcb` with receipt
`PHASE24_USB3_SELECTED_SOURCE_ESCAPE_ASTAR-drc.rpt`. No accepted board or
PCIe/power copper changed. The next route-development experiment must reserve
every source escape and transition in the native occupancy model and retain
monotonic pair ordering before any integrated promotion.

## Selected-macro source-escape continuation — 2026-09-06

The source-transition occupancy bug was corrected and a spread-via variant
was tested on the selected macro. Native endpoint connectivity passed all
four USB3 pairs, but native DRC still reported one crossing and six
clearances: the source-via spread now avoids true shorts, while the fixed
landing/dogbone choices conflict with the U7 pad field and one existing
PCIe-adjacent corridor. This is retained as a rejected
`ROUTE IMPLEMENTATION FAILURE`.

The experiment did not move the selected macro or alter accepted PCIe,
power, stack, or validation severity. The next valid cycle is a coordinated
U7/storage-island endpoint escape or a complete storage-island placement
trial, with all affected USB3/SATA/clock/support geometry revalidated
together. The historical route remains an oracle only; no raw mature-board
DRC comparison is being used to rank the floorplan.

## Coherent storage SATA bridge escape discriminator — 2026-09-06

The coherent storage candidate
`PHASE24_STORAGE_ISLAND_COHERENT_USB3_SATA_BRIDGE_ESCAPE_FIELD_AWARE.kicad_pcb`
was used for a native U7-to-coupling-capacitor escape trial. The first
direct-pad trial was rejected with U7 pad-field shorts/crossings. A second
field-aware trial left the U7 row vertically and reduced the candidate to
one inherited USB3-corridor crossing plus the board-baseline findings; the
crossing is between the proposed RX_N transition and the already-authored
USB3 corridor. A right-side detour variant then collided with existing
PCIe/PERST corridors and was also rejected. Native DRC counts for the
field-aware candidate are 179 violations and 446 unconnected items; this is
not a complete SATA route and does not close Phase 19 or Phase 24.

Both USB3 native endpoint assertions and the U7 pad-net authority audit pass
on the field-aware candidate. The failures are therefore classified as
`ROUTE IMPLEMENTATION FAILURE`, not a storage-architecture or macro-placement
failure. No accepted PCIe/power copper or clean-board authority was changed.
The next experiment must use an obstacle-aware complete SATA bridge-to-J3
escape, or transplant/adapt the preserved native SATA route while explicitly
avoiding the USB3 and PCIe corridors; it must validate all four bridge and
all four M.2 endpoints before promotion.

Receipts:
`PHASE24_STORAGE_ISLAND_COHERENT_USB3_SATA_BRIDGE_ESCAPE-drc.rpt`,
`PHASE24_STORAGE_ISLAND_COHERENT_USB3_SATA_BRIDGE_ESCAPE_FIELD_AWARE-drc.rpt`,
`phase24_sata_bridge_pad_escape.py`, and
`phase24_sata_bridge_pad_escape_field_aware.py`.

## Native storage-route oracle transplant — 2026-09-06

The preserved native Phase 19 USB3/SATA route was transplanted into a
disposable copy of the coherent storage base, moving U7, J3, and C30-C33 as
one data-island placement. The complete eight-net SATA path and four-net
CM5-to-U7 USB3 path pass native KiCad connectivity assertions. Native DRC
reports 177 findings and 442 unconnected items, but no `shorting_items`, no
`tracks_crossing`, and no SATA-specific clearance or dangling-via finding.
The three clearance findings are inherited CM5 USB3/reference-launch issues;
the remaining findings are incomplete-board baseline findings.

This is the strongest current storage routing candidate, but it is not yet
promoted or declared closed: the U7 power/clock/support neighborhood and
full-board open/short/parity gates still require revalidation, and the native
route's pair-length metrics must be checked against the Phase 24 SI limits.
The route itself is classified as a successful implementation discriminator,
not a Phase 24 pass.

The SATA audit derives connectivity from saved native pads, tracks, and vias;
its expected endpoint table is assertion-only. A disposable negative control
removing one required SATA trace fails as expected.

Receipts:
`PHASE24_STORAGE_NATIVE_ORACLE_TRANSPLANT-drc.rpt`,
`phase24_transplant_native_storage_oracle.py`,
`phase24_sata_native_connectivity_audit.py`, and
`phase24_sata_native_connectivity_negative_control.py`.

## U7 support-oracle integration discriminator — 2026-09-06

The proven U7 support/clock/3V3 copper from
`PHASE24_U7_STORAGE_3V3_PAD24_CURRENT.kicad_pcb` was transplanted into the
native data-route oracle, with C16/C17/C19 and Y1/R23/C42/C43 moved as a
support group. Native DRC exposed one true short: the support placement at
C19 conflicts with the transplanted CM5 USB3 TX_N corridor. The support
donor remains valid in its own coordinated context; the failure is a
`ROUTE_IMPLEMENTATION_FAILURE` caused by combining independently developed
placement/routing contexts, not evidence against the U7 storage architecture
or the proven SATA data route. The data-route oracle remains unchanged and
accepted as the current storage data reference.

Receipt:
`PHASE24_STORAGE_NATIVE_ORACLE_SUPPORT_TRANSPLANT-drc.rpt` and
`phase24_transplant_u7_support_oracle.py`.

## Coordinated U7 USB3/support escape attempts — 2026-09-06

Two local repairs were tested against the combined U7 support/data candidate.
Moving USB3 TX_N's long leg to B.Cu avoided the C19 top-side short but
introduced a native crossing with the PCIe B.Cu corridor and multiple
oscillator-return conflicts. Moving TX_N on F.Cu around C19 instead created
crossings with the transplanted RX_P lane and a clock-via short. Both
variants preserved native USB3 and SATA endpoint assertions but failed native
DRC, and are rejected as `ROUTE_IMPLEMENTATION_FAILURE`.

The evidence narrows the next repair to a coordinated local escape: reserve
the U7 USB3 pad-field ordering, clock return vias, and support-cap placement
in one occupancy model, then regenerate the affected USB3 route. No accepted
PCIe or storage data-route authority was altered.

Receipts:
`PHASE24_STORAGE_NATIVE_ORACLE_SUPPORT_TXN_BCU_REPAIR-drc.rpt`,
`PHASE24_STORAGE_NATIVE_ORACLE_SUPPORT_TXN_FCU_AROUND_C19-drc.rpt`,
`phase24_support_usb3_txn_bcu_repair.py`, and
`phase24_support_usb3_txn_fcu_around_c19.py`.

## Underside U7 support-cap discriminator — 2026-09-06

A true KiCad underside flip of C19 was tested in the combined support/data
candidate. It removes the prior C19-to-USB3 short without changing the
support net identity. Native DRC reports no shorts and no track crossings;
the candidate retains only the three inherited CM5 launch clearances among
its high-speed copper findings. Native USB3 and all eight SATA endpoint
assertions pass. The oscillator network is natively joined through U7.52/.53/.54,
and the reset/3V3 U7 pad fields are connected.

C19 underside placement remains provisional pending the full mechanical,
power-return, decoupling, and board-level parity gates. The remaining U7
power-cap connectivity is not being inferred from the data-route PASS and
must be closed from actual plane/track/pad contact. This candidate is the
current coordinated storage basis, not a Phase 24 closure.

Receipts:
`PHASE24_STORAGE_NATIVE_ORACLE_SUPPORT_C19_BOTTOM_FLIPPED-drc.rpt` and
`phase24_u7_support_c19_bottom_flip.py`.

The underside mechanical spot check found C19 at `(107.0,118.0)` on B.Cu,
with no nearby B.Cu component body or verified mounting feature within the
local 12 mm review radius. This is only local evidence; enclosure, M.2,
standoff, and assembly-side checks remain part of the later full-board gate.

## U7 supply hierarchy authority audit — 2026-09-06

The authoritative saved schematic/netlist was audited before adding copper.
`STORAGE.kicad_sch` has no hierarchical ports named `BRIDGE_3V3` or
`BRIDGE_1V1`; `REGULATORS.kicad_sch` likewise has neither port. The root
sheet exports `STORAGE_3V3` and `BRIDGE_1V1_3V3`, but not the two separate
bridge rails required by U7. The netlist consequently contains distinct
`/STORAGE/BRIDGE_3V3`, `/STORAGE/BRIDGE_1V1`, `/REGULATORS/BRIDGE_3V3`, and
`/REGULATORS/BRIDGE_1V1` nets with no authoritative join. This explains why
the board candidate's U7 supply pads and regulator decouplers cannot be
closed by valid PCB copper alone.

No synthetic net join was added. This is now the earliest unresolved Phase
24 authority defect: the minimum safe continuation is a native hierarchy-port
repair that explicitly maps both bridge rails between STORAGE and REGULATORS,
followed by schematic/netlist/PCB regeneration and revalidation. Until that
repair is made, U7 power closure and full Phase 24 closure remain open.

Receipt:
`phase24_u7_supply_hierarchy_audit.py`.

## U7 bridge-supply hierarchy repair proof and application — 2026-09-06

The missing U7 supply authority was repaired in the native schematic authoring
path. A disposable native KiCad fixture first added explicit `BRIDGE_3V3` and
`BRIDGE_1V1` hierarchical ports at both the STORAGE and REGULATORS children,
with real child-sheet wires to the existing local rail coordinates and root
sheet wires/global labels. KiCad's own netlist export then produced one
unscoped `BRIDGE_3V3` net containing the U7 supply/configuration pads and the
regulator/support members, and one unscoped `BRIDGE_1V1` net containing U7.41
and the regulator/load decoupling members. This is native hierarchy evidence,
not a PCB graph edge or synthetic net join.

The same edit was applied to the production clean schematic sources. Native
`kicad-cli sch export netlist` succeeds for the saved clean root, and its
export contains the merged bridge rails. Native ERC still returns the existing
project-wide violations (632 messages in this run), but a targeted search finds
no hierarchical sheet-pin, hierarchy, or sheet-pin association errors. ERC
therefore proves the repaired hierarchy association while not constituting a
full-project ERC pass.

Phase 24 remains open. The current PCB candidates were authored against the
pre-repair hierarchical net identities, so the next action is to regenerate or
authoritatively re-net the selected storage PCB from this corrected schematic,
then rerun U7 supply, clock, native connectivity, parity, DRC, and full-board
closure checks. No Phase 25/26 work has started.

Receipts:
`phase24_probe_bridge_supply_hierarchy.py`,
`PHASE24_CLEAN_HIERARCHY_REPAIRED.xml`, and
`PHASE24_CLEAN_HIERARCHY_REPAIRED-erc.rpt`.

## PCB synchronization discriminator after hierarchy repair — 2026-09-06

The first PCB-side synchronization trial was deliberately authority-checked
against the repaired native netlist before changing rail ownership. The
selected storage candidate contains stale `/STORAGE/BRIDGE_3V3` and
`/STORAGE/BRIDGE_1V1` names, which can be normalized for the authoritative U7
members. It also contains U7.3 assigned to `/STORAGE/BRIDGE_1V1`, but the TI
TUSB9261 Rev-I pin table identifies pin 3 as PWM1; the clean schematic does
not use that optional pin. The synchronization therefore clears U7.3 to no
net rather than incorrectly joining it to the 1.1-V rail. This is a real
schematic-to-footprint mapping defect exposed by the new authority, not a
routing failure.

The trial reassigned 36 authoritative bridge-rail pads and saved a disposable
candidate. Native DRC then exposed one additional pre-existing board-only
TP5 route ending on a no-net test pad, so that disposable result is rejected;
no PCB candidate is promoted. The native DRC still has zero track crossings,
but it has one short between `BRIDGE_3V3` and the no-net TP5 pad. The next
action is to remove or explicitly authorise that test-point circuit from the
schematic, then rerun net synchronization and the U7 power/connectivity/parity
audits. This preserves fail-closed validation and does not claim Phase 24
closure.

Receipt:
`phase24_sync_bridge_supply_nets.py` and
`PHASE24_STORAGE_NATIVE_ORACLE_SUPPORT_C19_BOTTOM_FLIPPED_HIERARCHY_SYNC-drc.rpt`.

## Authoritative U7 PCB sync and unsourced probe removal — 2026-09-06

The stale U7.3 assignment was corrected to no-net, while U7.24/U7.30/U7.31
were assigned to the native `BRIDGE_3V3` net and U7.41 to native
`BRIDGE_1V1`. The selected candidate also contained TP5, a board-only probe
absent from the saved schematic, with an explicit bridge-rail route ending at
its no-net pad. That probe and only its two launch segments were removed from
the disposable candidate; the adjacent bridge-rail grid was retained.

The resulting candidate has zero native shorting items and zero track
crossings. Native USB3 endpoint connectivity remains PASS for all four pairs,
and native SATA endpoint connectivity remains PASS for all eight endpoints.
The candidate still has inherited full-board DRC findings (184 violations,
429 unconnected items), so it is not promoted or called a Phase 24 pass. The
updated hierarchy audit now passes against the saved repaired KiCad XML, and
the next required work is full-board schematic-to-pad parity plus actual U7
power-plane/return closure.

Receipts:
`phase24_sync_bridge_supply_nets.py`,
`phase24_remove_unsourced_tp5_route.py`,
`phase24_u7_supply_hierarchy_audit.py`, and
`PHASE24_STORAGE_NATIVE_ORACLE_SUPPORT_C19_BOTTOM_FLIPPED_HIERARCHY_SYNC_TP5_REMOVED-drc.rpt`.

## U7 package-pin authority follow-up — 2026-09-06

The repaired-netlist U7 pad audit is intentionally fail-closed on the
disposable board. In addition to the corrected U7.3 PWM1 stale assignment,
the candidate assigns `/STORAGE/BRIDGE_CFG` to U7.1 and
`/STORAGE/BRIDGE_SATA_RX_N` to U7.5--U7.9, although the native schematic
netlist has no such U7 nodes. TI's TUSB9261 Rev-I pin table identifies these
physical pins as VDD/GPIO pins, while the actual SATA receive pins are 59/60
and bridge configuration is pin 21. Therefore the prior local connectivity
audits were insufficient: they proved the intended endpoint pads, but did not
prove the complete package pin field was authoritatively mapped.

This is now classified as a `SCHEMATIC_FOOTPRINT_AUTHORITY` defect, not a
route implementation failure. The next repair must expose or otherwise
authoritatively represent the TUSB9261 power, ground, GPIO/PWM, and NC pins
in the clean symbol and regenerate the U7 footprint net assignment from that
source. No PCB-only reassignment of U7.1/U7.5--U7.9 is accepted. Phase 24
remains open and no acreage candidate is promoted.

Receipt:
`phase24_u7_pad_net_authority_audit.py` and
the TI `TUSB9261-datasheet-revI.pdf` retained under
`authority-inventory/primary-docs/tusb9261/`.

## TI PVP0064A U7 footprint authority fixture — 2026-09-06

The retained TI TUSB9261 Rev-I package drawing was checked directly. It
specifies the PVP0064A HTQFP land pattern at 0.4 mm pitch with 1.2 mm by
0.2 mm perimeter lands, an approximately 8.5 mm land-pattern envelope, and
an exposed thermal pad 65 in the 3.321--3.581 mm range. The prior clean
`TUSB9261IPVP_HTQFP64` asset uses 0.5 mm pitch, has no pad 65, and is marked
as requiring final fab-library review; it cannot be treated as manufacturer
authoritative.

`phase24_generate_ti_u7_authoritative_footprint.py` now generates a
disposable `TUSB9261IPVP_PVP0064A` footprint basis from those dimensions.
KiCad 10.0.5 loads it with all 65 pads and the expected 3.45 mm exposed-pad
metal. The exposed-pad paste segmentation is intentionally not guessed and
therefore remains a fabrication/stencil review item. This asset is evidence
for the correction path, not a promoted production footprint.

The complete U7 authority repair remains open: the clean symbol must represent
the TI-required VDD/VDD33/VDDA33/VSS pins and the resulting schematic must be
regenerated into a correctly mapped footprint before any U7 route is accepted.

Receipt:
`phase24_generate_ti_u7_authoritative_footprint.py` and
`PiSXMe_RevA_Clean.pretty/TUSB9261IPVP_PVP0064A.kicad_mod`.

## TUSB9261 mandatory pin-contract audit — 2026-09-06

The native clean netlist currently represents only 17 U7 pins. Comparing it
with the TI Rev-I signal/power tables shows that the symbol/netlist is missing
mandatory package authority for VDD pins 1, 12, 19, 32, 33, 47, 49, 55, 61,
and 63; VDD33 pins 7 and 51; VDDA33 pins 34, 40, 48, and 62; USB_VBUS pin
50; USB2 pins 35/36; USB_R1/R1RTN pins 38/39; VSS pins 44/58; and exposed
thermal pad 65. Pin 53 is represented, but remains intentionally classified
as the oscillator-ground connection requiring its documented treatment.

`phase24_u7_ti_pin_contract_audit.py` fails with that exact missing-pin list.
This confirms the footprint discrepancy is coupled to an incomplete schematic
component contract; it is not safe to repair the PCB by assigning nets to
unrepresented pads. The next implementation step is to expand U7's clean
symbol and support network from the TI pin contract, then export a fresh
native netlist and regenerate the PCB mapping. Phase 24 remains open.

Receipt:
`phase24_u7_ti_pin_contract_audit.py`.

## Native complete U7 pin-field expansion — 2026-09-06

The disposable symbol expansion was promoted to the production clean STORAGE
sheet after native validation. U7 now represents the TI-required VDD, VDD33,
VDDA33, VSS, USB_VBUS, USB2, USB_R1/R1RTN, oscillator, signal, and exposed
thermal-pad pins. Native KiCad netlist export succeeds and contains 41 U7
nodes, including every mandatory pin in the TI contract. Native ERC reports
the existing project-wide violations (636 messages in this run), but targeted
hierarchy searches report no hierarchical sheet-pin or hierarchy-association
errors.

The new U7 support labels are explicit: VDD uses `BRIDGE_1V1`, VDD33/VDDA33
use `BRIDGE_3V3`, VSS and pad 65 use `POWER_GND`, USB VBUS uses `CM5_5V`, and
the USB2/reference pins have named local nets pending their support components.
This is an authority correction, not a waiver of those remaining support
circuits.

The U7 pad and mandatory-pin audits now consume
`PHASE24_CLEAN_TUSB_PINFIELD.kicadxml`. PCB regeneration is the next step;
existing routed candidates remain invalid until their footprint geometry,
complete pin ownership, support components, and native connectivity are
rebuilt against this source.

Receipts:
`phase24_expand_u7_ti_pinfield_fixture.py`,
`PHASE24_CLEAN_TUSB_PINFIELD.kicadxml`, and
`PHASE24_CLEAN_TUSB_PINFIELD-erc.rpt`.

## U7 footprint authoring-path correction — 2026-09-06

The Phase 14 footprint authoring path was updated so future clean-generation
runs no longer recreate the rejected generic 0.5 mm/64-pad U7 asset. It now
invokes the dedicated TI PVP0064A generator, assigns
`TUSB9261IPVP_PVP0064A`, and the Phase 14 regression test checks for all 65
pads. The production STORAGE symbol footprint field was updated to the new
asset and the Phase 14 footprint-authority test passes.

This corrects footprint selection and reproducibility only. It does not claim
that U7 is yet electrically complete: the symbol pin field is now present, but
the newly named USB2/reference support circuits and fresh routed PCB have not
yet been regenerated and validated. Phase 24 remains open.

Receipt:
`phase14_footprint_authority.py`,
`validation/phase3/test_phase14_footprint_authority.py`, and the passing test
output from 2026-09-06.

## TI-footprint replacement on storage PCB — 2026-09-06

The disposable `phase24_replace_u7_with_ti_footprint_fixture.py` replaced
only U7 in the latest storage candidate with the 65-pad TI PVP0064A footprint
and assigned all 41 U7 pad nets from the native repaired netlist. The complete
U7 pad-authority audit passes, proving the new footprint/net ownership is
consistent with the expanded schematic.

The inherited routes were authored against the rejected 0.5 mm footprint and
cannot be reused as-is. Native DRC on the replacement fixture finds 486
violations, including old copper terminating on the new pad field; USB3 and
SATA endpoint audits fail at the relocated U7 pads. This is
`ROUTE_IMPLEMENTATION_FAILURE`, not evidence against the TI footprint or the
storage architecture. The fixture is not promoted. Fresh obstacle-aware U7
USB3/SATA escapes must be generated against the TI pad coordinates, with all
support/power pins retained.

Receipt:
`phase24_replace_u7_with_ti_footprint_fixture.py` and
`PHASE24_STORAGE_TI_PINFIELD_REPLACED-drc.rpt`.

## Fresh-route basis with TI U7 pad geometry — 2026-09-06

`phase24_sync_u7_route_names.py` normalized the retained storage candidate's
USB3 aliases from `/CORE_CM5/...` to the native repaired netlist names and
cleared unsourced U7 pad assignments. The complete U7 pad-authority audit
still passes after synchronization. Native DRC remains at 486 violations and
449 unconnected items, with old copper now visibly terminating at the new
0.4 mm TI pad field; native SATA endpoint connectivity fails at U7.57 and
USB3 endpoint validation still uses the old route geometry.

This is a preserved `ROUTE_IMPLEMENTATION_FAILURE`: the experiment confirms
the schematic/footprint authority can be synchronized without synthetic graph
edges, but the prior route cannot be transplanted across the package change.
The next route attempt must regenerate the U7 USB3/SATA escapes from actual
TI pad coordinates and include the newly represented support/power pads. The
old storage route remains donor evidence only; Phase 24 is open.

Receipt:
`phase24_sync_u7_route_names.py` and
`PHASE24_STORAGE_TI_PINFIELD_REPLACED_ROUTE_NAMES-drc.rpt`.

## TUSB9261 precision-reference support added — 2026-09-06

The TI implementation guide requires a 10-kOhm, 1% precision resistor no
farther than 500 mil from USB_R1 (pin 38) to USB_R1RTN (pin 39). The clean
STORAGE sheet now includes R24, `RC0402FR-0710KL`, with explicit
`BRIDGE_R1` and `BRIDGE_R1RTN` connections to those native U7 pins. Native
netlist export shows both exact two-member nets, and the mandatory TI pin
contract audit passes with no missing pins. Native ERC still reports the
pre-existing project-wide findings (635 in this run), with no targeted
hierarchy-association errors.

USB_VBUS divider/support and fresh U7 PCB routing remain open; this resistor
addition is not being represented as completed hardware support until those
circuits and the regenerated PCB pass native validation.

Receipts:
`PHASE24_CLEAN_TUSB_PINFIELD_R1.kicadxml`,
`PHASE24_CLEAN_TUSB_PINFIELD_R1-erc.rpt`, and the TI
`TUSB9261-implementation-guide-revE.pdf`.

## TUSB9261 USB_VBUS divider support added — 2026-09-06

The TI implementation guide requires USB_VBUS to be driven through a 90.9 kOhm,
1% upper resistor and a 10 kOhm, 1% lower resistor to ground. The clean
STORAGE sheet now includes R32 (`RC0402FR-0790K9L`) from `CM5_5V` to the
native U7 pin-50 net `BRIDGE_USB_VBUS`, and R33 (`RC0402FR-0710KL`) from that
node to `POWER_GND`. The references were selected after checking the complete
clean hierarchy for duplicates.

Native KiCad export proves the exact three-member VBUS node (U7.50, R32.2,
R33.1), the CM5_5V source node (R32.1), and the POWER_GND return (R33.2 plus
the U7 ground pins). Native ERC remains project-wide nonzero (637 existing
messages) but has no targeted hierarchy/association errors. The VBUS support
network is now represented authoritatively; PCB materialization and routing
remain open.

Receipts:
`phase24_rename_storage_vbus_refs.py`,
`PHASE24_CLEAN_TUSB_VBUS_DIVIDER.kicadxml`, and
`PHASE24_CLEAN_TUSB_VBUS_DIVIDER-erc.rpt`.

## U7 support materialization and fresh-route discriminator — 2026-09-06

`phase24_materialize_u7_support_from_netlist.py` materialized R32/R33 and the
TI U7 pad ownership from `PHASE24_CLEAN_TUSB_VBUS_DIVIDER.kicadxml` onto a
disposable replacement board. The TI pad-authority audit and mandatory-pin
contract both pass against the latest VBUS-inclusive native export.

The first USB3 A* regeneration reaches all four native TI USB3 pads, but its
inherited-board DRC is not a pass and is not promoted. A subsequent SATA A*
discriminator reaches all eight SATA endpoints and the native SATA endpoint
audit passes; DRC still reports implementation defects, including pair
clearance/crossing and stale neighboring copper interactions. These are
`ROUTE_IMPLEMENTATION_FAILURE` results against the new package geometry, not
evidence to reject the TI footprint or storage architecture. The regenerated
fixtures are disposable and Phase 24 remains open pending clean local escape
authoring and support-circuit routing.

Receipts:
`phase24_materialize_u7_support_from_netlist.py`,
`PHASE24_STORAGE_TI_PINFIELD_SUPPORT_MATERIALIZED.kicad_pcb`,
`PHASE24_STORAGE_TI_PINFIELD_SUPPORT_USB3_ASTAR.kicad_pcb`,
`PHASE24_STORAGE_TI_PINFIELD_SUPPORT_USB3_SATA_ASTAR.kicad_pcb`, and
`PHASE24_STORAGE_TI_PINFIELD_SUPPORT_USB3_SATA_ASTAR-drc.rpt`.

## Canonical USB3 source-net normalization — 2026-09-06

The first fresh USB3 route exposed a second implementation defect: retained
PCB J7 pads still used the pre-repair `/CORE_CM5/CM5_USB3_*` aliases while the
authoritative TI U7 pads used `CM5_USB3_*`. The route generator was corrected
to assign J7 pads from the native net names before creating copper, preventing
split PCB identities for one USB3 channel.

The corrected disposable regeneration reaches all four canonical J7-to-U7
USB3 endpoints, all eight native SATA endpoints still pass, and U7 pad
authority passes. Native DRC reports 730 violations/448 unconnected items,
down from 736/448 in the prior same-basis route, so this remains
`ROUTE_IMPLEMENTATION_FAILURE`: the remaining defects include local pair
clearance/crossing and inherited-board corridor interactions. The fixture is
not promoted and Phase 24 remains open.

Receipt: `phase24_reroute_storage_usb3_native.py` and
`PHASE24_STORAGE_TI_VBUS_REAUTH_SUPPORT_USB3_CANONICAL_SATA-drc.rpt`.

## Isolated TI-U7 route-development boundary — 2026-09-06

`phase24_make_ti_storage_isolated_fixture.py` now creates a disposable native
route-development board containing only J7, the TI U7, J3, and authoritative
storage/support footprints. This prevents inherited acreage copper from being
used as direct evidence against the corrected package escape. The isolated
fixture reproduces the same native endpoint result: four USB3 and eight SATA
paths can be represented, but the current A* geometry still fails DRC with
local pair crossings, pad-field clearance, and support-copper interactions.
Those findings remain route-authoring failures; the isolated fixture is not
promoted. A clean next route must solve the local TI pad-field escape and keep
support returns outside its corridor before integration.

Receipt: `phase24_make_ti_storage_isolated_fixture.py` and
`PHASE24_TI_STORAGE_ISOLATED_USB3_SATA-drc.rpt`.

## TI PVP0064A rotation correction and ordered escape — 2026-09-06

Native DRC of the first TI footprint replacement exposed a footprint-authoring
defect: the 1.2 mm x 0.2 mm lands were rotated on the vertical sides, making
the 0.4 mm-pitch row overlap. The generator now keeps vertical-side lands at
rotation 0 and rotates only the horizontal-side lands. Replacing U7 with this
corrected asset reduces the unchanged inherited-candidate DRC from 488 to 213
before route regeneration, while the native TI pad-authority and mandatory-pin
audits continue to pass.

The disposable ordered escape then reduces local route-development DRC to 103
violations and preserves native endpoint connectivity for all four USB3 and
all eight SATA paths. It is still rejected as a route pass: remaining issues
are explicit pair crossings/clearances and connector launch keepouts. This is
now a valid package geometry and a useful route-development basis; prior
failures caused by the malformed land rotations are superseded.

Receipts: `phase24_generate_ti_u7_authoritative_footprint.py`,
`phase24_ti_u7_ordered_escape_fixture.py`, and
`PHASE24_TI_STORAGE_ORDERED_ESCAPE-drc.rpt`.

## Whole-board macro-floorplan discriminator and controlled selection — 2026-09-06

Per the steering correction, local Phase 24 routing experiments were paused
and the whole-board functional-island question was re-evaluated from the
native-loaded `PHASE24_U7_3V3_CURRENT_LOCAL.kicad_pcb`. The CM5 J7 source
groups were extracted after native transforms: Ethernet `(34.50,99.90)`,
PCIe `(69.60,101.50)`, USB3-storage `(70.04,105.30)`, and SERVICE
`(66.96,99.30)`. The review included complete Ethernet, PCIe/V100, storage
USB3->U7->SATA->J3 plus clock/support, SERVICE, power-entry/protection, and
regulator/load-delivery neighborhoods.

The placement comparison intentionally excluded existing route maturity,
DRC count, and open count. Multiple disposable native candidates were
generated and compared using transformed pad centroids, Euclidean/Manhattan
source distance, same-net ratsnest length, coarse body-box overlap, anchor
preservation, and corridor topology. `SWAP_ETH_STORAGE` was selected over
the current topology: Ethernet source distance falls from 59.2 mm to 22.5 mm
and storage source distance from 65.9 mm to 49.5 mm, while the selected swap
has zero coarse major-body overlaps and preserves PCIe, SERVICE, power, and
regulator anchors. `ETH_LOCAL_STORAGE_MID` was rejected by its native
body-box conflicts despite shorter distances.

The live basis was snapshotted as
`PHASE24_MACRO_REVIEW_LIVE_BASIS_20260906.kicad_pcb`. The selected disposable
macro basis is `PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE.kicad_pcb`; only
Ethernet/storage high-speed copper invalidated by coherent island moves was
removed. Native inspection confirmed J7/J1/J4 and the power/regulator
anchors are unchanged. Native DRC reports 287 violations and 459
unconnected items on this intentionally unrouted basis, classified as
`ROUTE_IMPLEMENTATION_FAILURE` and not used to rank the floorplan.

Consultant dispatch was attempted for the required independent review and
failed with `collab spawn failed: agent thread limit reached`; local native
geometry review completed the discriminator without retrying that unchanged
tooling failure. The next action is a fair, obstacle-aware route-development
cycle on the selected topology, followed by affected-subsystem revalidation.

Receipt: `phase24_whole_board_macro_floorplan_discriminator.py`,
`PHASE24_WHOLE_BOARD_MACRO_DISCRIMINATOR_20260906.md`,
`PHASE24_MACRO_REVIEW_LIVE_BASIS_20260906.kicad_pcb`, and
`PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE.kicad_pcb`.

## Selected macro storage route-development cycle 1 — 2026-09-06

The selected `SWAP_ETH_STORAGE` basis was reduced to a native isolated
storage fixture and regenerated against the actual bridge/socket pads. The
native SATA endpoint audit passes all eight required memberships:
U7-to-coupling-cap for TX/RX and coupling-cap-to-J3 for all four M.2 SATA
pairs. This proves the new placement has a representable endpoint topology;
it does not prove route quality.

Native DRC rejects the first SATA route implementation with 108 violations
and 84 unconnected items, including actual same-net-pair crossing/shorting
and clearance findings. The candidate is rejected as
`ROUTE_IMPLEMENTATION_FAILURE`, not `MACRO-PLACEMENT FAILURE`; the old
historical board was not used as a raw DRC comparator. The next cycle must
repair obstacle-aware SATA escape geometry on the selected macro basis and
then regenerate USB3 from the same moved U7 placement before integration.

Receipts: `PHASE24_SELECTED_MACRO_SWAP_STORAGE_ISOLATED.kicad_pcb`,
`PHASE24_SELECTED_MACRO_SWAP_STORAGE_SATA_ASTAR.kicad_pcb`,
`PHASE24_SELECTED_MACRO_SWAP_STORAGE_SATA_ASTAR-drc.rpt`, and
`phase24_sata_native_connectivity_audit.py`.

## Selected macro storage route-development cycle 2 — 2026-09-06

The native route generators were generalized to accept the selected macro
basis and resolve the saved hierarchical CM5/STORAGE net names without
creating synthetic connectivity. A second ordered USB3/SATA escape was run
from `PHASE24_SELECTED_MACRO_SWAP_STORAGE_ISOLATED.kicad_pcb`.

The USB3 A* output reaches all four native J7-to-U7 terminal pairs, while
native DRC rejects it with 217 violations and 88 unconnected items. The
ordered SATA output again passes all eight native SATA endpoint memberships,
but native DRC rejects the geometry with 112 violations and 80 unconnected
items, including real crossings/shorting/clearance findings. These are
`ROUTE_IMPLEMENTATION_FAILURE` results on an immature disposable route, not
evidence against the selected macro placement. No integrated copper or
production candidate was changed.

Receipts: `phase24_reroute_storage_usb3_native.py`,
`phase24_ti_u7_ordered_escape_fixture.py`,
`PHASE24_SELECTED_MACRO_SWAP_STORAGE_USB3_ASTAR.kicad_pcb`,
`PHASE24_SELECTED_MACRO_SWAP_STORAGE_USB3_ASTAR-drc.rpt`,
`PHASE24_SELECTED_MACRO_SWAP_STORAGE_ORDERED_ESCAPE.kicad_pcb`, and
`PHASE24_SELECTED_MACRO_SWAP_STORAGE_ORDERED_ESCAPE-drc.rpt`.

## Selected macro USB3 pair-corridor cycle 3 — 2026-09-06

The A* route class was replaced with an explicit pair-preserving monotonic
corridor based on native transformed pad coordinates. The four source-to-TI
USB3 pairs now all pass the native endpoint audit. The accepted route shape
uses ordered F.Cu corridors, no vias, and the selected U7 position; measured
track lengths are RX_N 41.56 mm, RX_P 41.66 mm, TX_N 40.66 mm, and TX_P
40.76 mm. Native DRC reports no `tracks_crossing`, `shorting_items`, or
high-speed clearance category on this candidate.

The fixture-wide DRC still reports 74 findings: 88 unconnected items from
the intentionally incomplete support/connector fixture and 63 inherited
J3 solder-mask bridge findings, plus unrelated silkscreen/text findings.
Those are not waived; this is a channel-level route-development result and
does not close USB3 or Phase 24. The candidate is retained as the current
USB3 escape method and the next work is a compatible SATA pair corridor and
complete support-circuit integration.

Receipt: `phase24_storage_usb3_pair_corridor.py`,
`PHASE24_SELECTED_MACRO_SWAP_STORAGE_USB3_PAIR_CORRIDOR_V3.kicad_pcb`,
`PHASE24_SELECTED_MACRO_SWAP_STORAGE_USB3_PAIR_CORRIDOR_V3-drc.rpt`, and
`phase24_usb3_native_connectivity_audit.py`.

## Selected macro SATA pair-corridor development — 2026-09-06

Several explicit native SATA corridor constructions were tested on the
selected macro storage island. Every construction passes the authoritative
eight-endpoint SATA connectivity audit through U7, all four coupling
capacitors, and J3. The attempts remain rejected for route quality: the best
current trial still contains six real track crossings and four true shorts,
principally from bridge-pad fanout ordering, the J3 connector launch field,
and local support footprints occupying the trial corridor.

These are `ROUTE_IMPLEMENTATION_FAILURE` results, not
`MACRO-PLACEMENT FAILURE`. The selected placement has not been changed and
no SATA copper has been promoted to the integrated board. The next action is
to use the native violation coordinates to refine the local bridge/socket
launch or rotate the coherent storage island, rather than compare these
immature routes against the mature historical board by raw DRC totals.

Receipts: `phase24_storage_sata_pair_corridor.py`,
`PHASE24_SELECTED_MACRO_SWAP_STORAGE_SATA_PAIR_CORRIDOR_V2.kicad_pcb`,
`PHASE24_SELECTED_MACRO_SWAP_STORAGE_SATA_PAIR_CORRIDOR_V3.kicad_pcb`,
`PHASE24_SELECTED_MACRO_SWAP_STORAGE_SATA_PAIR_CORRIDOR_V4.kicad_pcb`,
`PHASE24_SELECTED_MACRO_SWAP_STORAGE_SATA_PAIR_CORRIDOR_V5.kicad_pcb`,
and their native DRC reports.

## Storage orientation discriminator — 2026-09-06

The next solution class was a coherent U7/J3 orientation change. Native pad
coordinates were compared for `U7_180_J3_90`, `U7_0_J3_270`, and
`U7_270_J3_270`. The 0-degree U7/270-degree J3 candidate makes the SATA
pair order monotonic, but its native USB3 trial still creates three real
crossings, six true/field shorts around the U7 field, and J3/J7
hole-clearance conflicts. It is rejected as an orientation-level
route/mechanical candidate. The selected U7 180-degree/J3 90-degree basis
remains active because its USB3 pair-corridor trial passes all four native
endpoints with no high-speed crossings, shorts, or clearance findings.

This comparison does not use raw DRC totals against the mature historical
board. It distinguishes the tested alternate's concrete local
implementation/mechanical failures from the macro-floorplan decision.

Receipt: `phase24_storage_orientation_discriminator.py`,
`PHASE24_STORAGE_ORIENTATION_DISCRIMINATOR_20260906.md`,
`PHASE24_STORAGE_ORIENTATION_U7_0_J3_270_USB3_PAIR.kicad_pcb`, and
`PHASE24_STORAGE_ORIENTATION_U7_0_J3_270_USB3_PAIR-drc.rpt`.

The Phase 14 footprint-authority regression now also checks the four side
orientations, so future regeneration cannot silently restore the overlapping
vertical-land error.

## SATA source-ordered capacitor placement trial — 2026-09-06

V9/V10 tested a source-ordered coupling-capacitor arrangement intended to
make the M.2 socket launch monotonic. Native DRC rejected V10 with 96
violations. The actionable findings are a B.Cu TX_N/RX_N crossing at the
right launch, a TX_P via entering the M.2 no-net field, and a bridge TX_P
escape crossing the U7 USB3 pad field. This is `ROUTE IMPLEMENTATION FAILURE`:
the candidate received a distinct placement/escape implementation cycle, but
the selected SWAP_ETH_STORAGE macro topology is not being rejected.

The V10 board and DRC receipt are preserved as
`PHASE24_SELECTED_MACRO_SWAP_STORAGE_SATA_PAIR_CORRIDOR_V10.*`. No production
board or Phase 18 USB3 route was changed.

## Alternate native J3 orientation trial — 2026-09-06

The native placement discriminator was extended to test U7 180 degrees with
J3 at 0 and 270 degrees. The 0-degree launch presents the four SATA pads in
two ordered rows at the near connector edge and is a credible next topology;
the 270-degree placement introduces additional inherited mechanical/launch
interactions. A first 0-degree SATA route implementation was generated from
native pad coordinates, but native DRC rejected it with 137 violations,
including same-row TX/RX dogbone crossings and paired target vias within the
0.25 mm hole-clearance requirement. It is retained as
`ROUTE IMPLEMENTATION FAILURE`, not as a macro-placement rejection.

The next 0-degree route cycle must offset the final signal-pad dogbones in Y
and keep each pair's target vias outside the connector field. No production
board or validated USB3/PCIe copper was changed.

## V19 monotonic SATA route milestone — 2026-09-06

The corrected 0-degree J3 route was regenerated after removing redundant
socket transition vias and restoring monotonic B.Cu ordering. Native DRC
reports zero `shorting_items`, zero `tracks_crossing`, zero clearance or
hole-clearance findings, and zero `via_dangling` findings for the candidate.
The native SATA audit passes all eight bridge/coupler/socket endpoint pairs.

V19 remains a route-topology milestone, not Phase 19 closure: the full
candidate still reports the selected J3 footprint's 63 solder-mask-bridge
records and 80 unrelated/unrouted board connections. Measured route lengths
are retained for skew work: TX bridge P/N = 33.000/40.500 mm, RX bridge P/N =
21.736/30.000 mm, and socket-side P/N lengths are 36.206/36.679 mm (TX) and
34.945/40.858 mm (RX). The endpoint proof and high-speed DRC screen are
stronger than the earlier 90-degree candidates, but pair-length matching and
coexistence with the complete storage support network remain open.

## V21 authoritative J3 refresh — 2026-09-06

The embedded J3 instance was replaced from the corrected
`JAE_SM3ZS067U410ABR1000_BKEY` library footprint. The refresh path preserves
reference, value, native position/orientation, and each saved pad's net by
pad number, binding nets only after the replacement footprint is attached to
the board. The native SATA and USB3 audits both pass.

V21 native DRC reports zero errors and only 11 unrelated text/silkscreen
warnings; the earlier J3 solder-mask-bridge findings are gone. The
severity-error command still reports 80 unconnected board items, all outside
the SATA/USB3 endpoint set (regulator/support and other incomplete-board
connections), so V21 is not claimed as a full-board Phase 19 closure. The
corrected footprint and refresh script are now the authoritative route-fixture
path for the next coordinated storage integration.

## V26 selected storage data-route milestone — 2026-09-06

The J3 0-degree route was regenerated with separated final dogbones and a
short B.Cu RX-P meander. After refreshing J3 from the corrected authoritative
footprint, native DRC reports 11 unrelated text/silkscreen warnings and zero
shorting, crossing, clearance, hole-clearance, dangling-via, or footprint
errors. The native SATA audit passes all eight endpoints and the unchanged
USB3 audit passes all four CM5-to-U7 endpoints.

Measured end-to-end SATA pair skew is 0.97 mm TX and 0.365 mm RX, within the
recorded 1.2 mm bound. Ordinary through-vias are used; no plane-layer signals
or via-in-pad construction was introduced. V26 is therefore the selected
storage data-route milestone. Full Phase 19/24 closure remains open because
the board still has 80 unrelated support/power/ground connectivity opens and
the complete U7 clock/control/rail integration must be revalidated with this
data route.

Receipt: `PHASE24_STORAGE_DATA_ROUTE_V26_RECEIPT.md`.
# V26 support-oracle transplant rejection (2026-09-06)

`phase24_transplant_support_v26.py` was added as a disposable native-support
experiment. It copied the previously observed U7 clock/rail/control support
geometry by the actual U7 displacement and tested rigid rotations about the
native U7 origin. The unrotated transform is rejected: C16 lands in the J7
CM5 pad field and the transformed clock traces intersect the existing CM5
USB3 route. The rotated variants are also rejected as route-implementation
failures: native DRC reports true `BRIDGE_XI`/`BRIDGE_XO`/`BRIDGE_VSSOSC`
shorts and clearance violations in the transformed support geometry.

This evidence does not invalidate the V26 SATA/USB3 data corridors: the
native SATA audit still passes all eight SATA endpoints on the rejected
support candidate. The support donor itself was not a clean integrated
oracle, so it is not promoted. The V26 data-route milestone remains the
working basis while support is rebuilt from actual pad/net authority in a
dedicated local placement, with no PCIe or validated USB3/SATA copper change.

Classification: `ROUTE_IMPLEMENTATION_FAILURE` / support-placement
incompatibility, not `MACRO-PLACEMENT FAILURE` and not an architecture
blocker.

## V2 clock-oracle placement trial (rejected)

The standalone `PHASE24_COMPLETE_CLOCK_FIXTURE_V2.kicad_pcb` is retained as
the authoritative clock-topology source because its native clock-specific
receipt reports no clock shorting or crossing classes. A bounded transform
onto the V26 U7 frame was then tested with the required 180-degree footprint
orientation and a 10 mm east / 20 mm south local translation. The integrated
candidate was rejected by native DRC: 58 violations, including clock/SATA
shorts and track crossings, plus 77 unconnected records. This is a
`ROUTE_IMPLEMENTATION_FAILURE` caused by collision with inherited V26 copper,
not a failure of the standalone clock topology. The candidate was not
promoted and V26 SATA/USB3 copper remains unchanged.
## V2 clock-oracle south-40 placement probe (rejected)

A second placement of the native-clean V2 clock fixture moved the complete
passive island farther south, outside the immediate SATA corridor. Native
DRC reduced this integration result to 19 violations and one real
`BRIDGE_XI` to `BRIDGE_VSSOSC` short, with 77 unresolved opens. It is rejected
rather than waived. This localizes the remaining support work to correcting
the transformed clock pad escape and completing the support rails; V26
USB3/SATA data copper remains unchanged.

The follow-up corrected the footprint pad-layer sets from the fixture instead
of inheriting the acreage placeholders. The south-40 candidate then passed a
new actual KiCad connectivity audit for all XI/XO/VSSOSC passive endpoints and
native DRC reported no shorting, crossing, clearance, or dangling-via classes.
It still reports 73 board opens and three dangling F.Cu support tails, so it
is a clock-support milestone rather than an accepted Phase 24 ancestor. The
remaining work is to connect the three U7 clock launches and integrate the
rail/reset/configuration support without reintroducing data-route conflicts.

## Parallel U7 clock-launch probe (rejected)

Three ordinary through-vias and parallel B.Cu legs were added from U7.52/.53/.54
to the south-40 fixture launch points. Native DRC rejected this direct launch
class with 100 violations, including real clock shorts, crossings, and
clearance failures. It is preserved as `ROUTE_IMPLEMENTATION_FAILURE`; the
passive clock island and V26 USB3/SATA data corridors were not changed.

## Macro-floorplan comparison rule reaffirmed — 2026-09-06

The whole-board discriminator remains the controlling placement evidence. It
compares native transformed-pad topology, source-to-island distance, same-net
ratsnest, endpoint order, coarse body screening, corridor competition, and
mechanical/access constraints. It does not compare the mature historical
board's DRC/open count against first-pass routing on a rearranged candidate.

The selected `SWAP_ETH_STORAGE` / `STORAGE_LOCAL_J3_EDGE` topology therefore
remains a routing-development basis, not a route-quality claim. The latest
TI-authoritative U7 disposable escape (`PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI_ORDERED.kicad_pcb`)
was rejected for real crossings, shorts, and clearances caused by its fixed
escape coordinates. This is `ROUTE IMPLEMENTATION FAILURE`; it does not
invalidate the macro discriminator or justify reverting to the historical
floorplan. The next route cycle must use native TI pad coordinates with a
fresh obstacle-aware escape and retain the same separation between floorplan
question A and route-implementation question B.

## TI-U7 native-coordinate USB3 route-class trials — 2026-09-06

The selected macro was converted in a disposable copy to the authoritative
TI TUSB9261 PVP0064A footprint, preserving the 41 native U7 pad-net mappings.
The first ordered escape used fixed coordinates and was rejected by native DRC
for real SATA/USB3 crossings, shorts, and clearances. A second trial,
`phase24_ti_usb3_ordered_bcu.py`, derived all endpoints from saved native pad
coordinates and used ordinary vias outside the TI field. Its B.Cu corridor
was rejected with 403 native findings, including 18 crossings and 20 shorts,
because it competed with the existing PCIe copper. A mixed-layer revision was
also rejected with 407 findings, including 21 crossings and 21 shorts. These
are `ROUTE IMPLEMENTATION FAILURE` results; neither trial is floorplan
evidence and no production copper was promoted.

The next route-development class is obstacle-aware pair routing that treats
existing PCIe/power/footprint copper as live obstacles and derives actual TI
pad exits, rather than adding another fixed-coordinate corridor.

The obstacle model was then refined to use the actual 0.15 mm trace/clearance
envelope at the 0.4 mm TI USB3 pitch and to spread source transitions outside
the J7 row. The next run still found no F.Cu path from the first source
transition to U7 while retaining all existing board copper as obstacles. This
remains a router-model/integration result, not a placement verdict; the next
probe must distinguish stale/inherited copper from mandatory obstacles and
model explicit local launch corridors without deleting frozen PCIe evidence.

## Obstacle-aware TI-U7 USB3 router probe — 2026-09-06

`phase24_ti_usb3_obstacle_pair_astar.py` was added as a new route class. It
derives J7/U7 endpoints from the saved TI-authoritative PCB, removes only
USB3 copper, models native pads and retained PCIe/power copper as obstacles,
and reserves emitted pair paths. The first run could not find an F.Cu path
from the first source transition to U7 under its conservative raster model;
no board was promoted and no gate was relaxed. This is retained as
`ROUTE_IMPLEMENTATION_FAILURE / ROUTER_MODEL_LIMIT`, not
`MACRO-PLACEMENT FAILURE`, because local source/via escape exemptions and
package-approach geometry still need to be modeled explicitly.

The planner was further corrected to use anisotropic native pad envelopes and
to exempt only the four intentional U7 USB3 target lands from its obstacle
mask. The isolated selected-macro fixture still finds no first-lane path with
inherited storage-support copper retained, so this remains route-model
evidence rather than a macro-placement rejection.

## Clean TI-U7 source-to-package discriminator — 2026-09-06

To separate inherited-board obstruction from package escape, a disposable
two-footprint fixture was generated by `phase24_make_ti_usb3_minimal_fixture.py`.
With only native J7 and TI PVP0064A U7 retained, the obstacle-aware planner
authored all four native source-to-U7 paths. Native DRC still rejects this
first package-field implementation with 113 findings, including four
crossings and 30 shorts. This proves reachability of the selected macro
source-to-U7 relationship while identifying the remaining defect as
`ROUTE_IMPLEMENTATION_FAILURE / TI_PADFIELD_ESCAPE`, not
`MACRO-PLACEMENT FAILURE`. No integrated copper was changed or promoted.

## Monotonic TI-U7 direct-escape control — 2026-09-06

The grid A* path was replaced with a minimal monotonic control using one
ordinary source-side through-via per lane and a direct F.Cu segment to each
native TI USB3 land. Native DRC reduced the clean-fixture result to 37
findings, including five crossings and 11 shorts, but it remains rejected.
This separates the previous A* zigzag class as a router implementation
defect; the remaining failures are localized to source-via/lane assignment
and TI pad-field approach geometry. No integrated or PCIe copper was modified.

## TI-U7 package escape lane-assignment sweep — 2026-09-06

The package-aware monotonic control used separated source transitions and
per-lane columns before a horizontal dogbone into the TI lands. Native DRC
reduced the minimal-fixture result to 18 findings, but still reported 12
crossings and one short from shared-column interactions. A direct-sloped
variant was worse at 27 findings and was rejected. These are disposable
`ROUTE_IMPLEMENTATION_FAILURE` results; no integrated or PCIe copper was
changed. The next credible class is pair-preserving diagonal/offset escape
geometry without shared vertical lane crossings.

## TI-U7 mixed-layer pair assignment — 2026-09-06

The mixed-layer control kept RX on F.Cu and moved TX to B.Cu between ordinary
through-vias, with reversed/laterally separated source-via ordering to retain
pair monotonicity. The best saved native DRC result is 12 findings: zero
shorts, one crossing, one hole-clearance finding, and the expected incomplete
fixture opens. It is not promoted; the remaining crossing is in the TX source
escape and the hole finding is a transition-field geometry defect. This is
the strongest current package-route control and remains
`ROUTE_IMPLEMENTATION_FAILURE`, not a floorplan failure.

## TI-U7 diagonal escape control — 2026-09-06

The next disposable control kept each source transition on its native J7 row,
spread the transition vias laterally, and used a direct diagonal F.Cu segment
to the native TI lands. Native DRC reported 36 findings, including six
crossings and nine shorts, a small improvement over the column control but
still a rejection. The candidate remains `ROUTE_IMPLEMENTATION_FAILURE`;
the selected macro and PCIe ancestor are unchanged.

## TI-U7 mixed-layer transition refinement — 2026-09-06

The mixed-layer control was refined with separated TX source transitions and
reversed target-via ordering. The best native DRC result now reports 10
findings with zero `shorting_items` and zero `tracks_crossing`; remaining
errors are three local clearances and one hole-clearance interaction, plus
fixture-only dangling warnings. A farther-separated target-via variant
regressed to 15 findings and was rejected. The 10-finding result remains
disposable `ROUTE_IMPLEMENTATION_FAILURE`; no integrated or PCIe copper was
changed or promoted.

## TI-U7 RX approach-gate sweep — 2026-09-06

RX final-approach gates were offset by ±0.25 mm to reduce convergence near
the TI land field. Native DRC remained at the 10-finding baseline with zero
shorts/crossings; a ±0.5 mm variant regressed to 18 findings with shorts and
additional clearances. The best control was restored. This coordinate class
is exhausted without changing the selected macro or layer contract; the next
attempt must use a different legal transition topology.

## TI-U7 target-transition height sweep — 2026-09-06

A small TX target-transition height variation was tested against the best
mixed-layer control. It regressed to 23 native DRC findings, including one
crossing, five shorts, and four hole-clearance findings, so it was rejected
and the 10-finding control was restored. No validation severity, layer
contract, macro placement, or frozen PCIe copper changed.

## TI-U7 split-RX transition experiment — 2026-09-06

An alternate-layer RX_P experiment was tested while retaining the mixed-layer
TX assignment. Native DRC regressed to 14 findings with three crossings and
two clearances; no shorts were introduced, but the candidate was rejected.
The prior 10-finding mixed-layer control was restored. This remains route
implementation evidence only; no macro or frozen PCIe geometry changed.

## Whole-board functional-island macro-floorplan discriminator — 2026-09-06

Local Phase 24 net-by-net routing was paused as directed. The live integrated
storage candidate was snapshotted before review:
`PHASE24_MACRO_REVIEW_SNAPSHOT_20260906.kicad_pcb`, SHA-256
`48840a9e353249f43853547a891c5588cdc5254fd771ac7ddfdb21efaddd058e`.
The source basis was the native-loaded
`PHASE24_U7_3V3_CURRENT_LOCAL.kicad_pcb` with the same SHA-256, so the review
did not accidentally use a historical disposable fixture.

The review used transformed native pad positions from J7, not schematic
drawing positions, guessed rotations, or the previously generated pinout
image. The launch centroids are Ethernet `(34.5,99.9)`, PCIe/V100
`(69.6,101.5)`, storage USB3 `(70.0,105.3)`, and SERVICE USB2
`(67.0,99.3)`. Current functional-island anchors are Ethernet `(77.8,59.6)`,
PCIe/V100 `(150.0,90.0)`, storage `(130.7,131.0)`, SERVICE `(46.9,100.0)`,
power entry `(72.4,76.9)`, and regulators `(173.3,125.0)`.

Six disposable native placement candidates were generated without promoting
or ranking their retained copper: `CURRENT`, `ETH_LOCAL_STORAGE_MID`,
`SWAP_ETH_STORAGE`, `ETH_SOUTH_STORAGE_NORTH`, `STORAGE_LOCAL`, and
`POWER_EAST_REGULATORS_WEST`. Topology-only metrics were source-to-island
Euclidean/Manhattan distance, nearest source pad, same-net ratsnest, native
transformed-body overlap, endpoint neighborhood, corridor occupancy, and
mechanical/access screening. Mature historical DRC and immature candidate
DRC were explicitly excluded: a route implementation failure is not a
macro-placement failure.

`SWAP_ETH_STORAGE` remains the best candidate tested: Ethernet source-to-
island distance changes from 59.2 mm to 22.5 mm and same-net ratsnest from
443.9 mm to 127.7 mm; storage changes from 65.9 mm to 49.5 mm and 231.2 mm
to 116.5 mm. It retains the PCIe/V100 and SERVICE anchors and has zero coarse
major-body overlaps. The compact `ETH_LOCAL_STORAGE_MID` candidate is nearer
for Ethernet but has four coarse body overlaps, including SERVICE/power, and
is rejected as a worse shared-floorplan topology. `ETH_SOUTH_STORAGE_NORTH`
and `POWER_EAST_REGULATORS_WEST` do not improve both high-speed neighborhoods.

Power and regulator groups were included as corridor occupants and coherent
mechanical neighborhoods; their electrical topology was not changed. The
review did not treat historical edge assignments, old coordinates, or the
cooler hypothesis as hard constraints. Actual connector/mounting/access,
power return capacity, and native courtyard/3-D checks remain required after
any promotion.

Consultant dispatch was attempted for the independent review but the
orchestration service returned `collab spawn failed: agent thread limit
reached`; it was not retried unchanged. The local review is complete from
native PCB objects, and consultant unavailability is not treated as an
engineering blocker.

This is a floorplan discriminator, not a detailed routing result. The selected
macro receives a fair obstacle-aware native routing-development cycle before
any comparison against the mature historical board. No detailed Phase 24
open-by-open repair was resumed during this discriminator.

Receipt: `phase24_whole_board_macro_floorplan_discriminator.py`,
`PHASE24_WHOLE_BOARD_MACRO_DISCRIMINATOR_20260906.md`, and the six generated
`PHASE24_MACRO_DISCRIM_*.kicad_pcb` disposable candidates.

`WHOLE_BOARD_FUNCTIONAL_ISLAND_REVIEW = COMPLETE`
`SELECTED_MACRO_TOPOLOGY = SWAP_ETH_STORAGE`
`CURRENT_INTEGRATED_BASIS_SNAPSHOTTED = TRUE`
`ROUTE_COMPARISON_BIAS_CONTROL = PASS`
`PHASE24 = OPEN`

## Path-B RTL_5V pad-17 escape V1 — 2026-09-07

V1 attempted a coherent F.Cu side escape from U1 RTL_5V pad 17 to the
existing pad-33/C5 bus on the V2 rail baseline. It connected one required
rail endpoint and reduced the open count from 30 to 29, but native DRC
reported 8 violations from SPISO, SPISI, SPICLK, and the inherited PEDET
field. It is rejected as a route implementation; no power topology or
production CAD changed.

`PATHB_RTL_5V_PAD17_V1 = REJECTED`
`PHASE24 = OPEN`

## Path-B RTL_3V3 QFN zone V1 — 2026-09-07

V1 tested a local F.Cu RTL_3V3 power zone around U1 using the V2 RTL_1V1
collector. Native DRC remained 4 violations / 30 unconnected items and the
native pad connectivity census showed no additional required RTL_3V3 pads
were joined. The zone is rejected as ineffective; no power rule or plane
policy was changed and production CAD remains untouched.

`PATHB_RTL_3V3_ZONE_V1 = REJECTED`
`PHASE24 = OPEN`

## Path-B RTL_1V1 QFN collectors V2/V3 — 2026-09-07

V2 removed the duplicate via, omitted the SPI-conflicting pad-25 branch, and
jogged the bottom collector around CLKREQ. Native DRC reports 4 violations /
30 unconnected items; six RTL_1V1 pads are physically collected without
via-in-pad. V3 moved the pad-40 via left, but native DRC regressed to 6 / 30
with an RTL_1V1/USB_TXP0 short and a CLKREQ crossing. V2 is retained as the
best collector baseline; neither is integrated.

`PATHB_RTL_1V1_COLLECTOR_V2 = REJECTED_BEST_BASELINE`
`PATHB_RTL_1V1_COLLECTOR_V3 = REJECTED`
`PHASE24 = OPEN`

## Path-B RTL_1V1 QFN collector V1 — 2026-09-07

V1 added ordinary-via perimeter collection for the actual U1 RTL_1V1 pads,
without via-in-pad. Native DRC reports 9 violations / 29 unconnected items,
reducing the V12 baseline's 36 opens by seven. It is rejected as authored:
the first perimeter collides with SPICS/SPISO near the QFN edge, crosses the
CLKREQ field, and contains a duplicate existing transition. The reduction
confirms coherent rail collection is the correct next class; no copper is
promoted and production CAD remains unchanged.

`PATHB_RTL_1V1_COLLECTOR_V1 = REJECTED`
`PATHB_SUPPORT_OPEN = TRUE`
`PHASE24 = OPEN`

## Path-B native connectivity audit — 2026-09-07

`phase24_rtl9210b_control_connectivity_audit.py` now derives connectivity
from KiCad's saved pads, tracks, vias, and native connectivity engine. On
`PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL_V12.kicad_pcb`, PEDET, CLKREQ_N,
PERST_N, RESET_N, and SPICS/SPISO/SPISI/SPICLK U1↔U2 endpoints all pass.
The negative control removes all saved PEDET copper and fails as required.
The four SPI test pads are intentionally not asserted by this audit and
remain an open test-access task. No synthetic graph edges are used.

`PATHB_CONTROL_CONNECTIVITY_AUDIT = PASS`
`PATHB_TEST_ACCESS = OPEN`
`PHASE24 = OPEN`

## Path-B test-access V2 — 2026-09-07

V2 was generated from corrected V12 control geometry with four explicit
B.Cu test-access lanes and F.Cu pad dogbones. Native DRC reported 33
violations / 35 unconnected items, including source-pad shorts, crossings
through RESET/PERST/CLKREQ corridors, solder-mask bridges, and invalid via
clearances. It is rejected; test access requires a coordinated support-island
regeneration rather than appended lanes. No production CAD changed.

`PATHB_TEST_ACCESS_V2 = REJECTED`
`PHASE24 = OPEN`

## Path-B test-access V1 — 2026-09-07

The first four-SPI-test-pad route was generated against the older V6 control
baseline rather than the corrected PEDET baseline. Native DRC reported 12
violations / 35 unconnected items: it reintroduced the known RTL_5V/PEDET
short, crossed SPI/control corridors, and did not physically connect the
F.Cu test pads from B.Cu paths. V1 is rejected as a route implementation and
is preserved as a negative control; no test-access or production copper was
promoted.

`PATHB_TEST_ACCESS_V1 = REJECTED`
`PHASE24 = OPEN`

## Path-B PEDET reroute V11–V15 — 2026-09-07

V11 moved the PEDET upper return below the RTL_5V via but violated board-edge
clearance at 5 native findings / 35 opens. V12 moved the return to y=42.5;
native DRC reported 3 findings / 36 opens, with one PEDET/RTL_3V3 crossing and
two inherited RTL_3V3 dangling warnings. V13 moved the upper run to B.Cu and
reported 4 / 35 from GND-via clearance and a redundant transition. V14
repositioned that transition but reported 4 / 35 from RTL_5V/PEDET and
RTL_3V3/PEDET crossings. V15 attempted a two-layer detour and regressed to
15 / 35 with multiple rail-field shorts/crossings. All are rejected route
implementations. V6 remains the best Path-B control baseline at 3 / 36; no
production CAD or architecture decision changed.

`PATHB_PEDET_ROUTE_CLASS = REJECTED`
`PATHB_ARCHITECTURE = CONTINUE_BOTH`
`PHASE24 = OPEN`

## Path-A isolated M.2 lane-0 launch V14 — 2026-09-07

V14 repeated the V13 geometry at 0.15 mm, below the selected 0.20-mm
differential route width. Native DRC reported 105 violations / 34
unconnected items, including 28 track-width violations. It is rejected; the
approved width contract is not relaxed. V12 remains the valid-width baseline
with zero shorts and zero crossings.

`PATHA_M2_LANE0_V14 = REJECTED`
`FAILURE_CLASS = MANUFACTURING_RULE / ROUTE_IMPLEMENTATION`
`PHASE24 = OPEN`

## Path-A isolated M.2 lane-0 launch V13 — 2026-09-07

V13 retained V12 geometry with 0.10-mm disposable escape tracks as a
clearance discriminator. Native DRC reported 102 violations / 34
unconnected items: zero shorts/crossings, 68 clearance findings, and 28
track-width violations. It is rejected under the unchanged manufacturing
contract; width rules are not relaxed. V12 remains the best valid-width
topological baseline and no production CAD changed.

`PATHA_M2_LANE0_V13 = REJECTED`
`FAILURE_CLASS = MANUFACTURING_RULE / ROUTE_IMPLEMENTATION`
`PHASE24 = OPEN`

## Path-A isolated M.2 lane-0 launches V11/V12 — 2026-09-07

V11 staggered the four M.2 contact-row departure heights and reduced native
DRC to 79 violations / 34 unconnected items, but introduced one crossing
between RXP and TXN final dogbones. V12 swapped those two departure heights:
native DRC reports 81 violations / 34 unconnected items, with zero shorts and
zero track crossings. V12 is the strongest current topological candidate;
remaining findings are clearance, dangling disposable-fixture geometry, and
unconnected M.2 ground/mechanical contacts. Neither is integrated.

`PATHA_M2_LANE0_V11 = REJECTED`
`PATHA_M2_LANE0_V12 = REJECTED_BEST_TOPOLOGY`
`PHASE24 = OPEN`

## Path-A isolated M.2 lane-0 launches V9/V10 — 2026-09-07

V9 moved RXN farther left before its vertical source jog and removed the
source crossing, but native DRC reported 81 violations / 34 unconnected items
with one RXN/RXP source short at the RXP transition via. V10 moved that RXP
transition below RXN's escape. Native DRC remained at 81 / 34 with zero
shorts and zero track crossings. The remaining findings are clearance and
package/contact-field findings, notably the 0.5-mm-pitch M.2 final fanout.
V10 is the best topological baseline but is not integrated or closed.

`PATHA_M2_LANE0_V9 = REJECTED`
`PATHA_M2_LANE0_V10 = REJECTED_BEST_TOPOLOGY_BASELINE`
`PHASE24 = OPEN`

## Path-A isolated M.2 lane-0 launches V7/V8 — 2026-09-07

V7 moved RXP to a lower B.Cu corridor. Native DRC reported 84 violations /
34 unconnected items, with one M1 mounting-hole short and one source crossing.
V8 routed that B.Cu corridor below/outboard of M1; native DRC reported 82
violations / 34 unconnected items, with no shorts but one source crossing.
Neither is a pass. V5 remains the best isolated baseline at 80 / 33 with no
shorts; V7/V8 are preserved as alternative layer/clearance evidence.

`PATHA_M2_LANE0_V7 = REJECTED`
`PATHA_M2_LANE0_V8 = REJECTED`
`PHASE24 = OPEN`

## Path-A isolated M.2 lane-0 launches V5/V6 — 2026-09-07

V5 (`PHASE24_PATHA_M2_LANE0_LAUNCH_ISOLATED_V5.kicad_pcb`) used orthogonal
source escapes and vertical M.2 contact-row dogbones. Native DRC reported 80
violations / 33 unconnected items, with no shorting items; one RX source
track-crossing and package/contact-field clearance findings remain. V5 is
rejected but is the best current isolated launch baseline.

V6 (`PHASE24_PATHA_M2_LANE0_LAUNCH_ISOLATED_V6.kicad_pcb`) changed the RX
source corridors to remove that crossing. Native DRC reported 83 violations /
33 unconnected items and introduced an actual M1 mounting-hole interaction and
another crossing. V6 is rejected. Both are route implementation evidence only;
production CAD and Path-B authority remain unchanged.

`PATHA_M2_LANE0_V5 = REJECTED_BEST_BASELINE`
`PATHA_M2_LANE0_V6 = REJECTED`
`PHASE24 = OPEN`

## Path-A isolated M.2 lane-0 launch V3 — 2026-09-07

`PHASE24_PATHA_M2_LANE0_LAUNCH_ISOLATED_V3.kicad_pcb` tested split-layer
source routing with a connector-ordered target-via column. Native DRC reports
103 violations and 32 unconnected items. It is rejected: the RX target-via
field shorts RXN/RXP, TXN also contacts inherited TUSB_SATA_RXP copper, and
one track-crossing remains. The result is a route implementation failure, not
evidence against the shared M.2 architecture. No V3 copper is integrated.

`PATHA_M2_LANE0_V3 = REJECTED`
`FAILURE_CLASS = ROUTE_IMPLEMENTATION_FAILURE`
`PHASE24 = OPEN`

## Path-A isolated M.2 lane-0 launch V2 — 2026-09-07

`PHASE24_PATHA_M2_LANE0_LAUNCH_ISOLATED_V2.kicad_pcb` is preserved as a
disposable route experiment. It moved the RX lower corridors around the J3
M1 mounting-hole region, but native DRC still reports 83 violations and 32
unconnected items. The remaining failures are route-authoring defects: the
TXP final launch contacts J3 pad 47 (TXN), the TXN final launch contacts J3
ground pad 45, the RXP final launch contacts J3 ground pad 39, and the RXN/RXP
lower corridors cross near their target-via field. Inherited U13 QFN pad-field
clearance findings remain present as package/rule findings. V2 is rejected and
is not integrated; no Path-B or production CAD changed. The next experiment
must change the connector-side target-via/final-dogbone ordering rather than
repeat the V2 corridor.

`PATHA_M2_LANE0_V2 = REJECTED`
`FAILURE_CLASS = ROUTE_IMPLEMENTATION_FAILURE`
`PHASE24 = OPEN`

## TI-U7 separated-target-via approach refinement — 2026-09-06

The best disposable escape was refined by aligning the TX final F.Cu
dogbones to the actual native U7 pad rows. Native DRC reports 8 findings,
all expected incomplete-fixture warnings or unconnected items; there are zero
shorts, zero track crossings, and zero clearance violations. The geometry was
then authored into a selected-macro disposable integration basis with all
four USB3 nets and native net identity preserved. The integrated result is
not promoted until its full-board DRC/connectivity/reference checks pass.

Receipts: `phase24_ti_usb3_rx_split_v2_fixture.py`,
`phase24_promote_ti_usb3_rx_split_v2.py`,
`PHASE24_RX_SPLIT_V2_CHECK.rpt`, and
`PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI_USB3_RX_SPLIT_V2.kicad_pcb`.

`TI_U7_DISPOSABLE_ESCAPE = PASS`
`TI_U7_INTEGRATED_ESCAPE = OPEN`
`PHASE24 = OPEN`

## Macro-floorplan comparison-bias reconciliation — 2026-09-06

The whole-board discriminator was rechecked against the comparison rule that
historical routing maturity and first-pass candidate DRC must not rank a
floorplan. The native transformed-pad metrics and coarse major-body screen
select `SWAP_ETH_STORAGE`; the earlier `ETH_WEST_CLEAR_STORAGE_MID` preference
is retained only as a documented fallback. PCIe, SERVICE, power-entry, and
regulator anchors remain unchanged. The selected macro is a topology decision
only; USB3/SATA/clock routing remains route-development work and is not yet a
Phase 24 closure.

Receipt: `PHASE24_WHOLE_BOARD_MACRO_DISCRIMINATOR_20260906.md`,
`PHASE24_WHOLE_BOARD_FLOORPLAN_REVIEW.md`, and the six native disposable
candidate PCBs. Consultant dispatch remains unavailable because the known
orchestration thread limit was already reached; local native review supplies
the independent comparison and does not change the acceptance gate.

`MACRO_COMPARISON_BIAS_CONTROL = PASS`
`SELECTED_MACRO_TOPOLOGY = SWAP_ETH_STORAGE`
`ROUTE_IMPLEMENTATION_FAILURE != MACRO_PLACEMENT_FAILURE`
`PHASE24 = OPEN`

## TI-U7 separated-target-via route-class probe — 2026-09-06

A fresh disposable TI-U7 USB3 fixture tested a monotonic B.Cu source-to-target
escape with separated target transitions and short F.Cu pad-row dogbones.
The best geometry produced 10 native DRC violations, zero shorts, and zero
track crossings; the remaining two errors are local F.Cu approach clearances
into adjacent U7 pads, with the expected incomplete-fixture unconnected
items. A pad-row-aligned staggered-via variant regressed to 15 violations,
including two shorts and multiple hole-clearance errors, so it was rejected
and the best control was restored. This is route implementation evidence,
not a macro-placement failure and not an integrated-board pass.

Receipt: `phase24_ti_usb3_rx_split_v2_fixture.py`,
`PHASE24_USB3_LOCAL_TI_RX_SPLIT_V2.kicad_pcb`, and
`PHASE24_RX_SPLIT_V2_CHECK.rpt`.

`TI_U7_V2_SEPARATED_TARGET_PROBE = REJECTED_VARIANT_BEST_CONTROL_RESTORED`
`ZERO_SHORTS = TRUE`
`ZERO_TRACK_CROSSINGS = TRUE`
`PHASE24 = OPEN`

## U7 project-footprint replacement discriminator — 2026-09-06

`PHASE24_PATHA_U7_FOOTPRINT_REPLACEMENT_20260906.md` records a disposable
native replacement of embedded U7 with the project-local TUSB9261 footprint.
Native pad nets and placement were preserved. The eight-endpoint SATA audit
remained PASS and native DRC remained at 12 findings, so the suspected
embedded/project footprint mismatch is not the route root cause. The next
Path-A repair must address local route geometry and support connectivity.

The TI land-pattern receipt
`authority-inventory/primary-docs/tusb9261/TUSB9261_PVP_LAND_PATTERN_RECEIPT.md`
now confirms the exact 0.4-mm/1.2 x 0.2-mm PVP0064A geometry from the current
TI datasheet. A disposable 0.15-mm API clearance probe did not alter KiCad's
active 0.20-mm rule basis and is rejected as a rule-authoring method; no
production clearance rule has been weakened.

## U5 native recheck receipt — 2026-09-06

The corrected U5 audit was rerun against the saved U5 fixture and the
promoted `PHASE24_PGND_CLUSTER_CURRENT.kicad_pcb` basis using KiCad 10.0.5
`BuildConnectivity`. Both focused audits pass. The disposable negative
control removes an actual U5.9-connected trace and fails as required. The
audit derives connectivity from serialized pads, tracks, vias, and filled
zones; expected membership remains assertion-only. This is focused evidence,
not full-board closure: native DRC/unconnected findings remain open.

Receipt: `PHASE24_U5_NATIVE_RECHECK_20260906.md`.

`U5_NATIVE_AUDIT = PASS`
`U5_NEGATIVE_CONTROL = PASS`
`PHASE24 = OPEN`

## Phase 24 authority recheck — 2026-09-06

Reran the authoritative support-part pad-net audit, U7 supply-hierarchy
audit, and full schematic/PCB reference-set audit with KiCad 10.0.5. All
passed: eight support references were exact, U7 was present on both
canonical bridge rails, and the reference set was `78` schematic / `101` PCB
with the expected `23` PCB-only mechanical/test extras. These checks do not
close copper routing, native DRC, or the scoped dual-mode storage upgrade.

Receipt: `PHASE24_AUTHORITY_RECHECK_20260906.md`.

`PHASE24_AUTHORITY_RECHECK = PASS`
`PHASE24 = OPEN`

## USB3 selected-source A* trial — 2026-09-06

The disposable source-to-U7 A* continuation began from actual J7/U7 native
pad coordinates and explicit source transitions. Native KiCad DRC reported
180 violations and 450 unconnected items, including one track crossing, nine
dangling tracks, and five dangling vias. The candidate is rejected as
`ROUTE_IMPLEMENTATION_FAILURE`; it was not promoted and does not invalidate
the CM5IO source-anchor or selected macro evidence.

Receipt: `PHASE24_USB3_SELECTED_SOURCE_ESCAPE_ASTAR_RECEIPT_20260906.md` and
`PHASE24_USB3_SELECTED_SOURCE_ESCAPE_ASTAR-drc.json`.

`USB3_ASTAR_CONTINUATION = REJECTED`
`PHASE24 = OPEN`

## CM5IO manual south-span trial — 2026-09-06

The next distinct route class retained the official CM5IO source prefix and
used explicit standard-geometry through-vias with hand-authored B.Cu
south-span polylines to U7. Native KiCad DRC reported 207 violations, 465
unconnected items, 16 track crossings, and 4 shorting items. It is rejected
as `ROUTE_IMPLEMENTATION_FAILURE`; no production route or macro-floorplan
change was promoted.

Receipt: `PHASE24_USB3_CM5IO_MANUAL_SOUTH_SPAN_RECEIPT_20260906.md` and
`PHASE24_USB3_CM5IO_MANUAL_SOUTH_SPAN-drc.json`.

`USB3_MANUAL_SOUTH_SPAN = REJECTED`
`PHASE24 = OPEN`

## TI U7 RX target-via separation experiment — 2026-09-06

The best clean west-target control was challenged by moving only RX_P's
target via to `(82.0,106.5)` while retaining all other source/target
geometry. Native DRC regressed from 15 findings (one short, zero crossings)
to 34 findings (10 shorts, zero crossings, three clearances, 12
hole-clearance findings, and 80 expected unconnected items). The variant was
rejected and the 15-finding zero-crossing control restored.

The failure is localized to through-via interaction with the opposite RX
member, not a missing net or a macro-placement proof. The next credible class
is a cross-layer pair transition that avoids placing a through-via inside the
other member's B.Cu corridor.

`TI_U7_RX_TARGET_SEPARATION = REJECTED`
`BEST_CLEAN_FIXTURE_RESTORED = TRUE`
`PHASE24 = OPEN`

## Clean TI-U7 west-target package fixture — 2026-09-06

The source-local two-footprint fixture was regenerated from the corrected TI
PVP0064A package and given a west-side target transition topology. Source and
target transition fields were separated while final F.Cu dogbones remained
on the actual U7 USB3 land rows. Native DRC reached 15 findings: zero track
crossings, one short, three clearances, three hole-clearance findings, and
80 expected incomplete-fixture unconnected items. A lateral target-via
variant regressed to 21 findings with two shorts and seven hole-clearance
findings and was rejected; the 15-finding control was restored.

This is the strongest current package-only control, but it is not yet a
PASS: the remaining short/clearances must be removed before promotion into
the integrated acreage board. The result is `ROUTE_IMPLEMENTATION_FAILURE`
evidence at the package transition, not a macro-floorplan rejection.

Receipt: `phase24_ti_usb3_west_target_fixture.py` and
`PHASE24_USB3_LOCAL_TI_WEST_TARGET-drc.rpt`.

`TI_U7_CLEAN_FIXTURE = NEAR_PASS`
`TI_U7_CLEAN_FIXTURE_CROSSINGS = 0`
`PHASE24 = OPEN`

## USB3-source-local coherent storage discriminator — 2026-09-06

An additional coherent candidate moved U7/J3 and all clock, coupling, and
local support references to the native USB3 launch region. The placement
probe was corrected to remove every saved track/via incident on the old pads
of moved footprints, preventing stale unrelated nets from contaminating the
experiment. With authoritative TI U7 replacement, the native obstacle-aware
planner reached all four endpoints in 47/37/12/4 segments for RX_N/RX_P/
TX_N/TX_P respectively.

The resulting first route still fails native DRC because its fixed transition
geometry conflicts with the retained PCIe corridor and local package escape
(673 violations, 118 shorts, 5 crossings, 469 unconnected items). This is
`ROUTE_IMPLEMENTATION_FAILURE` evidence: the route was not regenerated with
a PCIe-safe source/target allocator. The local island is not promoted and
the selected `SWAP_ETH_STORAGE` macro remains the current basis.

Receipt: `phase24_storage_usb3_local_probe.py`,
`PHASE24_STORAGE_USB3_LOCAL_COHERENT_TI_ASTAR_CLEAN.kicad_pcb`, and its native
DRC report.

`USB3_SOURCE_LOCAL_DISCRIMINATOR = COMPLETE`
`USB3_SOURCE_LOCAL_PROMOTION = NONE`
`PHASE24 = OPEN`

## South coherent storage migration probe — 2026-09-06

As a bounded macro alternative, the complete U7/J3/clock/coupling support
neighborhood was moved to the south acreage in
`PHASE24_STORAGE_SOUTH_COHERENT.kicad_pcb`, then U7 was rebound to the
authoritative TI footprint. The native planner reached both RX targets but
could not find the TX continuation under its fixed source/target transition
assumptions; it emitted no accepted route. This is a route-planner failure,
not a valid placement rejection, and no production or PCIe geometry changed.

The unblocker dispatch for distinct blocker `PHASE24_TI_U7_USB3_INTEGRATED_ROUTING`
was attempted and returned `collab spawn failed: agent thread limit reached`.
No unchanged retry was made. Local evidence remains sufficient to continue
with a cross-class transition allocator; subagent availability is not treated
as an engineering blocker.

`STORAGE_SOUTH_COHERENT_PROBE = ROUTE_IMPLEMENTATION_FAILURE`
`PHASE24 = OPEN`

## TI U7 outside-field target-transition experiment — 2026-09-06

The prior integrated mixed-layer control was corrected to place target vias
outside the TI exposed-pad field on the U7 0-degree signal-pad side, with
1.2 mm vertical staggering. The layer-aware planner could not find an F.Cu
path from the RX source transitions to those outside-field targets in the
current integrated obstacle map and emitted no candidate for that branch.

This is a bounded `ROUTE_IMPLEMENTATION_FAILURE` before copper emission, not
a production or macro-placement failure. It separates the earlier native
DRC shorts caused by target vias inside U7 pad 65 from the next problem:
coordinating an outside-field B.Cu corridor and final F.Cu dogbones without
crossing the retained board corridors. No PCIe copper or production candidate
was changed.

Receipt: `phase24_ti_usb3_mixed_integrated_astar.py` (outside-field target
transition variant).

`TI_U7_OUTSIDE_FIELD_TRANSITION = UNREACHABLE_IN_CURRENT_LAYER_MODEL`
`FAILURE_CLASS = ROUTE_IMPLEMENTATION_FAILURE`
`PHASE24 = OPEN`

## U7 0-degree mixed-layer integrated cycle — 2026-09-06

The shortest-path U7 0-degree orientation candidate received a distinct
integrated route-development cycle using RX on F.Cu and TX on B.Cu, with
ordinary source/target transitions and native obstacle maps per layer. All
four paths were authored from the saved J7/U7 pad coordinates. Native DRC
rejected the disposable result with 546 violations, including 54 shorts, 16
track crossings, 108 clearances, 119 hole-clearance findings, and 469
unconnected items.

This is `ROUTE_IMPLEMENTATION_FAILURE`, not a macro-placement conclusion:
the source and target transition allocation was still generated by a first
integrated planner and was not a validated reference-aware route. The
selected `SWAP_ETH_STORAGE` macro, PCIe ancestor, and production board remain
unchanged. Orientation-only sweeps are now evidence that the next useful
change is coordinated transition topology, not another blind rotation.

Receipt: `phase24_ti_usb3_mixed_integrated_astar.py` and
`PHASE24_STORAGE_ORIENTATION_U7_0_J3_270_TI_MIXED_ASTAR-drc.rpt`.

`TI_U7_MIXED_ORIENTATION_CYCLE = REJECTED`
`FAILURE_CLASS = ROUTE_IMPLEMENTATION_FAILURE`
`PHASE24 = OPEN`

## TI U7 orientation reachability discriminator — 2026-09-06

Five disposable native storage-orientation candidates were generated and
authoritatively rebound to the TI PVP0064A footprint: U7 rotations 180°,
180° with J3 at 0°/270°, U7 0°/J3 270°, and U7 270°/J3 270°. The native
obstacle-aware planner successfully authored all four J7-to-U7 USB3 paths for
each candidate, so no orientation was unreachable in the current raster
model. The U7 0° candidate produced the shortest first-pass path counts
(121/107/90/88 segments), but its native DRC still reports 547 violations,
including 42 shorts, 37 track crossings, 149 clearances, and 469
unconnected items.

This is not a floorplan ranking by immature DRC and does not replace the
selected `SWAP_ETH_STORAGE` macro. The orientation experiments are
`ROUTE_IMPLEMENTATION_FAILURE` evidence until a reference-aware, obstacle-
valid regenerated route passes native DRC and the storage support gate.

Receipt: `phase24_storage_orientation_discriminator.py` and the generated
`PHASE24_STORAGE_ORIENTATION_*_TI_ASTAR.kicad_pcb` disposable boards.

`TI_U7_ORIENTATION_REACHABILITY = COMPLETE`
`TI_U7_ORIENTATION_PROMOTION = NONE`
`PHASE24 = OPEN`

## CM5IO-derived source-escape integrated cycle — 2026-09-06

The next route class copied only the measured source-side geometry from the
native CM5IO-derived USB3 fixture, clipped at the explicit x=77 mm handoff,
then routed the remaining corridor on B.Cu with ordinary transitions into
the TI U7 land field. Native source handoffs were `(77.0,103.40)`,
`(77.0,101.72)`, `(77.0,78.0)`, and `(77.0,78.5)` for RX_N, RX_P, TX_N,
and TX_P respectively.

Native DRC rejected `PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI_CM5IO_SOURCE_INTEGRATED.kicad_pcb`
with 422 violations: 16 shorts, 28 track crossings, 89 clearances, 114
hole-clearance findings, and 465 unconnected items. The TX handoffs expose a
long incomplete corridor and the candidate is discarded. This remains
`ROUTE_IMPLEMENTATION_FAILURE`: it is a clipped reference transplant plus a
first integrated continuation, not a validated route cycle proving a
placement-inherent obstruction. No PCIe copper or production candidate was
changed.

The high-speed specialist dispatch was attempted but the orchestration
service again returned `collab spawn failed: agent thread limit reached`.
This availability issue is not treated as an engineering blocker; the next
cycle will use the native source evidence and a different integrated
transition topology.

Receipt: `phase24_cm5io_source_escape_integrated.py` and
`PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI_CM5IO_SOURCE_INTEGRATED-drc.rpt`.

`CM5IO_SOURCE_ESCAPE_CYCLE = REJECTED`
`FAILURE_CLASS = ROUTE_IMPLEMENTATION_FAILURE`
`PHASE24 = OPEN`

## Selected-macro integrated B.Cu source-escape experiment — 2026-09-06

The integrated B.Cu-only obstacle-aware experiment was followed by a
dedicated source-boundary variant using one ordinary through-via and
monotonic dogbone per J7 USB3 pad before the corridor search. Native DRC
rejected the variant with 464 violations, including 36 shorts, 23 track
crossings, 106 clearance findings, 119 hole-clearance findings, and 469
unconnected items. It is discarded; the prior B.Cu control (341 violations,
one short, 12 crossings) remains evidence only.

This is another `ROUTE_IMPLEMENTATION_FAILURE`: the dedicated source
transitions were placed into the existing integrated obstacle field without
an approved complete source-escape corridor. It is not evidence that the
selected `SWAP_ETH_STORAGE` macro is inferior. No PCIe copper, schematic
authority, or production candidate was changed. The next cycle must use a
source-escape topology derived from the native CM5IO launch and validate that
escape in the integrated obstacle field before promoting any copper.

Receipt: `phase24_ti_usb3_bcu_integrated_astar.py` and
`PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI_BCU_INTEGRATED_ASTAR-drc.rpt`.

`SELECTED_MACRO_SOURCE_ESCAPE_VARIANT = REJECTED`
`FAILURE_CLASS = ROUTE_IMPLEMENTATION_FAILURE`
`PHASE24 = OPEN`

## Selected-macro TI-U7 integration cycle — 2026-09-06

The selected `SWAP_ETH_STORAGE` macro was reloaded and U7 was regenerated from
the authoritative 65-pad `TUSB9261IPVP_PVP0064A` footprint. The corrected
replacement helper now resolves exported local net names to an unambiguous
`/CORE_CM5/...` hierarchy suffix and does not create duplicate USB3 net
objects. The TI mandatory-pin contract and native U7 pad-net authority audit
both pass.

Two disposable native route-development controls were evaluated against this
integrated basis. The best isolated mixed-layer control copied 20 scalar
native track/via objects, but native DRC reported 336 violations, 15
`shorting_items`, 15 `tracks_crossing`, and 469 unconnected items. The
obstacle-aware native planner authored all four source-to-U7 paths, but DRC
reported 384 violations, 15 `shorting_items`, 15 `tracks_crossing`, and 469
unconnected items. The failures include USB3 against the retained PCIe
corridor, so neither candidate is promoted.

These results are explicitly `ROUTE_IMPLEMENTATION_FAILURE`, not
`MACRO-PLACEMENT FAILURE`: one control was a fixed-coordinate transplant and
the other was a first integrated planner pass. They do not answer whether
the selected macro is topologically better than the historical board. No
PCIe copper or production candidate was changed.

The generic authoring correction is recorded in
`phase24_replace_u7_with_ti_footprint_fixture.py`; the integration experiment
is reproducible with `phase24_promote_ti_usb3_mixed_fixture.py`. Native
receipts are `PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI_MIXED_REVIEW.kicad_pcb`
and `PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI_OBSTACLE_REVIEW.kicad_pcb`.

`TI_U7_AUTHORITY = PASS`
`SELECTED_MACRO_ROUTE_CYCLE = REJECTED`
`FAILURE_CLASS = ROUTE_IMPLEMENTATION_FAILURE`
`PHASE24 = OPEN`

## Selected-macro TI-U7 v2 escape integration cycle — 2026-09-06

The zero-clearance-error disposable TI-U7 escape was applied using native
pad/net identity to the selected `SWAP_ETH_STORAGE` macro. Native DRC found
356 violations, including USB3 collisions/crossings with retained board
copper and 469 unconnected items. The candidate is rejected as a route
implementation failure: the package-only proof passed, but its fixed
absolute transition corridors were not obstacle-aware in the integrated
board. No PCIe or production copper was changed, and the floorplan decision
is unaffected.

Receipt: `phase24_promote_ti_usb3_rx_split_v2.py`,
`PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI_USB3_RX_SPLIT_V2.kicad_pcb`, and
`PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI_USB3_RX_SPLIT_V2-drc.rpt`.

`TI_U7_DISPOSABLE_ESCAPE = PASS`
`TI_U7_INTEGRATED_ESCAPE = REJECTED`
`FAILURE_CLASS = ROUTE_IMPLEMENTATION_FAILURE`
`PHASE24 = OPEN`

## Obstacle-aware integrated USB3 regeneration — 2026-09-06

The next route class removed the source transition vias and began B.Cu A* at
the actual CM5 USB3 pads, then increased the obstacle margin for retained
tracks and routed each lane sequentially. All four paths were authored, but
native DRC still found 352 violations, including 15 shorts, 85 crossings, and
469 unconnected items. This remains `ROUTE IMPLEMENTATION FAILURE`: the
planner's coarse grid/obstacle model is not yet producing manufacturable
integrated copper. The selected macro is not rejected on this evidence, and
no PCIe or production board was changed.

Receipt: `phase24_ti_usb3_bcu_integrated_astar.py`,
`PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI_BCU_INTEGRATED_ASTAR_V3.kicad_pcb`,
and its native DRC report.

`INTEGRATED_USB3_ASTAR_V3 = REJECTED`
`FAILURE_CLASS = ROUTE_IMPLEMENTATION_FAILURE`
`PHASE24 = OPEN`

## Integrated USB3 A* source-field refinement — 2026-09-06

The planner was rerun with no source transition vias and a larger retained
B.Cu obstacle margin. It reached all four native U7 targets, but native DRC
still found 349 violations, including source-pad-field crossings and U7
target-transition conflicts, plus 469 unconnected items. The observed
failures are route-authoring defects: the grid planner is not respecting the
native CM5 escape/pad-field geometry closely enough. This candidate is
rejected; the next cycle must anchor the official CM5IO source escape and
route only its continuation through the selected macro corridor.

Receipt: `phase24_ti_usb3_bcu_integrated_astar.py` and
`PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI_BCU_INTEGRATED_ASTAR_V3.kicad_pcb`.

`INTEGRATED_USB3_SOURCE_FIELD_ASTAR = REJECTED`
`FAILURE_CLASS = ROUTE_IMPLEMENTATION_FAILURE`
`PHASE24 = OPEN`

Correction to the preceding A* entry: the authoritative native DRC report
contains 352 violations consisting of 15 `shorting_items`, 15
`tracks_crossing`, 85 `clearance`, and 78 `hole_clearance` findings, plus 469
unconnected items. The prior prose accidentally called the crossing and
shorting categories the other way around; no PASS claim depends on that
summary.

## Integrated USB3 explicit lane-escape experiment — 2026-09-06

The next route class reserves the measured PCIe B.Cu spine band
(`x≈84..190`, `y≈99.5..110.5`) and gives each native CM5 USB3 pad an ordered
west-side escape, a unique south corridor, and one U7-side through-via. Native
DRC validation is the deciding evidence; the candidate is not promoted unless
it has zero true shorts/crossings and the required connectivity/mechanical
checks pass.

Receipt: `phase24_ti_usb3_integrated_lane_escape.py`.

The explicit-lane candidate was rejected after native DRC: 354 violations,
including 6 shorts, 35 crossings, 58 clearance findings, 78 hole-clearance
findings, and 469 unconnected items. It is a route implementation failure,
not a macro-placement result; the measured PCIe band reservation alone does
not solve the native CM5 source escape. The next method must transplant the
official CM5IO source-side geometry as a fixed anchor and route its
continuation with native obstacle checks.

`INTEGRATED_USB3_LANE_ESCAPE = REJECTED`
`FAILURE_CLASS = ROUTE_IMPLEMENTATION_FAILURE`
`PHASE24 = OPEN`

## Independent route review and next-method selection — 2026-09-06

The available read-only independent review confirms that the selected macro
has not yet been fairly tested with an authoritative source escape. It also
identified the native PCIe B.Cu spine as a real shared corridor constraint,
while the U7 landing-field errors are router artifacts. The review recommends
anchoring the official CM5IO source-side geometry, treating the PCIe spine as
an explicit reserved band, and solving only the continuation with ordered
lanes. This is within the approved Phase 24 architecture and does not reopen
PCIe.

The current integrated route experiments remain rejected implementation
attempts. No comparison against mature historical DRC is used to rank the
floorplan, and no terminal blocker is declared.

`INDEPENDENT_ROUTE_REVIEW = COMPLETE`
`NEXT_ROUTE_CLASS = CM5IO_ANCHORED_CONTINUATION`
`PHASE24 = OPEN`

## CM5IO-anchored source escape continuation — 2026-09-06

The official CM5IO USB3 source-side geometry was extracted from the native
reference PCB, transformed into the native J7 carrier coordinates, and
copied through each first reference transition. A disposable continuation
planner then attempted to route from those fixed anchors to the selected TI
U7 island. Native DRC rejected the integrated candidate with 3,030
violations: 11 shorts, 2,251 track crossings, 499 clearance findings, 95
hole-clearance findings, and 465 unconnected items. The source anchoring
itself is retained as authoritative evidence; the continuation planner is
rejected as a route implementation failure. No PCIe or production copper was
changed.

Receipt: `phase24_usb3_cm5io_anchored_continuation.py`,
`PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI_CM5IO_ANCHORED.kicad_pcb`, and
its native DRC report.

`CM5IO_SOURCE_ANCHOR = AUTHORITATIVE`
`CM5IO_ANCHORED_CONTINUATION = REJECTED`
`FAILURE_CLASS = ROUTE_IMPLEMENTATION_FAILURE`
`PHASE24 = OPEN`

## CM5IO-anchored outer-acreage continuation discriminator — 2026-09-06

An explicit outer-acreage continuation was tested after the interior A* path
was rejected. Each lane used the native CM5IO first transition, a separate
west staging segment, an F.Cu upper corridor, an east staging transition, and
a B.Cu lower corridor into U7. Native DRC rejected the candidate with 453
violations: 19 shorts, 57 track crossings, 85 clearance findings, 112
hole-clearance findings, and 465 unconnected items. This is a route
implementation failure; the long outer path does not provide a valid
production route and does not disprove the selected macro. The official
source anchor remains preserved, and no PCIe or production copper changed.

Receipt: `phase24_usb3_cm5io_anchored_continuation.py`,
`PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI_CM5IO_ANCHORED_OUTER.kicad_pcb`,
and its native DRC report.

`CM5IO_OUTER_CONTINUATION = REJECTED`
`FAILURE_CLASS = ROUTE_IMPLEMENTATION_FAILURE`
`PHASE24 = OPEN`

## CM5IO-anchored F.Cu lane continuation — 2026-09-06

A second continuation class kept the exact CM5IO first transition and routed
four ordered lanes on separate F.Cu corridors west of the PCIe B.Cu spine,
then used a single U7-side transition. Native DRC rejected the integrated
candidate with 392 violations: 21 shorts, 32 track crossings, 70 clearance
findings, 88 hole-clearance findings, and 465 unconnected items. The source
anchor remains authoritative, but this continuation is rejected as route
implementation failure. The next cycle must validate the transformed source
escape by itself against the carrier J7 launch before adding a long
continuation.

Receipt: `phase24_usb3_cm5io_anchored_continuation.py`,
`PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI_CM5IO_FCU_LANES.kicad_pcb`, and
its native DRC report.

`CM5IO_FCU_LANE_CONTINUATION = REJECTED`
`FAILURE_CLASS = ROUTE_IMPLEMENTATION_FAILURE`
`PHASE24 = OPEN`

## Isolated CM5IO source-anchor audit — 2026-09-06

The source-only harness was corrected after a KiCad 10 SWIG object-lifetime
crash caused by deleting a full integrated board in-process. It now uses the
native two-footprint minimal fixture, preserving J7/U7 objects and removing
only disposable tracks. The four official CM5IO first-transition escapes
map to the actual J7 pads at `(70.04,103.9)`, `(70.04,104.3)`,
`(70.04,106.3)`, and `(70.04,106.7)`; the transformed first vias are
`(61.451,87.749)`, `(61.949,87.251)`, `(61.851,83.349)`, and
`(62.349,82.851)`. Native DRC reports no shorts, crossings, clearance, or
hole-clearance findings; only expected dangling source-only geometry and 80
unconnected fixture items remain. This closes the source-anchor question and
isolates the remaining failure to continuation placement/routing.

Receipt: `phase24_cm5io_source_anchor_audit.py`,
`PHASE24_CM5IO_SOURCE_ANCHOR_AUDIT.kicad_pcb`, and
`PHASE24_CM5IO_SOURCE_ANCHOR_AUDIT-drc.rpt`.

`CM5IO_SOURCE_ANCHOR_AUDIT = PASS`
`CONTINUATION_ROUTING = OPEN`
`PHASE24 = OPEN`

## CM5IO anchored pair-layer continuation correction — 2026-09-06

The pair-layer continuation was corrected after native inspection found a
generator defect: TX_N and TX_P had shared one F.Cu x-channel, and the target
row calculation skipped the U7 TX_N row. Distinct TX channels and the native
four-row target sequence were regenerated. Native DRC still rejected the
integrated candidate with 364 violations: 4 shorts, 36 track crossings, 68
clearance findings, 81 hole-clearance findings, and 465 unconnected items.
The corrected candidate is rejected as route implementation evidence; the
isolated CM5IO source-anchor PASS and selected macro decision remain valid.

Receipt: `phase24_usb3_cm5io_anchored_continuation.py`,
`PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE_TI_CM5IO_PAIR_LAYER_SPLIT.kicad_pcb`,
and its native DRC report.

`CM5IO_PAIR_LAYER_CONTINUATION = REJECTED`
`FAILURE_CLASS = ROUTE_IMPLEMENTATION_FAILURE`
`PHASE24 = OPEN`

## Carrier-context local B.Cu source escape discriminator — 2026-09-06

The full-context audit showed the transformed CM5IO F.Cu prefix conflicts with
the existing J7 PCIe/REFCLK breakout. A local ordered B.Cu source escape was
therefore tested from the actual J7 USB3 pads to four explicit first vias.
Compared with the same selected-macro baseline (287 violations, 50 clearance,
64 hole-clearance, and 469 unconnected), the variant has 315 violations, no
shorts, no track crossings, 58 clearance, 72 hole-clearance, and 469
unconnected items. The additional findings are localized to transition/via
clearance; the prior baseline findings remain inherited. This is an improved
source-field route class but not yet a PASS; the next iteration must move the
first vias away from the inherited SERVICE/zone conflict before continuation.

Receipts: `phase24_cm5io_source_anchor_audit.py`,
`PHASE24_CM5IO_SOURCE_ANCHOR_LOCAL_B_INTEGRATED_AUDIT.kicad_pcb`, and its
native DRC report.

`LOCAL_B_SOURCE_ESCAPE = IMPROVED_REJECTED`
`ZERO_SHORTS = TRUE`
`ZERO_TRACK_CROSSINGS = TRUE`
`PHASE24 = OPEN`
### Path-B RTL_3V3 local trunk V1 (rejected)

The disposable local 3V3 trunk reduced native opens 29 to 27 but produced 17
native DRC violations by crossing/shorting the SPI field and RTL_5V escape.
It is rejected as a route implementation; the RTL_5V V3 board remains the
preferred disposable baseline and production CAD is unchanged.
### Path-B RTL_3V3 pad-52 escapes V1/V2 (rejected)

Pad-52 V1 reduced opens 29 to 28 but shorted the verified GND transition;
V2 avoided it but collided with CLKREQ and regressed to 7 DRC violations /
30 opens. Neither is promoted. The clean RTL_5V V3 disposable fixture remains
the current Path-B baseline; production CAD is unchanged.
### Path-B RSET route variants V1/V2/V3 (rejected)

RSET V1/V2 collided with C1/Y1 pads. V3 used ordinary vias and B.Cu, reached
the endpoint, and reduced opens to 28, but crossed RTL_1V1 and retained a
control-via conflict. All are rejected as route implementations; production
CAD remains unchanged.
### Path-B crystal support V1 (rejected)

The crystal candidate reached all four signal endpoints and reduced opens
29 to 25, but introduced four XTAL_IN/XTAL_OUT crossings and a C1 thermal
violation. It is rejected as route implementation evidence; production CAD
is unchanged.
### Path-B crystal support V2 (rejected)

Layer-separated crystal routing still reached the endpoints but produced
8 native DRC violations / 25 opens from U1-side XTAL crossings, RTL_1V1
interaction, and C1 thermal relief. Rejected; production CAD unchanged.
### Path-B crystal support V3/V4 (rejected)

V3 reached the full crystal endpoint set at 6 DRC / 25 opens but crossed an
RTL_1V1 escape. V4 moved the final leg and introduced XTAL_OUT shorts to
XTAL_IN and RTL_1V1, at 7 DRC / 25 opens. Both are rejected; production CAD
is unchanged.
### Path-B QFN escape map and crystal V5 (rejected)

The native QFN map is saved in `PHASE24_RTL9210B_QFN_ESCAPE_MAP_20260907.txt`.
Crystal V5 used the mapped outer perimeter but produced 18 DRC violations
from RTL_5V/control/perimeter conflicts. It is rejected; production CAD is
unchanged.
### Path-B rail audit hygiene

The stale `phase24_rtl9210b_5v_1v1_support_audit.py` helper was corrected to
target the live V3 disposable board and derive endpoint membership from
KiCad's native connectivity. It now passes three RTL_5V endpoints and eight
RTL_1V1 endpoints; it no longer uses text-count heuristics or a nonexistent
historical board.
### Path-B V3 refreshed baseline

The live V3 disposable fixture was revalidated with native KiCad: 4 DRC
violations and 29 unconnected items. The focused native endpoint audits pass
RTL_5V (U1.17/U1.33/C5.1) and RTL_1V1 (eight asserted endpoints), including
the RTL_5V negative control. No production CAD changed.
### Path-B crystal V6/V7 with pad-55 1V1 move (rejected)

Moving only the pad-55 RTL_1V1 transition did not preserve the complete
collector. V7 reported 8 native DRC violations / 26 opens and retained a
crystal-to-transition conflict. Rejected; the next repair class is full
collector relocation or coherent support-island placement.
### QFN escape-map reproducibility refresh

The native escape-map utility now queries via width with an explicit copper
layer, eliminating the KiCad `PCB_VIA::GetWidth` warning. The regenerated
map preserves the measured 0.600/0.300-mm via dimensions and is suitable for
the forthcoming full RTL_1V1 collector relocation comparison.
### Path-B crystal V11 preferred disposable baseline

V11's native endpoint audit passes XTAL_IN, XTAL_OUT, and the eight asserted
RTL_1V1 endpoints, with a negative control that fails when XTAL_OUT copper is
removed. Native DRC remains 6 violations / 25 opens, so V11 is not a closed
or production board; it is the preferred support-routing baseline.
### Path-B U2 RTL_3V3 B.Cu trunks V1 (rejected)

The U2 3V3 transition trial reduced native opens 25 to 22 but produced 8 DRC
violations from B.Cu crossings with SPI/RTL_1V1 and a remaining 3V3 branch.
It is rejected; V11 remains the preferred disposable baseline.
### Path-B U1 RTL_3V3 pad-34 escape V1 (rejected)

The pad-34 escape reduced opens 25 to 24 but shorted the RTL_5V bus and
crossed RTL_1V1, producing 9 native DRC violations. Rejected; production CAD
is unchanged.
### Path-B pad-34 3V3 escape V1 (rejected)

The pad-34 escape reduced opens 25 to 24 but shorted RTL_5V and crossed
RTL_1V1, yielding 9 native DRC violations. Rejected; isolated 3V3 escapes
are no longer the active route class.
### Path-B support-corridor decision

The native QFN map and V11/V3 experiments establish that isolated 3V3 or
crystal trace nudges are no longer a viable class. The remaining repair is a
coherent 3V3/1V1 support-branch relocation or local bridge-support move;
production CAD and Path A remain unchanged. See
`PHASE24_RTL9210B_SUPPORT_CORRIDOR_DECISION_20260907.md`.

## Current RTL9210B disposable support state — V184

The current Path-B disposable basis is
`PHASE24_RTL9210B_REFCLK_SUPPORT_RELOCATED_V184.kicad_pcb`. It retains the
west-relocated Y1/C1/C2/R1 placement from V179, the translated REFCLK
topology from V174, and the V184 RSET transition above XTAL_OUT with a
B.Cu trunk below the crystal island.

Native KiCad 10.0.5 DRC reports 243 findings / 32 unconnected items. The
signal-specific gate passes: V184 contains zero `shorting_items` and zero
`tracks_crossing`. Remaining findings are inherited disposable-board
clearance/zone/manufacturing/open findings and are not waived.
`phase24_rtl9210b_refclk_support_relocated_v184_audit.py` passes saved native
connectivity for XTAL_IN, XTAL_OUT, RSET, REFCLK_P, and REFCLK_N, plus five
trace-removal negative controls.

V184 is a promoted local route sub-primitive, not a Path-B or production
board PASS. The next work is the remaining RTL9210B support network and its
full native/parity/mode validation. Path A, production CAD, and the accepted
macro-floorplan remain unchanged.

## Current RTL9210B rail slice — V185

The latest disposable support basis is
`PHASE24_RTL9210B_RTL3V3_U134_C3_V185.kicad_pcb`, which adds the
native-pad-derived U1.34-to-C3.1 RTL_3V3 handoff to V184. Native KiCad DRC
reports 254 findings / 31 unconnected items and zero `shorting_items` or
`tracks_crossing`. The saved-board audit passes U1.34↔C3.1 connectivity and
its trace-removal negative control.

This is a promoted local rail sub-primitive only. The other RTL_3V3 branches,
support rails, SPI/control paths, and full Path-B validation remain open;
Path A and production CAD remain unchanged.

## Current RTL9210B 5V rail slice — V187

`PHASE24_RTL9210B_RTL5V_U133_C5_V187.kicad_pcb` adds the native U1.33 to
C5.1 RTL_5V handoff above the V186 RTL_3V3 corridor. Native KiCad DRC
reports 270 findings / 29 unconnected items with zero `shorting_items` or
`tracks_crossing`; the saved-board connectivity audit and trace-removal
negative control pass.

This remains disposable support evidence only. RTL_5V's remaining source/
support joins, RTL_1V1, west-field RTL_3V3, SPI/control, and full Path-B mode
validation remain open.

## Current RTL9210B SPICS slice — V189

`PHASE24_RTL9210B_SPICS_U124_U2_V189.kicad_pcb` adds the native U1.24 to
U2.1 SPICS route above the existing rail corridors. Native KiCad DRC reports
293 findings / 27 unconnected items with zero `shorting_items` or
`tracks_crossing`; the saved native connectivity audit and trace-removal
negative control pass.

This is disposable SPI evidence only. The remaining SPI nets, rail branches,
controls, mode validation, and production integration remain open.

## Current RTL9210B 1V1 rail slice — V188

`PHASE24_RTL9210B_RTL1V1_U116_C4_V188.kicad_pcb` adds the native U1.16 to
C4.1 RTL_1V1 handoff on a dedicated B.Cu corridor. Native KiCad DRC reports
282 findings / 28 unconnected items with zero `shorting_items` or
`tracks_crossing`; saved native connectivity and the trace-removal negative
control pass.

This is disposable rail evidence only. The remaining RTL_1V1 collector,
west-field RTL_3V3 launches, SPI/control paths, and full Path-B validation
remain open.

## Current RTL9210B shared 3V3 rail — V186

The latest disposable rail basis is
`PHASE24_RTL9210B_RTL3V3_U134_PAD20_V186.kicad_pcb`. It extends the passing
V185 U1.34-to-C3.1 rail with a native U1.20 launch into the existing B.Cu
RTL_3V3 trunk. Native KiCad DRC reports 259 findings / 30 unconnected items
and zero `shorting_items` or `tracks_crossing`. The saved-board audit passes
U1.20/U1.34/C3.1 connectivity and the trace-removal negative control.

The west-field U1.39/U1.52 launches remain intentionally open because their
current placement is co-located with the crystal/RSET field; they are not
being misclassified as solved by V186. Path A and production CAD remain
unchanged.
## Current RTL9210B coordinated SPI source-field basis — V208

The current disposable Path-B support basis is
`PHASE24_RTL9210B_SPI_SOURCE_FIELD_V208.kicad_pcb`. It co-authors the
RTL_3V3, SPICLK, SPISI, and XTAL_IN source/destination fields rather than
stacking those routes independently. Native KiCad DRC reports 337 findings /
25 unconnected items, with zero `shorting_items` and zero
`tracks_crossing`. The saved-board native audit passes all four asserted net
groups and four trace-removal negative controls.

V208 is a promoted disposable route basis only. It is not a Path-B closure,
production-CAD change, or Path-A replacement. Remaining RTL9210B rails and
controls, USB/SATA high-speed paths, mode-aware validation, procurement and
firmware gates, and full integration remain open. Path A and the production
board remain unchanged.
## Current RTL9210B SPISO3 source-field basis — V211

`PHASE24_RTL9210B_SPISO3_U122_U2_V211.kicad_pcb` adds the U1.22-to-U2.7
SPISO3 path to the V208 coordinated source-field basis. The source uses a
short diagonal F.Cu dogbone, an ordinary-via B.Cu handoff, and an outboard
F.Cu corridor to the flash pad. Native DRC reports 357 findings / 24
unconnected items with zero `shorting_items` and zero `tracks_crossing`;
native saved-board connectivity and the trace-removal negative control pass.

V211 is disposable Path-B route evidence only. It does not close Path B or
change production CAD/Path A. Remaining support rails, controls, USB/SATA
high-speed paths, mode validation, firmware/procurement, and integration
gates remain open.
## Current RTL9210B PEDET sideband basis — V212

`PHASE24_RTL9210B_PEDET_U18_J1_69_V212.kicad_pcb` extends the V211
disposable basis with the native U1.8 PEDET connection to M.2 contact 69.
Native DRC reports 370 findings / 23 unconnected items with zero
`shorting_items` and zero `tracks_crossing`; native saved-board connectivity
and the trace-removal negative control pass.

This remains disposable Path-B evidence only. It does not close Path B or
change Path A/production CAD. Reset/CLKREQ, remaining rail branches, USB/SATA
high-speed paths, mode-aware validation, firmware/procurement, and integrated
mechanical/DFM gates remain open.
## Current RTL9210B complete PEDET support basis — V215

`PHASE24_RTL9210B_PEDET_R2_U18_J1_69_V215.kicad_pcb` extends the V212
U1.8-to-J1.69 sideband with the R2.1 PEDET pull network. The R2 return is
carried around the outboard ends of the existing REFCLK and RTL_5V B.Cu
corridors. Native DRC reports 381 findings / 22 unconnected items with zero
`shorting_items` and zero `tracks_crossing`; the saved-board audit joins all
three PEDET endpoints and passes its trace-removal negative control.

V215 is disposable Path-B evidence only; Path A and production CAD remain
unchanged. Remaining CLKREQ/PERST, support-rail branches, USB/SATA
high-speed, mode-aware, firmware/procurement, and integrated DFM gates remain
open.
## Current RTL9210B sideband state — PEDET complete; CLKREQ/PERST source fields open

V215 is the current complete PEDET basis. V220 provides a clean disposable
U1.13-to-J1.52 CLKREQ launch but does not include the R3.1 pull-network
return. V221's R3 completion attempt was rejected for PEDET/XTAL conflicts.
PERST attempts V222–V225 all pass narrow endpoint connectivity audits but are
rejected by native source-field crossings/shorts, with V225's remaining
defect localized to the U1.14/RTL_1V1 field. These are route-allocation
findings, not architecture or component rejection. Path A, production CAD,
and the accepted macro-floorplan remain unchanged.
## Current RTL9210B PERST source-field finding — V226 rejected

V226 preserved endpoint connectivity but its U1.14 transition still
intersects the promoted REFCLK_P B.Cu corridor. The remaining PERST issue is
therefore localized to the coupled U1.14/REFCLK/QFN source field; it is not a
connector or long-corridor failure. V220 remains the clean partial CLKREQ
U1/J1 slice, while R3.1 and complete PERST remain open. Path A and production
CAD are unchanged.
## Current RTL9210B coupled QFN sideband basis — V227

`PHASE24_RTL9210B_QFN_SIDEBAND_SPISO3_PERST_V227.kicad_pcb` is the current
disposable basis for the coupled U1 source field. It co-authors SPISO3 and
PERST around the QFN rather than preserving their conflicting historical
departures. Native DRC reports 392 findings / 21 unconnected items with zero
`shorting_items` and zero `tracks_crossing`; native connectivity and two
trace-removal negative controls pass.

This is not Path-B closure or production integration. CLKREQ/R3.1, remaining
support rails, USB/SATA high-speed routing, mode-aware validation,
firmware/procurement, and integrated mechanical/DFM gates remain open. Path A
and production CAD remain unchanged.
## Current RTL9210B CLKREQ finding — V228 rejected

V228 proves the complete U1.13/R3.1/J1.52 endpoint mapping natively, but its
candidate routing conflicts with RSET, REFCLK_N, and PERST in the local
sideband field. It is rejected as a route implementation. The next attempt
must co-author that three-net corridor; V227 remains the promoted disposable
SPISO3/PERST basis. Path A and production CAD remain unchanged.
## Current RTL9210B complete CLKREQ basis — V231

`PHASE24_RTL9210B_CLKREQ_R3_U113_J1_52_V231.kicad_pcb` extends the V227
coupled source-field basis with a complete U1.13/R3.1/J1.52 CLKREQ network.
The route uses a low B.Cu return, a short layer-separated overpass around
PERST, and a west-shifted R3 escape. Native DRC reports 435 findings / 19
unconnected items with zero `shorting_items` and zero `tracks_crossing`;
native connectivity and the trace-removal negative control pass.

V231 remains disposable Path-B evidence, not production integration or Path-B
closure. Remaining support rails, USB/SATA high-speed paths, mode-aware
validation, firmware/procurement, and integrated DFM/mechanical gates remain
open. Path A and production CAD remain unchanged.
## Current RTL9210B RTL_3V3 support basis — V232

`PHASE24_RTL9210B_RTL3V3_U139_V232.kicad_pcb` extends the V231 sideband
basis with the native U1.39 RTL_3V3 branch. Native DRC reports 448 findings /
18 unconnected items with zero `shorting_items` and zero `tracks_crossing`;
the saved-board U1.39/C3.1 audit and trace-removal negative control pass.

This remains disposable Path-B support evidence. Remaining rail branches,
high-speed routing, mode-aware validation, firmware/procurement, and
production integration remain open; Path A and production CAD are unchanged.
## Current RTL9210B lower 3V3 finding — U1.52 remains open

V233 proves U1.52-to-C3.1 endpoint connectivity but is rejected by native
DRC for a lower-field XTAL_OUT crossing and conflict with the promoted CLKREQ
return. This is a local coordinated rail/crystal allocation issue; the V232
U1.39 branch remains promoted. Path A and production CAD are unchanged.
## Current RTL9210B U1.52 RTL_3V3 basis — V237

`PHASE24_RTL9210B_RTL3V3_U152_V237.kicad_pcb` extends V232 with a
coordinated U1.52 rail escape above pad 49, RSET, and the XTAL_IN diagonal.
Native DRC reports 466 findings / 17 unconnected items with zero
`shorting_items` and zero `tracks_crossing`; the saved-board U1.52/C3.1
audit and trace-removal negative control pass.

V237 is disposable support evidence only. Remaining RTL_3V3/RTL_1V1
branches, high-speed paths, mode-aware validation, firmware/procurement, and
production integration remain open. Path A and production CAD remain
unchanged.
## Current RTL9210B rail-field state — U1.36 remains open

V238 proves the U1.36-to-C4.1 rail endpoints but retains one local crossing
with the U1.39 3V3 escape. V239's attempt to move U1.39 was rejected for
XTAL_OUT contact and U1.52 3V3 interaction. No rail branch is being called
closed from these partial results; the next repair is a coordinated
U1.36/U1.39/U1.52 lower-field allocation. Path A and production CAD remain
unchanged.

V240/V241 are rejected U1.36 RTL_1V1 co-allocation trials: V240 crossed the
SPISI field and V241 replaced that crossing with a via short. V242 is the
promoted corrected basis. Its first authoring pass omitted the B.Cu trunk
extension to the moved via; after correction, native connectivity joins
U1.36/C4.1, U1.39/C3.1, and U1.52/C3.1 and the trace-removal negative control
fails as required. Native DRC reports 484 findings / 16 unconnected items
with zero `shorting_items` or `tracks_crossing`. Remaining RTL_1V1 branches,
high-speed paths, and full Path-B validation remain open; Path A and
production/acreage CAD remain unchanged.
V244 is rejected as a U1.50 RTL_1V1 route implementation. Native connectivity
and the trace-removal negative control pass, but native DRC reports 496
findings / 15 unconnected items and three track crossings: the new B.Cu
vertical crosses RTL_5V and RTL_3V3, and the source leg crosses RTL_3V3.
V242 remains the promoted disposable rail basis.
V248 is rejected after its corrected native audit and full-rail-removal
negative control passed, but native DRC reports 527 findings / 14 opens with
an REFCLK_N crossing and a no-connect-pad/RTL_3V3 short in the source field.
The next source escape must move farther from those fields.
V249 is rejected: native rail/REFCLK connectivity and the trace-removal
negative control pass, but DRC reports two source-field crossings and one
REFCLK_N/RTL_1V1 short at the QFN launches (525 findings / 14 opens). The
next trial must separate the first F.Cu departures before either transition.
V246 is rejected pending one local overpass: its native audit and negative
control pass, while DRC reduces the new lower-edge problem to an
RTL_1V1/PERST_N crossing at the B.Cu handoff near (104.5,65.8). One retained
ISOLATEB/CLKREQ_N shorting class is also reported. No Path-A or production
CAD change occurred.
V245 is rejected as a translated U1.60/U1.63 lower-edge route. Native
connectivity and the trace-removal negative control pass, but native DRC
reports 502 findings / 14 unconnected items and five track crossings against
RTL_5V, PEDET, RTL_3V3, REFCLK_P, and PERST_N. The lower-edge topology must
be co-authored with those existing fields; V242 remains promoted.
V243 is rejected as a U1.40 RTL_1V1 route implementation. Its corrected
native audit passes U1.36/U1.40-to-C4.1 and U1.39/U1.52-to-C3.1 assertions
with the required trace-removal negative control, but native DRC introduces
three signal shorting classes (USB_RXN0/RTL_3V3 twice and ISOLATEB/CLKREQ_N)
at 493 findings / 15 unconnected items. V242 remains the promoted rail
basis; no Path-A or production/acreage CAD change occurred.
V250 is rejected: native rail/REFCLK connectivity and the trace-removal
negative control pass, but DRC reports 541 findings / 14 opens with three
signal shorts and one source-field crossing. The next experiment must
co-relocate inherited USB/3V3/GND fields with the QFN departures.
V255 is retained as native A* routing evidence, not a promotion: exact
pad-center endpoint emission and native U1.36/U1.40 connectivity pass, while
DRC reports 628 findings / 15 opens and one RTL_3V3/RSET short with no track
crossing class. V242 remains the promoted disposable rail basis.
V254 is rejected: its native connectivity and negative control pass, but DRC
reports 546 findings / 14 opens with new RTL_1V1/RTL_3V3 crossings and a
retained ISOLATEB/CLKREQ_N short. The complete adjacent support cluster must
move together.
V256 is retained as a local U1.52 co-clearance experiment, not a promotion:
native U1.36/U1.40 connectivity and the trace-removal negative control pass;
DRC reports 623 findings / 16 opens with no shorting or track-crossing class.
The promoted disposable rail basis remains V242.
V257 joins the repaired U1.52 RTL_3V3 branch and exposes the inherited
ISOLATEB/CLKREQ_N short (626 findings / 15 opens); it is rejected. V258's
independent bottom-edge RTL_1V1 vias reduce opens to 13 but create multiple
REFCLK/XTAL shorts (668 findings); it is also rejected. The next Path-B
experiment must co-author the complete QFN rail/clock support field.
V259/V260 are rejected CLKREQ_N re-escapes: V259 trades the ISOLATEB short
for a REFCLK_N crossing, and V260 retains that crossing after a south dogleg.
The next experiment is a coordinated CLKREQ/REFCLK/sideband field, not another
single-net departure.
V261 is retained as the best current CLKREQ_N local geometry: native DRC has
no shorting or track-crossing class (633 findings / 15 opens), but the full
RTL9210B QFN support field remains incomplete and unpromoted.
V262 is rejected: moving the RTL_1V1 via bus to y=68.8 mm reduced opens to 13
but created multiple RTL_1V1/REFCLK/XTAL shorting classes. The next repair is
coherent support-component relocation with coordinated field regeneration.
V266 is the retained scrubbed placement baseline: after correcting the V265
Y1/C1 overlap, native DRC reports 228 findings / 36 opens with no shorting or
track-crossing class and zero footprint errors. Support copper is intentionally
absent; route regeneration now starts from this placement.
V269 is the retained crystal-field basis: four native net joins (U1/Y1/C1/C2)
pass, while DRC reports 293 findings / 32 opens with no shorts/crossings and
zero footprint errors. V267/V268 are rejected crystal route implementations;
the remaining rail, reset, SPI, and high-speed support field is open.
V270 is the retained RSET-route basis: native U1.51/R1.1 connectivity passes;
DRC reports 307 findings / 31 opens with no shorts/crossings and zero footprint
errors. Rail, control, SPI, and high-speed support remain open.
V274 is the retained combined crystal/RSET/RTL_3V3 support basis: native
connectivity confirms four RTL_3V3 joins in addition to the V269 crystal and
V270 RSET joins. DRC reports 319 findings / 27 opens with no shorts/crossings
and zero footprint errors; the full Path-B support field remains open.
V275–V277 are rejected SPICS route implementations: V275 crosses both crystal
trunks, V276 crosses RTL_3V3, and V277 crosses B.Cu REFCLK. V278 is retained as
the corrected SPICS basis: native U1.24/U2.1 connectivity and a trace-removal
negative control pass; native DRC has 335 findings / 26 inherited opens, no
shorting or crossing class, and zero footprint errors. Remaining SPI, PEDET,
reset, rail, and high-speed support routes are still open.
V279–V281 are rejected SPISO route implementations: each retained a real
crossing with the promoted SPICS/crystal/support field. V282 is retained as
the corrected two-net SPI basis: native U1.24/U2.1 and U1.23/U2.2 connectivity
pass, both trace-removal negative controls pass, and native DRC has 366
findings / 25 inherited opens with no shorting or crossing class and zero
footprint errors. SPISO3, SPICLK, SPISI, PEDET, reset, remaining rails, and
high-speed support remain open.
V309/V310 are rejected CLKREQ source-field variants: V309 crossed SPISI and
PEDET, while V310 moved those crossings but retained SPISO3. V311 stops the
R3 B.Cu trunk above SPISO3 and is retained: native connectivity joins
R3.1/U1.13/J1.52, and DRC reports 514 findings / 18 inherited opens with no
shorting, crossing, or footprint-error class. Remaining reset, rails, and
high-speed support remain open.
V306/V307 removed the earlier CLKREQ/PEDET and CLKREQ/RTL_3V3 source-field
defects, but V306 retained a crystal-field crossing. V308 shifted the R3
departure and introduced real XTAL_IN/XTAL_OUT shorts at the vertical
transition, so it is rejected. CLKREQ remains open at the R3-to-transition
geometry; no architecture or production CAD changed.
V304 removes the V303 PEDET/R2 source-field shorts but crosses retained
SPICLK/SPISI and XTAL_IN geometry. V305 separates the outer column with a
layer transition, but still crosses the retained SPISI lane and XTAL_IN at
the R3 launch. Both are route-implementation failures; CLKREQ remains open.
V303 is rejected: the lower CLKREQ corridor avoids the prior SPI crossings,
but its R3 launch overlaps the PEDET field and its source geometry creates
CLKREQ/PEDET and CLKREQ/RTL_3V3 shorts. This remains a source-field route
implementation issue; the next repair must co-author R3/U1 escapes with the
existing PEDET and rail geometry.
V302 is rejected: the alternate CLKREQ launch shorts the PEDET R2 pad and
the U1 ISOLATEB field. Although its native endpoint count is 18, the source
geometry is invalid. The next CLKREQ repair must preserve R2 and ISOLATEB
clearance while co-authoring the local sideband field.
V301 is retained as a CLKREQ topology basis but not promoted. Native endpoint
connectivity reduces the saved-board open count to 18, while DRC identifies
CLKREQ/SPISO and CLKREQ/XTAL_IN crossings plus a CLKREQ/REFCLK_N short at the
U1 transition. The next repair is the U1-side CLKREQ transition; no
architecture or production CAD change was made.
V299 removed all PEDET/PERST crossing classes with a U-shaped approach but
exposed a floating J1 branch junction. V300 adds the missing same-net F.Cu
join. Native connectivity now joins R2.1/U1.8/J1.69; native DRC reports 454
findings / 20 inherited opens with no shorting, crossing, or footprint-error
class. PEDET is retained as closed in the disposable sideband basis; CLKREQ,
reset, remaining rails, and high-speed support remain open.
V295–V298 are retained PEDET/PERST local-field experiments, not promoted:
V295 moved PERST to B.Cu and crossed REFCLK; V296–V298 kept PERST on F.Cu
and progressively moved the local dogleg, but each retained one native
PEDET/PERST crossing. The next repair must co-author both sideband launches
as a single field. No production or Path-A CAD changed.
V294 improves the PEDET launch and retains the R2/J1 trunk, but native DRC
still reports one PEDET/PERST crossing at the U1 landing. PEDET remains open;
the next repair must coordinate the local PEDET and PERST sideband field.
V290 and V291 PEDET trials reduced the sideband open count but retained
crossings with the existing REFCLK/PERST corridors. V292 removes REFCLK and
leaves one PERST crossing. V293 avoids that crossing but shorts JTAG/undefined
field geometry, so it is rejected. PEDET remains open for a farther-out layer
transition; no architecture or production CAD change was made.
The combined V289 chain now passes the full native five-net SPI audit:
SPISI U1.18/U2.5, SPICLK U1.19/U2.6, SPISO3 U1.22/U2.7, SPISO U1.23/U2.2,
and SPICS U1.24/U2.1. The trace-removal negative control fails as required.
The saved V289 DRC summary remains 420 findings / 22 inherited opens with no
shorting, crossing, or footprint-error class. The SPI field is retained;
remaining RTL9210B control, rail, and high-speed support remain open.
V289 is retained as the SPISI basis: native U1.18/U2.5 connectivity passes;
native DRC reports 420 findings / 22 inherited opens with no shorting or
crossing class and zero footprint errors. The four-net SPI source escape is
now represented by retained SPICS, SPISO, SPISO3, and SPICLK/SPISI bases;
remaining support and high-speed routes remain open.
V288 is retained as the SPICLK basis: the shorter U1.19 escape reaches its
through-via before the RTL_3V3 handoff, native connectivity joins U1.19/U2.6,
and native DRC reports 402 findings / 23 inherited opens with no shorting or
crossing class and zero footprint errors. SPISI, PEDET, reset, remaining rails,
and high-speed support remain open.
V287 is rejected: the independent SPICLK trial crosses the retained
RTL_3V3 source-field handoff at the U1 north escape. The high-north B.Cu
destination corridor itself remains plausible, but the next pass must
co-author SPICLK with SPISO3/SPISI and the RTL_3V3 source field.
V285 is rejected because its SPISO3 B.Cu trunk crosses XTAL_IN. V286 is
retained as the corrected SPISO3 basis: native U1.22/U2.7 connectivity and
trace-removal negative control pass; DRC has 383 findings / 24 inherited
opens with no shorting or crossing class and zero footprint errors. SPICLK,
SPISI, PEDET, reset, remaining rails, and high-speed support remain open.
V283 is rejected: the independent SPISO3 trial creates native SPISO3/SPISO
and SPISO3/GND shorting classes and an RTL_3V3 source-field crossing. This is
a route-implementation failure; the retained V278/V282 placement and bases
remain valid. Remaining SPI channels must be allocated as one coordinated
field.
V284 is rejected: the high-north SPISO3 trial avoids the lower SPI crossings
but creates a native SPISO3/GND short at the C1 crystal-support pad. This is
another route-implementation failure; the next experiment must allocate
SPISO3, SPICLK, and SPISI together around the source/support field.

V312/V313 are rejected RTL_5V implementation trials from the saved V311
sideband basis. Both close the native RTL_5V endpoint opens, but V312 creates
three short/crossing classes in the upper QFN field and V313 creates one
short plus three crossing classes on its perimeter escape. They are route
implementation failures, not evidence against the RTL9210B support topology.
V311 remains the current disposable reference; RTL_1V1, RTL_3V3, and lane-0
support remain open.

V320 corrects a disposable authoring defect in the RTL9210B M.2 fixture:
J1's pad coordinates were board-absolute under a `(0,0)` footprint anchor.
The normalization gives J1 a real `(127,66)` local anchor while a reload
assertion proves every physical pad center is unchanged. Native DRC remains
the inherited V311 result (18 opens, no new short/crossing class), so V320 is
an authoring-basis correction, not a Path-B routing pass or production-CAD
promotion.

V314/V315 are rejected rail-field trials: V314 reduced opens to 13 but
introduced four shorts and three crossings; V315 reduced opens to 16 but
introduced four shorts and four crossings. V316/V317 are rejected lane-0
trials: both reduced opens to 14 but retained real lane shorts/crossings.
These are route-implementation failures in the dense V311 field, not a
Path-B architecture rejection; production CAD and Path A remain unchanged.

V318/V319 tested the cross-class coordinated rail hypothesis using the
designated In2 power layer. They reduced the native open count to 15 but are
rejected: the proposed transitions collided with existing SPI/PEDET copper,
U2 pad fields, and J1 SSD_3V3 at the chosen endpoints, with 7/11 native
shorting classes and crossings respectively. Inner-layer power remains an
available contract resource, but the next route must be generated with a
single coordinated rail/lane via map; no production CAD or Path A changed.

V323 is the retained coherent-placement probe: U1 is at `(106,62)` with
180-degree orientation and the local support cluster moves coherently. V328
routes all four RTL9210B lane-0 nets from the transformed U1 bank to J1 with
zero native shorting/crossing findings; its saved-board audit and trace-
removal negative control pass. Support rails/control/REFCLK remain open, so
V328 is a lane-only primitive rather than full Path-B closure.

V337 clears the relocated crystal trio from C4, producing an unrouted native
placement with no shorting or crossing class. V339 routes XTAL_IN and
XTAL_OUT on separate B.Cu spines with native F.Cu capacitor handoffs; DRC
reports zero shorting and zero crossing classes. The saved-board crystal
audit and trace-removal negative control pass. Crystal support is retained;
rails, controls, SPI, REFCLK, USB, M.2 launch, and power remain open.

V340 adds RSET on the retained V339 crystal/lane placement. Native DRC has
zero shorting and crossing classes; the saved-board U1.51/R1.1 audit and
trace-removal negative control pass. RSET is retained as a local primitive;
the remaining RTL9210B support/interface nets remain open.
## Active Path-B continuation — V552/V553 lower-field discriminator (2026-09-08)

The live isolated RTL9210B baseline remains V546: RTL_3V3 is fully collected,
RTL_5V U1.17/U1.33 is natively connected, and the east-side U1.40 RTL_1V1
escape is retained. V552 and V553 attempted coordinated completion of the
remaining U1.55/U1.60/U1.63 RTL_1V1 group while reallocating XTAL_OUT. Native
DRC rejected both candidates for actual lower-field crossings/clearance and
shorting involving XTAL_IN/XTAL_OUT, RTL_3V3, REFCLK, and LANE0. These are
route-implementation failures; Path A, production CAD, and the selected Path-B
architecture are unchanged. The next experiment must co-author the complete
bottom signal-field allocation, rather than add another collector-only route.
V554 is rejected as a lower-field route implementation: moving RX source
escapes to B.Cu reduced the isolated open count but created native RX P/N,
REFCLK, XTAL_OUT, RTL_3V3, and RTL_1V1 collision classes. The next Path-B
trial must regenerate the complete lower QFN source field coherently; no
architecture, Path-A, or production-CAD change was made.
V555 tested an outboard B.Cu RTL_1V1 return to the valid upper trunk. Native
DRC rejected it for crossings with RTL_3V3/RTL_5V and remaining XTAL_OUT,
RX, and REFCLK source-field conflicts. This is a route-implementation
failure; the complete lower QFN field remains open and no architecture,
Path-A, or production-CAD change was made.
V556 tested an In2.Cu RTL_1V1 plane with ordinary-via escapes. Native DRC
rejected the source dogbones/vias against adjacent RX/XTAL/TXN and support
geometry, so the plane does not remove the lower QFN breakout constraint.
The Path-B lower-field gate remains open for coherent source-field
regeneration; no architecture, Path-A, or production-CAD change was made.
V557 tested the V388 right-edge supply orientation with an In2 RTL_1V1 plane.
Native DRC rejected it for inherited RX/XTAL/GND source-field conflicts and a
C4 ground collision. This is a route-implementation/source-field integration
failure, not an architecture rejection; the next trial must regenerate the
orientation and neighboring launches together.
V558 corrected the V546 evidence basis by widening its 100 tracks to the
production 0.2 mm width and rerunning native DRC under the strict production
ruleset. It reports 25 findings / 26 unconnected items, including seven real
clearance errors but no shorting or crossing class. V546 is now a topology
basis only, not a production-clean primitive; the lower source-field gate
and strict-width cleanup remain open.
V560/V561 tested duplicate-copper cleanup on the V368 all-eight RTL_1V1
topology. Both reduced apparent DRC clutter but caused the native saved-board
graph to disconnect U1.25, so neither is promotable. The original V368
topology remains the evidence basis; cleanup is a tooling-risk item requiring
connectivity-preserving regression coverage.
V562 is the retained corrected Path-B support baseline. It regenerates the
V368 RTL_1V1 field from V342 without duplicate support copper and passes the
native all-eight 1V1/C4, 3V3, crystal, and RSET audit with a route-and-zone
negative control. Native DRC has 11 findings / 21 unconnected pads, zero
shorting/crossing classes, and zero footprint errors. Remaining open nets are
RTL_5V, GND attachment, PEDET/CLKREQ/PERST, SPI, REFCLK, and lane-0.
V563 connects U1.17/U1.33/C5.1 in the native saved-board graph, but native
DRC rejects its west/outer RTL_5V corridor for XTAL_OUT, RTL_3V3, and PEDET
collision classes. RTL_5V remains open; V562 remains the retained Path-B
support baseline.
V564 is rejected: its lower outboard RTL_5V route failed native source-pad
joining and introduced RTL_5V/SPISI, RTL_5V/RTL_3V3, and RTL_5V/PEDET DRC
collisions. V562 remains the retained support baseline; RTL_5V is still open.
V565 tested a local In2 RTL_5V plane with explicit source vias. Native DRC
rejected the vias against the RTL_3V3 field, and native connectivity left the
5V branches disconnected. RTL_5V remains open; V562 remains the retained
Path-B support baseline.
## Current Path-B continuation — U1.39 lower RTL_3V3 discriminator (2026-09-08)

The isolated RTL9210B Path-B gate remains OPEN. The U1.39-to-U2.8
RTL_3V3 subprimitive was regenerated from the retained V35/U2-left upper
RTL_3V3 basis and passes the saved-board native connectivity audit, including
the required trace-removal negative control. It is not promotable: native DRC
reports nine violations, including an RTL_1V1/RTL_3V3 short at the QFN field,
RTL_3V3 clearance/solder-mask conflicts with adjacent USB pads, and inherited
warnings. The earlier diagonal version reported eight violations; the revised
exit reduced neither the root QFN escape constraint nor the shorting class.
This is a route-implementation failure, not a Path-B architecture or Path-A
failure. The candidate is preserved as raw V620/V621/V622 evidence; no production
CAD or Path A changed. The next trial must allocate the complete lower QFN
source field coherently, with the active 0.20 mm width/clearance rules
unchanged.

The complete lower-3V3 V623 generator was also rerun as a coordinated
comparison. Native DRC rejects it for an RTL_3V3/RSET short and crossing at
U1.52/R1 plus the U1.39/USB_DM source-field clearance. It remains raw route
evidence only; the next implementation must allocate the lower QFN field and
RSET together rather than reuse these handoff coordinates.
The first copper implementation on the 0-degree basis is rejected as a route
implementation (V624): native DRC reports 30 findings, including source-pad
shorts/clearances, RSET adjacency, and edge-clearance violations. The clean
0-degree no-copper probe remains retained; V624 does not reject its placement
or the RTL9210B architecture.
V625 tested a farther-out U1.39 perimeter escape on the native 0-degree
basis. Native DRC still rejects the first F.Cu segment at adjacent USB_DP/DM
pad bodies and solder-mask bridging, despite moving the via well outside the
field. This confirms an intrinsic 0.4 mm-pitch QFN/strict-width source escape
constraint; V625 is rejected route evidence. No Path A or production CAD
changed.
V626 is a disposable JLC-width discriminator only. It used 0.13208 mm
tracks and 0.50/0.25 mm vias on the 0-degree U1.39 source escape. Native DRC
still found adjacent USB-pad clearance and solder-mask conflicts; it also
flagged the 0.25 mm drill below the saved board's 0.30 mm minimum and the
0.13208 mm track below the active 0.20 mm netclass. It is rejected and does
not authorize changing the production rules.
V627 tested an ordinary 0.60/0.30 mm through-via directly in the U1.39 pad
on the native 0-degree basis. Native DRC rejects via-in-pad here: the via
shorts adjacent USB_DM and violates the 0.25 mm hole-clearance rule to both
neighboring QFN pads. This authorized cross-class alternative is rejected;
no production rule or Path A artifact changed.
The storage parity audit was corrected to normalize only KiCad's hierarchical
XML net paths to the PCB's flattened net names. The older 64-actionable-
mismatch result on `PHASE24_DUAL_MODE_STORAGE_PLACEMENT.kicad_pcb` is
superseded by the live U12 instance-label correction recorded below; its
listed defects remain historical evidence, not current requirements.
V653's local Y1/C1/C2 relocation is rejected. It reduces the crystal span but
creates C2/RTL_1V1 clearance and shorting findings, while XTAL_IN still
contacts the nearby RTL_3V3 transition. Crystal routing requires co-authored
source-field and capacitor placement.
