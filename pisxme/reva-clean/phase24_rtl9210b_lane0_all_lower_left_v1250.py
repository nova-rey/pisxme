"""V1250: route all lower QFN lane pads away from the side-pad field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_RAILS_REFCLK_FIXED_V1243.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_LANE0_ALL_LOWER_LEFT_V1250.kicad_pcb'; F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def inside(p): return 90<=pcbnew.ToMM(p.x)<=104 and 63<=pcbnew.ToMM(p.y)<=80
def s(b,n,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(F);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for q in list(b.GetTracks()):
 if inside(q.GetStart()) or inside(q.GetEnd()): b.RemoveNative(q)
for q in list(b.GetTracks()):
 if type(q).__name__=='PCB_VIA' and inside(q.GetPosition()): b.RemoveNative(q)
u=b.FindFootprintByReference('U1')
R=[('LANE0_RXP','64',[(94.05,71.6),(95.0,71.6),(95.0,72.4)],(95.0,72.4)),('LANE0_RXN','65',[(94.05,72.0),(93.2,72.0)],(93.2,72.0)),('LANE0_TXN','67',[(94.05,72.8),(92.2,72.8),(92.2,72.6)],(92.2,72.6)),('LANE0_TXP','68',[(94.05,73.2),(90.8,73.2),(90.8,76.8)],(90.8,76.8))]
for n,p,ps,vp in R: s(b,b.FindNet(n),ps);v(b,b.FindNet(n),vp)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
