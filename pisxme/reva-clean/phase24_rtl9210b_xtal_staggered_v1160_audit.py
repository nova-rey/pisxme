"""Saved-board native XTAL connectivity audit and trace-removal controls."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
PCB=H/'PHASE24_RTL9210B_XTAL_STAGGERED_V1160.kicad_pcb'
GROUPS={'XTAL_IN':[('U1','53'),('Y1','1'),('C1','1')], 'XTAL_OUT':[('U1','54'),('Y1','2'),('C2','1')]}
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def connected(b,g):
    b.BuildConnectivity(); ps=pads(b); return all(ps[x] in b.GetConnectivity().GetConnectedItems(ps[g[0]]) for x in g[1:])
def main():
    b=pcbnew.LoadBoard(str(PCB)); result={k:connected(b,g) for k,g in GROUPS.items()}; assert result=={'XTAL_IN':True,'XTAL_OUT':True},result
    for name in GROUPS:
        t=pcbnew.LoadBoard(str(PCB)); victim=next(x for x in t.GetTracks() if x.GetNetname()==name and type(x).__name__!='PCB_VIA')
        t.RemoveNative(victim); assert not connected(t,GROUPS[name]),name
    print('PASS V1160 native XTAL_IN/XTAL_OUT connectivity; both source-trace negative controls PASS')
if __name__=='__main__': main()
