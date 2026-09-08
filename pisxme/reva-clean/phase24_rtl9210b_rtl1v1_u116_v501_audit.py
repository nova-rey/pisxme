"""Native V501 connectivity audit with a trace-removal negative control."""
import pcbnew
from pathlib import Path
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_RTL1V1_U116_V501.kicad_pcb'; G=[('U1','16'),('C4','1')]
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def ok(b):
 b.BuildConnectivity(); q=pads(b); return q[G[1]] in b.GetConnectivity().GetConnectedItems(q[G[0]])
b=pcbnew.LoadBoard(str(PCB)); assert ok(b); print('PASS V501 native U1.16 -> C4.1 RTL_1V1 connectivity')
t=pcbnew.LoadBoard(str(PCB)); vs=[x for x in t.GetTracks() if x.GetNetname()=='RTL_1V1' and not isinstance(x, pcbnew.PCB_VIA)]; assert vs; t.RemoveNative(vs[0]); assert not ok(t); print('PASS V501 trace-removal negative control')
