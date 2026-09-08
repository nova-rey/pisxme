"""Native V520 audit with stable graph identity and negative controls."""
import pcbnew
from pathlib import Path
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_QFN_COALLOCATE_V520.kicad_pcb'; GROUPS={'RTL_1V1':[('U1','16'),('U1','25'),('U1','36'),('C4','1')],'XTAL_IN':[('U1','53'),('Y1','1'),('C1','1')]}
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def key(x):
 if hasattr(x,'GetUuid'):
  try:return ('u',x.GetUuid().AsString())
  except Exception:pass
 p=x.GetPosition(); return (type(x).__name__,p.x,p.y,getattr(x,'GetNetCode',lambda:0)())
def reach(b,a,z):
 b.BuildConnectivity(); c=b.GetConnectivity(); seen={key(a)}; todo=[a]
 while todo:
  for x in c.GetConnectedItems(todo.pop()):
   if key(x) not in seen:seen.add(key(x));todo.append(x)
 return key(z) in seen
def ok(b,g):
 q=pads(b); return all(reach(b,q[g[0]],q[x]) for x in g[1:])
b=pcbnew.LoadBoard(str(PCB)); assert all(ok(b,g) for g in GROUPS.values()); print('PASS V520 native 1V1 + XTAL_IN support')
for name,g in GROUPS.items():
 t=pcbnew.LoadBoard(str(PCB)); vs=[x for x in t.GetTracks() if x.GetNetname()==name and not isinstance(x,pcbnew.PCB_VIA)]; assert vs
 for x in vs:t.RemoveNative(x)
 q=pads(t); assert not ok(t,g); print('PASS V520',name,'trace-removal negative control')
