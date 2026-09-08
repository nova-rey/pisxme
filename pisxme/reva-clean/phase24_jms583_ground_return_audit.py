"""Audit native JMS583 support ground access and its negative control."""
from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent
PCB=R/'PHASE24_JMS583_SUPPORT_COHORT_GROUND_FILLED_V2.kicad_pcb'
NEG=R/'PHASE24_JMS583_SUPPORT_COHORT_GROUND_FILLED_V2_NEGATIVE.kicad_pcb'
SUPPORT=('C80','C81','C82','C83','C84','C85','R80','R83','Y10')

def ground_pads(b):
    out=[]
    for ref in SUPPORT:
        f=b.FindFootprintByReference(ref)
        out.extend((ref,p) for p in f.Pads() if p.GetNetname()=='POWER_GND')
    return out

def all_join(b, pads, target):
    b.BuildConnectivity()
    return all(target in b.GetConnectivity().GetConnectedItems(p) for _,p in pads)

b=pcbnew.LoadBoard(str(PCB)); u=b.FindFootprintByReference('U11'); target=u.FindPadByNumber('63')
pads=ground_pads(b)
if not pads or not all_join(b,pads,target): raise SystemExit('FAIL JMS583 support ground return connectivity')

for item in list(b.GetTracks()):
    p=item.GetPosition()
    x,y=pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
    if item.GetNetname()=='POWER_GND' and 115 <= x <= 160 and 110 <= y <= 155:
        b.RemoveNative(item)
b.BuildConnectivity()
if all_join(b,pads,target): raise SystemExit('FAIL JMS583 ground return negative control')
b.Save(str(NEG)); print('PASS JMS583 support ground returns; PASS local ground-removal negative control')
