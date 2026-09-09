"""V1055: scrub stale vertical-U2 3V3 copper and add a GND return."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_ROTATE_U2_HORIZONTAL_V1053.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_ROTATE_U2_HORIZONTAL_V1055.kicad_pcb'; F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n3=b.FindNet('RTL_3V3'); ng=b.FindNet('GND')
for q in list(b.GetTracks()):
 if q.GetNetCode()!=n3.GetNetCode(): continue
 s,e=q.GetStart(),q.GetEnd(); xs=[s.x/1e6,e.x/1e6]; ys=[s.y/1e6,e.y/1e6]
 if max(xs)<121 and min(xs)>100 and max(ys)<82 and min(ys)>68: b.RemoveNative(q)
# Two local ordinary GND transitions spread from U2 pad 4; no via-in-pad.
add(b,ng,[(115,76.4),(114.4,77.2),(114.4,78.0)]); via(b,ng,(114.4,78.0))
add(b,ng,[(115,76.4),(115.6,77.2),(115.6,78.0)]); via(b,ng,(115.6,78.0))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
