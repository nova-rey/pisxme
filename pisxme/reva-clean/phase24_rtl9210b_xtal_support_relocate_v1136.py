"""V1136: relocate the crystal support pocket and test a separate XTAL_OUT lane."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / "PHASE24_RTL9210B_QFN_GND_ATTACH_V1123.kicad_pcb"
OUT = H / "PHASE24_RTL9210B_XTAL_SUPPORT_RELOCATE_V1136.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.20)

def P(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))

def track(board, net, layer, points):
    for start, end in zip(points, points[1:]):
        item = pcbnew.PCB_TRACK(board)
        item.SetStart(P(*start)); item.SetEnd(P(*end)); item.SetLayer(layer)
        item.SetWidth(W); item.SetNet(net); item.SetNetCode(net.GetNetCode())
        board.Add(item)

def via(board, net, point):
    item = pcbnew.PCB_VIA(board)
    item.SetPosition(P(*point)); item.SetWidth(pcbnew.FromMM(0.60))
    item.SetDrill(pcbnew.FromMM(0.30)); item.SetLayerPair(F, B)
    item.SetNet(net); item.SetNetCode(net.GetNetCode()); board.Add(item)

board = pcbnew.LoadBoard(str(BASE))
for ref, pos in {"Y1": (10.7, 25.0), "C1": (13.6, 28.0), "C2": (10.6, 28.0)}.items():
    footprint = next(f for f in board.GetFootprints() if f.GetReference() == ref)
    footprint.SetPosition(P(*pos))

ni, no = board.FindNet("XTAL_IN"), board.FindNet("XTAL_OUT")
# Separate the two QFN departures, then use independent lower-side lanes.
track(board, ni, F, [(94.05, 67.2), (93.5, 67.2), (93.0, 67.5), (91.5, 68.6)])
via(board, ni, (91.5, 68.6))
track(board, ni, B, [(91.5, 68.6), (91.5, 75.0), (80.0, 75.0), (80.0, 80.0)])
via(board, ni, (80.0, 80.0))
track(board, ni, F, [(80.0, 80.0), (80.0, 83.0)])

track(board, no, F, [(94.05, 67.6), (92.5, 68.8), (90.5, 70.8)])
via(board, no, (90.5, 70.8))
track(board, no, B, [(90.5, 70.8), (90.5, 77.0), (83.0, 77.0), (83.0, 83.0)])
via(board, no, (83.0, 83.0))
track(board, no, F, [(83.0, 83.0), (81.4, 80.0)])
track(board, no, F, [(83.0, 83.0), (83.0, 80.0), (81.4, 80.0)])

board.BuildListOfNets(); pcbnew.ZONE_FILLER(board).Fill(board.Zones())
board.Save(str(OUT)); print(OUT)
