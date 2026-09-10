"""V102: single U13.30 source branch around the acreage outer perimeter."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE24_STORAGE_AUTHORITY_J3_VERTICAL_V94.kicad_pcb'; OUT=R/'PHASE24_STORAGE_RAIL_U13_OUTER_V102.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetLayer(l); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetWidth(pcbnew.FromMM(.3)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*a)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); q.SetWidth(pcbnew.FromMM(.6)); q.SetDrill(pcbnew.FromMM(.3)); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('STORAGE_3V3'); assert n
tr(b,n,pcbnew.F_Cu,(181.5,135),(183.5,135)); via(b,n,(183.5,135))
for a,z in [((183.5,135),(183.5,110)),((183.5,110),(290,110)),((290,110),(290,149.05))]: tr(b,n,pcbnew.B_Cu,a,z)
via(b,n,(290,149.05)); tr(b,n,pcbnew.F_Cu,(290,149.05),(211.1,149.05))
b.Save(str(OUT)); print(OUT)
