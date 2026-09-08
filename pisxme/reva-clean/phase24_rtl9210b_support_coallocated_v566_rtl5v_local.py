"""V566: local RTL_5V escape with coherent decoupler relocation."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
base=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V562.kicad_pcb'
out=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V566_RTL5V_LOCAL.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,a,z,l=F):
    t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
b=pcbnew.LoadBoard(str(base)); n=b.FindNet('RTL_5V')
c5=next(x for x in b.Footprints() if x.GetReference()=='C5'); c5.SetPosition(P(100,56.5))
# Pad 33 exits west, then steps diagonally away from the adjacent 3V3 via.
for a,z in [((102.05,64.8),(101.5,64.8)),((101.5,64.8),(101.2,64.2)),((101.2,64.2),(101.2,58.05)),((102.8,58.05),(101.2,58.05)),((101.2,58.05),(101.2,56.5)),((101.2,56.5),(99.2,56.5))]: s(b,n,a,z)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
