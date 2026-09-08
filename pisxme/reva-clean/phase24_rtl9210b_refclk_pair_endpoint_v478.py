"""V478: REFCLK rows below XTAL_OUT and above the source controls."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_ROTATED_SOURCE_PLANAR_V462.kicad_pcb'; out=H/'PHASE24_RTL9210B_REFCLK_PAIR_ENDPOINT_V478.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.13208)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.60));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
b=pcbnew.LoadBoard(str(src));u=b.FindFootprintByReference('U1')
for name in ('REFCLK_P','REFCLK_N'):
 for x in list(b.GetTracks()):
  if x.GetNetname()==name:b.RemoveNative(x)
for name,pad,q,mid,row,side,entry,dst in [('REFCLK_N','62',(112,70.1),(118,70.1),(118,56),(136,56),(136.75,64.5),(136.75,62.725)),('REFCLK_P','61',(111,71),(119,71),(119,55),(137.25,55),(137.25,60.5),(137.25,62.725))]:
 n=b.FindNet(name);p=u.FindPadByNumber(pad);pp=p.GetPosition();a=(pcbnew.ToMM(pp.x),pcbnew.ToMM(pp.y));seg(b,n,F,a,(a[0],q[1]));seg(b,n,F,(a[0],q[1]),q);via(b,n,q);seg(b,n,B,q,mid);seg(b,n,B,mid,row);seg(b,n,B,row,side);seg(b,n,B,side,entry);via(b,n,entry);seg(b,n,F,entry,dst)
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
