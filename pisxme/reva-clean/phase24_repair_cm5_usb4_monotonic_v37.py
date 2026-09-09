"""V37: shift TXN away from the CM5_REFCLK transition via."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;BASE=R/'PHASE24_STORAGE_VBUS_LEFT_V32_FILLED.kicad_pcb';OUT=R/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V37.kicad_pcb'
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(b,r,n):
 q=b.FindFootprintByReference(r).FindPadByNumber(str(n)).GetPosition();return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
b=pcbnew.LoadBoard(str(BASE))
jobs=[('CM5_USB3_RX_N','128',67.5,(73,88)),('CM5_USB3_RX_P','130',68.8,(75,90)),('CM5_USB3_TX_N','140',70.5,(77,92)),('CM5_USB3_TX_P','142',74.5,(79,94))]
for name,padnum,lane,end in jobs:
 n=b.FindNet(name)
 for t in list(b.GetTracks()):
  if t.GetNetCode()!=n.GetNetCode() or isinstance(t,pcbnew.PCB_VIA):continue
  a=t.GetStart();z=t.GetEnd()
  if max(pcbnew.ToMM(a.x),pcbnew.ToMM(z.x))<100 and t.GetLayerName()=='F.Cu':b.RemoveNative(t)
 def seg(a,z):
  t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(pcbnew.F_Cu);t.SetWidth(pcbnew.FromMM(.15));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
 s=xy(b,'J7',padnum);seg(s,(lane,s[1]));seg((lane,s[1]),(lane,end[1]));seg((lane,end[1]),end)
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
