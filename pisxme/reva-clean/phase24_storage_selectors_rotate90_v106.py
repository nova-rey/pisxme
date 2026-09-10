"""V106: disposable geometry probe; rotate both storage selectors 90 degrees."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE24_STORAGE_AUTHORITY_J3_VERTICAL_V94.kicad_pcb'; OUT=R/'PHASE24_STORAGE_SELECTORS_ROTATE90_V106.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE))
for ref in ('U12','U13'):
 f=next(x for x in b.GetFootprints() if x.GetReference()==ref); f.SetOrientationDegrees(f.GetOrientationDegrees()+90)
b.Save(str(OUT)); print(OUT)
