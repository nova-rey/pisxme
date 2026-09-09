"""V683: connect the C1 GND pad to the V682 stitching via."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_CRYSTAL_GND_V682.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_CRYSTAL_GND_V683.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('GND')
q=pcbnew.PCB_TRACK(b);q.SetStart(P(85.6,63.0));q.SetEnd(P(85.6,63.8));q.SetLayer(F);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
