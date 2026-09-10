"""Native audit and negative control for the V1517 U1.55 rail rehome."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent; PCB=ROOT/'PHASE24_RTL9210B_U155_REHOME_V1517.kicad_pcb'
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
b=pcbnew.LoadBoard(str(PCB)); p=pads(b); b.BuildConnectivity(); c=b.GetConnectivity(); assert p[('U1','55')] in c.GetConnectedItems(p[('U1','63')]); print('V1517 native U1.55 RTL_1V1 connectivity: PASS')
t=pcbnew.LoadBoard(str(PCB)); q=pads(t); seg=next(x for x in t.GetTracks() if type(x).__name__=='PCB_TRACK' and x.GetNetname()=='RTL_1V1' and x.GetLayer()==pcbnew.F_Cu and abs(x.GetStart()[0]/1e6-94.05)<.01 and abs(x.GetEnd()[0]/1e6-92.8)<.01); t.RemoveNative(seg); t.BuildConnectivity(); assert q[('U1','55')] not in t.GetConnectivity().GetConnectedItems(q[('U1','63')]); print('removed U1.55 source negative control: PASS')
