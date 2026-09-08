"""V279: add an offset lower B.Cu SPISO corridor to the retained V278 basis."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_SUPPORT_ROUTE_SPICS_V278.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_SUPPORT_ROUTE_SPISO_V279.kicad_pcb"
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
    board = pcbnew.LoadBoard(str(BASE)); net = board.FindNet("SPISO")
    # Actual pads: U1.23=(99.2,58.05), U2.2=(84.5,70.0).
    via(board, net, (97.0, 57.0)); tr(board, net, F, (99.2, 58.05), (97.0, 57.0))
    tr(board, net, B, (97.0, 57.0), (97.0, 76.0))
    tr(board, net, B, (97.0, 76.0), (84.5, 76.0))
    tr(board, net, B, (84.5, 76.0), (84.5, 68.0)); via(board, net, (84.5, 68.0))
    tr(board, net, F, (84.5, 68.0), (84.5, 70.0))
    board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)


if __name__ == "__main__": main()
