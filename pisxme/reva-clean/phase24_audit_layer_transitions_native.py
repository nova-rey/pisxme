"""Audit saved-board F.Cu/B.Cu transitions for a physical through-via."""
from pathlib import Path
import sys
import pcbnew
R=Path(__file__).resolve().parent
P=Path(sys.argv[1]) if len(sys.argv)>1 else R/'PHASE24_STORAGE_JMS583_CRYSTAL_VIAS_V23.kicad_pcb'
def mm(q): return (round(pcbnew.ToMM(q.x),4),round(pcbnew.ToMM(q.y),4))
b=pcbnew.LoadBoard(str(P)); vias={}
for v in b.GetTracks():
 if isinstance(v, pcbnew.PCB_VIA): vias.setdefault(mm(v.GetPosition()),set()).add(v.GetNetname())
ends={}
for t in b.GetTracks():
 if not isinstance(t, pcbnew.PCB_TRACK): continue
 for q in (t.GetStart(),t.GetEnd()):
  ends.setdefault((mm(q),t.GetLayerName()),set()).add(t.GetNetname())
out=[]
for (q,l),nets in sorted(ends.items()):
 other='B.Cu' if l=='F.Cu' else 'F.Cu' if l=='B.Cu' else None
 if other and (q,other) in ends and not (set(nets)|ends[(q,other)]) & vias.get(q,set()):
  out.append((q,sorted(nets|ends[(q,other)])))
print('board:',P.name)
print('physical vias:',len(vias))
print('layer transitions without via:',len(out))
for q,n in out: print(q,','.join(n))
