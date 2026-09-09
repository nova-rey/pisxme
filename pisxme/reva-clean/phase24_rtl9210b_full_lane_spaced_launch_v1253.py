"""V1253: spaced B.Cu trunks with lateral J1-side transitions."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_LANE0_ALL_LOWER_LEFT_V1250.kicad_pcb';OUT=H/'PHASE24_RTL9210B_FULL_LANE_SPACED_LAUNCH_V1253.kicad_pcb';F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));j=b.FindFootprintByReference('J1')
R=[('LANE0_RXP',(95.0,72.4),(133.0,78.4),'43'),('LANE0_RXN',(93.2,72.0),(132.0,79.4),'41'),('LANE0_TXN',(92.2,72.6),(134.5,80.8),'47'),('LANE0_TXP',(90.8,76.8),(136.0,81.6),'49')]
for name,src,end,jpad in R:
 n=b.FindNet(name);s(b,n,B,[src,(src[0],end[1]),end]);v(b,n,end);dst=b.FindFootprintByReference('J1').FindPadByNumber(jpad).GetPosition();d=(pcbnew.ToMM(dst.x),pcbnew.ToMM(dst.y));s(b,n,F,[end,(end[0],d[1]),d])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
