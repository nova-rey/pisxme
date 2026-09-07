#!/usr/bin/env python3
"""Negative control for the selector-inclusive SATA native audit."""
import argparse
import pcbnew

def token(item):
    return f"{item.GetParentFootprint().GetReference()}.{item.GetNumber()}"

def connected(board, left, right):
    board.BuildConnectivity()
    pads={token(p):p for f in board.GetFootprints() for p in f.Pads()}
    return right in {token(x) for x in board.GetConnectivity().GetConnectedItems(pads[left])
                     if type(x).__name__ == "PAD"}

def main():
    ap=argparse.ArgumentParser();ap.add_argument("pcb");a=ap.parse_args()
    left,right,net_name="C30.1","U13.38","TUSB_SATA_TXP"
    base=pcbnew.LoadBoard(a.pcb)
    if base is None or not connected(base,left,right):
        raise SystemExit("baseline selector-side endpoint was not natively connected")
    candidates=[t for t in list(base.GetTracks()) if not isinstance(t,pcbnew.PCB_VIA)
                and (t.GetNetname()==net_name or t.GetNetname().endswith("/"+net_name))]
    for idx, candidate in enumerate(candidates):
        trial=pcbnew.LoadBoard(a.pcb)
        trial_candidates=[t for t in list(trial.GetTracks()) if not isinstance(t,pcbnew.PCB_VIA)
                          and (t.GetNetname()==net_name or t.GetNetname().endswith("/"+net_name))]
        trial.RemoveNative(trial_candidates[idx])
        if not connected(trial,left,right):
            print("PASS selector SATA negative control: removing one saved TUSB_SATA_TXP track disconnects C30.1 -> U13.38")
            return
    raise SystemExit("negative control could not find a necessary selector-side track")

if __name__ == "__main__": main()
