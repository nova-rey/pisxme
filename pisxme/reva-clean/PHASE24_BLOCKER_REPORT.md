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
