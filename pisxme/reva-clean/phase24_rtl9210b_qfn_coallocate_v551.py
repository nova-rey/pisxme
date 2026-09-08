"""V551: bottom 1V1 return below the REFCLK launch endpoint."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;src=H/'PHASE24_RTL9210B_QFN_COALLOCATE_V546.kicad_pcb';out=H/'PHASE24_RTL9210B_QFN_COALLOCATE_V551.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.13208)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,a):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*a));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());v.SetWidth(pcbnew.FromMM(.6));v.SetDrill(pcbnew.FromMM(.3));b.Add(v)
b=pcbnew.LoadBoard(str(src));n=b.FindNet('RTL_1V1')
for a,z in [((104.0,65.95),(103.5,72.5)),((106.0,65.95),(105.5,72.5)),((107.2,65.95),(108.0,72.5))]:tr(b,n,F,a,z);via(b,n,z)
for a,z in [((103.5,72.5),(105.5,72.5)),((105.5,72.5),(108.0,72.5)),((108.0,72.5),(113.0,72.5)),((113.0,72.5),(113.0,64.8)),((113.0,64.8),(102.9,64.8))]:tr(b,n,B,a,z)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
