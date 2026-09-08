"""V530: relocate C3 and regenerate the U1 RTL_3V3 source field together."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; src=H/'PHASE24_RTL9210B_QFN_COALLOCATE_V524.kicad_pcb'; out=H/'PHASE24_RTL9210B_QFN_COALLOCATE_V530.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.13208)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,a):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*a)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); v.SetWidth(pcbnew.FromMM(.6)); v.SetDrill(pcbnew.FromMM(.3)); b.Add(v)
b=pcbnew.LoadBoard(str(src)); n=b.FindNet('RTL_3V3')
for x in list(b.GetTracks()):
 if x.GetNetname()=='RTL_3V3': b.RemoveNative(x)
c=b.FindFootprintByReference('C3'); c.SetPosition(P(99.0,65.0))
# C3.1 is at (98.2,65.0) after the move. Build one shared B.Cu rail.
u=b.FindFootprintByReference('U1')
tr(b,n,F,(108.4,58.05),(108.4,57.2)); tr(b,n,F,(108.4,57.2),(109.5,57.2)); via(b,n,(109.5,57.2))
tr(b,n,B,(109.5,57.2),(109.5,56.0)); tr(b,n,B,(109.5,56.0),(98.2,56.0)); tr(b,n,B,(98.2,56.0),(98.2,64.2)); via(b,n,(98.2,64.2)); tr(b,n,F,(98.2,64.2),(98.2,65.0))
tr(b,n,F,(102.8,58.05),(102.8,55.8)); via(b,n,(102.8,55.8)); tr(b,n,B,(102.8,55.8),(102.8,56.0))
tr(b,n,F,(102.05,60.4),(100.5,60.4)); via(b,n,(100.5,60.4)); tr(b,n,B,(100.5,60.4),(100.5,56.0))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
