"""V856: straight rightward PERST_N escape from the U1 side pad."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V772_CONTROL_INBOARD_MONOTONIC_V837.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_V772_PERST_STRAIGHT_RIGHT_V856.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,x,y):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(x,y)); q.SetWidth(pcbnew.FromMM(.6)); q.SetDrill(pcbnew.FromMM(.3)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('PERST_N')
tr(b,n,F,[(101.95,68.0),(108.5,68.0)])
via(b,n,108.5,68.0)
tr(b,n,B,[(108.5,68.0),(108.5,84.0),(135.0,84.0),(135.0,70.275)])
via(b,n,135.0,70.275); tr(b,n,F,[(135.0,70.275),(136.0,70.275)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
