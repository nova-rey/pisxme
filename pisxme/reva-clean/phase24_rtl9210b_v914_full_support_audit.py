"""Saved-board audit for V914 complete relocated RTL support."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;PCB=H/'PHASE24_RTL9210B_V888_V772_SPLIT_NO_DUPLICATE_V914.kicad_pcb'
GROUPS={'XTAL_IN':(('U1','53'),('Y1','1'),('C1','1')),'XTAL_OUT':(('U1','54'),('Y1','2'),('C2','1')),'RSET':(('U1','51'),('R1','1')),'GND':(('C1','2'),('C2','2'),('R1','2')),'RTL_3V3':(('U1','52'),('U1','39'),('U2','3'),('U2','8'),('C3','1'))}
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def key(p): return (p.GetParentFootprint().GetReference(),p.GetNumber())
def reach(b,p):
 b.BuildConnectivity();return {key(x) for x in b.GetConnectivity().GetConnectedItems(p) if type(x).__name__ in ('PAD','PCB_PAD')}
b=pcbnew.LoadBoard(str(PCB));ps=pads(b)
for net,ends in GROUPS.items():
 assert all(e in ps and ps[e].GetNetname()==net for e in ends)
 assert all(e in (reach(b,ps[ends[0]])|{ends[0]}) for e in ends)
print('V914 XTAL_IN/XTAL_OUT/RSET/GND/RTL_3V3 support: PASS')
for net,start,src,missing in [('XTAL_IN',(95.2,73.95),('U1','53'),('Y1','1')),('XTAL_OUT',(95.6,73.95),('U1','54'),('Y1','2'))]:
 b=pcbnew.LoadBoard(str(PCB));ps=pads(b);victim=next(x for x in b.GetTracks() if x.GetNetname()==net and x.GetStart()==pcbnew.VECTOR2I_MM(*start));b.RemoveNative(victim);assert missing not in (reach(b,ps[src])|{src});print(net+' source-trace negative control: PASS')
