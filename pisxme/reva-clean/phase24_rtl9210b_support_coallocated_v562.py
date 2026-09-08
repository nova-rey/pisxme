"""V562: regenerate V368 1V1 allocation without duplicating V342 copper."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
base=H/'PHASE24_RTL9210B_RTL3V3_ROUTE_V342.kicad_pcb';out=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V562.kicad_pcb'
F,B,L=pcbnew.F_Cu,pcbnew.B_Cu,pcbnew.In2_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(base));n=b.FindNet('RTL_1V1')
esc=[((103.2,58.05),(103.2,56.8)),((102.05,61.6),(99.6,61.6)),((103.2,65.95),(103.2,67.2)),((103.2,67.2),(102,69)),((104.8,65.95),(104.8,67.8)),((104.8,67.8),(106,69)),((108.8,65.95),(108.8,69)),((109.95,64),(111.5,64)),((111.5,64),(111.5,63)),((109.95,62),(112,62)),((112,62),(112,61)),((109.95,60.8),(112,60.8)),((112,60.8),(112,59.5)),((113.2,53),(113.2,52)),((113.2,52),(115.5,52))]
for a,z in esc:s(b,n,F,a,z)
for q in [(103.2,56.8),(99.6,61.6),(102,69),(106,69),(108.8,69),(111.5,63),(112,61),(112,59.5),(115.5,52)]:v(b,n,q)
for a,z in [((103.2,56.8),(100,56.8)),((100,56.8),(100,51.5)),((100,51.5),(115.5,51.5)),((99.6,61.6),(97.5,61.6)),((97.5,61.6),(97.5,75)),((97.5,75),(114.8,75)),((102,69),(102,75)),((106,69),(106,75)),((108.8,69),(108.8,75)),((111.5,63),(114.8,63)),((112,61),(114.8,61)),((112,59.5),(114.8,59.5)),((114.8,59.5),(114.8,75)),((115.5,52),(115.5,75))]:s(b,n,B if a in [(103.2,56.8),(100,56.8),(99.6,61.6),(97.5,61.6)] else L,a,z)
z=pcbnew.ZONE(b);z.SetLayer(L);z.SetNet(n);z.SetNetCode(n.GetNetCode());z.SetPadConnection(pcbnew.ZONE_CONNECTION_THERMAL);z.SetLocalClearance(pcbnew.FromMM(.25));z.SetMinThickness(pcbnew.FromMM(.20));poly=pcbnew.SHAPE_POLY_SET();c=pcbnew.SHAPE_LINE_CHAIN()
for q in [(97,50),(116,50),(116,71),(97,71)]:c.Append(P(*q))
c.SetClosed(True);poly.AddOutline(c);z.SetOutline(poly);b.Add(z)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
