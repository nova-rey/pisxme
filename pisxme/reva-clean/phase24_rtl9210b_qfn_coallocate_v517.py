"""V517: regenerate XTAL_IN beside the validated V516 1V1 field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; src=H/'PHASE24_RTL9210B_QFN_COALLOCATE_V516.kicad_pcb'; out=H/'PHASE24_RTL9210B_QFN_COALLOCATE_V517.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.13208)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(src)); n=b.FindNet('XTAL_IN')
t=pcbnew.PCB_TRACK(b); t.SetStart(P(102.5,67.5)); t.SetEnd(P(102.5,42)); t.SetLayer(B); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
