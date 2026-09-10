"""V1450: disposable outboard REFCLK pair route from the V1428 base."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ACCEPTED_PRIMITIVES_V1428.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_REFCLK_OUTBOARD_V1450.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); p=b.FindNet('REFCLK_P'); n=b.FindNet('REFCLK_N'); assert p and n
for net,src,west,up,far,launch in [(p,[(94.05,70.4),(95.2,70.4),(95.2,65.5)],(72,65.5),(72,41.5),(141,60.5),(137.25,62.725)),(n,[(94.05,70.8),(96,70.8),(96,66.2)],(70.8,66.2),(70.8,42.2),(139.8,60.5),(136.75,62.725))]:
 tr(b,net,F,src); via(b,net,src[-1]); tr(b,net,B,[src[-1],west]); via(b,net,west); tr(b,net,F,[west,up]); via(b,net,up); tr(b,net,B,[up,(far[0],up[1]),far]); via(b,net,far); tr(b,net,F,[far,(launch[0],far[1]),launch])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
