"""V678: use F.Cu same-net collector joins after V676 source escapes."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_U139_U140_AROUND_V676.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_COLLECTORS_FCU_V678.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W)
 q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def rm(b,name,ends):
 for q in list(b.GetTracks()):
  if q.GetNetname()==name:
   a,z=q.GetStart(),q.GetEnd(); pts={(round(pcbnew.ToMM(a.x),3),round(pcbnew.ToMM(a.y),3)),(round(pcbnew.ToMM(z.x),3),round(pcbnew.ToMM(z.y),3))}
   if pts==set(ends): b.RemoveNative(q)
b=pcbnew.LoadBoard(str(BASE)); n3=b.FindNet('RTL_3V3'); n1=b.FindNet('RTL_1V1')
# Remove V676's disposable tails before replacing them with collector joins.
rm(b,'RTL_1V1',{(92.0,70.0),(90.0,70.0)})
rm(b,'RTL_1V1',{(90.0,70.0),(92.0,70.0)})
# Both source transitions remain on their validated separate vias. 3V3 joins
# the existing F.Cu trunk at (93,64); 1V1 joins its F.Cu collector at (88,68.8).
t(b,n3,F,(91.0,68.4),(91.0,66.0)); t(b,n3,F,(91.0,66.0),(93.0,64.0))
t(b,n1,F,(92.0,70.0),(90.0,70.0)); t(b,n1,F,(90.0,70.0),(88.0,68.8))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
