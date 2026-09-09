"""V978: source-row-only orthogonal escape discriminator.

This intentionally stops at open F.Cu dogbones.  It tests whether the QFN
source field can be exited without lateral pad-field crossings before adding
through-via transitions and remote support routes.
"""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / "PHASE24_RTL9210B_V926_SPISI_REGEN_V927.kicad_pcb"
OUT = H / "PHASE24_RTL9210B_ORTHOGONAL_SOURCE_ESCAPE_V978.kicad_pcb"
F = pcbnew.F_Cu
W = pcbnew.FromMM(0.20)

def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))

def tr(board, net, points):
    for a, z in zip(points, points[1:]):
        q = pcbnew.PCB_TRACK(board)
        q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F)
        q.SetWidth(W); q.SetNet(net); q.SetNetCode(net.GetNetCode())
        board.Add(q)

board = pcbnew.LoadBoard(str(BASE))
local = {
    "RTL_1V1", "RTL_3V3", "RTL_5V", "RSET", "XTAL_IN", "XTAL_OUT",
    "PEDET", "CLKREQ_N", "PERST_N", "SPISI", "SPICLK", "SPISO3",
    "SPISO", "SPICS",
}
for item in list(board.GetTracks()):
    if item.GetNetname() in local:
        board.RemoveNative(item)

# Keep every departure orthogonal to the horizontal pad row.  The two
# right-hand signals leave downward, away from the exposed pad and side row;
# the remaining source signals leave upward.  No via is added in this probe.
routes = {
    "SPICS": [(98.8, 66.05), (98.8, 64.0)],
    "SPISO": [(99.2, 66.05), (99.2, 63.6)],
    "SPISO3": [(99.6, 66.05), (99.6, 63.2)],
    "RTL_3V3": [(100.4, 66.05), (100.4, 62.8)],
    "SPICLK": [(100.8, 66.05), (100.8, 68.0)],
    "SPISI": [(101.2, 66.05), (101.2, 68.4)],
}
for name, points in routes.items():
    tr(board, board.FindNet(name), points)

board.BuildListOfNets()
pcbnew.ZONE_FILLER(board).Fill(board.Zones())
board.Save(str(OUT))
print(OUT)
