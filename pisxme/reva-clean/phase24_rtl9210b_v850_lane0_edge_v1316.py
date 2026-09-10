"""V1316: add RTL9210B lane-0 from the native-clean V850 edge field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_ROTATE_FLASH_270_SPI_CLEAN_CONTROLS_V850.kicad_pcb';OUT=H/'PHASE24_RTL9210B_V850_LANE0_EDGE_V1316.kicad_pcb';F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));u=b.FindFootprintByReference('U1');j=b.FindFootprintByReference('J1')
R=[('LANE0_RXP','64',68.4,106.0,130.0,'43'),('LANE0_RXN','65',68.0,107.0,131.0,'41'),('LANE0_TXN','67',67.2,108.5,132.0,'47'),('LANE0_TXP','68',66.8,110.0,133.0,'49')]
for name,pad,row,x0,x1,jp in R:
 n=b.FindNet(name);q=u.FindPadByNumber(pad).GetPosition();src=(pcbnew.ToMM(q.x),pcbnew.ToMM(q.y));d=j.FindPadByNumber(jp).GetPosition();dst=(pcbnew.ToMM(d.x),pcbnew.ToMM(d.y));s(b,n,F,[src,(x0,row)]);v(b,n,(x0,row));s(b,n,B,[(x0,row),(x1,row)]);v(b,n,(x1,row));s(b,n,F,[(x1,row),dst])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
