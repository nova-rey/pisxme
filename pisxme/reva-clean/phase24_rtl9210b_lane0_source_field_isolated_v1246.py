"""V1246: isolate the RTL9210B QFN source field and test lane-0 escapes."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_RAILS_REFCLK_FIXED_V1243.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_LANE0_SOURCE_FIELD_ISOLATED_V1246.kicad_pcb'; F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def inside(p): return 90<=pcbnew.ToMM(p.x)<=101 and 63<=pcbnew.ToMM(p.y)<=80
def seg(b,n,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,p):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for q in list(b.GetTracks()):
 if inside(q.GetStart()) or inside(q.GetEnd()): b.RemoveNative(q)
for q in list(b.GetTracks()):
 if type(q).__name__=='PCB_VIA' and inside(q.GetPosition()): b.RemoveNative(q)
u=b.FindFootprintByReference('U1')
for name,pad,ex in [('LANE0_RXP','64',(93.30,75.50)),('LANE0_RXN','65',(92.70,76.20)),('LANE0_TXN','67',(94.80,75.50)),('LANE0_TXP','68',(95.40,76.20))]:
 n=b.FindNet(name); p=u.FindPadByNumber(pad).GetPosition(); src=(pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)); seg(b,n,src,(ex[0],src[1])); seg(b,n,(ex[0],src[1]),ex); via(b,n,ex)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
