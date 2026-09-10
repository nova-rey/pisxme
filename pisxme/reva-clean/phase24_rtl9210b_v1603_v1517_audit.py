"""Native six-net audit for the V1517-support V1603 integration."""
from pathlib import Path
import pcbnew
P=Path(__file__).resolve().parent/'PHASE24_RTL9210B_PATHB_V1603_V1517_INTEGRATED.kicad_pcb'
S={'REFCLK_P':'61','REFCLK_N':'62','LANE0_RXP':'64','LANE0_RXN':'65','LANE0_TXN':'67','LANE0_TXP':'68'}
D={'REFCLK_P':'55','REFCLK_N':'53','LANE0_RXP':'43','LANE0_RXN':'41','LANE0_TXN':'47','LANE0_TXP':'49'}
def pad(b,r,n): return b.FindFootprintByReference(r).FindPadByNumber(n)
def join(b,a,z): b.BuildConnectivity(); return z in b.GetConnectivity().GetConnectedItems(a)
b=pcbnew.LoadBoard(str(P))
for net,sn in S.items():
 a,z=pad(b,'U1',sn),pad(b,'J1',D[net]); assert a.GetNetname()==net and z.GetNetname()==net and join(b,a,z),net
 b.BuildConnectivity(); v=next(x for x in b.GetConnectivity().GetConnectedItems(a) if isinstance(x,pcbnew.PCB_TRACK) and x.GetNetname()==net)
 n=pcbnew.LoadBoard(str(P)); nv=next(x for x in n.GetTracks() if x.GetNetname()==net and x.GetStart()==v.GetStart() and x.GetEnd()==v.GetEnd() and x.GetLayer()==v.GetLayer()); n.RemoveNative(nv)
 assert not join(n,pad(n,'U1',sn),pad(n,'J1',D[net])),net
print('V1603/V1517 integrated native six-net connectivity PASS; six negative controls PASS')
