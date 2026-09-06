"""Native connectivity audit for the obstacle-search LED probe."""
from pathlib import Path
import sys
import pcbnew

R = Path(__file__).resolve().parent
DEFAULT = R / "PHASE24_OFFICIAL_ETH_LED_ASTAR_PROBE.kicad_pcb"
EXPECTED = {
    'ETH_LEDY': ('J7.17', 'R30.1'),
    'ETH_LEDG': ('J7.15', 'R31.1'),
    '/ETHERNET/GBE_LED_Y_K': ('R30.2', 'J2.16'),
    '/ETHERNET/GBE_LED_G_K': ('R31.2', 'J2.18'),
}

def token(p): return p.GetParentFootprint().GetReference() + '.' + p.GetNumber()
def audit_board(b):
    b.BuildConnectivity(); c = b.GetConnectivity()
    pads = {token(p): p for f in b.GetFootprints() for p in f.Pads()}
    for net, members in EXPECTED.items():
        for member in members:
            assert member in pads, (net, member)
            assert pads[member].GetNetname() == net, (net, member, pads[member].GetNetname())
        for member in members:
            got = {token(x) for x in c.GetConnectedItems(pads[member]) if type(x).__name__ == 'PAD'} | {member}
            assert set(members) <= got, (net, member, sorted(got & set(members)))

def audit(path):
    b = pcbnew.LoadBoard(str(path)); audit_board(b); return b

def negative(path):
    b = audit(path)
    victim = next(x for x in b.GetTracks() if x.GetNetname() == 'ETH_LEDY')
    b.RemoveNative(victim); b.BuildConnectivity()
    try:
        audit_board(b)
    except AssertionError:
        return True
    raise AssertionError('negative control passed after removing an ETH_LEDY trace')

if __name__ == '__main__':
    p = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    audit(p); print('Phase24 LED native connectivity: PASS')
    print('negative_control_removed_real_LED_trace:', negative(p))
