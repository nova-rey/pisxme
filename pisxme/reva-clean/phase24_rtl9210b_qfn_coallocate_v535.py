"""V535: dogleg U1.52 B.Cu rise around the XTAL_IN endpoint."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_QFN_COALLOCATE_V532.kicad_pcb'; out=H/'PHASE24_RTL9210B_QFN_COALLOCATE_V535.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.13208)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,a):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*a)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); v.SetWidth(pcbnew.FromMM(.6)); v.SetDrill(pcbnew.FromMM(.3)); b.Add(v)
b=pcbnew.LoadBoard(str(src)); n=b.FindNet('RTL_3V3')
tr(b,n,F,(101.5,67.5),(101.5,68.5)); via(b,n,(101.5,68.5)); tr(b,n,B,(101.5,68.5),(103.5,68.5)); tr(b,n,B,(103.5,68.5),(103.5,65.5))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
