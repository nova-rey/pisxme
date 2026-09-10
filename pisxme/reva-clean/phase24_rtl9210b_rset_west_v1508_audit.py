"""Native saved-board audit and negative control for V1508 RSET."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent; PCB=ROOT/'PHASE24_RTL9210B_RSET_WEST_V1508.kicad_pcb'
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
b=pcbnew.LoadBoard(str(PCB)); p=pads(b); b.BuildConnectivity(); c=b.GetConnectivity(); assert p[('R1','1')] in c.GetConnectedItems(p[('U1','51')]); assert p[('R1','2')].GetNetname()=='GND'; print('V1508 native RSET pad connectivity: PASS')
# Removing the B.Cu segment between the two RSET layers must break the source
# to resistor connection; expected assertions never create graph edges.
t=pcbnew.LoadBoard(str(PCB)); q=pads(t); seg=next(x for x in t.GetTracks() if type(x).__name__=='PCB_TRACK' and x.GetNetname()=='RSET' and x.GetLayer()==pcbnew.B_Cu); t.RemoveNative(seg); t.BuildConnectivity(); assert q[('R1','1')] not in t.GetConnectivity().GetConnectedItems(q[('U1','51')]); print('removed RSET transition negative control: PASS')
