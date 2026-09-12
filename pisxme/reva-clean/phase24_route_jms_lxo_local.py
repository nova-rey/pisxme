"""Add the JMS583 LXO-to-L10 native-pad support join."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;BASE=R/'PHASE24_STORAGE_MKEY_USB3_REXT_AVDD33_LOCAL_V3_20260912.kicad_pcb';OUT=R/'PHASE24_STORAGE_MKEY_USB3_LXO_LOCAL_20260912.kicad_pcb'
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p):return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def tr(b,n,a,z,l,w):
 if a==z:return
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(w));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.60));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
b=pcbnew.LoadBoard(str(BASE));u=b.FindFootprintByReference('U11');l=b.FindFootprintByReference('L10');n=b.FindNet('LXO')
if not u or not l or not n:raise RuntimeError('missing LXO endpoint')
for item in list(b.GetTracks()):
 if item.GetNetCode()==n.GetNetCode():b.RemoveNative(item)
s=xy(u.FindPadByNumber('64'));d=xy(l.FindPadByNumber('1'));e=(143.0,130.0);z=(134.85,130.0)
tr(b,n,s,e,pcbnew.F_Cu,.15);via(b,n,e);tr(b,n,e,z,pcbnew.B_Cu,.20);via(b,n,z);tr(b,n,z,d,pcbnew.F_Cu,.20)
b.Save(str(OUT));print(OUT)
