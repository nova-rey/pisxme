"""Use a local 0.15 mm QFN escape, then normal JMS_XAVDDH routing."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE24_STORAGE_MKEY_USB3_REXT_LOCAL_20260912.kicad_pcb'; OUT=R/'PHASE24_STORAGE_MKEY_USB3_XAVDDH_LOCAL_V3_20260912.kicad_pcb'
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p):return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def tr(b,n,a,z,l,w):
 if a==z:return
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(w));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.60));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
b=pcbnew.LoadBoard(str(BASE));u=b.FindFootprintByReference('U11');c=b.FindFootprintByReference('C84');n=b.FindNet('JMS_XAVDDH')
if not u or not c or not n:raise RuntimeError('missing XAVDDH endpoint')
c.SetPosition(P(150,120))
for item in list(b.GetTracks()):
 if item.GetNetCode()==n.GetNetCode():b.RemoveNative(item)
s=xy(u.FindPadByNumber('52'));d=xy(c.FindPadByNumber('1'))
tr(b,n,s,(137.6,s[1]),pcbnew.F_Cu,.15);tr(b,n,(137.6,s[1]),(137.0,130.0),pcbnew.F_Cu,.15)
via(b,n,(137.0,130.0));tr(b,n,(137.0,130.0),(149.0,118.0),pcbnew.B_Cu,.20);via(b,n,(149.0,118.0));tr(b,n,(149.0,118.0),d,pcbnew.F_Cu,.20)
b.Save(str(OUT));print(OUT)
