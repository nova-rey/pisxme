"""V982: orientation-0 source exits with spread ordinary through-vias only."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_ORIENTATION0_SOURCE_ESCAPE_V981.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_ORIENTATION0_SOURCE_VIA_PROBE_V982.kicad_pcb'; F=pcbnew.F_Cu; B=pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
# Each via is separated by >=0.8 mm and is outside the QFN body.  The short
# dogbones are the only added copper in this discriminator.
routes={
 'SPISI':([(101.95,73.2),(103.8,73.2),(104.5,74.5)],(104.5,74.5)),
 'SPICLK':([(101.95,72.8),(103.8,72.8),(103.5,72.0)],(103.5,72.0)),
 'SPISO3':([(101.95,71.6),(103.8,71.6),(105.5,70.5)],(105.5,70.5)),
 'SPISO':([(101.95,71.2),(103.8,71.2),(104.5,69.0)],(104.5,69.0)),
 'SPICS':([(101.95,70.8),(103.8,70.8),(103.5,68.0)],(103.5,68.0)),
}
for name,(pts,v) in routes.items():
 n=b.FindNet(name); tr(b,n,pts,F); via(b,n,v)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
