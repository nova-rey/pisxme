"""Native saved-board RTL_5V U1.33/C5 audit and negative control."""
import pcbnew
from pathlib import Path
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_RTL5V_U133_V492.kicad_pcb';G=[('U1','33'),('C5','1')]
def m(b):return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def ok(b):
 b.BuildConnectivity();q=m(b);c=b.GetConnectivity().GetConnectedItems(q[G[0]]);return q[G[1]] in c
def main():
 b=pcbnew.LoadBoard(str(PCB));assert ok(b)
 t=pcbnew.LoadBoard(str(PCB));vs=[x for x in t.GetTracks() if x.GetNetname()=='RTL_5V'];assert vs
 for x in vs:t.RemoveNative(x)
 assert not ok(t);print('PASS V492 native U1.33-to-C5.1 connectivity; one trace-removal negative control PASS')
if __name__=='__main__':main()
