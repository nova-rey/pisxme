"""V1292: shift XTAL_IN's vertical leg clear of RSET."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_XTAL_IN_LIVE_PAD_V1279.kicad_pcb';OUT=H/'PHASE24_RTL9210B_XTAL_IN_RSET_CLEAN_V1292.kicad_pcb';F=pcbnew.F_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def route(b,n,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(F);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('XTAL_IN')
for q in list(b.GetTracks()):
 if q.GetNetname()=='XTAL_IN':b.RemoveNative(q)
route(b,n,[(94.05,67.2),(93.4,67.2),(92.8,66.8),(92.5,66.8),(92.5,57.0),(78.0,57.0),(78.0,59.0)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
