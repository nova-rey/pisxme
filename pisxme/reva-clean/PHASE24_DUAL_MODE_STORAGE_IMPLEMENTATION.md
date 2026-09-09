# Phase 24 dual-mode storage implementation

## CURRENT STATE — documentation authority (2026-09-08)

The live Path-A dual-mode storage implementation includes the corrected
J8 mode jumper, source-owned U12/U11 mappings, corrected TI selector and
JMS583 QFN64 package authorities, the authored JMS583 support network, and
the VBUS/sense divider. Current native focused audits pass USB3, SATA, mode
control, complete JMS583 support, and schematic-to-PCB pad parity on the
current regenerated basis. This does not close Phase 24: native DRC,
complete copper quality, power/ground attachment, and integrated-board
closure remain OPEN.

The older opening paragraphs and historical sections that describe support
circuitry as needing instantiation, use malformed pre-correction footprints,
or refer to pre-J8/pre-parity routing are SUPERSEDED evidence, not current
instructions. Raw receipts, negative controls, and rejected experiments are
retained unchanged. V13 is the current disposable co-authored
USB_TXP/USB_TXN/JMS_AVDDL local-field basis; complete storage-field
regeneration, native DRC, and full-board closure remain open.

The V3/V4 co-authored source-field experiments are superseded route evidence:
V3 passes the focused USB3 and JMS583 support audits without a shorting class,
but creates two local TX-pair crossings at the U11 escape; V4 adds an
asymmetric layer handoff and is worse at 734 native DRC findings. Neither is
production authority. The VBUS V1 basis remains the live parent for the next
source-field regeneration.

The subsequent straight-pair V5 and south-transition V6 experiments are also
superseded route evidence. V5 removes the TX self-crossing but shorts the
USB_TXP1 path to the AVDDL via; V6 moves the via and creates additional
USB_TXP1/AVDDL and USB_RXP1/AVDDL shorts. Focused endpoint audits remain
useful, but neither candidate is production authority. The required next
class is complete lower U11 pad-field allocation.

The C86/C87 local-relocation V1 is superseded route evidence. Focused USB3
and JMS583 support checks pass, but native DRC reports 760 findings and real
JMS_USB3_TXP/AVDD33 and JMS_USB3_TXN/USB_TXP1 shorts. It is not production
authority and does not change the selected parent.

The 180-degree JMS583/TX-island V1 is superseded route evidence. It reports
805 native DRC findings, multiple QFN/support shorts, and disconnected RX
endpoints after an incomplete full-island regeneration. No production
authority changed; the VBUS V1 parent remains selected.

The QFN-neckdown V7 is superseded route evidence. It retains focused USB3
connectivity but still creates a native USB_TXP1/JMS_AVDDL short at the
AVDDL via. This does not change electrical authority or the selected parent;
the next class is complete source-field/via allocation.

V8 is the current disposable local source-field basis. Its staggered TX
fanout preserves all focused connectivity/parity gates and introduces no
native shorting class, but native DRC remains at 730 findings with inherited
crossing/open/clearance/width debt. It is not production authority.

Native route metrics confirm V8 does not add USB TX vias or alter the CM5
paths, but its USB_TXN1/USB_TXP1 skew proxy is 4.718 mm versus 4.400 mm on
the VBUS parent. V8 therefore remains a source-escape basis, not a complete
pair-balance or Phase 24 closure.

V13 is the current disposable pair-balance basis. Its upper P-leg detour
reduces the USB TX skew proxy to 0.259 mm without a native shorting class;
focused storage audits and pad parity pass. Native DRC remains at 730
findings, so V13 is not production authority.

The fresh DRC receipt for the actual VBUS parent reports 732 findings and 400
unconnected items. All focused storage audits and pad parity pass on that
parent. This fresh baseline supersedes older parent report counts but does not
close native routing, power/ground, or full-board validation.

The V21 CM5_PERST outboard experiment is superseded evidence. It introduced
true shorts into no-net J1 pads and is not a valid low-speed repair. A native
audit confirms the existing J7.109/TP8.1/J1.E18 endpoint mapping and continuous
trunk; no storage or PCIe authority changed.

A disposable V13-plus-support trial joined the complete JMS583 support cohort
from native pad endpoints and passed its focused audit plus trace-removal
negative control. Native DRC nevertheless rose from 730 to 778 findings with
395 unconnected items, so the direct support-join route is rejected and no
production authority changed.

V14 is superseded route evidence. Its lateral TXN offset reduced the skew
proxy to 0.096 mm and preserved focused audits, but native DRC found a
0.000 mm clearance violation into U11 pad 23. No production authority changed.

V15 is superseded route evidence. Its ordinary-via/B.Cu TXN escape preserved
focused endpoint connectivity but introduced six TXP/TXN shorting findings and
raised native DRC to 746. Isolated TXN nudges are exhausted for now; the next
route class must co-author the complete lower U11 field and its adjacent
AVDDL/AVDD33/support escapes.

V16 is superseded route evidence. Its wider planar TXN dogleg removes the
pad-23 defect but leaves a 0.0925 mm native TXP/TXN clearance violation. It
retains focused endpoint connectivity but is not production authority.

V17 is superseded route evidence. Coordinated native A* regeneration of both
USB TX nets preserved endpoint connectivity and introduced no shorting class,
but native DRC rose to 781 findings with 33 crossings and 281 clearance
findings. The router implementation is rejected for this dense QFN field; a
complete hand-authored lower-field escape remains required.

V20 is superseded route evidence. Its B.Cu AVDDL branch removed the former
AVDDL/USB-TX crossing but shorted the new transition via into USB_RXP1 and
left native DRC at 736. AVDDL cannot be relocated independently; the next
field must co-author AVDD33 and USB TX/RX with it.

V18 and V19 are superseded cap-relocation experiments. V18 introduced U12
POWER_GND shorts during a direct launch (740 DRC findings); V19 retained the
U12 corridor but introduced JMS_AVDD33/TX shorts (736 findings). Neither is
production authority; moving the coupling capacitors alone does not solve the
coordinated U11/U12 field.

