"""V83: diagnostic only; shrink perimeter pad width in V79, no copper/rule changes."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_REALLOCATE_3V3_U140_V79.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_QFN_PADWIDTH_DIAG_V83.kicad_pcb'
def main():
 b=pcbnew.LoadBoard(str(BASE));u=b.FindFootprintByReference('U1')
 changed=[]
 for p in u.Pads():
  s=p.GetSize(); sx=s.x/1e6; sy=s.y/1e6
  if p.GetNumber()!='69' and (abs(sx-.2)<.001 or abs(sy-.2)<.001):
   if abs(sx-.2)<.001: p.SetSize(pcbnew.VECTOR2I_MM(.15,sy))
   else: p.SetSize(pcbnew.VECTOR2I_MM(sx,.15))
   changed.append(p.GetNumber())
 b.BuildListOfNets();b.Save(str(OUT));print(OUT, 'pads_shrunk=',len(changed))
if __name__=='__main__':main()
