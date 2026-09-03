# PiSXMe Rev A Clean — Blocker Report

## Final state

`PISXME_REVA_CLEAN_BLOCKED`

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

The generator was then aligned to the corrected TI pad coordinates and rerun.
That endpoint-corrected candidate reports **104 native DRC violations and 7
unconnected items**. It is also rejected. The reduced dangling count confirms
the footprint/endpoints are now being exercised, while the remaining defects
are genuine route crossings/shorts and connector-launch geometry failures.
