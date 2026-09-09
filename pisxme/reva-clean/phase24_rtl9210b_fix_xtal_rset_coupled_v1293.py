"""V1293: co-author XTAL_IN and RSET around the inherited crossing."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_XTAL_IN_LIVE_PAD_V1279.kicad_pcb';OUT=H/'PHASE24_RTL9210B_XTAL_RSET_COUPLED_CLEAN_V1293.kicad_pcb';F=pcbnew.F_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def route(b,n,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(F);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));xt=b.FindNet('XTAL_IN');rs=b.FindNet('RSET')
for q in list(b.GetTracks()):
 if q.GetNetname() in ('XTAL_IN','RSET'):b.RemoveNative(q)
route(b,xt,[(94.05,67.2),(93.4,67.2),(92.8,66.8),(92.5,66.8),(92.5,57.0),(78.0,57.0),(78.0,59.0)])
route(b,rs,[(94.8,66.05),(96.0,66.05),(96.0,68.5),(88.0,68.5),(88.0,65.0)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
