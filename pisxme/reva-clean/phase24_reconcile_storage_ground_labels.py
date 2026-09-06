"""Reconcile generated storage selector ground labels to the project rail."""
from pathlib import Path
p=Path(__file__).resolve().parent/'STORAGE.kicad_sch'
s=p.read_text()
s=s.replace('(label "GND"','(label "POWER_GND"')
p.write_text(s)
print('reconciled storage selector ground labels')
