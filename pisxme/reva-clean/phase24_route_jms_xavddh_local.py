"""Add a native-pad JMS_XAVDDH decoupler join to the REXT base."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_STORAGE_MKEY_USB3_REXT_LOCAL_20260912.kicad_pcb'
OUT=R/'PHASE24_STORAGE_MKEY_USB3_XAVDDH_LOCAL_20260912.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def tr(b,n,a,z,l):
 if a==z:return
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.60));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
b=pcbnew.LoadBoard(str(BASE));u=b.FindFootprintByReference('U11');c=b.FindFootprintByReference('C84');n=b.FindNet('JMS_XAVDDH')
if not u or not c or not n:raise RuntimeError('missing XAVDDH endpoint')
c.SetPosition(P(150,120))
for item in list(b.GetTracks()):
 if item.GetNetCode()==n.GetNetCode():b.RemoveNative(item)
src=xy(u.FindPadByNumber('52'));dst=xy(c.FindPadByNumber('1'));p=[src,(140,src[1]),(140,140)]
for a,z in zip(p,p[1:]):tr(b,n,a,z,pcbnew.F_Cu)
via(b,n,p[-1]); q=(149,121.5); tr(b,n,p[-1],q,pcbnew.B_Cu); via(b,n,q); tr(b,n,q,dst,pcbnew.F_Cu)
b.Save(str(OUT));print(OUT)
