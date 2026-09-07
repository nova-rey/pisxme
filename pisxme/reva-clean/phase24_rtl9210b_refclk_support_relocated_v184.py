"""V184: move the RSET transition into the verified gap above XTAL_OUT."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_REFCLK_SUPPORT_RELOCATED_V183.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_REFCLK_SUPPORT_RELOCATED_V184.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
NARROW = 0.10


def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))


def tr(board, net, layer, a, z):
    item = pcbnew.PCB_TRACK(board)
    item.SetStart(P(*a)); item.SetEnd(P(*z)); item.SetLayer(layer)
    item.SetWidth(pcbnew.FromMM(NARROW)); item.SetNet(net)
    item.SetNetCode(net.GetNetCode()); board.Add(item)


def via(board, net, xy):
    item = pcbnew.PCB_VIA(board); item.SetPosition(P(*xy))
    item.SetWidth(pcbnew.FromMM(0.6)); item.SetDrill(pcbnew.FromMM(0.3))
    item.SetLayerPair(F, B); item.SetNet(net); item.SetNetCode(net.GetNetCode())
    board.Add(item)


def main():
    board = pcbnew.LoadBoard(str(BASE))
    for item in list(board.GetTracks()):
        if item.GetNetname() == "RSET": board.RemoveNative(item)
    rset = board.FindNet("RSET")
    tr(board, rset, F, (94.05, 65.2), (93.4, 65.2))
    tr(board, rset, F, (93.4, 65.2), (93.4, 67.5))
    via(board, rset, (93.4, 67.5))
    tr(board, rset, B, (93.4, 67.5), (83.4, 68.5))
    via(board, rset, (83.4, 68.5))
    tr(board, rset, F, (83.4, 68.5), (83.4, 66.0))
    board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)


if __name__ == "__main__": main()
