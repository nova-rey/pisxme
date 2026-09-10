"""V1453: coherent R1 move plus local RTL_1V1 branch reallocation."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ACCEPTED_PRIMITIVES_V1428.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_RSET_REALLOCATE_1V1_V1453.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); r=next(f for f in b.GetFootprints() if f.GetReference()=='R1'); r.SetPosition(r.GetPosition()+P(-4,5))
for t in list(b.GetTracks()):
 if t.GetNetname()=='GND' and not isinstance(t,pcbnew.PCB_VIA):
  a,z=t.GetStart(),t.GetEnd()
  if (a==P(89.2,65.0) and z==P(89.2,67.0)) or (a==P(89.2,67.0) and z==P(89.2,65.0)): b.RemoveNative(t)
one=b.FindNet('RTL_1V1'); g=b.FindNet('GND'); n=b.FindNet('RSET'); assert one and g and n
for t in list(b.GetTracks()):
 if t.GetNetname()!='RTL_1V1' or isinstance(t,pcbnew.PCB_VIA): continue
 a,z=t.GetStart(),t.GetEnd()
 if (a==P(94.05,68.0) and z==P(92.0,68.0)) or (a==P(92.0,68.0) and z==P(94.05,68.0)) or (a==P(92.0,68.0) and z==P(92.0,64.0)) or (a==P(92.0,64.0) and z==P(92.0,68.0)) or (a==P(92.0,64.0) and z==P(97.8,63.6)) or (a==P(97.8,63.6) and z==P(92.0,64.0)): b.RemoveNative(t)
tr(b,one,F,(94.05,68.0),(96.0,68.0)); via(b,one,(96.0,68.0)); tr(b,one,B,(96.0,68.0),(102.0,68.0))
tr(b,g,F,(85.2,70.0),(85.2,68.0)); tr(b,g,F,(85.2,68.0),(89.2,67.0))
tr(b,n,F,(94.8,66.05),(84.0,66.05)); tr(b,n,F,(84.0,66.05),(84.0,70.0))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
