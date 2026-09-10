"""Native PEDET endpoint and source-removal audit for V1340."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
PCB=H/'PHASE24_RTL9210B_PEDET_BCU_THEN_FCU_V1340.kicad_pcb'
def pads(b): return {(f.GetReference(),str(p.GetNumber())):p for f in b.GetFootprints() for p in f.Pads()}
def ok(b):
    b.BuildConnectivity(); p=pads(b); c=b.GetConnectivity().GetConnectedItems(p[('U1','8')]); return all(p[k] in c for k in [('R2','1'),('J1','69')])
b=pcbnew.LoadBoard(str(PCB)); assert ok(b)
t=pcbnew.LoadBoard(str(PCB)); p=pads(t); victim=next(x for x in t.GetTracks() if x.GetNetname()=='PEDET' and not isinstance(x,pcbnew.PCB_VIA) and x.GetStart()==p[('U1','8')].GetPosition()); t.RemoveNative(victim); assert not ok(t)
print('PASS V1340 native PEDET U1.8-R2.1-J1.69 connectivity and source-removal negative control')
