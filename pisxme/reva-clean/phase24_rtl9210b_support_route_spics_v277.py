"""V277: route SPICS below the retained crystal trunks on B.Cu."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_SUPPORT_ROUTE_RAILS_V274.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_SUPPORT_ROUTE_SPICS_V277.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu


def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))


def tr(board, net, layer, a, z):
    item = pcbnew.PCB_TRACK(board); item.SetStart(P(*a)); item.SetEnd(P(*z))
    item.SetLayer(layer); item.SetWidth(pcbnew.FromMM(0.20)); item.SetNet(net)
    item.SetNetCode(net.GetNetCode()); board.Add(item)


def via(board, net, xy):
    item = pcbnew.PCB_VIA(board); item.SetPosition(P(*xy)); item.SetWidth(pcbnew.FromMM(0.50))
    item.SetDrill(pcbnew.FromMM(0.25)); item.SetLayerPair(F, B); item.SetNet(net)
    item.SetNetCode(net.GetNetCode()); board.Add(item)


def main():
    board = pcbnew.LoadBoard(str(BASE)); net = board.FindNet("SPICS")
    # Actual pads: U1.24=(98.8,58.05), U2.1=(83.3,70.0).
    via(board, net, (98.8, 57.0)); tr(board, net, F, (98.8, 58.05), (98.8, 57.0))
    tr(board, net, B, (98.8, 57.0), (98.8, 72.0))
    tr(board, net, B, (98.8, 72.0), (83.3, 72.0))
    tr(board, net, B, (83.3, 72.0), (83.3, 68.0)); via(board, net, (83.3, 68.0))
    tr(board, net, F, (83.3, 68.0), (83.3, 70.0))
    board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)


if __name__ == "__main__": main()
