"""Disposable 180-degree U1.39-to-U2.8 RTL_3V3 corridor probe."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / 'PHASE24_RTL9210B_QFN_ORIENTATION180_PROBE.kicad_pcb'
OUT = HERE / 'PHASE24_RTL9210B_ORIENTATION180_U139_PROBE.kicad_pcb'
F, B = pcbnew.F_Cu, pcbnew.B_Cu
WIDTH = pcbnew.FromMM(0.20)

def point(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))

def track(board, net, layer, start, end):
    item = pcbnew.PCB_TRACK(board)
    item.SetStart(point(*start)); item.SetEnd(point(*end))
    item.SetLayer(layer); item.SetWidth(WIDTH); item.SetNet(net)
    item.SetNetCode(net.GetNetCode()); board.Add(item)

def via(board, net, position):
    item = pcbnew.PCB_VIA(board); item.SetPosition(point(*position))
    item.SetWidth(pcbnew.FromMM(0.60)); item.SetDrill(pcbnew.FromMM(0.30))
    item.SetLayerPair(F, B); item.SetNet(net); item.SetNetCode(net.GetNetCode())
    board.Add(item)

board = pcbnew.LoadBoard(str(BASE))
net = board.FindNet('RTL_3V3')
# The path leaves U1.39 on the lower edge, changes layer outside the QFN,
# crosses the open lower corridor, and returns beside the U2 endpoint field.
track(board, net, F, (96.4, 73.95), (96.4, 75.2))
via(board, net, (96.4, 75.2))
track(board, net, B, (96.4, 75.2), (80.2, 75.2))
via(board, net, (80.2, 75.2))
track(board, net, F, (80.2, 75.2), (80.2, 80.0))
board.BuildListOfNets()
pcbnew.ZONE_FILLER(board).Fill(board.Zones())
board.Save(str(OUT))
print(OUT)
