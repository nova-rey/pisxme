"""Disposable right-side F.Cu join for bridge-3V3 R14.1."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;BASE=R/'PHASE24_BRIDGE_3V3_SUPPORT_JOIN.kicad_pcb';OUT=R/'PHASE24_BRIDGE_3V3_R14_JOIN.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('/REGULATORS/BRIDGE_3V3')
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(a,z):
    t=pcbnew.PCB_TRACK(b);t.SetLayer(pcbnew.F_Cu);t.SetNet(n);t.SetWidth(pcbnew.FromMM(.20));t.SetStart(V(*a));t.SetEnd(V(*z));b.Add(t)
for a,z in [((219.5,115.0),(217.0,115.0)),((217.0,115.0),(217.0,112.0)),((217.0,112.0),(229.0,112.0)),((229.0,112.0),(229.0,107.0)),((229.0,107.0),(227.25,107.0))]: tr(a,z)
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
