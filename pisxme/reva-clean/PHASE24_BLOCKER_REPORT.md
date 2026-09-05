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
