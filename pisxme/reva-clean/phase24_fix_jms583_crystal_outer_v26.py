"""V26: orthogonal QFN departures before separated outer crystal corridors."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;BASE=R/'PHASE24_STORAGE_USB_TX_PAIR_UPPER_DETOUR_V13.kicad_pcb';OUT=R/'PHASE24_STORAGE_JMS583_CRYSTAL_OUTER_V26.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(b,r,n):
 q=b.FindFootprintByReference(r).FindPadByNumber(str(n)).GetPosition();return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
def clear(b,n):
 for t in list(b.GetTracks()):
  if t.GetNetCode()==n.GetNetCode():b.RemoveNative(t)
def seg(b,n,a,z,l):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.15));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.55));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
def route(b,name,up,crystal,src,low,high,outer):
 n=b.FindNet(name);clear(b,n);d=xy(b,'Y10',crystal)
 seg(b,n,xy(b,'U11',up),src,pcbnew.F_Cu);seg(b,n,src,low,pcbnew.F_Cu);via(b,n,low)
 seg(b,n,low,(low[0],106.0),pcbnew.B_Cu);seg(b,n,(low[0],106.0),high,pcbnew.B_Cu);via(b,n,high)
 for a,z in zip([high]+outer+[d],outer+[d]):seg(b,n,a,z,pcbnew.F_Cu)
b=pcbnew.LoadBoard(str(BASE))
route(b,'XIN',50,1,(137.4,128.0),(128.0,128.0),(151.0,106.0),[(151.0,112.0)])
route(b,'XOUT',51,2,(137.8,127.2),(125.0,127.2),(146.0,106.0),[(146.0,115.85)])
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
