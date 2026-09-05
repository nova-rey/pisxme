"""Disposable local join for the isolated 12V input bypass pad C3.2."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;BASE=R/'PHASE24_BRIDGE_3V3_R14_JOIN.kicad_pcb';OUT=R/'PHASE24_12VA_C3_JOIN.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('/POWER_INPUT/12V_IN_A')
def V(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
for a,z in [((15.8,70.0),(18.0,70.0)),((18.0,70.0),(18.0,76.45)),((18.0,76.45),(21.45,76.45))]:
 t=pcbnew.PCB_TRACK(b);t.SetLayer(pcbnew.F_Cu);t.SetNet(n);t.SetWidth(pcbnew.FromMM(.5));t.SetStart(V(*a));t.SetEnd(V(*z));b.Add(t)
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
