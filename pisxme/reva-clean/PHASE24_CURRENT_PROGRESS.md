# PiSXMe Rev A Clean — current progress checkpoint

## Current checkpoint — coherent generator grid path isolated — 2026-09-11

The generic `phase3_scaffold.py` authoring path now emits 2.54 mm contract
pitch and native-grid sheet anchors/connection stubs. A fresh disposable
native KiCad hierarchy generated from that path reports 9 off-grid findings,
but 59 disconnected pins remain because legacy direct-root links were not
transformed to the new sheet coordinate map. This is not promoted production
authority. The next implementation target is to transform those links by
the same coordinate map, then rerun native hierarchy/ERC and netlist
comparison. The canonical clean source and its 872-warning report remain
unchanged.

## Current checkpoint — hierarchy grid discriminator classified — 2026-09-11

The disposable native KiCad grid probe did not justify a production
coordinate rewrite. A broad root-graph snap increased ERC findings from the
canonical 872 warnings to 1132 by detaching hierarchy-associated geometry.
A child-contract-only snap, with the root graph preserved, produced 946
findings and 56 `pin_not_connected` results because the embedded contract
symbol still used its original 3 mm pin pitch. These are route/authoring
experiment results, not production-board changes.

The discriminator closes the narrow hypothesis that labels or wires can be
snapped independently. Any repair must regenerate the contract symbol pin
geometry, child labels/wires, and parent sheet pins/wires as one coherent
native-grid authoring path, then compare hierarchy connectivity and netlist
before promotion. The canonical schematic and its 872-warning report remain
unchanged; the Phase 24 ERC gate remains open and unwaived.

## Current checkpoint — canonical storage-library namespace repaired — 2026-09-11

The canonical `PiSXMe_RevA_Clean_complete.kicad_sym` now contains the eight
storage definitions embedded by `STORAGE.kicad_sch`, added by the auditable
`phase24_reconcile_storage_library.py` path. Existing canonical symbol
definitions were preserved; the earlier broad rebuild that replaced an
unrelated Ethernet-contract variant was discarded. Native KiCad ERC now
reports zero `lib_symbol_issues` and zero missing-library-symbol messages.
The remaining report is now 872 warnings (0 errors), after qualifying the 20
storage passive/crystal footprint references against the registered local
library. It consists of existing off-grid, isolated-label, endpoint, naming,
no-connect, and power/Ethernet symbol-mismatch findings; the footprint-link
class is absent. These remain open authority work; no severity was waived.
Storage library package audit passes, and Path-B routing/support work
continues from the accepted candidate.

Receipts: `PHASE24_CLEAN_SCHEMATIC_ERC_LIBRARY_REPAIRED.rpt` and
`PHASE24_CLEAN_SCHEMATIC_ERC_FOOTPRINTS_REPAIRED.rpt`.

## Current checkpoint — local QFN exception integrated — 2026-09-10

The accepted RTL9210B orientation and V1603 downstream launch are unchanged.
The six U1 high-speed departures now use the authorized local 0.15 mm
trace/clearance exception, returning immediately to the normal 0.20 mm
board routing. Existing ordinary 0.60/0.30 mm through-vias were retained.
Native integrated DRC is 0/0/0, and the saved-board six-net audit plus six
trace-removal negative controls pass. The corrected standalone fixture also
passes native DRC and its physical scope/connectivity audit. Fine-breakout
implementation is closed; overall Phase 24 remains open for the independent
Path-B and full-board gates.

## Current next action — corrected ISOLATEB support authority — 2026-09-11

An open-acreage U3 support candidate was evaluated using the accepted U1/V1603
baseline. It has complete native connectivity (0 unconnected items) and 20
native DRC findings. The remaining failures are identifiable physical
corridor crossings/local-rule receipts; it is not promoted, but is the best
current disposable integration basis.

With the candidate-local QFN rule applied, the same saved candidate reports 11
native DRC violations and 1 unconnected item. The rule removes only the
authorized local 0.15-mm width/clearance accounting; the remaining findings
are real corridor crossings and one board-GND transition.

