"""Disposable USB3 pair-skew tuning from the current native workbench."""
from pathlib import Path
import os
import pcbnew
R=Path(__file__).resolve().parent
base=R/os.environ.get("P24_USB_TUNE_BASE","PHASE24_STORAGE_VCCK_LOCAL_V1.kicad_pcb")
out=R/os.environ.get("P24_USB_TUNE_OUT","PHASE24_STORAGE_USB3_SKEW_TUNE_V1.kicad_pcb")
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def vi(n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.50));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
b=pcbnew.LoadBoard(str(base))
if b is None:raise SystemExit("load failure")
# Tune only the shorter members; the endpoint positions and layer contract are
# unchanged.  RXP receives a small B.Cu dogleg; TXP receives a small F.Cu
# meander between its existing native endpoints.
for name in ("USB_RXP1","USB_TXP1"):
 n=b.FindNet(name)
 if n is None:raise SystemExit(f"missing {name}")
 for item in list(b.GetTracks()):
  if item.GetNetCode()==n.GetNetCode():b.RemoveNative(item)
# USB_RXP1 U11.26 -> U12.23
n=b.FindNet("USB_RXP1"); vi(n,(139.4,142.0)); vi(n,(159.0,137.8))
tr(n,F,(139.4,138.6),(139.4,142.0))
for a,z in zip(((139.4,142.0),(145.0,145.0),(152.0,145.0),(159.0,137.8)),((145.0,145.0),(152.0,145.0),(159.0,137.8))):tr(n,B,a,z)
tr(n,F,(159.0,137.8),(156.5,137.8))
# USB_TXP1 U11.21 -> C86.1
n=b.FindNet("USB_TXP1");tr(n,F,(141.4,138.6),(141.4,144.0));tr(n,F,(141.4,144.0),(144.0,144.0));tr(n,F,(144.0,144.0),(144.0,146.0));tr(n,F,(144.0,146.0),(146.5,146.0));tr(n,F,(146.5,146.0),(146.5,145.0))
b.BuildListOfNets();b.Save(str(out));print(out)
