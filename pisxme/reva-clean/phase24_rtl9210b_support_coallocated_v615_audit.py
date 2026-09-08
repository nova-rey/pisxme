"""Native saved-board audit for the V615 two-net SPI endpoint field."""
from pathlib import Path
import pcbnew
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V615_SPI_BOTTOM_CLEAR2.kicad_pcb'
GROUPS={'SPISI':[('U1','18'),('U2','5')],'SPISO3':[('U1','22'),('U2','7')]}
def pads(b):return {(f.GetReference(),str(p.GetNumber())):p for f in b.GetFootprints() for p in f.Pads()}
def connected(b,g):
 b.BuildConnectivity();q=pads(b);c=b.GetConnectivity().GetConnectedItems(q[g[0]])
 return all(q[x] in c for x in g[1:])
b=pcbnew.LoadBoard(str(PCB));assert all(connected(b,g) for g in GROUPS.values())
for name,g in GROUPS.items():
 t=pcbnew.LoadBoard(str(PCB));victims=[x for x in t.GetTracks() if x.GetNetname()==name];assert victims
 for x in victims:t.RemoveNative(x)
 assert not connected(t,g),name
print('PASS V615 native SPISI/SPISO3 connectivity; independent trace-removal negative controls PASS')
