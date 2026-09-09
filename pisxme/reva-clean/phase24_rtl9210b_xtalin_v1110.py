"""V1110: XTAL_IN transition outside the right-side QFN pad clearance field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_RSET_V1092.kicad_pcb';OUT=H/'PHASE24_RTL9210B_XTALIN_V1110.kicad_pcb';F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('XTAL_IN');via(b,n,(99.8,67.5));tr(b,n,F,[(94.05,67.2),(95.0,67.2),(99.8,67.5)]);tr(b,n,B,[(99.8,67.5),(99.8,58.0),(88.0,58.0)]);via(b,n,(88.0,58.0));tr(b,n,F,[(88.0,58.0),(88.0,59.0)]);tr(b,n,B,[(88.0,58.0),(86.5,58.0),(86.5,61.0),(88.0,61.0)]);via(b,n,(88.0,61.0));tr(b,n,F,[(88.0,61.0),(88.0,62.0)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