V10 is superseded route evidence: its local P-leg meander improves TX skew to
0.259 mm, but creates two same-layer USB TX pair self-crossings. The next
pair-balance attempt must remain layer-separated or shorten the opposite leg.

The V9 TXN micro-adjustment is superseded route evidence: focused USB3 still
passes, but native DRC rises to 731 and adds a real CM5_PET0_P/CM5_USB3_RX_N
short. V8 remains the selected disposable parent.

V11 is superseded route evidence: shortening TXN improves its skew proxy to
1.620 mm, but native DRC reports 731 findings and a CM5 USB RX pair short.
The candidate is not production authority; subsequent edits must use a
serialization-safe whole-net regeneration path.

The installed local USB3 router is superseded evidence: focused USB3 remains
passing, but native DRC reports 734 findings and a JMS_USB3_TXN/USB_RXP1
short. The router is not production authority; a source-owned corridor
regeneration remains required.

The V8 USB3 negative control independently passes: removing a required native
trace breaks the asserted endpoint graph. The check strengthens evidence
sensitivity but does not waive the open native DRC or full-board gates.

## SUPERSEDED OPEN-GATE SNAPSHOT — pre-VBUS/J8 basis

The following historical snapshot is retained for archaeology only. It is not
the current implementation instruction; current state and next action are
defined in the authority section above.

The Y10 relocation trial is rejected implementation evidence: it preserved
USB3 endpoint assertions but produced 695 native DRC violations and five true
shorts. The live clock topology remains U11/XIN-XOUT to Y10, and the next
repair must be a net-aware escape method rather than an unvalidated support
move.

The U12 HD3SS6126 QFN exposed-pad authority defect is corrected in the live
schematic source: pin/pad 43 is explicitly `POWER_GND` and is included in the
source-driven PCB map. Native export `PHASE24_U12_EP_GROUND_V6.kicadxml`
proves U12.43 membership; `PHASE24_STORAGE_NETLIST_REGENERATED_V5.kicad_pcb`
has pad parity PASS and passes the USB3, SATA, and JMS583 support audits.
Native DRC remains open at 685 violations / 403 unconnected items. The
remaining gate is routing-quality repair, beginning with the U12 source-field
USB3 escape. The V5 PCB is a disposable corrected routing basis, not closure.

The prior V2/V3 regeneration and escape-trial statements below are historical
evidence. They remain useful for rejected-route archaeology but do not describe
the current implementation state or an outstanding support-network TODO.

The V5 RX_N escape follow-ups are likewise rejected implementation trials:
moving the target via outside U12's grounded exposed pad removed that specific
authority defect, but the remaining candidate corridors interact with XOUT
and inherited USB3/SATA copper. Native USB3 endpoint assertions pass; native
DRC remains the acceptance gate. No trial copper is promoted.

The V5 all-four-net A* trial is superseded route evidence: native USB3
assertions passed, but native DRC reported 841 violations and 16 true
shorts. Its search clearance model is rejected for this dense inherited
corridor; this is not a storage schematic or U12 package-authority failure.

The live JMS583 clock authority is U11/XIN-XOUT to Y10. Native export and
source-regenerated V2 evidence confirm that Y1 is a superseded, separate
support island; it must not be joined in parallel. Clock-source cleanup is
therefore complete, while native routing remains open at the U12/source-field
and neighboring-corridor gate.

## CURRENT STATE — authoritative now (2026-09-08)

The first generic netlist-driven PCB regeneration is retained as
`PHASE24_STORAGE_NETLIST_REGENERATED_V2.kicad_pcb`, but is rejected route
evidence. Pad parity, native USB3, SATA, and JMS583 support audits pass, while
native DRC reports 700 violations / 399 unconnected items and 7 true
`shorting_items` after inherited hierarchical copper was normalized without
rerouting. The authoring path is useful, but V2 copper is not promoted.

The CM5 ground-label authority has been repaired at source. All 51 local
`POWER_GND` labels in `CORE_CM5.kicad_sch` are now native global labels, so
the saved schematic export resolves CM5 ground contacts and the board plane
to one `POWER_GND` net. Receipt `PHASE24_CORE_CM5_GLOBAL_GROUND.xml` records
154 nodes on that net and the companion ERC receipt has no hierarchy errors.
This does not promote the disposable PCB net remap: the active routed board
must still be regenerated through the source-authoritative path and then
rechecked natively.

The live schematic had a real U13 lane-ownership regression: pins 6/7 were
overridden to M.2 PCIe lane 1, leaving the shared lane-0 SATA RX contacts
unowned. The authoring map and live instance labels are corrected to
`M2_SATA_B_P_PCIE_RXN0` / `M2_SATA_B_N_PCIE_RXP0`; fresh native export and
schematic-to-PCB pad parity both pass. The SATA route author now resolves
native transformed pad coordinates rather than relying on historical U13/J3
coordinates. The corrected disposable V2 corridor passes all 12 SATA
endpoint assertions. Native DRC is still open at 734 violations / 499
unconnected items, and the candidate is not production authority.

The current integrated workbench is
`PHASE24_STORAGE_MODEAUTH_USB3_ALIGNED_SATA_SUPPORT_ZONES_V1.kicad_pcb`. It
was regenerated from the corrected embedded symbol definitions, has zero
schematic-to-PCB pad-net parity mismatches, and passes all ten USB3, all 12
SATA, and complete JMS583 support endpoint audits with negative control.
Native DRC remains open at 681 violations / 499 unconnected items. This is
active routing workbench evidence, not closure.

The first native-pad-aware integrated M.2 launch replacement was tested in
V1/V2. Although V2 lowered the aggregate DRC count, it created true socket
ground collisions and TX pair/via conflicts, so both are rejected route
implementations. The corrected source-authoritative support workbench remains
the active basis; the launch copper was not promoted.

