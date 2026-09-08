"""V337: clear C2 from the adjacent C4 ground pad."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_CRYSTAL_RELOCATED_V336.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_CRYSTAL_RELOCATED_V337.kicad_pcb'
def main():
 b=pcbnew.LoadBoard(str(BASE));f=b.FindFootprintByReference('C2');f.SetPosition(f.GetPosition()+pcbnew.VECTOR2I_MM(5,0));b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
