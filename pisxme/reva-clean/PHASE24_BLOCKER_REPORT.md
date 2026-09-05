# Phase 24 outboard return-row rejection

The isolated global-return trials are rejected. A C14–C19 horizontal chain
produced three shorts and two crossings; narrowing the experiment to adjacent
C14–C15 still produced two native shorts. Neither candidate changes the
active design or validation severity.

The earlier J1 ground-column candidate was tested against the current
cumulative basis and rejected at 217 native violations, 122 unconnected
records, one short, and two crossings. This is a composition-coordinate
failure, not evidence against the earlier isolated J1 result.

The U5 exposed-ground stitch was rejected on the cumulative board. The full
field candidate reports 210 violations, 117 unconnected records, and one
native `POWER_GND`/`BRIDGE_1V1` short. Single-segment discriminators reproduce
the same short class, so this is not a missing-U5-audit issue; the corrected
audit and its negative control remain passing on their dedicated fixture.

# Phase 24 same-row collector continuation

`PHASE24_CM5_GROUND_RIGHT_SAME_ROWS.kicad_pcb` was regenerated from the
accepted right-outer collector. It adds only F.Cu same-row ground bridges
between the two lower-right J7 ground banks (y=109.5–117.9). Fresh native
KiCad DRC reports 209 violations, 122 unconnected records, zero
`[shorting_items]`, and zero `[tracks_crossing]` records when the complete
report is counted. The candidate is accepted as the current working basis;
the remaining Phase 24 census is still open and no validation severity was
changed.

The dedicated In1 CM5-ground plane-attachment experiment is rejected. A
corrected ordinary via at the accepted outer collector plus a distinct
`/CORE_CM5/POWER_GND` inner-layer zone produced 210 native violations and
122 unconnected records, with zero shorts/crossings and no connectivity gain.
The via/zone was not promoted; the 209/122/0/0 same-row collector remains the
working basis.

The upper outer-escape candidate is rejected at 215 native violations, 118
unconnected records, two shorts, and three crossings. The failure is a real
upper Ethernet-launch collision, not a parser or severity issue. Specialist
geometry review measured the preserved lane spacing as below the clearance
needed by an ordinary 0.50/0.30 mm via, so further same-class upper F.Cu
collector variants are not justified.

# PiSXMe Rev A Clean — Phase 24 blocker report

Status: `PHASE24_IN_PROGRESS` (recoverable implementation blocker)

## Exact gate

Schematic↔PCB component authority parity is not closed. Native KiCad 10.0.5
schematic ERC at error severity is clean and the native netlist exports without
annotation warnings, but the accepted acreage PCB ancestor is missing the
schematic-authoritative storage clock parts `Y1`, `R23`, `C42`, `C43` and the
regulator support parts `C44`–`C47`.

## Current evidence

- `PHASE24_NATIVE_ERC_FINAL2.rpt`: `Found 0 violations` at `--severity-error`.
- `PHASE24_NETLIST_FINAL5.xml`: warning-free native export.
- `PHASE23_TEST_DEBUG_PADS_V5.kicad_pcb` remains the accepted acreage ancestor.
- The relocated storage donor was rejected because its USB3 corridor crosses
  the Phase 16 PCIe corridor after merge.
- The new coordinate-derived `PHASE24_SUPPORT_V2.kicad_pcb` was rejected by
  native DRC: `234` violations and `409` unconnected items, including new
  clock `tracks_crossing` and `shorting_items`.

## Root cause and continuation

The attempted common B.Cu clock surface is incompatible with the actual U7 pad
field and inherited SATA/USB launches. This is not evidence against the storage
architecture. The active next class is a layer-separated, obstacle-aware clock
fanout derived from actual U7 pad coordinates, followed by a separate coherent
U5 rail/return capacitor island.

Bounded options are: (1) retain U7/J3 and regenerate only the clock fanout with
F.Cu dogbones and ordinary vias outside the U7 field (preferred); (2) reopen
the storage island and regenerate USB3/SATA/clock together around PCIe; or (3)
consider a new support architecture only if both in-scope routing classes fail.
No Phase 25 freeze or READY claim is made.

## Follow-up discriminator

The rotated-U7 probe was rejected as a proof artifact. Its generator rotated
the footprint but retained a hard-coded pre-rotation clock endpoint graph, so
native DRC correctly found mismatches at unrelated U7 pads. This does not
invalidate U7 rotation as an in-scope option. A valid next experiment must
derive both the rotated U7 clock pads and every support pad from the serialized
post-rotation footprints before generating copper.

## New source-escape oracle

The corrected rotated-U7 source-escape discriminator in
`phase24_storage_rot90_probe.py` derives post-rotation U7 endpoints before
authoring copper. Its native DRC report records zero `shorting_items` and zero
`tracks_crossing` for the clock escape. It remains disposable because the
support-passive branches and U5 C44-C47 island are not yet complete.

## Spread-support experiment (rejected)

The completed Y1/R23/C42/C43 acreage-spread fanout was run through native
KiCad 10.0.5 DRC as `PHASE24_STORAGE_ROT90_PROBE-spread-drc.rpt`.
It produced `229` violations, including three genuine `tracks_crossing`
records between XI, XO, and VSSOSC. The underlying rotated-U7 source escape
remained free of `shorting_items`; the failure is confined to the newly added
passive branch geometry. The experiment is rejected and is not production
authority. Next repair remains layer-separated passive fanout with explicit
via/layer ownership, followed by the missing U5 C44-C47 island.

## U5 capacitor-island experiments (rejected)

The first C44-C47 materialization placed the four schematic-authoritative
1210 capacitors near the U5 region, but native DRC found new shorts against
the existing `/REGULATORS/RT_BRIDGE_3V3` corridor and new crossings. A
second outboard translation was run as `PHASE24_U5_CAPS_ISLAND-outboard-drc.rpt`;
it still found two true shorts involving inherited feedback/ground geometry
and two crossings involving the existing PG corridor. Both experiments are
rejected. The component parity gap remains real, and the next attempt must
select a clear rail/return corridor relative to actual U5/feedback/PG pads,
not merely translate the same fanout.

