"""Storage-local crystal placement/escape trial on the passing support cohort."""
from pathlib import Path
import argparse
import pcbnew

R=Path(__file__).resolve().parent
ap=argparse.ArgumentParser(); ap.add_argument('base'); ap.add_argument('output'); args=ap.parse_args()
BASE=R/args.base; OUT=R/args.output
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def seg(b,n,a,z,layer=pcbnew.F_Cu):
    if a==z:return
    t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(layer)
    t.SetWidth(pcbnew.FromMM(.15));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,q):
    v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.55));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
def pad(b,r,p): return b.FindFootprintByReference(r).FindPadByNumber(str(p))
def clear(b,name):
    n=b.FindNet(name)
    for i in list(b.GetTracks()):
        if i.GetNetCode()==n.GetNetCode():b.RemoveNative(i)
    return n
b=pcbnew.LoadBoard(str(BASE)); y=b.FindFootprintByReference('Y10'); y.SetPosition(P(131,124))
# Remove the trial's old crystal/REXT copper and rebuild only these nets.
n=clear(b,'JMS_REXT');s=xy(pad(b,'U11',39));d=xy(pad(b,'R80',1))
seg(b,n,s,(145,s[1]));seg(b,n,(145,s[1]),(145,d[1]));seg(b,n,(145,d[1]),d)
for name,up,yp,x1,y1,x2,y2 in [('XIN',50,1,135,129,129.9,123.15),('XOUT',51,2,133,132.2,129.9,124.85)]:
    n=clear(b,name);s=xy(pad(b,'U11',up));d=xy(pad(b,'Y10',yp));v1=(x1,y1);v2=(x2,y2)
    seg(b,n,s,(x1,s[1]));seg(b,n,(x1,s[1]),v1);via(b,n,v1);seg(b,n,v1,v2,pcbnew.B_Cu);via(b,n,v2);seg(b,n,v2,d)
b.Save(str(OUT));print(OUT)
