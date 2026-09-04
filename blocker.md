# PiSXMe Rev A Clean — Blocker Report

## Final state

`PISXME_REVA_CLEAN_RECOVERABLE_PHASE17`

## Earliest failed gate

Phase 17 — Ethernet routing.

Phases 0–16 are not the current blocker. Phase 3 schematic/library authority
is closed, and Phase 16 PCIe routing is closed with its documented bounded
Rev-A empirical risk.

## Blocking condition

The Phase 11/12 placement is frozen with the CM5 Ethernet source at J7 near
the left side and the Ethernet ESD and MagJack at the right edge, separated by
the V100 cooler reservation and existing regulator, power, PCIe, and connector
keepout geometry.

Under the approved six-layer contract—F.Cu primary signals, In1/In4 solid
ground, In2/In3 power, B.Cu secondary signals, ordinary through-vias, and no
ordinary signals on plane layers—the frozen placement does not admit a short,
monotonic, no-maze Ethernet route.

## Evidence

- Latest native KiCad DRC candidate: `pisxme/reva-clean/CM5IO_J7_CM5IO_BOUNDARY_FIXTURE-swap5-drc.rpt`
- Latest disposable bridge report: 247 total violations, including 4
  track crossings, 78 unconnected items, 16 dangling tracks, and 2 dangling
  vias. This is the current remote-island permutation trial; it does not
  replace the independent official-fixture or J7-launch evidence.
- Representative Ethernet failures include CM5 pair crossings at J7,
  pair shorts near U6/U9, crossings against existing power/regulator tracks,
  NPTH hole-clearance violations at J7/F2/J2, and ESD pad-field clearance
  violations.
- Tested variants included perimeter routing, separated B.Cu corridors,
  via-in-pad transitions, and compact ESD placements. None passed the Phase 17
gate.

## Layer-separated 180-degree launch refinement — 2026-09-03

The isolated 180-degree fixture was refined using measured failure data.
TD2/TD0 and the right-side source groups were moved to B.Cu through ordinary
through-vias; via centers were increased to approximately 0.8 mm separation
where the previous trial had 0.5 mm clearance failures. No plane-layer
signals or via-in-pad transitions were used.

Native KiCad DRC improved from 192 to **163 violations**, with **3
unconnected items**, but still rejects the fixture. Remaining failures
include B.Cu tracks crossing other MDI routes, J2 through-hole/route
collisions, and residual J7/ESD transition clearances. This is a bounded
refinement, not Phase 17 closure. The updated fixture and report remain at
`CM5IO_ROT180_WEST_FIXTURE.kicad_pcb` and
`CM5IO_ROT180_LAYER_SPLIT_FIXTURE-drc.rpt`.
- No rejected candidate was accepted as production routing.

## Authority status

Closed:

- Native Ethernet hierarchy and eight MDI-pair connectivity.
- EDAC `A70-112-331N126` manufacturer pad mapping.
- Complete logical-pin to physical-pad aliases for all 18 MagJack contacts.
- Native PCB mapping regression.
- CM5/J7, ESD, and MagJack net authority.

Relevant commits:

- `490ae22` — EDAC physical pad alias correction.
- `ce62f86` — Phase 17 routing rejection and blocker record.

## Impact

Phase 17 cannot close. Phase 18 USB3, Phase 19 SATA, final acreage freeze, and
external-review-ready status must not begin or be claimed.

No accepted routed design was pushed, fabricated, ordered, or published.

## Best practical resolution

Reopen the Phase 11/12 placement decision and create a compact CM5-adjacent
Ethernet island containing J7 breakout, ESD protection, EDAC MagJack, and local
shield/return and center-tap circuitry. Then regenerate and revalidate affected
downstream phases before retrying Phase 17.

Routing Ethernet on power/ground plane layers or accepting the current maze
would violate the approved plan and is rejected.

## Current exact-EDAC CM5IO transplant result — 2026-09-03

The official Raspberry Pi CM5IO MDI graph was regenerated against the exact
PiSXMe EDAC authority. J2 pads 11..14 now carry distinct `ETH_CT1` through
`ETH_CT4`; pads 4 and 5 remain NC. The PCB mapping regression passes:

`phase17 Ethernet PCB pin mapping: PASS; ESD/MagJack pin authority preserved`

The prior common-center-tap construction was rejected as an invented net
collapse. A disposable individually-routed J9 experiment connected all four
tap nets, but native DRC rejected that support geometry because its routes
collided with the EDAC through-hole launch field and shield return. It is not
promoted and is preserved as negative evidence in
`pisxme/reva-clean/CM5IO_DIRECT_J7_ETHERNET_FIXTURE-exactct-individual-drc.rpt`.

The valid focused MDI fixture is regenerated with support omitted solely to
isolate the proven signal path. Native KiCad 10.0.5 DRC reports no MDI track
crossings or shorts; the four remaining unconnected items are deliberately
omitted ESD ground/shield support connections. This is a subgate, not Phase
17 closure. The direct official MDI transplant remains the selected topology;
exact clean center-tap/support integration is the current recoverable blocker.

The CM5IO reference design closes the MDI routing architecture, but cannot by
itself close PiSXMe's EDAC support mapping: the clean Ethernet schematic
exposes four distinct CT nets and does not contain the CM5IO common CT
capacitor/header network. The next bounded continuation is to derive a real
four-net support implementation from the clean schematic and EDAC authority,
or document the required schematic support addition before acreage promotion.
No Phase 18+ work has started.

### Best exact EDAC RC corridor — 2026-09-03

The B.Cu-local branch fixture was refined with an off-pad CT2 transition and
an isolated shield transition. Native KiCad 10.0.5 DRC now reports **244
findings, 0 unconnected items, and 0 shorts**, with exactly **1 remaining
support-track crossing**. The PCB pin-mapping regression still passes.

The remaining crossing is between the CT2 final approach and the CT1 branch
escape; it is localized and has not involved the official F.Cu MDI graph. The
candidate is not promoted until that crossing is removed and the complete
fixture/acreage checks pass.

### Best B.Cu-local EDAC RC island — 2026-09-03

The branch footprints were flipped onto B.Cu, keeping the four authoritative
RC branches and the shield return on the support side opposite the official
F.Cu MDI graph. Pair-specific source detours were added for CT4 and CT2, and
the shield path was isolated with an ordinary transition.

Native KiCad 10.0.5 DRC now reports **238 findings, 0 unconnected items, and
0 shorts**. Four localized support-track crossings remain, so this is not a
Phase 17 pass. A subsequent single-CT layer swap regressed to 251 findings
with many MDI/support crossings and was rejected. The best candidate is
preserved in `CM5IO_DIRECT_J7_ETHERNET_FIXTURE-edac-rc-bcu-best4-drc.rpt`.

### EDAC manufacturer RC termination authority — 2026-09-03

The EDAC A70-series electrical drawing resolves the previously missing CT
support authority. `VC1 P11` through `VC4 P14` each feed an independent
`22 nF / 100 V` series capacitor and `75 ohm` resistor into a common
termination node; that node returns to shield through `1 nF / 2 kV`. The
clean design must preserve the four CT nets through their individual branches.
This supersedes both the common-net and zero-ohm experiments.

The first disposable fixture using this exact RC network was rejected by
native KiCad DRC (**262 findings / 8 unconnected items**, with CT branch
shorts and crossings). The MDI graph was not changed and no production file
was modified. The remaining blocker is the physical branch escape, not the
electrical authority.

### Explicit four-net net-tie experiment — 2026-09-03

The next bounded experiment modeled four ordinary 0402 zero-ohm/net-ties
(`RCT1..RCT4`) from `ETH_CT1..4` into a local common CT node, with a 0603
100 nF shunt to `ETH_GND`. Source-side transitions were kept off the SMT
lands and used only ordinary through-vias on the permitted signal layers.

Native KiCad 10.0.5 DRC rejected the disposable fixture at **312 findings / 22
unconnected items**, including support-net shorts and crossings at the EDAC
launch field and dangling dogbones. This candidate is rejected. It confirms
that the missing piece is not solved by adding an unverified net-tie row; a
schematic-authoritative support topology and a physically legal local escape
are still required. No production PCB or schematic was modified.

### Follow-up support escape trial

A second exact-EDAC support escape used separate `ETH_CT1..4` routes on the
permitted F.Cu/B.Cu signal layers and connected all four disposable J9 pads.
Native DRC found **0 unconnected items**, but rejected the geometry with
support-net shorts/crossings at the EDAC shield/MDI launch field. This confirms
that simply splitting the routes across the two signal layers is insufficient;
the next experiment must use local off-pad transitions and/or a support
topology that is explicitly represented by the clean schematic. The result is
preserved in
`CM5IO_DIRECT_J7_ETHERNET_FIXTURE-exactct-individual-drc.rpt`.

## 2026-09-03 placement-repair sprint evidence

The authorized Phase 11/12 Ethernet-only reopening was attempted with nine
compact CM5-adjacent candidates plus a complete west-edge island trial. The
most promising topology placed U9 at (25,100), U6 at (29,106), and the EDAC
MagJack at (12,119), with U9 and U6 rotated 180 degrees so the CM5 source
ordering is monotonic at each ESD package. The complete trial is preserved as
`pisxme/reva-clean/ACREAGE_ETHERNET_TRIAL_ORDERED_WEST.kicad_pcb` and its
native report as
`pisxme/reva-clean/ACREAGE_ETHERNET_TRIAL_ORDERED_WEST-drc.rpt`.

That candidate still has true Ethernet failures: same-layer crossings and
shorts in the CM5-to-ESD escape, WSON power/ground pad-field interference,
right-column escape collisions, and MDI corridor collisions with the J2 NPTH
and PTH pad field. It reports 390 total native DRC violations, including the
known acreage baseline debt, and 237 unconnected items. It is rejected and is
not a production PCB.

This closes the authorized local placement-repair attempt for the current
standard TPD4E004 two-layer topology. Phase 17 remains blocked; no Phase 18+
work was started. The smallest practical continuation is an Ethernet-local
component change. The preferred candidate for the next disposable trial is
Littelfuse `SP3019-04HTG`: its gullwing SOT-23-6L layout has I/O on 1/3/4/6,
GND on 2, and NC on 5, avoiding the current TPD4E004 power/signal choke
point. This is not yet promoted; it must first pass pin-accurate footprint,
sourcing, native DRC, and complete Phase 17 validation.

## Independent specialist correction — 2026-09-03

The high-speed review determined that SP3019 is not geometrically impossible.
The prior SP3019 trial is invalid as a feasibility proof because it has
electrical construction defects:

- B.Cu routes do not transition to the F.Cu-only SMD pads through vias.
- `CM5_GBE_TD0_P` is declared by the generator but absent from the saved PCB.
- The trial footprint lacks authoritative solder-mask, paste, courtyard, and
  complete assembly data.
- The trial mixes 0.10 mm and 0.13208 mm tracks without a documented impedance
  basis; the latter was inherited from an approximately 90 ohm result, not a
  verified 100 ohm solution.
- SP3019 ground pads are floating in the trial because `ETH_GND` is not
  assigned in its generated net table.
- The trial does not contain the complete ESD-to-MagJack channel, center-tap
  support, shield return, or connector launch.

Therefore the 335-violation / 238-unconnected result is a rejected artifact,
not evidence that SP3019 cannot work. The specialist’s bounded topology is:
keep each pair together, assign one pair per device to F.Cu over L2, use
ordinary through-vias outside J7 and the ESD pads for the alternate B.Cu pair,
use short F.Cu dogbones at the ESD pads, and add verified GND stitching at
reference transitions. This remains within the approved layer policy.

