#!/usr/bin/env python3
"""Regenerate the project-local U12 RUA0042A footprint with pcbnew.

Authority: P24-PACKAGE-AUTHORITY-U12-U11-20260918-R1.
This script intentionally changes only pad centres and the courtyard of the
named project-local footprint.  Pad numbers, pad sizes, layers, attributes,
and the exposed-pad contract are preserved.
"""

from __future__ import annotations

import json
from pathlib import Path

import pcbnew


ROOT = Path("/workspace/project/pisxme/reva-clean")
LIB = ROOT / "PiSXMe_RevA_Clean.pretty"
NAME = "HD3SS6126_RUA0042A"
RAW = ROOT / "validation-receipts/u12-rua0042a-footprint-producer-20260918/raw"
RAW.mkdir(parents=True, exist_ok=True)


def mm(value: float) -> int:
    return pcbnew.FromMM(value)


def xy(x: float, y: float) -> pcbnew.VECTOR2I:
    return pcbnew.VECTOR2I(mm(x), mm(y))


footprint = pcbnew.FootprintLoad(str(LIB), NAME)
if footprint is None:
    raise SystemExit(f"failed to load {LIB / (NAME + '.kicad_mod')}")

pads = {pad.GetNumber(): pad for pad in footprint.Pads()}
expected = {str(index) for index in range(1, 44)}
if set(pads) != expected:
    raise SystemExit(f"unexpected pad set: {sorted(pads)}")

# TI RUA0042A example land-pattern coordinates.  Numbering/orientation follows
# the existing schematic and project footprint: counter-clockwise from pin 1
# at the upper end of the left long-side row.
positions: dict[str, tuple[float, float]] = {}
for index in range(1, 18):
    positions[str(index)] = (-1.65, -4.0 + 0.5 * (index - 1))
for index, x_pos in zip(range(18, 22), (0.75, 0.25, -0.25, -0.75)):
    positions[str(index)] = (x_pos, 4.5)
for index in range(22, 39):
    positions[str(index)] = (1.65, 4.0 - 0.5 * (index - 22))
for index, x_pos in zip(range(39, 43), (-0.75, -0.25, 0.25, 0.75)):
    positions[str(index)] = (x_pos, -4.5)
positions["43"] = (0.0, 0.0)

for number, position in positions.items():
    pads[number].SetPosition(xy(*position))

# The old courtyard was inside the end-pad copper.  Use the standard 0.25 mm
# courtyard clearance around the regenerated land extents: x +/-1.95 and
# y +/-4.80, yielding x +/-2.20 and y +/-5.05.
courtyard = [
    item
    for item in footprint.GraphicalItems()
    if pcbnew.LayerName(item.GetLayer()) == "F.Courtyard"
]
if len(courtyard) != 1 or not isinstance(courtyard[0], pcbnew.PCB_SHAPE):
    raise SystemExit(f"expected one F.CrtYd PCB_SHAPE, got {len(courtyard)}")
shape = courtyard[0]
if shape.GetShape() != pcbnew.SHAPE_T_RECT:
    raise SystemExit(f"expected rectangular courtyard, got {shape.GetShape()}")
shape.SetStart(xy(-2.20, -5.05))
shape.SetEnd(xy(2.20, 5.05))

# KiCad 10's SWIG wrapper returns ``None`` after a successful save.  Reloading
# and auditing the serialized footprint below is the success criterion.
pcbnew.FootprintSave(str(LIB), footprint)

serialized = pcbnew.FootprintLoad(str(LIB), NAME)
if serialized is None:
    raise SystemExit("serialized footprint could not be reloaded")
serialized_pads = {pad.GetNumber(): pad for pad in serialized.Pads()}
if set(serialized_pads) != expected:
    raise SystemExit("serialized pad-number set changed")

report = {
    "schema": "pisxme.p24.u12-footprint-mutation.v1",
    "kicad_version": pcbnew.Version(),
    "authority": "P24-PACKAGE-AUTHORITY-U12-U11-20260918-R1",
    "footprint": f"{NAME}.kicad_mod",
    "pad_count": len(pads),
    "positions_mm": positions,
    "courtyard_mm": {"x0": -2.20, "y0": -5.05, "x1": 2.20, "y1": 5.05},
}
(RAW / "mutation-report.json").write_text(
    json.dumps(report, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(report, indent=2))
