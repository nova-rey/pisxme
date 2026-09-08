"""Final local XOUT corridor trial; keep both crystal lanes off XAVDDH."""
from pathlib import Path
import os
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/os.environ.get('PISXME_QFN_ESCAPE_BASE','PHASE24_DUAL_MODE_STORAGE_NC39_SUPPORT_COHORT.kicad_pcb')
OUT=R/os.environ.get('PISXME_QFN_ESCAPE_OUT','PHASE24_DUAL_MODE_STORAGE_NC39_QFN_ESCAPE_REPAIR_V3.kicad_pcb')
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def pad(b,r,n): return b.FindFootprintByReference(r).FindPadByNumber(str(n))
def clear(b,name):
 n=b.FindNet(name)
 for i in list(b.GetTracks()):
  if i.GetNetCode()==n.GetNetCode():b.RemoveNative(i)
 return n
def seg(b,n,a,z,layer=pcbnew.F_Cu):
 if a==z:return
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(layer);t.SetWidth(pcbnew.FromMM(.15));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.55));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
b=pcbnew.LoadBoard(str(BASE))
n=clear(b,'JMS_REXT');s=xy(pad(b,'U11',39));d=xy(pad(b,'R80',1));a=(145.5,135.6);v=(145.5,129.5);w=(147.5,129.5);seg(b,n,s,a);via(b,n,a);seg(b,n,a,v,pcbnew.B_Cu);seg(b,n,v,w,pcbnew.B_Cu);via(b,n,w);seg(b,n,w,d)
# XIN remains on the far-left lane. XOUT also exits left, but uses a distinct
# horizontal y lane; its B.Cu path therefore does not cross XAVDDH or XIN.
for name,up,yp,ex,y_lane,endx,approach in (
 ('XIN',50,1,137.4,129.8,147.0,(147.0,114.15)),
 ('XOUT',51,2,137.8,129.2,146.5,(146.5,115.85)),
):
 n=clear(b,name);s=xy(pad(b,'U11',up));d=xy(pad(b,'Y10',yp));v1=(ex,y_lane);v2=(endx,110.5 if name=='XIN' else 112.0)
 seg(b,n,s,(s[0],y_lane));seg(b,n,(s[0],y_lane),v1);via(b,n,v1)
 if name=='XIN':
  seg(b,n,v1,(130.0,129.8),pcbnew.B_Cu);seg(b,n,(130.0,129.8),(130.0,110.5),pcbnew.B_Cu);seg(b,n,(130.0,110.5),v2,pcbnew.B_Cu)
 else:
  seg(b,n,v1,(132.0,129.2),pcbnew.B_Cu);seg(b,n,(132.0,129.2),(132.0,112.0),pcbnew.B_Cu);seg(b,n,(132.0,112.0),v2,pcbnew.B_Cu)
 via(b,n,v2);seg(b,n,v2,approach);seg(b,n,approach,d)
b.Save(str(OUT));print(OUT)
