"""V824: add staggered source transitions for SPISI, SPICLK, and SPISO3."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ORIENTATION180_SPISO_HIGH_V823.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ORIENTATION180_SPI_REMAINING_V824.kicad_pcb'
F=pcbnew.F_Cu; B=pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def T(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def V(b,n,p):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.6)); q.SetDrill(pcbnew.FromMM(.3)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for name in ('SPISI','SPICLK','SPISO3'):
 for item in list(b.GetTracks()):
  if item.GetNetname()==name: b.RemoveNative(item)
n=b.FindNet('SPISI'); T(b,n,F,(94.05,66.8),(92.8,66.8)); V(b,n,(92.8,66.8)); T(b,n,B,(92.8,66.8),(92.8,51.5)); T(b,n,B,(92.8,51.5),(88.1,51.5)); V(b,n,(88.1,51.5)); T(b,n,F,(88.1,51.5),(88.1,50))
n=b.FindNet('SPICLK'); T(b,n,F,(94.05,67.2),(91.5,67.2)); V(b,n,(91.5,67.2)); T(b,n,B,(91.5,67.2),(91.5,52.5)); T(b,n,B,(91.5,52.5),(89.3,52.5)); V(b,n,(89.3,52.5)); T(b,n,F,(89.3,52.5),(89.3,50))
n=b.FindNet('SPISO3'); T(b,n,F,(94.05,68.4),(93.2,68.4)); T(b,n,F,(93.2,68.4),(93.2,65.5)); T(b,n,F,(93.2,65.5),(90.5,65.5)); V(b,n,(90.5,65.5)); T(b,n,B,(90.5,65.5),(90.5,51)); V(b,n,(90.5,51)); T(b,n,F,(90.5,51),(90.5,50))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
