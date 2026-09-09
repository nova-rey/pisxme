"""V1280 native XTAL_OUT endpoint and saved-board negative-control audit."""
from pathlib import Path
import pcbnew

P = Path(__file__).resolve().parent / "PHASE24_RTL9210B_XTAL_OUT_LIVE_PAD_V1280.kicad_pcb"

def pads(board):
    return {(f.GetReference(), p.GetNumber()): p
            for f in board.GetFootprints() for p in f.Pads()}

b = pcbnew.LoadBoard(str(P))
p = pads(b)
u = p[("U1", "54")]
y = p[("Y1", "2")]
b.BuildConnectivity()
assert y in b.GetConnectivity().GetConnectedItems(u)

t = pcbnew.LoadBoard(str(P))
pt = pads(t)
for q in list(t.GetTracks()):
    if q.GetNetname() == "XTAL_OUT":
        t.RemoveNative(q)
t.BuildConnectivity()
assert pt[("Y1", "2")] not in t.GetConnectivity().GetConnectedItems(pt[("U1", "54")])
print("PASS V1280 native U1.54-to-Y1.2 XTAL_OUT endpoint and saved-board negative control")