Launch V3/V4 are retained as rejected route evidence: V3 still shorted the
U13 source-field pair, and V4 crossed adjacent U13 pads while staggering its
source vias. No launch copper was promoted; the source-authoritative support
workbench remains the active basis.

The aligned USB3 promotion now passes the complete ten-net native audit, and
the subsequent V3 SATA integration passes all 12 SATA endpoints. V3 remains
disposable because its regenerated parent lacks the earlier zone-backed
AVDDL/VCCO/VCCK support coverage. The SATA author now preserves unrelated
integrated copper and zones; board scrubbing is limited to explicitly
minimal fixtures.

The corrected support-zone promotion now passes the complete JMS583 support
audit and negative control. The final combined workbench also passes the
complete ten-net USB3 audit and all 12 SATA endpoint assertions. Native DRC
remains open at 669 violations / 499 unconnected items, so the storage island
is still in active route cleanup rather than closure.

A bounded integrated REXT repair was tested and rejected. The via escape
introduced QFN-ground/power conflicts, while the no-via perimeter escape
left the adjacent POWER_GND short in place. Neither variant was promoted;
the zone-backed integrated workbench remains the baseline for the next
selector-to-M.2 launch repair.

Mode-control ownership is now source-corrected: U12.9, U13.9, and U14.4 use
the shared `STORAGE_SEL` net; J3.69 and J5.2 use `AUTO_PEDET`. The regenerated
placement passes parity. A saved-board mode-control fixture connects those
control paths. The latest disposable V5 native fixture passes four saved-PCB
endpoint connectivity assertions with a removal negative control, but native
DRC still reports a local mode-route crossing plus inherited fixture findings;
this is not mode closure.

Status: `IN PROGRESS — support circuitry and mode-control authority are
authored; native copper, mode-aware validation, and release checks remain
open` (2026-09-06, live checkpoint).

The active implementation is the storage-local two-bridge topology:

`CM5 USB -> HD3SS6126RUAR -> {TUSB9261 SATA | JMS583-QHFA3A NVMe}
-> HD3SS3412RUAR -> TE 1-2199230-4 M-key Socket 3`.

The selected JMS583-QHFA3A is factory mask-ROM qualified for baseline use.
Optional SPI NVRAM remains DNP. Firmware is not a design dependency, but
authorized prototype supply remains a procurement risk: the retained JLC
listing currently reports zero stock and broker listings are corroborating
only.

## CURRENT STATE — authoritative now

The native root schematic export resolves the CM5 USB3 source nets directly:
`CM5_USB3_RX_N/P` are J7 128/130, U12 16/15, and U7 42/43; `CM5_USB3_TX_N/P`
are J7 140/142, U12 12/11, and U7 45/46. The placement author normalizes
donor hierarchy aliases before generating disposable PCB candidates. This
closes the aliasing ambiguity in the authoring path, not the remaining
physical USB3 routing or native DRC gates.

The current live-source audits pass for schematic/library authority,
component pad counts and maps, selector truth table (`SATA=0`, `NVMe=1`),
and the mode contract. Native copper, mode-aware switched connectivity, and
DRC closure remain open.

The current support-routing basis includes the native all-F.Cu `JMS_VCCK`
repair `PHASE24_DUAL_MODE_STORAGE_FULL7_VCCK_F_center.kicad_pcb`. Its U11.2
to C82.1 native connectivity and trace-removal negative control pass. Native
DRC is 877 violations / 499 inherited unconnected items, with no new VCCK
short or crossing relative to the AVDD33 parent. Other support rails,
mode-control, storage routing, and full-board gates remain open.

The saved support receipt and local-zone candidates cover AVDDL, VCCO,
VDDREG_5V, and LXO; REXT, crystal, reset, AVDD33, and VCCK are connected on
the current basis. The first AVDDL corridors are retained as rejected route
evidence because native DRC found shorts into existing USB3/PCIe copper. The
support primitive is not yet promoted as integrated production copper.

VCCO is promoted on `PHASE24_DUAL_MODE_STORAGE_FULL7_VCCO_rectangle_zone`
using a local F.Cu power-copper zone. Native U11.6-to-C81.1 connectivity and
the zone-removal negative control pass; native DRC is 514 findings with no
VCCO-authored short/crossing class. This does not close the remaining AVDDL,
VDDREG_5V, LXO, mode-control, or full-board gates.

VDDREG_5V is promoted on `PHASE24_DUAL_MODE_STORAGE_FULL7_VDDREG_local_zone`
as a local F.Cu power-copper zone between U11.1 and L10.2. Native zone-aware
connectivity and zone-removal negative-control checks pass; native DRC remains
514 findings with no VDDREG-authored short/crossing class.

The shared LXO path is promoted on
`PHASE24_DUAL_MODE_STORAGE_FULL7_LXO_below_vddreg.kicad_pcb`. Native
U11.64-to-L10.1 connectivity and the trace-removal negative control pass;
native DRC remains 514 findings with no LXO-authored short/crossing class.

Fresh native root ERC reports 925 violations on the current source. The older
927-count report is historical. The current report has no dangling M.2
entries; remaining findings are inherited
off-grid/same-label and other source-quality warnings. ERC remains an
independent open gate. The six isolated legacy M.2 labels were removed at the
source boundary; unrelated inherited
findings.

FULL7 saved-copper metrics are retained in
`PHASE24_DUAL_MODE_STORAGE_NC39_USB3_FULL7-metrics.txt`. They expose
source-leg length imbalance and three-via-per-pair paths; the measurements are
diagnostic only and do not close impedance, skew, or DRC requirements.

The live U12 map was also reconciled at the source-authoring boundary:
pins 24/25 use bridge-side `JMS_USB3_TXN/P` across the TX coupling capacitors,
while pins 22/23 retain direct `USB_RXN1/P` bridge links. The resulting
USB3_FULL7 disposable route passes all ten native endpoint assertions and
reduces native DRC to 827 violations / 499 inherited unconnected items.
Three inherited J1 launch shorts and local crossings remain, so this is not
closure; FULL5 and FULL6 are superseded routing evidence.

