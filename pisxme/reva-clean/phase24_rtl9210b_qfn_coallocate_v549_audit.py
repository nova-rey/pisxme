"""V549 native bottom 1V1 connectivity and exact branch negative control."""
import pcbnew
from pathlib import Path
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_QFN_COALLOCATE_V549.kicad_pcb'
def pads(b):return{(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def key(x):
 if hasattr(x,'GetUuid'):
  try:return('u',x.GetUuid().AsString())
  except Exception:pass
 p=x.GetPosition();return(type(x).__name__,p.x,p.y,getattr(x,'GetNetCode',lambda:0)())
def reach(b,a,z):
 b.BuildConnectivity();c=b.GetConnectivity();s={key(a)};q=[a]
 while q:
  for x in c.GetConnectedItems(q.pop()):
   if key(x) not in s:s.add(key(x));q.append(x)
 return key(z) in s
b=pcbnew.LoadBoard(str(PCB));q=pads(b)
for n in ['55','60','63']:assert reach(b,q['U1',n],q['C4','1']),n
print('PASS V549 native U1.55/U1.60/U1.63 -> C4.1 RTL_1V1 connectivity')
t=pcbnew.LoadBoard(str(PCB));branch=[]
for x in t.GetTracks():
 if x.GetNetname()!='RTL_1V1':continue
 if isinstance(x,pcbnew.PCB_VIA):
  p=x.GetPosition();xy=(round(p.x/1e6,4),round(p.y/1e6,4))
  if xy in [(103.5,69.5),(105.5,69.5),(108.0,69.5)]:branch.append(x)
 else:
  a=x.GetStart();z=x.GetEnd();aa=(round(a.x/1e6,4),round(a.y/1e6,4));zz=(round(z.x/1e6,4),round(z.y/1e6,4))
  if aa[1]>=69.5 and zz[1]>=69.5:branch.append(x)
assert branch
for x in branch:t.RemoveNative(x)
q=pads(t);assert not reach(t,q['U1','60'],q['C4','1']);print('PASS V549 exact bottom-edge branch negative control')
