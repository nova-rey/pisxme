"""V1356: REFCLK pair uses a left B.Cu transition and upper F.Cu corridor."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_PERST_LOWER_SHELF_V1355.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_REFCLK_LEFT_UPPER_V1356.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def v(b,n,p):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); p=b.FindNet('REFCLK_P'); n=b.FindNet('REFCLK_N'); assert p and n
for net,src,yb,xf,jx in [(p,(94.05,70.4),56.0,106.0,137.25),(n,(94.05,70.8),57.0,106.0,136.75)]:
 t(b,net,F,src,(90.0,src[1])); t(b,net,F,(90.0,src[1]),(90.0,yb)); v(b,net,(90.0,yb)); t(b,net,B,(90.0,yb),(xf,yb)); v(b,net,(xf,yb)); t(b,net,F,(xf,yb),(jx,yb)); t(b,net,F,(jx,yb),(jx,62.725))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