## Exact current blocker

Phase 17 is blocked because the current clean authority still specifies
TPD4E004 and no valid SP3019-authoritative implementation has yet been built.
The next bounded action is to construct a proper SP3019 disposable fixture
with the manufacturer land pattern, explicit vias, all eight pair nets,
documented 100 ohm JLC stack calculations, and complete J7 -> ESD -> EDAC
routing. If that corrected fixture passes candidate-specific native DRC, the
component replacement can be evaluated for promotion. If it fails, the failure
will be attributable to a valid topology rather than the prior malformed
trial.

The 100 ohm field solution and final SP3019 promotion remain unresolved. No
Phase 18+ work may begin until the complete Phase 17 gate passes.

## Resumed Phase 17 remap investigation — 2026-09-03

This is a recoverable Phase 17 authority-boundary report, not a new terminal
design failure. The requested BCM54210PE lateral-thinking path was checked
against the exact CM5 and CM5IO authorities.

CM5 documentation explicitly lists automatic MDI crossover, pair-skew
correction, and pair-polarity correction. Broadcom's public BCM54210 page
confirms the active 10/100/1000BASE-T PHY and common wiring-problem
correction. However, no public BCM54210PE-specific register/table or
application schematic was found that authorizes arbitrary four-pair PCB
permutation. The official CM5IO implementation remains four intact TRD0..3
pairs into a standard 1:1 MagJack.

The legal candidate matrix is preserved in
`pisxme/reva-clean/PHASE17_ETHERNET_REMAP_CANDIDATES.md`:

- authoritative baseline: intact TRD0..3, 1:1;
- conditional disposable candidates: complete pair swaps 0↔1, 2↔3, or both;
- conditional polarity: P/N inversion only within an intact pair;
- rejected: arbitrary pair permutation and individual-conductor mixing.

Because 1000BASE-T uses all four pairs bidirectionally, 10/100 TX/RX MDI-X
language cannot be used to silently authorize an arbitrary four-pair router.
Pair-skew correction also does not legalize copper crossings. No remapped
fixture was promoted, and no clean PCB/schematic was modified.

Current status: `RECOVERABLE_AUTHORITY_BOUNDARY`; Phase 17 remains open.
The smallest authorized continuation is to obtain exact BCM54210PE mapping
authority, or explicitly choose a different Ethernet connector/ESD/launch
architecture under the existing layer contract. Accepting unproven remapping
as Rev-A empirical risk would be a user-controlled gate decision.

Additional exact-part check: Broadcom's public product page is family-level
and reports BCM54210 as active, but the CM5 variant `BCM54210PEB1KMLG` is
identified in a Broadcom EOL notice as obsolete (last-time-buy 2023-04-26,
last-time-ship 2024-04-25). This is lifecycle evidence about the embedded CM5
PHY, not a reason to alter CM5 hardware; it does mean generic BCM54210-family
collateral cannot substitute for an exact BCM54210PE register or permutation
document.

## Independent specialist confirmation — 2026-09-03

The independent high-speed/documentation review confirms that the CM5
datasheet is exact-device evidence for MDI crossover, polarity correction,
pair-skew guidance, and the 1:1 MagJack topology, but not for arbitrary
four-pair reassignment. It specifically rejects treating `TRD0↔TRD2`, cyclic
rotation, or wholesale reversal as guaranteed BCM54210PE behavior.

The review also records the exact lifecycle/procurement boundary: public
EOL-254829 lists `BCM54210PEB1KMLG` with MOQ 32,760 and passed LTB/LTS dates;
TrustedParts' authorized-channel snapshot reports no stock. Broker or
marketplace listings do not close that procurement gap.

Final disposition remains `PISXME_REVA_CLEAN_BLOCKED`, earliest failed gate
Phase 17 Ethernet routing. The complete remap evidence is in
`PHASE17_BCM54210PE_REMAP_AUTHORITY.md`; no clean design asset changed.
## Phase 17 SP3019 authoritative fixture update — 2026-09-03

Status: `RECOVERABLE_FIXTURE_ROUTING_BLOCKER`

The Littelfuse SP3019-04HTG candidate is not rejected on the basis of the
earlier malformed trial. A new manufacturer-footprint trial was generated with
the exact four-channel SOT23-6L pin assignment, explicit pin-2
`/ETHERNET/ETH_GND`, pin-5 NC, and all eight CM5 Ethernet nets. The generator
now uses KiCad's typed `FOOTPRINT` copy constructor and native
`FindPadByNumber`, so both U6 and U9 are actually populated and saved.

Evidence:

- Fixture: `pisxme/reva-clean/SP3019_ETHERNET_DISPOSABLE_FIXTURE.kicad_pcb`
- Generator: `pisxme/reva-clean/phase17_sp3019_trial.py`
- Manufacturer footprint: `pisxme/reva-clean/PiSXMe_RevA_Clean.pretty/SP3019_04HTG_SOT23_6L.kicad_mod`
- Native DRC: `pisxme/reva-clean/SP3019_ETHERNET_DISPOSABLE_FIXTURE-drc.rpt`
- Initial full-board DRC result: 96 violations, 76 unconnected items.
- Isolated-base rerun: 65 violations, 21 unconnected items after removing
  unrelated CM5 source pads from the disposable J7 copy.
- Reoriented two-layer corridor experiment: 105 violations, 4 unconnected
  items. This reduced dangling connectivity but introduced multiple true
  same-layer shorts/crossings at the J2 launch and did not provide a valid
  transition topology; it is rejected.
- Third explicit-transition corridor experiment: 86 violations, 4
  unconnected items after correcting the ordinary via to the board minimum
  0.50 mm diameter / 0.30 mm drill. It still has true source/via fanout and
  J2 support-pad shorts/crossings, so it is also rejected.
- Separated-placement corridor experiment: 74 violations, 4 unconnected
  items. Moving the disposable J7/J2 anchors farther apart and keeping the
  F.Cu/B.Cu pair groups monotonic reduced the failure set further, but native
  DRC still reports genuine four-pair fanout/launch crossings and shorts. It
  is rejected; this is the current best bounded SP3019 trial.
- Return-path correction: 79 violations, 0 unconnected pads after joining the
  two external SP3019 GND return vias with a B.Cu GND spine. Connectivity and
  return continuity now pass, but true pair crossings/shorts remain, so the
  fixture is still rejected for Phase 17.
- Source-fanout correction: 76 violations, 0 unconnected pads after moving the
  source transitions onto separated external lanes and correcting the B.Cu
  segment construction. This removes the prior dangling-net class, but true
  pair crossings/shorts and connector clearances remain.
- Material isolated-fixture failures are true pair crossings, connector-launch
  shorts to center-tap pads, and no ordinary via/F.Cu dogbone transitions for
  the B.Cu-assigned pairs. Therefore this is not a valid Phase 17 proof.

The result does not prove SP3019 is geometrically impossible. It proves the
current disposable route construction is not yet a valid fixture. SP3019 is
not promoted and the clean board is unchanged.

## Official CM5IO CAD oracle audit — 2026-09-03

The official Raspberry Pi CM5IO Rev 2 KiCad archive was downloaded from the
Raspberry Pi design-files page, SHA-256
`48b14a6757b0edc0ac110331445f35a4212b5ce432bdcec6605c99431b59496b`, and
inspected as native `CM5IO.kicad_sch` and `CM5IO.kicad_pcb` files. The archive,
exact-copy fixture, and DRC receipts are privately pushed in commit `56f4b2d`.

The native CM5IO Ethernet block is a valid reference implementation: intact
TRD0..TRD3 pair order and polarity; two rotated `TPD4EUSB30` /
`USON-10_2.5x1.0mm_P0.5mm` protectors; all eight MDI routes on F.Cu at
0.127 mm; compact source -> ESD -> MagJack placement; and complete tap, LED,
shield, GND, and support routing. Native source and exact-copy DRC found zero
unconnected items and no MDI crossing, shorting, or dangling-via findings.

The oracle cannot be copied blindly into PiSXMe: official U3 uses Trxcom
`TRJG0926HENL`, while PiSXMe authority selected EDAC `A70-112-331N126`, and
their mounting/shield-hole geometry differs. The official ESD value/BOM had a
hidden metadata conflict, now resolved by TI's current authority as exact
orderable `TPD4EUSB30DQAR` (active DQA/USON-10). PiSXMe previously used
TPD4E004 WSON6 devices and a remote MagJack, unlike the official compact
topology.

This is a recoverable transplant/authoring blocker, not evidence that CM5
Ethernet is architecturally impossible. The next authorized experiment is a
disposable CM5-adjacent PiSXMe fixture using separately authoritative
PiSXMe footprints/MPNs and the proven pair-preserving topology under the
six-layer/100-ohm/no-plane-signal contract. No clean PCB/schematic or Phase
18+ artifact has been changed.

## CM5IO-derived MDI transplant — 2026-09-03

The official 189-segment MDI geometry was rigidly transformed onto the
PiSXMe J7 and EDAC physical contact coordinates in disposable fixture
`pisxme/reva-clean/CM5IO_PISXME_ETHERNET_TRANSPLANT_FIXTURE.kicad_pcb`.
The fixture uses the official TI `TPD4EUSB30DQAR` USON-10 footprint and the
CM5IO flow-through pin map.

Evidence:

- `validation/phase17/test_cm5io_transplant_fixture.py` passes all eight
  J7 -> ESD -> EDAC MDI mappings, 0.127 mm F.Cu width, and pair skew below
  2 mm.
- Native DRC reports zero MDI crossings, shorts, dangling vias, and footprint
  errors. The DRC file is
  `pisxme/reva-clean/CM5IO_PISXME_ETHERNET_TRANSPLANT_FIXTURE-drc.rpt`.
- The exact official fixture remains the complete support/tap/shield oracle;
  the adapted fixture's separately routed support overlay still fails and is
  rejected. No clean acreage asset has been promoted.

Current state remains `PISXME_REVA_CLEAN_RECOVERABLE_PHASE17`: the proven MDI
geometry is closed as an experiment, but full connector support/return and
acreage placement/routing still require a valid complete fixture before Phase
17 can close. The next work is bounded support adaptation, not another ESD
component safari.

Bounded continuation options, all within the approved architecture:

1. Recommended next: continue from the now-created minimal base containing
   only the eight authoritative J7 source pads, the complete authoritative J2
   Ethernet launch/support pads, two manufacturer SP3019 footprints, explicit
   GND/return vias, and a large acreage outline. Solve the four pair corridors
   there before reintegrating the full connector footprints.
2. Reorient the EDAC launch and split the four pairs into monotonic top/bottom
   corridors, adding symmetric ordinary through-via transitions outside the
   SP3019 pads.
3. If the corrected SP3019 fixture still fails, repeat the same minimal
   experiment with the active TI `ESDS304DBVR` SOT23-5 Ethernet protector,
   preserving the same approved layer and 100-ohm constraints.

No frozen subsystem has been changed. No clean PCB/schematic has been changed.
Phase 17 remains open pending a complete fixture with zero candidate-specific
opens/shorts/crossings, complete connector launch, and documented 100-ohm
geometry.

## Correction to ESDS304 evidence — 2026-09-03

The initial ESDS304 DRC result was not admissible as component evidence: the
local footprint had the wrong pad-side distribution and overlapping pads.
The footprint has now been corrected to the TI DBV0005A arrangement and the
fixture was regenerated from scratch. The corrected rerun reports **100
native DRC violations and 11 unconnected items**, including true ESD/source
shorts, crossings, and incomplete launches. That candidate route is rejected,
but the corrected result does not reject ESDS304 electrically. A further
Ethernet-local escape construction remains required before Phase 17 can pass.

