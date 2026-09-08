"""V464: V462 source fanout with proven connector-side handoff positions."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_ROTATED_SOURCE_PLANAR_V462.kicad_pcb'; out=H/'PHASE24_RTL9210B_FULL_LANE_REFCLK_V464.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.13208)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
b=pcbnew.LoadBoard(str(src)); u=b.FindFootprintByReference('U1')
data=[('REFCLK_P','61',(111,71),(137.25,60.5),(137.25,62.725)),('REFCLK_N','62',(112,70.1),(136.75,64.5),(136.75,62.725)),('LANE0_RXP','64',(113,69.2),(134.25,66.5),(134.25,62.725)),('LANE0_RXN','65',(114,68.3),(133.75,64.5),(133.75,62.725)),('LANE0_TXN','67',(115,67.4),(135.25,59.2),(135.25,62.725)),('LANE0_TXP','68',(116,66.5),(135.75,58.8),(135.75,62.725))]
for name,_,_,_,_ in data:
 for x in list(b.GetTracks()):
  if x.GetNetname()==name: b.RemoveNative(x)
for name,pad,q,h,dst in data:
 n=b.FindNet(name); p=u.FindPadByNumber(pad); pp=p.GetPosition(); a=(pcbnew.ToMM(pp.x),pcbnew.ToMM(pp.y)); seg(b,n,F,a,(a[0],q[1])); seg(b,n,F,(a[0],q[1]),q); via(b,n,q)
 seg(b,n,B,q,(h[0],q[1])); seg(b,n,B,(h[0],q[1]),h); via(b,n,h); seg(b,n,F,h,dst)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
