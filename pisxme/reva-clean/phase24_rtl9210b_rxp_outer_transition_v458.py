"""V458: move RX_P's source transition beyond the RX_N fanout endpoint."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_REFCLK_LANE_COALLOCATE_V454.kicad_pcb'; out=H/'PHASE24_RTL9210B_RXP_OUTER_TRANSITION_V458.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z,w=W):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(w); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
b=pcbnew.LoadBoard(str(src)); n=b.FindNet('LANE0_RXP')
for x in list(b.GetTracks()):
 if x.GetNetname()=='LANE0_RXP': b.RemoveNative(x)
# Source pad -> outer transition, then the already-established B.Cu corridor.
seg(b,n,F,(109.95,60.4),(114.5,60.4)); via(b,n,(114.5,60.4))
seg(b,n,B,(114.5,60.4),(114.5,66.5)); via(b,n,(114.5,66.5))
seg(b,n,B,(114.5,66.5),(132.0,66.5)); via(b,n,(132.0,66.5))
seg(b,n,F,(132.0,66.5),(134.25,66.5)); seg(b,n,F,(134.25,66.5),(134.25,62.725))
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
