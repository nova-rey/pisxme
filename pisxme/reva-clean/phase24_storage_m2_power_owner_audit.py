#!/usr/bin/env python3
"""Audit the saved M.2 storage-rail connectivity from native PCB objects.

This deliberately derives reachability from KiCad's saved pads, tracks, vias,
and filled zones.  Net names are a scope check, never graph edges.
"""
from pathlib import Path
import sys
import pcbnew

J3_POWER = {"2", "4", "12", "14", "16", "18", "70", "72", "74"}
SOURCE_PADS = [("U12", "13"), ("U12", "20"), ("U12", "30"),
               ("U13", "5"), ("U13", "13"), ("U13", "20"), ("U13", "30"),
               ("R81", "2")]

def pad_map(board):
    return {(f.GetReference(), str(p.GetNumber())): p
            for f in board.GetFootprints() for p in f.Pads()}

def audit(board):
    board.BuildConnectivity()
    pads = pad_map(board)
    j3 = {("J3", n): pads[("J3", n)] for n in J3_POWER}
    sources = {k: pads[k] for k in SOURCE_PADS if k in pads}
    if len(j3) != len(J3_POWER) or not sources:
        return False, ["missing pads/source"]
    reach = {k: board.GetConnectivity().GetConnectedItems(p) for k, p in j3.items()}
    missing = [k for k, items in reach.items()
               if not any(sources[s] in items for s in sources)]
    return not missing, missing

def main(path):
    board = pcbnew.LoadBoard(str(path))
    if board is None:
        raise SystemExit(f"cannot load {path}")
    ok, missing = audit(board)
    if missing:
        print("FAIL M.2 power owner native connectivity")
        print("unreached J3 pads:", ", ".join(f"{r}.{p}" for r, p in missing))
        return 1
    print(f"PASS M.2 power owner native connectivity: {len(J3_POWER)} J3 contacts")
    # The disposable negative control removes one actual saved-board copper
    # object; expected connectivity never supplies an edge.
    negative = pcbnew.LoadBoard(str(path))
    victim = next((x for x in negative.GetTracks()
                   if x.GetNetname() == "STORAGE_3V3"), None)
    if victim is None:
        raise SystemExit("FAIL no STORAGE_3V3 copper available for negative control")
    negative.RemoveNative(victim)
    neg_ok, _ = audit(negative)
    if neg_ok:
        raise SystemExit("FAIL trace-removal negative control did not fail")
    print("PASS trace-removal negative control")
    return 0

if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1]) if len(sys.argv) > 1 else
                   Path(__file__).with_name("PHASE24_STORAGE_CM5_USB4_MONOTONIC_V79_M2_POWER_OWNER.kicad_pcb")))
