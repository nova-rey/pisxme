"""Audit U7 pad net ownership against the native exported netlist contract."""
from pathlib import Path
import sys
import pcbnew

EXPECTED={
 '4':'/STORAGE/BRIDGE_RESET','21':'/STORAGE/BRIDGE_CFG',
 '24':'/STORAGE/BRIDGE_3V3','30':'/STORAGE/BRIDGE_3V3','31':'/STORAGE/BRIDGE_3V3',
 '41':'/STORAGE/BRIDGE_1V1','42':'/CORE_CM5/CM5_USB3_RX_N','43':'/CORE_CM5/CM5_USB3_RX_P',
 '45':'/CORE_CM5/CM5_USB3_TX_N','46':'/CORE_CM5/CM5_USB3_TX_P',
 '52':'/STORAGE/BRIDGE_XI','53':'/STORAGE/BRIDGE_VSSOSC','54':'/STORAGE/BRIDGE_XO',
 '56':'/STORAGE/BRIDGE_SATA_TX_N','57':'/STORAGE/BRIDGE_SATA_TX_P',
 '59':'/STORAGE/BRIDGE_SATA_RX_N','60':'/STORAGE/BRIDGE_SATA_RX_P'}
def audit(path):
 b=pcbnew.LoadBoard(str(path)); f=b.FindFootprintByReference('U7'); errors=[]
 for num,name in EXPECTED.items():
  p=next((p for p in f.Pads() if str(p.GetNumber())==num),None)
  if p is None: errors.append(f'missing U7.{num}')
  elif p.GetNetname()!=name: errors.append(f'U7.{num}: {p.GetNetname()!r} != {name!r}')
 if errors: raise AssertionError('; '.join(errors))
 return True
if __name__=='__main__':
 audit(Path(sys.argv[1])); print('Phase24 U7 pad-net authority: PASS')
