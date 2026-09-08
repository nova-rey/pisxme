"""V576: restore omitted physical In2 bridges in the V574 coupled field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; base=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V574_COUPLED_POWER_FIELD.kicad_pcb'; out=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V576_RESTORE_3V3_BRIDGES.kicad_pcb'
L=pcbnew.In2_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(L); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
b=pcbnew.LoadBoard(str(base)); n=b.FindNet('RTL_3V3')
# These are physical joins between the already present via endpoints.
s(b,n,(100.5,59.6),(100.1,51.0)); s(b,n,(100.5,59.6),(112.0,65.2))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
