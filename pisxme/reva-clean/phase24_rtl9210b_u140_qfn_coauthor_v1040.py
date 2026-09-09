"""V1040: scrub local 1V1/3V3 copper before joint QFN-field allocation."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / "PHASE24_RTL9210B_1V1_U163_V1019.kicad_pcb"
OUT = H / "PHASE24_RTL9210B_U140_QFN_COAUTHOR_V1040.kicad_pcb"
F, B, L = pcbnew.F_Cu, pcbnew.B_Cu, pcbnew.In2_Cu
W = pcbnew.FromMM(0.20)

def P(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))

def add(board, net, pts, layer):
    for a, z in zip(pts, pts[1:]):
        q = pcbnew.PCB_TRACK(board)
        q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(layer)
        q.SetWidth(W); q.SetNet(net); q.SetNetCode(net.GetNetCode())
        board.Add(q)

def via(board, net, xy):
    q = pcbnew.PCB_VIA(board); q.SetPosition(P(*xy))
    q.SetWidth(pcbnew.FromMM(0.60)); q.SetDrill(pcbnew.FromMM(0.30))
    q.SetNet(net); q.SetNetCode(net.GetNetCode()); board.Add(q)

board = pcbnew.LoadBoard(str(BASE))
n3, n1 = board.FindNet("RTL_3V3"), board.FindNet("RTL_1V1")
for q in list(board.GetTracks()):
    if q.GetNetCode() not in {n3.GetNetCode(), n1.GetNetCode()}:
        continue
    s, e = q.GetStart(), q.GetEnd()
    xs = [s.x / 1e6, e.x / 1e6]; ys = [s.y / 1e6, e.y / 1e6]
    # Remove only the QFN/support-field acreage; remote rails remain intact.
    if max(xs) < 106 and min(xs) > 84 and max(ys) < 78 and min(ys) > 54:
        board.Remove(q)

# 3V3: source pad 34 into a vertical B.Cu spine; pad 39 gets a short F.Cu
# branch and its own transition.  The remote rail uses the east/top corridor.
add(board, n3, [(94.8, 66.05), (92.5, 65.5)], F)
via(board, n3, (92.5, 65.5))
add(board, n3, [(92.5, 65.5), (92.5, 74.8)], B)
via(board, n3, (92.5, 67.2)); via(board, n3, (92.5, 74.8))
add(board, n3, [(94.05, 68.4), (93.2, 68.4), (93.2, 67.2), (92.5, 67.2)], F)
add(board, n3, [(94.8, 73.95), (92.5, 74.8)], F)
add(board, n3, [(92.5, 65.5), (95.0, 65.5), (95.0, 59.5),
                (100.4, 59.5), (100.4, 60.8)], B)

# 1V1 pad 40 exits west on F.Cu, then transitions below the 3V3 field.
add(board, n1, [(94.05, 68.8), (90.8, 68.8)], F)
via(board, n1, (90.8, 68.8))
add(board, n1, [(90.8, 68.8), (90.5, 68.8)], L)

board.BuildListOfNets(); pcbnew.ZONE_FILLER(board).Fill(board.Zones())
board.Save(str(OUT)); print(OUT)
