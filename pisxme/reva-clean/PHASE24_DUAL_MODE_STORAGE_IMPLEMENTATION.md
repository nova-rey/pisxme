# Phase 24 dual-mode storage implementation

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

Fresh native ERC reports 927 violations on the current source. The post-fix
report has no dangling M.2 entries; remaining findings are inherited
off-grid/same-label and other source-quality warnings. ERC remains an
independent open gate. The six isolated legacy M.2 labels were removed at the
source boundary, while the total remains 927 due to unrelated inherited
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

1. Finish the native USB3/source and selector copper, then complete the
   remaining SATA/PCIe, USB2, support, return, and power routing without
   synthetic connectivity edges.
2. Complete native ERC/DRC, mode-aware connectivity and inactive-state checks
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
removes representational false positives without adding connectivity. The
current placement candidate still fails with 64 actionable mismatches,
including missing R24/R32/R33 support pads, incorrect J3.69 PEDET ownership,
selector pin-map mismatches, and missing/incorrect M.2 no-connect and power
contacts. This remains an open source-authority/parity gate.
