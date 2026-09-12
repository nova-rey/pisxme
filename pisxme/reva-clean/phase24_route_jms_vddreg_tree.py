#!/usr/bin/env python3
"""Connect the shared JMS VDDREG_5V rail on the current storage candidate."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_STORAGE_MKEY_USB3_EAST_SUPPORT_V6_U14_REPAIR_20260912.kicad_pcb'
OUT=R/'PHASE24_STORAGE_MKEY_USB3_VDDREG_TREE_20260912.kicad_pcb'
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('JMS_VDDREG_5V')
def tr(a,z,l=pcbnew.F_Cu):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(.20)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(p):
 v=pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
# One two-layer rail tree, with transitions outside all package pads.
tr((136.35,132.0),(132.5,132.0)); tr((132.5,132.0),(132.5,123.5),pcbnew.B_Cu); via((132.5,123.5)); tr((132.5,123.5),(137.15,123.5)); tr((137.15,123.5),(137.15,125.0))
tr((163.5,131.8),(157.0,131.8)); tr((157.0,131.8),(157.0,123.5),pcbnew.B_Cu); via((157.0,123.5)); tr((157.0,123.5),(132.5,123.5))
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
