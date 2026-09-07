"""Assert native U7/coupler/J3 SATA connectivity without synthetic edges."""
from pathlib import Path
import sys, pcbnew
ROOT=Path(__file__).resolve().parent
BOARD=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'PHASE24_STORAGE_NATIVE_ORACLE_TRANSPLANT.kicad_pcb'
ENDPOINTS={
 'BRIDGE_SATA_TX_P':('U7.57','C30.2'), 'BRIDGE_SATA_TX_N':('U7.56','C31.2'),
 'BRIDGE_SATA_RX_P':('U7.60','C32.2'), 'BRIDGE_SATA_RX_N':('U7.59','C33.2'),
 # Coupling capacitors terminate at HD3SS3412 Port B; Port A continues to J3.
 # A direct capacitor-to-socket bypass is explicitly rejected.
 'TUSB_SATA_TXP':('C30.1','U13.38'),
 'TUSB_SATA_TXN':('C31.1','U13.37'),
 'TUSB_SATA_RXP':('C32.1','U13.36'),
 'TUSB_SATA_RXN':('C33.1','U13.35'),
 'M2_SATA_A_P_PCIE_TXP0':('U13.2','J3.49'),
 'M2_SATA_A_N_PCIE_TXN0':('U13.3','J3.47'),
 'M2_SATA_B_P_PCIE_RXN0':('U13.6','J3.41'),
 'M2_SATA_B_N_PCIE_RXP0':('U13.7','J3.43'),
}
def tok(p): return f'{p.GetParentFootprint().GetReference()}.{p.GetNumber()}'
b=pcbnew.LoadBoard(str(BOARD))
if b is None: raise SystemExit(f'cannot load {BOARD}')
b.BuildConnectivity(); conn=b.GetConnectivity()
pads={tok(p):p for f in b.GetFootprints() for p in f.Pads()}
for net,ends in ENDPOINTS.items():
 for e in ends:
  if e not in pads: raise AssertionError(f'missing endpoint {e}')
  if pads[e].GetNetname() not in (net, '/STORAGE/'+net) and not pads[e].GetNetname().endswith('/'+net):
   raise AssertionError(f'wrong net {e}: {pads[e].GetNetname()}')
 for e in ends:
  reached={tok(x) for x in conn.GetConnectedItems(pads[e]) if type(x).__name__=='PAD'}|{e}
  if not set(ends)<=reached: raise AssertionError(f'{net} disconnected at {e}: {sorted(reached)}')
 print(f'{net}: PASS ({ends[0]} <-> {ends[1]})')
for cap, socket in (('C30.1','J3.49'),('C31.1','J3.47'),('C32.1','J3.41'),('C33.1','J3.43')):
 reached={tok(x) for x in conn.GetConnectedItems(pads[cap]) if type(x).__name__=='PAD'}
 if socket in reached:
  raise AssertionError(f'rejected direct SATA bypass remains: {cap} reaches {socket}')
print('SATA native endpoint connectivity: PASS')
