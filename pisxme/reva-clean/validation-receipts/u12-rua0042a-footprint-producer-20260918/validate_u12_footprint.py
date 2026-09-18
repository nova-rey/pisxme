#!/usr/bin/env python3
"""Focused native validation for the U12 RUA0042A footprint candidate."""

from __future__ import annotations

import json
import xml.etree.ElementTree as ET
from pathlib import Path

import pcbnew


ROOT = Path("/workspace/project/pisxme/reva-clean")
OUT = ROOT / "validation-receipts/u12-rua0042a-footprint-producer-20260918/raw/native-validation.json"
LIB = ROOT / "PiSXMe_RevA_Clean.pretty"
NAME = "HD3SS6126_RUA0042A"
BOARD = ROOT / "PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb"
NETLIST = Path("/workspace/output/u12-candidate-native.xml")


def mm(value: int) -> float:
    return round(pcbnew.ToMM(value), 6)


expected_positions: dict[str, tuple[float, float]] = {}
for index in range(1, 18):
    expected_positions[str(index)] = (-1.65, -4.0 + 0.5 * (index - 1))
for index, x_pos in zip(range(18, 22), (0.75, 0.25, -0.25, -0.75)):
    expected_positions[str(index)] = (x_pos, 4.5)
for index in range(22, 39):
    expected_positions[str(index)] = (1.65, 4.0 - 0.5 * (index - 22))
for index, x_pos in zip(range(39, 43), (-0.75, -0.25, 0.25, 0.75)):
    expected_positions[str(index)] = (x_pos, -4.5)
expected_positions["43"] = (0.0, 0.0)

fp = pcbnew.FootprintLoad(str(LIB), NAME)
if fp is None:
    raise SystemExit("candidate footprint did not load")
pads = {pad.GetNumber(): pad for pad in fp.Pads()}
expected_numbers = {str(index) for index in range(1, 44)}
checks: dict[str, bool] = {}
checks["pad_number_set_1_through_43"] = set(pads) == expected_numbers
checks["pad_centres_match_ti_contract"] = all(
    (mm(pads[number].GetPosition().x), mm(pads[number].GetPosition().y)) == position
    for number, position in expected_positions.items()
)
checks["signal_land_size_0p60_by_0p25"] = all(
    (mm(pads[str(index)].GetSize().x), mm(pads[str(index)].GetSize().y)) == (0.6, 0.25)
    for index in range(1, 43)
)
checks["exposed_pad_2p05_by_7p55"] = (
    mm(pads["43"].GetSize().x), mm(pads["43"].GetSize().y)
) == (2.05, 7.55)
checks["signal_and_ep_layers_preserved"] = all(
    {pcbnew.LayerName(layer) for layer in pad.GetLayerSet().Seq()}
    == {"F.Cu", "F.Mask", "F.Paste"}
    for pad in pads.values()
)
checks["end_row_rotation_90_degrees"] = all(
    round(pads[str(index)].GetOrientationDegrees(), 6) == 90.0
    for index in list(range(18, 22)) + list(range(39, 43))
)
checks["side_row_rotation_zero"] = all(
    round(pads[str(index)].GetOrientationDegrees(), 6) == 0.0
    for index in list(range(1, 18)) + list(range(22, 39))
)

courtyard = [
    item for item in fp.GraphicalItems()
    if pcbnew.LayerName(item.GetLayer()) == "F.Courtyard"
]
checks["single_rectangular_courtyard"] = (
    len(courtyard) == 1
    and isinstance(courtyard[0], pcbnew.PCB_SHAPE)
    and courtyard[0].GetShape() == pcbnew.SHAPE_T_RECT
)
if checks["single_rectangular_courtyard"]:
    checks["courtyard_4p40_by_10p10"] = (
        mm(abs(courtyard[0].GetEnd().x - courtyard[0].GetStart().x)),
        mm(abs(courtyard[0].GetEnd().y - courtyard[0].GetStart().y)),
    ) == (4.4, 10.1)
else:
    checks["courtyard_4p40_by_10p10"] = False

board = pcbnew.LoadBoard(str(BOARD))
board_u12 = [item for item in board.GetFootprints() if item.GetReference() == "U12"]
checks["selected_board_has_one_u12"] = len(board_u12) == 1
board_pad_nets: dict[str, str] = {}
if board_u12:
    board_pads = {pad.GetNumber(): pad for pad in board_u12[0].Pads()}
    checks["selected_board_u12_pad_ids_match"] = set(board_pads) == expected_numbers
    board_pad_nets = {number: pad.GetNetname() for number, pad in sorted(board_pads.items(), key=lambda x: int(x[0]))}
else:
    checks["selected_board_u12_pad_ids_match"] = False

tree = ET.parse(NETLIST)
component = tree.find(".//components/comp[@ref='U12']")
assignment = component.findtext("footprint") if component is not None else None
schematic_nodes = sorted(
    {node.attrib["pin"] for node in tree.findall(".//node[@ref='U12']")},
    key=int,
)
checks["native_netlist_has_u12"] = component is not None
checks["schematic_footprint_assignment_matches"] = assignment == f"PiSXMeRevAClean:{NAME}"
checks["all_native_u12_nodes_have_candidate_pads"] = set(schematic_nodes) <= expected_numbers

report = {
    "schema": "pisxme.p24.u12-footprint-validation.v1",
    "kicad_version": pcbnew.Version(),
    "authority": "P24-PACKAGE-AUTHORITY-U12-U11-20260918-R1",
    "source_board": str(BOARD.relative_to(ROOT)),
    "checks": checks,
    "status": "PASS" if all(checks.values()) else "FAIL",
    "schematic_footprint_assignment": assignment,
    "schematic_connected_u12_pins": schematic_nodes,
    "selected_board_u12_pad_nets": board_pad_nets,
}
OUT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, indent=2))
if report["status"] != "PASS":
    raise SystemExit(1)