## U5 capacitor-island topology pass

## U5 input-power field stitch (accepted targeted evidence)

The disposable `PHASE24_U5_INPUT_POWER_STITCH.kicad_pcb` candidate adds the
missing same-net U5 12V_PROTECTED and POWER_GND exposed-pad joins from actual
serialized pad coordinates. The NC pad 15 is avoided with an outer dogbone.
Native DRC improved the inherited unconnected count from 397 to 390 without
introducing any `shorting_items` or `tracks_crossing`; the candidate has no
remaining U5 12V_PROTECTED or POWER_GND unconnected record. It is retained as
targeted evidence, but cannot be promoted as the board solution while the
remaining native records include 12V_PROTECTED, POWER_GND, CM5 ground,
input/fused 12V, low-voltage, and clock/storage connectivity gaps.

## Regulator-field follow-up

The generalized exposed-pad experiment confirms that local field stitching is
useful but must respect existing control routes. The all-U3/U4/U5 candidate
was rejected by one native crossing and three true shorts at U4's existing
PG_BRIDGE_3V3 path. The bounded U3+U5 candidate has zero shorts/crossings and
384 native unconnected records, so it is retained as targeted evidence. U4
and the board-wide 12V/ground distribution remain open and need
obstacle-aware launches; no severity was changed and no connection was
waived.

## CM5 upper comb rejected

The upper J7 ground-comb extension is rejected at three shorts and nine
crossings despite reducing unconnected records to 121. The live Ethernet
fanout must be locally regenerated before upper-row CM5-ground collection can
be attempted.

The horizontal-only upper bridges were separately tested and rejected at one
short and six crossings. This exhausts comb-only upper-row variants; the next
authorized class is Ethernet-launch regeneration.

## CM5 lower comb accepted

The lower J7 ground bank now has an explicit outer-column F.Cu comb. It passes
full-report native DRC at 208 violations and 127 unconnected records with no
shorts or crossings. Upper Ethernet-row grounds remain intentionally
untouched pending a separate fanout/collector solution.

## U7 BRIDGE_CFG accepted

The remaining U7 configuration pad pair is now natively joined on the current
ancestor. DRC reports zero shorts/crossings and 136 unconnected records; no
validation severity or storage topology was changed.

The C5/C6 direct ground join was tested and rejected at one native short,
despite reducing unconnected records to 140. This confirms that the remaining
global-ground field requires layer-aware escape geometry.

## Native DRC evidence correction

Fresh KiCad DRC on the exact current ancestor reports 235 violations, 136
unconnected records, 4 shorts, and 7 crossings. Prior zero short/crossing
claims were produced by a parser that began at the unconnected section and
missed earlier report sections; they are superseded. The J7 top-row trial is
also rejected at 8 shorts and 10 crossings despite reducing unconnected
records to 134.

The clean repair sequence now ends at `PHASE24_BRIDGE_3V3_CAP_CHAIN_V2`:
208 DRC violations, 141 unconnected records, zero shorts, and zero
crossings. This candidate includes only the clean 1V1 capacitor field/R19
path and the clean 3V3 capacitor field. Later support/CFG/input joins remain
rejected until regenerated from this clean basis.

## Working-basis correction

Full-report counting establishes the clean basis as
`PHASE24_BRIDGE_1V1_CAP_CHAIN.kicad_pcb` at 205 DRC violations, 145
unconnected records, zero shorts, and zero crossings. The later composite
candidate is not clean: fresh DRC reports 235 violations, 136 unconnected,
four shorts, and seven crossings. Those later joins are rejected pending
regeneration from the clean basis.

## 12V input bypass accepted

C3.2 was joined to the existing `/POWER_INPUT/12V_IN_A` component with a
short F.Cu dogleg. Native DRC reports zero shorts/crossings and 137 remaining
unconnected records. No power topology or validation severity was changed.

After removing the stale bridge-1V1 source segments and moving the island to
an open acreage shelf, `PHASE24_U5_CAPS_ISLAND-far4-drc.rpt` reports `214`
inherited/disposable violations and `391` unrelated unconnected items, but
zero `shorting_items`, zero `tracks_crossing`, zero `track_width`, and zero
footprint errors. C44-C47 and the `/REGULATORS/BRIDGE_1V1`/`POWER_GND`
support group do not appear in the unconnected-items section. This closes the
local capacitor topology proof only; the final combined candidate must still
replace the affected acreage rail corridor and preserve all other power
connectivity.

## Full clock-support discriminator (still open)

The subsequent no-via-in-pad revision uses rule-width tracks and offset
ordinary vias at all six passive SMD endpoints. Native DRC reports `168`
violations and `499` unconnected items on the stripped ancestor, with zero
`tracks_crossing`, zero `shorting_items`, zero `track_width`, and zero
footprint errors. The target XI/XO/VSSOSC groups still appear in the native
unconnected report, so this is not yet connectivity proof. The remaining
issue is authoring/connectivity attachment through the generated layer
transitions; no production board or Phase 24 gate has been promoted.

## Clock-support topology pass

After correcting the SWIG-safe copper reset and separating the common
VSSOSC return with an additional ordinary-via layer transition, the complete
U7/Y1/R23/C42/C43 discriminator was rerun as
`PHASE24_STORAGE_ROT90_PROBE-native5-drc.rpt`. Native DRC reports zero
`tracks_crossing`, zero `shorting_items`, zero `track_width`, and zero
footprint errors. The target XI/XO/VSSOSC nets do not appear in the
unconnected-items section. The report still contains `499` unrelated
unconnected items because all inherited acreage copper is intentionally
removed; therefore this closes only the local clock-support topology proof.
Next work is to transplant this generated support into a coordinated acreage
candidate and materialize C44-C47 against the actual U5 rail pads.

## Corrected reproducible rerun

