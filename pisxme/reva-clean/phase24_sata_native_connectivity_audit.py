"""Assert native U7/coupler/J3 SATA connectivity without synthetic edges."""
from pathlib import Path
import sys, pcbnew
ROOT=Path(__file__).resolve().parent
BOARD=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'PHASE24_STORAGE_NATIVE_ORACLE_TRANSPLANT.kicad_pcb'
ENDPOINTS={
 'BRIDGE_SATA_TX_P':('U7.57','C30.2'), 'BRIDGE_SATA_TX_N':('U7.56','C31.2'),
 'BRIDGE_SATA_RX_P':('U7.60','C32.2'), 'BRIDGE_SATA_RX_N':('U7.59','C33.2'),
 'SATA_M2_TX_P':('C30.1','J3.1'), 'SATA_M2_TX_N':('C31.1','J3.2'),
 'SATA_M2_RX_P':('C32.1','J3.3'), 'SATA_M2_RX_N':('C33.1','J3.4'),
}
def tok(p): return f'{p.GetParentFootprint().GetReference()}.{p.GetNumber()}'
b=pcbnew.LoadBoard(str(BOARD))
if b is None: raise SystemExit(f'cannot load {BOARD}')
b.BuildConnectivity(); conn=b.GetConnectivity()
pads={tok(p):p for f in b.GetFootprints() for p in f.Pads()}
for net,ends in ENDPOINTS.items():
 for e in ends:
  if e not in pads: raise AssertionError(f'missing endpoint {e}')
  if not pads[e].GetNetname().endswith('/'+net): raise AssertionError(f'wrong net {e}: {pads[e].GetNetname()}')
 for e in ends:
  reached={tok(x) for x in conn.GetConnectedItems(pads[e]) if type(x).__name__=='PAD'}|{e}
  if not set(ends)<=reached: raise AssertionError(f'{net} disconnected at {e}: {sorted(reached)}')
 print(f'{net}: PASS ({ends[0]} <-> {ends[1]})')
print('SATA native endpoint connectivity: PASS')
