"""Native saved-board audit for the relocated crystal pocket."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; PCB=H/'PHASE24_RTL9210B_CRYSTAL_POCKET_RELOCATED_V1165.kicad_pcb'
GROUPS={'XTAL_IN':[('U1','53'),('Y1','1'),('C1','1')], 'XTAL_OUT':[('U1','54'),('Y1','2'),('C2','1')], 'GND':[('C1','2'),('C2','2')]}
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def conn(b,g):
 b.BuildConnectivity();p=pads(b);return all(p[x] in b.GetConnectivity().GetConnectedItems(p[g[0]]) for x in g[1:])
for name,g in GROUPS.items():
 b=pcbnew.LoadBoard(str(PCB));assert conn(b,g),name
 if name != 'GND':
  t=pcbnew.LoadBoard(str(PCB));pp=pads(t);targets=[pp[x].GetPosition() for x in g]
  v=next(x for x in t.GetTracks() if x.GetNetname()==name and type(x).__name__!='PCB_VIA' and (x.GetStart() in targets or x.GetEnd() in targets))
  t.RemoveNative(v);assert not conn(t,g),name
print('PASS V1165 relocated XTAL_IN/XTAL_OUT/GND connectivity; two crystal trace-removal negative controls PASS')
