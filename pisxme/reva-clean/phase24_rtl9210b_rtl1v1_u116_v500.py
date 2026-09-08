"""V500: move C4 beside U1.16 and test a bottom-layer 1V1 branch."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
src = H / "PHASE24_RTL9210B_SOURCE_FIELD_V498.kicad_pcb"
out = H / "PHASE24_RTL9210B_RTL1V1_U116_V500.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.13208)

def P(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))

def mm(pos):
    return pcbnew.ToMM(pos.x), pcbnew.ToMM(pos.y)

def track(board, net, layer, a, z):
    t = pcbnew.PCB_TRACK(board)
    t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(layer)
    t.SetWidth(W); t.SetNet(net); t.SetNetCode(net.GetNetCode())
    board.Add(t)

def via(board, net, x, y):
    v = pcbnew.PCB_VIA(board)
    v.SetPosition(P(x, y)); v.SetNet(net); v.SetNetCode(net.GetNetCode())
    v.SetWidth(pcbnew.FromMM(0.6)); v.SetDrill(pcbnew.FromMM(0.3))
    board.Add(v)

board = pcbnew.LoadBoard(str(src))
net = board.FindNet("RTL_1V1")
u1 = board.FindFootprintByReference("U1")
c4 = board.FindFootprintByReference("C4")
c4.SetPosition(P(114.0, 59.0))
a = mm(u1.FindPadByNumber("16").GetPosition())
z = mm(c4.FindPadByNumber("1").GetPosition())
mid = (111.5, 59.2)
track(board, net, F, a, mid)
via(board, net, *mid)
track(board, net, B, mid, (z[0], mid[1]))
via(board, net, z[0], mid[1])
track(board, net, F, (z[0], mid[1]), z)
pcbnew.ZONE_FILLER(board).Fill(board.Zones())
board.Save(str(out))
print(out)
