#!/usr/bin/env python3
"""Route JMS_AVDD33 to a rehomed local C80 decoupler."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_STORAGE_MKEY_USB3_VCCK_LOCAL_20260912.kicad_pcb'
OUT=R/'PHASE24_STORAGE_MKEY_USB3_AVDD33_REHOME_20260912.kicad_pcb'
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); c=b.FindFootprintByReference('C80'); n=b.FindNet('JMS_AVDD33')
if c is None or n is None: raise SystemExit('missing C80/AVDD33')
c.SetPosition(V(150,146))
def tr(a,z,l=pcbnew.F_Cu,w=.20):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(w)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
tr((142.2,138.6),(142.2,139.5),w=.15); tr((142.2,139.5),(146.5,139.5),w=.15); tr((146.5,139.5),(149.5,139.5),w=.15); tr((149.5,139.5),(149.5,146.0),w=.15)
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