The latest authoring script was rerun from the V5 input with native KiCad
10.0.5 DRC output `PHASE24_STORAGE_ROT90_PROBE-final-drc.rpt`.
The script exited successfully. DRC reports `164` disposable/inherited
violations, zero `tracks_crossing`, zero `shorting_items`, zero
`track_width`, and zero footprint errors; the unconnected-items section has
no XI/XO/VSSOSC entries. This is the clean local topology proof. It is not
yet an acreage proof because the discriminator intentionally removes
unrelated ancestor copper and has not materialized the U5 C44-C47 island.

## Combined proven-clock transplant (rejected)

`phase24_transplant_proven_clock.py` rigidly transformed the passing rot90
U7/Y1/R23/C42/C43 copper graph into the V5 rot180 U7 orientation, deriving
all support footprints and post-transform vias from the saved oracle. The
result was tested as `PHASE24_PROVEN_CLOCK_ROT180_ACREAGE-drc.rpt` and
rejected: native DRC found true shorts and crossings against the inherited
PCIe/SATA corridors, plus a POWER_GND-to-XO conflict. This rejects that
placement transform only; it does not invalidate the passing local clock
topology. The next integration candidate must select a genuinely open
acreage support shelf and preserve the existing PCIe/SATA corridors.

## Open-shelf clock candidate (rejected)

`phase24_open_shelf_clock.py` tested a shelf at approximately x204-218,
y140-155, immediately left of the M.2 mechanical envelope, with U7 held at
the validated rot180 placement. Native DRC reported `271` violations,
including new clock tracks crossing and shorting at the U7/source and
crystal fanout. The shelf itself is not the obstruction; the candidate used
hand-authored rot180 source coordinates and failed pad-field attachment.
It is rejected. The next candidate must derive every rot180 U7 clock endpoint
and source dogbone from the serialized footprint, reusing the proven local
clock graph rather than absolute hand coordinates.

## Combined integration attempt

The existing rot180 acreage clock generator and a rigid transform of the
passing rot90 clock graph were both tested against the V5 PCIe/SATA/USB3
ancestor. The generator produced local clock-to-storage shorts/crossings;
the rigid transform produced true PCIe/SATA shorts and crossings. These are
rejected integration candidates. The local clock and U5 capacitor topology
proofs remain valid and are retained as the authoritative sub-fixtures for
the next open-shelf integration pass.

## Generic rot180 endpoint rerun (rejected)

The open-shelf generator was corrected to derive U7 pins 52/53/54 from the
serialized post-rotation footprint. The rerun exited successfully, but
`PHASE24_OPEN_SHELF_CLOCK-derived-drc.rpt` still reports `271` violations,
including clock shorting and crossing records in the local branch topology.
The endpoint-authoring defect is fixed, but this shelf routing graph remains
rejected. The proven rot90 topology and U5-cap topology remain the valid
local oracles for the next integration attempt.

## Underside open-shelf source attempt (rejected)

The shelf candidate was revised so Y1/R23/C42/C43 use B.Cu pads and the
three source lanes terminate directly on the serialized underside Y1 pads.
This removes the prior F.Cu crystal-launch crossing, but the long lanes still
intersect inherited SATA copper. Native DRC reported `224` violations with
clock/SATA crossings and shorts. The underside placement remains mechanically
permitted, but this corridor is rejected; a successful acreage candidate
must choose a route corridor that avoids the inherited SATA field as well as
the PCIe corridor.

## Rot180 source-escape oracle

`phase24_rot180_source_escape.py` now derives U7 pins 52/53/54 after setting
the footprint to rot180 and validates the asymmetric top-row escape: XI
exits diagonally right, VSSOSC exits upward, and XO exits diagonally left
before the ordinary through-vias. Native DRC report
`PHASE24_ROT180_SOURCE_ESCAPE-derived-drc.rpt` contains `164` inherited
violations but zero `shorting_items`, zero `tracks_crossing`, zero
`track_width`, zero footprint errors, and no XI/XO/VSSOSC unconnected
records. This closes the rot180 source-escape geometry proof only; shelf
fanout and full acreage parity remain open.

## Compact clock-position sweep (in progress)

`phase24_clock_position_sweep.py` tested five compact/open support positions
against the V5 rot180 ancestor using serialized U7 pad coordinates and the
outward pad-row escape. The best candidate is `nearwest` (`Y1` approximately
108/130 mm, underside pads): native DRC reports 212 violations, with the
remaining new clock defect reduced to a localized B.Cu lane crossing at the
U7 escape. The other candidates remain worse because they intersect inherited
PCIe, SATA, or M.2 geometry. This is evidence that the open-acreage class is
viable, but the candidate is not promoted: the next experiment must rotate or
reorder the crystal footprint and make the three clock lanes monotonic before
full support fanout is restored.

The follow-up 90-degree crystal-orientation trial was rejected: native DRC
remained at 214 violations and added several short B.Cu crossings at the Y1
pad field. Orientation alone is insufficient; the next candidate must author
an explicit ordered three-lane escape rather than use the generic Manhattan
fanout.

The ordered-lane rerun exposed and corrected a disposable-script output-path
bug that had left the previous orientation report stale. The corrected
near-west 0-degree/layer-split artifact reports 215 native DRC violations;
remaining new defects are the U7-to-crystal source corridor and one inherited
CM5 USB3 overlap. The prior 214 count is discarded. No acreage promotion or
parity closure is claimed.

## Mixed-layer ordered escape trial (rejected)

The next class separated XI/XO onto B.Cu and kept VSSOSC on F.Cu, with an
explicit ordered lane set and an underside Y1. The corrected artifact still
reports 224 native DRC violations. Failures remain concentrated at the U7
oscillator pad escape and inherited SATA-TX launch. The mixed-layer choice did
not remove that local pad-field obstruction. Consultant/unblocker dispatch was
retried but remains unavailable because the agent thread limit is exhausted;
local analysis continues and this is not treated as an architectural block.

## Obstacle-aware route-search diagnostic

