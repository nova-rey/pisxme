"""V181: keep RSET on a separated B.Cu corridor after the V180 DRC result."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_REFCLK_SUPPORT_RELOCATED_V180.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_REFCLK_SUPPORT_RELOCATED_V181.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
NARROW = 0.10
W = 0.13208


def P(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))


def tr(board, net, layer, start, end, width=W):
    track = pcbnew.PCB_TRACK(board)
    track.SetStart(P(*start))
    track.SetEnd(P(*end))
    track.SetLayer(layer)
    track.SetWidth(pcbnew.FromMM(width))
    track.SetNet(net)
    track.SetNetCode(net.GetNetCode())
    board.Add(track)


def via(board, net, xy):
    item = pcbnew.PCB_VIA(board)
    item.SetPosition(P(*xy))
    item.SetWidth(pcbnew.FromMM(0.6))
    item.SetDrill(pcbnew.FromMM(0.3))
    item.SetLayerPair(F, B)
    item.SetNet(net)
    item.SetNetCode(net.GetNetCode())
    board.Add(item)


def remove_net(board, name):
    for item in list(board.GetTracks()):
        if item.GetNetname() == name:
            board.RemoveNative(item)


def main():
    board = pcbnew.LoadBoard(str(BASE))
    remove_net(board, "RSET")
    rset = board.FindNet("RSET")

    # Exit pad 51 below/left, transition outside the QFN pad field, then use
    # a B.Cu corridor below XTAL_OUT.  Return to F.Cu only at R1 pad 1.
    tr(board, rset, F, (94.05, 65.2), (93.15, 66.0), NARROW)
    via(board, rset, (93.15, 66.0))
    tr(board, rset, B, (93.15, 66.0), (83.4, 66.0), NARROW)
    via(board, rset, (83.4, 66.0))

    board.BuildListOfNets()
    board.Save(str(OUT))
    print(OUT)


if __name__ == "__main__":
    main()
