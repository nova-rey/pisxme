"""V527: short F.Cu local join from U1.39 to the V524 U1.34 branch."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; src=H/'PHASE24_RTL9210B_QFN_COALLOCATE_V524.kicad_pcb'; out=H/'PHASE24_RTL9210B_QFN_COALLOCATE_V527.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.13208)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(F); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
b=pcbnew.LoadBoard(str(src)); n=b.FindNet('RTL_3V3')
# U1.39 is already on the validated x=100.5 handoff; this short local
# channel reaches the V524 U1.34 source without a new layer transition.
tr(b,n,(101.5,60.4),(101.5,58.05)); tr(b,n,(101.5,58.05),(102.8,58.05))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
