"""Move only the JMS_VCCO destination transition away from C86.1."""
from pathlib import Path
import os
import pcbnew
R = Path(__file__).resolve().parent
base = R / os.environ.get("P24_VCCO_DEST_BASE", "PHASE24_STORAGE_USB3_RIGHT_LAUNCH_V2.kicad_pcb")
out = R / os.environ.get("P24_VCCO_DEST_OUT", "PHASE24_STORAGE_VCCO_DEST_V1.kicad_pcb")
F, B = pcbnew.F_Cu, pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(n,l,a,z):
    t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l)
    t.SetWidth(pcbnew.FromMM(.20)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(n,q):
    v=pcbnew.PCB_VIA(b); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(.50)); v.SetDrill(pcbnew.FromMM(.30))
    v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
b=pcbnew.LoadBoard(str(base))
if b is None: raise SystemExit(f"cannot load {base}")
n=b.FindNet("JMS_VCCO")
if n is None: raise SystemExit("missing JMS_VCCO")
for item in list(b.GetTracks()):
    if item.GetNetCode()==n.GetNetCode(): b.RemoveNative(item)
tr(n,F,(136.35,134.0),(134.5,134.0)); via(n,(134.5,134.0))
tr(n,B,(134.5,134.0),(134.5,145.0)); tr(n,B,(134.5,145.0),(147.0,147.0)); via(n,(147.0,147.0))
tr(n,F,(147.0,147.0),(147.5,147.0))
b.BuildListOfNets(); b.Save(str(out)); print(out)
