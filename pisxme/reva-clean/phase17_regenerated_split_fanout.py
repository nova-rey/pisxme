"""Disposable Phase-17 split-island trial with regenerated J7 fanout.

The outboard island geometry is supplied by the CM5IO transplant.  This
script removes only the translated source-side MDI copper and regenerates
the J7-to-ESD escape with explicit ordinary through-vias for the interleaved
TD2/TD0 groups.  Connector-side CM5IO launch/support copper is retained.
"""
from pathlib import Path
import os
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = Path(os.environ.get("PISXME_BASE", ROOT / "ACREAGE_PHASE17_SPLIT_OUTBOARD_ETH.kicad_pcb"))
OUT = Path(os.environ.get("PISXME_OUT", ROOT / "ACREAGE_PHASE17_REGENERATED_SPLIT.kicad_pcb"))
W = pcbnew.FromMM(0.13208)

def V(x, y): return pcbnew.VECTOR2I_MM(x, y)
def xy(p): return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)
def net(b, name):
    n = b.FindNet(name)
    if n is None: raise RuntimeError(name)
    return n
def pad(b, ref, number):
    f = b.FindFootprintByReference(ref)
    p = f.FindPadByNumber(str(number))
    if p is None: raise RuntimeError(f"{ref}.{number}")
    return xy(p.GetPosition())
def track(b, n, a, z, layer):
    q = pcbnew.PCB_TRACK(b); q.SetStart(V(*a)); q.SetEnd(V(*z));
    q.SetLayer(layer); q.SetWidth(W); q.SetNet(n); b.Add(q)
def via(b, n, p):
    q = pcbnew.PCB_VIA(b); q.SetPosition(V(*p)); q.SetWidth(pcbnew.FromMM(.50));
    q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu); q.SetNet(n); b.Add(q)
def route(b, n, points, layer):
    for a, z in zip(points, points[1:]): track(b, n, a, z, layer)

b = pcbnew.LoadBoard(str(BASE))
names = [f"CM5_GBE_TD{i}_{p}" for i in range(4) for p in "PN"]
codes = {net(b, n).GetNetCode() for n in names}
j7 = {n: pad(b, "J7", {"CM5_GBE_TD3_P":"3","CM5_GBE_TD3_N":"5",
                         "CM5_GBE_TD2_N":"9","CM5_GBE_TD2_P":"11",
                         "CM5_GBE_TD1_P":"4","CM5_GBE_TD1_N":"6",
                         "CM5_GBE_TD0_N":"10","CM5_GBE_TD0_P":"12"}[n]) for n in names}
esd = {"CM5_GBE_TD3_P":pad(b,"U9","5"), "CM5_GBE_TD3_N":pad(b,"U9","4"),
       "CM5_GBE_TD2_P":pad(b,"U9","1"), "CM5_GBE_TD2_N":pad(b,"U9","2"),
       "CM5_GBE_TD1_P":pad(b,"U6","5"), "CM5_GBE_TD1_N":pad(b,"U6","4"),
       "CM5_GBE_TD0_P":pad(b,"U6","1"), "CM5_GBE_TD0_N":pad(b,"U6","2")}
# Remove source-side translated MDI copper only.  All connector-side
# geometry is beyond x=230 in this +180 mm outboard candidate.
for item in list(b.GetTracks()):
    if item.GetNetCode() not in codes: continue
    pts = [item.GetPosition()] if isinstance(item, pcbnew.PCB_VIA) else [item.GetStart(), item.GetEnd()]
    if any(pcbnew.ToMM(p.x) < 230.0 for p in pts): b.Remove(item)

# Same-layer pair corridors are monotonic; TD2 and TD0 use B.Cu to avoid the
# source-column P/N inversion, with ordinary vias outside J7 and ESD pads.
fpaths = {
 "CM5_GBE_TD3_P": [j7["CM5_GBE_TD3_P"], (50,98.0),(180,98.0),esd["CM5_GBE_TD3_P"]],
 "CM5_GBE_TD3_N": [j7["CM5_GBE_TD3_N"], (50,99.0),(180,99.0),esd["CM5_GBE_TD3_N"]],
 "CM5_GBE_TD1_P": [j7["CM5_GBE_TD1_P"], (50,102.0),(180,102.0),esd["CM5_GBE_TD1_P"]],
 "CM5_GBE_TD1_N": [j7["CM5_GBE_TD1_N"], (50,103.0),(180,103.0),esd["CM5_GBE_TD1_N"]],
}
for n, pts in fpaths.items(): route(b, net(b,n), pts, pcbnew.F_Cu)

bpaths = {
 "CM5_GBE_TD2_N": ((40.0,100.3),(248.0,96.0),(251.0,103.8)),
 "CM5_GBE_TD2_P": ((40.8,100.7),(248.0,97.0),(251.5,103.8)),
 "CM5_GBE_TD0_N": ((42.0,100.3),(248.0,106.0),(258.0,103.8)),
 "CM5_GBE_TD0_P": ((42.8,100.7),(248.0,107.0),(258.5,103.8)),
}
for n, pts in bpaths.items():
    nobj = net(b,n); via(b,nobj,pts[0]); route(b,nobj,[pts[0]]+list(pts[1:]),pcbnew.B_Cu)
    # dogbone from the ESD-side transition to the corresponding pad
    route(b,nobj,[pts[-1],esd[n]],pcbnew.F_Cu); via(b,nobj,pts[-1])

pcbnew.ZONE_FILLER(b).Fill(b.Zones()); pcbnew.SaveBoard(str(OUT), b)
print(f"saved {OUT}; regenerated {len(names)} source MDI nets")
