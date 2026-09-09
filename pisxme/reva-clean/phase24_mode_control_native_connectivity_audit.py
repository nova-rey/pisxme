"""Native, saved-PCB audit for the storage mode-control fixture.

Connectivity is obtained only from KiCad's saved-board connectivity graph.
The endpoint table is an assertion set; it never supplies graph edges.
"""
from pathlib import Path
import argparse
import pcbnew

GROUPS = (
    (("J3", "69"), ("J8", "2")),
    (("J8", "4"), ("U14", "2")),
    (("U14", "4"), ("U13", "9")),
    (("U14", "4"), ("U12", "9")),
)

def getpad(board, ref, number):
    fp = board.FindFootprintByReference(ref)
    if fp is None:
        raise AssertionError(f"missing footprint {ref}")
    pad = fp.FindPadByNumber(number)
    if pad is None:
        raise AssertionError(f"missing pad {ref}.{number}")
    return pad

def check(board):
    board.BuildConnectivity()
    conn = board.GetConnectivity()
    failures = []
    for group in GROUPS:
        pads = [getpad(board, *endpoint) for endpoint in group]
        actual = conn.GetConnectedItems(pads[0])
        if pads[1] not in actual:
            failures.append(f"{group[0][0]}.{group[0][1]} not connected to {group[1][0]}.{group[1][1]}")
    return failures

def run(path, negative=False):
    board = pcbnew.LoadBoard(str(path))
    if board is None:
        raise SystemExit(f"cannot load {path}")
    failures = check(board)
    if negative:
        victim = next((item for item in board.GetTracks()
                       if item.GetNetname() == "MODE_IN" and type(item).__name__ == "PCB_TRACK"), None)
        if victim is None:
            raise SystemExit("negative control could not find MODE_IN track")
        board.Remove(victim)
        if not check(board):
            raise SystemExit("negative control did not fail after removing MODE_IN track")
        print("PASS native mode-control negative control: removed MODE_IN track fails")
        return
    if failures:
        for failure in failures:
            print("FAIL", failure)
        raise SystemExit(1)
    print("PASS native mode-control connectivity: 4/4 endpoint groups")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pcb")
    parser.add_argument("--negative-control", action="store_true")
    args = parser.parse_args()
    run(Path(args.pcb), args.negative_control)
