"""Remove PCB-only legacy Ethernet CCT/RCT aliases from a parity candidate."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;BASE=R/'PHASE24_ALL_AUTHORITATIVE_PARTS.kicad_pcb';OUT=R/'PHASE24_NO_LEGACY_CT_ALIASES.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE))
for ref in ['CCT','CCT1','CCT2','CCT3','CCT4','RCT1','RCT2','RCT3','RCT4']:
 f=b.FindFootprintByReference(ref)
 if f is not None:b.Remove(f)
b.Save(str(OUT));print(OUT)
