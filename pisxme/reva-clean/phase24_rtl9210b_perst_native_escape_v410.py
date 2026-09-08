"""V410: regenerate PERST_N from the actual U1.14 pad to J1.50."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_XTALIN_ENDPOINT_V404.kicad_pcb'; out=H/'PHASE24_RTL9210B_PERST_NATIVE_ESCAPE_V410.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(.50)); v.SetDrill(pcbnew.FromMM(.25)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
b=pcbnew.LoadBoard(str(src)); n=b.FindNet('PERST_N')
seg(b,n,F,(104.0,58.05),(105.2,58.05)); via(b,n,(105.2,58.05)); seg(b,n,B,(105.2,58.05),(105.2,74.0)); seg(b,n,B,(105.2,74.0),(134.5,74.0)); via(b,n,(134.5,74.0)); seg(b,n,F,(134.5,74.0),(136.0,70.275))
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
