"""Create a disposable coherent storage-island placement candidate."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_CORRECTED_MACRO_PLACEMENT.kicad_pcb'
OUT=R/'PHASE24_STORAGE_ISLAND_COHERENT_U7_110_105.kicad_pcb'
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); u=b.FindFootprintByReference('U7')
old=(pcbnew.ToMM(u.GetPosition().x),pcbnew.ToMM(u.GetPosition().y)); new=(110.,105.)
dx,dy=new[0]-old[0],new[1]-old[1]
# Complete local storage support moves with U7; J3 remains the serviceable
# board-edge endpoint so the SATA corridor stays a distinct short launch.
refs=('U7','C16','C17','C19','C30','C31','C32','C33','Y1','R23','C42','C43')
for ref in refs:
 f=b.FindFootprintByReference(ref)
 if f is None: raise RuntimeError(f'missing {ref}')
 p=f.GetPosition(); f.SetPosition(V(p.x/1e6+dx,p.y/1e6+dy))
u.SetOrientationDegrees(180.)
affected=('CM5_USB3_','BRIDGE_SATA_','SATA_M2_','BRIDGE_XI','BRIDGE_XO','BRIDGE_VSSOSC')
for t in list(b.GetTracks()):
 if any(k in t.GetNetname() for k in affected): b.Remove(t)
b.BuildListOfNets();b.Save(str(OUT));print(OUT,'translation_mm',dx,dy)
