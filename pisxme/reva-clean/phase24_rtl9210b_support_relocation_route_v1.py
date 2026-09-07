"""Regenerate the first complete moved support branch from native pads.

Only the local XTAL/RSET/RTL_1V1 copper is copied from the staged oracle and
translated with the moved island.  The external 1V1 leg is newly authored;
SPI/control/rail destinations remain intentionally open for later stages.
"""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_1V1_CRYSTAL_RSET_STAGED_V4.kicad_pcb"
PLACED = HERE / "PHASE24_RTL9210B_SUPPORT_RELOCATION_V2.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_SUPPORT_RELOCATION_ROUTE_V2.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
DX, DY = 18.0, 8.0
W = pcbnew.FromMM(0.20)

def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def shift(q): return P(q.x / 1e6 + DX, q.y / 1e6 + DY)
def add_seg(board, net, layer, a, z):
    t = pcbnew.PCB_TRACK(board); t.SetStart(a); t.SetEnd(z)
    t.SetLayer(layer); t.SetWidth(W); t.SetNet(net)
    t.SetNetCode(net.GetNetCode()); board.Add(t)
def add_via(board, net, q):
    v = pcbnew.PCB_VIA(board); v.SetPosition(q)
    v.SetWidth(pcbnew.FromMM(0.60)); v.SetDrill(pcbnew.FromMM(0.30))
    v.SetLayerPair(F, B); v.SetNet(net); v.SetNetCode(net.GetNetCode())
    board.Add(v)

def main():
    src = pcbnew.LoadBoard(str(BASE)); board = pcbnew.LoadBoard(str(PLACED))
    names = {name: board.FindNet(name) for name in
             ("XTAL_IN", "XTAL_OUT", "RSET", "RTL_1V1")}
    for item in src.GetTracks():
        name = str(item.GetNetname())
        if name not in names: continue
        pts = ([item.GetPosition()] if isinstance(item, pcbnew.PCB_VIA)
               else [item.GetStart(), item.GetEnd()])
        xy = [(q.x / 1e6, q.y / 1e6) for q in pts]
        if not all(62 <= x <= 88 and 45 <= y <= 72 for x, y in xy):
            continue
        net = names[name]
        if isinstance(item, pcbnew.PCB_VIA):
            add_via(board, net, shift(item.GetPosition()))
        else:
            add_seg(board, net, item.GetLayer(), shift(item.GetStart()),
                    shift(item.GetEnd()))
    # New outboard 1V1 continuation from the translated local collector to C4.
    net = names["RTL_1V1"]
    for a, z in [(P(103.2, 71.2), P(105.0, 71.2)),
                 (P(105.0, 71.2), P(105.0, 41.0)),
                 (P(105.0, 41.0), P(123.4, 41.0))]:
        add_seg(board, net, B, a, z)
    add_via(board, net, P(123.4, 41.0))
    add_seg(board, net, F, P(123.4, 41.0), P(123.4, 51.0))
    board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)

if __name__ == "__main__": main()