After adding the real board-GND continuation and removing two redundant
single-layer vias, the candidate reports 10 native DRC violations and 0
unconnected items. All remaining findings are explicit same-layer corridor
crossings.

The latest coherent outboard U3 relocation trial is rejected at 31 native DRC
violations and 2 unconnected items, improving the prior 38/3 trial. Remaining
failures are localized to occupied B.Cu corridors and two local ground joins;
this is disposable route evidence, not a change to the frozen RTL9210B/V1603
authority.

The subsequent local ground-spine repair, including an outboard B.Cu perimeter
return to the existing board-GND transition at (115.6,78.0), improved the same
candidate to 24 native DRC violations and 0 unconnected items. The remaining
findings are physical corridor/clearance issues; this remains disposable
implementation evidence.

The latest real-pad full-board support attempt is rejected at 38 native DRC
violations and 3 unconnected items. It improved the prior 6-open result but
still crosses occupied SPI/control/power corridors. This is route-implementation
evidence only; the next bounded repair is coherent local support-island
translation, with U1 orientation and V1603 launch frozen.

The MIC2545A fixture correction is complete: U3.2/FLG is netless rather than
incorrectly tied to GND. Native DRC, physical duplicated-pin joins, negative
control, and DFM pass. The prior combined-placement trial is rejected. The
latest full-board overlay reports 37 native DRC violations and 6 unconnected
items; the preceding overlay reported 36 violations and 6 opens. Neither is
production authority. Build one fresh co-routed U1.12-to-U3.1 support candidate
next, retaining the frozen
RTL9210B orientation, local QFN rule, and V1603 launch.

The disposable combined U1/MIC2545A fixture now passes native KiCad DRC
0/0/0 and its saved-board audit: U1.12→U3.1, IN 5/7, OUT 6/8, rail, ILIM,
and ground ownership are physically connected; U3.2/FLG is netless; and the
ISOLATEB trace-removal negative control fails as required. This is a geometry
and authority proof only; full-board promotion remains the next gate.

## Safe pause / GitHub checkpoint — 2026-09-10

The active RTL9210B Path-B routing work is paused at the validated local
support/launch checkpoint. No route search is running. The latest committed
checkpoint is `21a3002c` (`phase24: record MIC2545A support pin authority`).
The accepted orientation remains U1 RTL9210B-CG, 0 degrees, top side, pin 1
southwest, V1517 lineage; orientation search is closed.

The current isolated candidate is
`PHASE24_RTL9210B_PATHB_V1603_V1517_INTEGRATED.kicad_pcb` (generated from the
V1523 support baseline). Native KiCad DRC reports 0 violations, 0
unconnected items, and 0 footprint errors. The saved-board six-net audit
passes all six U1-to-J1 high-speed mappings and six actual-trace-removal
negative controls. The route-policy metrics are in
`PHASE24_RTL9210B_PATHB_V1603_METRICS.json`.

This is an isolated Path-B implementation checkpoint, not Phase 24 closure.
Open gates are full Path-B authority/procurement/firmware/bring-up,
production parity, acreage integration, and the remaining Phase 24 native
validation. Path A remains preserved. Historical disposable experiments are
not current routing authority.

Resume from `21a3002c`. The next productive action is a corrected disposable
MIC2545A support fixture: both duplicated `IN` pins and both duplicated `OUT`
pins must be physically joined, with native connectivity and a negative
control. The authoritative pin correction is recorded in
`authority-inventory/rtl9210b/MIC2545A_ISOLATEB_SUPPORT_AUTHORITY.md`.
Do not reopen U1 orientation or revive rejected route bases.

## Post-pause audit — 2026-09-10

The saved-board census `phase24_rtl9210b_pathb_census.py` passes against the
actual pads, tracks, vias, and zones: all asserted U1/J1 net identities and
six endpoint connections pass, six actual-trace-removal negative controls
fail as required, and no legacy `PiSXMe:` namespace is present. The current
native DRC receipt reports 0 violations, 0 unconnected pads, and 0 footprint
errors. This strengthens the isolated Path-B CAD gate only; it does not close
firmware, procurement, production parity, acreage integration, or full Phase
24 validation.

