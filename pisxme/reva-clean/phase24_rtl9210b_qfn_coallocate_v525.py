"""V525: test an outer B.Cu return for the U1.39 RTL_3V3 source pad."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; src=H/'PHASE24_RTL9210B_QFN_COALLOCATE_V524.kicad_pcb'; out=H/'PHASE24_RTL9210B_QFN_COALLOCATE_V525.kicad_pcb'
B=pcbnew.B_Cu; W=pcbnew.FromMM(.13208)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(B); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
b=pcbnew.LoadBoard(str(src)); n=b.FindNet('RTL_3V3')
# Existing vias at (100.5,60.4) and (109.5,57.2) are the endpoints.
tr(b,n,(100.5,60.4),(100.5,72.0)); tr(b,n,(100.5,72.0),(116.0,72.0)); tr(b,n,(116.0,72.0),(116.0,57.2)); tr(b,n,(116.0,57.2),(109.5,57.2))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
