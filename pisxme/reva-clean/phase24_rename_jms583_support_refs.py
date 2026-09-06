"""Move JMS583 support references out of inherited acreage reference space."""
from pathlib import Path
import re
from phase3_scaffold import balanced

SCH=Path(__file__).resolve().parent/'STORAGE.kicad_sch'
MAP={'R34':'R80','R35':'R81','R36':'R82','R37':'R83','L2':'L10','Y2':'Y10',**{f'C{i}':f'C{80+i-44}' for i in range(44,58)}}
def main():
 s=SCH.read_text()
 for old,new in MAP.items():
  # Restrict replacements to the support component symbols/instances and
  # their instance paths; the storage child has no other use of these refs.
  s=s.replace(f'property "Reference" "{old}"',f'property "Reference" "{new}"')
  s=s.replace(f'(reference "{old}")',f'(reference "{new}")')
 SCH.write_text(s); print('renamed JMS583 support refs:',', '.join(f'{a}->{b}' for a,b in MAP.items()))
if __name__=='__main__': main()
