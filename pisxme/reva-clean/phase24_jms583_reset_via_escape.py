"""Disposable native-pad JMS583 reset escape using an ordinary via corridor."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_DUAL_MODE_STORAGE_PLACEMENT_CURRENT.kicad_pcb"
OUT = R / "PHASE24_JMS583_RESET_VIA_ESCAPE.kicad_pcb"
def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def add_track(board, net, a, z, layer):
    t = pcbnew.PCB_TRACK(board); t.SetStart(P(*a)); t.SetEnd(P(*z))
    t.SetLayer(layer); t.SetWidth(pcbnew.FromMM(.20)); t.SetNet(net)
    t.SetNetCode(net.GetNetCode()); board.Add(t)
def add_via(board, net, q):
    v = pcbnew.PCB_VIA(board); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(.60))
    v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
    v.SetNet(net); v.SetNetCode(net.GetNetCode()); board.Add(v)

b = pcbnew.LoadBoard(str(BASE))
u11 = b.FindFootprintByReference('U11'); r81 = b.FindFootprintByReference('R81')
net = b.FindNet('JMS_RESET_N')
if not u11 or not r81 or not net: raise RuntimeError('missing reset fixture object')
for item in list(b.GetTracks()):
    if item.GetNetCode() == net.GetNetCode(): b.RemoveNative(item)
src = u11.FindPadByNumber('15').GetPosition(); dst = r81.FindPadByNumber('1').GetPosition()
s = (pcbnew.ToMM(src.x), pcbnew.ToMM(src.y)); d = (pcbnew.ToMM(dst.x), pcbnew.ToMM(dst.y))
# Leave the QFN field on F.Cu, cross the open west corridor on B.Cu, and
# return beside the passive. Both transitions are ordinary through-vias.
v1, v2 = (134.0, 140.0), (118.0, 140.0)
add_track(b, net, s, (134.0, s[1]), pcbnew.F_Cu)
add_track(b, net, (134.0, s[1]), v1, pcbnew.F_Cu); add_via(b, net, v1)
add_track(b, net, v1, v2, pcbnew.B_Cu); add_via(b, net, v2)
add_track(b, net, v2, (118.0, d[1]), pcbnew.F_Cu)
add_track(b, net, (118.0, d[1]), d, pcbnew.F_Cu)
b.Save(str(OUT)); print(OUT)