The native-pad A* source-router trial passed endpoint connectivity but is
rejected on native DRC (929 violations, 25 shorts, 6 crossings). It is not a
macro-placement conclusion; FULL7 remains active.

The U12 x=148 mm translation trial is rejected on native DRC (851
violations, 8 shorts, 15 crossings) despite 10/10 USB3 endpoint connectivity.
It is a negative placement experiment, not an architecture conclusion.

The inward source-launch relocation FULL10 was rejected after native DRC
showed new shorts into J1 12V pads and the U11 ground pad. It remains a
negative route experiment, not a placement or architecture finding.

The disposable U12 180-degree rotation trial preserves endpoint connectivity
but is rejected on native DRC (845 violations, six shorts, 19 crossings).
This is a placement-route negative result, not an electrical architecture
finding.

The saved-board USB3 negative control passes: FULL7 is connected at baseline,
and removing a required RX_N track breaks the native endpoint assertion. This
is validation-method evidence only; routing and DRC remain open.

The local USB3 router now defaults to the saved FULL7 native authority. Its
older canonical-placement default was rejected by native connectivity because
U12.24/U12.25 retained stale USB_TXN1/P ownership. No PCB-only net repair was
used. The corrected disposable `PHASE24_DUAL_MODE_STORAGE_USB3_LOCAL_FROM_FULL7`
passes all ten endpoint assertions and reports 830 DRC violations / 499
unconnected items; it is the current routing basis, not closure.
The saved-board negative control also passes on this candidate: removing a
required CM5_USB3_RX_N track breaks native endpoint connectivity.

The first composite of this USB3 basis with the existing JMS583 support
cohort is rejected. Although the support audit and negative control pass,
native DRC reports 870 violations / 499 unconnected items and identifies new
support-placement conflicts in the USB3 field, including a JMS_USB3_TXN to
USB_RXP1 short. The support cohort remains a reusable primitive, not an
integrated route; the next pass must allocate its placement and escapes
against the USB3 geometry together.

The north-side support co-author is likewise rejected: support endpoint and
negative-control audits pass, but native DRC reports 924 violations / 499
unconnected items and new local support-to-USB, crystal/rail, and return-via
conflicts. This is preserved as placement/route evidence; the next support
pass must use obstacle-aware native-pad allocation across the complete local
field.

The native-pad A* support allocator is rejected as a routing implementation:
retaining all non-current endpoint pads caused the dense QFN to require a
bounded terminal escape, but the resulting 2 mm halo admitted paths through
neighboring QFN fields. Native DRC reports 1,013 violations and multiple real
shorts. The candidate and report are preserved; the next implementation must
encode legal per-pad escape corridors rather than a broad halo.

The verified JMS583 support primitive was transplanted onto the unmodified
FULL7 USB3 basis and rejected as an integrated route. Native support audits
pass, but DRC reports 917 violations including a real XAVDDH-to-CM5_USB3_TX_N
collision and local XIN/XOUT via-clearance. The primitive remains valid
isolated evidence; the next pass must regenerate its QFN exits in-place around
the USB3 copper.

The focused three-exit transplant passes native XIN/XOUT/XAVDDH connectivity
and its XIN negative control, but native DRC rejects the integrated route at
851 violations / 499 unconnected items because the XAVDDH departure collides
with CM5_USB3_TX_N. The candidate is preserved as rejected evidence; the
remaining work is an in-place XAVDDH escape repair.

The left/up in-place XAVDDH repair is now the current support/USB3 integration
basis. Its native XIN/XOUT/XAVDDH audit and XIN-removal negative control pass;
the USB3 endpoint audit remains 10/10. Native DRC reports 853 violations /
499 unconnected inherited items with no authored shorting or track-crossing
class. It is a routing basis, not full Phase 24 closure.

The current basis now includes the native-pad-aware JMS_RESET_N repair after
REXT. U11.15-to-R81.1-to-C85.1 connectivity and its trace-removal negative
control pass; REXT, XIN/XOUT/XAVDDH, and USB3 remain passing. Native DRC is
863 violations / 499 inherited unconnected items with no authored shorts or
crossings. Remaining support rails and full storage validation are open.

The current basis also includes the validated lateral REXT route. Native REXT
and XIN/XOUT/XAVDDH audits pass with their trace-removal controls, and the
USB3 endpoint audit remains 10/10. Native DRC is 853 violations / 499
inherited unconnected items with no authored shorts or crossings. This is
still only a support/USB3 routing primitive, not full storage or Phase 24
closure.

The current basis includes the upper native-pad-aware JMS_AVDD33 repair after
REXT and RESET_N. U11.19-to-C80.1 connectivity and its trace-removal negative
control pass; all prior USB3 and three-exit checks remain passing. Native DRC
is 876 violations / 499 inherited unconnected items with no authored shorts or
crossings. Remaining support rails and full storage validation are open.

The FULL11 TX layer-transition experiment is rejected after native DRC rose
to 845 with additional local clearance/crossing findings. It remains route
evidence only; FULL7 is still the active basis.

The alternate source-layer trial passed 10/10 USB3 endpoints but is rejected
on native DRC (851 violations, 4 shorts, 18 crossings). The source escape is
restored to the all-B.Cu FULL7 basis.

The U11 180-degree rotation trial is rejected on native DRC (843 violations,
7 shorts, 21 crossings) despite 10/10 endpoint connectivity. It remains
negative placement evidence, not an architecture conclusion.

The FULL14 TX source-launch relocation is rejected on native DRC (832
violations, 5 shorts, 19 crossings) despite 10/10 endpoint connectivity.
The generator is restored to the FULL7 launch columns.

The FULL12/FULL13 TX dogbone trials are rejected route evidence: they did not
produce a clean pad-field escape and introduced local shorts. The authoring
path is restored to the FULL7 geometry.

