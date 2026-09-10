"""V1595: deterministic monotonic handoff-to-J1 launch experiment."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_QFN_ESCAPE_HANDOFF_V1590.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_MANUAL_J1_MONOTONIC_V1595.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(V(*a));q.SetEnd(V(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(V(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
routes=(
 ('REFCLK_P',70.4,59.2,82.0,137.25),
 ('REFCLK_N',70.8,61.0,84.0,136.75),
 ('LANE0_RXP',71.6,65.0,86.0,134.25),
 ('LANE0_RXN',72.0,65.8,88.0,133.75),
 ('LANE0_TXN',72.8,66.6,90.0,135.25),
 ('LANE0_TXP',73.2,68.0,92.0,135.75),
)
for name,yh,yc,xh,xt in routes:
 n=b.FindNet(name); assert n
 tr(b,n,F,(85.,yh),(xh,yc)); via(b,n,(xh,yc))
 tr(b,n,B,(xh,yc),(xt,yc)); via(b,n,(xt,yc))
 tr(b,n,F,(xt,yc),(xt,62.725))
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