The clean authority and production PCB remain unchanged. This is the current
blocker record; Phase 18+ has not started.

## ESDS304 large-acreage escape experiment — 2026-09-03

A fresh large-acreage fixture was built with the corrected TI-authoritative
ESDS304 footprint, U9/U6 placed away from J7, separate F.Cu/B.Cu corridors,
ordinary transitions, local ground returns, and J2 moved to a dedicated
connector launch zone. Native KiCad DRC reports **92 violations and 8
unconnected items**. The failure set includes B.Cu shelf crossings, direct
source/ESD interactions, connector launch shorts/clearance failures, and
incomplete connectivity. This candidate is rejected; no production asset was
changed.

Reproducible artifacts:

- `pisxme/reva-clean/phase17_esds304_clean_trial.py`
- `pisxme/reva-clean/ESDS304_ETHERNET_CLEAN_DISPOSABLE_FIXTURE.kicad_pcb`
- `pisxme/reva-clean/ESDS304_ETHERNET_CLEAN_DISPOSABLE_FIXTURE-drc.rpt`

The blocker remains recoverable within the approved Ethernet-local placement
repair. Phase 18+ has not started.

## Additional fallback candidate — TI ESDS311DYFR

The next practical solution class has been identified but not yet promoted:
eight active TI `ESDS311DYFR` single-channel SOD-323 shunt protectors. TI
explicitly rates ESDS311 for 10/100/1000 Ethernet and lists the active device
with a simple two-pad topology. Regional distributor evidence captured
Mouser stock of 4,510 and Digi-Key stock of 2,745. Its 4.5 pF typical
capacitance and eight-device assembly burden make it a fallback behind
SP3019/ESDS304. A proper disposable fixture and native validation are still
required; no production asset has changed.

## ESDS311 disposable fixture — 2026-09-03

The authorized single-line fallback was instantiated with eight TI ESDS311DYFR
SOD-323 footprints, explicit signal/ground pad mapping, ordinary source and
ESD transition vias, and the EDAC launch. The first run exposed a malformed
SMD-to-B.Cu termination; that was corrected with a local F.Cu dogbone and
ordinary via at every protector line pad. The corrected native KiCad run still
reports **212 DRC violations and 24 unconnected items**, including B.Cu
crossings, source-lane interactions, connector-launch conflicts, and residual
connectivity defects. The fixture is rejected and ESDS311 is not promoted.

Artifacts: `pisxme/reva-clean/phase17_esds311_trial.py`,
`pisxme/reva-clean/ESDS311_ETHERNET_DISPOSABLE_FIXTURE.kicad_pcb`, and
`pisxme/reva-clean/ESDS311_ETHERNET_DISPOSABLE_FIXTURE-drc.rpt`.

This is a further routing-construction failure, not a new authority or
software-installation blocker. No clean production asset changed; Phase 18+
remains unopened.

## ESDS304 authority-only proof — 2026-09-03

The corrected TI DBV0005A footprint and disposable mapping now pass the
machine-check in `pisxme/reva-clean/PHASE17_ESDS304_AUTHORITY_CHECK.md`:
pad positions, 0.6 mm × 1.1 mm exposed metal, 1/2/3-left and 5/4-right
arrangement, F.Cu/F.Paste/F.Mask layers, courtyard, U9/U6 pin mapping, all
eight MDI nets, and explicit ETH_GND are verified. This closes the package
authority sub-question. It does not close Ethernet routing; the latest route
fixture still fails native DRC and remains unpromoted.

The written research note was also corrected to state TI's 2.6 mm DBV0005A
row separation (rather than the earlier 1.9 mm typo). The machine-check and
footprint now agree.

## Final Phase 17 disposition — 2026-09-03

The authorized repair space has been exhausted without a passing candidate:

- SP3019-04HTG: best corrected native result still had 76 violations.
- ESDS304DBVR: best corrected native result had 92 violations and 8
  unconnected items.
- ESDS311DYFR: corrected eight-device fixture had 212 violations and 24
  unconnected items.

The repeated common failure is the CM5/J7 to ESD to EDAC launch geometry under
the frozen F.Cu/B.Cu-only signal-layer contract, ordinary-via rule, and fixed
connector fields. The remaining choices require a user-controlled
architectural decision:

1. Select a different authoritative Ethernet connector/ESD land-pattern
   arrangement and reopen the corresponding authority and placement gates.
2. Permit an additional signal-routing layer or changed layer contract, then
   redo stack/impedance and affected routing validation.
3. Retain the current contract and defer until a physically different
   authoritative connector/ESD combination is selected.

Recommendation: option 1, preserving the six-layer board while addressing the
connector-boundary launch choke point. Final state:
`PISXME_REVA_CLEAN_BLOCKED`; earliest failed gate: Phase 17 Ethernet routing.
Production files remain untouched.

## BCM54210PE remap investigation — 2026-09-03

The requested PHY-capability unblocker was investigated. Broadcom's public
BCM54210 authority confirms active 10/100/1000BASE-T operation and correction
of common wiring problems; Raspberry Pi's official CM5IO Rev 2 authority
preserves four intact TRD differential pairs. No public BCM54210PE-specific
register/table was found that authorizes arbitrary four-pair permutation.

The legal trial boundary is therefore: intact pairs only; conditional
complete-pair MDI/MDIX variants; conditional P/N inversion per intact pair;
no individual-conductor mixing and no unproven arbitrary permutation. The
full evidence and remap table are in
`pisxme/reva-clean/PHASE17_BCM54210PE_REMAP_AUTHORITY.md`. This investigation
does not yet close Phase 17 routing.

The generator was then aligned to the corrected TI pad coordinates and rerun.
That endpoint-corrected candidate reports **104 native DRC violations and 7
unconnected items**. It is also rejected. The reduced dangling count confirms
the footprint/endpoints are now being exercised, while the remaining defects
are genuine route crossings/shorts and connector-launch geometry failures.

## Official CM5IO oracle and current support-adaptation boundary — 2026-09-03

The official Raspberry Pi CM5 IO Board Rev 2 native KiCad source was
downloaded, extracted, and inspected. Its complete disposable copy passes
native connectivity with 0 unconnected pads and no MDI crossing, shorting, or
dangling-via findings. The official implementation uses intact TRD0..TRD3
pairs, rotated flow-through TPD4EUSB30 USON-10 protection, and a compact
MagJack launch; it does not require arbitrary PHY pair remapping.

The PiSXMe CM5IO-derived MDI transplant separately passes its focused
regression: all eight MDI nets map J7 -> USON -> EDAC, use the authoritative
0.127 mm F.Cu geometry, and meet the recorded pair-skew limit. It is not yet
a Phase 17 pass because its support overlay is incomplete. Native DRC reports
five unconnected support/return pads and an invalid disposable outline; the
first full overlay also showed real center-tap, shield, and ESD-ground
crossings/shorts. These are support-adaptation construction defects, not a
failure of the official Ethernet architecture. No clean PCB or schematic has
been promoted from this experiment.

Current status: `PISXME_REVA_CLEAN_RECOVERABLE_PHASE17_SUPPORT_ADAPTATION`.
The next authorized action is to repair the EDAC support fanout using the
official support topology, explicit EDAC pad aliases, a valid fixture outline,
and deliberate GND/shield return, then rerun native DRC and the acreage gate.
Phase 18+ remains gated. This is a recoverable implementation blocker, not a
terminal design rejection.

## Support-zone repair experiment — 2026-09-03

The next bounded experiment used the passing official MDI transplant as an
immutable base and attempted to close the remaining support nets with a
common `ETH_CT_COMMON` In2 island, local F.Cu/In1/B.Cu `ETH_GND` return
islands, an outer B.Cu `GBE_SHIELD` return, and a valid Edge.Cuts rectangle.

Native DRC result: 82 violations and 13 unconnected support pads. The
experiment is rejected. The errors are fixture-authoring issues—detached
zone connectivity, hole-clearance against the large zone, and support/return
placement—not MDI crossings in the transplanted pair routes. The official
CM5IO complete fixture still independently proves the support topology with
0 unconnected pads and no MDI crossings or shorts.

The blocker therefore remains recoverable and specifically localized to
transplanting the official support copper/return structure across the EDAC
mechanical land pattern. Next continuation: copy/transform the official
support zones and support footprints from the native oracle, then replace
only the EDAC boundary pads with the explicitly authorized aliases. Do not
promote the current failed support-zone experiment or begin Phase 18+.

## Explicit support-fanout follow-up — 2026-09-03

The broad detached zones were replaced with explicit same-net B.Cu
center-tap fanout, compact local GND islands, ordinary return vias, and an
outer shield route. This reduced native DRC from 82 to 18 violations and
unconnected support pads from 13 to 7, while preserving the passing MDI
geometry. It is still rejected: the remaining failures are two EDAC common
center-tap lands, C1 common, four USON ground connections, and one shield /
center-tap clearance interaction. No MDI pair crossing or MDI short was
introduced.

This remains an active recoverable Phase 17 support-adaptation blocker. The
next bounded repair is to use the official support footprint/zone geometry as
the donor for those exact return connections, rather than continuing to
invent detached support copper. The clean production assets remain
unpromoted and Phase 18+ remains gated.

## Complete CM5IO-derived fixture — 2026-09-03

The explicit support-fanout repair now passes the substantive disposable
fixture gate. Native DRC reports 0 unconnected pads, 0 footprint errors, and
no shorting, crossing, hole-clearance, dangling-via, invalid-outline, or
silkscreen errors. Five warnings remain: three low-clearance EDAC support
warnings and two detached-library footprint mismatches. The focused MDI
regression and the warning-only DRC regression both pass.

The passing artifact is still a disposable topology proof. The clean acreage
board has not yet been updated because its authoritative schematic/footprint
path still requires promotion from TPD4E004 to the CM5IO-authoritative
`TPD4EUSB30DQAR` flow-through package and then a fresh Phase 11/12 placement
and Phase 17 production-routing validation. Phase 18+ remains gated.

## Acreage application attempt — 2026-09-03

The clean schematic authoring path has now been promoted to the active TI
`TPD4EUSB30DQAR` USON-10 package. Its native netlist contains the expected
eight CM5 MDI nets and the focused PCB pin-mapping regression passes.

The first acreage application script was rejected before promotion. The
CM5IO-derived disposable fixture uses a temporary common center-tap alias and
an oracle-specific EDAC assignment: its route reaches fixture J2 pads 1/2,
3/6, 7/8, and 9/10, while the production EDAC A70-112-331N126 authority uses
MDI groups 1/2, 3/4, 5/6, and 7/8, with center taps on 9..12. Copying those
tracks onto the production footprint would therefore silently change the
magnetics pin mapping. That is a real integration mismatch, not evidence
against the CM5IO Ethernet topology.

A disposable acreage attempt that retained the production EDAC footprint and
the unmodified oracle tracks was run only as a diagnostic. Native DRC found
628 violations and 482 unconnected items, including the expected connector
launch/support mismatch plus unrelated pre-existing acreage courtyard and
hole-clearance violations. It is rejected and was not promoted. The report is
`pisxme/reva-clean/ACREAGE_CM5IO_ETHERNET_PHASE17-drc.rpt`.

Current status:
`PISXME_REVA_CLEAN_RECOVERABLE_PHASE17_EDAC_LAUNCH_ADAPTATION`

Exact blocker: adapt the passing CM5IO source-to-ESD geometry to the
manufacturer-authoritative EDAC MDI pad groups, then regenerate only the
EDAC-side pair launches and center-tap/support connections. The remaining
authorized options are:

