"""V336: move the crystal/support trio coherently before rerouting."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_COHERENT_REORIENT_V323.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_CRYSTAL_RELOCATED_V336.kicad_pcb'
def main():
 b=pcbnew.LoadBoard(str(BASE))
 for ref,dx,dy in [('Y1',11,-4),('C1',11,-4),('C2',11,-2)]:
  f=b.FindFootprintByReference(ref); f.SetPosition(f.GetPosition()+pcbnew.VECTOR2I_MM(dx,dy))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
