"""Restore the shared JMS_VDDREG_5V tree on the cumulative AVDDL base."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;BASE=R/'PHASE24_STORAGE_MKEY_USB3_AVDDL_U12_LOCAL_20260912.kicad_pcb';OUT=R/'PHASE24_STORAGE_MKEY_USB3_VDDREG_AVDDL_BASE_20260912.kicad_pcb'
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p):return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def tr(b,n,a,z,l,w=.20):
 if a==z:return
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(w));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.60));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
b=pcbnew.LoadBoard(str(BASE));u=b.FindFootprintByReference('U11');u12=b.FindFootprintByReference('U12');l=b.FindFootprintByReference('L10');n=b.FindNet('JMS_VDDREG_5V')
if not u or not u12 or not l or not n:raise RuntimeError('missing VDDREG endpoint')
for item in list(b.GetTracks()):
 if item.GetNetCode()==n.GetNetCode():b.RemoveNative(item)
a=xy(u.FindPadByNumber('1'));c=xy(u12.FindPadByNumber('1'));d=xy(l.FindPadByNumber('2'));v1=(132.5,132.0);v2=(132.5,123.5);v3=(157.0,131.8);v4=(157.0,123.5)
tr(b,n,a,v1,pcbnew.F_Cu);via(b,n,v1);tr(b,n,v1,v2,pcbnew.B_Cu);via(b,n,v2);tr(b,n,v2,v4,pcbnew.B_Cu);via(b,n,v4);tr(b,n,v4,v3,pcbnew.F_Cu);via(b,n,v3);tr(b,n,v3,c,pcbnew.F_Cu)
tr(b,n,v2,(137.15,123.5),pcbnew.F_Cu);tr(b,n,(137.15,123.5),d,pcbnew.F_Cu)
b.Save(str(OUT));print(OUT)
