"""V659 disposable: add all RTL9210B rails on a dedicated In2 power field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; base=H/'PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_NATIVE_REFILLED.kicad_pcb'; out=H/'PHASE24_RTL9210B_V35_ALL_RAILS_IN2_PROBE.kicad_pcb'
F,B,I=pcbnew.F_Cu,pcbnew.B_Cu,pcbnew.In2_Cu; W=pcbnew.FromMM(.30)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z,w=W):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(float(w)) if isinstance(w,float) else w);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(base)); u=b.FindFootprintByReference('U1')
rails={'RTL_1V1':{'pads':['16','25','36','40','50','55','60','63'],'dest':(113.4,69.0)},'RTL_3V3':{'pads':['20','34','39','52'],'dest':(110.4,69.0)},'RTL_5V':{'pads':['17','33'],'dest':(116.4,69.0)}}
esc={'16':(103.0,67.2),'25':(97.0,65.0),'36':(92.8,67.2),'40':(92.8,69.2),'50':(92.8,73.8),'55':(96.0,75.0),'60':(98.0,75.0),'63':(99.2,75.0),'20':(100.4,64.8),'34':(93.0,65.0),'39':(92.8,68.4),'52':(94.8,75.0),'17':(103.0,66.8),'33':(95.2,65.0)}
for name,info in rails.items():
 n=b.FindNet(name); pts=[]
 for pn in info['pads']:
  a=u.FindPadByNumber(pn).GetPosition(); A=(a.x/1e6,a.y/1e6); e=esc[pn]
  tr(b,n,F,A,e); via(b,n,e); pts.append(e)
 d=info['dest']; dv=(d[0],d[1]+2.0); via(b,n,dv); tr(b,n,I,dv,d,.45)
 # Power-plane collector is intentionally broad and does not carry signals.
 for e in pts: tr(b,n,I,e,dv,.45)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
