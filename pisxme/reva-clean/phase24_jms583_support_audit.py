"""Fail-closed structural audit for the JMS583 required support network."""
from pathlib import Path
import re
import argparse

ROOT=Path(__file__).resolve().parent
REQUIRED={
 'R80':'12k 1%', 'L10':'4.7uH', 'Y10':'25MHz +/-30ppm',
 'C80':'4.7uF', 'C81':'100n', 'C82':'100n', 'C83':'100n', 'C84':'100n',
 'R81':'10k reset pullup', 'C85':'100n reset delay',
 'R82':'100k VBUS top', 'R83':'100k VBUS bottom',
 'C86':'100n USB TX1P', 'C87':'100n USB TX1N',
 'C90':'220n PCIe TX0P', 'C91':'220n PCIe TX0N',
 'C92':'220n PCIe TX1P', 'C93':'220n PCIe TX1N'}
NETS=('JMS_REXT','JMS_LXO','JMS_VDDREG_5V','JMS_XIN','JMS_XOUT',
      'JMS_AVDD33','JMS_VCCO','JMS_VCCK','JMS_AVDDL','JMS_XAVDDH',
      'JMS_RESET_N','STORAGE_3V3','VBUS','JMS_VBUS_SENSE',
      'JMS_USB3_TXP','JMS_USB3_TXN','JMS_PCIE_TXP0','JMS_PCIE_TXN0',
      'JMS_PCIE_TXP1','JMS_PCIE_TXN1')
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('input',nargs='?',default='STORAGE.kicad_sch'); args=ap.parse_args()
 s=Path(args.input).read_text(); failures=[]
 for ref,val in REQUIRED.items():
  block=re.search(r'\(symbol \(lib_id "PiSXMeRevAClean:STORAGE_(?:PASSIVE_2|CRYSTAL_4)".*?\(property "Reference" "'+ref+r'".*?\(property "Value" "([^"]+)"',s,re.S)
  if not block: failures.append('missing support instance '+ref)
  elif block.group(1)!=val: failures.append(f'{ref} value mismatch: {block.group(1)!r}')
 for net in NETS:
  if f'(label "{net}"' not in s: failures.append('missing support net label '+net)
 if failures:
  for x in failures: print('FAIL',x)
  raise SystemExit(1)
 print('PASS JMS583 required support network authority')
if __name__=='__main__': main()
