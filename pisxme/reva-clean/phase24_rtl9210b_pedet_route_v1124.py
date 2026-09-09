"""V1124: disposable PEDET route from RTL9210B to R2 and M.2 contact."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_QFN_GND_ATTACH_V1123.kicad_pcb';OUT=H/'PHASE24_RTL9210B_PEDET_ROUTE_V1124.kicad_pcb';F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.6));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('PEDET')
tr(b,n,F,[(97.6,73.95),(97.6,76.5),(105.0,76.5)]);via(b,n,(105.0,76.5));tr(b,n,B,[(105.0,76.5),(119.0,76.5),(119.0,80.0)]);via(b,n,(119.0,80.0));tr(b,n,F,[(119.0,80.0),(120.0,80.0)]);tr(b,n,B,[(119.0,80.0),(124.0,80.0)]);via(b,n,(124.0,80.0));tr(b,n,F,[(124.0,80.0),(132.0,80.0),(140.75,70.0),(140.75,62.725)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