- The support-symbol authoring path emits canonical JMS583 support nets using
  the native KiCad label ordering. The endpoint-overlap repair removed stale
  generated label atoms at U11 pin 12/pin 39, and the shared-selector maps no
  longer assign `JMS_GPIO7_NC` to pin 39. The regenerated
  `PHASE24_DUAL_MODE_STORAGE_PLACEMENT_NC39.kicad_pcb` passes the native
  schematic-to-PCB pad-net parity audit with zero expected-pad mismatches.
  Earlier duplicate-label deletion/reauthor probes remain rejected historical
  evidence; they are not current requirements. Native routing and DRC remain
  open.

- `STORAGE.kicad_sch` contains the existing TUSB9261 SATA branch, JMS583
  NVMe branch, both TI selectors, the TE M-key socket, the JMS583 support
  network, and J5/U14 mode control. The schematic and mode-contract audits
  pass; native ERC is still open.
- The generated libraries contain a structurally audited 64-pad JMS583 QFN
  package identity, TI RUA0042A selector packages, and the 67-contact TE
  M-key candidate. Selector/contact-count audits pass; final JMS583
  land-pattern pad, paste, mask, courtyard, and exposed-pad authority remains
  open as documented in `PHASE24_JMS583_LAND_PATTERN_RECONCILIATION.md`.
- The corrected NC39 source/placement candidate passes native schematic-to-PCB
  pad-net parity with zero expected-pad mismatches. Its direct support replay,
  `PHASE24_DUAL_MODE_STORAGE_NC39_SUPPORT_TRIAL.kicad_pcb`, is rejected route
  evidence: native DRC reports 836 violations / 499 unconnected items,
  including a real `JMS_REXT`-to-`JMS_AVDDL` short and authored crossings.
  The next support implementation must use native-pad-aware per-net escape
  allocation.
- A coherent native-pad-aware support cohort was then generated as
  `PHASE24_DUAL_MODE_STORAGE_NC39_SUPPORT_COHORT.kicad_pcb`. Its eight-net
  connectivity audit and trace-removal negative control pass. Native DRC
  reports 820 violations / 499 unconnected items, with zero authored shorts;
  the seven crossings are inherited CM5 donor USB escape findings. Retain it
  as the current support-routing primitive while the complete storage island
  remains open.
- The co-located-crystal follow-up
  `PHASE24_DUAL_MODE_STORAGE_NC39_LOCAL_CRYSTAL.kicad_pcb` is rejected: native
  DRC reports 850 violations / 499 unconnected items and real XIN/XOUT shorts
  into the support field. The crystal field still needs obstacle-aware
  allocation; no rule relaxation or production promotion occurred.
- The V3 QFN escape repair,
  `PHASE24_DUAL_MODE_STORAGE_NC39_QFN_ESCAPE_REPAIR_V3.kicad_pcb`, completes
  REXT, XIN, and XOUT with ordinary through-via corridors. The complete
  support audit and trace-removal negative control pass for all ten support
  endpoint pairs. Native DRC reports 852 violations / 499 unconnected items;
  no storage-local short/crossing is present, while seven crossings are
  inherited CM5 donor USB geometry. This remains a support-field primitive,
  not full storage closure.
- The current regenerated disposable placement candidate is
  `PHASE24_DUAL_MODE_STORAGE_PLACEMENT_CURRENT.kicad_pcb`; it is not
  production authority. The current fresh native result is recorded in
  `PHASE24_DUAL_MODE_STORAGE_PLACEMENT_CURRENT_FIXED_GRID-drc.rpt` as 857
  DRC violations and 499 unconnected items. The V3 disposable relocation
  (`phase24_storage_candidate_v3.rpt`) is rejected evidence, not the current
  candidate. The older
  `PHASE24_DUAL_MODE_STORAGE_PLACEMENT.kicad_pcb` remains historical evidence.
  The latest corrected-package USB3 fixture is
  `PHASE24_DUAL_MODE_STORAGE_USB3_ISOLATED.kicad_pcb`, with native report
  `PHASE24_DUAL_MODE_STORAGE_USB3_ISOLATED40-drc.rpt`: zero authored shorts,
  track-width findings, and track-crossing findings; 152 clearance, 4
  board-edge, and 7 solder-mask findings remain, plus partial-fixture
  unconnected items. It is not yet a route or release pass.
- `phase24_dual_mode_storage_usb3_native_connectivity_audit.py` passes all ten
  intended CM5/U12/U11/coupling-capacitor endpoint pairs on the regenerated
  candidate. This proves native endpoint connectivity only; it does not waive
  the physical DRC findings above.
  The accepted disposable placement basis is the U11-west/J5-clear result:
  native DRC has zero shorting items, but eight crossings and 499 unconnected
  items remain. The dual-mode island remains open integration work; no
  placement experiment has been promoted to production authority.
  The placement generator now reuses the reviewed JMS583 pin map and places
  generated support parts inside the acreage outline; this corrects an
  authoring defect but does not close routing. The first current-candidate
  support-routing trial is retained as rejected evidence: five native shorts
  and seven crossings resulted from stale distributed support placement. A
  subsequent local-anchor trial is also rejected below; the next support pass
  is per-net native-pad escape allocation.
  The subsequent local-anchor trial is also rejected evidence: it reports one
  reset short and six crossings, showing that co-location alone is insufficient
  and that each support net needs a native-pad-aware escape corridor.
  The isolated reset discriminator independently rejects a direct F.Cu join
  because it enters the USB coupling field at 0.0379 mm clearance; the next
  route must allocate a layer-transition corridor deliberately.
- The live native XML export used for the corrected disposable candidate is
  `PHASE24_STORAGE_NATIVE_FINAL.xml`; its schematic-to-PCB pad audit passes
  with zero expected-pad mismatches. The older five-mismatch and two-mismatch
  reports are superseded association evidence, not current open gates. The
  The earlier corrected candidate result (797 violations / 499 unconnected
  items) is superseded. The current regenerated placement result is 857
  violations / 499 unconnected items; those physical findings remain open.

## CURRENT OPEN GATES

