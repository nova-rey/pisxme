"""V810: move the SPICS upper leg behind PEDET and restore U2 GND return."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ORIENTATION180_SPICS_V809.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ORIENTATION180_SPICS_V810.kicad_pcb'
F=pcbnew.F_Cu; B=pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def T(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def V(b,n,p):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.6)); q.SetDrill(pcbnew.FromMM(.3)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('SPICS')
for item in list(b.GetTracks()):
 if item.GetNetname()=='SPICS': b.RemoveNative(item)
T(b,n,F,(94.05,69.2),(92.5,69.2)); T(b,n,F,(92.5,69.2),(92.5,64)); T(b,n,F,(92.5,64),(93.5,63)); T(b,n,F,(93.5,63),(93.5,54)); V(b,n,(93.5,54)); T(b,n,B,(93.5,54),(93.5,49)); T(b,n,B,(93.5,49),(83.3,49)); V(b,n,(83.3,49)); T(b,n,F,(83.3,49),(83.3,50))
g=b.FindNet('GND'); T(b,g,F,(86.9,50),(86.9,51)); V(b,g,(86.9,51))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
