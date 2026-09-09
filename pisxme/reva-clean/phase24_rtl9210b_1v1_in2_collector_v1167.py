"""V1167: use the designated In2 low-voltage power layer for 1V1 collector."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_CRYSTAL_POCKET_RELOCATED_V1165.kicad_pcb';OUT=H/'PHASE24_RTL9210B_1V1_IN2_COLLECTOR_V1167.kicad_pcb';F,B,L=pcbnew.F_Cu,pcbnew.B_Cu,pcbnew.In2_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,c,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNetCode(c);b.Add(q)
def via(b,c,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.6));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(F,B);q.SetNetCode(c);b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_1V1').GetNetCode();tr(b,n,F,[(94.05,68.0),(92.0,68.0),(91.8,69.0)]);via(b,n,(91.8,69.0));tr(b,n,L,[(91.8,69.0),(130.0,69.0),(130.0,48.0)]);via(b,n,(130.0,48.0));tr(b,n,F,[(130.0,48.0),(123.4,48.0),(123.4,51.0)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
