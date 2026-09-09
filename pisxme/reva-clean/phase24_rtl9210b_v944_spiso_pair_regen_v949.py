"""V949: re-author SPISO/SPISO3 from the clean U1.20 field.

Both nets are deliberately given independent F.Cu source escapes, B.Cu
corridors, transitions, and U2 launches.  This is a disposable native-DRC
candidate; no expected connectivity is synthesized.
"""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / "PHASE24_RTL9210B_V942_U120_CLEANFIELD_V944.kicad_pcb"
OUT = H / "PHASE24_RTL9210B_V944_SPISO_PAIR_REGEN_V949.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.20)

def P(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))

def tr(board, net, pts, layer):
    for a, z in zip(pts, pts[1:]):
        q = pcbnew.PCB_TRACK(board)
        q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(layer)
        q.SetWidth(W); q.SetNet(net); q.SetNetCode(net.GetNetCode())
        board.Add(q)

def via(board, net, xy):
    q = pcbnew.PCB_VIA(board)
    q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(0.60))
    q.SetDrill(pcbnew.FromMM(0.30)); q.SetNet(net)
    q.SetNetCode(net.GetNetCode()); board.Add(q)

board = pcbnew.LoadBoard(str(BASE))

# SPISO3: left source dogbone, upper B.Cu corridor, right-side U2 launch.
n = board.FindNet("SPISO3")
tr(board, n, [(99.6, 66.05), (99.6, 62.5), (97.2, 62.5), (97.2, 60.5)], F)
via(board, n, (97.2, 60.5))
tr(board, n, [(97.2, 60.5), (97.2, 56.5), (102.5, 56.5),
              (106.5, 60.5), (106.5, 72.8)], B)
via(board, n, (106.5, 72.8))
tr(board, n, [(106.5, 72.8), (105.0, 72.8)], F)

# SPISO: separate source transition and lower B.Cu corridor.
n = board.FindNet("SPISO")
tr(board, n, [(99.2, 66.05), (99.2, 64.5), (99.0, 63.5),
              (99.0, 57.0)], F)
via(board, n, (99.0, 57.0))
tr(board, n, [(99.0, 57.0), (99.0, 84.0), (104.5, 84.0),
              (104.5, 78.8)], B)
via(board, n, (104.5, 78.8))
tr(board, n, [(104.5, 78.8), (105.0, 78.8)], F)

board.BuildListOfNets()
pcbnew.ZONE_FILLER(board).Fill(board.Zones())
board.Save(str(OUT))
print(OUT)
