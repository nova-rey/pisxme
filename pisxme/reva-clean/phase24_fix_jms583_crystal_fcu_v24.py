"""V24: disposable all-F.Cu crystal escape, avoiding B.Cu SATA corridors."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_STORAGE_USB_TX_PAIR_UPPER_DETOUR_V13.kicad_pcb'
OUT=R/'PHASE24_STORAGE_JMS583_CRYSTAL_FCU_V24.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(b,r,n):
 q=b.FindFootprintByReference(r).FindPadByNumber(str(n)).GetPosition(); return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
def clear(b,n):
 for t in list(b.GetTracks()):
  if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
def route(b,name,up,crystal,pts):
 n=b.FindNet(name);clear(b,n); p=[xy(b,'U11',up)]+pts+[xy(b,'Y10',crystal)]
 for a,z in zip(p,p[1:]):
  t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(pcbnew.F_Cu);t.SetWidth(pcbnew.FromMM(.15));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
b=pcbnew.LoadBoard(str(BASE))
route(b,'XIN',50,1,[(135.0,131.4),(135.0,107.0),(147.0,107.0)])
route(b,'XOUT',51,2,[(133.0,131.4),(133.0,105.0),(145.0,105.0),(146.5,112.0)])
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
