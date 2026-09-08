"""V459: RX_P lower source transition, preserving V454's RX_N launch."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_REFCLK_LANE_COALLOCATE_V454.kicad_pcb'; out=H/'PHASE24_RTL9210B_RXP_LOWER_TRANSITION_V459.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
b=pcbnew.LoadBoard(str(src)); n=b.FindNet('LANE0_RXP')
for x in list(b.GetTracks()):
 if x.GetNetname()=='LANE0_RXP': b.RemoveNative(x)
seg(b,n,F,(109.95,60.4),(110.8,60.4)); seg(b,n,F,(110.8,60.4),(110.8,62.5)); via(b,n,(110.8,62.5))
seg(b,n,B,(110.8,62.5),(110.8,66.5)); via(b,n,(110.8,66.5)); seg(b,n,B,(110.8,66.5),(132,66.5)); via(b,n,(132,66.5))
seg(b,n,F,(132,66.5),(134.25,66.5)); seg(b,n,F,(134.25,66.5),(134.25,62.725))
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
