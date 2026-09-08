"""Native V360 1V1-first co-allocation audit and trace-removal negative control."""
import pcbnew
from pathlib import Path
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_RTL1V1_COALLOCATE_V360.kicad_pcb'
GROUP=[('U1','16'),('U1','25'),('U1','36'),('U1','40'),('U1','50'),('U1','55'),('U1','60'),('U1','63'),('C4','1')]
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def ok(b):
 b.BuildConnectivity(); ps=pads(b); ci=b.GetConnectivity().GetConnectedItems(ps[GROUP[0]])
 return all(ps[x] in ci for x in GROUP[1:])
def main():
 b=pcbnew.LoadBoard(str(PCB)); assert ok(b)
 t=pcbnew.LoadBoard(str(PCB)); victim=next(x for x in t.GetTracks() if x.GetNetname()=='RTL_1V1'); t.RemoveNative(victim); assert not ok(t)
 print('PASS V360 native RTL_1V1 co-allocation; trace-removal negative control PASS')
if __name__=='__main__': main()
