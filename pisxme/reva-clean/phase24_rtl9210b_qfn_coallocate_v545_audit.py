"""V545 native U1.40 1V1 connectivity and exact branch negative control."""
import pcbnew
from pathlib import Path
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_QFN_COALLOCATE_V545.kicad_pcb'
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
b=pcbnew.LoadBoard(str(PCB));q=pads(b);assert reach(b,q['U1','40'],q['C4','1']);print('PASS V545 native U1.40 -> C4.1 RTL_1V1 connectivity')
t=pcbnew.LoadBoard(str(PCB));branch=[]
for x in t.GetTracks():
 if x.GetNetname()!='RTL_1V1' or isinstance(x,pcbnew.PCB_VIA):continue
 a=x.GetStart();z=x.GetEnd();aa=(round(a.x/1e6,4),round(a.y/1e6,4));zz=(round(z.x/1e6,4),round(z.y/1e6,4))
 if (aa,zz) in [((102.05,60.8),(101.0,60.8)),((101.0,60.8),(101.5,64.8)),((101.5,64.8),(101.5,57.3))]:branch.append(x)
assert branch
for x in branch:t.RemoveNative(x)
q=pads(t);assert not reach(t,q['U1','40'],q['C4','1']);print('PASS V545 exact U1.40 branch negative control')
