"""V1258: align final transition vias with native J1 pad x coordinates."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_LANE0_PER_PAIR_ASCENT_V1256.kicad_pcb';OUT=H/'PHASE24_RTL9210B_J1_PAD_ALIGNED_LAUNCH_V1258.kicad_pcb';F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));j=b.FindFootprintByReference('J1')
R=[('LANE0_RXP',(128,42),(130,42),(134.25,68.0),'43'),('LANE0_RXN',(128,43),(131,43),(132.75,65.0),'41'),('LANE0_TXN',(128,44),(132,44),(135.25,64.0),'47'),('LANE0_TXP',(128,45),(133,45),(135.75,61.0),'49')]
for name,row_end,sw,ep,jpad in R:
 n=b.FindNet(name);s(b,n,B,[row_end,sw]);v(b,n,sw);s(b,n,F,[sw,(sw[0],ep[1])]);v(b,n,(sw[0],ep[1]));s(b,n,B,[(sw[0],ep[1]),ep]);v(b,n,ep);d=j.FindPadByNumber(jpad).GetPosition();dst=(pcbnew.ToMM(d.x),pcbnew.ToMM(d.y));s(b,n,F,[ep,(ep[0],dst[1]),dst])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
