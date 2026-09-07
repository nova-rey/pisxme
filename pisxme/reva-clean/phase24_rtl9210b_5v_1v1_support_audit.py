#!/usr/bin/env python3
"""Audit the saved Path-B rail components using KiCad connectivity."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
PCB = ROOT / "PHASE24_RTL9210B_5V_PAD17_V3.kicad_pcb"
RAILS = {
    "RTL_5V": {("U1", "17"), ("U1", "33"), ("C5", "1")},
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

def connected_keys(board, anchor):
    board.BuildConnectivity()
    keys = {(anchor.GetParentFootprint().GetReference(), anchor.GetNumber())}
    for item in board.GetConnectivity().GetConnectedItems(anchor):
        if isinstance(item, pcbnew.PAD):
            keys.add((item.GetParentFootprint().GetReference(), item.GetNumber()))
    return keys

board = pcbnew.LoadBoard(str(PCB))
for net, expected in RAILS.items():
    got = connected_keys(board, pad(board, "U1", "17" if net == "RTL_5V" else "16"))
    missing = expected - got
    if missing:
        raise AssertionError(f"{net}: missing native endpoints {sorted(missing)}")
    print(f"PASS native {net}: {len(expected)} asserted endpoints")
