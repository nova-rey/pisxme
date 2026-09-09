"""Saved-board native audit for the relocated XTAL_IN primitive."""
from pathlib import Path
import pcbnew
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_V932_XTAL_IN_RELOCATE_V933.kicad_pcb'; END=[('U1','53'),('Y1','1'),('C1','1')]
def pads(b):return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def key(p):return (p.GetParentFootprint().GetReference(),p.GetNumber())
def reach(b,p):
 b.BuildConnectivity();return {key(x) for x in b.GetConnectivity().GetConnectedItems(p) if type(x).__name__ in ('PAD','PCB_PAD')}
b=pcbnew.LoadBoard(str(PCB));p=pads(b);assert all(p[e].GetNetname()=='XTAL_IN' for e in END);assert all(e in reach(b,p[END[0]])|{END[0]} for e in END);print('V933 XTAL_IN connectivity: PASS')
t=pcbnew.LoadBoard(str(PCB));q=pads(t);victim=next(x for x in t.GetTracks() if x.GetNetname()=='XTAL_IN' and x.GetStart()==q[END[0]].GetPosition());t.RemoveNative(victim);assert END[1] not in reach(t,pads(t)[END[0]])|{END[0]};print('V933 XTAL_IN source-trace negative control: PASS')
