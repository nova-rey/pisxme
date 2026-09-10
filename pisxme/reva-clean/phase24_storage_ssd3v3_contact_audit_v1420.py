"""Native saved-board audit for the V1420 SSD_3V3 contact join."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; PCB=H/'PHASE24_STORAGE_SSD3V3_CONTACT_JOIN_V1420.kicad_pcb'
def pads(b): return {(f.GetReference(),str(p.GetNumber())):p for f in b.GetFootprints() for p in f.Pads()}
def key(p): return (p.GetParentFootprint().GetReference(),str(p.GetNumber()))
def reach(b,p):
 b.BuildConnectivity(); return {key(x) for x in b.GetConnectivity().GetConnectedItems(p) if hasattr(x,'GetParentFootprint') and x.GetParentFootprint() is not None}|{key(p)}
expected={('J1',str(n)) for n in (2,4,6,8)}
b=pcbnew.LoadBoard(str(PCB)); p=pads(b); assert expected<=reach(b,p[('J1','2')])
t=pcbnew.LoadBoard(str(PCB)); q=pads(t); v=next(x for x in t.GetTracks() if x.GetNetname()=='SSD_3V3' and not isinstance(x,pcbnew.PCB_VIA) and x.GetStart()==q[('J1','2')].GetPosition()); t.RemoveNative(v); assert ('J1','4') not in reach(t,pads(t)[('J1','2')])
print('PASS V1420 J1 SSD_3V3 pads 2/4/6/8 native connectivity and source-removal negative control')
