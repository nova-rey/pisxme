"""V938: monotonic XTAL_OUT handoff with the U1.55 1V1 departure scrubbed."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_V932_CRYSTAL_PAIR_REGEN_V937.kicad_pcb';OUT=H/'PHASE24_RTL9210B_V937_XTAL_OUT_U155_SCRUB_V938.kicad_pcb';F=pcbnew.F_Cu;B=pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n1=b.FindNet('RTL_1V1')
for x in list(b.GetTracks()):
 if x.GetNetname()=='XTAL_OUT':b.RemoveNative(x);continue
 if x.GetNetname()!='RTL_1V1':continue
 if type(x).__name__=='PCB_VIA' and x.GetPosition()==P(96,75.5):b.RemoveNative(x)
 elif type(x).__name__!='PCB_VIA' and (x.GetStart()==P(96,73.95) or x.GetEnd()==P(96,73.95) or x.GetStart()==P(96,75.5) or x.GetEnd()==P(96,75.5)):b.RemoveNative(x)
n=b.FindNet('XTAL_OUT');tr(b,n,[(95.6,73.95),(95.6,79.0)],F);via(b,n,(95.6,79.0));tr(b,n,[(95.6,79.0),(95.6,50.0),(91.0,50.0)],B);via(b,n,(91.0,50.0));tr(b,n,[(91.0,50.0),(91.0,54.0),(89.4,51.0)],F)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
