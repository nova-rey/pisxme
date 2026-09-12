"""Native four-link audit for the M-key USB3 actual-pad probe.

Connectivity is derived only from saved pads/tracks/vias.  The expected
endpoint table is an assertion, and the optional negative control removes one
serialized route segment to prove the audit is sensitive to missing copper.
"""
from pathlib import Path
import argparse
import pcbnew

CHECKS = (
    ("CM5_USB3_RX_N", "J7.128", "U12.16"),
    ("CM5_USB3_RX_P", "J7.130", "U12.15"),
    ("CM5_USB3_TX_N", "J7.140", "U12.12"),
    ("CM5_USB3_TX_P", "J7.142", "U12.11"),
)


def token(pad):
    return f"{pad.GetParentFootprint().GetReference()}.{pad.GetNumber()}"


def pads(board):
    return {token(p): p for f in board.GetFootprints() for p in f.Pads()}


def connected(board, left, right):
    board.BuildConnectivity()
    return token(right) in {token(x) for x in board.GetConnectivity().GetConnectedItems(left)
                            if type(x).__name__ == "PAD"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pcb", type=Path)
    ap.add_argument("--negative-control", action="store_true")
    args = ap.parse_args()
    board = pcbnew.LoadBoard(str(args.pcb))
    if board is None:
        raise SystemExit(f"cannot load {args.pcb}")
    p = pads(board)
    for net, left_name, right_name in CHECKS:
        left = p.get(left_name); right = p.get(right_name)
        if left is None or right is None:
            raise SystemExit(f"missing endpoint {left_name} or {right_name}")
        for endpoint in (left, right):
            if endpoint.GetNetname().rsplit("/", 1)[-1] != net:
                raise SystemExit(f"wrong net on {token(endpoint)}: {endpoint.GetNetname()}")
        if not connected(board, left, right):
            raise SystemExit(f"FAIL {net}: {left_name} -> {right_name}")
        print(f"PASS {net}: {left_name} <-> {right_name}")

    if args.negative_control:
        victim = next((x for x in board.GetTracks()
                       if not isinstance(x, pcbnew.PCB_VIA)
                       and x.GetNetname() == CHECKS[0][0]), None)
        if victim is None:
            raise SystemExit("negative control found no serialized route segment")
        board.RemoveNative(victim)
        board.BuildConnectivity()
        if connected(board, p[CHECKS[0][1]], p[CHECKS[0][2]]):
            raise SystemExit("FAIL negative control: removed route still connected")
        print("PASS negative control: removed RX_N route segment disconnects endpoint")

    print("M-key USB3 actual-pad four-link audit: PASS")


if __name__ == "__main__":
    main()
