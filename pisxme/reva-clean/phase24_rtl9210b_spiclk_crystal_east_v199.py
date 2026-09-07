"""V199: modest east crystal-cluster translation to clear SPICLK."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_SPISO_U123_U2_V193.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_SPICLK_CRYSTAL_EAST_V199.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu


def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))


def tr(board, net, layer, a, z):
    item = pcbnew.PCB_TRACK(board)
    item.SetStart(P(*a)); item.SetEnd(P(*z)); item.SetLayer(layer)
    item.SetWidth(pcbnew.FromMM(0.20)); item.SetNet(net)
    item.SetNetCode(net.GetNetCode()); board.Add(item)


def via(board, net, xy):
    item = pcbnew.PCB_VIA(board); item.SetPosition(P(*xy))
    item.SetWidth(pcbnew.FromMM(0.60)); item.SetDrill(pcbnew.FromMM(0.30))
    item.SetLayerPair(F, B); item.SetNet(net); item.SetNetCode(net.GetNetCode())
    board.Add(item)


def remove_net(board, name):
    for item in list(board.GetTracks()):
        if item.GetNetname() == name: board.RemoveNative(item)


def main():
    board = pcbnew.LoadBoard(str(BASE))
    for ref, xy in (("Y1", (90.0, 60.0)), ("C1", (87.5, 60.0)),
                    ("C2", (92.5, 60.0)), ("R1", (78.0, 66.0))):
        board.FindFootprintByReference(ref).SetPosition(P(*xy))
    for name in ("XTAL_IN", "XTAL_OUT", "RSET", "SPICLK"):
        remove_net(board, name)
    xi, xo = board.FindNet("XTAL_IN"), board.FindNet("XTAL_OUT")
    rs, clk = board.FindNet("RSET"), board.FindNet("SPICLK")

    tr(board, xi, F, (95.2, 65.95), (95.2, 67.2)); tr(board, xi, F, (95.2, 67.2), (94.5, 67.2))
    via(board, xi, (94.5, 67.2)); tr(board, xi, B, (94.5, 67.2), (89.8, 61.0)); via(board, xi, (89.8, 61.0))
    tr(board, xi, F, (89.8, 61.0), (89.3, 60.0)); tr(board, xi, F, (89.3, 60.0), (88.1, 60.0))

    tr(board, xo, F, (95.6, 65.95), (96.0, 68.0)); tr(board, xo, F, (96.0, 68.0), (89.2, 68.0))
    tr(board, xo, F, (89.2, 68.0), (90.7, 60.0)); tr(board, xo, F, (90.7, 60.0), (91.9, 60.0))

    tr(board, rs, F, (94.05, 65.2), (93.4, 65.2)); tr(board, rs, F, (93.4, 65.2), (93.4, 68.5))
    via(board, rs, (93.4, 68.5)); tr(board, rs, B, (93.4, 68.5), (77.4, 68.5)); via(board, rs, (77.4, 68.5))
    tr(board, rs, F, (77.4, 68.5), (77.4, 66.0))

    tr(board, clk, F, (100.8, 58.05), (100.8, 57.2)); tr(board, clk, F, (100.8, 57.2), (101.4, 57.2))
    tr(board, clk, F, (101.4, 57.2), (101.4, 50.0)); via(board, clk, (101.4, 50.0))
    tr(board, clk, B, (101.4, 50.0), (87.8, 50.0)); via(board, clk, (87.8, 50.0)); tr(board, clk, F, (87.8, 50.0), (87.8, 72.0))
    board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)


if __name__ == "__main__": main()
