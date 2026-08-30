# PiSXMe Mac-to-Linux workstation handoff

Status: documentation handoff only. The active Rev A schematic, PCB,
footprints, rules, zones, manufacturing outputs, and Git history were not
redesigned in this handoff. M6 is blocked and M7–M10 are unstarted.

## Read first

Read this file, [`TOOLING_STATUS.md`](TOOLING_STATUS.md),
[`references/REFERENCE_INDEX.md`](references/REFERENCE_INDEX.md), and
[`plans/M6_LINUX_RESTART_CHECKLIST.md`](plans/M6_LINUX_RESTART_CHECKLIST.md)
before touching PiSXMe source.

## Project and architecture

PiSXMe is a 12 V, approximately 300 W-class compute appliance using a
Raspberry Pi Compute Module 5, one NVIDIA Tesla V100 SXM2 module, and a
PCIe Gen2 x1 host path. The current approved redesign direction is a
controlled M6 reconstruction with native CM5 Gigabit Ethernet, an internal
JMS578 USB3-to-SATA bridge feeding a SATA-only M.2 socket, and one USB-C
SERVICE/recovery port. The two external FAST USB3 host ports are abandoned for
this direction; do not restart their old routing.

The current board baseline is 240 x 140 mm. The outline is a resource, not an
immutable contract: consider a modest I/O-side expansion only after a
pin-accurate disposable candidate demonstrates a measured clearance or
routing need. Do not jump directly to a larger board.

## Execution state

M1–M5 contain historical/partial work and evidence, but the approved execution
gate was not closed cleanly. M6 remains blocked before active-source migration.
M7–M10 have not started. The blocker is source authority and routability:
the current schematic lacks authoritative Ethernet/JMS578/M.2/SERVICE islands,
the legacy FAST neighborhood contains disconnected fragments, and PCB-only
proxy insertions did not prove schematic-to-PCB authority. Earlier U16 and USB
support corrections also remain unpromoted.

The latest trustworthy conclusion is `SCHEMATIC_AUTHORING_TOOLING_BLOCKED`.
Do not treat disposable Ethernet/SATA candidates as active design completion.

## Active source

Authoritative paths:

- [`pisxme/PiSXMe.kicad_sch`](pisxme/PiSXMe.kicad_sch)
- [`pisxme/PiSXMe.kicad_pcb`](pisxme/PiSXMe.kicad_pcb)
- [`pisxme/PiSXMe.kicad_sym`](pisxme/PiSXMe.kicad_sym)
- [`pisxme/PiSXMe.kicad_pro`](pisxme/PiSXMe.kicad_pro)
- [`pisxme/PiSXMe.kicad_dru`](pisxme/PiSXMe.kicad_dru)

Verified hashes at the Mac handoff boundary:

```text
PiSXMe.kicad_sch  d31ff8e96fd1df211f5528f0b4c70f8b7a7891d68383d4561bfae83116bf5bbb
PiSXMe.kicad_pcb  a53e6751a59eb530afd3b522672b5ce967515710bf7eece54a5aa4242e81316e
PiSXMe.kicad_sym  5f017fe96dfcd394939034f490e67596571583226110bd7b2ee54a9c32b2d8f8
bible.md          29040b4dbdc15642bad09ceb9fb53ac391763cf2e1ee14cccd597489439400c4
```

The Mac checkout is under an iCloud/FileProvider-backed path. At handoff,
`.git/HEAD`, the index, and pack metadata were marked dataless and
FileProvider materialization was failing; bounded Git status/add operations
therefore timed out. The Linux thread must verify branch, HEAD, status, and
remote from a fully materialized clone before any edit or commit; do not infer
them from historical reports.

## Settled design basis

- CM5-to-V100 PCIe Gen2 x1 remains the Rev-A basis. No contradictory V100
  evidence was found; the residual sequencing uncertainty is empirical, not an
  architecture blocker.
- Preserve PER0 and the accepted PCIe route unless new physical evidence forces
  a change.
- Preserve CM5/V100 macro zoning, J3/J4 power-entry locations, cooler and
  backplate contracts, dual 12 V input/protection concept, separate CM5 5 V
  rail, and distributed SXM2 power concept.
- Target layer philosophy: F.Cu components/local/high-speed loops; In1 solid
  GND; In2 low-voltage power; In3 protected 12 V; In4 solid GND; B.Cu
  secondary routing. No signal tracks on inner plane layers; ordinary through
  vias only unless explicitly reopened with manufacturing evidence.
- SERVICE remains a USB2 fixed-UFP/recovery/device function. It must not source
  VBUS or retain the old TUSB320/DRP architecture.
- M.2 SATA uses 3.3 V, never 12 V. Use a real SATA-capable B-key or
  B+M-compatible socket and label the product SATA-only; NVMe is not implied.

