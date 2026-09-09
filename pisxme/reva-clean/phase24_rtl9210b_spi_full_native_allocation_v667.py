"""V667: fresh native five-net SPI allocation on the V595 support base."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V595_CLKREQ_LOCAL.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SPI_FULL_NATIVE_ALLOCATION_V667.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(BASE))
routes={
 'SPISI':[(102.05,58.8),(100.8,58.8),(100.0,59.6)],
 'SPICLK':[(102.05,59.2),(100.4,59.2),(99.4,60.2)],
 'SPISO3':[(102.05,60.4),(100.0,60.4),(98.8,61.2)],
 'SPISO':[(102.05,60.8),(98.8,60.8),(97.8,61.8)],
 'SPICS':[(102.05,61.2),(99.2,61.2),(98.2,62.2)],
}
ends={'SPISI':(96.1,70.0),'SPICLK':(97.3,70.0),'SPISO3':(98.5,70.0),'SPISO':(92.5,70.0),'SPICS':(91.3,70.0)}
# Three upper channels use separated B.Cu drops; two lower channels use
# independent F/B corridors to avoid the reversed U2 endpoint ordering.
for name,pts in routes.items():
 n=b.FindNet(name)
 for a,z in zip(pts,pts[1:]): t(b,n,F,a,z)
 if name in ('SPISI','SPICLK','SPISO3'):
  q=pts[-1]; v(b,n,q); x=ends[name][0]; t(b,n,B,q,(x,q[1])); t(b,n,B,(x,q[1]),(x,68.0)); v(b,n,(x,68.0)); t(b,n,F,(x,68.0),ends[name])
 elif name=='SPISO':
  q=pts[-1]; t(b,n,F,q,(94.0,64.0)); t(b,n,F,(94.0,64.0),(94.0,68.5)); t(b,n,F,(94.0,68.5),ends[name])
 else:
  q=pts[-1]; v(b,n,q); t(b,n,B,q,(91.3,q[1])); t(b,n,B,(91.3,q[1]),(91.3,68.5)); v(b,n,(91.3,68.5)); t(b,n,F,(91.3,68.5),ends[name])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
