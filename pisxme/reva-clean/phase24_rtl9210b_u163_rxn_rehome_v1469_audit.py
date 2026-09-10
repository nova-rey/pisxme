"""Native saved-board audit and negative controls for V1469."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
PCB=H/'PHASE24_RTL9210B_U163_RXN_REHOME_V1469.kicad_pcb'
def pad(b,r,p):
 f=b.FindFootprintByReference(r); assert f is not None
 q=f.FindPadByNumber(p); assert q is not None,(r,p); return q
def c(b,a,z):
 b.BuildConnectivity(); return pad(b,*z) in b.GetConnectivity().GetConnectedItems(pad(b,*a))
b=pcbnew.LoadBoard(str(PCB))
assert c(b,('U1','66'),('U1','69'))
for s,t in (('64','43'),('65','41'),('67','47'),('68','49')):
 assert c(b,('U1',s),('J1',t)),(s,t)
assert c(b,('U1','63'),('C4','1'))

def negative(name, net, start, end, assertion):
 q=pcbnew.LoadBoard(str(PCB)); victim=None
 for item in q.GetTracks():
  if item.GetNetname()==net and hasattr(item,'GetStart'):
   a=tuple(round(float(v)/1e6,3) for v in item.GetStart()); z=tuple(round(float(v)/1e6,3) for v in item.GetEnd())
   if {a,z}=={start,end}: victim=item; break
 assert victim is not None,(net,start,end)
 q.RemoveNative(victim); assert not assertion(q)
 q.Save(str(H/f'PHASE24_RTL9210B_U163_RXN_REHOME_V1469-negative-{name}.kicad_pcb'))
negative('rail','RTL_1V1',(94.05,71.2),(92.8,71.2),lambda q:c(q,('U1','63'),('C4','1')))
negative('rxn','LANE0_RXN',(94.05,72.0),(88.8,72.0),lambda q:c(q,('U1','65'),('J1','41')))
print('PASS V1469 native U1.66/U1.69, four lanes, and U1.63 RTL_1V1')
print('PASS V1469 saved-board rail and RXN trace-removal negative controls')
