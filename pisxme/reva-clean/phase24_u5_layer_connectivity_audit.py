"""Audit U5 connectivity using KiCad's native serialized-copper model.

The target table is assertion-only. Connectivity comes from the saved PCB's
actual pads, tracks, vias and filled zones after KiCad rebuilds connectivity.
"""
from pathlib import Path
import sys
import pcbnew

R = Path(__file__).resolve().parent
DEFAULT_BOARD = R / "PHASE24_U5_INTEGRATED_LAYERED.kicad_pcb"
TARGET = {
    "/REGULATORS/BRIDGE_1V1": ["U5.9", "C44.1", "C45.1", "C46.1", "C47.1"],
    "POWER_GND": ["R20.2", "C44.2", "C45.2", "C46.2", "C47.2"],
}

def token(pad):
    return f"{pad.GetParentFootprint().GetReference()}.{pad.GetNumber()}"

def pads_by_token(board):
    return {token(pad): pad for fp in board.GetFootprints() for pad in fp.Pads()}

def native_components(board):
    """Return native connected pad sets; never add expected graph edges."""
    board.BuildConnectivity()
    connectivity = board.GetConnectivity()
    pads = pads_by_token(board)
    components = {}
    for name, members in TARGET.items():
        for member in members:
            if member not in pads:
                raise AssertionError(f"missing serialized pad {member}")
            pad = pads[member]
            if pad.GetNetname() != name:
                raise AssertionError(f"wrong net on {member}: {pad.GetNetname()} != {name}")
            connected = {token(item) for item in connectivity.GetConnectedItems(pad)
                         if type(item).__name__ == "PAD"}
            connected.add(member)
            components[member] = connected
        expected = set(members)
        if not all(expected <= components[member] for member in members):
            details = {m: sorted(components[m] & expected) for m in members}
            raise AssertionError(f"{name} target pads are not natively connected: {details}")
    return components

def audit(board_path=DEFAULT_BOARD):
    board = pcbnew.LoadBoard(str(board_path))
    native_components(board)
    return True

def signature(item):
    return (item.GetNetname(), int(item.GetLayer()), item.GetStart().x,
            item.GetStart().y, item.GetEnd().x, item.GetEnd().y, item.GetWidth())

def negative_controls(board_path=DEFAULT_BOARD):
    """Prove removing an actually connected trace makes the audit fail."""
    source = pcbnew.LoadBoard(str(board_path))
    native_components(source)
    source.BuildConnectivity()
    pads = pads_by_token(source)
    candidates = []
    for member in TARGET["/REGULATORS/BRIDGE_1V1"]:
        for item in source.GetConnectivity().GetConnectedItems(pads[member]):
            if type(item).__name__ == "PCB_TRACK":
                candidates.append((member, signature(item)))
    for member, wanted in candidates:
        trial = pcbnew.LoadBoard(str(board_path))
        victim = next((item for item in trial.GetTracks()
                       if type(item).__name__ == "PCB_TRACK" and signature(item) == wanted), None)
        if victim is None:
            continue
        trial.RemoveNative(victim)
        try:
            native_components(trial)
        except AssertionError:
            return {"removed_member": member, "trace_removal_fails": True}
    raise AssertionError("negative control failed: no necessary target trace was found")

if __name__ == "__main__":
    board_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_BOARD
    audit(board_path)
    print("Phase24 U5 native connectivity audit: PASS")
    if len(sys.argv) > 2 and sys.argv[2] == "--negative-controls":
        print("negative controls:", negative_controls(board_path))
