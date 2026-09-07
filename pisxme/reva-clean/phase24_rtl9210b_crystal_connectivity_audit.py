#!/usr/bin/env python3
"""Audit crystal and moved RTL_1V1 endpoint components natively."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
PCB = ROOT / "PHASE24_RTL9210B_CRYSTAL_V11.kicad_pcb"
EXPECTED = {
    "XTAL_IN": {("U1", "53"), ("Y1", "1"), ("C1", "1")},
    "XTAL_OUT": {("U1", "54"), ("Y1", "2"), ("C2", "1")},
    "RTL_1V1": {("U1", n) for n in ("16", "36", "40", "50", "55", "60", "63")} | {("C4", "1")},
}

def pad(board, ref, number):
    fp = board.FindFootprintByReference(ref)
    if fp is None:
        raise AssertionError(f"missing footprint {ref}")
    result = fp.FindPadByNumber(number)
    if result is None:
        raise AssertionError(f"missing pad {ref}.{number}")
    return result

def keys(board, anchor):
    board.BuildConnectivity()
    result = {(anchor.GetParentFootprint().GetReference(), anchor.GetNumber())}
    for item in board.GetConnectivity().GetConnectedItems(anchor):
        if isinstance(item, pcbnew.PAD):
            result.add((item.GetParentFootprint().GetReference(), item.GetNumber()))
    return result

def audit(board):
    for net, expected in EXPECTED.items():
        anchor = next(iter(expected))
        missing = expected - keys(board, pad(board, *anchor))
        if missing:
            raise AssertionError(f"{net}: missing native endpoints {sorted(missing)}")
        print(f"PASS native {net}: {len(expected)} asserted endpoints")

def negative_control():
    board = pcbnew.LoadBoard(str(PCB))
    removed = 0
    for item in list(board.GetTracks()):
        if item.GetNetname() == "XTAL_OUT":
            board.RemoveNative(item)
            removed += 1
    if not removed:
        raise AssertionError("negative control found no XTAL_OUT copper")
    try:
        audit(board)
    except AssertionError:
        print("PASS negative control: removed XTAL_OUT copper fails")
    else:
        raise AssertionError("negative control unexpectedly passed")

if __name__ == "__main__":
    audit(pcbnew.LoadBoard(str(PCB)))
    negative_control()
