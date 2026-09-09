"""V1285: co-author U1.25 RTL_1V1 and U1.24 SPICS source fields."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_XTAL_IN_LIVE_PAD_V1279.kicad_pcb';OUT=H/'PHASE24_RTL9210B_COUPLED_1V1_SPICS_V1285.kicad_pcb';F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def route(b,n,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));one=b.FindNet('RTL_1V1');spi=b.FindNet('SPICS')
for q in list(b.GetTracks()):
 a=q.GetStart();z=q.GetEnd();aa=(pcbnew.ToMM(a.x),pcbnew.ToMM(a.y));zz=(pcbnew.ToMM(z.x),pcbnew.ToMM(z.y))
 if q.GetNetname()=='RTL_1V1' and (aa,zz) in [((101.95,70.4),(103.0,70.4)),((103.0,70.4),(87.0,70.4))]: b.RemoveNative(q)
for q in list(b.GetTracks()):
 if not isinstance(q, pcbnew.PCB_VIA): continue
 p=q.GetPosition()
 if q.GetNetname()=='RTL_1V1' and abs(p.x-pcbnew.FromMM(103.0))<2 and abs(p.y-pcbnew.FromMM(70.4))<2: b.RemoveNative(q)
route(b,one,F,[(101.95,70.4),(102.7,70.4),(102.7,69.3)]);via(b,one,(102.7,69.3))
route(b,one,B,[(102.7,69.3),(109.5,69.3),(109.5,60.0),(103.0,60.0)])
route(b,spi,F,[(101.95,70.8),(103.8,70.8)]);via(b,spi,(103.8,70.8))
route(b,spi,B,[(103.8,70.8),(109.5,70.8),(109.5,66.5),(110.8,66.5),(110.8,70.8)])
via(b,spi,(110.8,70.8));route(b,spi,F,[(110.8,70.8),(110.8,76.4),(111.4,76.4)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
