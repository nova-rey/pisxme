#!/usr/bin/env python3
"""Native R81 power-attachment audit with a disposable negative control."""
from pathlib import Path
import sys
import pcbnew


def connected(board, a, z):
    board.BuildConnectivity()
    return z in board.GetConnectivity().GetConnectedItems(a)


def main(path):
    board = pcbnew.LoadBoard(str(path))
    if board is None:
        raise SystemExit(f"cannot load {path}")
    r81 = board.FindFootprintByReference("R81")
    u14 = board.FindFootprintByReference("U14")
    if r81 is None or u14 is None:
        raise SystemExit("FAIL missing R81/U14")
    src = r81.FindPadByNumber("2")
    dst = u14.FindPadByNumber("5")
    if src is None or dst is None or src.GetNetname() != "STORAGE_3V3":
        raise SystemExit("FAIL missing or wrongly owned R81/U14 power pads")
    if not connected(board, src, dst):
        raise SystemExit("FAIL R81.2 is not natively connected to U14.5")
    all_tracks = list(board.GetTracks())
    candidates = [(index, item) for index, item in enumerate(all_tracks)
                  if item.GetNetname() == "STORAGE_3V3"]
    if not candidates:
        raise SystemExit("FAIL no saved STORAGE_3V3 copper for negative control")
    for index, _item in candidates:
        negative = pcbnew.LoadBoard(str(path))
        tracks = list(negative.GetTracks())
        if index >= len(tracks):
            continue
        negative.RemoveNative(tracks[index])
        nsrc = negative.FindFootprintByReference("R81").FindPadByNumber("2")
        ndst = negative.FindFootprintByReference("U14").FindPadByNumber("5")
        if not connected(negative, nsrc, ndst):
            print("PASS R81.2->U14.5 native connectivity")
            print("PASS R81 STORAGE_3V3 trace-removal negative control")
            return 0
    raise SystemExit("FAIL removing a necessary R81 power object did not break connectivity")


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1])))
