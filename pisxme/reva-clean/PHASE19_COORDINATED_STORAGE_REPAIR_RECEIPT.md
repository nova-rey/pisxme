# Phase 19 coordinated storage-island repair receipt

Date: 2026-09-04
Status: `REJECTED_EXPERIMENT`; Phase 19 remains active.

## Authoring-path correction

`phase19_storage_coordinated_fresh.py` now removes donor C30-C33 footprints
before loading the project-local `C_0402_1005Metric` footprint. The Phase 18
ancestor already uses those references for unrelated regulator capacitors.
New socket-side nets receive explicit net codes and are attached to C30-C33
and J3 before the KiCad 10 synchronization save/reload; otherwise KiCad emits
blank or stale unconnected nets.

## Disposable candidate

Candidate: U7 `(150,140)`, rotation 180 degrees; J3 `(180,125)`, rotation 90
degrees; regenerated USB3 and four SATA split-cap paths from the Phase 18
ancestor.

Native evidence:

* generator completed under KiCad 10 Flatpak Python;
* J3 pads 1-4 serialize as `SATA_M2_TX_P/N` and `SATA_M2_RX_P/N`;
* C30 pad 1 is socket-side and pad 2 is bridge-side;
* native DRC: 262 violations, including candidate-introduced SATA launch
  crossings/shorts and interactions with inherited CM5/PERST copper.

The candidate is rejected and is not promoted to the clean acreage board. The
corrected generic authoring path is retained for the next experiment.

## Follow-up escape refinement

The generator was then changed to derive the USB3 landing from serialized U7
coordinates and to avoid routing through the vertical QFN pad field. The
USB-only V3 disposable run completed and reduced the report to 200 native DRC
violations, but retained inherited CM5/PCIe source-corridor crossings and one
candidate USB transition interaction. It is also rejected; the PCIe ancestor
remains unchanged.

## Coordinated corridor refinement

The next V3 run used the corrected USB3 escape, four rotated 0402 coupling
parts, split-net SATA routes, and separate F.Cu/B.Cu pair corridors. Native
DRC measured 206 violations. The candidate still has one stale J3 auxiliary
pad short and two local/PCIe corridor crossings, so it is rejected and not
promoted.

## Best current synchronized corridor

The refined USB3 TX_P lower-corridor escape and separated SATA cap lanes
produced `PHASE19_LIVE3.kicad_pcb`. Native DRC measured 207 violations, with
zero `shorting_items` records and one remaining `tracks_crossing` record in
the USB3 source/landing corridor; inherited clearance, hole, and
unconnected-acreage debt remains. It is not promoted because Phase 19
requires zero true crossings and clean connector/mechanical clearance.