1. preserve the CM5IO source/ESD island and author a pin-accurate EDAC launch;
2. use the official CM5IO MagJack as a disposable comparison fixture to
   isolate the connector-specific delta; or
3. if EDAC geometry remains incompatible after a pin-accurate launch trial,
   evaluate the official CM5IO MagJack as the production connector candidate
   with a new procurement/mechanical authority review.

Recommended next step: option 1. No software installation, frozen-subsystem
move, layer-contract change, or validation relaxation is required. Phase 17
and all later phases remain gated.

## Pin-accurate EDAC launch trial — 2026-09-03

A second, narrower disposable experiment was built from the passing CM5IO
transplant. It retained the CM5-to-ESD portion, cut the oracle connector-side
tracks, assigned the production EDAC MDI pads 1..8, and regenerated the
EDAC-side launch to the actual EDAC pad coordinates at 0.127 mm F.Cu width.
This is the first trial that exercises the production EDAC MDI numbering
without copying the fixture's temporary common-tap alias.

It is rejected by native KiCad DRC: 20 violations, 17 unconnected items,
including pair crossings and shorts between TD1/TD0/TD2 and the retained
ESD-side geometry. The support footprints are intentionally retained in this
fixture, so the unconnected count includes support pads; the candidate is not
a production-board change. The complete report is
`pisxme/reva-clean/CM5IO_EDAC_PIN_ACCURATE_LAUNCH_FIXTURE-drc.rpt`.

This result is useful: it proves that a naive straight EDAC launch cannot be
accepted, but it does not reject the CM5IO architecture. The next distinct
authorized experiment is a connector-side layer-split/pair-preserving launch
or an official-connector comparison, with explicit return/support treatment.
No Phase 18+ work has started.

## EDAC connector-side layer-split trial — 2026-09-03

The next distinct trial moved TD1 and TD3 through ordinary F.Cu-to-B.Cu
transitions outside the ESD pads, leaving TD0 and TD2 on F.Cu. This follows
the approved layer policy and keeps each differential pair together. Native
DRC improved the launch-specific total from 20 to 14 violations, but still
found two track crossings, three net shorts, and 17 unconnected items.

The candidate is rejected. The remaining unconnected count includes support
pads inherited by the disposable source; the shorts/crossings are sufficient
to fail the acceptance gate independently. No production asset or later
phase was changed. The candidate and report are retained as
`CM5IO_EDAC_PIN_ACCURATE_LAUNCH_FIXTURE.kicad_pcb` and
`CM5IO_EDAC_PIN_ACCURATE_LAUNCH_FIXTURE-drc.rpt`.

The next bounded option is the official CM5IO MagJack comparison fixture,
which separates the already-passing source/ESD escape from the EDAC-specific
launch geometry. The complete official CM5IO fixture remains passing; the
EDAC production launch remains the earliest failed Phase 17 gate.

## CM5IO/EDAC mapping correction — 2026-09-03

The official CM5IO PCB and EDAC drawing were rechecked together. The prior
EDAC-launch blocker used the wrong interpretation of the footprint: the
authoritative MDI pads are `1,2,3,6,7,8,9,10`, exactly matching the official
CM5IO launch; pads `11..14` are center taps. The failed sequential-pad and
asymmetric layer-split trials are therefore withdrawn as geometry evidence.

The clean authoring path now uses the production grouping `U6 = TD0/TD1`
and `U9 = TD2/TD3`, with the physical references swapped to the official
right/left CM5IO locations. Native netlist export and the corrected PCB
mapping regression pass. The regenerated official transplant fixture still
passes native DRC with zero unconnected pads and no MDI crossings/shorts.

A fresh acreage placement diagnostic remains failed because the current
floorplan contains unrelated copper/keepout conflicts around the transplanted
island; its DRC is not an Ethernet-only gate. The next authorized action is
to place the CM5IO-aligned island in genuinely free acreage, then run the
Ethernet-specific native DRC/connectivity and full Phase 11/12 review. Phase
17 remains open; Phase 18+ has not started.

The corrected CM5IO-aligned acreage diagnostic was then regenerated from the
native netlist and applied through a single-board geometry-snapshot path.
The Ethernet mapping regression passed and all 189 official MDI segments were
preserved at the corrected physical positions. Full-board native DRC still
reports 539 violations and 477 unconnected items, with Ethernet pair shorts
against neighboring power/keepout geometry. This is a placement/floorplan
failure of the current acreage context, not a valid rejection of the now
pin-correct CM5IO/EDAC island; the disposable oracle remains the clean
reference. The current dirty legacy candidate was not overwritten.

## Phase 16 routed-ancestor restore — 2026-09-03

To avoid drawing conclusions from the unrouted floorplan, Phase 16 copper was
exported by stable net name into `phase16_copper_snapshot.json` and restored
onto a corrected clean materialization. The snapshot contains 320 routed
copper items; the Ethernet MDI vectors were then applied through a separate
single-board path. The corrected Ethernet footprint mapping regression passes.

The restored routed-ancestor DRC reports 835 total violations and 460
unconnected items. The report includes existing Phase 16/acreage debt, but it
also shows the relocated Ethernet vectors colliding with neighboring power
routes/keepouts. Therefore this is not a Phase 17 pass and the candidate was
not promoted. The snapshot/export/restore scripts preserve a reproducible
boundary for the next Ethernet-local placement experiment.

## Authoring-path correction — 2026-09-03

The current-source audit found two stale assumptions in the earlier Phase 17
evidence. The transplant generator had been using a 90° USON with swapped net
labels, while the clean schematic authority maps U6 pads 1/2/9/10 to TD0 and
U9 pads 1/2/9/10 to TD2. The generic transplant path now uses 270° local
USON orientation with the clean pad mapping, preserving the official copper
geometry without relabeling pads.

The schematic generator also emitted ordinary local labels for the generated
MDI symbol instances. Those are now emitted as global labels for the eight
MDI nets; the correction is generic in `phase17_promote_cm5io_ethernet.py`
and was applied idempotently to `ETHERNET.kicad_sch`. The regenerated native
netlist contains the complete duplicated flow-through pads:

`U6:1,10` / `U6:2,9` / `U6:4,7` / `U6:5,6` and the corresponding U9 pairs,
plus J7 and J2, with no local MDI labels remaining. The hierarchy-authority
regression now passes from current files.

The corrected disposable transplant was regenerated and natively checked:
8 warning-only violations, 0 unconnected pads, and 0 footprint errors. This
is an authoring/fixture correction, not a Phase 17 acreage pass. The routed
ancestor still has the placement-context failures documented above, so
Phase 18+ remains gated.

## J7 launch nested-lane refinement — 2026-09-03

The J7-only oracle was refined again using the measured field geometry. The
left source group remains on B.Cu; the right group transitions through
ordinary vias and uses nested F.Cu lanes above the J7 body, with 2.0 mm via
pitch and reverse-ordered bus x positions. This construction avoids the
opposing pad field and the earlier same-y bus crossings.

Native KiCad DRC reports **34 total violations / 63 unconnected non-MDI
pads**. The 63 are expected because the full CM5 footprint is present without
the rest of its circuit. Among candidate-local findings there are **zero
tracks-crossing, zero shorting-items, and zero hole-clearance violations**;
two adjacent source-via clearance violations remain, plus the fixture's
track-width rule still reports the intentionally CM5IO-derived 0.127 mm
width. This is not yet a Phase 17 pass, but it proves the J7 launch can be
made crossing-free under a bounded two-layer construction.

The failed height-offset variant was not promoted because it reintroduced a
TD1_N/TD0_N crossing. The controlling fixture/report are
`CM5IO_J7_LAUNCH_FIXTURE.kicad_pcb` and
`CM5IO_J7_LAUNCH_FIXTURE-drc.rpt`.

## Top-left side-escape placement trial — 2026-09-03

After correcting the USON orientation/mapping, a distinct placement class was
tested: the official connector/ESD-side geometry was translated to J2=(30,45)
above and left of J7, with J7 pair groups exiting around the connector sides
before rising to the ESD island. This avoids the regulator/C5-C8 corridor that
invalidated the previous CM5IO-aligned placement.

The candidate is rejected by native KiCad DRC: 428 violations and 485
unconnected items. The Ethernet-local failures include pair crossings and a
TD2_P/TD2_N short in the side escape. The translated EDAC LED/support lands
also overlap the nearby F1/input-envelope region. The unconnected count is
not used as an Ethernet-only metric because this candidate was built on the
unrouted acreage ancestor; the true pair crossings/short are independently
fatal. No frozen subsystem was moved and no production PCB was promoted.

The experiment is retained as
`ACREAGE_CM5IO_TOP_ISLAND_SIDE_ESCAPE_PHASE17.kicad_pcb` with its native DRC
report and generator. It narrows the authorized placement search: a passing
candidate needs both a J7 side escape that preserves pair order and a support
placement clear of F1, while retaining the official CM5IO topology.

## Top-left B.Cu escape trial — 2026-09-03

The same top-left island was tested with ordinary through-vias immediately
outside the J7 body, B.Cu pair corridors, and F.Cu dogbones into the official
ESD-side graph. This stays within the approved layer contract and does not
use via-in-pad or plane-layer signals.

The candidate is rejected by native KiCad DRC: 495 violations and 485
unconnected items. The focused Ethernet failures include TD2/TD3 and TD0/TD1
pair shorts/crossings at the hand-placed transition lanes. The remaining
unconnected count again includes the unrouted acreage ancestor and is not
used as an Ethernet-only conclusion. The variant is retained as
`ACREAGE_CM5IO_TOP_ISLAND_BCU_ESCAPE_PHASE17.kicad_pcb` with its native DRC
report. The official CM5IO all-F.Cu topology remains the reference; this
local B.Cu trial does not supersede it.

## Coordinate-corrected top-left trials — 2026-09-03

The prior top-left report was itself internally inconsistent: its translation
constant moved the route, but the script left U6/U9/J2 at the old coordinates.
That was corrected so the rigid island is U9=(27.6,57.215),
U6=(33.6,57.215), and J2=(30,45), matching the translated official vectors.

The corrected all-F.Cu side-escape candidate still fails native DRC at 383
violations and 453 unconnected items, including true TD2 pair shorts and
multiple source-side crossings. The corrected B.Cu transition candidate
fails at 448 violations and 453 unconnected items, including true TD0/1,
TD2, and TD3 pair shorts/crossings. These are valid rejections of the
hand-authored escape paths; the official CM5IO connector/ESD-side geometry
remains clean. The corrected candidate files and reports are preserved for
comparison, and no production or frozen subsystem was changed.

## Monotonic-lane Ethernet trial — 2026-09-03

The side-escape generator was corrected again to keep the left J7 group in
ordered lanes (TD3 at approximately x=27, TD2 at x=24) and the right group
in ordered lanes (TD1 at x=40, TD0 at x=43), with the translated island now
at the consistent coordinates U9=(27.6,57.215), U6=(33.6,57.215), J2=(30,45).

This reduced the candidate to 364 native DRC violations and 453 unconnected
items. The unconnected count is inherited from the unrouted acreage ancestor;
the Ethernet-specific failure is four true pair crossings at the source-side
fan-in, plus clearance violations at the dense ESD/connector launch. The
candidate is rejected. The result shows that the remaining obstacle is the
relative source-to-ESD pair order, not the regulator or F1 placement alone.
The candidate and DRC report are retained as
`ACREAGE_CM5IO_TOP_ISLAND_MONOTONIC_FCU_PHASE17.*`.

## Current native root ERC revalidation — 2026-09-03

