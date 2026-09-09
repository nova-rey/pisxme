"""V930: clean-field discriminator for all RTL_1V1 package-pad escapes."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_V926_SPISI_REGEN_V927.kicad_pcb';OUT=H/'PHASE24_RTL9210B_V927_RTL1V1_CLEANFIELD_V930.kicad_pcb'
F=pcbnew.F_Cu;L=pcbnew.In2_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,a,z,l=F):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for t in list(b.GetTracks()):
 if t.GetNetname() in ('RTL_3V3','RTL_5V','RSET','XTAL_IN','XTAL_OUT','GND'):b.RemoveNative(t)
n=b.FindNet('RTL_1V1')
esc=[([(101.95,67.2),(102.8,67.2)],(102.8,67.2)),
 ([(94.05,67.2),(92.5,67.2)],(92.5,67.2)), ([(94.05,68.8),(92.5,68.8)],(92.5,68.8)),
 ([(94.05,72.8),(92.5,72.8)],(92.5,72.8)), ([(96,73.95),(96,75.5)],(96,75.5)),
 ([(98,73.95),(98,75.5)],(98,75.5)), ([(99.2,73.95),(99.2,77.0),(101.5,77.0)],(101.5,77.0))]
for pts,z in esc:
 for a,q in zip(pts,pts[1:]):tr(b,n,a,q)
 via(b,n,z)
z=pcbnew.ZONE(b);z.SetLayer(L);z.SetNet(n);z.SetNetCode(n.GetNetCode());z.SetPadConnection(pcbnew.ZONE_CONNECTION_THERMAL);z.SetLocalClearance(pcbnew.FromMM(.25));z.SetMinThickness(pcbnew.FromMM(.20));poly=pcbnew.SHAPE_POLY_SET();c=pcbnew.SHAPE_LINE_CHAIN()
for q in [(91.5,62),(103.5,62),(103.5,77),(91.5,77)]:c.Append(P(*q))
c.SetClosed(True);poly.AddOutline(c);z.SetOutline(poly);b.Add(z);b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
