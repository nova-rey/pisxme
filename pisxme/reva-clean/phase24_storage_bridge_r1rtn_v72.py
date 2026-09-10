"""V72: native-pad BRIDGE_R1RTN support connection probe."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V54_STORAGE_GND_SOLID.kicad_pcb'
OUT=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V72_BRIDGE_R1RTN.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('BRIDGE_R1RTN'); assert n
t=pcbnew.PCB_TRACK(b); t.SetStart(P(92.2,123.4)); t.SetEnd(P(138.0,122.0)); t.SetLayer(F); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
