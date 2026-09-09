"""V1244: lane-0 source escape and outer B.Cu corridor from V1243."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_RAILS_REFCLK_FIXED_V1243.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_LANE0_FROM_V1243_V1244.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); u=b.FindFootprintByReference('U1'); j=b.FindFootprintByReference('J1')
# Each pair leaves the south edge in a dedicated F.Cu escape. The four
# outer B.Cu rows then launch monotonically to separate J1-side transitions.
routes=[('LANE0_RXP','64',(93.6,75.5),(134.25,82.0),'43'),('LANE0_RXN','65',(93.0,76.2),(133.75,83.0),'41'),('LANE0_TXN','67',(95.0,75.5),(135.25,84.0),'47'),('LANE0_TXP','68',(95.6,76.2),(135.75,85.0),'49')]
for name,padnum,escape,end,jpad in routes:
 n=b.FindNet(name); pp=u.FindPadByNumber(padnum).GetPosition(); src=(pcbnew.ToMM(pp.x),pcbnew.ToMM(pp.y)); ex=escape; dst=(pcbnew.ToMM(j.FindPadByNumber(jpad).GetPosition().x),pcbnew.ToMM(j.FindPadByNumber(jpad).GetPosition().y))
 seg(b,n,F,[src,(ex[0],src[1]),ex]); via(b,n,ex)
 seg(b,n,B,[ex,(end[0],ex[1])]); via(b,n,end)
 seg(b,n,F,[end,(dst[0],end[1]),dst])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
