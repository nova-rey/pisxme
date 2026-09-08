"""Native saved-board crystal connectivity audit and negative control."""
import pcbnew
from pathlib import Path
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_CRYSTAL_ROUTE_V339.kicad_pcb'
GROUPS={'XTAL_IN':[('U1','53'),('Y1','1'),('C1','1')],'XTAL_OUT':[('U1','54'),('Y1','2'),('C2','1')]}
def mp(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def check(b,group):
 b.BuildConnectivity(); ps=mp(b); root=ps[group[0]]
 return all(ps[x] in b.GetConnectivity().GetConnectedItems(root) for x in group[1:])
def main():
 b=pcbnew.LoadBoard(str(PCB)); assert all(check(b,g) for g in GROUPS.values())
 t=pcbnew.LoadBoard(str(PCB)); victim=next(x for x in t.GetTracks() if x.GetNetname()=='XTAL_IN'); t.RemoveNative(victim)
 assert not check(t,GROUPS['XTAL_IN'])
 print('PASS V339 native XTAL_IN/XTAL_OUT audit; trace-removal negative control PASS')
if __name__=='__main__':main()
