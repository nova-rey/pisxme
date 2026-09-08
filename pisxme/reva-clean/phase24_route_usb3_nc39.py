"""Disposable USB3 regeneration on the corrected NC39/support basis."""
from pathlib import Path
import os
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/os.environ.get('PISXME_USB3_REGEN_BASE','PHASE24_DUAL_MODE_STORAGE_NC39_QFN_ESCAPE_REPAIR_V3.kicad_pcb');OUT=R/os.environ.get('PISXME_USB3_REGEN_OUT','PHASE24_DUAL_MODE_STORAGE_NC39_USB3_REGEN.kicad_pcb')
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p):return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def pad(b,r,n):return b.FindFootprintByReference(r).FindPadByNumber(str(n))
def seg(b,n,a,z,layer=pcbnew.F_Cu,w=.147):
 if a==z:return
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(layer);t.SetWidth(pcbnew.FromMM(w));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.55));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
b=pcbnew.LoadBoard(str(BASE))
routes=[
 ('CM5_USB3_RX_N','128','16',73.0,88.0,145.0),
 ('CM5_USB3_RX_P','130','15',75.0,90.0,147.0),
 ('CM5_USB3_TX_N','140','12',77.0,92.0,149.0),
 ('CM5_USB3_TX_P','142','11',79.0,94.0,151.0),
]
for name,jp,up,xsrc,ylane,xend in routes:
 n=b.FindNet(name) or b.FindNet('/CORE_CM5/'+name)
 if n is None: raise RuntimeError('missing USB3 net '+name)
 for i in list(b.GetTracks()):
  if i.GetNetname() in (name,'/CORE_CM5/'+name):b.RemoveNative(i)
 s=xy(pad(b,'J7',jp));d=xy(pad(b,'U12',up));sv=(xsrc,s[1]);v1=(xsrc,ylane);v2=(xend,ylane);ev=(xend,d[1])
 seg(b,n,s,sv);seg(b,n,sv,v1);via(b,n,v1);seg(b,n,v1,v2,pcbnew.B_Cu);via(b,n,v2);seg(b,n,v2,ev,pcbnew.B_Cu);via(b,n,ev);seg(b,n,ev,d)
b.Save(str(OUT));print(OUT)
