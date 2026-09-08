"""V529: keep U1.39 on B.Cu to the existing V524 transition."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; src=H/'PHASE24_RTL9210B_QFN_COALLOCATE_V524.kicad_pcb'; out=H/'PHASE24_RTL9210B_QFN_COALLOCATE_V529.kicad_pcb'
B=pcbnew.B_Cu; W=pcbnew.FromMM(.13208)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(B); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
b=pcbnew.LoadBoard(str(src)); n=b.FindNet('RTL_3V3')
tr(b,n,(100.5,60.4),(100.0,58.05)); tr(b,n,(100.0,58.05),(100.0,55.8)); tr(b,n,(100.0,55.8),(102.8,55.8))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
