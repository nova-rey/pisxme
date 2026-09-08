"""V555: outboard B.Cu bottom RTL_1V1 return to the valid upper trunk."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_QFN_COALLOCATE_V546.kicad_pcb';out=H/'PHASE24_RTL9210B_QFN_COALLOCATE_V555.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.13208)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,a):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*a));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());v.SetWidth(pcbnew.FromMM(.6));v.SetDrill(pcbnew.FromMM(.3));b.Add(v)
b=pcbnew.LoadBoard(str(src));n=b.FindNet('RTL_1V1')
for a,z in [((104.0,65.95),(104.0,68.8)),((106.0,65.95),(105.5,68.8)),((107.2,65.95),(108.6,68.8))]:tr(b,n,F,a,z);via(b,n,z)
tr(b,n,B,(104.0,68.8),(112.4,68.8));tr(b,n,B,(105.5,68.8),(104.0,68.8));tr(b,n,B,(108.6,68.8),(105.5,68.8));tr(b,n,B,(112.4,68.8),(112.4,57.3));tr(b,n,B,(112.4,57.3),(106.4,57.3))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
