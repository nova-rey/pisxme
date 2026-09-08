"""Disposable V35 RTL_5V source/support co-allocation probe.

All endpoints are taken from the saved V35 board's actual pads.  This is a
route experiment only; it never edits the production schematic or PCB.
"""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_NATIVE_REFILLED.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_RTL5V_PROBE.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
WIDTH = pcbnew.FromMM(0.20)

def mm(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))

def segment(board, net, layer, start, end):
    track = pcbnew.PCB_TRACK(board)
    track.SetStart(mm(*start)); track.SetEnd(mm(*end)); track.SetLayer(layer)
    track.SetWidth(WIDTH); track.SetNet(net); track.SetNetCode(net.GetNetCode())
    board.Add(track)

def via(board, net, xy):
    item = pcbnew.PCB_VIA(board)
    item.SetPosition(mm(*xy)); item.SetWidth(pcbnew.FromMM(0.60))
    item.SetDrill(pcbnew.FromMM(0.30)); item.SetLayerPair(F, B)
    item.SetNet(net); item.SetNetCode(net.GetNetCode()); board.Add(item)

def main():
    board = pcbnew.LoadBoard(str(BASE))
    net = board.FindNet("RTL_5V")
    # Native V35 pad coordinates: U1.33, U1.17, and C5.1.
    # Escape the QFN pads before each ordinary through-via; no via-in-pad.
    segment(board, net, F, (95.20, 66.05), (93.00, 64.80))
    via(board, net, (93.00, 64.80))
    segment(board, net, B, (93.00, 64.80), (93.00, 55.00))
    via(board, net, (93.00, 55.00))
    segment(board, net, F, (93.00, 55.00), (116.40, 55.00))
    via(board, net, (116.40, 55.00))
    segment(board, net, B, (116.40, 55.00), (116.40, 67.80))
    segment(board, net, F, (116.40, 67.80), (116.40, 69.00))
    segment(board, net, F, (101.95, 66.80), (104.00, 65.60))
    via(board, net, (104.00, 65.60))
    segment(board, net, B, (104.00, 65.60), (104.00, 55.00))
    board.BuildListOfNets()
    pcbnew.ZONE_FILLER(board).Fill(board.Zones())
    board.Save(str(OUT))
    print(OUT)

if __name__ == "__main__":
    main()
