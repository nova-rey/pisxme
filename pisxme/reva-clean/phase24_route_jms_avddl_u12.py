"""Join U12.36 to the existing JMS_AVDDL decoupler node."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;BASE=R/'PHASE24_STORAGE_MKEY_USB3_AVDDL_LOCAL_20260912.kicad_pcb';OUT=R/'PHASE24_STORAGE_MKEY_USB3_AVDDL_U12_LOCAL_20260912.kicad_pcb'
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p):return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def tr(b,n,a,z,l,w):
 if a==z:return
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(w));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.60));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
b=pcbnew.LoadBoard(str(BASE));u=b.FindFootprintByReference('U12');c=b.FindFootprintByReference('C83');n=b.FindNet('JMS_AVDDL')
if not u or not c or not n:raise RuntimeError('missing AVDDL endpoint')
# Preserve the existing U11-to-C83 branch and its vias.  Only add the U12
# branch; removing same-net items would silently break the accumulated tree.
s=xy(u.FindPadByNumber('36'));d=xy(c.FindPadByNumber('1'));e=(168.0,132.6);f=(168.0,150.5);g=(154.5,150.5)
tr(b,n,s,e,pcbnew.F_Cu,.15);via(b,n,e);tr(b,n,e,f,pcbnew.B_Cu,.20);tr(b,n,f,g,pcbnew.B_Cu,.20);via(b,n,g);tr(b,n,g,d,pcbnew.F_Cu,.20)
b.Save(str(OUT));print(OUT)
