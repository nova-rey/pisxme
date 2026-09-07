#!/usr/bin/env python3
"""Disposable full Path-B support placement: U2 + decoupling outboard."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL_V6.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_FULL_LATERAL_SUPPORT_PLACEMENT_V1.kicad_pcb'
def main():
 b=pcbnew.LoadBoard(str(BASE))
 for ref,dx in [('U2',35),('C3',20),('C4',20),('C5',20)]:
  f=next(x for x in b.GetFootprints() if x.GetReference()==ref)
  f.SetPos(f.GetPosition()+pcbnew.VECTOR2I_MM(dx,0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
