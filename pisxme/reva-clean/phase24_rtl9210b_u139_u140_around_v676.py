"""V676: route U1.40 around the U1.39 source transition."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_RSET_INTERIOR_V672.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_U139_U140_AROUND_V676.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
# Remove the old U1.40 horizontal departure at its exact saved endpoints.
for q in list(b.GetTracks()):
 if q.GetNetname()=='RTL_1V1':
  a,z=q.GetStart(),q.GetEnd(); pts={(round(pcbnew.ToMM(a.x),3),round(pcbnew.ToMM(a.y),3)),(round(pcbnew.ToMM(z.x),3),round(pcbnew.ToMM(z.y),3))}
  if pts=={(94.05,68.8),(88.0,68.8)}: b.RemoveNative(q)
n3=b.FindNet('RTL_3V3'); n1=b.FindNet('RTL_1V1')
# U1.39 uses the west transition. U1.40 turns down before changing layer.
t(b,n3,F,(94.05,68.4),(91.0,68.4)); v(b,n3,(91.0,68.4))
t(b,n1,F,(94.05,68.8),(93.2,68.8)); t(b,n1,F,(93.2,68.8),(92.0,70.0)); v(b,n1,(92.0,70.0))
t(b,n1,B,(92.0,70.0),(90.0,70.0))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
