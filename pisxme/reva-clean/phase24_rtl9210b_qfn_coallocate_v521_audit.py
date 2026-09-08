"""Native V521 connectivity audit with negative control."""
import pcbnew
from pathlib import Path
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_QFN_COALLOCATE_V521.kicad_pcb';G=[('U1','20'),('U1','34'),('C3','1')]
def pads(b):return{(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def key(x):
 if hasattr(x,'GetUuid'):
  try:return('u',x.GetUuid().AsString())
  except Exception:pass
 p=x.GetPosition();return(type(x).__name__,p.x,p.y,getattr(x,'GetNetCode',lambda:0)())
def reach(b,a,z):
 b.BuildConnectivity();c=b.GetConnectivity();seen={key(a)};todo=[a]
 while todo:
  for x in c.GetConnectedItems(todo.pop()):
   if key(x) not in seen:seen.add(key(x));todo.append(x)
 return key(z) in seen
b=pcbnew.LoadBoard(str(PCB));q=pads(b);assert all(reach(b,q[G[0]],q[x]) for x in G[1:]);print('PASS V521 native U1.20/U1.34 -> C3.1 RTL_3V3 connectivity')
t=pcbnew.LoadBoard(str(PCB));
# Remove the exact newly-authored U1.34 escape, rather than an arbitrary
# RTL_3V3 segment.  The latter can be redundant and makes a false negative
# control possible on a real saved-board graph.
branch=[]
for x in t.GetTracks():
 if x.GetNetname()!='RTL_3V3': continue
 if isinstance(x,pcbnew.PCB_VIA):
  p=x.GetPosition(); xy=(round(p.x/1e6,4),round(p.y/1e6,4))
  if xy==(102.8,57.0): branch.append(x)
 else:
  a=x.GetStart();z=x.GetEnd(); aa=(round(a.x/1e6,4),round(a.y/1e6,4)); zz=(round(z.x/1e6,4),round(z.y/1e6,4))
  if (aa,zz) in [((102.8,58.05),(102.8,57.0)),((102.8,57.0),(109.5,57.0)),((109.5,57.0),(109.5,57.2))]: branch.append(x)
assert branch, 'new U1.34 branch not found'
for x in branch:t.RemoveNative(x)
q=pads(t);assert not reach(t,q['U1','34'],q['U1','20']);print('PASS V521 exact U1.34-branch negative control')
