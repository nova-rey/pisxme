"""V1455: left-first U1.66 GND escape with ordinary-via return."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ACCEPTED_PRIMITIVES_V1428.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_U166_GND_LEFT_V1455.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('GND'); assert n
v=(92.8,73.8); w=(97.2,73.8)
tr(b,n,F,[(94.05,72.4),(93.2,72.4),(92.8,73.8)]); via(b,n,v); tr(b,n,B,[v,(97.2,73.8)]); via(b,n,w); tr(b,n,F,[w,(97.2,71.5),(98.0,70.0)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
