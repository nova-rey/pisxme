"""V1279 native XTAL_IN endpoint and saved-board negative-control audit."""
from pathlib import Path
import pcbnew

P = Path(__file__).resolve().parent / "PHASE24_RTL9210B_XTAL_IN_LIVE_PAD_V1279.kicad_pcb"

def pads(board):
    return {(f.GetReference(), p.GetNumber()): p
            for f in board.GetFootprints() for p in f.Pads()}

b = pcbnew.LoadBoard(str(P))
p = pads(b)
u = p[("U1", "53")]
y = p[("Y1", "1")]
b.BuildConnectivity()
assert y in b.GetConnectivity().GetConnectedItems(u)

# Negative control: remove every XTAL_IN segment from a reloaded copy.  The
# native connectivity graph must then lose the crystal endpoint.
t = pcbnew.LoadBoard(str(P))
pt = pads(t)
for q in list(t.GetTracks()):
    if q.GetNetname() == "XTAL_IN":
        t.RemoveNative(q)
t.BuildConnectivity()
assert pt[("Y1", "1")] not in t.GetConnectivity().GetConnectedItems(pt[("U1", "53")])
print("PASS V1279 native U1.53-to-Y1.1 XTAL_IN endpoint and saved-board negative control")
