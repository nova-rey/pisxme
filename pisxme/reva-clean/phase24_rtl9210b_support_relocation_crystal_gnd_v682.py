"""V682: correct the crystal-field GND thermal connection on V2."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_ROUTE_V2.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_CRYSTAL_GND_V682.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('GND')
# Add ordinary local GND stitching beside the two crystal load caps.
for x,y in ((85.6,63.0),(91.6,63.0)):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(x,y+0.8));q.SetWidth(pcbnew.FromMM(.6));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
