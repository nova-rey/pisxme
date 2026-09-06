"""Assert USB3 endpoint connectivity from saved native KiCad objects.

The expected endpoint membership is assertion-only.  Connectivity is derived
from KiCad BuildConnectivity over the saved pads, tracks, and vias; this audit
does not add graph edges or infer contact from XY alone.
"""
from pathlib import Path
import sys
import pcbnew

ROOT = Path(__file__).resolve().parent
BOARD = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "PHASE24_STORAGE_USB3_REFERENCE_ESCAPE.kicad_pcb"
ENDPOINTS = {
    "CM5_USB3_RX_N": ("J7.128", "U7.42"),
    "CM5_USB3_RX_P": ("J7.130", "U7.43"),
    "CM5_USB3_TX_N": ("J7.140", "U7.45"),
    "CM5_USB3_TX_P": ("J7.142", "U7.46"),
}

def token(pad):
    return f"{pad.GetParentFootprint().GetReference()}.{pad.GetNumber()}"

board = pcbnew.LoadBoard(str(BOARD))
if board is None:
    raise SystemExit(f"cannot load {BOARD}")
board.BuildConnectivity()
conn = board.GetConnectivity()
pads = {
    token(pad): pad
    for footprint in board.GetFootprints()
    for pad in footprint.Pads()
}

for net, members in ENDPOINTS.items():
    for member in members:
        pad = pads.get(member)
        if pad is None:
            raise AssertionError(f"missing endpoint {member}")
        if not pad.GetNetname().endswith("/" + net):
            raise AssertionError(f"wrong net on {member}: {pad.GetNetname()}")
    for member in members:
        reached = {token(item) for item in conn.GetConnectedItems(pads[member])
                   if type(item).__name__ == "PAD"}
        reached.add(member)
        if not set(members) <= reached:
            raise AssertionError(f"{net} disconnected at {member}: {sorted(reached)}")
    print(f"{net}: PASS ({members[0]} <-> {members[1]})")
print("USB3 native endpoint connectivity: PASS")
