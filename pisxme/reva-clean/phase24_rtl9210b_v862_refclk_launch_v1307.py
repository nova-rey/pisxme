"""V1307: add a crossed-layer REFCLK launch on the V862 basis."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_V862_FAR_CONTROLS_V1306.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_V862_REFCLK_LAUNCH_V1307.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def r(b,n,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def v(b,n,p):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); p=b.FindNet('REFCLK_P'); n=b.FindNet('REFCLK_N')
r(b,p,F,[(98.4,73.95),(98.4,76.0),(130.0,76.0),(130.0,64.0)]); v(b,p,(130.0,64.0)); r(b,p,B,[(130.0,64.0),(137.25,64.0)]); v(b,p,(137.25,64.0)); r(b,p,F,[(137.25,64.0),(137.25,62.725)])
r(b,n,F,[(98.8,73.95),(98.8,77.0),(136.75,77.0),(136.75,62.725)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
