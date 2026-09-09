"""V840: PERST_N transition beyond the occupied SPI-via columns."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V772_CONTROL_INBOARD_MONOTONIC_V837.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_V772_PERST_OUTER_TRANSITION_V840.kicad_pcb'
F=pcbnew.F_Cu; B=pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def T(b,n,l,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def V(b,n,p):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.6)); q.SetDrill(pcbnew.FromMM(.3)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('PERST_N')
T(b,n,F,[(101.95,68.0),(104,66.5),(108.5,64.5)]); V(b,n,(108.5,64.5)); T(b,n,B,[(108.5,64.5),(108.5,84),(135,84),(135,70.275)]); V(b,n,(135,70.275)); T(b,n,F,[(135,70.275),(136,70.275)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
