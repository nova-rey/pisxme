"""Disposable local joins for the bridge-3V3 support island."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE24_BRIDGE_3V3_CAP_CHAIN.kicad_pcb'; OUT=R/'PHASE24_BRIDGE_3V3_SUPPORT_JOIN.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('/REGULATORS/BRIDGE_3V3')
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(layer,a,z):
    t=pcbnew.PCB_TRACK(b);t.SetLayer(layer);t.SetNet(n);t.SetWidth(pcbnew.FromMM(.20));t.SetStart(V(*a));t.SetEnd(V(*z));b.Add(t)
# R11.1 and C18.2 form the adjacent support island.
tr(pcbnew.F_Cu,(214.5,95.0),(220.95,95.0))
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
