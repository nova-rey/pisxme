"""Disposable U12 RX pair escape outside the HD3SS6126 exposed pad."""
from pathlib import Path
import argparse, pcbnew
ap=argparse.ArgumentParser(); ap.add_argument('base'); ap.add_argument('output'); a=ap.parse_args()
R=Path(__file__).resolve().parent; b=pcbnew.LoadBoard(str(R/a.base)); F,B=pcbnew.F_Cu,pcbnew.B_Cu
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def p(ref,num): return b.FindFootprintByReference(ref).FindPadByNumber(str(num))
def xy(q): return pcbnew.ToMM(q.GetPosition().x),pcbnew.ToMM(q.GetPosition().y)
def tr(n,a,z,l):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(.15)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(n,q):
 v=pcbnew.PCB_VIA(b); v.SetPosition(V(*q)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
for name,pin,src in [('CM5_USB3_RX_N',16,(73.0,88.0)),('CM5_USB3_RX_P',15,(75.0,90.0))]:
 n=b.FindNet(name)
 for t in list(b.GetTracks()):
  if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
 # Existing source-side B.Cu corridor is retained to an external transition.
 q=(150.9,137.8) if name.endswith('_N') else (151.9,137.4)
 # Preserve the proven source-side slope to its former endpoint on B.Cu;
 # backtrack outside the exposed-pad footprint before the F.Cu dogbone.
 old=(155.0,137.8) if name.endswith('_N') else (157.0,137.4)
 via(n,src)
 tr(n,xy(p('J7','128' if name.endswith('_N') else '130')),src,F)
 tr(n,src,old,B); tr(n,old,q,B)
 via(n,q); tr(n,q,xy(p('U12',pin)),F)
b.BuildListOfNets(); b.Save(str(R/a.output)); print(R/a.output)
