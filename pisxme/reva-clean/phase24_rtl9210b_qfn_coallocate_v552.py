"""V552: reallocate XTAL_OUT to free a clean bottom RTL_1V1 collector."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
src = H / "PHASE24_RTL9210B_QFN_COALLOCATE_V546.kicad_pcb"
out = H / "PHASE24_RTL9210B_QFN_COALLOCATE_V552.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.13208)

def P(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))

def tr(board, net, layer, a, z):
    t = pcbnew.PCB_TRACK(board)
    t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(layer); t.SetWidth(W)
    t.SetNet(net); t.SetNetCode(net.GetNetCode()); board.Add(t)

def via(board, net, a):
    v = pcbnew.PCB_VIA(board)
    v.SetPosition(P(*a)); v.SetLayerPair(F, B)
    v.SetNet(net); v.SetNetCode(net.GetNetCode())
    v.SetWidth(pcbnew.FromMM(0.6)); v.SetDrill(pcbnew.FromMM(0.3))
    board.Add(v)

b = pcbnew.LoadBoard(str(src))
n1 = b.FindNet("RTL_1V1")
nx = b.FindNet("XTAL_OUT")

# Remove only the prior XTAL_OUT copper; the far crystal-side launch remains
# the authority, and is rejoined at its existing B.Cu endpoint.
for item in list(b.GetTracks()):
    if item.GetNetname() == "XTAL_OUT":
        b.RemoveNative(item)

# Move XTAL_OUT away from the lower QFN pad field.
tr(b, nx, F, (103.6, 65.95), (103.6, 64.0))
tr(b, nx, F, (103.6, 64.0), (99.0, 64.0))
via(b, nx, (99.0, 64.0))
tr(b, nx, B, (99.0, 64.0), (99.0, 43.5))
tr(b, nx, B, (99.0, 43.5), (105.0, 43.5))
tr(b, nx, B, (105.0, 43.5), (105.0, 44.0))

# Escape the three bottom RTL_1V1 pads, collect on B.Cu, and return through
# a new F.Cu handoff left of the existing 3V3 field.
for a, z in [
    ((104.0, 65.95), (104.0, 67.5)),
    ((106.0, 65.95), (106.0, 67.5)),
    ((107.2, 65.95), (107.2, 67.5)),
]:
    tr(b, n1, F, a, z); via(b, n1, z)
tr(b, n1, B, (104.0, 67.5), (99.0, 67.5))
tr(b, n1, B, (106.0, 67.5), (104.0, 67.5))
tr(b, n1, B, (107.2, 67.5), (106.0, 67.5))
via(b, n1, (99.0, 67.5))
tr(b, n1, F, (99.0, 67.5), (99.0, 61.2))
tr(b, n1, F, (99.0, 61.2), (99.5, 61.2))

b.BuildListOfNets()
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(out))
print(out)
