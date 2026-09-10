"""Native connectivity audit for the V1603 launch in the full Path-B board."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
PCB = H / "PHASE24_RTL9210B_PATHB_V1603_INTEGRATED.kicad_pcb"
SRC = {'REFCLK_P':'61','REFCLK_N':'62','LANE0_RXP':'64','LANE0_RXN':'65','LANE0_TXN':'67','LANE0_TXP':'68'}
DST = {'REFCLK_P':'55','REFCLK_N':'53','LANE0_RXP':'43','LANE0_RXN':'41','LANE0_TXN':'47','LANE0_TXP':'49'}

def pad(b, ref, num): return b.FindFootprintByReference(ref).FindPadByNumber(num)
def joined(b, a, z):
    b.BuildConnectivity()
    return z in b.GetConnectivity().GetConnectedItems(a)

b = pcbnew.LoadBoard(str(PCB))
for net, sn in SRC.items():
    a, z = pad(b,'U1',sn), pad(b,'J1',DST[net])
    assert a.GetNetname() == net and z.GetNetname() == net, net
    assert joined(b,a,z), f'missing integrated native connection: {net}'
    b.BuildConnectivity()
    victim = next(x for x in b.GetConnectivity().GetConnectedItems(a)
                  if isinstance(x, pcbnew.PCB_TRACK) and x.GetNetname() == net)
    n = pcbnew.LoadBoard(str(PCB))
    nv = next(x for x in n.GetTracks() if x.GetNetname() == net and
              x.GetStart() == victim.GetStart() and x.GetEnd() == victim.GetEnd() and
              x.GetLayer() == victim.GetLayer())
    n.RemoveNative(nv)
    assert not joined(n, pad(n,'U1',sn), pad(n,'J1',DST[net])), f'negative control failed: {net}'
print('V1603 integrated native six-net connectivity PASS; six negative controls PASS')
