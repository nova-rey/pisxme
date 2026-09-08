"""V578: make the first U1.33 RTL_5V escape exactly horizontal."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; base=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V576_RESTORE_3V3_BRIDGES.kicad_pcb'; out=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V578_HORIZONTAL_ESCAPE.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def mm(p): return (round(pcbnew.ToMM(p.x),4),round(pcbnew.ToMM(p.y),4))
def s(b,n,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(F); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
b=pcbnew.LoadBoard(str(base)); n=b.FindNet('RTL_5V')
for x in list(b.GetTracks()):
 if x.GetNetname()=='RTL_5V' and x.GetLayer()==F: b.RemoveNative(x)
s(b,n,(102.05,64.8),(101.5,64.8)); s(b,n,(101.5,64.8),(100.8,63.8))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
