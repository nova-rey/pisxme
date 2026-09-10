"""Native CLKREQ_N endpoint and source-removal audit for V1347."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
PCB=H/'PHASE24_RTL9210B_CLKREQ_OVERPASS_V1347.kicad_pcb'
def pads(b): return {(f.GetReference(),str(p.GetNumber())):p for f in b.GetFootprints() for p in f.Pads()}
def ok(b):
    b.BuildConnectivity(); p=pads(b); c=b.GetConnectivity().GetConnectedItems(p[('U1','13')]); return all(p[k] in c for k in [('R3','1'),('J1','52')])
b=pcbnew.LoadBoard(str(PCB)); assert ok(b)
t=pcbnew.LoadBoard(str(PCB)); p=pads(t); victim=next(x for x in t.GetTracks() if x.GetNetname()=='CLKREQ_N' and not isinstance(x,pcbnew.PCB_VIA) and x.GetStart()==p[('U1','13')].GetPosition()); t.RemoveNative(victim); assert not ok(t)
print('PASS V1347 native CLKREQ U1.13-R3.1-J1.52 connectivity and source-removal negative control')
