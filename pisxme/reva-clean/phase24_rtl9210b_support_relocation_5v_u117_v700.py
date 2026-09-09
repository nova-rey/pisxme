"""V700: connect U1.17 RTL_5V to the retained V699 source/C5 trunk."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / 'PHASE24_RTL9210B_SUPPORT_RELOCATION_5V_OVERPASS_FINAL_V699.kicad_pcb'
OUT = H / 'PHASE24_RTL9210B_SUPPORT_RELOCATION_5V_U117_V700.kicad_pcb'
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.20)

def P(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))

def track(board, net, layer, start, end):
    q = pcbnew.PCB_TRACK(board)
    q.SetStart(P(*start)); q.SetEnd(P(*end)); q.SetLayer(layer)
    q.SetWidth(W); q.SetNet(net); q.SetNetCode(net.GetNetCode())
    board.Add(q)

def via(board, net, xy):
    q = pcbnew.PCB_VIA(board)
    q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(0.60))
    q.SetDrill(pcbnew.FromMM(0.30)); q.SetLayerPair(F, B)
    q.SetNet(net); q.SetNetCode(net.GetNetCode()); board.Add(q)

board = pcbnew.LoadBoard(str(BASE))
net = board.FindNet('RTL_5V')
# Leave the QFN bottom-edge pad field on F.Cu, then take an ordinary-via
# handoff below the existing 1V1 B.Cu shelves and rise outside the field.
track(board, net, F, (101.20, 73.95), (101.20, 75.50))
track(board, net, F, (101.20, 75.50), (103.50, 75.50))
via(board, net, (103.50, 75.50))
track(board, net, B, (103.50, 75.50), (108.50, 75.50))
track(board, net, B, (108.50, 75.50), (108.50, 50.00))
track(board, net, B, (108.50, 50.00), (106.00, 50.00))
board.BuildListOfNets()
pcbnew.ZONE_FILLER(board).Fill(board.Zones())
board.Save(str(OUT))
print(OUT)
