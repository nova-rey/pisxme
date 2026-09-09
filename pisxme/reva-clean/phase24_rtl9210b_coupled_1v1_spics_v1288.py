"""V1288: move only the U1.25 source via onto the existing 1V1 trunk."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_XTAL_IN_LIVE_PAD_V1279.kicad_pcb';OUT=H/'PHASE24_RTL9210B_COUPLED_1V1_SPICS_V1288.kicad_pcb';F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def route(b,n,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));one=b.FindNet('RTL_1V1');spi=b.FindNet('SPICS')
for q in list(b.GetTracks()):
 a=q.GetStart();z=q.GetEnd();aa=(round(pcbnew.ToMM(a.x),2),round(pcbnew.ToMM(a.y),2));zz=(round(pcbnew.ToMM(z.x),2),round(pcbnew.ToMM(z.y),2))
 if q.GetNetname()=='RTL_1V1' and (aa,zz)==((101.95,70.4),(103.0,70.4)):b.RemoveNative(q)
for q in list(b.GetTracks()):
 if isinstance(q,pcbnew.PCB_VIA) and q.GetNetname()=='RTL_1V1':
  p=q.GetPosition()
  if abs(p.x-pcbnew.FromMM(103.0))<0.01 and abs(p.y-pcbnew.FromMM(70.4))<0.01:b.RemoveNative(q)
route(b,one,F,[(101.95,70.4),(100.5,70.4)]);via(b,one,(100.5,70.4))
route(b,spi,F,[(101.95,70.8),(103.8,70.8)]);via(b,spi,(103.8,70.8))
route(b,spi,B,[(103.8,70.8),(109.5,70.8),(109.5,66.5),(110.8,66.5),(110.8,70.8)])
via(b,spi,(110.8,70.8));route(b,spi,F,[(110.8,70.8),(110.8,76.4),(111.4,76.4)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
