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
