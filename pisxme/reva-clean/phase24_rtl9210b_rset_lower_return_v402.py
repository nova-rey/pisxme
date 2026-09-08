"""V402: lower the RSET B.Cu return below the RTL_3V3 transition."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_RXP_SOURCE_OFFSET_V401.kicad_pcb'; out=H/'PHASE24_RTL9210B_RSET_LOWER_RETURN_V402.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
b=pcbnew.LoadBoard(str(src))
for x in list(b.GetTracks()):
 if x.GetNetname()=='RSET': b.RemoveNative(x)
n=b.FindNet('RSET'); seg(b,n,F,(109.2,65.95),(109.2,67.5)); seg(b,n,F,(109.2,67.5),(108.5,67.5)); seg(b,n,F,(108.5,67.5),(108.5,69.5)); via(b,n,(108.5,69.5)); seg(b,n,B,(108.5,69.5),(101.4,69.5)); via(b,n,(101.4,69.5)); seg(b,n,F,(101.4,69.5),(101.4,71.0))
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
