"""V660 disposable: relocated rail endpoints with separate In2 collectors."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; base=H/'PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_NATIVE_REFILLED.kicad_pcb'; out=H/'PHASE24_RTL9210B_V35_RELOCATED_RAIL_ENDPOINTS_PROBE.kicad_pcb'
F,B,I=pcbnew.F_Cu,pcbnew.B_Cu,pcbnew.In2_Cu; W=pcbnew.FromMM(.30)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z,w=W):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(float(w)) if isinstance(w,float) else w);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(base)); u=b.FindFootprintByReference('U1')
for ref,xy in [('C3',(122,88)),('C4',(126,88)),('C5',(130,88))]: b.FindFootprintByReference(ref).SetPosition(P(*xy))
groups={'RTL_1V1':(['16','25','36','40','50','55','60','63'],(126,88),[(103,65),(97,64.5),(92.5,67.2),(92.5,69.2),(92.5,73.8),(96,75.5),(98,75.5),(99.2,75.5)],85.0),'RTL_3V3':(['20','34','39','52'],(122,88),[(100.4,64.5),(93.0,64.5),(92.5,68.4),(94.8,75.5)],87.0),'RTL_5V':(['17','33'],(130,88),[(103.0,66.8),(95.2,64.5)],89.0)}
for name,(pads,dest,esc,y) in groups.items():
 n=b.FindNet(name); dv=(dest[0],dest[1]+2.0); via(b,n,dv); tr(b,n,I,dv,dest,.45)
 for pn,e in zip(pads,esc):
  a=u.FindPadByNumber(pn).GetPosition(); A=(a.x/1e6,a.y/1e6); tr(b,n,F,A,e); via(b,n,e); tr(b,n,I,e,(e[0],y),.45); tr(b,n,I,(e[0],y),dv,.45)
 # external pull-up rail pads are included in the same physical collector
 if name=='RTL_3V3':
  for e in [(90.2,54.5),(93.2,54.5)]: via(b,n,e); tr(b,n,I,e,dv,.45)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
