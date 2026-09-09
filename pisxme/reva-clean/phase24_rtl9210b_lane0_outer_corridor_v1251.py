"""V1251: adapt the known monotonic J1 launch corridors to V1250."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_LANE0_ALL_LOWER_LEFT_V1250.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_LANE0_OUTER_CORRIDOR_V1251.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));u=b.FindFootprintByReference('U1');j=b.FindFootprintByReference('J1')
R=[('LANE0_RXP','64',(95.0,72.4),(110.6,66.5),(132.0,66.5),'43'),('LANE0_RXN','65',(93.2,72.0),(111.5,64.5),(132.0,64.5),'41'),('LANE0_TXN','67',(92.2,72.6),(109.95,59.2),(None,None),'47'),('LANE0_TXP','68',(90.8,76.8),(108.0,58.8),(None,None),'49')]
for name,pad,src,mid,end,jpad in R:
 n=b.FindNet(name); s(b,n,B,[src,(src[0],mid[1]),mid]); v(b,n,mid)
 if end[0] is not None: s(b,n,B,[mid,end]); v(b,n,end); s(b,n,F,[end,(end[0],pcbnew.ToMM(j.FindPadByNumber(jpad).GetPosition().y)),(pcbnew.ToMM(j.FindPadByNumber(jpad).GetPosition().x),pcbnew.ToMM(j.FindPadByNumber(jpad).GetPosition().y))])
 else:
  s(b,n,F,[mid,(pcbnew.ToMM(j.FindPadByNumber(jpad).GetPosition().x),pcbnew.ToMM(j.FindPadByNumber(jpad).GetPosition().y))])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
