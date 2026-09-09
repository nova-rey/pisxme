"""V1204: immediate CLKREQ source transition and dedicated upper corridor."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_PEDET_LAYER_BOUNDARY_V1200.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_CLKREQ_UPPER_CORRIDOR_V1204.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('CLKREQ_N'); add(b,n,[(99.6,73.95),(99.6,74.5)],F); via(b,n,(99.6,74.5)); add(b,n,[(99.6,74.5),(88.0,74.5),(88.0,45.0),(121.0,45.0),(121.0,74.5)],B); via(b,n,(121.0,74.5)); add(b,n,[(121.0,74.5),(120.0,75.0)],F); add(b,n,[(121.0,45.0),(136.5,45.0),(136.5,69.0)],B); via(b,n,(136.5,69.0)); add(b,n,[(136.5,69.0),(136.5,70.275)],F); b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
