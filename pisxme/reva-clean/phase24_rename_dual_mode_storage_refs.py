"""Use unused project references for the new storage silicon."""
from pathlib import Path
p=Path(__file__).resolve().parent/'STORAGE.kicad_sch'; t=p.read_text()
for old,new in (('U8','U11'),('U9','U12'),('U10','U13')):
    t=t.replace(f'(property "Reference" "{old}"',f'(property "Reference" "{new}"')
    t=t.replace(f'(reference "{old}"',f'(reference "{new}"')
p.write_text(t); print('renamed dual-mode storage refs U11/U12/U13')
