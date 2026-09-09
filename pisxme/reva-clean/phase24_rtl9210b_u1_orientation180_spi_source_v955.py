"""V955: staggered U1-180 SPI source escapes."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_U1_ORIENTATION_180_V953.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_U1_ORIENTATION180_SPI_SOURCE_V955.kicad_pcb'; F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts):
    for a,z in zip(pts,pts[1:]):
        q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
    q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for name,src,mid,esc in [('SPISI',(94.05,66.8),(93.0,65.5),(92.0,65.5)),('SPICLK',(94.05,67.2),(93.0,67.5),(91.0,67.5)),('SPISO3',(94.05,68.4),(93.0,69.5),(90.0,69.5)),('SPISO',(94.05,68.8),(93.0,71.5),(89.0,71.5))]:
    n=b.FindNet(name); tr(b,n,[src,mid,esc]); via(b,n,esc)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
