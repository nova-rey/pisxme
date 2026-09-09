"""Saved-board native audit for V940 RTL_5V."""
from pathlib import Path
import pcbnew
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_V939_RESTORE_5V_V940.kicad_pcb';E=[('U1','17'),('U1','33'),('C5','1')]
def pads(b):return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def key(p):return(p.GetParentFootprint().GetReference(),p.GetNumber())
def reach(b,p):
 b.BuildConnectivity();return{key(x) for x in b.GetConnectivity().GetConnectedItems(p) if type(x).__name__ in('PAD','PCB_PAD')}
b=pcbnew.LoadBoard(str(PCB));p=pads(b);assert all(p[e].GetNetname()=='RTL_5V' for e in E);assert all(e in reach(b,p[E[0]])|{E[0]} for e in E);print('V940 RTL_5V native connectivity: PASS')
t=pcbnew.LoadBoard(str(PCB));q=pads(t);dst=q[E[2]].GetPosition();victims=[x for x in t.GetTracks() if x.GetNetname()=='RTL_5V' and type(x).__name__=='PCB_TRACK' and (x.GetStart()==dst or x.GetEnd()==dst)];assert victims
for v in victims:t.RemoveNative(v)
assert E[2] not in reach(t,pads(t)[E[0]])|{E[0]};print('V940 RTL_5V source-trace negative control: PASS')
