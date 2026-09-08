"""Native V516 connectivity audit with trace-removal negative control."""
import pcbnew
from pathlib import Path
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_QFN_COALLOCATE_V516.kicad_pcb'; G=[('U1','16'),('U1','25'),('U1','36'),('C4','1')]
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def reach(b,src,target):
 b.BuildConnectivity(); c=b.GetConnectivity()
 def key(x):
  if hasattr(x,'GetUuid'):
   try: return ('u',x.GetUuid().AsString())
   except Exception: pass
  if hasattr(x,'GetPosition'):
   p=x.GetPosition(); return (type(x).__name__,p.x,p.y,getattr(x,'GetNetCode',lambda:0)())
  return (type(x).__name__,id(x))
 seen={key(src)}; todo=[src]
 while todo:
  for x in c.GetConnectedItems(todo.pop()):
   if key(x) not in seen: seen.add(key(x)); todo.append(x)
 return key(target) in seen
b=pcbnew.LoadBoard(str(PCB)); q=pads(b); assert all(reach(b,q[G[0]],q[x]) for x in G[1:]); print('PASS V516 native U1.16/U1.25/U1.36 -> C4.1 RTL_1V1 connectivity')
t=pcbnew.LoadBoard(str(PCB)); vs=[x for x in t.GetTracks() if x.GetNetname()=='RTL_1V1' and not isinstance(x,pcbnew.PCB_VIA)]; assert vs; t.RemoveNative(vs[-1]); q=pads(t); assert not reach(t,q[G[0]],q['U1','25']); print('PASS V516 U1.25-branch trace-removal negative control')
