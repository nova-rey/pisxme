#!/usr/bin/env python3
"""Repair the inherited U14 STORAGE_3V3 track through STORAGE_SEL."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT/'PHASE24_STORAGE_MKEY_USB3_EAST_SUPPORT_V6_20260912.kicad_pcb'
OUT = ROOT/'PHASE24_STORAGE_MKEY_USB3_EAST_SUPPORT_V6_U14_REPAIR_20260912.kicad_pcb'
def mm(v): return v/1e6
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))

b=pcbnew.LoadBoard(str(BASE))
if b is None: raise SystemExit('cannot load base')
target=[]
for t in b.GetTracks():
    if t.GetNetname()!='STORAGE_3V3' or not hasattr(t,'GetStart'):
        continue
    a,z=t.GetStart(),t.GetEnd()
    if {round(mm(a.x),3),round(mm(z.x),3)}=={211.1} and {round(mm(a.y),3),round(mm(z.y),3)}=={149.05,152.05}:
        target.append(t)
if len(target)!=1: raise SystemExit(f'expected one U14 vertical track, found {len(target)}')
b.Remove(target[0])
n=b.FindNet('STORAGE_3V3')
def tr(a,z,w=.20):
    t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(pcbnew.F_Cu); t.SetWidth(pcbnew.FromMM(w)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
tr((211.1,149.05),(212.5,149.05),.20)
tr((212.5,149.05),(212.5,152.05),.20)
tr((212.5,152.05),(211.1,152.05),.20)
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