`phase24_clock_astar.py` was added as a bounded route-search diagnostic over
the inherited F.Cu/B.Cu track and pad field. Its initial conservative model
correctly refused to seed an XI path through the dense U7 pad field and
returned `no route XI`; no candidate was generated or promoted. This is a
model limitation: the solver must seed the manufacturer-style package-edge
dogbone outside the source pad before searching downstream lanes. It is not
evidence that the clock topology or the board is impossible.

## Surgical SATA-launch reroute trial (rejected)

The next bounded class removed only the inherited U7-to-AC-capacitor TX_N/TX_P
launch tracks and regenerated them with ordinary F.Cu/B.Cu vias, leaving the
post-cap SATA paths and all unrelated high-speed routes inherited. Native DRC
reported 252 violations, including new TX_N/TX_P crossings, clock/SATA
crossings, and a PCIe interaction. The candidate is rejected. It does not
invalidate the storage architecture; it shows that the two SATA launches and
the three oscillator exits require one coordinated pad-field escape graph.

The seeded follow-up used the proven rot180 source-via exits before invoking
the downstream search. It still found no XI route once the inherited SATA
launch and U7 pad field were treated as obstacles. No board was generated or
promoted. This narrows the next experiment to a single coordinated escape
graph containing the package-edge dogbones and adjacent SATA launch; it does
not justify a terminal architecture blocker.

The route-search diagnostic was refined to seed the exact proven rot180
ordinary-via exits and then search downstream corridors. The conservative
search still returns `no route XI` against the inherited SATA/pad field, so no
candidate is promoted. This remains a geometry discriminator; it does not
replace native KiCad proof or establish an architectural block.

The seeded search was then widened to a genuinely adjacent shelf (`Y1` near
130/145 mm, between U7 and the lower J3 boundary). It still returned `no
route XI` before producing a board. Because the search is intentionally
conservative around pad fields and existing tracks, this rejects the current
search model/candidate only; it does not claim that the shelf is physically
impossible. The next implementation must seed an explicit legal dogbone graph
and search from its first free grid cell.

## Coordinated storage relocation, expanded acreage (rejected)

The approved option-2 experiment moved the complete coordinated storage donor
by +80 mm in Y and expanded the disposable outline to 300 x 280 mm. Native
DRC reported 283 violations. The relocation removed the prior donor clock
crossings against the preserved PCIe band, but shifted donor copper no longer
connected to the fixed CM5 USB3 launch; U7 reset/rail and storage-side
connections also remained incomplete. The candidate is rejected. Relocation
must regenerate the CM5-to-U7 USB3 corridor separately from the relocated
bridge/SATA/clock island; blind rigid translation is not a valid integration
method.

## Authoritative tunnel-guided solver result (in progress)

The independent geometry review identified a clear inherited B.Cu tunnel at
approximately y=123--129 mm and recommended moving the XI/VS seeds into it.
That recommendation was implemented in `phase24_clock_astar.py`. The solver
now finds all three downstream routes and, after real via-clearance reservation
was added, native DRC reports 238 violations with no new close-via cluster.
The remaining first errors are localized to the XO F.Cu package-edge launch
against the inherited SATA-TX/RX F.Cu rails. This is the strongest current
candidate but remains unpromoted until the XO source launch is also clean.

## Tunnel-guided source-launch refinement (in progress)

The tunnel-guided A* candidate was refined using the measured y=123--129 mm
B.Cu tunnel, explicit via reservation, an XO staging point at (111,132), and
explicit Y1 pad-layer metadata. The latest generated artifact
`PHASE24_CLOCK_ASTAR_NEARWEST.kicad_pcb` reports 226 native DRC violations.
The prior XO/SATA source crossing is removed; remaining errors are localized
to the Y1 XI/VSSOSC approach and one inherited CM5 USB3 interaction. This
remains unpromoted; Phase 24 parity is open.

## Side-separated crystal escape refinement (in progress)

The next disposable refinement assigns all four crystal pads to B.Cu, routes
XI to a west-side staging point, carries VSSOSC around the south side to an
outboard vertical, and terminates XO through a separate B.Cu staging point.
The generated candidate reports 207 native DRC violations, with zero
`tracks_crossing` and zero `shorting_items` records. The remaining report
violations are inherited board hygiene (including 391 inherited unconnected
items and existing presentation/clearance findings); this is not a clean
Phase 24 board and is not promoted. The next step is support-part
materialization on this clock oracle followed by a targeted connectivity and
parity audit.

## First support materialization (rejected)

`phase24_materialize_clock_support.py` added Y1's R23/C42/C43 and C44--C47
to the side-separated clock candidate. Native DRC reported 240 violations,
including 3 new track crossings and 8 new shorting records. The clock passive
branches entered the Y1 pad field and the C44--C47 placement overlapped
existing regulator feedback/support geometry. This candidate is rejected;
the clean clock escape remains useful, but support parts must be placed and
routed as independently bounded islands before integration.

## Native-orientation clock discriminator

The existing parameterized `phase19_clock_minimal_fixture.py` was rerun as a
disposable native fixture with its native U7 orientation. The resulting
`PHASE24_CLOCK_MINIMAL_ROT0.kicad_pcb` has zero reported unconnected items,
zero shorting records, zero track crossings, and zero footprint errors in
native KiCad DRC. However, inspection shows that this legacy fixture does not
route every passive branch to R23/C42/C43, so it is only a source-escape and
footprint discriminator, not complete support-topology closure. A genuinely
complete support fixture and the rot180 acreage transformation remain open.

## Strict complete-fixture attempt (rejected)

`phase24_complete_clock_fixture.py` required every Y1/R23/C42/C43 pad to
participate in the routed graph. Its first generic three-bus layout reported
24 native DRC violations: 5 track crossings, 4 shorts, and 8 disconnected
pads. The failure is retained as a valid rejection; the next implementation
must derive branch escape points from the serialized pad field and reserve
that field explicitly.