The corrected local RTL9210B QFN land pattern also passes
`phase24_rtl9210b_landpattern_audit.py`: 69 SMD/F.Cu pads, GND exposed pad
69 at 4.8 x 4.8 mm, and no `through_hole` metadata in the source module.
This is isolated CAD/DFM evidence; traceable production land-pattern
confirmation remains open.

## Generator transition correction — 2026-09-10

The layer-transition audit found one real RTL_3V3 B.Cu/F.Cu handoff in the
V1523 baseline without a via at (99.6, 66.05). The generator was corrected
to remove that adjacent-QFN stub and place the through-via at (99.6, 66.8),
outside the USB_DM/RTL_1V1 pad envelope. Regenerated native DRC is 0
violations, 0 unconnected pads, and 0 footprint errors; the layer-transition
audit reports zero un-viaed handoffs. Endpoint connectivity and all six
negative controls remain passing. This is a local implementation correction,
not an orientation or architecture change.

## MIC2545A support fixture — 2026-09-10

The disposable `PHASE24_MIC2545A_SUPPORT_FIXTURE.kicad_pcb` now passes native
KiCad DRC with zero violations, zero unconnected pads, and zero footprint
errors. Its saved-board audit proves physical duplicated-pin joins for
MIC2545A `IN` 5/7 and `OUT` 6/8, and its trace-removal negative control passes.
Its 1.27-mm pitch, 5.40-mm row spacing, and 1.55×0.60-mm pads match
Microchip's current recommended 3BX SOIC land pattern; mask/paste/courtyard
DFM geometry is now authored explicitly, but final assembly-house review and
production RTL9210B integration remain open. Receipt:
`PHASE24_MIC2545A_SUPPORT_FIXTURE_RECEIPT.md`.

The independent `phase24_mic2545a_dfm_audit.py` now passes against the saved
PCB: all eight pads are SMD/F.Cu with 1.55×0.60-mm dimensions, 1.27-mm pitch,
5.40-mm row spacing, explicit mask/paste settings, and present courtyard and
silkscreen graphics. This closes the disposable footprint geometry audit;
assembly-house review and production integration remain open.

The first MIC2545A-to-Path-B integration trial is rejected as
`REJECTED_ROUTE_IMPLEMENTATION`: native DRC found 22 violations and 4 opens
from the attempted U1.12 and SSD_3V3 corridor geometry. It does not invalidate
the corrected support circuit or frozen V1517/V1603 baseline. Receipt:
`PHASE24_MIC2545A_INTEGRATION_TRIAL_REJECT.md`.

Native pad inspection records the specific next escape class in
`PHASE24_RTL9210B_ISOLATEB_ESCAPE_ANALYSIS.md`: U1.12 is in a 0.4-mm-pitch
0.2×0.9-mm pad row, so lateral escape is not legal at the current route
width/clearance. The next repair must use a pad-end vertical escape and an
outboard ordinary via before attaching the local support network.

The first shifted-corridor source-escape probe is also rejected as a route
implementation: native DRC found 17 violations, specifically crossings into
PEDET/PERST_N and via/ground-zone clearance conflicts. Its raw board/report
are preserved with the escape analysis; no copper from either probe is
promoted.

The latest opposite-side jog reduces the isolated escape probe to two native
crossings, specifically the existing `RTL_5V` and `PERST_N` pad-row
departures. The next in-scope repair is a coordinated local reroute of those
adjacent departures around U1.12; no new MIC2545A topology or RTL9210B
orientation search is warranted.

The left-dogbone escape variant also fails native DRC with four violations
(PEDET via collision, CLKREQ_N crossing, and JTAG_TDO/pad-row clearance).
Simple ISOLATEB escape variants are exhausted; the next repair is coordinated
source-row rerouting or a bounded local support relocation.

The canonical blocker packet for this recoverable routing issue is
`PHASE24_RTL9210B_ISOLATEB_UNBLOCKER_PACKET.md`. The custom unblocker agent
was unavailable because the agent-thread limit was reached; local blocker
analysis was performed instead. The next bounded implementation is a
co-routed U1 south-row repair or, if that is not viable, relocation of only
the nearest support/via field. No orientation or architecture decision is
being reopened, and no rejected probe copper is authority.

