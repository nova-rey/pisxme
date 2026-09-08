"""V529 native source-field connectivity and exact U1.39 branch control."""
import pcbnew
from pathlib import Path
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_QFN_COALLOCATE_V529.kicad_pcb'
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
print('PASS V529 native U1.20/U1.34/U1.39 -> C3.1 RTL_3V3 connectivity')
t=pcbnew.LoadBoard(str(PCB)); branch=[]
for x in t.GetTracks():
 if x.GetNetname()!='RTL_3V3' or isinstance(x,pcbnew.PCB_VIA): continue
 a=x.GetStart(); z=x.GetEnd(); aa=(round(a.x/1e6,4),round(a.y/1e6,4)); zz=(round(z.x/1e6,4),round(z.y/1e6,4))
 if (aa,zz) in [((100.5,60.4),(100.0,58.05)),((100.0,58.05),(100.0,55.8)),((100.0,55.8),(102.8,55.8))]: branch.append(x)
assert branch, 'new U1.39 local branch not found'
for x in branch:t.RemoveNative(x)
q=pads(t); assert not reach(t,q['U1','39'],q['U1','20'])
print('PASS V529 exact U1.39 branch negative control')
