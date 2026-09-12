"""Bounded VDDREG outer escape trial on the current crystal candidate."""
import argparse
import pcbnew

ap = argparse.ArgumentParser(); ap.add_argument("base"); ap.add_argument("output"); a = ap.parse_args()
def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(q): return pcbnew.ToMM(q.GetPosition().x), pcbnew.ToMM(q.GetPosition().y)
def track(b, n, p, q, layer, width=.15):
    t=pcbnew.PCB_TRACK(b); t.SetStart(P(*p)); t.SetEnd(P(*q)); t.SetLayer(layer)
    t.SetWidth(pcbnew.FromMM(width)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b, n, p):
    v=pcbnew.PCB_VIA(b); v.SetPosition(P(*p)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30))
    v.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
b=pcbnew.LoadBoard(a.base); n=b.FindNet("JMS_VDDREG_5V"); u=b.FindFootprintByReference("U11"); l=b.FindFootprintByReference("L10")
for t in list(b.GetTracks()):
    if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
s=xy(u.FindPadByNumber("1")); d=xy(l.FindPadByNumber("2")); v1=(134.0,132.0); v2=(134.0,125.0)
track(b,n,s,v1,pcbnew.F_Cu); via(b,n,v1); track(b,n,v1,v2,pcbnew.B_Cu,.20); via(b,n,v2); track(b,n,v2,d,pcbnew.F_Cu)
b.Save(a.output); print(a.output)
