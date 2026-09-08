"""V564: route RTL_5V through the outboard lower acreage corridor."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V562.kicad_pcb';out=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V564_RTL5V.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,a):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*a));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());v.SetWidth(pcbnew.FromMM(.6));v.SetDrill(pcbnew.FromMM(.3));b.Add(v)
b=pcbnew.LoadBoard(str(src));n=b.FindNet('RTL_5V')
tr(b,n,F,(102.8,58.05),(96.5,58.05));tr(b,n,F,(102.05,64.8),(96.5,64.8));tr(b,n,F,(96.5,64.8),(96.5,77.0));via(b,n,(96.5,77.0));tr(b,n,B,(96.5,77.0),(124.4,77.0));via(b,n,(124.4,77.0));tr(b,n,F,(124.4,77.0),(124.4,61.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
