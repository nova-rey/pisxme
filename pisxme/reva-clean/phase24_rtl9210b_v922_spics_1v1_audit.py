"""Saved-board audit for V922 U1.25 RTL_1V1 and regenerated SPICS."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;PCB=H/'PHASE24_RTL9210B_V920_SPICS_REGEN_V922.kicad_pcb'
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def key(p): return (p.GetParentFootprint().GetReference(),p.GetNumber())
def reach(b,p): b.BuildConnectivity();return {key(x) for x in b.GetConnectivity().GetConnectedItems(p) if type(x).__name__ in ('PAD','PCB_PAD')}
b=pcbnew.LoadBoard(str(PCB));ps=pads(b)
for net,ends in [('RTL_1V1',(('U1','25'),('C4','1'))),('SPICS',(('U1','24'),('U2','1')))]:
 assert all(e in ps and ps[e].GetNetname()==net for e in ends)
 assert all(e in (reach(b,ps[ends[0]])|{ends[0]}) for e in ends)
print('V922 U1.25 RTL_1V1->C4 and SPICS U1.24->U2.1: PASS')
b=pcbnew.LoadBoard(str(PCB));ps=pads(b);victim=next(x for x in b.GetTracks() if x.GetNetname()=='SPICS' and x.GetStart()==pcbnew.VECTOR2I_MM(98.8,66.05));b.RemoveNative(victim)
assert ('U2','1') not in (reach(b,ps[('U1','24')])|{('U1','24')})
print('V922 SPICS source-trace negative control: PASS')
