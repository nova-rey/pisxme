"""Disposable outboard B.Cu join for the isolated R19.1 rail pad."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_BRIDGE_1V1_FIELD_JOIN.kicad_pcb'; OUT=R/'PHASE24_BRIDGE_1V1_R19_JOIN.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('/REGULATORS/BRIDGE_1V1')
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(layer,a,z):
    t=pcbnew.PCB_TRACK(b);t.SetLayer(layer);t.SetNet(n);t.SetWidth(pcbnew.FromMM(.20));t.SetStart(V(*a));t.SetEnd(V(*z));b.Add(t)
q=pcbnew.PCB_VIA(b);q.SetPosition(V(243.5,118.5));q.SetWidth(pcbnew.FromMM(.50));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);q.SetNet(n);b.Add(q)
tr(pcbnew.F_Cu,(242.0,118.5),(243.5,118.5))
tr(pcbnew.B_Cu,(243.5,118.5),(263.0,118.5));tr(pcbnew.B_Cu,(263.0,118.5),(263.0,139.35));tr(pcbnew.B_Cu,(263.0,139.35),(248.55,139.35))
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