After the generic MDI-label correction, native KiCad 10 ERC was rerun from
the current root project. It reports 644 warning-only findings, dominated by
the existing scaffold's off-grid/unconnected endpoints and library metadata;
no root hierarchy-association error was found. The focused Ethernet
hierarchy-authority regression and current XML netlist mapping pass, but the
historical Phase 3 receipt's claim of zero total ERC findings is no longer
current and has been corrected in `PHASE3_STATUS.md`. The complete current
ERC report is `pisxme/reva-clean/PHASE17_NATIVE_ROOT_ERC_CURRENT.rpt`.

## TD3-outer physical-order trial — 2026-09-03

The official CM5IO source was rechecked before another Ethernet experiment.
Its working implementation remains the authoritative 1:1 mapping: the left
CM5 source group is TD3 then TD2, the right group is TD1 then TD0, both ESD
devices are TPD4EUSB30 in the official USON-10 footprint, and the MDI copper
is F.Cu-only. No arbitrary PHY pair permutation was introduced.

The next disposable trial changed the physical order of the left source
escape so TD3 occupies the outer/left lane and TD2 the inner/right lane. This
tests the source-order reversal identified in the monotonic trial while
retaining the official translated ESD/MagJack graph, ordinary through-via
policy, and no plane-layer signal routing.

Native KiCad DRC still reports **364 violations / 453 unconnected items**.
The candidate is rejected: Ethernet-local source/launch crossing and
clearance failures remain. The inherited unconnected count is not used as
the sole conclusion because this disposable is based on the unrouted acreage
ancestor; the true Ethernet crossings/clearance failures are independently
fatal. The candidate and native report are preserved as
`pisxme/reva-clean/ACREAGE_CM5IO_TOP_ISLAND_TD3_OUTER_PHASE17.kicad_pcb` and
`pisxme/reva-clean/ACREAGE_CM5IO_TOP_ISLAND_TD3_OUTER_PHASE17-drc.rpt`.

### Exact current blocker

The official CM5IO topology reproduces cleanly in the disposable fixture,
but no tested CM5-adjacent acreage adaptation has yet produced a legal
connector-to-ESD launch around fixed J7 while keeping the official
ESD/MagJack geometry and support acreage clear. Phase 17 remains open and
Phase 18+ is gated. The authorized next continuation is a fresh physical
placement class: move the complete official Ethernet island to an open board
edge or below/left of J7 and regenerate all source-to-island vectors, then run
native DRC. No new software, architecture change, or validation relaxation
is required.

## Right-shelf complete-island trials — 2026-09-03

Following the sidecar review, the complete CM5IO island was moved to the open
right shelf below the cooler reservation: J2 `(270,20)`, U9 `(267.6,32.215)`,
and U6 `(273.6,32.215)`, all with the authoritative orientations. The source
breakout was regenerated from the actual J7 pad anchors, with the left group
using a west corridor and the right group using a right corridor before
turning above the cooler.

The all-F.Cu trial was rejected by native DRC at **431 violations / 484
unconnected items**. A second ordinary-through-via layer-separated trial was
also rejected at **499 violations / 484 unconnected items**. Both contain
true Ethernet crossings/shorts/clearance failures and are not candidates for
promotion. They are preserved as
`ACREAGE_CM5IO_RIGHT_SHELF_PHASE17.*` and
`ACREAGE_CM5IO_RIGHT_SHELF_BCU_PHASE17.*`.

The official CM5IO fixture remains clean; the remaining failure is the
generated J7 breakout geometry, not the reference Ethernet architecture.
Phase 17 is still the earliest failed gate and Phase 18+ remains gated.

## 180-degree ESD reorientation fixture — 2026-09-03

The recommended high-information experiment was implemented as a fresh
disposable fixture. U9 (TD2/TD3) was placed at `(24,68)` and U6 (TD0/TD1) at
`(30,68)`, both at 180 degrees, with the EDAC MagJack at `(24,45)` at 180
degrees. MDI copper was regenerated from actual local pad coordinates rather
than copied from the stale translated graph. Pair identities and polarity
were preserved; no arbitrary PHY remap was used.

The first run was found to have inherited unrelated acreage context and is
superseded. The fixture was rebuilt as a genuinely disposable board using
only the authoritative J7, USON, and MagJack footprints. The isolated native
KiCad DRC reports **94 violations / 4 unconnected items**. Ethernet-specific
failures include true tracks-crossing and shorting items at the J7 launch,
including MDI-to-MDI and MDI-to-J7-pad conflicts, plus the fixture's default
0.200 mm minimum-width rule rejecting the CM5IO-derived 0.127 mm width. The
fixture is therefore not a passing proof and was not promoted.
It is preserved as
`pisxme/reva-clean/CM5IO_ROT180_WEST_FIXTURE.kicad_pcb` with
`CM5IO_ROT180_WEST_FIXTURE-drc.rpt` and its generator.

This experiment closes the hypothesis that package reorientation alone
removes the blocker. The official CM5IO block remains valid; the unresolved
item is a legal, mechanically clear escape from the fixed PiSXMe J7 pad
field into an Ethernet island. Phase 17 remains open and Phase 18+ remains
gated.

## Parametric right-channel trial — 2026-09-03

The right-shelf source fanout was rebuilt as a constrained channel from the
actual J7 Ethernet pad anchors: unique short dogbones, ordered parallel
lanes, and an upper corridor into the translated official island. This
removed the prior hand-fan diagonals while preserving intact PHY pairs,
F.Cu signal routing, and the approved layer contract.

Native KiCad DRC rejected the candidate at **447 violations / 485
unconnected items**. The candidate remains invalid because Ethernet-local
crossings/clearances persist; it was not promoted. It is preserved as
`pisxme/reva-clean/ACREAGE_CM5IO_RIGHT_CHANNEL_PHASE17.kicad_pcb` and
`pisxme/reva-clean/ACREAGE_CM5IO_RIGHT_CHANNEL_PHASE17-drc.rpt`.

The next high-information experiment is a complete CM5IO-derived island
reorientation with both USON ESD footprints at 180 degrees, regenerated
internal copper, and a monotonic four-lane fanout. This is still within the
approved Ethernet architecture and requires no software installation or gate
relaxation.

## Exact J7-launch-only oracle — 2026-09-03

The hardware-audit review required a fixture preserving the complete
authoritative J7 instance, including its opposing pad field and courtyards,
without inheriting acreage copper or unrelated footprints. That fixture now
uses the exact J7 instance and pad metadata, a valid outline, and separated
left/right external boundary pads.

Native KiCad DRC reports **27 violations / 63 unconnected pads**. The 63 are
non-MDI CM5 pads intentionally left without their surrounding CM5 circuit,
so they are not treated as a launch pass/fail metric. The 27 candidate-local
findings include real MDI launch crossings and clearance/hole issues and are
independently fatal. The fixture is retained as
`pisxme/reva-clean/CM5IO_J7_LAUNCH_FIXTURE.kicad_pcb` with
`CM5IO_J7_LAUNCH_FIXTURE-drc.rpt` and
`phase17_j7_launch_fixture.py`.

This is stronger evidence than the prior contaminated full-board trials: the
J7 launch is not yet proven routable under the current trial paths, but the
official CM5IO Ethernet architecture remains valid. Phase 17 remains open;
Phase 18+ remains gated.

## J7 launch sub-gate closure — 2026-09-03

The final J7-only source-order-preserving transition trial uses the exact J7
instance, opposing pad field, separated boundary exits, ordinary
through-vias, and nested F.Cu lanes above the body. Right-group via heights
preserve the measured source order: TD1_P, TD1_N, TD0_N, TD0_P.

Native KiCad DRC reports **zero tracks-crossing, zero shorting-items, zero
clearance violations, and zero hole-clearance violations**. Remaining DRC
categories are 24 track-width findings because the isolated board's default
netclass says 0.200 mm while the CM5IO-authoritative launch uses 0.127 mm,
plus 8 diagnostic dangling ends and 63 expected non-MDI unconnected J7 pads.
Those findings are explicit; the launch-specific geometric gate is closed,
while full Ethernet still requires ESD/MagJack integration, width-rule
reproduction, and complete connectivity.

The corrected oracle is preserved as
`pisxme/reva-clean/CM5IO_J7_LAUNCH_FIXTURE.kicad_pcb` with its generator and
native report. This closes the hypothesis that the fixed J7 pad field is
intrinsically unroutable; remaining Phase 17 work is complete-island
integration and validation.

## Current J7 launch receipt correction — 2026-09-03

The controlling rerun after the final source-order-preserving offset change
reports **32 total DRC violations / 63 expected non-MDI unconnected pads**:
24 width-rule findings and 8 diagnostic dangling ends. It still reports zero
tracks-crossing, zero shorting-items, zero clearance, and zero hole-clearance
findings. The prior 34-total count is superseded by this receipt.

The complete official CM5IO transplant was also rerun natively and reports 8
silkscreen-only violations with zero unconnected items. It remains the
complete-island authority baseline; the acreage copy is not accepted because
its unrelated floorplan debt is still present.

## Corrected J7 transition rerun — 2026-09-03

The prior receipt overstated the result because the right-side source
dogbones were initially started on B.Cu even though the authoritative J7
pads are F.Cu-only. The disposable generator was corrected so every J7
source begins on F.Cu, transitions through an ordinary through-via, and then
uses the intended permitted signal-layer corridor. The right group returns to
F.Cu through a second ordinary through-via; no via-in-pad is used.

The corrected native rerun reports **38 findings / 55 unconnected items**.
The unconnected items are fixture omissions dominated by the unpopulated CM5
power/ground pad field; no `CM5_GBE_*` item is reported as unconnected. There
are zero `tracks_crossing`, zero `shorting_items`, zero `via_dangling`, and
zero hole-clearance findings. Remaining findings are fixture diagnostics: 28
width-rule findings because the detached fixture still carries a 0.200 mm
default minimum instead of the CM5IO-authoritative 0.127 mm MDI width, eight
J7-adjacent copper-clearance findings against the dense pad field, and one
board-edge-clearance finding.

This supersedes the immediately preceding 32-finding receipt. It proves the
source-transition construction is electrically connected and crossing-free
under the trial geometry, but it is not a complete Ethernet or Phase 17
pass. The next authorized step is to combine this corrected J7 launch with
the official ESD/MagJack island and eliminate the remaining local
clearance/width-rule diagnostics before acreage promotion.

## Complete-island acreage adaptation rerun — 2026-09-03

The official CM5IO-derived disposable island was regenerated and checked
again. Native KiCad DRC reports **8 findings / 0 unconnected items** for
`CM5IO_PISXME_ETHERNET_TRANSPLANT_FIXTURE.kicad_pcb`; the findings are
library/silkscreen/known detached-fixture diagnostics, with no electrical
short or open in the eight MDI pairs.

The same transformed MDI geometry was then applied to the current acreage
candidate as a controlled adaptation test. Native DRC reports **539
findings / 477 unconnected items**, including **40 true shorting-items**, 42
clearances, 4 hole-clearances, and 189 width-rule findings. The failures are
at the local U6/U9 pad fields and collisions with existing acreage
power/regulator copper; this candidate is rejected and is not a production
PCB. The result confirms that the official topology is valid, but a direct
coordinate transplant is not a valid PiSXMe placement adaptation.

Preserved evidence:
`pisxme/reva-clean/CM5IO_PISXME_ETHERNET_TRANSPLANT_FIXTURE-current3-drc.rpt`
and
`pisxme/reva-clean/ACREAGE_CM5IO_MAPPED_CM5IO_PHASE17-current-drc.rpt`.
Phase 17 remains the earliest failed gate; no Phase 18+ work has started.

## Adapter-orientation correction — 2026-09-03

