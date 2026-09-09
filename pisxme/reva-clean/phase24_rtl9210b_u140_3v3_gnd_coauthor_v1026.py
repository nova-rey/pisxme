"""V1026: co-author U1.40/RTL_3V3 with the local GND return corridor."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_1V1_U163_V1019.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_U140_3V3_GND_COAUTHOR_V1026.kicad_pcb'; F=pcbnew.F_Cu; B=pcbnew.B_Cu; L=pcbnew.In2_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n3=b.FindNet('RTL_3V3'); n1=b.FindNet('RTL_1V1'); ng=b.FindNet('GND'); items=list(b.GetTracks())
for q in items:
 if q.GetNetCode() not in (n3.GetNetCode(),ng.GetNetCode()): continue
 s=q.GetStart(); e=q.GetEnd(); sx,sy=s.x/1e6,s.y/1e6; ex,ey=e.x/1e6,e.y/1e6
 if sx<95 and ex<95 and sy<76 and ey<76: b.Remove(q)
add(b,n3,[(94.8,66.05),(92.5,65.5)],F); via(b,n3,(92.5,65.5)); add(b,n3,[(92.5,65.5),(90.5,65.5),(90.5,74.8),(92.5,74.8)],B); via(b,n3,(92.5,74.8)); add(b,n3,[(92.5,74.8),(94.8,73.95)],F)
add(b,n3,[(94.05,68.4),(93.0,68.4),(93.0,67.8)],F); add(b,n3,[(93.0,67.8),(90.5,67.8)],F); via(b,n3,(90.5,67.8)); add(b,n3,[(90.5,67.8),(90.5,65.5)],B)
add(b,ng,[(94.0,62.0),(96.0,59.8),(89.2,59.8),(89.2,67.0)],B)
add(b,n1,[(94.05,68.8),(92.5,68.8),(92.5,69.5)],F); via(b,n1,(92.5,69.5)); add(b,n1,[(92.5,69.5),(93.5,69.5)],L)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
