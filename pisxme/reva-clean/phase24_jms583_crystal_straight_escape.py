"""Disposable direct crystal escape with Y10 fixed at its accepted position."""
import argparse
import pcbnew

ap=argparse.ArgumentParser(); ap.add_argument('base'); ap.add_argument('output'); a=ap.parse_args()
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(q): return pcbnew.ToMM(q.GetPosition().x),pcbnew.ToMM(q.GetPosition().y)
def seg(b,n,p,q,layer,w=.15):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*p)); t.SetEnd(P(*q)); t.SetLayer(layer); t.SetWidth(pcbnew.FromMM(w)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,p):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*p)); v.SetWidth(pcbnew.FromMM(.55)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
b=pcbnew.LoadBoard(a.base); u=b.FindFootprintByReference('U11'); y=b.FindFootprintByReference('Y10')
for name,up,yp,escape,transition,approach in [
 ('XIN','50','1',(138.6,132.4),(138.6,124.0),(142.8,124.0)),
 ('XOUT','51','2',(139.6,132.4),(139.6,125.6),(142.8,125.6)),
]:
 n=b.FindNet(name)
 for t in list(b.GetTracks()):
  if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
 s=xy(u.FindPadByNumber(up)); d=xy(y.FindPadByNumber(yp))
 seg(b,n,s,escape,pcbnew.F_Cu); via(b,n,escape); seg(b,n,escape,transition,pcbnew.B_Cu,.20); via(b,n,transition); seg(b,n,transition,approach,pcbnew.F_Cu); seg(b,n,approach,d,pcbnew.F_Cu)
b.Save(a.output); print(a.output)
