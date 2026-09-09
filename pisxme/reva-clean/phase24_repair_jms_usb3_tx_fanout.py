"""Disposable outboard F.Cu JMS USB3 TX fanout around U12."""
from pathlib import Path
import os
import pcbnew
R=Path(__file__).resolve().parent
base=R/os.environ.get("P24_JMS_TX_BASE","PHASE24_STORAGE_VCCK_LOCAL_V1.kicad_pcb")
out=R/os.environ.get("P24_JMS_TX_OUT","PHASE24_STORAGE_JMS_USB3_TX_FANOUT_V1.kicad_pcb")
F=pcbnew.F_Cu
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(n,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(F);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
b=pcbnew.LoadBoard(str(base))
if b is None: raise SystemExit("load failure")
for name,src,dst,x in (("JMS_USB3_TXP",(147.5,145.0),(156.5,137.0),165.0),
                       ("JMS_USB3_TXN",(147.5,149.0),(156.5,137.4),167.0)):
 n=b.FindNet(name)
 if n is None: raise SystemExit(f"missing {name}")
 for item in list(b.GetTracks()):
  if item.GetNetCode()==n.GetNetCode():b.RemoveNative(item)
 tr(n,src,(x,src[1]));tr(n,(x,src[1]),(x,dst[1]));tr(n,(x,dst[1]),dst)
b.BuildListOfNets();b.Save(str(out));print(out)
