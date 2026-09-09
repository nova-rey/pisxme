"""V954: test source-field escapes with U1 rotated 180 degrees."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_U1_ORIENTATION_180_V953.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_U1_ORIENTATION180_SPI_SOURCE_V954.kicad_pcb'; F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts):
    for a,z in zip(pts,pts[1:]):
        q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
    q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE));
for name,src,esc in [('SPISI',(94.05,66.8),(92.0,66.8)),('SPICLK',(94.05,67.2),(91.0,67.2)),('SPISO3',(94.05,68.4),(90.0,68.4)),('SPISO',(94.05,68.8),(89.0,68.8))]:
    n=b.FindNet(name); tr(b,n,[src,esc]); via(b,n,esc)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
