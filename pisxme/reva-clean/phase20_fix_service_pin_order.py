"""Correct SERVICE label Y order for KiCad's generated symbol transforms."""
from pathlib import Path
import re
P=Path(__file__).resolve().parent/'SERVICE.kicad_sch'
def main():
 t=P.read_text()
 groups={
  'dd000000': [('SERVICE_USB2_DP',101.25),('SERVICE_USB2_DM',98.75),('SERVICE_VBUS_SENSE',96.25),('SERVICE_GND',93.75),('SERVICE_RD_A',91.25),('SERVICE_RD_B',88.75)],
  'de000000': [('SERVICE_USB2_DP',97.5),('SERVICE_USB2_DM',95.0),('SERVICE_GND',92.5)],
  'df000000': [('SERVICE_RD_A',111.25),('SERVICE_GND',108.75)],
  '0e000000': [('SERVICE_RD_B',111.25),('SERVICE_GND',108.75)],
 }
 for prefix,items in groups.items():
  for name,y in items:
   pat=rf'(\(label "{re.escape(name)}" \(at )[^ ]+ [^ ]+ (0\) .*?\(uuid {prefix}[0-9a-f-]+\)\))'
   x=50 if prefix=='dd000000' else (90 if prefix in ('de000000','0e000000') else 70)
   repl=rf'\g<1>{x:g} {y:g} \g<2>'
   t,n=re.subn(pat,repl,t,count=1)
   if n!=1: raise RuntimeError(f'missing {prefix} {name}')
 P.write_text(t); print('SERVICE label pin order corrected')
if __name__=='__main__':main()
