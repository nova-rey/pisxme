"""Native saved-board common RTL_5V rail audit and negative control."""
import pcbnew
from pathlib import Path
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_RTL5V_U133_JOIN_V494.kicad_pcb';G=[('U1','33'),('U1','17'),('C5','1')]
def m(b):return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def ok(b):
 b.BuildConnectivity();q=m(b);c=b.GetConnectivity().GetConnectedItems(q[G[0]]);return all(q[x] in c for x in G[1:])
def main():
 b=pcbnew.LoadBoard(str(PCB));assert ok(b)
 t=pcbnew.LoadBoard(str(PCB));vs=[x for x in t.GetTracks() if x.GetNetname()=='RTL_5V'];assert vs
 for x in vs:t.RemoveNative(x)
 assert not ok(t);print('PASS V494 native common RTL_5V connectivity; one trace-removal negative control PASS')
if __name__=='__main__':main()
