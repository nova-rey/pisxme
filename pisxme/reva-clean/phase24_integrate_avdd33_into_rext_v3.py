"""Route AVDD33 around CM5_PERST with a local ordinary-via transition."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;BASE=R/'PHASE24_STORAGE_MKEY_USB3_REXT_LOCAL_20260912.kicad_pcb';OUT=R/'PHASE24_STORAGE_MKEY_USB3_REXT_AVDD33_LOCAL_V3_20260912.kicad_pcb'
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,a,z,l,w=.15):
 if a==z:return
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(w));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.60));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
b=pcbnew.LoadBoard(str(BASE));u=b.FindFootprintByReference('U11');c=b.FindFootprintByReference('C80');n=b.FindNet('JMS_AVDD33')
if not u or not c or not n:raise RuntimeError('missing AVDD33 endpoint')
c.SetPosition(P(155,146))
for item in list(b.GetTracks()):
 if item.GetNetCode()==n.GetNetCode():b.RemoveNative(item)
s=u.FindPadByNumber('19').GetPosition();d=c.FindPadByNumber('1').GetPosition();src=(pcbnew.ToMM(s.x),pcbnew.ToMM(s.y));dst=(pcbnew.ToMM(d.x),pcbnew.ToMM(d.y));a=(142.2,139.5);z=(154.5,139.5)
tr(b,n,src,a,pcbnew.F_Cu);via(b,n,a);tr(b,n,a,z,pcbnew.B_Cu);via(b,n,z);tr(b,n,z,dst,pcbnew.F_Cu)
b.Save(str(OUT));print(OUT)
