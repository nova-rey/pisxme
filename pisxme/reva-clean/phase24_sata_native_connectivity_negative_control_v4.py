#!/usr/bin/env python3
"""Negative control for the native V4 SATA connectivity audit.

The audit's expected endpoint list is assertion-only. This control removes a
real saved track from the V4 board, rebuilds KiCad connectivity, and requires
the corresponding native endpoint connection to disappear.
"""
import argparse
import pcbnew


def token(item):
    return f"{item.GetParentFootprint().GetReference()}.{item.GetNumber()}"


def connected(board, left, right):
    board.BuildConnectivity()
    pads = {token(p): p for f in board.GetFootprints() for p in f.Pads()}
    reached = {token(item) for item in board.GetConnectivity().GetConnectedItems(pads[left])
               if type(item).__name__ == "PAD"}
    return right in reached


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pcb")
    args = ap.parse_args()
    board = pcbnew.LoadBoard(args.pcb)
    if board is None:
        raise SystemExit("native board load failed")

    left, right, net_name = "C30.1", "J3.49", "M2_SATA_A_P_PCIE_TXP0"
    if not connected(board, left, right):
        raise SystemExit("baseline V4 endpoint was not natively connected")

    candidates = [t for t in list(board.GetTracks())
                  if not isinstance(t, pcbnew.PCB_VIA)
                  and (t.GetNetname() == net_name or t.GetNetname().endswith("/" + net_name))]
    for candidate in candidates:
        board.RemoveNative(candidate)
        if not connected(board, left, right):
            print("PASS SATA negative control: removing one real saved track disconnected C30.1 -> J3.49")
            return
        # Re-load the untouched input for the next candidate. This keeps the
        # trial independent and avoids synthetic graph edits.
        board = pcbnew.LoadBoard(args.pcb)
    raise SystemExit("negative control could not find a necessary saved track")


if __name__ == "__main__":
    main()
