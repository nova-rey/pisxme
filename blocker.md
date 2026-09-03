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

- Latest native KiCad DRC candidate: `pisxme/reva-clean/ACREAGE_ETHERNET_PHASE17-drc10.rpt`
- Latest candidate report: 319 total violations, including existing acreage
  debt.
- Representative Ethernet failures include CM5 pair crossings at J7,
  pair shorts near U6/U9, crossings against existing power/regulator tracks,
  NPTH hole-clearance violations at J7/F2/J2, and ESD pad-field clearance
  violations.
- Tested variants included perimeter routing, separated B.Cu corridors,
  via-in-pad transitions, and compact ESD placements. None passed the Phase 17
  gate.
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
