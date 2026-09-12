"""Compose the accepted V1562 J3 handoff with the accepted V1570 R81 branch."""
from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent
b=pcbnew.LoadBoard(str(R/'PHASE24_STORAGE_M2_POWER_IN2_ZONE_V1562.kicad_pcb'))
n=b.FindNet('STORAGE_3V3'); assert n
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(layer,a,z,w):
    t=pcbnew.PCB_TRACK(b); t.SetLayer(layer); t.SetStart(P(*a)); t.SetEnd(P(*z));
    t.SetWidth(pcbnew.FromMM(w)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(x,y):
    v=pcbnew.PCB_VIA(b); v.SetPosition(P(x,y)); v.SetWidth(pcbnew.FromMM(.80));
    v.SetDrill(pcbnew.FromMM(.40)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);
    v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)

# Exact V1570 R81 branch, joining V1562's existing In2 handoff at x=232.
tr(pcbnew.F_Cu,(125.5,145.0),(126.5,144.2),.30)
via(126.5,144.2)
tr(pcbnew.In2_Cu,(126.5,144.2),(132.0,138.5),.60)
tr(pcbnew.In2_Cu,(132.0,138.5),(150.0,138.5),.60)
tr(pcbnew.In2_Cu,(150.0,138.5),(232.0,146.0),.60)
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
out=R/'PHASE24_STORAGE_M2_POWER_V1562_PLUS_R81_V96.kicad_pcb'
b.Save(str(out)); print(out)
