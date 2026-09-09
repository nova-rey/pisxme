"""V1286: route SPICS through the open QFN interior and west of RXN."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_XTAL_IN_LIVE_PAD_V1279.kicad_pcb';OUT=H/'PHASE24_RTL9210B_SPICS_INTERIOR_ESCAPE_V1286.kicad_pcb';F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def route(b,n,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('SPICS')
for q in list(b.GetTracks()):
 if q.GetNetname()=='SPICS':b.RemoveNative(q)
route(b,n,F,[(101.95,70.8),(99.5,70.8)]);via(b,n,(99.5,70.8))
route(b,n,B,[(99.5,70.8),(99.5,72.0),(85.5,72.0),(85.5,66.0),(110.8,66.0),(110.8,70.8)])
via(b,n,(110.8,70.8));route(b,n,F,[(110.8,70.8),(110.8,76.4),(111.4,76.4)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
