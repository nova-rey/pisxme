"""V538: move U1.40 1V1 transition farther left of the QFN field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; src=H/'PHASE24_RTL9210B_QFN_COALLOCATE_V535.kicad_pcb'; out=H/'PHASE24_RTL9210B_QFN_COALLOCATE_V538.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.13208)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,a):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*a)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); v.SetWidth(pcbnew.FromMM(.6)); v.SetDrill(pcbnew.FromMM(.3)); b.Add(v)
b=pcbnew.LoadBoard(str(src)); n=b.FindNet('RTL_1V1'); tr(b,n,F,(102.05,60.8),(101.3,60.8)); tr(b,n,F,(101.3,60.8),(100.5,61.5)); via(b,n,(100.5,61.5)); tr(b,n,B,(100.5,61.5),(100.5,57.3)); tr(b,n,B,(100.5,57.3),(101.5,57.3))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
