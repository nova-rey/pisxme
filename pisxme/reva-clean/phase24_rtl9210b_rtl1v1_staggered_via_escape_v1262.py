"""V1262: staggered individual RTL_1V1 QFN escapes on the V1258 lane base."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_J1_PAD_ALIGNED_LAUNCH_V1258.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_RTL1V1_STAGGERED_VIA_ESCAPE_V1262.kicad_pcb'
F,B,W=pcbnew.F_Cu,pcbnew.B_Cu,pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_1V1')
for q in list(b.GetTracks()):
 if q.GetNetname()=='RTL_1V1': b.Remove(q)
# Small, deliberately separated source cohort: three left-edge pads and one right-edge pad.
esc=[((94.05,68.0),(92.6,68.0)),((94.05,70.0),(92.0,69.6)),((94.05,71.2),(91.4,71.2)),((101.95,70.4),(103.0,70.4))]
for src,via_p in esc:
 s(b,n,F,[src,via_p]);v(b,n,via_p)
for _,p in esc:
 s(b,n,B,[p,(90.0,p[1])])
s(b,n,B,[(90.0,68.0),(90.0,60.0),(103.0,60.0),(103.0,50.0),(123.4,50.0)])
v(b,n,(103.0,60.0));v(b,n,(123.4,50.0));s(b,n,F,[(123.4,50.0),(123.4,51.0)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
