"""Disposable local B.Cu join for the isolated R22.1 rail pad."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_BRIDGE_1V1_R19_JOIN.kicad_pcb'; OUT=R/'PHASE24_BRIDGE_1V1_R22_JOIN.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('/REGULATORS/BRIDGE_1V1')
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(layer,a,z):
    t=pcbnew.PCB_TRACK(b);t.SetLayer(layer);t.SetNet(n);t.SetWidth(pcbnew.FromMM(.20));t.SetStart(V(*a));t.SetEnd(V(*z));b.Add(t)
q=pcbnew.PCB_VIA(b);q.SetPosition(V(239.5,116.5));q.SetWidth(pcbnew.FromMM(.50));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);q.SetNet(n);b.Add(q)
tr(pcbnew.F_Cu,(239.5,115.0),(239.5,116.5))
tr(pcbnew.B_Cu,(239.5,116.5),(239.5,113.0));tr(pcbnew.B_Cu,(239.5,113.0),(243.5,113.0));tr(pcbnew.B_Cu,(243.5,113.0),(243.5,118.5))
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
