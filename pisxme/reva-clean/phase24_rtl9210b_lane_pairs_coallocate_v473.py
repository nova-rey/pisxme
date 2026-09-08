"""V473: integrate the validated RX and TX pair endpoint primitives."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_ROTATED_SOURCE_PLANAR_V462.kicad_pcb'; out=H/'PHASE24_RTL9210B_LANE_PAIRS_COALLOCATE_V473.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.13208)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.60));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
b=pcbnew.LoadBoard(str(src));u=b.FindFootprintByReference('U1')
for name in ('LANE0_RXP','LANE0_RXN','LANE0_TXN','LANE0_TXP'):
 for x in list(b.GetTracks()):
  if x.GetNetname()==name:b.RemoveNative(x)
for name,pad,q,mid,handoff,dst in [('LANE0_RXN','65',(114,68.3),(124,68.3),(133.25,64.5),(133.75,62.725)),('LANE0_RXP','64',(113,69.2),(125,69.2),(134.25,66.5),(134.25,62.725))]:
 n=b.FindNet(name);p=u.FindPadByNumber(pad);pp=p.GetPosition();a=(pcbnew.ToMM(pp.x),pcbnew.ToMM(pp.y));seg(b,n,F,a,(a[0],q[1]));seg(b,n,F,(a[0],q[1]),q);via(b,n,q);seg(b,n,B,q,(mid[0],q[1]));seg(b,n,B,(mid[0],q[1]),(mid[0],handoff[1]));seg(b,n,B,(mid[0],handoff[1]),handoff);via(b,n,handoff);seg(b,n,F,handoff,dst)
for name,q,mid,row,side,entry,dst in [('LANE0_TXN',(115,67.4),(120,67.4),(120,78),(142,78),(134.75,59.2),(135.25,62.725)),('LANE0_TXP',(116,66.5),(121,66.5),(121,77),(121,57.5),(135.75,57.5),(135.75,62.725))]:
 n=b.FindNet(name);seg(b,n,B,q,mid);seg(b,n,B,mid,row);seg(b,n,B,row,side);seg(b,n,B,side,entry);via(b,n,entry);seg(b,n,F,entry,dst)
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