The J7 ground-return-via probe is rejected: its 51 vias used flattened
`POWER_GND` on pads owned by `/CORE_CM5/POWER_GND`, so it did not provide a
valid native plane connection and introduced additional DRC findings. No
PCB-only ground-net merge was made.

The endpoint-safe layer-aware SATA search with selector-side copper retained
passes all 12 native SATA endpoint assertions, but leaves a U7 source-field
crossing and reports 676 native DRC violations / 499 unconnected items,
including one inherited non-storage short. It is rejected as a full-board
candidate; its safe-exit routing method is retained.

The coherent storage-island transplant
`PHASE24_STORAGE_COHERENT_ISLAND_V1.kicad_pcb` is rejected stale route
evidence. After correcting its capacitor-side net assumptions, native SATA
still failed at `TUSB_SATA_RXP` due to the historical U13 socket template;
native DRC reported 802 violations / 499 unconnected items.

The reordered SATA source-field probe
`PHASE24_STORAGE_SATA_SOURCE_ORDER_V1.kicad_pcb` is rejected route
implementation evidence: its corrected native-net authoring passes all 12
SATA endpoint assertions but introduces real same-field shorts/clearances
(612 DRC violations / 499 unconnected items). The raw fixture and report are
preserved; the active no-short basis remains
`PHASE24_STORAGE_VCCK_LOCAL_V1.kicad_pcb`.

The layer-aware native-pad A* trial
`PHASE24_STORAGE_SATA_ASTAR_V1.kicad_pcb` is rejected route implementation
evidence. It passes all 12 SATA endpoint assertions, but native DRC reports
822 violations including real SATA-to-power/support shorts and crossings.
The corrected pad-layer obstacle model and raw artifacts are preserved; no
A* copper was promoted.

The post-escape SATA corridor trial
`PHASE24_STORAGE_SATA_POST_ESCAPE_V1.kicad_pcb` passes all 12 native SATA
endpoint assertions and lowers the aggregate DRC count to 583, but introduces
three real shorts, including TUSB SATA copper into the JMS_REXT/USB3 field.
It is rejected route evidence and does not replace the active no-short basis.

The minimal TXN-via-spacing trial
`PHASE24_STORAGE_SATA_TXN_VIA_SPACING_V1.kicad_pcb` passes all 12 SATA
endpoint assertions and lowers DRC to 575, but creates a real TXP/TXN short
at the U7 escape. It is rejected; further tiny source-via nudges are not the
next solution class.

1. SUPERSEDED SNAPSHOT: the former `PHASE24_STORAGE_VCCK_LOCAL_V1.kicad_pcb`
   candidate combined an earlier CM5 USB3 launch with selector-side SATA and
   destination-only VCCO work. Its focused audits were useful, but its 669
   finding / 499 unconnected-item DRC result predates the VBUS/J8 correction
   and it is not the current integrated parent.
2. The storage-local JMS583 support, USB3, SATA, and mode-control endpoint
   audits remain current evidence only when run against the saved board named
   in CURRENT STATE. The older VCCK/V6/V3/V4 route snapshots are disposable
   historical evidence, not current implementation instructions.
3. Complete native ERC/DRC, mode-aware connectivity and inactive-state checks
   for forced SATA, forced NVMe, AUTO, empty socket, reset, and power-off
   states.
3. Finish TE M-key pad-by-pad, courtyard, mask/paste, mechanical, and model
   parity against the retained manufacturer material.
4. Reconcile the NVMe 3.3-V transient/inrush budget and document the current
   JMS583 prototype sourcing risk. No purchase or firmware binary is assumed.
5. Integrate only after the complete storage island passes; then resume the
   preserved whole-board Phase 24 closure work.

The following implementation history is retained below for archaeology. Its
older TODO wording is superseded by the current-state and open-gate sections
above; raw reports and rejected experiments remain evidence.

## Land-pattern artifacts

`phase24_generate_dual_mode_storage_libraries.py` emits native
footprints from retained authorities:

- `JMS583_QFN64_8x8.kicad_mod`: QFN64, 0.4-mm pitch, 8-mm body, 64 pads.
- `HD3SS6126_RUA0042A.kicad_mod` and `HD3SS3412_RUA0042A.kicad_mod`: TI
  RUA0042A, 42 pads plus exposed pad 43. Separate names preserve distinct
  pin ownership despite the common package drawing.
- `TE_1-2199230-4_MKEY.kicad_mod`: 67 contacts with the TP-053 M-key gap.

The generated files are review candidates until native pad-by-pad comparison
against the TE DXF/application drawing and TI/JMicron package pages is signed
off. The library audit is intentionally structural; it does not assert PCB
connectivity.

## SUPERSEDED HISTORICAL SNAPSHOT — pre-label-fix evidence

`STORAGE.kicad_sch` now contains U7 plus native U8 JMS583, U9 HD3SS6126,
U10 HD3SS3412, and J3 TE 1-2199230-4. The B-key J3 is removed. The saved
sheet parses under KiCad 10.0.5, and `phase24_dual_mode_storage_schematic_audit.py`
passes; its negative-control copy fails when a required M-key label is removed.
The pre-label-fix native ERC reported 205 violations, so that snapshot was
not an ERC pass. The report is retained as immutable historical evidence and
includes inherited abstract-sheet issues, off-grid generated symbol
endpoints, and isolated labels that were subsequently removed or superseded.
It must not be used as the current ERC count; the current post-fix report is
`PHASE24_DUAL_MODE_STORAGE_ERC_AFTER_LABEL_FIX.rpt` with 927 violations and
no dangling M.2 entries.

`PHASE24_DUAL_MODE_STORAGE_PLACEMENT.kicad_pcb` is a disposable native
placement candidate derived from the selected storage macro ancestor. It
contains the M-key J3 and U11/U12/U13 footprints with physical pad nets. KiCad
10.0.5 loads it and reports 1,013 violations / 482 unconnected items; this is
expected evidence that the candidate is not routed or promoted. Existing U8/U9
references on the ancestor were preserved, so the new storage silicon uses
U11/U12/U13 consistently.