The launch-height refinement was also rejected: native DRC reported 9
violations, including 8 B.Cu perimeter crossings and 8 isolated non-clock
U7 pads. It improved the prior shorts but did not produce a valid complete
fixture. The next credible class is an obstacle-mapped transplant of a proven
routed support template, not further generic Manhattan bus tuning.

## Obstacle-aware passive-router attempt (rejected)

`phase24_support_astar.py` routed each R23/C42/C43 pad toward its matching
serialized Y1 endpoint while treating other-net copper as an obstacle. The
router found all six paths, but native DRC reported 380 violations, including
29 shorts and 13 crossings. The candidate is rejected: endpoint targeting at
the dense Y1 field is insufficient without a branch-aware regenerated clock
topology.

## Branch-to-existing-rail attempt (rejected)

`phase24_support_astar.py` was revised to attach the six passive branches to
open points on the validated XI/XO/VSSOSC rails rather than directly to Y1.
The VSSOSC branch could not reach its selected rail point; the generated
candidate reported 268 native DRC violations, including 12 shorts and 9
crossings. This class is rejected. The next candidate must generate the
complete clock island as one coordinated graph, including passive branches,
before emitting any copper.

## Multi-net graph-anchor sweep (rejected)

The branch solver was upgraded to evaluate all existing same-net B.Cu graph
points and reserve each selected path before the next branch. It found six
candidate paths, but native DRC reported 271 violations including 10 shorts
and 4 crossings; the selected anchors still lie inside the inherited
crystal-field corridor. This class is rejected. The next implementation will
use F.Cu passive dogbones and offset through-vias followed by short B.Cu rail
joins, so branch copper does not enter the crystal pad field.

## Coordinated-island placement sweep (rejected)

The branch router was parameterized and swept across five acreage placements
for the R23/C42/C43 island. Four placements had no conservative path to at
least one serialized rail anchor; the best generated placement still
reported 322 native DRC violations. No placement was promoted. The sweep
supports replacing the current fixed-rail attachment model with a fresh
multi-net graph whose clock and passive branches are solved together.

## Layer-separated passive branch attempt (rejected)

The next experiment placed passive pads on F.Cu, added offset ordinary
through-vias, and routed only post-via branches on B.Cu. Native DRC still
reported 306 violations, including 14 shorts and 6 crossings. Four further
outboard placement variants had no conservative route to a clock graph point.
This class is rejected; the inherited clock oracle cannot accept passive
fanout incrementally.
## Coordinated layer-owned clock graph (source proof)

`phase24_clock_coordinated_layers.py` now emits the complete Y1/R23/C42/C43
## Coordinated layer-owned clock graph (source proof)

`phase24_clock_coordinated_layers.py` now emits the complete Y1/R23/C42/C43
graph with XI on B.Cu, XO on F.Cu, and VSSOSC on a separate B.Cu perimeter.
The latest native DRC report `PHASE24_CLOCK_COORDINATED_LAYERS-drc.rpt`
contains no `tracks_crossing`, no `shorting_items`, and no footprint errors.
The only DRC warning is R23 silkscreen text height; the eight reported
unconnected items are unrelated non-clock U7 pads intentionally left isolated
by the disposable fixture. All clock source and support pads are connected.
This is the first complete clock/support topology proof; it is not yet an
acreage promotion.
## Acreage transplant and U5 island trials

`phase24_clock_support_transplant.py` was tested against the rot180 A* clock
oracle and rejected. Native DRC reported 218 violations, including clock-net
crossings and a VSSOSC/XO short; the passive branches entered inherited USB3
and clock corridors. This is an integration-placement failure, not evidence
against the proven clock topology.

`phase24_u5_caps_island.py` was independently tested from the Phase 23
ancestor. Its native DRC reported 214 inherited violations but no
`shorting_items` or `tracks_crossing` records. Ten dangling-track/via records
remain, so this is a useful electrical island discriminator, not closure.
## U5 surface-only trial (rejected)

`phase24_u5_caps_surface.py` removed the added ground vias and attempted a
single F.Cu bridge-1V1 trunk to C44-C47. Native DRC reported 202 violations,
including a rail/POWER_GND short and track crossings. The variant is rejected;
the prior no-crossing U5 island remains the better starting point, subject to
correcting its source/return geometry.
## Complete authoritative component baseline

`phase24_materialize_all_authoritative_parts.py` materializes Y1, R23, C42,
C43, and C44-C47 from the clean local footprint library with explicit
schematic net maps. `phase24_authoritative_parts_audit.py` passes all eight
references and every pad-net assignment. Native DRC for
`PHASE24_ALL_AUTHORITATIVE_PARTS.kicad_pcb` reports 187 inherited violations
and 406 unconnected pads, but no `shorting_items` or `tracks_crossing`
records. This proves component/net authority, while routing and full parity
remain open.

The recommended three-pad CM5-ground discriminator passes full native DRC at
209 violations and 139 unconnected records with zero shorts/crossings. It
closes only the tested lower-right subcluster; the upper interleaved Ethernet
rows remain unresolved.

The horizontal-only upper J7 bridges were tested independently and rejected
at one native short and six crossings. The lower comb remains the accepted
basis; upper-row closure requires Ethernet-launch regeneration.
## U5 outboard surface placement (rejected)

`phase24_u5_caps_outboard.py` moved C44-C47 to a separate outboard acreage
region and routed a monotonic F.Cu bridge-1V1 trunk. Native DRC reported 203
violations, including a bridge-1V1/POWER_GND short and crossings. Together
with the prior surface-only trial, this rejects the surface-rail-trunk class.
The next experiment must map existing copper/ground clearances and provide a
deliberate return path.
## Independent audit and ground-aware U5 V2

The hardware-auditor review confirms that the eight-part baseline is only
narrow materialization evidence. It does not prove full schematic↔PCB parity,
routing connectivity, footprint-filter parity, or source ownership. It also
flags the existing electrical Ethernet center-tap references as a separate
source/PCB parity reservation.

