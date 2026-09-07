"""Assert native U7/coupler/J3 SATA connectivity without synthetic edges."""
from pathlib import Path
import sys, pcbnew
ROOT=Path(__file__).resolve().parent
BOARD=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'PHASE24_STORAGE_NATIVE_ORACLE_TRANSPLANT.kicad_pcb'
ENDPOINTS={
 'BRIDGE_SATA_TX_P':('U7.57','C30.2'), 'BRIDGE_SATA_TX_N':('U7.56','C31.2'),
 'BRIDGE_SATA_RX_P':('U7.60','C32.2'), 'BRIDGE_SATA_RX_N':('U7.59','C33.2'),
 # M.2 Socket 3 shared SATA/PCIe lane-0 contacts.  J3.1..4 are
 # configuration/power contacts on the native M-key footprint and are not
 # valid SATA endpoints.
 'M2_SATA_A_P_PCIE_TXP0':('C30.1','J3.49'),
 'M2_SATA_A_N_PCIE_TXN0':('C31.1','J3.47'),
 'M2_SATA_B_N_PCIE_RXP0':('C32.1','J3.43'),
 'M2_SATA_B_P_PCIE_RXN0':('C33.1','J3.41'),
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
print('SATA native endpoint connectivity: PASS')
