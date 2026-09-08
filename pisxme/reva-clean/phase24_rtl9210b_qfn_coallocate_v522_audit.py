"""V522 native RTL_3V3 connectivity and exact branch negative control."""
import pcbnew
from pathlib import Path
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_QFN_COALLOCATE_V522.kicad_pcb'
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def key(x):
 if hasattr(x,'GetUuid'):
  try:return ('u',x.GetUuid().AsString())
  except Exception: pass
 p=x.GetPosition(); return (type(x).__name__,p.x,p.y,getattr(x,'GetNetCode',lambda:0)())
def reach(b,a,z):
 b.BuildConnectivity(); c=b.GetConnectivity(); seen={key(a)}; todo=[a]
 while todo:
  for x in c.GetConnectedItems(todo.pop()):
   if key(x) not in seen: seen.add(key(x)); todo.append(x)
 return key(z) in seen
b=pcbnew.LoadBoard(str(PCB)); q=pads(b)
for x in [('U1','20'),('U1','34'),('U1','39'),('C3','1')]: assert reach(b,q['U1','20'],q[x]), x
print('PASS V522 native U1.20/U1.34/U1.39 -> C3.1 RTL_3V3 connectivity')
t=pcbnew.LoadBoard(str(PCB)); branch=[]
for x in t.GetTracks():
 if x.GetNetname()!='RTL_3V3': continue
 if isinstance(x,pcbnew.PCB_VIA):
  p=x.GetPosition(); xy=(round(p.x/1e6,4),round(p.y/1e6,4))
  if xy in [(101.3,58.05),(101.3,60.4)]: branch.append(x)
 else:
  a=x.GetStart(); z=x.GetEnd(); aa=(round(a.x/1e6,4),round(a.y/1e6,4)); zz=(round(z.x/1e6,4),round(z.y/1e6,4))
  if (aa,zz) in [((102.8,58.05),(101.3,58.05)),((101.3,58.05),(101.3,60.4)),((101.3,60.4),(102.05,60.4))]: branch.append(x)
assert branch, 'new U1.34 branch not found'
for x in branch:t.RemoveNative(x)
q=pads(t); assert not reach(t,q['U1','34'],q['U1','20'])
print('PASS V522 exact U1.34 branch negative control')
