"""Disposable USB RX endpoint-via relocation around the SATA field."""
from pathlib import Path
import os
import pcbnew
R=Path(__file__).resolve().parent
base=R/os.environ.get("P24_USB_RX_BASE","PHASE24_STORAGE_SELECTOR_SATA_ESCAPE_V14.kicad_pcb")
out=R/os.environ.get("P24_USB_RX_OUT","PHASE24_STORAGE_USB_RX_VIA_RELOC_V2.kicad_pcb")
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def vi(n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.50));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
b=pcbnew.LoadBoard(str(base))
if b is None:raise SystemExit("load failure")
specs=(("USB_RXP1","U11","26","U12","23",(139.4,142.0),(153.0,137.8)),
       ("USB_RXN1","U11","27","U12","22",(139.0,143.0),(151.0,138.2)))
for name,sa,sp,da,dp,sv,dv in specs:
 n=b.FindNet(name)
 if n is None:raise SystemExit(f"missing {name}")
 for item in list(b.GetTracks()):
  if item.GetNetCode()==n.GetNetCode():b.RemoveNative(item)
 src=b.FindFootprintByReference(sa).FindPadByNumber(sp).GetPosition();dst=b.FindFootprintByReference(da).FindPadByNumber(dp).GetPosition()
 srcmm=(pcbnew.ToMM(src.x),pcbnew.ToMM(src.y));dstmm=(pcbnew.ToMM(dst.x),pcbnew.ToMM(dst.y))
 vi(n,sv);vi(n,dv);tr(n,F,srcmm,sv);tr(n,B,sv,dv);tr(n,F,dv,dstmm)
b.BuildListOfNets();b.Save(str(out));print(out)
