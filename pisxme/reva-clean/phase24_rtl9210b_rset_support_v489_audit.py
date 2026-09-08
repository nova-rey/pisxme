"""Native saved-board RSET audit and trace-removal negative control."""
import pcbnew
from pathlib import Path
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_RSET_SUPPORT_V489.kicad_pcb'
G=[('U1','51'),('R1','1')]
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def ok(b):
 b.BuildConnectivity();m=pads(b);c=b.GetConnectivity().GetConnectedItems(m[G[0]]);return all(m[x] in c for x in G[1:])
def main():
 b=pcbnew.LoadBoard(str(PCB));assert ok(b)
 t=pcbnew.LoadBoard(str(PCB));vs=[x for x in t.GetTracks() if x.GetNetname()=='RSET'];assert vs
 for x in vs:t.RemoveNative(x)
 assert not ok(t)
 print('PASS V489 native RSET connectivity; one trace-removal negative control PASS')
if __name__=='__main__':main()
