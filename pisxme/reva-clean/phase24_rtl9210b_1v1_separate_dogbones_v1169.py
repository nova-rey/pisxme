"""V1169: separate U1.60/U1.63 dogbones into accepted In2 1V1 collector."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_1V1_IN2_COLLECTOR_V1167.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_1V1_SEPARATE_DOGBONES_V1169.kicad_pcb'; F,L=pcbnew.F_Cu,pcbnew.In2_Cu; W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,c,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNetCode(c);b.Add(q)
def via(b,c,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.6));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(F,pcbnew.B_Cu);q.SetNetCode(c);b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_1V1').GetNetCode()
tr(b,n,F,[(94.05,70.0),(92.5,70.0)]);via(b,n,(92.5,70.0));tr(b,n,L,[(92.5,70.0),(91.8,69.0)])
tr(b,n,F,[(94.05,71.2),(92.5,71.2)]);via(b,n,(92.5,71.2));tr(b,n,L,[(92.5,71.2),(91.8,69.0)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
