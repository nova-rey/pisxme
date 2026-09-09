"""V1306: add far-side PEDET/CLKREQ_N launches on the V862 basis."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_V860_5V_ADD_U133_V862.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_V862_FAR_CONTROLS_V1306.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def r(b,n,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def v(b,n,p):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); pe=b.FindNet('PEDET'); ck=b.FindNet('CLKREQ_N')
# PEDET: leave R2.1 to the west, then use a dedicated B.Cu spine and enter
# J1.69 from the connector's right edge.
r(b,pe,F,[(120.0,80.0),(118.0,80.0)]); v(b,pe,(118.0,80.0)); r(b,pe,B,[(118.0,80.0),(118.0,64.0),(143.5,64.0)]); v(b,pe,(143.5,64.0)); r(b,pe,F,[(143.5,64.0),(143.5,62.725),(140.75,62.725)])
# CLKREQ_N: remain on F.Cu and approach J1.52 from the right/upper side.
r(b,ck,F,[(120.0,75.0),(120.0,73.0),(123.0,73.0),(123.0,68.0),(138.5,68.0),(138.5,70.275),(136.5,70.275)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
