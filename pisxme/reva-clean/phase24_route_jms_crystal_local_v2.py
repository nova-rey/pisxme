"""Combined REXT/crystal local support arrangement, second bounded trial."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_STORAGE_MKEY_USB3_REXT_LOCAL_20260912.kicad_pcb"
OUT = R / "PHASE24_STORAGE_MKEY_USB3_CRYSTAL_LOCAL_V2_20260912.kicad_pcb"

def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(p): return pcbnew.ToMM(p.GetPosition().x), pcbnew.ToMM(p.GetPosition().y)
def track(b, n, a, z, layer=pcbnew.F_Cu):
    if a == z: return
    t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(layer)
    t.SetWidth(pcbnew.FromMM(.20)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b, n, p):
    v=pcbnew.PCB_VIA(b); v.SetPosition(P(*p)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30))
    v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)

b=pcbnew.LoadBoard(str(BASE)); u=b.FindFootprintByReference('U11'); r=b.FindFootprintByReference('R80'); y=b.FindFootprintByReference('Y10')
if not u or not r or not y: raise RuntimeError('missing support endpoint')
r.SetPosition(P(155,130)); y.SetPosition(P(150,125))
for name, ref, pad, pts in [('JMS_REXT','R80','1',[(147,135.6),(154,135.6),(154,130)]),
                             ('XIN','Y10','1',[(135,131.4),(135,128)]),
                             ('XOUT','Y10','2',[(136,131.4),(136,129.5)])]:
    n=b.FindNet(name)
    if not n: raise RuntimeError('missing '+name)
    for item in list(b.GetTracks()):
        if item.GetNetCode()==n.GetNetCode(): b.RemoveNative(item)
    if name=='JMS_REXT':
        src=xy(u.FindPadByNumber('39')); dst=xy(r.FindPadByNumber('1'))
        q=[src,*pts,dst]
        for a,z in zip(q,q[1:]): track(b,n,a,z)
    else:
        up='50' if name=='XIN' else '51'; src=xy(u.FindPadByNumber(up)); dst=xy(y.FindPadByNumber(pad)); q=[src,*pts]
        for a,z in zip(q,q[1:]): track(b,n,a,z)
        via(b,n,pts[-1]); end=(148 if name=='XIN' else 149,128 if name=='XIN' else 129.5)
        track(b,n,pts[-1],end,pcbnew.B_Cu); via(b,n,end)
        q2=[end,(end[0],dst[1]),dst]
        for a,z in zip(q2,q2[1:]): track(b,n,a,z)
b.Save(str(OUT)); print(OUT)
