"""Native V364 coallocated RTL_1V1/RTL_3V3 audit with negative controls."""
import pcbnew
from pathlib import Path
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_1V1_3V3_COALLOCATE_V364.kicad_pcb'
G1=[('U1','16'),('U1','25'),('U1','36'),('U1','40'),('U1','50'),('U1','55'),('U1','60'),('U1','63'),('C4','1')]
G3=[('U1','20'),('U1','34'),('U1','39'),('U1','52'),('R2','2'),('R3','2'),('C3','1'),('U2','3'),('U2','8')]
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def connected(b,g):
 b.BuildConnectivity(); ps=pads(b); c=b.GetConnectivity().GetConnectedItems(ps[g[0]])
 return all(ps[x] in c for x in g[1:])
def main():
 b=pcbnew.LoadBoard(str(PCB)); assert connected(b,G1); assert connected(b,G3)
 t=pcbnew.LoadBoard(str(PCB)); victim=next(x for x in t.GetTracks() if x.GetNetname()=='RTL_1V1'); t.RemoveNative(victim); assert not connected(t,G1)
 q=pcbnew.LoadBoard(str(PCB)); victim=next(x for x in q.GetTracks() if x.GetNetname()=='RTL_3V3'); q.RemoveNative(victim); assert not connected(q,G3)
 print('PASS V364 native RTL_1V1 + RTL_3V3 coallocation; both trace-removal negative controls PASS')
if __name__=='__main__': main()
