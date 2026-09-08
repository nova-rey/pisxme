"""V530 native three-source 3V3 connectivity and branch negative controls."""
import pcbnew
from pathlib import Path
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_QFN_COALLOCATE_V530.kicad_pcb'
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
print('PASS V530 native U1.20/U1.34/U1.39 -> relocated C3.1 connectivity')
for target,coords in [('U1.34',[((102.8,58.05),(102.8,55.8)),((102.8,55.8),(102.8,56.0))]),('U1.39',[((102.05,60.4),(100.5,60.4)),((100.5,60.4),(100.5,56.0))])]:
 t=pcbnew.LoadBoard(str(PCB)); removed=[]
 for x in t.GetTracks():
  if x.GetNetname()!='RTL_3V3' or isinstance(x,pcbnew.PCB_VIA): continue
  a=x.GetStart();z=x.GetEnd(); aa=(round(a.x/1e6,4),round(a.y/1e6,4));zz=(round(z.x/1e6,4),round(z.y/1e6,4))
  if (aa,zz) in coords: removed.append(x)
 assert removed, target
 for x in removed:t.RemoveNative(x)
 q=pads(t); assert not reach(t,q['U1',target.split('.')[0] if False else '20'],q['U1','34' if target=='U1.34' else '39'])
 print('PASS V530 exact '+target+' branch negative control')
