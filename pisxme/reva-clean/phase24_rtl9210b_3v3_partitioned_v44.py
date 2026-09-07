"""V44: remove the redundant same-layer 3V3 transition from V43."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_3V3_PARTITIONED_V43.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_3V3_PARTITIONED_V44.kicad_pcb'
def main():
 b=pcbnew.LoadBoard(str(BASE))
 for x in list(b.GetTracks()):
  if x.GetNetname()=='RTL_3V3' and type(x).__name__=='PCB_VIA':
   p=x.GetPosition()
   if abs(p.x/1e6-90.5)<.001 and abs(p.y/1e6-74.5)<.001:b.RemoveNative(x)
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
