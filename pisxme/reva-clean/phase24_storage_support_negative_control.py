#!/usr/bin/env python3
"""Saved-board negative control for the six-net U11/U12 support primitive."""
from pathlib import Path
import argparse
import pcbnew

CHECKS = (("USB_TXP1", "U11.21", "C86.1"),
          ("USB_TXN1", "U11.22", "C87.1"),
          ("JMS_USB3_TXP", "C86.2", "U12.25"),
          ("JMS_USB3_TXN", "C87.2", "U12.24"),
          ("USB_RXP1", "U11.26", "U12.23"),
          ("USB_RXN1", "U11.27", "U12.22"))

def key(p):
    return f"{p.GetParentFootprint().GetReference()}.{p.GetNumber()}"

def connected(board, left, right):
    board.BuildConnectivity()
    pads = {key(p): p for f in board.GetFootprints() for p in f.Pads()}
    return right in {key(p) for p in board.GetConnectivity().GetConnectedItems(pads[left])
                     if type(p).__name__ == "PAD"}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pcb", type=Path)
    ap.add_argument("negative", type=Path)
    args = ap.parse_args()
    board = pcbnew.LoadBoard(str(args.pcb))
    for net, left, right in CHECKS:
        if not connected(board, left, right):
            raise SystemExit(f"baseline disconnected: {net}")
    removed = next((t for t in board.GetTracks()
                    if t.GetNetname() == "JMS_USB3_TXN"), None)
    if removed is None:
        raise SystemExit("necessary JMS_USB3_TXN track not found")
    board.RemoveNative(removed)
    board.Save(str(args.negative))
    if connected(board, "C87.2", "U12.24"):
        raise SystemExit("negative control failed: removed track did not break JMS_USB3_TXN")
    print("support baseline native connectivity: PASS")
    print("support removed-track negative control: PASS (audit fails as required)")

if __name__ == "__main__":
    main()
