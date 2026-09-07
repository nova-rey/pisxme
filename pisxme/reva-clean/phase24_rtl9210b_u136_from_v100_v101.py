"""V101: add the remaining U1.36 RTL_1V1 edge handoff to V100."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / 'PHASE24_RTL9210B_XTALOUT_U155_LEFT_ESCAPE_V100.kicad_pcb'
OUT = HERE / 'PHASE24_RTL9210B_U136_FROM_V100_V101.kicad_pcb'
F, B = pcbnew.F_Cu, pcbnew.B_Cu

def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def add_track(board, net, layer, a, z):
    t = pcbnew.PCB_TRACK(board); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(layer)
    t.SetWidth(pcbnew.FromMM(.15)); t.SetNet(net); t.SetNetCode(net.GetNetCode()); board.Add(t)
def add_via(board, net, at):
    v = pcbnew.PCB_VIA(board); v.SetPosition(P(*at)); v.SetWidth(pcbnew.FromMM(.60))
    v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F, B); v.SetNet(net); v.SetNetCode(net.GetNetCode()); board.Add(v)

def main():
    board = pcbnew.LoadBoard(str(BASE)); net = board.FindNet('RTL_1V1')
    # Native pad-derived U1.36 departure, via, and same-net collector join.
    add_track(board, net, F, (94.05, 67.2), (92.8, 67.2))
    add_via(board, net, (92.8, 67.2))
    add_track(board, net, B, (92.8, 67.2), (92.8, 69.0))
    board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)

if __name__ == '__main__': main()
