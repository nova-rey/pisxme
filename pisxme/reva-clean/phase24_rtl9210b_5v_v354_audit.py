"""Native RTL_5V field audit and trace-removal negative control."""
import pcbnew
from pathlib import Path
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_RTL5V_ROUTE_V354.kicad_pcb'
GROUP=[('U1','17'),('U1','33'),('C5','1')]
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def connected(b, group):
 ps=pads(b); root=ps[group[0]]; ci=b.GetConnectivity().GetConnectedItems(root)
 return all(ps[x] in ci for x in group[1:])
def main():
 b=pcbnew.LoadBoard(str(PCB)); b.BuildConnectivity(); assert connected(b,GROUP)
 t=pcbnew.LoadBoard(str(PCB)); victim=next(x for x in t.GetTracks() if x.GetNetname()=='RTL_5V'); t.RemoveNative(victim); t.BuildConnectivity()
 assert not connected(t,GROUP)
 print('PASS V354 native RTL_5V field; trace-removal negative control PASS')
if __name__=='__main__': main()
