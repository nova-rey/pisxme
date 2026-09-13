"""Bounded MPA producer: native F.Cu AUTO_PEDET J3.69 to J8.2.
Only this required control net is edited; no placement, rules, or other copper.
"""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
base=R/'PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb'
out=R/'validation-receipts/mpa-autopedet-corridor-producer-20260913/AUTO_PEDET_CORRIDOR_CANDIDATE.kicad_pcb'
out.parent.mkdir(parents=True,exist_ok=True)
b=pcbnew.LoadBoard(str(base))
if b is None: raise SystemExit('board load failed')
net=b.FindNet('AUTO_PEDET')
if net is None: raise SystemExit('AUTO_PEDET net missing')
def pad(ref,num):
 fp=b.FindFootprintByReference(ref)
 if fp is None: raise SystemExit('missing '+ref)
 p=fp.FindPadByNumber(str(num))
 if p is None: raise SystemExit(f'missing {ref}.{num}')
 return p
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(ref,num):
 p=pad(ref,num).GetPosition(); return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def tr(a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(pcbnew.F_Cu); t.SetWidth(pcbnew.FromMM(0.20)); t.SetNet(net); t.SetNetCode(net.GetNetCode()); b.Add(t)
s=xy('J3',69); d=xy('J8',2)
# MPA-authorized dedicated east/lower control corridor, using exact native pads.
way=[s,(227.75,157.5),(255.0,157.5),d]
for a,z in zip(way,way[1:]): tr(a,z)
b.Save(str(out))
print('saved',out)
print('source_pad',s,'dest_pad',d,'segments',len(way)-1,'width_mm',.2,'layer','F.Cu')
