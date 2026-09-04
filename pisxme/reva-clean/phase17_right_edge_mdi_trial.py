"""Phase-17 discriminator: CM5IO Ethernet ESD local, MagJack at right edge."""
from pathlib import Path
import os
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = Path(os.environ.get("PISXME_BASE", ROOT / "ACREAGE_PHASE17_F1RIGHT40_ETH_GROUND_FIXED.kicad_pcb"))
OUT = Path(os.environ.get("PISXME_OUT", ROOT / "ACREAGE_PHASE17_RIGHT_EDGE_MDI.kicad_pcb"))
WIDTH = pcbnew.FromMM(0.13208)

def V(x, y): return pcbnew.VECTOR2I_MM(x, y)
def xy(p): return (pcbnew.ToMM(p.x), pcbnew.ToMM(p.y))
def net(board, name):
    result = board.FindNet(name) or board.FindNet("/ETHERNET/" + name) or board.FindNet("/" + name)
    if result is None: raise RuntimeError("missing net " + name)
    return result
def pad(board, ref, number):
    fp = board.FindFootprintByReference(ref)
    p = fp.FindPadByNumber(str(number))
    if p is None: raise RuntimeError(f"missing {ref}.{number}")
    return xy(p.GetPosition())
def segment(board, n, a, z, layer=pcbnew.F_Cu):
    t = pcbnew.PCB_TRACK(board)
    t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer); t.SetWidth(WIDTH); t.SetNet(n)
    board.Add(t)
def route(board, n, points, layer=pcbnew.F_Cu):
    for a, z in zip(points, points[1:]): segment(board, n, a, z, layer)
def via(board, n, point):
    q = pcbnew.PCB_VIA(board)
    q.SetPosition(V(*point)); q.SetWidth(pcbnew.FromMM(0.50)); q.SetDrill(pcbnew.FromMM(0.30))
    q.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu); q.SetNet(n); board.Add(q)

board = pcbnew.LoadBoard(str(BASE))
j2 = board.FindFootprintByReference("J2")
j2.SetPosition(V(282.5, 53)); j2.SetOrientationDegrees(180)

names = {
    "CM5_GBE_TD3_P": ("J7", 3, "U9", 5, "J2", 9),
    "CM5_GBE_TD3_N": ("J7", 5, "U9", 4, "J2", 10),
    "CM5_GBE_TD2_N": ("J7", 9, "U9", 2, "J2", 8),
    "CM5_GBE_TD2_P": ("J7", 11, "U9", 1, "J2", 7),
    "CM5_GBE_TD1_P": ("J7", 4, "U6", 5, "J2", 3),
    "CM5_GBE_TD1_N": ("J7", 6, "U6", 4, "J2", 6),
    "CM5_GBE_TD0_N": ("J7", 10, "U6", 2, "J2", 2),
    "CM5_GBE_TD0_P": ("J7", 12, "U6", 1, "J2", 1),
}
endpoints = {n: (pad(board, a, b), pad(board, c, d), pad(board, e, f)) for n, (a,b,c,d,e,f) in names.items()}
for item in list(board.GetTracks()):
    if item.GetNetname().split("/")[-1].startswith(("CM5_GBE_TD", "ETH_", "GBE_")):
        board.Remove(item)

# Preserve the proven CM5/J7-to-ESD escape from the accepted local candidate.
local = {
 "CM5_GBE_TD3_P": [(32.960,99.100),(33.910,98.821),(64.421,67.210),(73.704,67.210),(74.160,66.754)],
 "CM5_GBE_TD3_N": [(32.960,99.500),(34.290,98.979),(64.579,67.590),(73.862,67.590),(74.540,66.912)],
 "CM5_GBE_TD2_N": [(32.960,100.300),(34.810,99.321),(34.810,98.121),(64.821,68.110),(74.521,68.110),(75.660,66.971)],
 "CM5_GBE_TD2_P": [(32.960,100.700),(35.190,99.479),(35.190,98.279),(64.979,68.490),(74.679,68.490),(76.040,67.129)],
 "CM5_GBE_TD1_P": [(36.040,99.100),(37.210,98.521),(37.210,97.121),(65.321,69.010),(78.021,69.010),(80.160,66.871)],
 "CM5_GBE_TD1_N": [(36.040,99.500),(37.590,98.679),(37.590,97.279),(65.479,69.390),(78.179,69.390),(80.540,67.029)],
 "CM5_GBE_TD0_N": [(36.040,100.300),(36.731,100.300),(38.210,98.821),(38.210,97.521),(65.821,69.910),(78.321,69.910),(81.660,66.571)],
 "CM5_GBE_TD0_P": [(36.040,100.700),(36.869,100.700),(38.590,98.979),(38.590,97.679),(65.979,70.290),(78.479,70.290),(82.040,66.729)],
}
for name, points in local.items():
    route(board, net(board, name), [endpoints[name][0]] + points[1:] + [endpoints[name][1]])

# Two F.Cu pairs use separate monotonic outboard corridors.
top = {
 "CM5_GBE_TD3_P": [(74.160,66.754),(74.160,90.0),(276.785,90.0),(276.785,59.350)],
 "CM5_GBE_TD3_N": [(74.540,66.912),(74.540,89.0),(278.055,89.0),(278.055,61.890)],
 "CM5_GBE_TD1_P": [(80.160,66.871),(80.160,86.0),(281.865,86.0),(281.865,59.350)],
 "CM5_GBE_TD1_N": [(79.0,67.029),(79.0,85.0),(285.675,85.0),(285.675,61.890)],
}
for name, points in top.items(): route(board, net(board, name), points)

# TD2 and TD0 make ordinary through-via transitions in unique, separated
# lanes, remain on B.Cu over the permitted In4 reference, then return beside
# the connector. No signal is placed on an internal plane layer.
bottom = {
 "CM5_GBE_TD2_P": (76.8, 74.0, 280.0, 88.0, 280.595, 88.0, 280.595, 61.890),
 "CM5_GBE_TD2_N": (77.8, 74.0, 279.0, 87.0, 279.325, 87.0, 279.325, 59.350),
 "CM5_GBE_TD0_P": (82.8, 74.0, 288.0, 84.0, 288.215, 84.0, 288.215, 61.890),
 "CM5_GBE_TD0_N": (83.8, 74.0, 286.7, 83.0, 286.945, 83.0, 286.945, 59.350),
}
for name, (x0,y0,x1,y1,x2,y2,x3,y3) in bottom.items():
    q = net(board, name); start = endpoints[name][1]; finish = endpoints[name][2]
    v0 = (x0, y0); v1 = (x1, y1)
    route(board, q, [start, (x0, start[1]), v0])
    via(board, q, v0); route(board, q, [v0, v1], pcbnew.B_Cu); via(board, q, v1)
    route(board, q, [(x2, y2), finish])

pcbnew.ZONE_FILLER(board).Fill(board.Zones())
pcbnew.SaveBoard(str(OUT), board)
print(f"saved {OUT}")
