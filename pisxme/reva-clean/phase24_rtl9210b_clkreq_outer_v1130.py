"""V1130: V788-inspired separated CLKREQ_N pocket adapted to current U1."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_PEDET_ROUTE_V1124.kicad_pcb';OUT=H/'PHASE24_RTL9210B_CLKREQ_OUTER_V1130.kicad_pcb';F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.6));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));r=b.FindFootprintByReference('R3');r.SetPosition(r.GetPosition()+P(-9,-13));n=b.FindNet('CLKREQ_N')
t(b,n,F,[(99.6,73.95),(99.0,74.5),(103.0,74.5),(103.0,68.0)]);v(b,n,(103.0,68.0));t(b,n,B,[(103.0,68.0),(103.0,52.0),(111.0,52.0)]);v(b,n,(111.0,52.0));t(b,n,F,[(111.0,52.0),(111.0,62.0)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
