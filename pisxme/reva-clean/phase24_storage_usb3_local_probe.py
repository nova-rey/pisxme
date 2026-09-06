"""Disposable storage island directly adjacent to the native CM5 USB3 launch."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE.kicad_pcb';OUT=R/'PHASE24_STORAGE_USB3_LOCAL_COHERENT.kicad_pcb'
MOVES={
 'U7':(88,105,180),'J3':(150,105,90),
 'C30':(95,97,180),'C31':(95,113,180),'C32':(101,101,180),'C33':(101,109,180),
 'Y1':(80,118,0),'R23':(74,118,0),'C42':(74,114,0),'C43':(74,122,0),
 'C16':(87,93,0),'C17':(93,93,0),'C19':(99,93,0),
}
b=pcbnew.LoadBoard(str(BASE))
# Capture old pad locations so the placement probe can discard every stale
# endpoint attached to a moved footprint, including unrelated support nets.
old_pads=[]
for ref in MOVES:
 f=b.FindFootprintByReference(ref)
 for p in f.Pads():
  q=p.GetPosition(); old_pads.append((q.x,q.y))
for ref,(x,y,r) in MOVES.items():
 f=b.FindFootprintByReference(ref)
 if f is None:raise RuntimeError('missing '+ref)
 f.SetPosition(pcbnew.VECTOR2I_MM(x,y));f.SetOrientationDegrees(r)
for t in list(b.GetTracks()):
 if any(k in t.GetNetname() for k in ('CM5_USB3_','BRIDGE_SATA_','SATA_M2_','BRIDGE_XI','BRIDGE_XO','BRIDGE_VSSOSC')):
  b.Remove(t); continue
 endpoints=[]
 if isinstance(t,pcbnew.PCB_VIA): endpoints=[t.GetPosition()]
 else: endpoints=[t.GetStart(),t.GetEnd()]
 if any(min((q.x-p[0])**2+(q.y-p[1])**2 for p in old_pads) <= pcbnew.FromMM(.03)**2 for q in endpoints):
  b.Remove(t)
b.Save(str(OUT));print(OUT)
