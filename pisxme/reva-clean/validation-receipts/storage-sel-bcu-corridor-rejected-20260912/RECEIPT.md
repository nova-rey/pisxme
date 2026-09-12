# Phase 24 Path-A STORAGE_SEL B.Cu corridor probe — rejected

Base source: `09c15cf8` (physical board unchanged by subsequent documentation-only commits)
Candidate: `PHASE24_STORAGE_SEL_BCU_CORRIDOR_CANDIDATE.kicad_pcb`
Toolchain: KiCad Light 10.0.6, image `sha256:37d60e6797eaa14ea393de005b9793af5d9b5e7464aac1e4d58bec1b7803b4a9`

## Hypothesis

A native-pad, outboard B.Cu monotonic corridor could close all three `STORAGE_SEL` endpoints (U12.9, U13.9, U14.4) while keeping the U12/U13 fields on short F.Cu dogbones. The probe added only native tracks/vias; it changed no schematic, footprint, rule, or net assignment.

## Result

**REJECTED — real integrated physical defects.** Native DRC reports 361 violations / 499 unconnected items. The `STORAGE_SEL` net has zero unconnected-item entries, but the candidate introduces two real `shorting_items`, including the new `STORAGE_SEL` via shorting the existing `CM5_USB3_RX_N` B.Cu route, and four `tracks_crossing` findings. It also conflicts with the existing `STORAGE_3V3` route and ground-return zones. The candidate is not a production ancestor and no route was promoted.

The broader control/power outer-corridor variant is retained in the worker output only as a preliminary rejected probe; this receipt binds the final bounded attempt.

Raw DRC: `sel-candidate-drc.json`
Command: `kicad-cli pcb drc --format json --severity-all -o sel-candidate-drc.json PHASE24_STORAGE_SEL_BCU_CORRIDOR_CANDIDATE.kicad_pcb`
Candidate SHA-256: `de027de195de743dda8d17b5d45c286f9c1b159d6917d750deb6745366433f8c`
DRC SHA-256: `2f5539870bafc559ed47276ac00354df46ec69708ff89357800866b53696e367`
Script SHA-256: `bf7d631c999a3c97831f5b1b72534c303409641841b32f190549cda8f7536190`

## Disposition

This closes one bounded outer-corridor hypothesis for the current placement. Do not retry the same corridor or move vias into the existing USB3 return field. A next attempt requires a materially different coordinated storage-local placement/routing plan or explicit authority on local geometry; U12 package pitch remains an open domain-authority dependency.