`phase24_u5_caps_ground_aware_v2.py` was then tested with rotated C44-C47,
separate rail/return lanes, and the existing local ground launch. Native DRC
reported 197 violations and 392 unconnected pads, with one localized rail/
return crossing and no shorting record. It is rejected as incomplete, but is
the best U5 placement class so far; the next trial must separate its source
and return lanes by layer or use a mapped return launch.
## U5 source-launch refinement (rejected)

The U5 V2 source launch was moved around the feedback corridor and rerun with
the same ground-aware capacitor placement. Native DRC remained at 197
violations and 392 unconnected pads; one source/return crossing remained and
no shorting record was present. This is not promoted. The remaining repair
class is a genuinely layer-separated source/return launch.
## U5 left-side source detour (rejected)

The latest V2 rerun moved the 1V1 source detour left of the regulator
feedback segment. Native DRC still reports 197 violations, including one
source/return crossing and 392 unconnected pads. This remains a negative
disposable result and does not alter the accepted power architecture.
## U5 layer-owned source/return fixture (targeted proof)

`phase24_u5_layer_fixture.py` strips unrelated copper/zones and proves the
C44-C47 source/return geometry with explicit F.Cu launches, ordinary
through-vias, and separate B.Cu rail/return corridors. Native DRC reports zero
shorting and zero crossing records. The 499 unconnected pads belong to
deliberately unconnected non-target U5/fixture pads. This closes the U5
topology discriminator only; acreage integration remains open.
## Corrected U5 layer fixture rerun

The U5 layer fixture was corrected so the B.Cu rail and return trunks reach
the actual rotated C44-C47 pad rows. Native DRC reports zero
`shorting_items` and zero `tracks_crossing` records, with 499 deliberate
non-target U5/fixture unconnected pads. A first graph-audit implementation
was found to have a coordinate-join defect and is excluded from the evidence.
This remains a topology discriminator, not acreage closure.
## U5 fixture connectivity regression audit

`phase24_u5_layer_connectivity_audit.py` now passes against the corrected
fixture, proving the four C44-C47 rail pads join U5.9 and the four return pads
join R20.2. The audit explicitly accounts for KiCad's serialized via/track
layer representation. Native DRC still reports zero shorts and crossings for
the fixture. This is a regression/topology receipt, not integrated acreage
closure.
## PCB-only Ethernet alias removal

`phase24_filter_legacy_ethernet_aliases.py` removes the nine PCB-only
`CCT/RCT` electrical aliases whose nets are absent from the clean schematic.
The filtered candidate has all 78 schematic references and only the expected
13 mechanical/test markers. Native DRC adds no shorting or crossing records.
This is a parity-source correction, not routed Ethernet closure; the clean
schematic's Ethernet return/support implementation still requires its own
validated routing evidence.
## Filtered candidate revalidation

The filtered candidate was rerun through the exact reference-set audit and
native DRC. The audit remains PASS for 78 schematic references plus 13
mechanical/test markers; native DRC reports no `shorting_items` or
`tracks_crossing` records. The report still contains 201 violations and 406
unconnected pads, therefore the routed Phase 24 gate remains open.

## Latest bounded U5 integration result

The corrected real-pad layered integration reuses the authoritative C44-C47
footprints, refills the ground planes, and routes the ground branches below
the separated B.Cu rail trunk. The integrated graph audit passes for all
C44-C47 rail/return pads. Native DRC reports zero shorting and zero
track-crossing records; the board report is 201 violations and 397
unconnected pads. This is validated local U5 integration, not full Phase 24
closure. Full-board routed schematic-to-PCB parity remains open.

## Rejected clock-oracle overlay

The proven rotated-U7 clock copper was overlaid on the U5-integrated acreage
candidate using existing authoritative clock footprints. Native DRC found 288
violations, 400 unconnected pads, track crossings, and clock-to-SATA/bridge
shorts. This is a rejected coordinate-overlay experiment, not evidence that
the clock architecture is invalid; the clock island must be regenerated in a
free local corridor or the surrounding storage copper must be coordinated.

## Corrected transform rerun

The fixture-to-acreage mapping was corrected using the serialized U7 pad frame
(`(97,104.5)` to `(123,135.5)`). The consistent rerun still fails promotion:
native DRC reports 227 violations, 393 unconnected pads, crossings, and
clock-to-SATA shorts. The remaining work is local clock-corridor regeneration;
the clock architecture itself remains supported by the standalone fixture.

## U5 audit correction

The former U5 regression audit was not accepted as physical proof because it
injected hard-coded edges. It has now been replaced with a net-aware,
layer-aware graph derived from the saved PCB's tracks, vias, pads, and filled
zones. Positive proof passes on the integrated U5 board. Disposable missing
trace and missing via controls both fail as required. This closes the audit
method defect, but not full-board Phase 24 routed parity; native DRC still
reports 397 non-target unconnected pads.

## Native connection census

The committed census parses all 397 native missing-connection records. The
largest unresolved classes are `12V_PROTECTED` (146), `POWER_GND` (128), and
`/CORE_CM5/POWER_GND` (50), followed by regulator rails, power-entry rails,
SATA RX-N, and bridge clock nets. No records were waived; the table is
diagnostic evidence for sequencing the remaining physical repairs.

## Promoted U7 RX-N local repair

The first RX-N pad-field launch was rejected for SATA-TX crossing and RX-P
clearance. A bounded dogleg variant around the existing B.Cu SATA-TX trunk
passes the local native gate: five missing RX-N connections were removed,
with no new short or crossing record. The full candidate still has 392 native
unconnected records, so this does not close Phase 24.

## Protected 12 V plane rejected as sole repair

Adding the plan-defined `In3.PROTECTED_12V` plane was electrically clean but
only removed two native missing-connection records (397 to 395). It cannot
contact the unresolved F.Cu SMD regulator and capacitor pads without explicit
vias/dogbones. No DRC severity was relaxed; the remaining issue is a
launch-mapped power implementation.

The B-side fuse pad-field trial joined F2's raw and fused four-pad groups as
separate same-net fields. Native DRC stayed at 201 violations with zero
shorts/crossings and removed six unconnected records (397 to 391). This is
accepted targeted evidence only; it does not falsely bridge raw-to-fused
power, and the named J6/F2/U2/Q2 branch and board-wide distribution remain
open.

