"""V583: move only the RTL_5V upper B.Cu corridor clear of 3V3."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; base=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V582_3V3_GAP.kicad_pcb'; out=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V583_5V_UPPER_CLEARANCE.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(B); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
b=pcbnew.LoadBoard(str(base)); n=b.FindNet('RTL_5V')
for x in list(b.GetTracks()):
 if x.GetNetname()=='RTL_5V' and x.GetLayer()==B: b.RemoveNative(x)
for a,z in [((100.8,64.8),(101.2,64.8)),((101.2,64.8),(101.2,58.05)),((101.2,58.05),(104.5,58.05)),((104.5,58.05),(104.5,49.5)),((104.5,49.5),(95.2,49.5)),((95.2,49.5),(95.2,54.8))]: s(b,n,a,z)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
