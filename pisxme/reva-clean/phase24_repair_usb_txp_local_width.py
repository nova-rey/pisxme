"""Disposable USB_TXP local escape at the active 0.20 mm rule."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;b=pcbnew.LoadBoard(str(R/'PHASE24_STORAGE_J8_V5_VBUS_V1.kicad_pcb'));F=pcbnew.F_Cu
def V(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(r,n):
 p=b.FindFootprintByReference(r).FindPadByNumber(str(n)).GetPosition();return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def tr(n,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(F);t.SetWidth(pcbnew.FromMM(.2));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
n=b.FindNet('USB_TXP1')
for t in list(b.GetTracks()):
 if t.GetNetCode()==n.GetNetCode():b.RemoveNative(t)
tr(n,xy('U11',21),(141.4,139.4));tr(n,(141.4,139.4),(140.4,140.4));tr(n,(140.4,140.4),(140.4,144.0));tr(n,(140.4,144.0),(146.5,144.0));tr(n,(146.5,144.0),xy('C86',1))
b.BuildListOfNets();out=R/'PHASE24_STORAGE_J8_V5_USB_TXP_WIDTH_V1.kicad_pcb';b.Save(str(out));print(out)
