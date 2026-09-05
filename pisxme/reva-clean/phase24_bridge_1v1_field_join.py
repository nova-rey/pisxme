"""Disposable join from the separated bridge-1V1 cap field to output caps."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_BRIDGE_1V1_CAP_CHAIN.kicad_pcb'; OUT=R/'PHASE24_BRIDGE_1V1_FIELD_JOIN.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('/REGULATORS/BRIDGE_1V1')
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(layer,a,z,w=.20):
    t=pcbnew.PCB_TRACK(b);t.SetLayer(layer);t.SetNet(n);t.SetWidth(pcbnew.FromMM(w));t.SetStart(V(*a));t.SetEnd(V(*z));b.Add(t)
def via(x,y):
    q=pcbnew.PCB_VIA(b);q.SetPosition(V(x,y));q.SetWidth(pcbnew.FromMM(.50));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);q.SetNet(n);b.Add(q)
# C41.1 already has the field via at (203.20,168.00). Approach C46.1
# from its left side with a second ordinary via, outside the pad body.
via(248.55,139.35)
add(pcbnew.B_Cu,(203.20,168.00),(248.55,168.00))
add(pcbnew.B_Cu,(248.55,168.00),(248.55,139.35))
add(pcbnew.F_Cu,(250.00,139.35),(248.55,139.35))
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
