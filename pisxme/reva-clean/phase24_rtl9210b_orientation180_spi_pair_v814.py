"""V814: paired SPICS/SPISO source allocation with a lower SPICS jog."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ORIENTATION180_SPICS_V810.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ORIENTATION180_SPI_PAIR_V814.kicad_pcb'
F=pcbnew.F_Cu; B=pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def T(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def V(b,n,p):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.6)); q.SetDrill(pcbnew.FromMM(.3)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for item in list(b.GetTracks()):
 if item.GetNetname() in ('SPICS','SPISO'): b.RemoveNative(item)
n=b.FindNet('SPICS'); T(b,n,F,(94.05,69.2),(93,69.2)); T(b,n,F,(93,69.2),(93,70)); T(b,n,F,(93,70),(91.5,70)); T(b,n,F,(91.5,70),(91.5,64)); T(b,n,F,(91.5,64),(92.5,63)); T(b,n,F,(92.5,63),(92.5,49)); T(b,n,F,(92.5,49),(83.3,49)); T(b,n,F,(83.3,49),(83.3,50))
n=b.FindNet('SPISO'); T(b,n,F,(94.05,68.8),(92,68.8)); V(b,n,(92,68.8)); T(b,n,B,(92,68.8),(91,64)); T(b,n,B,(91,64),(91,52)); T(b,n,B,(91,52),(84.5,52)); V(b,n,(84.5,52)); T(b,n,F,(84.5,52),(84.5,50))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
