"""V23: separated ordinary XIN/XOUT crystal transition vias."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_STORAGE_USB_TX_PAIR_UPPER_DETOUR_V13.kicad_pcb'
OUT=R/'PHASE24_STORAGE_JMS583_CRYSTAL_VIAS_V23.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(b,r,n):
 q=b.FindFootprintByReference(r).FindPadByNumber(str(n)).GetPosition(); return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
def seg(b,n,a,z,l,w=.15):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(w));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.55));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
def clear(b,n):
 for t in list(b.GetTracks()):
  if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
def route(b,name,up,crystal,low,mid,high):
 n=b.FindNet(name);clear(b,n);s=xy(b,'U11',up);d=xy(b,'Y10',crystal)
 seg(b,n,s,low,pcbnew.F_Cu);via(b,n,low);seg(b,n,low,mid,pcbnew.B_Cu);seg(b,n,mid,high,pcbnew.B_Cu);via(b,n,high);seg(b,n,high,d,pcbnew.F_Cu)
b=pcbnew.LoadBoard(str(BASE))
route(b,'XIN',50,1,(137.4,129.8),(130.0,129.8),(147.0,110.5))
route(b,'XOUT',51,2,(139.5,129.2),(132.0,129.2),(146.5,112.0))
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
