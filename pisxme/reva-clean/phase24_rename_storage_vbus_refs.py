from pathlib import Path
p=Path(__file__).resolve().parent/'STORAGE.kicad_sch'
s=p.read_text()
for old,new in [('"Reference" "R25"','"Reference" "R32"'),('(reference "R25"','(reference "R32"'),('"Reference" "R26"','"Reference" "R33"'),('(reference "R26"','(reference "R33"')]:
    s=s.replace(old,new)
p.write_text(s)
print('renamed STORAGE VBUS divider refs R25/R26 -> R32/R33')
