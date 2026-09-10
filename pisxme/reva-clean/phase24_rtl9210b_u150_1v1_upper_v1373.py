"""V1373: extend U1.50 to the existing RTL_1V1 via at 97.8,63.6."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_U150_1V1_UPPER_V1372.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_U150_1V1_UPPER_V1373.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20); P=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_1V1'); assert n
q=pcbnew.PCB_TRACK(b); q.SetStart(P(97.8,65.0)); q.SetEnd(P(97.8,63.6)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
