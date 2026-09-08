"""V460: rotated U1, all source transitions outboard in pad order."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_CLKREQ_QFN_CLEARANCE_V431.kicad_pcb'; out=H/'PHASE24_RTL9210B_ROTATED_SOURCE_OUTBOARD_V460.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.13208)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(F); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
b=pcbnew.LoadBoard(str(src)); u=b.FindFootprintByReference('U1'); pos=u.GetPosition(); exp=u.FindPadByNumber('69').GetPosition(); u.SetOrientationDegrees(90); rot=u.FindPadByNumber('69').GetPosition(); u.SetPosition(pcbnew.VECTOR2I(pos.x+exp.x-rot.x,pos.y+exp.y-rot.y))
def local(q):
 x,y=pcbnew.ToMM(q.x),pcbnew.ToMM(q.y); return 98<=x<=117 and 52<=y<=78
for x in list(b.GetTracks()):
 if local(x.GetPosition()) or (hasattr(x,'GetStart') and local(x.GetStart())) or (hasattr(x,'GetEnd') and local(x.GetEnd())): b.RemoveNative(x)
srcs=[('REFCLK_P','61',(111.0,68.0)),('REFCLK_N','62',(112.0,68.0)),('LANE0_RXP','64',(113.0,68.0)),('LANE0_RXN','65',(114.0,68.0)),('LANE0_TXN','67',(115.0,68.0)),('LANE0_TXP','68',(116.0,68.0))]
for name,pad,q in srcs:
 n=b.FindNet(name); p=u.FindPadByNumber(pad); pp=p.GetPosition(); seg(b,n,(pcbnew.ToMM(pp.x),pcbnew.ToMM(pp.y)),q); via(b,n,q)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