The first acreage transplant was also found to contain an authoring defect:
the adapter had both swapped U6/U9 placement ownership and a 90-degree
USON orientation, while the validated CM5IO fixture uses U9 for TD3/TD2,
U6 for TD1/TD0, and both protectors at -90 degrees. The adapter was corrected
to preserve that exact reference orientation and ownership.

The corrected controlled rerun improved the result from 539 to **435 native
DRC findings / 453 unconnected items**, and reduced true shorting findings
from 40 to **11**. It has no reported `tracks_crossing` or `via_dangling`
category, but the remaining shorts include collisions with existing
regulator/power copper and residual local ESD/connector geometry. It is
rejected as an acreage candidate, while the complete disposable reference
island remains valid. This is a corrected, narrower blocker—not evidence
against the official CM5IO Ethernet architecture.

The corrected report is
`pisxme/reva-clean/ACREAGE_CM5IO_MAPPED_CM5IO_PHASE17-corrected-drc.rpt`.
The next experiment remains a fresh local placement/escape adaptation that
uses the corrected U6/U9 ownership and official -90-degree orientation, with
the J7-to-ESD legs regenerated rather than coordinate-transplanted.

## Local-bottom island trial — 2026-09-03

A fresh acreage trial placed the CM5IO-derived island below the cooler
reservation (`U9/U6` near `(120,150)`, EDAC near `(122,138)`) and generated
new J7 source legs. The first all-F.Cu version was rejected at **441 native
DRC findings / 485 unconnected items**, including 18 crossings and 13
shorting findings. A split F.Cu/B.Cu variant was then run and rejected at
**540 findings / 453 unconnected items**, including 9 crossings, 30 shorts,
and 6 dangling vias.

The discriminating cause is now identified: the official -90-degree ESD
orientation expects the CM5 source to approach the lower side of the package
as on CM5IO. Moving that rigid island below J7 without rotating the complete
island reverses the approach side; the trial landing points then collide with
the official internal ESD escape. The split-layer trial also reused the
incorrect lane heights for both pair groups. Both candidates are rejected.

This is not evidence against the CM5IO design. The next bounded experiment is
to rotate the complete official island geometry and footprints as a rigid
180-degree local block, then regenerate the J7-to-ESD transitions from the
actual source pads. No Phase 18+ work has started.

## Rigid-rotation local-island trial — 2026-09-03

The complete official ESD/MagJack island was rotated 180 degrees as one
block, including the internal MDI graph, footprints, and connector
orientation. The CM5/J7 remained fixed. J7-to-ESD routes were regenerated
with immediate ordinary through-via transitions and no plane-layer signals.

Native KiCad DRC rejected the candidate at **491 findings / 453 unconnected
items**, including 12 crossings, 14 shorts, and 4 dangling vias. The
dominant newly isolated cause is insufficient separation of several pair
transition vias (0.4–0.5 mm) and overlap between same-layer lane segments
near the rotated ESD landing. The candidate is not promoted and does not
weaken the official CM5IO result.

This experiment closes the prior approach-side hypothesis: the official
island can be rotated as a coherent mechanical/electrical block. Remaining
work is a legal via-offset and lane-order repair. The next bounded trial will
use at least 0.8 mm center spacing for every adjacent transition-via pair and
will keep each pair's final ESD landing on one layer where possible.

Preserved evidence:
`pisxme/reva-clean/ACREAGE_CM5IO_ROTATED_LOCAL_PHASE17.kicad_pcb` and
`pisxme/reva-clean/ACREAGE_CM5IO_ROTATED_LOCAL_PHASE17-drc.rpt`.

## Mode-coordinate authoring correction — 2026-09-03

The earlier right-shelf/channel placement trials also contained a generator
defect: mode-specific `DX/DY` translations were applied to the MDI tracks but
not to U6/U9/J2 footprint positions. The generic mode path was corrected to
place U9 at the TD3/TD2 island location, U6 at TD1/TD0, and J2 at the same
translated CM5IO-relative location before DRC.

The corrected right-channel rerun reports **425 findings / 453 unconnected
items**, including 13 shorting findings and 9 crossings. It is rejected, but
the result is now valid evidence: the long F.Cu channel crosses frozen
power/regulator copper and the current source-lane fanout still crosses at
J7. The prior right-channel reports are superseded for placement conclusions
because their footprints were not co-located with their route graph.

The corrected generator is preserved in
`pisxme/reva-clean/phase17_top_island_side_escape.py`, with the native report
at
`pisxme/reva-clean/ACREAGE_CM5IO_RIGHT_CHANNEL_PHASE17-corrected-drc.rpt`.

## Right-channel B.Cu trial — 2026-09-03

The corrected right-channel candidate was rerun with its long source corridor
on B.Cu and ordinary through-via transitions. This reduced source-channel
crossings from 9 to **6**, but native DRC rejected the result at **467
findings / 453 unconnected items**. The remaining failures include 22 true
shorts, pair-via spacing violations at both ends, and overlapping B.Cu
segments caused by a single shared fanout path. It is rejected; the layer
policy itself remains valid.

This result distinguishes a useful layer assignment from an invalid
transition construction. The next experiment must stagger each pair's
source and return vias by at least 0.8 mm and give each pair its own B.Cu
lane; a single B.Cu bundle is not acceptable evidence.

Preserved evidence:
`pisxme/reva-clean/ACREAGE_CM5IO_RIGHT_CHANNEL_PHASE17-bcu-corrected-drc.rpt`.

## Independent west/east source-group trial — 2026-09-03

The B.Cu construction was changed again so the TD3/TD2 group exits west and
the TD1/TD0 group exits east, with separate vertical rises and separated top
corridors. This removed the single shared source fanout and retained
ordinary through-vias only.

Native KiCad DRC rejected the candidate at **455 findings / 453 unconnected
items**, including 18 crossings and 7 shorts. The remaining findings are
localized to the dense J7 dogbones, the connector-side final F.Cu return
segments, and the first pair-lane transitions. The trial is rejected, but it
confirms that source-group separation is necessary and that the remaining
problem is the pad-field escape construction—not the long top corridor.

Preserved evidence:
`pisxme/reva-clean/ACREAGE_CM5IO_RIGHT_CHANNEL_WEST_SPLIT_PHASE17.kicad_pcb`
and
`pisxme/reva-clean/ACREAGE_CM5IO_RIGHT_CHANNEL_WEST_SPLIT_PHASE17-drc.rpt`.

## Current continuation state — 2026-09-03

Phase 17 is **not closed**. The authoritative reference chain is still
validated independently: the extracted Raspberry Pi CM5IO Ethernet CAD
fixture has zero unconnected MDI nets, and the corrected J7 launch fixture
has no MDI crossings, shorts, dangling vias, or hole-clearance findings.

The remaining failure is the acreage integration geometry. The latest valid
candidate is the west/east source-group trial above; it is rejected. No
Phase 18+ work has started, and no clean production PCB/schematic has been
modified or promoted by these disposable experiments.

Next authorized action: reuse the exact J7-launch-only dogbone/transition
construction as the source boundary, then connect that proven boundary to a
freshly placed official CM5IO island with pair-specific lanes and native DRC
before any acreage promotion.

## J7-boundary to official-island fixture — 2026-09-03

The exact J7 launch fixture was joined to the complete official CM5IO-derived
U9/U6/EDAC/J9/C1 island. The original J7-to-boundary construction was kept
unchanged; only boundary-to-ESD bridge routes were added. Support copper and
the official internal MDI island graph were retained.

Native KiCad DRC rejected the first bridge layout at **277 findings / 68
unconnected items**, including 16 crossings, one electrical short, and 26
dangling tracks. The failures are confined to the newly authored boundary
bridges: the simple left/right paths intersect the existing J7 launch
geometry and the connector-side ESD approach. The exact J7 launch and exact
CM5IO island remain independently valid; this bridge candidate is rejected.

Preserved evidence:
`pisxme/reva-clean/CM5IO_J7_CM5IO_BOUNDARY_FIXTURE.kicad_pcb`,
`pisxme/reva-clean/CM5IO_J7_CM5IO_BOUNDARY_FIXTURE-drc.rpt`, and
`pisxme/reva-clean/phase17_j7_cm5io_boundary_fixture.py`.

The next experiment will route the bridge as four pair-specific corridors
with explicit layer separation and no reuse of the existing launch corridor.

## Outer-edge bridge-layer trial — 2026-09-03

The boundary bridge was rebuilt with pair-specific layer ownership: TD3/TD1
on F.Cu and TD2/TD0 on B.Cu, outer-edge detours, and 2 mm-separated return
vias before the official ESD lands. Native KiCad DRC rejected it at **303
findings / 68 unconnected items**, including 16 crossings, 6 shorts, and 4
dangling vias. The exact J7 launch remains valid independently; the failure
comes from the island still occupying the launch fixture's reserved bridge
envelope and from connector-side return-via/ESD approach collisions.

This candidate is rejected. The next authorized experiment will place the
official island outside the launch envelope first, then bridge it with
pair-specific routes; no further routing-only changes will be applied to the
overlapping placement.

Preserved evidence:
`pisxme/reva-clean/CM5IO_J7_CM5IO_BOUNDARY_FIXTURE-outer-drc.rpt`.

## Island-outside-launch-envelope trial — 2026-09-03

The complete official island was translated 90 mm east of the J7 launch
envelope, with all copied footprints and internal MDI tracks translated
together. The unchanged J7 launch boundary was then bridged to that remote
island. Native DRC improved to **254 findings / 78 unconnected items** for
the ordinary bridge and **266 findings / 78 unconnected items** for the
outer-layer bridge. The ordinary version has 11 crossings and 3 shorts; the
outer-layer version has 16 crossings and 4 shorts. Both are rejected, but
this confirms that island overlap was a real contributor and that the remote
island placement is a valid basis for the next pair-order repair.

The latest preserved report is
`pisxme/reva-clean/CM5IO_J7_CM5IO_BOUNDARY_FIXTURE-island-right-drc.rpt`.
No production acreage board was modified or promoted, and Phase 18+ remains
gated.

## Remote-island bridge rerun — 2026-09-03

The complete official island was moved 90 mm east of the J7 launch envelope
and all copied island geometry was translated together. This reduced the
ordinary bridge fixture to **254 findings / 78 unconnected items** with 11
crossings and 3 shorts. A pair-layer outer-detour variant measured **266 / 78**
with 16 crossings and 4 shorts. Neither passes, but both are materially
better than the overlapping placement and have no production-board impact.

The remaining crossings are now attributable to the bridge path ordering and
return approach, not footprint placement. The next construction is a
round-the-envelope bridge with pair-specific monotonic lanes, using the
remote island as the fixed endpoint and retaining the exact J7 launch as the
source endpoint.

## Pair/polarity-permutation bridge trial — 2026-09-03

The next disposable experiment deliberately used the BCM54210PE-supported
physical pair swap and per-pair polarity reversal while preserving P/N pair
integrity. TD1/TD0 were exchanged at the official island and the left-group
polarity order was corrected to match the measured J7 pad order. Each pair
was assigned to an ordinary F.Cu or B.Cu corridor; no plane-layer signal or
via-in-pad was used.

The first generator construction still had source dogleg crossings. The
corrected planar escape reduced the crossing count to **4**, but native KiCad
10.0.5 DRC still reports **247 violations / 78 unconnected items**, 16
dangling tracks, and 2 dangling vias. The candidate is rejected. The
remaining crossing locations are exact source/return approach intersections
and do not prove that the PHY remap or official Ethernet island is invalid.

