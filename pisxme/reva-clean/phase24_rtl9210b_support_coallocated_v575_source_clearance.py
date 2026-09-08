"""V575: shift only the U1.34 RTL_3V3 departure for strict source clearance."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; base=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V574_COUPLED_POWER_FIELD.kicad_pcb'; out=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V575_SOURCE_CLEARANCE.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(F); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
b=pcbnew.LoadBoard(str(base)); n=b.FindNet('RTL_3V3')
for x in list(b.GetTracks()):
 if x.GetNetname()=='RTL_3V3' and x.GetLayer()==F: b.RemoveNative(x)
for a,z in [((102.05,65.2),(104.4,65.25)),((104.4,65.25),(104.4,65.95)),((104.4,65.95),(104.4,68.5)),((102.05,59.6),(100.5,59.6)),((109.95,65.2),(112,65.2)),((102.6,53),(102.6,51)),((100.1,53),(100.1,51)),((110.2,53),(110.2,51)),((99.7,70),(99.7,68)),((93.7,70),(93.7,72))]: s(b,n,a,z)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