The initial J1 protected bus was rejected: B.Cu copper did not physically
contact the serialized surface pads and native DRC rose to 214 violations.
The corrected F.Cu-column plus offset-via/B.Cu-bus candidate passes its local
native gate with 201 inherited violations, zero shorts/crossings, and 268
unconnected records versus 397. It is retained as the next promoted physical
power-field evidence, while full named distribution and all remaining native
connection classes remain open.

The F1 A-side pad-field trial likewise passed as local evidence: 201 native
DRC violations, zero shorts/crossings, and five fewer unconnected records
(397 to 392). Raw and fused nets remain separate. Full Phase 24 still awaits
complete named input-branch, protected-12V, ground, low-voltage, and
clock/storage connectivity.

The bridge low-voltage field trial initially shorted the intervening U4/U5
POWER_GND pad and was rejected. The corrected perimeter escape passes native
DRC with 201 inherited violations, zero shorts/crossings, and reduces the
plane-based candidate from 265 to 261 unconnected records. It is retained as
targeted evidence; full bridge rail/capacitor/control connectivity remains
open.

The protected-12V plane was tested on the corrected J1 field bus. It remains
native-clean relative to the candidate (201 DRC violations, zero
shorts/crossings) and reduces unconnected records from 268 to 265. This
confirms the In3 distribution layer can be used with the J1 field, while
explicit surface launches remain required elsewhere.

The initial J1 ground-column launch location was rejected because six
through-vias intersected the protected B.Cu bus. Relocating the seven ground
launches below that bus produces a native-clean targeted candidate: 201
inherited DRC violations, zero shorts/crossings, and 195 unconnected records.
The separate `/CORE_CM5/POWER_GND` net was not bridged; remaining local and
board-wide ground distribution is still required.

An U4-specific left-side dogbone trial was run after the all-regulator trial.
It removed the U4 short class but introduced four native F.Cu crossings at
the existing PG_BRIDGE_3V3 and U4 ground geometry, so it is rejected. U3/U5
remain clean targeted field repairs; U4 requires layer-separated or locally
regenerated routing, and the board-wide native connection census remains the
active Phase 24 gate.

The corrected U4 perimeter variant moves the protected-12V escape above the
nearby PG via/feedback corridor. Native DRC returns to the inherited 201
violations with zero shorts and zero crossings; the earlier layer-separated
variant was rejected for two feedback crossings and one short. This closes
only the U4 local geometry discriminator and does not close the board-wide
native connection gate (390 unconnected records remain).

The CM5-ground launch attempts were rejected. The first two offsets entered
the J7 signal escape field; the widest tested perimeter offset reduced
unconnected records but caused 17 shorts and eight crossings in native DRC.
No CM5 ground was bridged to global `POWER_GND`. This remains an explicit
local routing/authority blocker, not evidence that the CM5 architecture is
electrically impossible.

The U3 POWER_GND field now has a clean targeted perimeter escape: 201
inherited native DRC violations, zero shorts/crossings, and 258 unconnected
records versus 261. The remaining board-wide ground distribution and CM5
ground authority are still unresolved.

The combined U4/U5 ground-field experiment was rejected after two native
crossings at U4's PG_BRIDGE_3V3 corridor. The U5-only follow-up passes with
201 inherited DRC violations, zero shorts/crossings, and 255 unconnected
records, and is retained as targeted evidence. U4 control/power routing and
board-wide ground distribution remain open.

The consultant-recommended global POWER_GND launch cluster was validated
after correcting one J4 via that intersected an existing USB2 B.Cu track.
The final candidate has 201 inherited native DRC violations, zero
shorts/crossings, and 188 unconnected records versus 195. It targets only
U1/U2/J4/U8 global returns; CM5 ground was not bridged and remains a separate
authority issue.

The first cumulative local-repair composition was rejected for three native
12V-to-ground crossings at U3/U5/U4 field routes. The corrected composition
preserves the clean J1/global-return/bridge/input repairs while omitting the
overlapping regulator ground traces. It passes native DRC at 201 inherited
violations with zero shorts/crossings and 168 unconnected records. This is
the current best power/rail integration candidate, not Phase 24 closure.

The validated U7 RX-N pad-field stitch was then composed onto the cumulative
candidate. Native DRC remains at 201 inherited violations with zero
shorts/crossings and reduces unconnected records from 168 to 163. This
storage repair composes cleanly; clock and remaining SATA/control records
remain unresolved.

The right-column CM5-ground collector expanded cleanly from the accepted
three-pad discriminator: the V2 and V3 trials report 209 DRC violations,
zero shorts/crossings, and 136 then 130 unconnected records. The upper
Ethernet-interleaved rows remain the only J7 portion not covered by this
collector class.

The lower x=70.04 J7 group was added to a separate x=71.50 outer F.Cu rail.
Fresh DRC reports 209 violations, 124 unconnected records, zero shorts, and
zero crossings. The remaining J7 work is confined to upper interleaved rows
and connector-plane attachment.

The cumulative PCB was missing serialized net identity on U7 clock pads
52/53/54. That was corrected in a disposable candidate using the schematic's
XI/VSSOSC/XO mapping. Native DRC remains at 201 violations with zero
shorts/crossings; the unconnected census rises 163 to 166 because the source
pads are now correctly included. No clock routing claim is made yet.

The U7 `BRIDGE_CFG` repeated-pad join was tested and rejected: the direct
link hit pad 24 on `BRIDGE_3V3`, while the perimeter reroute produced two
shorts and one crossing. No severity was relaxed; the control escape remains
an open pad-frame routing task.

The initial oracle-derived XO escape crossed the inherited SATA-TX corridor
and was rejected. Moving only XO below that corridor yields a disposable
source escape with zero native shorts/crossings (204 total DRC violations,
166 unconnected records). This is source-side clock evidence, not complete
clock closure; the passive island still needs obstacle-aware branches.

