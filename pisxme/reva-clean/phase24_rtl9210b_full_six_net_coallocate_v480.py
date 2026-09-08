"""V480: complete six-net coallocation from native U1 pads to J1."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_ROTATED_SOURCE_PLANAR_V462.kicad_pcb'; out=H/'PHASE24_RTL9210B_FULL_SIX_NET_COALLOCATE_V480.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.13208)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.60));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
b=pcbnew.LoadBoard(str(src));u=b.FindFootprintByReference('U1')
names=('REFCLK_P','REFCLK_N','LANE0_RXP','LANE0_RXN','LANE0_TXN','LANE0_TXP')
for name in names:
 for x in list(b.GetTracks()):
  if x.GetNetname()==name:b.RemoveNative(x)
source={'REFCLK_P':('61',(111,71)),'REFCLK_N':('62',(112,70.1)),'LANE0_RXP':('64',(113,69.2)),'LANE0_RXN':('65',(114,68.3)),'LANE0_TXN':('67',(115,67.4)),'LANE0_TXP':('68',(116,66.5))}
for name,(pad,q) in source.items():
 n=b.FindNet(name);p=u.FindPadByNumber(pad);pp=p.GetPosition();a=(pcbnew.ToMM(pp.x),pcbnew.ToMM(pp.y));seg(b,n,F,a,(a[0],q[1]));seg(b,n,F,(a[0],q[1]),q);via(b,n,q)
# RX pair, from V466: separated B.Cu pair with outward RX_N transition.
for name,q,mid,handoff,dst in [('LANE0_RXN',(114,68.3),(124,68.3),(133.25,64.5),(133.75,62.725)),('LANE0_RXP',(113,69.2),(125,69.2),(134.25,66.5),(134.25,62.725))]:
 n=b.FindNet(name);seg(b,n,B,q,(mid[0],q[1]));seg(b,n,B,(mid[0],q[1]),(mid[0],handoff[1]));seg(b,n,B,(mid[0],handoff[1]),handoff);via(b,n,handoff);seg(b,n,F,handoff,dst)
# TX pair, layer split before the side corridor to avoid the RX/control field.
for name,q,mid,row,side,entry,dst in [('LANE0_TXN',(115,67.4),(120,67.4),(120,80),(142,80),(134.75,59.2),(135.25,62.725)),('LANE0_TXP',(116,66.5),(121,66.5),(121,79),(143,79),(135.75,57.5),(135.75,62.725))]:
 n=b.FindNet(name);seg(b,n,B,q,mid);via(b,n,mid);seg(b,n,F,mid,row);seg(b,n,F,row,side);via(b,n,side);seg(b,n,B,side,(side[0],entry[1]));seg(b,n,B,(side[0],entry[1]),entry);via(b,n,entry);seg(b,n,F,entry,dst)
# REFCLK_P uses the spare B.Cu vertical x112; REFCLK_N changes to F.Cu
# before the lane source corridors. Both use separated connector handoffs.
n=b.FindNet('REFCLK_P');seg(b,n,B,(111,71),(112,71));seg(b,n,B,(112,71),(112,55));seg(b,n,B,(112,55),(137.25,55));seg(b,n,B,(137.25,55),(137.25,60.5));via(b,n,(137.25,60.5));seg(b,n,F,(137.25,60.5),(137.25,62.725))
n=b.FindNet('REFCLK_N');seg(b,n,F,(112,70.1),(105,70.1));seg(b,n,F,(105,70.1),(105,56));seg(b,n,F,(105,56),(136.0,56));seg(b,n,F,(136,56),(136.75,64.5));via(b,n,(136.75,64.5));seg(b,n,F,(136.75,64.5),(136.75,62.725))
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
