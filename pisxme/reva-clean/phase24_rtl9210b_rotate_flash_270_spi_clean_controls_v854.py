"""V854: left-side, vertically staggered source escapes for SPISO/SPICS."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ROTATE_FLASH_270_SPI_CLEAN_CONTROLS_V850.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ROTATE_FLASH_270_SPI_CLEAN_CONTROLS_V854.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,ps):
 net=b.FindNet(n)
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(net); q.SetNetCode(net.GetNetCode()); b.Add(q)
def via(b,n,x,y):
 net=b.FindNet(n); q=pcbnew.PCB_VIA(b); q.SetPosition(P(x,y)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(net); q.SetNetCode(net.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for q in list(b.GetTracks()):
 if q.GetNetname() in ('SPISO','SPICS'): b.RemoveNative(q)
via(b,'SPISO',89,70.8); via(b,'SPISO',89,52.4)
tr(b,'SPISO',F,[(94.05,68.8),(94.05,70.8),(89,70.8)])
tr(b,'SPISO',B,[(89,70.8),(89,52.4)])
tr(b,'SPISO',F,[(89,52.4),(88,52.4)])
via(b,'SPICS',87,72.0); via(b,'SPICS',87,51.2)
tr(b,'SPICS',F,[(94.05,69.2),(94.05,72.0),(87,72.0)])
tr(b,'SPICS',B,[(87,72.0),(87,51.2)])
tr(b,'SPICS',F,[(87,51.2),(88,51.2)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
