"""V815: retain clean V810 SPICS and give SPISO a separate B.Cu corridor."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ORIENTATION180_SPICS_V810.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ORIENTATION180_SPISO_SEPARATE_V815.kicad_pcb'
F=pcbnew.F_Cu; B=pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def T(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def V(b,n,p):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.6)); q.SetDrill(pcbnew.FromMM(.3)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('SPISO')
for item in list(b.GetTracks()):
 if item.GetNetname()=='SPISO': b.RemoveNative(item)
T(b,n,F,(94.05,68.8),(90,68.8)); V(b,n,(90,68.8))
T(b,n,B,(90,68.8),(90,54)); T(b,n,B,(90,54),(84.5,54)); V(b,n,(84.5,54))
T(b,n,F,(84.5,54),(84.5,50))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
