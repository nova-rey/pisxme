"""V1009: far-right U1.16 RTL_1V1 QFN escape probe."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_1V1_U125_V1005.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_1V1_U116_V1009.kicad_pcb'; F=pcbnew.F_Cu; L=pcbnew.In2_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_1V1')
tr(b,n,[(101.95,67.2),(104.5,67.2),(104.5,69.5),(103.0,69.5)],F); via(b,n,(103.0,69.5)); tr(b,n,[(103.0,69.5),(102.5,69.5)],L)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