## SUPERSEDED HISTORICAL SNAPSHOT — not current instructions

The next section records the earlier pre-integration snapshot. It is retained
to explain prior checkpoints and must not be read as a current TODO list.

## SUPERSEDED historical implementation gates at that snapshot

The checklist below describes work that was outstanding at the earlier
pre-integration snapshot. It is archaeological context only. It is not a
current TODO list; the authoritative current state and open gates above take
precedence.

1. Native symbols were added and checked against the retained TI tables,
   JMS583 evidence, and TP-053 socket table.
2. The old B-key J3 was replaced in authoritative `STORAGE.kicad_sch` by the
   TE M-key candidate; this was not a PCB-only connector patch.
3. The two selector truth tables and latched AUTO/FORCE SATA/FORCE NVMe
   control circuit were authored. Their mode-contract audit passes; the
   state and release checks remain open as recorded above.
4. The JMS583 support network was instantiated, including rails, 25-MHz
   crystal, REXT, reset, VBUS detect, USB/PCIe AC coupling, internal-regulator
   inductor, and optional DNP SPI NVRAM. Its support-network audit passes;
   physical routing and release validation remain open.
5. The storage 3.3-V budget was identified as an open release check for
   NVMe inrush/transient and both bridges; it has not been silently declared
   closed.
6. Disposable native fixtures were built and partially validated. Complete
   forced SATA, forced NVMe, AUTO, empty, reset, and inactive-state closure
   remains open as stated in CURRENT OPEN GATES.

No production PCB change is claimed by the footprint generation alone.

## USB3 fixture discriminator — 2026-09-06

`phase24_usb3_dual_mode_isolated_fixture.py` created a disposable native
fixture containing only J7, U12, U11, and the two JMS583 TX coupling
capacitors. The fixture uses saved pad coordinates and native copper; it does
not inject graph edges. It was rejected as a route implementation, not as an
architecture decision: the first attempt drove straight into the dense U12
QFN pad field, producing six track crossings and twenty shorting findings in
native DRC. The remaining findings include inherited package mask/clearance
and unconnected pads because this is a deliberately partial fixture.

The next implementation must use package-side dogbones and layer-separated
escapes outside the U12 pad field, then reconnect the four USB2 pins from an
explicit CM5 port-0 source. The current CORE_CM5 sheet exposes `CM5_USB3`
and SERVICE USB2 but does not yet expose CM5 port-0 USB2 `USB3-0-D_P/N` as
hierarchical storage nets. That is an authority/interface omission to repair
before production regeneration; `CM5_USB2_DP/DM` must not be invented as a
replacement without tying them to the actual CM5 port-0 pads.

## CM5 USB2 source correction — 2026-09-06

The omission was repaired in the schematic authoring path. CM5 carrier pads
134/136 (`USB3-0-D_P/N`, the USB2 companion of port 0) now export explicit
`CM5_STORAGE_USB2_DP/DM` global nets from `CORE_CM5`; the storage selector
uses those same nets. Native root netlist export now shows J7.134 to U12.8
and J7.136 to U12.7 on the same nets. U12-to-JMS583 USB3 names were also
normalized to `USB_TXP1/TXN1` and `USB_RXP1/RXN1`. The prior isolated PCB
fixture predates this source correction and remains rejected evidence.

The follow-on isolated fixture was regenerated with the corrected source and
package-side dogbone intent. It is still rejected as implementation evidence:
the U12 pad-field direct shorts were removed, but the current B.Cu lane order
crosses at the staggered through-via escapes. Native DRC reports 11 crossing
findings and 22 shorting findings in the current route, plus expected partial
fixture/unconnected/package-rule findings. The next bounded repair is to make
the B.Cu corridor ordering match the staggered escape ordering; no component
or architecture change is indicated.

The fifth isolated routing iteration corrected the B.Cu destination ordering
and reduced native DRC shorting findings to 17. Remaining crossings are
localized to the CM5 source fanout, the final U12 dogbones, and the separate
U11 selector-side pair fanouts. These are still route implementation defects;
the next experiment will partition those corridors by permitted copper layer.

## TI RUA0042A footprint correction — 2026-09-06

The retained TI package drawing identifies RUA0042A as 9.0 x 3.5 mm with a
17/4/17/4 perimeter. The previous generated footprint was a square,
10/10/10/10 construction and placed pads 11 and 21 at the same coordinate.
The generator now emits the documented perimeter, and the selector geometry
audit passes for both selectors. The placement candidate was regenerated from
that corrected library.

The latest isolated native USB3 fixture uses the corrected pad positions and
orthogonal package-side dogbones. Native DRC reports zero shorting findings;
seven track crossings remain in the final dogbones/selector continuation and
are not accepted as a routing pass.

The TI example board layout also specifies 0.60 mm perimeter-pad length;
the generator now uses 0.60 x 0.25 mm pads for both selectors. The geometry
audit still passes after this correction and the isolated native fixture
remains zero-short. Track-width findings in the fixture are retained and
must be resolved against the approved JLC routing rule before promotion.

The sixth iteration split RX/TX source fanout layers, but native DRC showed
the B.Cu source trunk now colliding with the selector-side U11/U12
continuation. It is rejected as a shared-corridor route implementation; the
next fixture must reserve separate local corridors for source escape and
selector continuation.

The seventh/eighth escape trial uses actual CM5 pad-order monotonic routing
and outward-Y U12 dogbones. It removes the prior source-field crossing class,
but native DRC still finds via-to-neighbor clearance at the dense package
edge and inherited selector-continuation crossings. It is rejected as a
fixture route implementation. The next bounded repair moves the vias farther
outside the package and gives selector continuation a separate corridor.

