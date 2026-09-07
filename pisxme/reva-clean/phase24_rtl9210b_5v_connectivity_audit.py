#!/usr/bin/env python3
"""Audit RTL_5V rail endpoints from native KiCad connectivity only."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
PCB = ROOT / "PHASE24_RTL9210B_5V_PAD17_V3.kicad_pcb"
EXPECTED = {("U1", "17"), ("U1", "33"), ("C5", "1")}

def endpoint(b, ref, number):
    fp = b.FindFootprintByReference(ref)
    if fp is None:
        raise AssertionError(f"missing footprint {ref}")
    pad = fp.FindPadByNumber(number)
    if pad is None:
        raise AssertionError(f"missing pad {ref}.{number}")
    return pad

def component_keys(b, anchor):
    b.BuildConnectivity()
    keys = {(anchor.GetParentFootprint().GetReference(), anchor.GetNumber())}
    for item in b.GetConnectivity().GetConnectedItems(anchor):
        if isinstance(item, pcbnew.PAD):
            keys.add((item.GetParentFootprint().GetReference(), item.GetNumber()))
    return keys

def audit(b):
    got = component_keys(b, endpoint(b, "U1", "17"))
    missing = EXPECTED - got
    if missing:
        raise AssertionError(f"RTL_5V native component missing: {sorted(missing)}")
    print("PASS native RTL_5V U1.17/U1.33/C5.1 connectivity")

def negative_control():
    b = pcbnew.LoadBoard(str(PCB))
    removed = 0
    for item in list(b.GetTracks()):
        if item.GetNetname() == "RTL_5V" and item.GetStart().x == pcbnew.FromMM(83.6):
            b.RemoveNative(item)
            removed += 1
    if not removed:
        raise AssertionError("negative control found no pad-17 escape segment")
    try:
        audit(b)
    except AssertionError:
        print("PASS negative control: removed pad-17 escape fails")
    else:
        raise AssertionError("negative control unexpectedly passed")

if __name__ == "__main__":
    audit(pcbnew.LoadBoard(str(PCB)))
    negative_control()
