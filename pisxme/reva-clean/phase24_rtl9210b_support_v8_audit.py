"""Saved-board native audit for the V8 RTL9210B support-route baseline.

Connectivity is derived only from KiCad's saved pads/tracks/vias/zones.  The
negative control removes one required XTAL_OUT track and must fail.
"""
from pathlib import Path
import sys
import pcbnew

TARGET = {
    "XTAL_IN": (("U1", "53"), ("Y1", "1"), ("C1", "1")),
    "XTAL_OUT": (("U1", "54"), ("Y1", "2"), ("C2", "1")),
    "RSET": (("U1", "51"), ("R1", "1")),
}


def pad(board, ref, number):
    fp = board.FindFootprintByReference(ref)
    if fp is None:
        raise AssertionError(f"missing footprint {ref}")
    result = fp.FindPadByNumber(number)
    if result is None:
        raise AssertionError(f"missing pad {ref}.{number}")
    return result


def key(item):
    return (str(item.GetParentFootprint().GetReference()), str(item.GetNumber()))


def audit(board):
    board.BuildConnectivity()
    connectivity = board.GetConnectivity()
    for net, endpoints in TARGET.items():
        anchor = pad(board, *endpoints[0])
        reached = {key(item) for item in connectivity.GetConnectedItems(anchor)
                   if isinstance(item, pcbnew.PAD)} | {endpoints[0]}
        missing = set(endpoints) - reached
        if missing:
            raise AssertionError(f"{net}: missing {sorted(missing)}")
        print(f"PASS native {net}: {len(endpoints)} endpoints")


def negative_control(path):
    board = pcbnew.LoadBoard(str(path))
    board.BuildConnectivity()
    anchor = pad(board, "U1", "54")
    victim = next((item for item in board.GetConnectivity().GetConnectedItems(anchor)
                   if isinstance(item, pcbnew.PCB_TRACK)
                   and item.GetNetname() == "XTAL_OUT"), None)
    if victim is None:
        raise AssertionError("negative control found no XTAL_OUT track")
    board.RemoveNative(victim)
    try:
        audit(board)
    except AssertionError:
        print("PASS negative control: removed XTAL_OUT copper fails")
        return
    raise AssertionError("negative control unexpectedly passed")


if __name__ == "__main__":
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name(
        "PHASE24_RTL9210B_ROTATED_SUPPORT_RELOCATION_V8.kicad_pcb")
    board = pcbnew.LoadBoard(str(path))
    audit(board)
    negative_control(path)