The authoritative fixture and J7 launch remain separately valid. The
current blocker is therefore still a recoverable Ethernet bridge geometry
failure. The next implementation should use a genuinely layer-separated
pair escape (with explicit transition points) rather than further lane
coordinate tuning on this same two-layer construction.

Preserved evidence:
`pisxme/reva-clean/CM5IO_J7_CM5IO_BOUNDARY_FIXTURE-swap5-drc.rpt` and
`pisxme/reva-clean/phase17_j7_cm5io_boundary_fixture.py`.

### Canonical continuation packet

- `BLOCKER_ID`: `PHASE17_ETHERNET_REMOTE_BRIDGE_GEOMETRY`
- `SOLUTION_CLASS`: algorithm/design change — two-signal-layer bridge escape
- `ATTEMPTS_IN_CLASS`: round-envelope bridge; pair/polarity permutation;
  planar pair escape
- `AUTHORITATIVE_ORACLE`: official Raspberry Pi CM5IO KiCad source; its
  complete Ethernet fixture passes focused connectivity/DRC checks
- `UNBLOCK_CONDITION`: a complete acreage-adapted bridge with zero true
  crossings/shorts/opens, valid references and native DRC evidence

## Corrected copied-island handoff trial — 2026-09-03

Read-only review of the preceding bridge found that its `land` table pointed
to the ESD-side coordinates near x=116–125, while the copied official island
graph actually hands off at the omitted-CM5-source boundary near x=149–151
after the 90 mm translation. The MDI-copy filter also discarded the official
island-side handoff segments at the y=70 boundary. Both generator defects
were corrected in the disposable bridge path.

The corrected run reduced the unconnected count from 78 to **72**, confirming
that the stale handoff coordinates were a real failure cause. Native KiCad
10.0.5 DRC still rejected the candidate at **274 violations / 72 unconnected
items**, including **17 crossings, 1 short, 12 dangling tracks, and 2
dangling vias**. The bridge is rejected; the reduction is diagnostic, not a
Phase 17 pass. The remaining failure is the still-unrouted bridge geometry
to the real handoffs, with ordinary 0.127 mm fixture tracks also conflicting
with the board's 0.200 mm minimum-width rule.

Preserved evidence:
`pisxme/reva-clean/CM5IO_J7_CM5IO_BOUNDARY_FIXTURE-corrected-handoff-drc.rpt`,
`pisxme/reva-clean/CM5IO_J7_CM5IO_BOUNDARY_FIXTURE.kicad_pcb`, and
`pisxme/reva-clean/phase17_j7_cm5io_boundary_fixture.py`.

The goal remains active and recoverable. Phase 18+ remains gated. The next
authorized construction must route to these measured handoff endpoints with
the two approved signal layers and explicit per-pair transitions; no further
experiment may use the stale ESD-side endpoint table.

## Real-handoff layer-transition trial — 2026-09-03

The next bridge construction retained the measured official island-side
handoff segments, changed every long bridge corridor to B.Cu, and added
ordinary through-vias at the handoff/source boundaries. Native KiCad DRC
reduced the disconnected count further to **70**, but rejected the candidate
at **297 violations**, including **17 shorts, 7 crossings, 8 hole/colocation
findings, and 70 unconnected items**.

The new shorting evidence is decisive for the next construction: the official
handoff P/N centers are only about 0.38 mm apart, so 0.50 mm through-vias
cannot be placed directly on both handoff endpoints. A legal transition must
put each pair's ordinary vias in a separated fanout field before the tight
F.Cu handoff, then use short F.Cu dogbones into the retained official graph.
The long B.Cu bridge itself also must be kept clear of the copied F.Cu island
routes. This is a concrete mechanical/routing constraint, not a reason to
reject the official topology.

Preserved evidence:
`pisxme/reva-clean/CM5IO_J7_CM5IO_BOUNDARY_FIXTURE-layerbridge-drc.rpt`.
Phase 17 remains open and Phase 18+ remains gated.

## Direct +5 mm CM5IO alignment fixture — 2026-09-03

The official CM5IO transplant generator was given a direct-alignment mode.
Its complete 189-segment official MDI graph and CM5IO ESD/MagJack geometry
were translated +5 mm, matching the authoritative PiSXMe J7 pad coordinates
without an artificial boundary bridge. This is the first experiment that
tests the native official source legs directly against the production J7
launch.

With support routing deliberately omitted to isolate MDI, native KiCad DRC
reported **202 total violations / 15 unconnected items**, but **zero
`CM5_GBE_*` unconnected items, zero MDI crossings, and zero MDI shorts**.
The remaining unconnected findings are the intentionally omitted center-tap
and ESD-GND support network; 189 official MDI segments are present. The
candidate is therefore a passing focused MDI/source-leg subgate, not a
complete Phase 17 fixture. The existing PCB mapping regression also exposes
the known fixture-only CT-common-versus-ETH_CT1..4 net-authority mismatch,
which must be resolved before promotion.

Preserved evidence:
`pisxme/reva-clean/CM5IO_DIRECT_J7_ETHERNET_FIXTURE-mdi2-drc.rpt`,
`pisxme/reva-clean/CM5IO_DIRECT_J7_ETHERNET_FIXTURE.kicad_pcb`, and
`pisxme/reva-clean/phase17_cm5io_transplant_fixture.py`.

Next authorized action: apply the same +5 mm transform to the complete
support network, retain the exact CM5IO center-tap/ground/shield strategy,
and rerun the full disposable fixture before any acreage promotion.

## Exact EDAC center-tap mapping subgate — 2026-09-03

The direct transplant was rerun with the manufacturer/clean-footprint EDAC
mapping corrected: pads 4 and 5 are NC, and pads 11, 12, 13, and 14 are
`ETH_CT1`, `ETH_CT2`, `ETH_CT3`, and `ETH_CT4`. The native
`test_phase17_ethernet_pcb_mapping.py` regression now passes on the direct
fixture.

With support routing omitted to isolate mapping and MDI, native KiCad DRC
reports **202 violations / 9 unconnected items**, with no MDI crossings,
shorts, or width-independent MDI opens. The nine remaining findings are
support-only (J9/C1/ESD-GND/shield) and are expected from the intentionally
omitted support routes. This closes the exact EDAC pad-mapping subgate but
does not close complete Ethernet support or Phase 17.

The next action is to replace the obsolete common-node support construction
with four individually named center-tap routes/terminations while retaining
the now-passing direct CM5IO MDI topology.

## Full direct CM5IO support transplant — 2026-09-03

The +5 mm direct alignment was applied with the complete existing support
network enabled. The fixture contains the authoritative J7, both official
TPD4EUSB30 ESD footprints, EDAC A70-112-331N126, center-tap bus, shield
return, LED support, and 189 official MDI segments.

Native KiCad 10.0.5 DRC reports **0 unconnected items, 0 shorting items, and
0 track crossings**. It reports 229 total findings, dominated by the
fixture's inherited 0.200 mm minimum-width rule versus the official 0.127 mm
Ethernet geometry, plus footprint/edge/mechanical checks. This closes the
complete direct-transplant connectivity subgate but is not yet a Phase 17
production pass: controlled-impedance rule reconciliation, exact clean
center-tap net mapping (`ETH_CT1..4` rather than the fixture's common support
node), and the acreage mechanical/DRC review remain open.

This result materially changes the blocker: the official CM5IO routing can be
transplanted directly onto PiSXMe's J7 with no artificial boundary bridge.
The next authorized step is to preserve this direct topology, normalize its
support-net authority, and validate the resulting Ethernet island against the
acreage board.

Preserved evidence:
`pisxme/reva-clean/CM5IO_DIRECT_J7_ETHERNET_FIXTURE-full-drc.rpt`,
`pisxme/reva-clean/CM5IO_DIRECT_J7_ETHERNET_FIXTURE.kicad_pcb`, and
`pisxme/reva-clean/phase17_cm5io_transplant_fixture.py`.

## Separated-fanout bridge trial — 2026-09-03

The direct-via failure was addressed with separated 1 mm fanout pairs before
the tight official handoffs. Long bridge corridors were split between F.Cu
and B.Cu, with ordinary source-boundary transitions and short F.Cu dogbones
from the fanout field into the retained CM5IO graph.

Native KiCad 10.0.5 DRC still rejected the candidate at **288 violations / 70
unconnected items**, including **23 crossings, 10 shorts, 8 co-located-hole
findings, 6 solder-mask bridges, 8 dangling tracks, and 4 dangling vias**.
The fanout spacing removed the prior direct-handoff via-short class, but the
two-layer bridge still intersects itself and the copied official F.Cu graph.
This candidate is rejected.

Preserved evidence:
`pisxme/reva-clean/CM5IO_J7_CM5IO_BOUNDARY_FIXTURE-fanout-drc.rpt`.
The next experiment must retain separated fanout vias while making the
F.Cu dogbones pair-specific and monotonic at the island boundary; no direct
via placement on the 0.38 mm official pair centers is permitted.

## Round-the-envelope bridge trial — 2026-09-03

The proposed round-the-envelope bridge was implemented and run under native
KiCad 10.0.5 DRC. It reduced the prior remote-island result to **248
violations / 78 unconnected items**, but still contains **5 track crossings**,
**16 dangling bridge tracks**, and 10 board-edge-clearance violations. The
crossings are in the long boundary-to-island corridors; the unconnected and
dangling items show that the bridge endpoints do not form a complete
electrical path. This is rejected as a production candidate.

The fixture remains useful evidence: the official CM5IO-derived ESD,
MagJack, support network, and internal island were not the source of the new
failures. The failure is confined to the newly authored bridge construction
between the proven J7 launch boundary and the remote island. The negative
result is therefore a recoverable placement/escape blocker, not a reason to
reject the CM5IO Ethernet architecture.

Preserved evidence:
`pisxme/reva-clean/CM5IO_J7_CM5IO_BOUNDARY_FIXTURE.kicad_pcb`,
`pisxme/reva-clean/CM5IO_J7_CM5IO_BOUNDARY_FIXTURE-round-drc.rpt`, and
`pisxme/reva-clean/phase17_j7_cm5io_boundary_fixture.py`.

Current state: **PISXME_REVA_CLEAN_BLOCKED** at Phase 17 Ethernet routing;
Phase 18+ remains gated. The next practical continuation is a fresh
pair-specific bridge generated from the actual launch-boundary endpoint
coordinates, with a legal expanded fixture outline and per-pair lanes that
are checked for crossings before native DRC. No clean production
PCB/schematic has been promoted.

## Corrected source-transition RC trial — 2026-09-03

The latest disposable fixture used the manufacturer-authoritative four
`22 nF + 75 ohm` center-tap branches, explicit off-pad source/capacitor vias,
and ordinary F.Cu/B.Cu transitions. Native KiCad DRC rejected it at **311
findings / 2 unconnected items**, with CT branch shorts/crossings and a
shield-return discontinuity. This candidate is rejected; the EDAC electrical
authority remains valid and production remains unchanged.

## Current Phase 17 status — 2026-09-03

The corrected reordered EDAC support-island fixture is no longer electrically
blocked. It implements the authoritative `ETH_CT1..4 -> 22 nF -> 75 ohm ->
common -> 1 nF/2 kV -> shield` topology. Native KiCad 10.0.5 DRC reports 235
findings, zero unconnected pads, and no `tracks_crossing`, `shorting_items`,
or `unconnected_items` categories. The mapping, hierarchy-authority, and new
fixture regression tests pass.

This closes the disposable exact-support subgate, not Phase 17 itself. The
remaining gate is acreage adaptation: promote this proven support geometry,
rerun affected Phase 11/12 review, complete production Ethernet routing, and
re-run the full Phase 17 evidence set. Phase 18+ remains gated and no clean
production PCB/schematic has been promoted in this experiment.

