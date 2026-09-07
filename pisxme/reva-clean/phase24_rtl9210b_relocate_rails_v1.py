"""Disposable 3V3/5V rail escapes for the relocated RTL9210B island."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_SUPPORT_RELOCATION_CAPS_V1.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_SUPPORT_RELOCATION_RAILS_V1.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.20)

def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def seg(board, net, layer, a, z):
    t = pcbnew.PCB_TRACK(board); t.SetStart(P(*a)); t.SetEnd(P(*z))
    t.SetLayer(layer); t.SetWidth(W); t.SetNet(net)
    t.SetNetCode(net.GetNetCode()); board.Add(t)
def via(board, net, q):
    v = pcbnew.PCB_VIA(board); v.SetPosition(P(*q))
    v.SetWidth(pcbnew.FromMM(0.60)); v.SetDrill(pcbnew.FromMM(0.30))
    v.SetLayerPair(F, B); v.SetNet(net); v.SetNetCode(net.GetNetCode())
    board.Add(v)
def rail(board, name, src, sv, dv, dst, bend=None):
    n = board.FindNet(name)
    seg(board, n, F, src, sv); via(board, n, sv)
    seg(board, n, B, sv, bend or dv)
    if bend is not None: seg(board, n, B, bend, dv)
    via(board, n, dv)
    seg(board, n, F, dv, dst)

def main():
    board = pcbnew.LoadBoard(str(BASE))
    # U1.20 RTL_3V3 -> C3.1; U1.17 RTL_5V -> C5.1.
    rail(board, "RTL_3V3", (101.95, 72.4), (110.0, 72.4),
         (109.6, 68.5), (110.4, 69.0), bend=(110.0, 68.5))
    rail(board, "RTL_5V", (101.2, 73.95), (115.6, 73.95),
         (115.6, 68.5), (116.4, 69.0))
    board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)

if __name__ == "__main__": main()
