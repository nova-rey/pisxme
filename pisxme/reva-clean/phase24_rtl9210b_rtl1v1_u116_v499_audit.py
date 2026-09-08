"""Native saved-board RTL_1V1 U1.16/C4 audit and negative control."""
import pcbnew
from pathlib import Path
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_RTL1V1_U116_V499.kicad_pcb';G=[('U1','16'),('C4','1')]
def m(b):return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def ok(b):
 b.BuildConnectivity();q=m(b);c=b.GetConnectivity().GetConnectedItems(q[G[0]]);return q[G[1]] in c
def main():
 b=pcbnew.LoadBoard(str(PCB));assert ok(b)
 t=pcbnew.LoadBoard(str(PCB));vs=[x for x in t.GetTracks() if x.GetNetname()=='RTL_1V1'];assert vs
 for x in vs:t.RemoveNative(x)
 assert not ok(t);print('PASS V499 native U1.16-to-C4.1 connectivity; one trace-removal negative control PASS')
if __name__=='__main__':main()