The first relocation-class probe is also rejected as
`REJECTED_ROUTE_IMPLEMENTATION`: `PHASE24_RTL9210B_MIC2545A_SUPPORT_RELOCATED.kicad_pcb`
has 26 native DRC violations and 5 unconnected items. It confirms that
moving MIC2545A alone, without co-planning U1 south-row departures and the
existing PEDET/power corridors, is insufficient. The next attempt must use
one physical channel plan for those handoffs; orientation and architecture
remain closed.

The staggered source-row funnel probe is preserved as
`PHASE24_RTL9210B_SOURCE_ROW_STAGGERED_FUNNEL.md`. Its reserved 1.0-mm via
rows and parallel B.Cu handoffs are separated, but native DRC still reports
two real adjacent-U1 pad-end clearance violations (9 total fixture findings,
4 intentional remote opens). This narrows the remaining capacity problem to
the first QFN handoff; the next production-worthy repair must re-author that
handoff geometry or use an explicitly approved finer local escape rule.

The directional variant of the same funnel (ISOLATEB west, neighboring
controls east) was also rejected: native DRC found 11 findings, including
four U1 pad-clearance violations. The downstream channels remain separable;
the remaining blocker is specifically the frozen 0.4-mm QFN source handoff
under the production 0.20-mm trace/clearance envelope.

The authorized local exception has now been implemented in
`PHASE24_RTL9210B_FINE_QFN_ESCAPE_FIXTURE.kicad_pcb`: native DRC is 0/0/0,
all five source-to-handoff connections and five actual trace-removal
negative controls pass, and the scope guard proves 0.15-mm geometry is
confined to the QFN window with 0.20-mm handoff tracks. The receipt records
the selected rule and the earlier DFM rejection as superseded historical
evidence. Apply this proven primitive to the integrated support field next;
do not alter U1 orientation or V1603.

The first coordinated local reroute of U1.12 `ISOLATEB`, `CLKREQ_N`,
`PERST_N`, and `RTL_5V` is rejected: native DRC found 12 violations and zero
opens. The exact conflicts are recorded in
`PHASE24_RTL9210B_LOCAL_DEPARTURE_REPAIR.md`; the accepted baseline remains
untouched.

## Support parity consolidation — 2026-09-10

Claude's bounded review identified the missing consolidated support audit.
The new native audit passes 14 mapped support groups against actual saved-
board connectivity. The integrated candidate now restores the V12 `TP6`
endpoint for `RESET_N`; only `ISOLATEB` and `PERST_N` remain boundary/control
findings. Receipt:
`PHASE24_RTL9210B_PATHB_SUPPORT_PARITY_RECEIPT.md`.

The retained RTL9210B reference XML narrows `ISOLATEB` to a documented
corroborating pattern: U1.12 enables a MIC2545A-1YM SSD high-side switch.
This is recorded in `RTL9210B_ISOLATEB_CORROBORATION.md`; it remains a
candidate until PiSXMe rail/inrush/fault authority is reconciled.

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

`PHASE24_STATUS.md` now has a current-state override documenting this clean
V1603/V1523 candidate; older V1517/V1583 prose remains historical evidence.

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

## CURRENT PATH-B SUPPORT CANDIDATE — 2026-09-11

The disposable open-acreage MIC2545A support candidate now has native KiCad
DRC 0 violations and 0 unconnected items. The remaining QFN source handoff
uses the authorized local exception: 0.15 mm immediate escape geometry and a
single local 0.40/0.20 mm ordinary through-via for `CLKREQ_N`; normal board
geometry remains 0.20 mm trace/clearance and 0.60/0.30 mm vias. The candidate
sidecar rule records the local via exception; it does not change validation
severity or global board rules.

Saved-board support connectivity passes for U3/MIC2545A, R15, C18, the U1
`ISOLATEB` handoff, both switched-output pins, and the existing J1 rail. Two
actual trace-removal negative controls pass; GND is independently retained by
the filled-zone connection and is audited as such. This is an integrated
Path-B candidate checkpoint, not Phase 24 closure: schematic parity, full
support-field authority, production integration, and broader Phase 24 gates
remain OPEN.
