"""V1252: four independent B.Cu trunks from the clean V1250 source field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_LANE0_ALL_LOWER_LEFT_V1250.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_FULL_LANE_BCU_ROWS_V1252.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));j=b.FindFootprintByReference('J1')
R=[('LANE0_RXP',(95.0,72.4),(78.8,132.0),'43'),('LANE0_RXN',(93.2,72.0),(79.2,132.5),'41'),('LANE0_TXN',(92.2,72.6),(80.8,133.0),'47'),('LANE0_TXP',(90.8,76.8),(81.2,133.5),'49')]
for name,src,(row,jx),jpad in R:
 n=b.FindNet(name);s(b,n,B,[src,(src[0],row),(jx,row)]);v(b,n,(jx,row)); dst=(pcbnew.ToMM(j.FindPadByNumber(jpad).GetPosition().x),pcbnew.ToMM(j.FindPadByNumber(jpad).GetPosition().y));s(b,n,F,[(jx,row),(dst[0],row),dst])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
