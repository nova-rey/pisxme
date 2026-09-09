"""Disposable all-F.Cu JMS_VCCO route to remove the source via conflict."""
from pathlib import Path
import os
import pcbnew
R=Path(__file__).resolve().parent
base=R/os.environ.get("P24_VCCO_F_BASE","PHASE24_STORAGE_VCCO_DEST_V1.kicad_pcb")
out=R/os.environ.get("P24_VCCO_F_OUT","PHASE24_STORAGE_VCCO_ALL_FCU_V1.kicad_pcb")
F=pcbnew.F_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(n,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(F);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
b=pcbnew.LoadBoard(str(base));n=b.FindNet("JMS_VCCO")
if b is None or n is None: raise SystemExit("load/net failure")
for item in list(b.GetTracks()):
 if item.GetNetCode()==n.GetNetCode(): b.RemoveNative(item)
pts=((136.35,134.0),(130.0,134.0),(130.0,150.0),(147.5,150.0),(147.5,147.0))
for a,z in zip(pts,pts[1:]):tr(n,a,z)
b.BuildListOfNets();b.Save(str(out));print(out)
