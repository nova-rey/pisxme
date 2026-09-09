"""V780: rechannel SPICS/SPISO endpoints to clear a control corridor."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V760_SUPPORT_SIGNALS_GROUND_V772.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SPI_RECHANNEL_SPICS_SPISO_V780.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def v(b,n,a):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*a)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for netname in ('SPICS','SPISO'):
 n=b.FindNet(netname)
 for item in list(b.GetTracks()):
  if item.GetNetname()==netname: b.RemoveNative(item)
n=b.FindNet('SPICS'); t(b,n,F,(98.8,66.05),(98.8,64.5)); t(b,n,F,(98.8,64.5),(97,60.5)); v(b,n,(97,60.5)); t(b,n,B,(97,60.5),(97,80)); v(b,n,(97,80)); t(b,n,F,(97,80),(105,80))
n=b.FindNet('SPISO'); t(b,n,F,(99.2,66.05),(99.2,64.5)); t(b,n,F,(99.2,64.5),(99,60.5)); v(b,n,(99,60.5)); t(b,n,B,(99,60.5),(99,78.8)); v(b,n,(99,78.8)); t(b,n,F,(99,78.8),(105,78.8))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
