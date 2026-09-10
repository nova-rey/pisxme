"""Native saved-board connectivity audit for J7 USB3 to U12."""
from pathlib import Path
import sys
import pcbnew

ROOT = Path(__file__).resolve().parent
BOARD = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'PHASE24_STORAGE_USB3_SHIFTED_ESCAPE_V121.kicad_pcb'
ENDPOINTS = {
    'CM5_USB3_RX_N': ('J7.128', 'U12.16'),
    'CM5_USB3_RX_P': ('J7.130', 'U12.15'),
    'CM5_USB3_TX_N': ('J7.140', 'U12.12'),
    'CM5_USB3_TX_P': ('J7.142', 'U12.11'),
}


def token(pad):
    return f'{pad.GetParentFootprint().GetReference()}.{pad.GetNumber()}'


board = pcbnew.LoadBoard(str(BOARD))
if board is None: raise SystemExit(f'cannot load {BOARD}')
board.BuildConnectivity()
conn = board.GetConnectivity()
pads = {token(p): p for f in board.GetFootprints() for p in f.Pads()}
for net, members in ENDPOINTS.items():
    for member in members:
        pad = pads.get(member)
        if pad is None: raise AssertionError(f'missing endpoint {member}')
        if pad.GetNetname().rsplit('/', 1)[-1] != net:
            raise AssertionError(f'wrong net on {member}: {pad.GetNetname()}')
    for member in members:
        reached = {token(i) for i in conn.GetConnectedItems(pads[member])
                   if type(i).__name__ == 'PAD'}
        reached.add(member)
        if not set(members) <= reached:
            raise AssertionError(f'{net} disconnected at {member}: {sorted(reached)}')
    print(f'{net}: PASS ({members[0]} <-> {members[1]})')
print('USB3 native U12 endpoint connectivity: PASS')
