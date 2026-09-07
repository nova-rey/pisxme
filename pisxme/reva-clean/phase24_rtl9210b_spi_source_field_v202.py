"""V202: co-author RTL_3V3, SPICLK, SPISI, and C1 destination field."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_SPICLK_CRYSTAL_EAST_V200.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_SPI_SOURCE_FIELD_V202.kicad_pcb"
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
    board.FindFootprintByReference("C1").SetPosition(P(89.0, 60.0))
    for name in ("RTL_3V3", "SPICLK", "SPISI", "XTAL_IN"):
        remove_net(board, name)
    rail = board.FindNet("RTL_3V3")
    clk = board.FindNet("SPICLK")
    si = board.FindNet("SPISI")
    xi = board.FindNet("XTAL_IN")

    # Rebuild the V185 U1.34-to-C3.1 rail with U1.20 joining above the SPI field.
    tr(board, rail, F, (94.8, 58.05), (93.8, 56.5)); via(board, rail, (93.8, 56.5))
    tr(board, rail, B, (93.8, 56.5), (110.4, 56.5)); via(board, rail, (110.4, 56.5))
    tr(board, rail, F, (110.4, 56.5), (110.4, 61.0))
    tr(board, rail, F, (100.4, 58.05), (100.4, 54.5)); via(board, rail, (100.4, 54.5))
    tr(board, rail, B, (100.4, 54.5), (93.8, 54.5)); via(board, rail, (93.8, 54.5))
    tr(board, rail, F, (93.8, 54.5), (93.8, 56.5))

    # Co-authored top-row source exits and separate destination columns.
    tr(board, clk, F, (100.8, 58.05), (100.8, 56.8)); tr(board, clk, F, (100.8, 56.8), (101.4, 56.8))
    tr(board, clk, F, (101.4, 56.8), (101.4, 50.0)); via(board, clk, (101.4, 50.0))
    tr(board, clk, B, (101.4, 50.0), (87.8, 50.0)); via(board, clk, (87.8, 50.0)); tr(board, clk, F, (87.8, 50.0), (87.8, 72.0))

    tr(board, si, F, (101.2, 58.05), (101.2, 57.2)); tr(board, si, F, (101.2, 57.2), (102.6, 57.2))
    tr(board, si, F, (102.6, 57.2), (102.6, 46.5)); via(board, si, (102.6, 46.5))
    tr(board, si, B, (102.6, 46.5), (86.6, 46.5)); via(board, si, (86.6, 46.5)); tr(board, si, F, (86.6, 46.5), (86.6, 72.0))

    # Re-terminate XTAL_IN at the transformed C1.1=(89.6,60.0).
    tr(board, xi, F, (95.2, 65.95), (95.2, 67.2)); tr(board, xi, F, (95.2, 67.2), (94.5, 67.2))
    via(board, xi, (94.5, 67.2)); tr(board, xi, B, (94.5, 67.2), (89.8, 61.0)); via(board, xi, (89.8, 61.0))
    tr(board, xi, F, (89.8, 61.0), (89.3, 60.0)); tr(board, xi, F, (89.3, 60.0), (89.6, 60.0))
    board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)


if __name__ == "__main__": main()