## Rejected acreage integration trial — 2026-09-03

Applying the validated MDI island to the current `ACREAGE_EDAC_CORRECTED_PHASE17`
base was rejected: native KiCad DRC reported 435 findings and 453
unconnected items. This is an invalid/incomplete acreage integration base,
not evidence against the passing disposable Ethernet fixture. The generated
candidate is retained as negative evidence only; the next authorized action
is to select the last valid Phase 16 acreage checkpoint, then apply the exact
CM5IO MDI plus EDAC RC support island there and rerun the Phase 11/12 and
Phase 17 gates.

## Authorized local reopening experiments — 2026-09-04

Three disposable in-scope trials were run from `ACREAGE_PCIE_PHASE16`:

- coherent U3 regulator-island translation down 30 mm: rejected at 918
  findings / 265 unconnected items;
- coherent U3 regulator-island translation left 30 mm with its local copper:
  rejected at 896 findings / 262 unconnected items;
- Ethernet-local CT support translation right 40 mm with staggered source
  escapes: rejected by CT source-launch shorts/crossings in the fixture.

The exact fixture was then regenerated without experiment variables and
revalidated at 237 findings, zero unconnected pads, zero shorts, and zero
track crossings; mapping and fixture regressions pass. These results show
that the proven Ethernet island remains sound and that a single local
translation does not clear the combined corridor. The next escalation is a
coherent local regulator/support-area move with complete Phase 15 copper
re-authoring, followed by Phase 15/16 revalidation; no production promotion
has occurred.

## Frozen-boundary conflict after official-oracle promotion — 2026-09-03

The correct Phase 16 ancestor was tested with the passing CM5IO-derived
Ethernet geometry at the shared J7 datum. The electrical fixture remains
closed, but the acreage overlay is rejected because the frozen regulator and
power copper occupies the official compact Ethernet corridor. Representative
native DRC evidence includes `FB_CM5_5V` crossing the EDAC MDI launch and
`FUSED_12V_A` crossing the CT support island; the overlay reports 906 total
findings and 263 unconnected items. This is a placement-boundary conflict,
not an Ethernet architecture failure.

The smallest bounded choices are:

1. Reopen Phase 11/12 for a local regulator-island translation sufficient to
   clear the official Ethernet corridor, then rerun the affected Phase 15/16
   checks.
2. Reopen Phase 11/12 for a larger Ethernet-local bridge/island adaptation,
   accepting another complete routing proof attempt; prior bridge classes
   have already failed, so this is higher risk.
3. Keep the frozen placement and accept that Phase 17 cannot close under the
   current plan constraints.

No production PCB/schematic has been promoted. The first option is the
recommended smallest architectural change, but it moves frozen non-Ethernet
regulator geometry and therefore requires explicit user authorization.

The Phase 16 ancestor independently passes
`validation/phase3/test_phase16_pcie_route.py`. Its recorded DRC baseline is
92 findings plus 241 expected unconnected pads; the Ethernet overlay rises to
906 findings plus 263 unconnected pads and introduces Ethernet-related
shorts/copper conflicts. This confirms the overlay failure is an integration
delta, not a regression of the Phase 16 PCIe gate.

The acreage apply path was also corrected to refill GND zones after replacing
through-hole Ethernet footprints. A fresh Phase 16 overlay with refilled
zones still fails at 820 findings / 271 unconnected items, confirming that
zone staleness was not the root cause. A coherent U3-left-30 mm trial with
refill improved to 778 findings / 270 unconnected items but retained power
and Ethernet conflicts, so it is rejected as insufficient.

An additional coherent U3-right-70 mm trial was tested after the refill-path
correction. It reduced the report to 869 findings but increased the ancestor
connectivity debt to 291 unconnected items and was rejected. A support-island
translation to the left also retained CT launch shorts/crossings. The exact
compact CM5IO fixture was restored and revalidated at 237 findings with zero
unconnected pads, shorts, or crossings.

The authorized widened trials are now complete for this repair wave. The
right-70 mm U3 move and left/right Ethernet-support alternatives do not clear
the combined obstruction without either reauthoring the adjacent power-input
fuse corridor or inventing another long Ethernet bridge. The latter has
already failed as a solution class. The exact CM5IO/EDAC fixture remains the
selected electrical authority; no production promotion or Phase 18 work has
started.

## Current blocker — F1-only power-entry reopening exhausted — 2026-09-04

The first authorized power-entry repair was executed from the validated
`ACREAGE_PCIE_PHASE16.kicad_pcb` ancestor. A disposable harness moved only
the coherent F1 fuse footprint and its directly attached high-current copper,
preserving the dual-12-V concept, both fuse nets, the protected-load trunk,
and the proven CM5IO Ethernet island. Three targets were tested:

| Trial | F1 target | Native DRC disposition |
| --- | ---: | --- |
| `ACREAGE_PHASE17_F1_left_ETHERNET` | (20,40) mm | REJECTED: genuine Ethernet/U3 shorts and unconnected items |
| `ACREAGE_PHASE17_F1_leftlow_ETHERNET` | (20,60) mm | REJECTED: same U3/CM5-5V feedback collision class |
| `ACREAGE_PHASE17_F1_upper_ETHERNET` | (100,20) mm | REJECTED: same U3/CM5-5V feedback collision class |

Moving F1 removes the original `FUSED_12V_A`/CT-support body overlap, but does
not remove the dominant obstruction: the fixed Ethernet MDI launch and
return-via field still intersects adjacent U3 `CM5_5V`/`FB_CM5_5V` support
geometry. Native DRC reports real shorts involving `CM5_GBE_TD0_N`,
`CM5_GBE_TD1_P`, `CM5_GBE_TD3_N`, `/REGULATORS/FB_CM5_5V`, and `POWER_GND`,
plus connectivity debt. This is not stale zone fill; the isolated exact
CM5IO/EDAC fixture still passes its zero-short/zero-crossing/zero-open
subgate.

The consultant unblocker was invoked as required but did not return within
bounded 10-second and 60-second waits. Consultant availability is not being
used as an engineering conclusion. Local evidence identifies the remaining
blocker: the F1-only repair class is insufficient. Phase 17 remains open and
Phase 18+ remains gated.

Smallest practical continuation options:

1. Re-author and move the complete U3 regulator island together with the
   relocated F1/protection corridor, including all local copper, then rerun
   Phase 15/16 and the full Phase 17 gate. Recommended; this requires a
   complete regulator-copper proof, not a footprint-only translation.
2. Move the complete proven Ethernet island to open acreage and re-prove the
   J7-to-island launch under the same stack/layer contract.
3. If neither coherent path clears the collision, request a decision on the
   smallest major floorplan change. No architecture, layer, stack, PCIe,
   CM5, V100/SXM2, or Ethernet electrical change has been made.

`phase17_move_f1_trial.py` and the three disposable board/report artifacts
are retained as reproducible negative evidence. No clean PCB/schematic was
modified or promoted.

## Follow-up combined repair evidence — 2026-09-04

To test whether the F1 relocation could be combined with the previously
authorized U3-local reopening, four disposable combined variants were run:

- F1 at (20,40) mm plus U3 translated down 50 mm: rejected for real track
  crossings and missing connections.
- F1 at (20,40) mm plus U3 translated right 60 mm: rejected for regulator/
  core-PCIe shorts and track crossings.
- F1 at (20,40) mm plus U3 translated right 80 mm: rejected for
  `POWER_GND`/core-PCIe shorts and track crossings.
- F1 at (20,40) mm plus U3 translated right 60 mm/down 30 mm: rejected for
  power-ground, protected-input, and feedback-net shorts plus crossings.

These are diagnostic footprint/copper translations, not production
promotions. They show that the next valid experiment must move the complete
U3 island as a re-authored electrical block: regulator, all local passives,
all vendor-reference local copper, and explicit boundary reconnections for
`12V_PROTECTED`, `POWER_GND`, `CM5_5V`, feedback, PG, and RT. A footprint-only
translation cannot satisfy the Phase 15/17 gates. PCIe, CM5, V100/SXM2,
Ethernet topology, stack, and layer contract remain unchanged.

The goal is therefore still recoverable within the user-authorized local
reopening, but Phase 17 is not closed. The recommended next experiment is a
complete U3 island re-authoring on the F1-cleared ancestor, followed by native
DRC and Phase 15/16 regression before Ethernet promotion.

## Complete-island translation diagnostic — 2026-09-04

A further disposable trial translated the complete U3 footprint set and all
local regulator-net copper by (+48,+82) mm, placing the island near (100,160)
mm, below the V100 mechanical envelope and away from the Ethernet launch. In
combination with F1 at (20,40) mm, native DRC found no `shorting_items`,
confirming that a complete coherent island move can remove the former
U3/Ethernet short class. The candidate still failed with two
`tracks_crossing` findings and 271 unconnected pads, including Ethernet J7,
ESD, and MagJack handoff opens. It is diagnostic only, not a Phase 17 pass.

This narrows the remaining implementation work to proper boundary
re-authoring: preserve the transformed U3 vendor-layout island, explicitly
reconnect every external power/control boundary, and repair the exact J7
handoff in the acreage apply path. No architecture or frozen major subsystem
has been changed. The next credible in-scope trial is this complete boundary
re-authoring, followed by native DRC and Phase 15/16 regression.

## Consultant unblocker synthesis — 2026-09-04

The required read-only consultant review confirms that the accepted U3 block
is `U3 + C5-C9 + R3-R6`, including thermal PGND vias, VOUT-land tie, VIN/
VOUT edge escapes, and FB/RT/PG copper. Its required explicit boundaries are
`12V_PROTECTED`, `POWER_GND`, `CM5_5V`, `FB_CM5_5V`, `RT_CM5_5V`, and
`PG_CM5_5V`; `VCC_U3_INTERNAL` must remain isolated. The consultant’s
recommended path is complete U3 re-authoring from Phase 15 authority, not
another translation, with exact net-object assignment and explicit boundary
ports, followed by Phase 15/16 and Phase 17 validation.

That recommendation is accepted as the next implementation path. The
consultant returned `PROPOSED_UNBLOCK`; it did not authorize relaxing any
gate or changing the architecture. A second read-only KiCad review was
invoked but returned no result before the bounded run ended; no conclusion is
attributed to it.

## Ethernet overlay serialization fix and rerun — 2026-09-04

The acreage apply script contained a generic KiCad 10 Python/SWIG defect: its
`PCB_TRACK(item)` copy constructor produced zeroed segment geometry when
copying the exact Ethernet fixture into another board. This was corrected by
recording scalar segment/via geometry and explicitly reconstructing each
destination item. The fix is generic and does not hand-edit PiSXMe.

Rerunning the F1-cleared, complete-U3-bottom diagnostic with the corrected
authoring path produced 576 real tracks, including 26 `CM5_GBE_TD2_P`
segments, and reduced DRC unconnected debt from 271 to 222. The former
U3/Ethernet short class is absent. The candidate nevertheless remains
rejected: native DRC reports real Ethernet CT1/CT2 crossings, J7 launch
clearance violations, power-entry/fuse hole-clearance violations, two
CM5_5V/CM5_PERST crossings at the relocated island, and the remaining
baseline board connectivity debt. The isolated CM5IO fixture still passes at
237 findings with no crossing, shorting, or unconnected-item categories.

This closes the malformed-overlay hypothesis but not Phase 17. The next
authorized trial must correct the complete acreage boundary/placement path,
including CT support launch and the F1 service-clearance location, while
preserving the exact CM5IO electrical topology and the Phase 16 ancestor.
