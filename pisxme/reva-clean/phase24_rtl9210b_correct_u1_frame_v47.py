"""V47: normalize RTL9210B U1 footprint anchor while preserving pad geometry."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_3V3_PARTITIONED_V44.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CORRECT_U1_FRAME_V47.kicad_pcb'
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def main():
 b=pcbnew.LoadBoard(str(BASE));f=b.FindFootprintByReference('U1')
 coords={p.GetNumber():p.GetPosition() for p in f.Pads()}
 f.SetPosition(P(98.0,70.0))
 for p in f.Pads():p.SetPosition(coords[p.GetNumber()])
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
