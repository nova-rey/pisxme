"""Native SPICS endpoint audit and negative control for V278."""
from pathlib import Path
import sys
import pcbnew

HERE = Path(__file__).resolve().parent
DEFAULT = HERE / "PHASE24_RTL9210B_SUPPORT_ROUTE_SPICS_V278.kicad_pcb"


def key(pad):
    f = pad.GetParentFootprint()
    return f"{f.GetReference()}.{pad.GetNumber()}"


def pads(board):
    return {key(p): p for f in board.GetFootprints() for p in f.Pads()}


def joined(board, start):
    board.BuildConnectivity()
    return {key(x) for x in board.GetConnectivity().GetConnectedItems(start)
            if type(x).__name__ == "PAD"} | {key(start)}


def audit(path):
    board = pcbnew.LoadBoard(str(path))
    ps = pads(board)
    for endpoint in ("U1.24", "U2.1"):
        assert endpoint in ps, endpoint
        assert str(ps[endpoint].GetNetname()) == "SPICS", endpoint
    assert {"U1.24", "U2.1"} <= joined(board, ps["U1.24"])
    assert {"U1.24", "U2.1"} <= joined(board, ps["U2.1"])
    print("SPICS native U1.24 <-> U2.1: PASS")


def negative(path):
    board = pcbnew.LoadBoard(str(path)); ps = pads(board)
    board.BuildConnectivity()
    items = [x for x in board.GetConnectivity().GetConnectedItems(ps["U1.24"])
             if type(x).__name__ == "PCB_TRACK" and x.GetNetname() == "SPICS"]
    assert items, "no SPICS track available for negative control"
    victim = items[0]
    board.RemoveNative(victim)
    try:
        assert {"U1.24", "U2.1"} <= joined(board, ps["U1.24"])
    except AssertionError:
        print("SPICS trace-removal negative control: PASS")
        return
    raise AssertionError("removing a necessary SPICS trace did not fail audit")


if __name__ == "__main__":
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    audit(path)
    if "--negative-controls" in sys.argv[2:]: negative(path)