The subsequent orthogonal SMD-pad-escape experiment is retained as
`PHASE24_DUAL_MODE_STORAGE_USB3_ISOLATED17-drc.rpt` and rejected. It used
native pad/via/track objects, but introduced real collisions between the
selector continuation, CM5 source fanout, and cap-side return corridors.
That result is a route implementation failure, not evidence against the
dual-mode architecture or the corrected TI package. The committed generator
remains at the preceding zero-short baseline; no production PCB was promoted.

The local-cap/F.Cu corridor experiments are retained as
`PHASE24_DUAL_MODE_STORAGE_USB3_ISOLATED18-drc.rpt` and
`PHASE24_DUAL_MODE_STORAGE_USB3_ISOLATED19-drc.rpt`. Moving C86/C87 locally
reduced the artificial detour, but the F.Cu selector paths still intersected
native CM5-source escape vias and package-edge corridors. They are rejected
as a route implementation class. The saved generator remains the committed
zero-short baseline pending a proper two-layer via-handoff construction.

The explicit via-handoff trial is retained as
`PHASE24_DUAL_MODE_STORAGE_USB3_ISOLATED21-drc.rpt` and rejected. Native DRC
found shorts between handoff vias and the inherited CM5 source corridor, plus
crossing split-cap paths. The experiment confirms that handoff vias must be
planned with a reserved corridor; inserting them into existing copper is not
a valid repair. The generator was restored to the committed zero-short
baseline.

The JMS583 package audit then exposed that the prior generator had silently
emitted only 42 pads for the 64-pin device. The generator was corrected to
emit a 16/16/16/16 QFN64 perimeter, and the placement candidate was
regenerated. Structural audits now pass against the corrected native U11
package. USB3 isolated report
`PHASE24_DUAL_MODE_STORAGE_USB3_ISOLATED24-drc.rpt` is retained from the
first route against that corrected geometry: it reports no selector/source
shorting items and five localized track crossings. It is not a route pass,
but it supersedes results obtained with the malformed 42-pad footprint.

The follow-on QFN64 package-aware escape moved RXP perpendicular to the
bottom pad row and retained RXN on the reserved lower B.Cu lane. The later
source-via alignment in report
`PHASE24_DUAL_MODE_STORAGE_USB3_ISOLATED40-drc.rpt` records zero authored
shorting, track-width, and track-crossing findings after partitioning the
CM5-source TX pair onto F.Cu and the RX pair onto B.Cu and ordering the local
bridge vias monotonically. Native clearance, board-edge, solder-mask, and
intentional support-pad unconnected findings remain; it is not yet a complete
storage pass.
## Current parity audit correction — 2026-09-08

The schematic-to-PCB pad audit now normalizes only hierarchical XML net names
such as `/STORAGE/NET` to the PCB's flattened `NET` representation. This
removes representational false positives without adding connectivity. Its
older 64-mismatch result is superseded by the live U12 label correction below;
it remains historical evidence and is not a current requirement.

The complete ten-net JMS583 support connectivity audit passes on the AVDDL
local-zone basis, including the combined track/zone-removal negative control.
Support connectivity is a validated primitive; USB3/SATA/mode/DRC/ERC and
full-board gates remain open.

The current support-route candidate was independently compared against the
native schematic export and reports 111 expected-pad mismatches. It remains a
disposable routing candidate until schematic-to-PCB authority is regenerated
and the parity gate passes; no PCB-only ownership repair is accepted.

## Current live source/parity correction — 2026-09-08

`STORAGE.kicad_sch` now has authoritative `JMS_USB3_TXN/P` instance labels on
U12.24/U12.25, matching the reviewed source map and C86/C87 bridge-side nets.
Fresh native export plus regenerated
`PHASE24_DUAL_MODE_STORAGE_PLACEMENT_CURRENT.kicad_pcb` reports zero
expected-pad mismatches and a passing dual-mode mode contract. The prior
64/111 mismatch reports are superseded historical probes. This closes source
pad-net parity for the regenerated placement candidate only; copper routing,
ERC, DRC, and full Phase 24 remain open.

## Current VBUS/RX_N launch discriminator — V3 rejected (2026-09-08)

`PHASE24_DUAL_MODE_STORAGE_FULL7_VBUS_RXN_REPAIR_V3` passes native VBUS
connectivity with a trace-removal negative control, the complete ten-net
JMS583 support audit, and all ten USB3 endpoint assertions. It removes the
earlier RX_N-to-J1 short, but native DRC still reports 509 findings / 499
inherited unconnected items and an RX_N/refclk crossing. This is rejected as
route-implementation evidence only; no production authority or Path-B
artifact changed.

V4 is also rejected: it passes VBUS and USB3 endpoint connectivity, but
native DRC reports 512 findings / 499 inherited unconnected items with real
RX_N/TX_N shorting/crossing classes. It remains negative route evidence and
does not change the selected support basis.

The VBUS audit now requires the complete U11.10 sense endpoint as well as
U11.16, R82, and R83. V10 passes all three native endpoint assertions and the
trace-removal negative control, but native DRC reports 532 findings with a
real VBUS/JMS_VBUS_SENSE handoff short. VBUS remains open; no route has been
promoted.

V14 is the cleanest complete-endpoint VBUS trial so far: the strengthened
audit passes U11.16, U11.10, R82, and R83 with its trace-removal negative
control, and no DRC shorting class involves VBUS or JMS_VBUS_SENSE. It still
adds QFN/zone clearance findings and 24 crossing classes overall, so it is
retained evidence rather than a promoted route.
# Current implementation checkpoint — 2026-09-08

The active disposable routing basis is `PHASE24_STORAGE_U12_EP_RX_PAIR_V6`.
It keeps source-authoritative U11/Y10 XIN/XOUT unchanged and moves the U12
USB3 RX transitions outside the HD3SS6126 exposed pad using ordinary
through-vias. Native endpoint, SATA, JMS583-support, and pad-parity audits
pass; native DRC is still open at 684 violations / 403 unconnected items,
with no native shorting class. Mode-control connectivity remains open at the
inherited J3.69-to-J5.2 route and is the next focused repair. V6 is not a
production closure candidate yet.
