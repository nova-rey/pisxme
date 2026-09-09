"""Repair only the malformed V3 RX source dogbones with FULL7 geometry."""
from pathlib import Path
import argparse
import pcbnew

R=Path(__file__).resolve().parent
ap=argparse.ArgumentParser(); ap.add_argument('base'); ap.add_argument('output'); args=ap.parse_args()
BASE=R/args.base; OUT=R/args.output
F=pcbnew.F_Cu; W=pcbnew.FromMM(.15)
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def xy(p):
    q=p.GetPosition() if hasattr(p,'GetPosition') else p
    return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
def tr(b,n,a,z):
    t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(F)
    t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
b=pcbnew.LoadBoard(str(BASE));j=b.FindFootprintByReference('J7')
for name,jp,x in (('CM5_USB3_RX_N','128',73.0),('CM5_USB3_RX_P','130',75.0)):
    n=b.FindNet(name);p=xy(j.FindPadByNumber(jp))
    for t in list(b.GetTracks()):
        if t.GetNetCode()!=n.GetNetCode() or t.GetLayer()!=F: continue
        a=xy(t.GetStart());z=xy(t.GetEnd())
        if max(a[0],z[0])<80: b.RemoveNative(t)
    tr(b,n,p,(x,p[1]));tr(b,n,(x,p[1]),(x,88.0 if name.endswith('N') else 90.0))
    v=pcbnew.PCB_VIA(b);v.SetPosition(V(x,88.0 if name.endswith('N') else 90.0));v.SetWidth(pcbnew.FromMM(.5));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
# Keep RX_N's target via outside U12's 2.05 x 7.55 mm exposed pad.  The
# inherited V3 endpoint at (155,137.8) becomes a real short once pad 43 is
# correctly grounded by the source authority.
n=b.FindNet('CM5_USB3_RX_N')
for t in list(b.GetTracks()):
    if t.GetNetCode()!=n.GetNetCode(): continue
    a=xy(t.GetStart()); z=xy(t.GetEnd())
    if t.GetLayer()==pcbnew.B_Cu and abs(z[0]-155.0)<.01 and abs(z[1]-137.8)<.01:
        t.SetEnd(V(151.0,137.8))
    elif t.GetLayer()==pcbnew.F_Cu and max(a[0],z[0])>150 and min(a[1],z[1])>137.0:
        b.RemoveNative(t)
for item in list(b.GetTracks()):
    if not isinstance(item, pcbnew.PCB_VIA): continue
    q=xy(item)
    if item.GetNetCode()==n.GetNetCode() and abs(q[0]-155.0)<.01 and abs(q[1]-137.8)<.01:
        b.RemoveNative(item)
# The straight B.Cu corridor intersects the existing XOUT return via.  Add a
# small, layer-permitted dogleg around that single obstacle; this is a route
# implementation trial, not a synthetic connectivity edge.
for t in list(b.GetTracks()):
    if not isinstance(t, pcbnew.PCB_TRACK) or t.GetNetCode()!=n.GetNetCode() or t.GetLayer()!=pcbnew.B_Cu: continue
    z=xy(t.GetEnd())
    if abs(z[0]-151.0)<.01 and abs(z[1]-137.8)<.01:
        b.RemoveNative(t)
path=[(73.0,88.0),(134.0,124.0),(134.0,126.5),(140.0,126.5),(140.0,131.0),(151.0,137.8)]
for a,z in zip(path,path[1:]):
    t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(pcbnew.B_Cu); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
tr(b,n,(151.0,137.8),(153.5,137.8))
v=pcbnew.PCB_VIA(b);v.SetPosition(V(151.0,137.8));v.SetWidth(pcbnew.FromMM(.5));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
