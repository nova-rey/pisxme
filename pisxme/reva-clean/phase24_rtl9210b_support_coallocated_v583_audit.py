"""Native saved-board audit for V583 and independent rail negative controls."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; PCB=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V583_5V_UPPER_CLEARANCE.kicad_pcb'
def pads(b): return {(f.GetReference(),str(p.GetNumber())):p for f in b.GetFootprints() for p in f.Pads()}
def conn(b,g):
 b.BuildConnectivity(); q=pads(b); c=b.GetConnectivity().GetConnectedItems(q[g[0]])
 return all(q[x] in c for x in g[1:])
def main():
 g5=[('U1','17'),('U1','33'),('C5','1')]; g3=[('U1','20'),('U1','34'),('U1','39'),('U1','52'),('R2','2'),('R3','2'),('C3','1'),('U2','3'),('U2','8')]
 b=pcbnew.LoadBoard(str(PCB)); assert conn(b,g5); assert conn(b,g3)
 t=pcbnew.LoadBoard(str(PCB))
 for x in list(t.GetTracks()):
  if x.GetNetname() in ('RTL_5V','RTL_3V3'): t.RemoveNative(x)
 assert not conn(t,g5); assert not conn(t,g3)
 print('PASS V583 native 5V/3V3 endpoint connectivity; trace-removal negative controls PASS')
if __name__=='__main__': main()