The first complete passive clock-branch attempt was rejected despite reducing
unconnected records to 156: native DRC reported three shorts and ten
crossings in the B.Cu passive-pad approaches. No gate was relaxed. The next
clock class is isolated pad launches with layer-separated buses.

The isolated passive-launch clock candidate was rejected: native DRC found 17
crossings and three shorts. The primary failures were F.Cu source corridors
crossing inherited SATA/USB routes and an XO segment touching an unassigned
U7 pad. This evidence does not change the storage architecture; it narrows
the required next implementation to an obstacle-aware layer-separated clock
route.

The exact rotated-U7 clock oracle was transplanted for comparison and
rejected by native DRC at 288 violations, with clock/SATA crossings and
clock/J3 interactions. This is coordinate-context evidence, not an
architectural rejection; the next implementation must regenerate the clock
corridor locally from the serialized U7 pads.
## Exact coordinated oracle transplant — rejected

The disposable `phase24_clock_oracle_coordinated.py` experiment copied the
complete rotated-U7 clock support placement and clock-net copper from
`PHASE19_PASS_CLOCK_ROT180_S20.kicad_pcb` onto the current U7 authority
candidate. Native KiCad DRC reported 288 violations and 166 unconnected
items, including clock/SATA crossings, clock/J3 interactions, and
shorts/clearance failures. This rejects the fixed-coordinate transplant only;
the oracle topology remains valid and requires obstacle-aware local
regeneration around the current U7/storage launch.

## U5 audit regression fixed

The former U5 audit's synthetic geometry graph was replaced with KiCad's
native saved-board connectivity rebuild. Assertions identify required pads
only; pads, tracks, vias, layers, nets, and filled zones supply the evidence.
The saved U5 board passes native connectivity, while a disposable removal of
an actually connected U5.9 trace fails the audit. This removes the false-pass
risk without waiving any remaining board connection.

## Clock fixture V2 evidence

The split-layer V2 clock fixture passes native clock connectivity and has no
clock short or crossing. Transforming it into the current acreage frame is
rejected by native DRC at 226 violations, including seven clock shorts and 16
crossings. This is integration-coordinate evidence; the proven isolated
topology remains available for a new obstacle-aware acreage placement.

## Incremental clock evidence

XI and XO source-to-crystal discriminators pass without native short or
crossing findings. The first VSSOSC perimeter is rejected: native DRC reports
two short and two crossing classes at the SATA/clock corridor. The failure is
localized to VSSOSC layer ownership and does not invalidate the XI/XO routes.

## Complete clock promoted

The corrected V2 complete-clock candidate passes native component checks for
all XI/XO/VSSOSC passive and crystal pads. Composing it onto the cumulative
local-repair board yields 205 DRC violations and 156 unconnected records, but
zero native shorting or track-crossing classes. The complete clock source is
accepted as the Phase 24 ancestor; the remaining blocker is the unrelated
board-wide connectivity/DRC census, not clock topology.

## Bridge 1V1 field accepted

The spaced bridge-1V1 capacitor field was regenerated with pad-adjacent
ordinary vias and a B.Cu rail chain. Native DRC reports zero shorting and
crossing classes and 145 unconnected records, down from 156. This is accepted
targeted progress; R19, R22, and C41 remain explicit native findings.

## Bridge 1V1 field joined to output island

The field-to-U5 output join passes native DRC with zero shorts and crossings
and reduces the unconnected census to 144. Native connectivity confirms the
capacitors and U5 output pads are joined. R19.1 and R22.1 remain explicit
isolated rail endpoints.

## Bridge 1V1 endpoints accepted

Sequential R19.1 and R22.1 local joins pass native DRC with zero shorts and
crossings, reducing the cumulative unconnected census to 142. The identified
BRIDGE_1V1 endpoint cluster is closed; remaining Phase 24 findings are other
net classes.

## Bridge 3V3 class accepted

The 3V3 capacitor field, R11/C18 support join, and R14-to-U4 output dogleg
were validated sequentially. Native DRC reports zero shorts and crossings;
the cumulative unconnected census is 138. No severity or connection was
waived.
# Current Phase 24 macro-floorplan assessment

The live integrated baseline is `PHASE24_CM5_GROUND_RIGHT_SAME_ROWS.kicad_pcb`.
Native-loaded geometry places CM5 Ethernet pads at (32.96/36.04, 99.1–100.7)
mm, U8 at (58,100), and J2 at (77.5,53), with 21.54 mm nearest-pad distance
and 534.4 mm of routed Ethernet F.Cu copper. CM5 USB3 to the U7/J3 storage
island is 53.81 mm nearest-pad distance. The macro-floorplan is therefore
materially nonlocal for these two neighborhoods.

`PHASE24_MACRO_ETH_WEST`, `PHASE24_MACRO_ETH_SOUTH`, and
`PHASE24_MACRO_STORAGE_LOCAL` are disposable placement-only candidates with
no major footprint-body overlaps. Their existing tracks are invalidated by
movement and are not evidence of routing closure. The next action is to
select a coherent candidate using consultant/specialist review, then
regenerate affected Ethernet/storage copper and revalidate all dependent
subsystems.

## Identity correction

The earlier current-state paragraph mislabeled `U8` as Ethernet ESD. The
native PCB shows `U8` is SERVICE USB2 ESD; Ethernet ESD is `U6`/`U9`
(`TPD4EUSB30`). Candidate moves and the macro assessment use the corrected
Ethernet set `U6`/`U9` plus `J2`. This does not promote moved copper or relax
Phase 24 acceptance gates.

## ETH_WEST trial result

The independent review recommends the west-edge coherent Ethernet move. The
first disposable rigid transplant was rejected after native DRC reported 571
total violations, 123 unconnected records, 12 shorts, and 20 crossings. This
is a placement-plus-authoring failure caused by carrying reference copper
through the acreage board, not evidence against the CM5IO Ethernet
architecture. The next authorized step is obstacle-aware regeneration from
native moved pads.
