"""Disposable V35 RTL_1V1 lower-field fanout probe."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
base=H/'PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_RTL5V_PROBE_V4.kicad_pcb'
out=H/'PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_RTL1V1_PROBE.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(p(*a));q.SetEnd(p(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(p(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(base));n=b.FindNet('RTL_1V1')
for src,esc,drop in [((94.05,67.20),(92.0,67.20),(92.0,84.0)),((94.05,68.80),(91.0,68.80),(91.0,84.0)),((94.05,72.80),(90.0,72.80),(90.0,84.0)),((96.0,73.95),(96.0,78.5),(96.0,84.0)),((98.0,73.95),(98.0,79.0),(98.0,84.0)),((99.2,73.95),(99.2,79.5),(99.2,84.0))]:
 s(b,n,F,src,esc);v(b,n,esc);s(b,n,F,esc,drop);v(b,n,drop)
s(b,n,B,(90.0,84.0),(114.5,84.0));v(b,n,(114.5,84.0));s(b,n,F,(114.5,84.0),(114.5,69.0));s(b,n,F,(114.5,69.0),(113.4,69.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
