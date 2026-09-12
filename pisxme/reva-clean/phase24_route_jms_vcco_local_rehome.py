#!/usr/bin/env python3
"""Route JMS_VCCO to a rehomed local C81 decoupler."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_STORAGE_MKEY_USB3_VCCK_LOCAL_20260912.kicad_pcb'
OUT=R/'PHASE24_STORAGE_MKEY_USB3_VCCO_REHOME_20260912.kicad_pcb'
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); c=b.FindFootprintByReference('C81'); n=b.FindNet('JMS_VCCO')
if c is None or n is None: raise SystemExit('missing C81/VCCO')
c.SetPosition(V(150,148))
def tr(a,z,w=.20):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(pcbnew.F_Cu); t.SetWidth(pcbnew.FromMM(w)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
tr((136.35,134.0),(134.5,134.0),.15); tr((134.5,134.0),(134.5,145.0),.15); tr((134.5,145.0),(149.5,145.0),.15); tr((149.5,145.0),(149.5,148.0),.15)
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
