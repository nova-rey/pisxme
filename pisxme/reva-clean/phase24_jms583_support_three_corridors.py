"""Disposable JMS583 crystal/VDDREG routing with separated B.Cu corridors."""
import argparse
import pcbnew

ap=argparse.ArgumentParser(); ap.add_argument('base'); ap.add_argument('output'); a=ap.parse_args()
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(q): return pcbnew.ToMM(q.GetPosition().x),pcbnew.ToMM(q.GetPosition().y)
def seg(b,n,p,q,l,w=.15):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*p));t.SetEnd(P(*q));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(w));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,p):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*p));v.SetWidth(pcbnew.FromMM(.55));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
b=pcbnew.LoadBoard(a.base);u=b.FindFootprintByReference('U11');y=b.FindFootprintByReference('Y10');l=b.FindFootprintByReference('L10')
def clear(name):
 n=b.FindNet(name)
 for t in list(b.GetTracks()):
  if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
 return n
n=clear('JMS_VDDREG_5V');s=xy(u.FindPadByNumber('1'));d=xy(l.FindPadByNumber('2'));q=(128.0,130.5);v=(128.0,123.5)
seg(b,n,s,q,pcbnew.F_Cu);via(b,n,q);seg(b,n,q,v,pcbnew.B_Cu,.20);via(b,n,v);seg(b,n,v,(137.15,123.5),pcbnew.F_Cu,.15);seg(b,n,(137.15,123.5),d,pcbnew.F_Cu,.15)
for name,up,yp,source,escape,transition,launch,via_y in [
 ('XIN','50','1',xy(u.FindPadByNumber('50')),(137.4,134.8),(130.0,134.8),(140.0,122.5),122.5),
 ('XOUT','51','2',xy(u.FindPadByNumber('51')),(137.8,135.6),(131.0,135.6),(140.0,126.5),126.5),
]:
 n=clear(name);d=xy(y.FindPadByNumber(yp));via1=transition;via2=launch
 seg(b,n,source,escape,pcbnew.F_Cu);seg(b,n,escape,transition,pcbnew.F_Cu);via(b,n,via1)
 seg(b,n,via1,(via1[0],via_y),pcbnew.B_Cu,.20);seg(b,n,(via1[0],via_y),via2,pcbnew.B_Cu,.20);via(b,n,via2)
 seg(b,n,via2,(146.0,via_y),pcbnew.F_Cu,.15);seg(b,n,(146.0,via_y),d,pcbnew.F_Cu,.15)
b.Save(a.output);print(a.output)
