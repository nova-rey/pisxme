"""V558: re-emit the V546 primitive at the production 0.2 mm track width."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_QFN_COALLOCATE_V546.kicad_pcb';out=H/'PHASE24_RTL9210B_QFN_COALLOCATE_V558_STRICT.kicad_pcb'
old=pcbnew.FromMM(.13208);new=pcbnew.FromMM(.2)
b=pcbnew.LoadBoard(str(src));changed=0
for t in b.GetTracks():
 if t.GetWidth()==old:
  t.SetWidth(new);changed+=1
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out,'tracks widened',changed)
