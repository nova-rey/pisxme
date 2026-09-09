"""V691: move the C2 GND stitch clear of the U1.52 corridor."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_3V3_U139_JOG_V687.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_C2_GND_U152_V691.kicad_pcb'
F=pcbnew.F_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(F);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,pcbnew.B_Cu);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n3=b.FindNet('RTL_3V3');ng=b.FindNet('GND')
for q in list(b.GetTracks()):
 if type(q).__name__=='PCB_VIA' and q.GetNetname()=='GND':
  p=q.GetPosition();xy=(round(pcbnew.ToMM(p.x),3),round(pcbnew.ToMM(p.y),3))
  if xy==(91.6,63.8):b.RemoveNative(q)
# Keep C2's pad-side return explicit and move its stitch east/up.
v(b,ng,(92.8,62.0));t(b,ng,(91.6,63.0),(92.8,62.0))
t(b,n3,(94.05,66.8),(92.0,66.8));t(b,n3,(92.0,66.8),(92.0,55.0));t(b,n3,(92.0,55.0),(103.0,55.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
