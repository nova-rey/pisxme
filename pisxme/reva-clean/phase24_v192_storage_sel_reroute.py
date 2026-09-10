"""Disposable V192 STORAGE_SEL reroute using saved native pad positions."""
from pathlib import Path
import sys, pcbnew

R=Path(__file__).resolve().parent
BASE=R/'PHASE24_STORAGE_V75_COAUTHORED_V192.kicad_pcb'
OUT=R/'PHASE24_STORAGE_V75_COAUTHORED_V193.kicad_pcb'
if len(sys.argv)>1: BASE=R/sys.argv[1]
if len(sys.argv)>2: OUT=R/sys.argv[2]
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('STORAGE_SEL'); assert n
def route(points, layer):
    for a,z in zip(points,points[1:]):
        if a==z: continue
        t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(layer)
        t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(p):
    v=pcbnew.PCB_VIA(b); v.SetPosition(P(*p)); v.SetWidth(pcbnew.FromMM(.5))
    v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
for t in list(b.GetTracks()):
    if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
# U12 -> U13 local branch, then take the mode trunk north and outboard.
route([(153.5,135.0),(178.5,135.0)],F)
route([(178.5,135.0),(176.0,135.0),(176.0,125.0)],F); via((176.0,125.0))
route([(176.0,125.0),(220.0,125.0),(220.0,151.0)],B); via((220.0,151.0))
route([(220.0,151.0),(211.1,150.95)],F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.BuildConnectivity(); b.Save(str(OUT)); print(OUT)
