"""Route source-owned J8 mode control on a disposable regenerated board."""
from pathlib import Path
import argparse, pcbnew
ap=argparse.ArgumentParser(); ap.add_argument('base'); ap.add_argument('output'); a=ap.parse_args()
R=Path(__file__).resolve().parent; b=pcbnew.LoadBoard(str(R/a.base)); F=pcbnew.F_Cu
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def xy(ref,num):
 p=b.FindFootprintByReference(ref).FindPadByNumber(str(num)).GetPosition(); return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def tr(n,p,q):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*p)); t.SetEnd(V(*q)); t.SetLayer(F); t.SetWidth(pcbnew.FromMM(.15)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
for name in ('AUTO_PEDET','MODE_IN'):
 n=b.FindNet(name)
 for t in list(b.GetTracks()):
  if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
tr(b.FindNet('AUTO_PEDET'),xy('J3',69),(227.75,157.5))
tr(b.FindNet('AUTO_PEDET'),(227.75,157.5),(255.0,157.5))
tr(b.FindNet('AUTO_PEDET'),(255.0,157.5),xy('J8',2))
tr(b.FindNet('MODE_IN'),xy('J8',4),(264.0,166.27))
tr(b.FindNet('MODE_IN'),(264.0,166.27),(264.0,158.0))
tr(b.FindNet('MODE_IN'),(264.0,158.0),xy('U14',2))
b.BuildListOfNets(); b.Save(str(R/a.output)); print(R/a.output)
