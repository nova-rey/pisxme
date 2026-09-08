"""Saved-board audit for V570; edges come only from KiCad connectivity."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; PCB=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V570_RTL5V_UPPER_LOOP.kicad_pcb'
def pads(b): return {(f.GetReference(),str(p.GetNumber())):p for f in b.GetFootprints() for p in f.Pads()}
def connected(b, group):
 b.BuildConnectivity(); q=pads(b); c=b.GetConnectivity().GetConnectedItems(q[group[0]])
 return all(q[x] in c for x in group[1:])
def main():
 b=pcbnew.LoadBoard(str(PCB)); assert connected(b,[('U1','17'),('U1','33'),('C5','1')])
 t=pcbnew.LoadBoard(str(PCB))
 for x in list(t.GetTracks()):
  if x.GetNetname()=='RTL_5V': t.RemoveNative(x)
 assert not connected(t,[('U1','17'),('U1','33'),('C5','1')])
 print('PASS V570 native RTL_5V source/decoupler connectivity; trace-removal negative control PASS')
if __name__=='__main__': main()