## Verified findings to carry forward

- U16 TPSM63606 support was not proven complete. FB/RT/PG and the local input,
  output, ground, and thermal network require a reference-derived correction or
  a documented removal decision.
- Q1/Q2 orientation/implementation concerns and TPS2553/USB ESD
  symbol-footprint mismatches are real review items.
- U6/U10 are 10-pad TPD4E05U06 flow-through arrays: signal pads 1/2/4/5,
  GND pads 3/8, NC pads 6/7/9/10. Earlier six-pad wording was inaccurate.
- Literal GND-via count was about five in one audit, but this was a
  classification finding, not proof that all return stitching was absent.
  The active board had about 165 ordinary through-vias in the verified census;
  use functional return-path analysis, not a raw GND-via target.
- The current USB neighborhood contains stale connector-side fragments that do
  not terminate at corrected ESD pads, fragmented USB2 paths, and a failed
  disposable fanout corridor. DRC cleanliness of a proxy copy did not close
  this issue.
- Mechanical evidence includes the F1/Q1 cooler intrusion and J5/J6/J7
  mating-envelope overlap. Keep the existing reports as constraints.
- The repository contains substantial historical routing thrash and stale
  USB-C/mux-era reports. Use current source and the M6 checklist as authority,
  not old acceptance language.

## Tooling state

The bridge is intentionally hybrid:

- PCB operations use the official KiCad Python IPC path (`kicad-python` 0.7.1).
- Schematic operations use a direct `.kicad_sch` backend based on
  `kicad-sch-api` 0.5.6, exposed through `bridge/schematic_backend.py` and
  schematic additions in `server.py`.
- Transactional save/reopen, symbols, wires, labels, sheets, connectivity
  helpers, and project-local symbol registration exist. Basic unit/regression
  tests passed.

The authority gate is still open. KiCad 10.0.5 has no clean headless
schematic-to-PCB update command. Native reopen/ERC was demonstrated for basic
files, but existing PiSXMe round-trip introduced semantic/library warnings and
the complete hierarchy/custom-symbol/schematic-derived PCB authority chain was
not proven. The normal `.venv311` did not have a reproducibly installed
backend at the Mac boundary; wheel metadata also disagreed with runtime
version fields. Do not claim tooling readiness from the unit-test pass alone.

SKiDL 2.3.0 and kinet2pcb 1.1.4 were exercised on Mac with Python 3.11. The
flat fixture generated a usable schematic/netlist and a disposable PCB pad-net
mapping. Genuine hierarchy ERC and custom-part/authority proofs did not close.
The Mac Python environment lacked a usable `pcbnew` module for the kinet2pcb
path, so Linux/NYX is the preferred reproduction host.

Linux success condition:

```text
SKiDL source -> KiCad schematic/netlist -> Linux pcbnew/kinet2pcb
-> .kicad_pcb -> KiCad 10 native parse/ERC/DRC/parity
```

## Exact next task

Do not begin by redesigning PiSXMe. First verify the Linux KiCad, `pcbnew`,
SKiDL, bridge, and symbol-library environment. Then prove a flat source-
authoritative fixture, a genuine hierarchy fixture, and a custom pin-to-pad
mapping fixture. Only after those pass should the new thread construct the
ETHERNET, STORAGE, and SERVICE source-bound islands in that order, validate
them natively, and generate a disposable PCB. No PCB-only proxy nets and no
resumption of the old FAST USB work are allowed.

## Evidence map

Durable M6 evidence is under [`validation/m6/`](validation/m6/) and the
existing [`validation/`](validation/) tree. Reference captures include the
official CM5IO design, TI USB/power material, the EEWorld JMS578 implementation
under [`references/jms578-ee-world/`](references/jms578-ee-world/), and the
MiSaKa capture under [`references/jms578-misaka/`](references/jms578-misaka/).
SKiDL source fixtures are under [`experiments/skidl/`](experiments/skidl/).
The earlier generated spike may still exist under the ignored local
`work/skidl_spike/` directory, but the Linux handoff must reproduce outputs
from the checked-in source rather than depend on that ignored workspace.

## Handoff stop condition

This document does not authorize active-source migration. The Linux thread may
resume M6 only after the tooling authority gate and disposable source-bound
M6 candidate gate both pass. Until then, preserve the hashes above and report
the exact failing validation rather than forcing a route or inventing a net.

## Mac commit status

The documentation/reference changes in this handoff are present in the working
tree but could not be committed or pushed from the Mac checkout: its Git
metadata is an unmaterialized iCloud/FileProvider placeholder and bounded
`git status`/`git add` attempts timed out. The first Linux action is therefore
to clone or fully download the repository, verify the working-tree changes,
then commit the handoff as a normal repository checkpoint. Do not assume a
remote branch or HEAD from this document.
