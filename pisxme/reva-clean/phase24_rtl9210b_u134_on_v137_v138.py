"""V138: apply the promoted U1.34 RTL_3V3 escape to the V137 rail basis."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_RTL5V_BELOW_C5_V137.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_U134_ON_V137_V138.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu

def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def tr(board, net, layer, a, z):
    q = pcbnew.PCB_TRACK(board); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(layer)
    q.SetWidth(pcbnew.FromMM(.20)); q.SetNet(net); q.SetNetCode(net.GetNetCode()); board.Add(q)
def via(board, net, xy):
    q = pcbnew.PCB_VIA(board); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60))
    q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F, B); q.SetNet(net); q.SetNetCode(net.GetNetCode()); board.Add(q)

def main():
    board = pcbnew.LoadBoard(str(BASE)); net = board.FindNet("RTL_3V3")
    tr(board, net, F, (94.8, 66.05), (93.6, 66.05))
    tr(board, net, F, (93.6, 66.05), (93.6, 62.0)); via(board, net, (93.6, 62.0))
    tr(board, net, B, (93.6, 62.0), (98.8, 62.0))
    tr(board, net, B, (98.8, 62.0), (98.8, 61.2))
    tr(board, net, B, (98.8, 61.2), (100.4, 61.2))
    tr(board, net, B, (100.4, 61.2), (100.4, 60.8)); via(board, net, (100.4, 60.8))
    board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)

if __name__ == "__main__": main()
