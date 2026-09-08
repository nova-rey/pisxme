"""V582: center the RTL_3V3 In2 lower spine between RSET and 1V1 vias."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; base=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V581_3V3_RSET_CLEARANCE.kicad_pcb'; out=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V582_3V3_GAP.kicad_pcb'
L=pcbnew.In2_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(L); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
b=pcbnew.LoadBoard(str(base)); n=b.FindNet('RTL_3V3')
for x in list(b.GetTracks()):
 if x.GetNetname()=='RTL_3V3' and x.GetLayer()==L: b.RemoveNative(x)
for a,z in [((102.6,51),(110.2,51)),((100.1,51),(102.6,51)),((100.5,59.6),(100.1,51)),((100.5,59.6),(99,59.6)),((99,59.6),(98,59.6)),((98,59.6),(98,66.5)),((98,66.5),(97.5,66.5)),((97.5,66.5),(97.5,68.25)),((97.5,68.25),(104.4,68.25)),((104.4,68.25),(104.4,68.5)),((104.4,68.5),(112,65.2)),((104.4,68.5),(99.7,68)),((99.7,68),(93.7,72))]: s(b,n,a,z)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
