"""V554: move RX source escapes to B.Cu and use the freed F.Cu field for 1V1."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_QFN_COALLOCATE_V546.kicad_pcb'; out=H/'PHASE24_RTL9210B_QFN_COALLOCATE_V554.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.13208)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,a):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*a));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());v.SetWidth(pcbnew.FromMM(.6));v.SetDrill(pcbnew.FromMM(.3));b.Add(v)
b=pcbnew.LoadBoard(str(src)); n1=b.FindNet('RTL_1V1')
np=b.FindNet('LANE0_RXP'); nn=b.FindNet('LANE0_RXN')
# Remove only the two F.Cu source-to-launch segments; downstream pair copper
# remains unchanged and is rejoined at its existing F.Cu endpoints.
for x in list(b.GetTracks()):
 a=x.GetStart();z=x.GetEnd();
 if x.GetNetname()=='LANE0_RXP' and ((a.x/1e6,a.y/1e6,z.x/1e6,z.y/1e6) in [(107.6,65.95,107.6,69.2),(107.6,69.2,113.0,69.2)] or (z.x/1e6,z.y/1e6,a.x/1e6,a.y/1e6) in [(107.6,65.95,107.6,69.2),(107.6,69.2,113.0,69.2)]): b.RemoveNative(x)
 if x.GetNetname()=='LANE0_RXN' and ((a.x/1e6,a.y/1e6,z.x/1e6,z.y/1e6) in [(108.0,65.95,108.0,68.3),(108.0,68.3,114.0,68.3)] or (z.x/1e6,z.y/1e6,a.x/1e6,a.y/1e6) in [(108.0,65.95,108.0,68.3),(108.0,68.3,114.0,68.3)]): b.RemoveNative(x)
# RX pair source escapes: short F.Cu dogbone, ordinary via, then B.Cu
# outboard of the proposed 1V1 collector, with F.Cu rejoin.
via(b,np,(107.6,66.8)); tr(b,np,F,(107.6,65.95),(107.6,66.8)); tr(b,np,B,(107.6,66.8),(110.0,66.8)); tr(b,np,B,(110.0,66.8),(110.0,69.2)); via(b,np,(110.0,69.2)); tr(b,np,F,(110.0,69.2),(113.0,69.2))
via(b,nn,(108.0,66.8)); tr(b,nn,F,(108.0,65.95),(108.0,66.8)); tr(b,nn,B,(108.0,66.8),(111.0,66.8)); tr(b,nn,B,(111.0,66.8),(111.0,68.3)); via(b,nn,(111.0,68.3)); tr(b,nn,F,(111.0,68.3),(114.0,68.3))
# Remaining bottom 1V1 group, with a B.Cu collector ending left of the RX
# source transitions and a new F.Cu handoff to the existing 1V1 trunk.
for a,z in [((104.0,65.95),(104.2,68.8)),((106.0,65.95),(105.8,68.8)),((107.2,65.95),(108.4,68.8))]: tr(b,n1,F,a,z);via(b,n1,z)
tr(b,n1,B,(104.2,68.8),(98.5,68.8));tr(b,n1,B,(105.8,68.8),(104.2,68.8));tr(b,n1,B,(108.4,68.8),(105.8,68.8));via(b,n1,(98.5,68.8));tr(b,n1,F,(98.5,68.8),(98.5,61.2));tr(b,n1,F,(98.5,61.2),(99.5,61.2))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
