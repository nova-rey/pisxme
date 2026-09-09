"""V1188: U1.52 3V3 via to upper In2 power handoff."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_1V1_U116_U125_MERGED_V1183.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_U152_3V3_V1188.kicad_pcb'; F,L=pcbnew.F_Cu,pcbnew.In2_Cu; WF=pcbnew.FromMM(.20); WP=pcbnew.FromMM(.50)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,pts,l,w):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(w); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_3V3'); add(b,n,[(94.05,66.8),(93.0,66.0)],F,WF); via(b,n,(93.0,66.0)); add(b,n,[(93.0,66.0),(93.0,60.0),(108.0,60.0),(108.0,64.0)],L,WP); via(b,n,(108.0,64.0)); b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
