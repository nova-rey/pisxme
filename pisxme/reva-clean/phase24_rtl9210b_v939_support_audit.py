"""Saved-board audit for V939 RTL_1V1 plus crystal support."""
from pathlib import Path
import pcbnew
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_V938_RESTORE_U155_V939.kicad_pcb';GROUP={'RTL_1V1':[('U1',n) for n in ('16','25','36','40','50','55','60','63')]+[('C4','1')],'XTAL_IN':[('U1','53'),('Y1','1'),('C1','1')],'XTAL_OUT':[('U1','54'),('Y1','2'),('C2','1')],'RSET':[('U1','51'),('R1','1')]}
def pads(b):return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def key(p):return (p.GetParentFootprint().GetReference(),p.GetNumber())
def reach(b,p):
 b.BuildConnectivity();return {key(x) for x in b.GetConnectivity().GetConnectedItems(p) if type(x).__name__ in ('PAD','PCB_PAD')}
b=pcbnew.LoadBoard(str(PCB));p=pads(b)
for net,ends in GROUP.items():
 assert all(p[e].GetNetname()==net for e in ends);assert all(e in reach(b,p[ends[0]])|{ends[0]} for e in ends)
print('V939 RTL_1V1/crystal/RSET native connectivity: PASS')
for net,ends in GROUP.items():
 t=pcbnew.LoadBoard(str(PCB));q=pads(t);v=next(x for x in t.GetTracks() if x.GetNetname()==net and type(x).__name__=='PCB_TRACK' and x.GetStart()==q[ends[0]].GetPosition());t.RemoveNative(v);assert ends[1] not in reach(t,pads(t)[ends[0]])|{ends[0]}
print('V939 four source-trace negative controls: PASS')
