"""Saved-board audit for the complete clean-field RTL_1V1 fanout."""
from pathlib import Path
import pcbnew
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_V927_RTL1V1_CLEANFIELD_V930.kicad_pcb'; GROUP=[('U1',n) for n in ('16','25','36','40','50','55','60','63')]+[('C4','1')]
def pads(b):return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def connected(b,group):
 b.BuildConnectivity();p=pads(b);return all(p[x] in b.GetConnectivity().GetConnectedItems(p[group[0]]) for x in group[1:])
b=pcbnew.LoadBoard(str(PCB));assert connected(b,GROUP);print('V930 complete RTL_1V1 fanout: PASS')
t=pcbnew.LoadBoard(str(PCB));p=pads(t);victim=next(x for x in t.GetTracks() if x.GetNetname()=='RTL_1V1' and x.GetStart()==p[('U1','36')].GetPosition());t.RemoveNative(victim);assert not connected(t,GROUP);print('V930 source-trace negative control: PASS')
