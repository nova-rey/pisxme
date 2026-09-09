"""V1291: remove the inherited RSET/XTAL_IN crossing from V1279."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_XTAL_IN_LIVE_PAD_V1279.kicad_pcb';OUT=H/'PHASE24_RTL9210B_RSET_XTAL_CLEAN_V1291.kicad_pcb';F=pcbnew.F_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def route(b,n,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(F);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RSET')
for q in list(b.GetTracks()):
 if q.GetNetname()=='RSET':b.RemoveNative(q)
route(b,n,[(94.8,66.05),(92.0,66.05),(88.0,66.05),(88.0,65.0)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
