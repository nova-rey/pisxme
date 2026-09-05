"""Disposable native-copper join for the remaining U7 BRIDGE_CFG pads."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_12VA_C3_JOIN.kicad_pcb'
OUT=R/'PHASE24_U7_CFG_JOIN_CURRENT.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('/STORAGE/BRIDGE_CFG')
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
points=((117.5,144.5),(114.0,144.5),(114.0,141.0),(126.0,141.0),(126.0,144.5),(124.5,144.5))
for a,z in zip(points,points[1:]):
    t=pcbnew.PCB_TRACK(b);t.SetLayer(pcbnew.F_Cu);t.SetNet(n);t.SetWidth(pcbnew.FromMM(.20));t.SetStart(V(*a));t.SetEnd(V(*z));b.Add(t)
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
