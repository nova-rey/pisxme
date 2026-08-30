#!/usr/bin/env python3
"""Trial a source-to-local-VBUS-field connection on a disposable board."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

import pcbnew

from finalize_zones_and_thermal import add_zone, mm


def track(board: pcbnew.BOARD, net: str, layer: int, width: float,
          points: list[tuple[float, float]]) -> None:
    code = board.FindNet(net).GetNetCode()
    for a, b in zip(points, points[1:]):
        t = pcbnew.PCB_TRACK(board)
        t.SetStart(pcbnew.VECTOR2I(mm(a[0]), mm(a[1])))
        t.SetEnd(pcbnew.VECTOR2I(mm(b[0]), mm(b[1])))
        t.SetWidth(mm(width))
        t.SetLayer(layer)
        t.SetNetCode(code)
        board.Add(t)


def build(source: Path, output: Path) -> None:
    shutil.copy2(source, output)
    board = pcbnew.LoadBoard(str(output))
    net = "/USB_FAST_A_VBUS"
    add_zone(
        board, layer=pcbnew.F_Cu, net=net, netcode=board.FindNet(net).GetNetCode(),
        name="TRIAL_A_VBUS_PAD_FIELD", points=[(208.9, 54.7), (212.1, 54.7),
        (212.1, 61.3), (208.9, 61.3)], priority=3, clearance=0.05,
        thermal_gap=0.10, thermal_spoke=0.20, solid=True,
    )
    # The source pad exits to the east, then angles into the field from a
    # clear left-side corridor.  This is a short current path, not a global
    # top-layer pour.
    track(board, net, pcbnew.F_Cu, 0.25,
          [(203.25, 51.5), (205.5, 51.5), (208.9, 54.7)])
    board.BuildConnectivity()
    pcbnew.ZONE_FILLER(board).Fill(board.Zones())
    pcbnew.SaveBoard(str(output), board)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--board", required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path)
    args = ap.parse_args()
    build(args.board, args.output)


if __name__ == "__main__":
    main()
